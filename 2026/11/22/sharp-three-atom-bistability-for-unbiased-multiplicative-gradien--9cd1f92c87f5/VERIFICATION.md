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

## Reproduction

Run `python3 verify.py` with Python 3 (no external libraries). It checks 3,497 rational assertions, including the exact four-piece drift, the two nonzero positive roots in the sample oracle, the three-atom sign-count rule over enumerated rational test cases, and forward-invariance inequalities for selected mean-gradient steps. All supplied computations were executed from this file.

## Analytic verification and scope

The general classification requires only the breakpoint-value signs and affine interpolation, with an equality case distinguished from simple sign-changing roots. The proof's probability bound uses a stopped-square supermartingale, the deterministic square-sum identity \(\sum_{n\ge0}[4(n+1)]^{-2}=\pi^2/96\), and almost-sure convergence of nonnegative supermartingales. Unclipped almost-sure convergence uses an eventual supermartingale estimate. The finite executable is an independent computational cross-check of rational formulas, not a substitute for infinite-domain reasoning. No independent mathematical audit or external certificate is claimed.
