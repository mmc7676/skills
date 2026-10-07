# skills

Personal agent skills by [mmc7676](https://github.com/mmc7676), written in the open [Agent Skills](https://agentskills.io) format (a folder with a `SKILL.md`), so they are not tied to one product. Claude, Codex and many other agents and clients read the same format; see [Other agents and clients](#other-agents-and-clients). Each skill is a self-contained folder (`SKILL.md`, a `README.md`, and its own `LICENSE`) that works on its own, and each also ships as a ready-to-import zip in [`dist/`](dist/).

> More skills are queued for upload. These are the first.

## Skills

| Skill | What it does | Contents | Folder | Zip |
|---|---|---|---|---|
| `effort-optimizer` | Always-on skill that matches reasoning and verification effort to a task's real stakes: fast on mechanical, reversible steps; slow and directly verified on anything touching auth, security, production, or a claim the user will act on unchecked. Reports "verified directly" and "plausible but untested" as different things. | `SKILL.md`, `README.md`, `LICENSE` | [effort-optimizer/](effort-optimizer/) | [zip](dist/effort-optimizer.zip) |
| `supersystem-integrate` | Generative engineering skill: discover the intent and feasibility of a new model, protocol, idea or capability, integrate it modularly into an existing system, validate it, and ship the finished artifact. Its Maxey0/SuperSpace passages are examples from the author's runtime; the loop works for any codebase. | `SKILL.md`, `README.md`, `LICENSE` | [supersystem-integrate/](supersystem-integrate/) | [zip](dist/supersystem-integrate.zip) |
| `linktree-search` | The LINKTREE method: deterministic, level-preserving URL crawling and indexing. A root URL goes in; a tree, a normalized graph and an outline come out. Sitemap-first, same-origin, robots-aware, polite and bounded by default. A specification package: it contains no crawler code. | `SKILL.md`, `references/` (5 files), `agents/openai.yaml` (used by Codex-style runtimes, ignored by Claude), `README.md`, `LICENSE` | [linktree-search/](linktree-search/) | [zip](dist/linktree-search.zip) |

## How effort-optimizer works with each skill

`effort-optimizer` sets how hard each step of another skill is pushed, by stakes and reversibility rather than by how big the task sounds. It does not grant permission for anything, and it does not replace another skill's own rules. Nothing here depends on a particular model.

- **FAST lane** (mechanical, reversible, already checked): batch independent steps, run them in parallel, move on.
- **SLOW lane** (touches auth, security or production, or a claim you will act on unchecked): one change at a time, verified directly before the next.
- **Report:** "verified directly" and "plausible but untested" are stated as different things.

The lane mappings below are the default when you give no explicit effort signal. An effort signal you type yourself (for example "quick pass") overrides them, as `effort-optimizer` Step 1 says; it does not change what the other skill itself requires.

**With `supersystem-integrate`.** Its loop (discover, model, bound, design, integrate, implement, validate, package, verify) can run at two speeds.
- FAST: reading the existing source, listing files, scaffolding, formatting.
- SLOW: validation, secret scanning, archive and checksum checks (including re-checking any regenerated file), and anything outward-facing (push, deploy, publish). Each is checked directly before the next step.
- `supersystem-integrate` has its own consent boundary and requires your confirmation before push, deploy, publish and similar steps. `effort-optimizer` classifies those steps as SLOW and verifies them directly, but it does not authorize them or ask for confirmation itself.
- Its rule to never claim completion, tests, files, API behavior or execution results that did not occur is closely related to effort-optimizer's split between verified and untested claims. Applied together, a ship report states what was checked directly and what was not.
- Where `supersystem-integrate` says to ask only when no defensible assumption exists, `effort-optimizer` Step 2 adds that a cheap fact should be checked directly before it is asserted.

**With `linktree-search`.** A crawl is bounded and compliance-sensitive, so the two lanes map cleanly.
- FAST: lowercasing hosts, stripping fragments, normalizing slashes, tree and graph assembly, schema and output-field checks, and running tests once a crawler exists.
- SLOW: redacting secrets from query strings (test sample URLs that carry token parameters and confirm they come out redacted), URL and address validation, and anything that widens scope or weakens a protection. Check `robots.txt` and the sitemap directly instead of assuming them.
- Verification is not permission: weakening robots, origin or address protections still needs the operator's explicit instruction for a host they own or are authorized to crawl, as the skill itself requires.
- Coverage claims: "verified directly" applies to pages that were actually fetched. A page only listed in a sitemap is "listed, not fetched".

**With `scw-default-deployer`** (lives in Maxey0). A suggested pairing, not a built-in dependency. The deployer creates a bounded context window before a task runs. Use effort-optimizer to set how much verification happens inside it: mechanical child tasks run FAST, while admission, gate and provenance steps take the SLOW lane.

## Related skill that lives elsewhere

- `scw-default-deployer` is part of the Maxey0 runtime and is maintained there, so it is not duplicated here: [Maxey0/skills/scw-default-deployer](https://github.com/mmc7676/Maxey0/tree/main/skills/scw-default-deployer). It expects the Maxey0 gates and MCP surfaces.

See also [Maxey0](https://github.com/mmc7676/Maxey0) (the runtime and its core skills) and [logical-scws](https://github.com/mmc7676/logical-scws) (the Logical SCWs paper and dashboard).

## Install

**Claude Code plugin marketplace (easiest):** this repo is also a plugin marketplace, so you can install by name and update with a command.

```bash
claude plugin marketplace add mmc7676/skills
claude plugin install effort-optimizer@mmc7676-skills
claude plugin install supersystem-integrate@mmc7676-skills
claude plugin install linktree-search@mmc7676-skills
```

Inside a session you can run `/plugin marketplace add mmc7676/skills` and then `/plugin install effort-optimizer@mmc7676-skills`. Plugin skills are namespaced by plugin name, for example `/effort-optimizer:effort-optimizer`.

**Claude Code, manual copy:** copy a skill folder into your skills directory. Each skill folder installs the same way.

```bash
git clone https://github.com/mmc7676/skills.git
mkdir -p ~/.claude/skills
cp -r skills/effort-optimizer skills/supersystem-integrate skills/linktree-search ~/.claude/skills/
```

PowerShell:

```powershell
git clone https://github.com/mmc7676/skills.git
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse skills\effort-optimizer, skills\supersystem-integrate, skills\linktree-search "$HOME\.claude\skills\"
```

**Codex and other Agent Skills clients:** the folders are plain Agent Skills, so copy them into that client's skills directory. For Codex that is `$HOME/.agents/skills` for your user, or `.agents/skills` inside a repository, per OpenAI's Codex skills documentation. Invoke by name (for example `$effort-optimizer` in the Codex CLI) or let the agent match the skill's description.

**Claude desktop / claude.ai:** open Customize, then Skills, then add a skill (the label varies by app version; look for "Upload a skill") and upload the matching zip from [`dist/`](dist/). Code execution and file creation must be enabled in your Claude settings for skills to run.

Verify a download against [`dist/SHA256SUMS.txt`](dist/SHA256SUMS.txt):

```bash
cd dist && sha256sum -c SHA256SUMS.txt
```

On Windows PowerShell, compare `(Get-FileHash .\effort-optimizer.zip -Algorithm SHA256).Hash` with the matching line in `SHA256SUMS.txt`.

## Other agents and clients

These skills follow the open [Agent Skills specification](https://agentskills.io/specification): a folder named after the skill, a `SKILL.md` with `name` and `description` frontmatter, and optional supporting files. All three pass those constraints (lowercase hyphenated name matching the folder, descriptions under the 1,024-character limit, `SKILL.md` under 500 lines, optional `license` field). The Agent Skills site lists the clients that support the format, including Claude, Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot, VS Code, OpenCode and Goose. Each client has its own skills folder and its own triggering behavior, so follow that client's own skills documentation for where to put the folder.

What to know when you use them outside Claude:
- I built and used these skills with Claude, and I have run Claude's validator on them. I have not run them inside Codex or the other clients, so treat cross-client behavior as expected from the spec rather than tested.
- `effort-optimizer` is written to apply on every turn. That works where the client activates skills from their descriptions, or where you invoke it by name.
- `linktree-search` includes `agents/openai.yaml`, which Codex-style clients use for display metadata. Other clients ignore it. The other two skills do not need one.
- Install steps for the zips in `dist/` differ by client; the folders themselves work anywhere the format is supported.

## Repository layout

- `effort-optimizer/`, `supersystem-integrate/`, `linktree-search/`: the skills. These folders are the source of truth.
- `plugins/<name>/`: a Claude plugin wrapper around each skill (a `plugin.json`, the skill under `skills/<name>/`, plus the README and LICENSE). Generated, so don't edit it by hand.
- `dist/`: the importable zips and `SHA256SUMS.txt`. Also generated.
- `.claude-plugin/marketplace.json`: the plugin marketplace that lists the three plugins.
- `scripts/build.py`: after editing a skill, run `python scripts/build.py` to regenerate `plugins/` and `dist/`. Bump `PLUGIN_VERSION` in it for each release so installed plugins update.

## Licensing

| Repo | License | Notes |
|---|---|---|
| [skills](https://github.com/mmc7676/skills) (this repo) | MIT, copyright 2026 Mike Cohan | Every skill folder and zip carries its own copy of the license, and each `SKILL.md` declares `license: MIT`. |
| [Maxey0](https://github.com/mmc7676/Maxey0) | Apache-2.0 (repo root; the `logical_scws/` subfolder is MIT) | Includes the `scw-default-deployer` skill and `research-paper-pdf-skill.zip`. |
| [logical-scws](https://github.com/mmc7676/logical-scws) | MIT | The Logical SCWs paper and dashboard. |

This repo bundles no third-party code or assets. The example hosts in `linktree-search` are placeholders (`example.com`).

The full text is in [LICENSE](LICENSE).
