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

The proof is analytic and exact. It derives the dual zonotope and recovers its generator vectors from all one-dimensional exposed faces, then classifies the signed generator permutations using the wheel's dependent triples. Its special case uses coefficient ratios of triangle relations and vertex-reanchoring operations on \(K_4\).

The executable `check.py` uses exact rational arithmetic, not floating-point tolerances. It enumerates candidate signed-generator isometries for \(n=3,4\) and \(\gamma=1/2,1,2\) and tests every such transformation on all ternary vectors. Run `python3 check.py` to reproduce `DISCRETE_W11_WHEEL_ISOMETRY_CHECK_OK 5840`.

These finite checks do not certify the arbitrary-dimension or arbitrary-positive-weight statements. The analytic proof supplies those quantifiers. Bibliographic originality is subject to the identified oriented-matroid and graph-norm terminology risk. Independent mathematical audit has not been performed.
