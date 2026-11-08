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

Run `python3 verify.py` in the same directory as `RESULT.md`. The script requires only Python 3's standard library. It verifies exact characteristic-two polynomial identities for \(n=2,3,4,5,6\), then enumerates the finite field \(\mathbb F_{2^{2n}}\) for \(n=2,3,4\). For each of these fields it tests all \((2^n+1)\)-st roots of unity, their actions on every affine parameter, all subgroup rationality counts, and minimal full-descent degrees.

Recorded output:
```
POLYNOMIAL_OK n= 2 q= 4
POLYNOMIAL_OK n= 3 q= 8
POLYNOMIAL_OK n= 4 q= 16
POLYNOMIAL_OK n= 5 q= 32
POLYNOMIAL_OK n= 6 q= 64
FIELD_OK n= 2 geometric_order= 5 full_descent_degree= 4
FIELD_OK n= 3 geometric_order= 9 full_descent_degree= 6
FIELD_OK n= 4 geometric_order= 17 full_descent_degree= 8
CERTIFICATE_OK
```

The script does **not** computationally enumerate projective stabilizers of all possible degrees. Completeness and the all-degree formulas instead follow from the singular-point, affine-parameter, and monomial-coefficient proof in `RESULT.md`. The checker is an exact finite consistency test, not an independent certification of the infinite result.
