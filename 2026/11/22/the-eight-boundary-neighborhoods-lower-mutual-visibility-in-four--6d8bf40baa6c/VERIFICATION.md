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

Reconstructed the infinite reduction: a geodesic traverses path columns monotonically and uses a shortest C4 row route. In an obstacle-free column run, any row changes made inside that run can all be consolidated into one column without changing entry/exit rows, blocking status, or geodesicity. Thus visibility for marked endpoints depends on the ordered marked columns and solely on whether successive columns have a nonempty intervening run. Adding a test vertex retains its row and either its already marked column or the two adjacency booleans on its sides. For a gap of distances 2,3,>=4 these interior possibilities are respectively (1,1), (1,>=2)/(>=2,1), and those last two plus (>=2,>=2); a single side at a vacant end needs only distance 1 versus >=2. Every extension type has a representative before and after compression, also for old pairs whose paths could now be blocked by the new vertex. The bound 17 follows, with m>=2 and with m=2 only if the original cylinder has n=2. The independent replay checks every possible reduced pattern of sizes two through four, with exact set comparisons. Singletons and the empty set are extensible. Lift each surviving pattern by the preserved boundary and distance-one markers. At every length a terminal neighborhood is visible because the three pairs of leaves have alternative common neighbors outside it; no outside vertex can be added because a geodesic from the center must first use an already selected neighbor. The cube's two bipartition sets occur in the uncompressed height-two check.

## originality

PASS

Credit the neighborhood upper-bound method. The independently supported difference is the lower bound and full rigidity on a four-cycle cylinder family, with a distinct cube case. Neither the triangular-cylinder result nor the higher-visibility extrema cover it.

## value

PASS

The result precisely settles an infinite subfamily of the natural lower-visibility cylinder problem, going beyond a neighborhood upper bound to exact minimizer structure. Compression gives an exact finite reduction, not a list of arbitrary small tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
