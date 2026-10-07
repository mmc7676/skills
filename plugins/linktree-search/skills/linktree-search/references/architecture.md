# Architecture

## Layers

These layers are specified here and are not shipped in this package; build them to this spec.

### 1. Skill layer
Defines reusable behavior, schema, guardrails, and examples.

### 2. Crawl API
Executes sitemap fetch, robots checks, bounded HTML crawl, normalization, and tree assembly.

### 3. Dashboard UI
Allows URL input, displays tree, stats, warnings, and raw JSON/outline.

### 4. Artifact UI
Single-file TSX variant for Claude-style artifact environments.

## Flow

1. User enters root URL
2. API normalizes root
3. API loads robots.txt
4. API attempts sitemap discovery:
   - `/sitemap.xml`
   - robots-declared sitemap entries (kept only if they pass the same origin, scheme, and robots checks)
5. API builds candidate queue
6. API fetches HTML pages within policy bounds
7. API extracts anchors
8. API normalizes/canonicalizes URLs
9. API emits:
   - node list
   - edge list
   - primary tree
   - markdown outline

## Primary data model

- `LinkTreeNode`
- `LinkTreeEdge`
- `LinkTreeTreeNode`
- `CrawlConfig`
- `CrawlStats`
- `CrawlResult`

These names are conceptual; the package defines only the input schema (`linktree_search_schema.json`). The output field list is in `contract.md`.

## Design decisions

- **Primary parent wins** in the tree
- Cross-links are preserved only in graph edges
- Same-origin default reduces compliance risk and noise
- Sitemap-first improves coverage on structured documentation sites
- Outline export helps feed other agents and indexing systems; label it untrusted data when passing it on
