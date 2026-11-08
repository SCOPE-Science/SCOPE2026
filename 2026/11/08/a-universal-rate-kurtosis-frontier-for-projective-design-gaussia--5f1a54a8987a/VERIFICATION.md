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

# Verification and limits

The exact checker is `verify.py` and its recorded standard output is `verify_output.txt`. With Python 3 and SymPy installed, run:

```bash
python verify.py
```

The checker verifies the exact polynomial identities for the three pair projectors on the two-dimensional centered subspace of \(\mathbb R^3\), including the projective design's quadratic and quartic moments for a symbolic centered vector. It verifies the factorization \(t_4-\rho^2=\eta^2(2-\eta)^2/8\), the stationary fourth-moment fixed-point equation, the calibrated covariance, and the exact frontier. It also checks 21 exact-rational parameter/variance combinations.

The general theorem for arbitrary projective second-moment design laws is justified by the analytic proof's one-step moment identities, \(W_2\) contraction, fourth-moment drift, and strict contraction on homogeneous quartic polynomials. Finite symbolic examples do not replace that proof. No experiment establishes uniqueness in the literature, and no external independent validation has been performed.
