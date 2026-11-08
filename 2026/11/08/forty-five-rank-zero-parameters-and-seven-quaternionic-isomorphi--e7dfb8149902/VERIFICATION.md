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
Two standard-library Python programs in this package were executed successfully:

```sh
python3 verify_coefficients.py
python3 verify_frobenius.py
```

`verify_coefficients.py` independently extracts the exact characteristic-eleven Cartier matrix from the fifth power of the defining hyperelliptic polynomial, and also performs a characteristic-seven contrast. `verify_frobenius.py` independently forms the Frobenius-twisted product, confirms the polynomial matrix factorization, tests every rank-one-block minor and exceptional value, confirms the rank-zero polynomial is squarefree with exactly 45 geometric roots, and algebraically checks invariance of its zero set under six published isomorphism transformations. The resultant identities are polynomial identities over the prime field and therefore valid over its algebraic closure.

The geometric automorphism and isomorphism classification is used as an attributed published theorem and was examined in the primary paper. These checks are not independent peer review and do not certify absence of older equivalent results. The statement does not infer Newton polygons or stronger p-torsion structure from the rank data.
