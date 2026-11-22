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

Run the two Python 3 standard-library scripts in the same directory:

```
python3 check_polynomial.py
python3 check_coefficients.py
```

Both completed successfully. `check_polynomial.py` enumerates all 256 bit-polynomial characteristic polynomials, verifies the joint entropy–strong-transitivity table, traverses all six onsite invertible matrices, and verifies all 56 orbit strata and orbit sizes. `check_coefficients.py` separately enumerates all 256 binary matrix pairs using exact componentwise coefficient formulas, checks all 32 entries of the trace–determinant multiplicity table, classifies the 256 cases into disjoint test outcomes, and reproduces the joint table.

The analytically quantified finite Laurent root bound uses integrality of polynomial-ring eigenvalues and degree comparison, not finite testing. The infinite strong-transitivity equivalence and the entropy normalization depend on published theorems explicitly cited in `RESULT.md`. The finite scripts do not provide any additional independent audit or theorem certification. The exact joint census covers onsite basis-change orbits only, and historical priority against unindexed numerical classifications is not established.
