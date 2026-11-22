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

# Verification

The attached `check_eight_moments.py` was executed from its actual delivered source before packaging and printed:

```
PASS: 700 random configurations; 5355 root-grid and coefficient configurations; empty case.
```

All 700 random configurations span seven regimes: distinct projections, equal coefficients, each coinciding coordinate, full cancellation along either axis, and the one-atom case. The grid consists of all unordered pairs of the 35 points on the product of seventh and fifth roots of unity, with all nine coefficient-pair choices from \(\{1,-1,1+2i\}\). Both numerical tests and algebraic proof cover more than just generic position. The code runs with standard-library Python 3, as `python3 check_eight_moments.py`.

The proof is algebraic. Its pivotal identities are \(\Delta=c_1c_2(u_1-u_2)^2\), the two symmetric-node formulas, the mixed-moment pairing difference, and the cancellation recovery formula. Exact root extraction and equality checks are stipulated for the theorem; floating-point tests do not establish correctness on all continuous inputs or numerical conditioning. No independent audit has been performed.
