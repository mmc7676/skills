# skills

Personal Claude skills by [mmc7676](https://github.com/mmc7676). Each skill is a self-contained folder (`SKILL.md` plus a `README.md`) that works on its own, and each also ships as a ready-to-import zip in [`dist/`](dist/).

> More skills are queued for upload. These are the first.

## Skills

| Skill | What it does | Folder | Zip |
|---|---|---|---|
| `effort-optimizer` | Always-on skill that matches reasoning and verification effort to a task's real stakes: fast on mechanical, reversible steps; slow and directly verified on anything touching auth, security, production, or a claim the user will act on unchecked. Reports "verified directly" and "plausible but untested" as different things. | [effort-optimizer/](effort-optimizer/) | [zip](dist/effort-optimizer.zip) |
| `supersystem-integrate` | Generative engineering skill: discover the intent and feasibility of a new model, protocol, idea or capability, integrate it modularly into an existing system, validate it, and ship the finished artifact. Its Maxey0/SuperSpace passages are optional conventions; the loop works for any codebase. | [supersystem-integrate/](supersystem-integrate/) | [zip](dist/supersystem-integrate.zip) |

## Related skill that lives elsewhere

- `scw-default-deployer` is part of the Maxey0 runtime and is maintained there, so it is not duplicated here: [Maxey0/skills/scw-default-deployer](https://github.com/mmc7676/Maxey0/tree/main/skills/scw-default-deployer). It expects the Maxey0 gates and MCP surfaces.

See also [Maxey0](https://github.com/mmc7676/Maxey0) (the runtime and its core skills) and [logical-scws](https://github.com/mmc7676/logical-scws) (the Logical SCWs paper and dashboard).

## Install

**Claude Code:** copy a skill folder into your skills directory. Each skill folder installs the same way.

```bash
git clone https://github.com/mmc7676/skills.git
mkdir -p ~/.claude/skills
cp -r skills/effort-optimizer skills/supersystem-integrate ~/.claude/skills/
```

PowerShell:

```powershell
git clone https://github.com/mmc7676/skills.git
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse skills\effort-optimizer, skills\supersystem-integrate "$HOME\.claude\skills\"
```

**Claude desktop / claude.ai:** open Customize, then Skills, then add a skill (the label varies by app version; look for "Upload a skill") and upload the matching zip from [`dist/`](dist/). Code execution and file creation must be enabled in your Claude settings for skills to run.

Verify a download against [`dist/SHA256SUMS.txt`](dist/SHA256SUMS.txt).

## License

MIT, see [LICENSE](LICENSE).
