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
# Verification record

The forward-KL theorem for fixed nonexponential Gamma shape was evaluated against the exact finite-sample maximum density and the analytic incomplete-gamma expansion. The proof's global optimizer is the unique minimum of a strictly convex inverse-scale function. The score projection uses the exact Gamma-function derivative moment identity, not Monte Carlo. The separate `verify.py` numerical diagnostic reproduced the score Gram determinant, optimizing location and scale corrections, positive zeta-value residual, and finite-sample KL integrals for Gamma shapes two and three at sample size one million, as recorded in `CHECKS.txt`. The numerical evaluations check signs and leading-scale plausibility but cannot independently certify the infinite-domain asymptotic or historical novelty.

The result is limited to forward KL, fixed positive shape other than one, and first-order asymptotics. Reverse KL is infinite due to support mismatch. No mathematical claim about independent verification is made.
