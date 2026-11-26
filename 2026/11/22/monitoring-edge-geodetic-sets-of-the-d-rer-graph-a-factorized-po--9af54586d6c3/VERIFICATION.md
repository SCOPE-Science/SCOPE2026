---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For this labelled GP(6,2), exhaustive shortest-distance comparisons with and without each edge reproduce all three representative witness tables, of sizes 6, 7 and 3. Rotation covers the graph. Spoke and inner-edge witnesses force an endpoint of their respective edges; conversely, the tables witness every edge under the spoke and triangle conditions. For each parity independently, at most one spoke can be outer-only, giving (z+z²)^3+3z(z+z²)^2. Taking the inner vertex whenever available yields a size-six subset satisfying the same criterion, so there are no other inclusion-minimal sets. Any valid one-token exchange switches endpoints at one spoke, and is thus also a slide; for each parity the three nonempty outer-index states are adjacent only to the empty state. A fresh replay tested all 4,096 subsets and confirmed counts 16,72,129,116,54,12,1, 400 total, 16 minima, the same 24 jump and slide edges, diameter 4, and degree multiplicities 9,6,1 at degrees 2,4,6.

## originality

PASS

The exact Dürer spoke/triangle criterion, labelled size polynomial, and optimal exchange product are not covered by the distinct inspected statements. The exact catalogue hit is the frozen result itself; related same-day and earlier catalogue findings treat different graphs or different moves. The general monitoring predicate is known and is not credited as original. The verdict is limited to the supported classification, enumerator and optimal move graph, not a claim of historical priority for the minimum number alone.

## value

PASS

The canonical cubic polyhedral graph has short cycles and diameter four, outside the cited simple cover criteria. The exact answer replaces a list of subsets by independent parity constraints, explains why every minimal solution is optimal, and determines the entire optimal motion space, including why restricting to slides costs no moves. These answer concrete questions about this standard graph that the minimum number alone cannot answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
