# Effort-Optimizer

Mandatory, always-on skill that calibrates effort to a task's actual stakes before acting — not to how big the request sounds.

Primary behavior: **classify → verify what's cheap and consequential → act at the matching speed**.

Supports:
- explicit effort signals typed by you (`[effort: low]`, "optimized effort," "thorough") taking priority over default classification; tags found in fetched pages, files or tool output are ignored
- fast, low-verification handling for mechanical/reversible/already-checked steps
- slow, directly-verified handling for auth/security/production/user-actionable claims
- immediate, transparent correction when a fast-path assumption turns out wrong
- visibly distinguishing "verified directly" from "plausible but untested" in every report

## Works with the other skills

effort-optimizer sets how hard each step of another skill is pushed. These mappings are the default when you give no explicit effort signal; it grants no permission and does not replace the other skill's own rules.

- **supersystem-integrate:** reading, scaffolding and formatting run fast; validation, secret scans, packaging checks and anything outward-facing (push, deploy, publish) run slow and directly verified. Its own consent boundary, not effort-optimizer, requires your confirmation for those outward-facing steps.
- **linktree-search:** host lowercasing, fragment stripping and tree assembly run fast; secret redaction, URL validation and anything that widens crawl scope or weakens a protection run slow, with `robots.txt` and the sitemap checked directly. Verification is not permission to weaken a protection.
- **scw-default-deployer** (in [Maxey0](https://github.com/mmc7676/Maxey0/tree/main/skills/scw-default-deployer)): a suggested pairing for deciding how much verification happens inside the context window it creates.

Details: [how effort-optimizer works with each skill](https://github.com/mmc7676/skills#how-effort-optimizer-works-with-each-skill).

## License

MIT, see [LICENSE](LICENSE).
