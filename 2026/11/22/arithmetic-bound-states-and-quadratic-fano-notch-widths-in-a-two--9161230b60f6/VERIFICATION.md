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

Run `python verify.py` with Python 3, SymPy, NumPy and SciPy. The script reconstructs finite path Hamiltonians, compares their endpoint resolvents to independently generated Chebyshev polynomials exactly over rational energies, checks the polynomial gcd criterion, and independently solves the complex scattering boundary system on the infinite lead. It then uses numerical bisection to verify the exact transparency/notch structure and the leading displacement and width coefficients as detuning decreases. The recorded execution output is:

```
ALL_CHECKS_PASSED exact_resolvents=24 gcd_bics=8 direct_scattering=28 width_asymptotics=16
```

The proof is analytic for all positive integer arm lengths. Finite computations verify implementations and selected boundary regimes but do not establish the universal statements by enumeration. The asymptotics exclude joint limits in which arm lengths diverge with vanishing detuning. An independent scientific audit has not been performed.
