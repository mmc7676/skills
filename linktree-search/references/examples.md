# Examples

The hosts below are placeholders. Replace them with a site you own or are authorized to crawl.

## Example 1: Public documentation section

Input:

```json
{
  "rootUrl": "https://example.com/docs/",
  "maxDepth": 4,
  "sameOriginOnly": true,
  "respectRobots": true
}
```

Expected behavior:

- treat the normalized root URL as the traversal anchor
- expand downward by level within the origin
- use sitemaps where available
- output nested outline + graph

## Example 2: A docs portal you own

Input:

```json
{
  "rootUrl": "https://docs.example.com/platform/",
  "maxDepth": 3,
  "sameOriginOnly": true,
  "respectRobots": true,
  "preferSitemaps": true
}
```

Expected behavior:

- stay within the origin (path-prefix scoping is not part of the contract)
- skip login redirects and blocked areas
- warn on inaccessible pages
