# skills

Personal Claude skills by [mmc7676](https://github.com/mmc7676). Each skill is a self-contained folder (`SKILL.md`, a `README.md`, and its own `LICENSE`) that works on its own, and each also ships as a ready-to-import zip in [`dist/`](dist/).

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

**Claude Code:** copy a skill folder into your skills directory. Each skill folder installs the same way.

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

**Claude desktop / claude.ai:** open Customize, then Skills, then add a skill (the label varies by app version; look for "Upload a skill") and upload the matching zip from [`dist/`](dist/). Code execution and file creation must be enabled in your Claude settings for skills to run.

Verify a download against [`dist/SHA256SUMS.txt`](dist/SHA256SUMS.txt):

```bash
cd dist && sha256sum -c SHA256SUMS.txt
```

On Windows PowerShell, compare `(Get-FileHash .\effort-optimizer.zip -Algorithm SHA256).Hash` with the matching line in `SHA256SUMS.txt`.

## Licensing

| Repo | License | Notes |
|---|---|---|
| [skills](https://github.com/mmc7676/skills) (this repo) | MIT, copyright 2026 Mike Cohan | Every skill folder and zip carries its own copy of the license, and each `SKILL.md` declares `license: MIT`. |
| [Maxey0](https://github.com/mmc7676/Maxey0) | Apache-2.0 (repo root; the `logical_scws/` subfolder is MIT) | Includes the `scw-default-deployer` skill and `research-paper-pdf-skill.zip`. |
| [logical-scws](https://github.com/mmc7676/logical-scws) | MIT | The Logical SCWs paper and dashboard. |

This repo bundles no third-party code or assets. The example hosts in `linktree-search` are placeholders (`example.com`).

The full text is in [LICENSE](LICENSE).
