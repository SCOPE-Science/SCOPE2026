---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite verification and proof boundaries

Execute `python3 verify.py` using only the Python 3 standard library. The code enumerates every distance-preserving partial injection on a star with one, two, three and four leaves, then applies **both** inverse-semigroup conjugacy equations for every map and potential conjugator. It compares the resulting rank-class distributions and the complete multiset of rank/class-size pairs with the independently derived cycle/path profile formulas. The observed distributions are:

| Leaf count | Number of monoid elements | Conjugacy classes by rank |
|---:|---:|---|
| 1 | 7 | 1, 2, 2 |
| 2 | 22 | 1, 3, 6, 2 |
| 3 | 83 | 1, 3, 8, 7, 3 |
| 4 | 442 | 1, 3, 9, 12, 12, 5 |

A separate formal-series dynamic program verifies the scalar two-colored-partition identity for two through twelve leaves and the one-class jump at the sharp stabilization boundary for ranks one through five. Passing the finite tests is not a proof for infinitely many leaves: the full argument is the metric-span lemma, the exhaustive hub-moving classification and the support-size bound in `RESULT.md`. No external independent audit has occurred. The test script deliberately has no network dependencies or remote services.
