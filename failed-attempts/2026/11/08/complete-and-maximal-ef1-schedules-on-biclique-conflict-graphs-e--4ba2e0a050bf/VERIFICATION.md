---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Independently reconstructed the maximality trichotomy: one unassigned A forces all agents to hold B, so all A unassigned and all B allocated, and symmetrically. With identical unit chores EF1 is precisely max load - min load <=1. Splitting each part among its unique labeled recipient agents yields C and E_n formulas; if no side has >=n items, the singleton/two-item construction yields a complete equitable allocation. If no complete solution, retaining the larger side gives max(a,b) items >=(a+b)/2; K_(2h-1,2h+1) with four agents h>=3 blocks four bundles of size h and approaches half. Independently enumerated every assignment for n=2,3 and a,b<=3, matching count and throughput.

## originality

FAIL

Already-covered result: published maximal-EF1 theorem for arbitrary complete multipartite unit-good conflict graphs contains identical maximal-partial biclique trichotomy, identical exact factorial labeled count, and identical optimal retention formula. Identical unit-value goods and unit-cost chores both reduce EF1 to max-minus-min <=1. The submitted four-agent half example is a parallel simple sharpness witness, not an independent motivating discovery after known sharp half guarantee.

## value

FAIL

The labeled biclique maximal-allocation census, throughput dichotomy and sharp half guarantee are already an exact established subcase of the published multipartite theorem. The four-agent K_(2h-1,2h+1) witness is an elementary variation with no independently motivated new invariant; a different parity witness already establishes sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
