# SuperSystem-Integrate

Generative engineering skill for integrating newly discovered models, protocols, ideas, and capabilities into an existing software/agentic system.

Primary behavior: **understand → integrate → validate → ship**.

Supports:
- direct LLM execution
- optional observable human-side / LLM-side activation observers
- zero-shot shipping discipline
- provider-neutral integration
- bounded authority
- explicit failure semantics
- end-to-end traceability
- artifact packaging and verification
- an explicit consent boundary: "ship" means a verified local artifact; pushing, deploying, publishing or other outward-facing steps need the user's confirmation

## Notes

The skill is self-contained. Its references to Maxey0/SuperSpace, SCW, and "System One/Jev" are examples from the author's own runtime that can be ignored elsewhere ([Maxey0](https://github.com/mmc7676/Maxey0)); the discover → model → bound → design → integrate → implement → validate → package → verify loop applies to any codebase.

## With effort-optimizer

Reading, scaffolding and formatting run fast. Validation, secret scans, archive and checksum checks, and anything outward-facing (push, deploy, publish) run slow and directly verified. This skill's own consent boundary, not effort-optimizer, requires your confirmation for the outward-facing steps. Its rule against claiming results that did not occur is closely related to effort-optimizer's verified-versus-untested split. See [how effort-optimizer works with each skill](https://github.com/mmc7676/skills#how-effort-optimizer-works-with-each-skill).

## License

MIT, see [LICENSE](LICENSE).

