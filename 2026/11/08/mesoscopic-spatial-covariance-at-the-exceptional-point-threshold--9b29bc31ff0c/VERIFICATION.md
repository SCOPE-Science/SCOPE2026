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

# Verification of the stationary directed-chain covariance theorem

The exact finite-size covariance formula follows directly from the stationary Gaussian stochastic convolution and evaluation of gamma integrals. For every \(\kappa>0\), the matrix \(-\kappa I+J\) is Hurwitz; the covariance solves the unique stationary Lyapunov equation. An independent finite recursion solves that equation using exact rational arithmetic and checks each entry against the displayed binomial sum.

Running `python VERIFY.py` with the Python standard library returned:

`PASS: 15215 exact-rational and bounded asymptotic/integral checks`

The script also numerically compares critical covariance values at several sizes, detunings, and distances; validates the error-function representation; and confirms the known subcritical infinite-chain variance at large finite size. The code and proof use the same noise convention \(\sqrt{2D}\,dW\), giving a stationary single-site variance of \(D/\kappa\) when the coupling is absent. Finite tests alone do not establish the infinite-size limit: its validity rests on the uniform local-binomial limit and bounded-singular-endpoint contribution proved in `RESULT.md`.

No independent external scientific review, formal proof certification, or exhaustive publication-priority determination has been performed.
