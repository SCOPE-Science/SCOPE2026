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

# Reproducibility and verification

This package includes `verify_theta.py` and `check_dynamics.py`. Execute from this directory using Python 3, NumPy and SciPy:

```
python verify_theta.py
python check_dynamics.py
```

The first program independently diagonalizes the full adjacency Hamiltonian on all 343 ordered length triples in \(\{2,\ldots,8\}^3\), resolves degenerate eigenspaces and projects onto the joint kernel of the two hub evaluations. It checks the analytic projector, its rank and idempotence, commutation with the Hamiltonian, the explicit gcd dimension, and the exact full-capture criterion. Its coverage includes 4116 internal-site comparisons and 126 complete-capture cases.

The second program constructs the actual no-capture non-Hermitian propagator with **unequal positive terminal loss rates** for 28 parameter cases. It compares 282 localized long-time survival values with the arithmetic projector prediction. The observed tolerance bound is \(8\times10^{-5}\); convergence at finite numerical time is not a proof of infinite-time disappearance of transients.

The mathematical proof in `RESULT.md` covers all integer path lengths at least two and every pair of strictly positive capture rates. The tests are finite corroboration and do not certify every parameter. Independent scientific audit has not been performed.
