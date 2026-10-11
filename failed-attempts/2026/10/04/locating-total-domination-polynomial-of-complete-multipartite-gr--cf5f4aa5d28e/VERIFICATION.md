---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Total domination is equivalent to meeting at least two parts. Two omitted vertices in one part have identical open-neighborhood traces, so at most one may be omitted. For omitted vertices from distinct parts \(i,j\), the traces are \(S\setminus V_i\) and \(S\setminus V_j\), equal exactly when both selected intersections with those parts are empty; under the one-omission rule this occurs exactly for two omitted singleton parts. This proves the three conditions, and the product polynomial with the two small support exceptions follows by independent choices in each part.

## originality

PASS

The checked primary locating-total literature gives general bounds, complexity results, and special families but no all-set polynomial for complete multipartite graphs. Resultary searches returned the assigned formula and related domination variants, not an earlier equivalent locating-total enumerator.

## value

FAIL

Although the enumerator is exact and apparently unpublished, on complete multipartite graphs it follows immediately from three elementary observations about support across parts and identical traces, followed by a product expansion and two tiny boundary exceptions. Under the shared value bar this is routine definition chasing rather than a substantive structural gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
