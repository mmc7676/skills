# linktree-search

Skill for the **LINKTREE** method: deterministic, level-preserving hierarchical URL crawling and indexing. A root URL goes in; a navigation tree, a normalized node/edge graph and a compact outline come out.

## What is in this folder

| File | Purpose |
|---|---|
| `SKILL.md` | Operating rules, output contract and build targets |
| `references/contract.md` | Canonical required behavior, output fields, semantics and prohibited behavior |
| `references/linktree_search_schema.json` | Canonical input schema and defaults |
| `references/compliance.md` | What is allowed, what is not, and the safe defaults |
| `references/architecture.md` | The four layers and the crawl flow |
| `references/examples.md` | Realistic request shapes and expected behavior |
| `agents/openai.yaml` | Display name and default prompt for Codex-style runtimes |
| `LICENSE` | MIT |

## What it does not include

This is a specification package. It contains **no crawler, dashboard or test code**. When you ask for a full LINKTREE system, `SKILL.md` lists what the agent should build and keep consistent: a crawler API, a React dashboard, a single-file artifact variant, tests for normalization and tree construction, and architecture, deployment and compliance docs.

## Defaults

Public `http`/`https` URLs only; sitemap discovery before recursive crawling; same-origin traversal; `robots.txt` respected; polite crawling (low concurrency, per-host delay, back-off); depth, page-count, timeout, response-size and total budgets; secrets redacted from query strings; fetched content treated as untrusted data. No authentication bypass, CAPTCHA solving, stealth browsing, or access to loopback or private-network addresses without the operator's confirmation for a host they own.

## With effort-optimizer

Host lowercasing, fragment stripping, tree and graph assembly and schema checks run fast. Secret redaction, URL validation and anything that widens crawl scope or weakens a protection take the slow, directly verified lane (and still need the operator's explicit authorization). A page is "verified directly" only if it was fetched; a page only listed in a sitemap is "listed, not fetched". See the [repo README](https://github.com/mmc7676/skills#how-effort-optimizer-works-with-each-skill).

## License

MIT, see [LICENSE](LICENSE).
