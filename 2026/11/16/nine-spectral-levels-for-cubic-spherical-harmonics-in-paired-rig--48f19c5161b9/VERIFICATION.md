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

# Verification of the degree-three paired-lune spectrum

## Analytical checks
The complete proof is in `RESULT.md`. Its normalized radial beta-correlation identities, four-by-four characteristic polynomial, multiplicity sum, and core strict-ordering identity are reconstructed by `verification/symbolic_check.py` using exact SymPy expressions. The two positive correlations are explicitly calculated, rather than inferred from floating-point matrix diagonalization.

## Direct Gram computation
`verification/gram_check.py` independently constructs all harmonic cubic polynomials by projecting degree-three monomials via \(P\mapsto P-|x|^2\Delta P/[2(d+2)]\). It computes full-sphere and wedge-restricted moments via sphere beta moments and the regularized incomplete beta function, whitens a full Gram matrix and compares its entire spectrum to the explicit formula in dimensions \(3,4,5,6,7,8\). Every rank count agrees with \(d(d-1)(d+4)/6\); the largest absolute eigenvalue discrepancy observed was \(3.66\times10^{-15}\). The dimension-three test checks agreement with the known boundary specialization and is not included in the new claim.

## Reproduction
From the unpacked artifact directory, execute:

```bash
python verification/symbolic_check.py
python verification/gram_check.py
```

Dependencies: Python 3, SymPy, NumPy and SciPy. Both checks passed in the present package construction. They are checkers, not proof of an infinite claim in isolation. The all-dimensional argument uses symbolic identities and decomposition, and does not use finite enumeration to justify its universal part. No human or independent audit has been performed.
