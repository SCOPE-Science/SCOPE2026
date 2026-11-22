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

# Verification notes

- An exact strong-Markov argument and backward ODE give the no-reset open-gate contact transforms for each initial gate state, with an arbitrary shared reaction-threshold factor.
- The two-state gate-at-reset resolvent and renewal equations give the universal delay by explicit matrix inversion; the proof has no numerical extrapolation.
- `CHECK.py` verifies symbolic algebra for the arbitrary threshold factor and finite Robin specialization, performs 10 direct matrix-renewal tests spanning several distinct threshold distributions, and compares 5 full finite-difference boundary-value problem pairs against the exact Robin means.
- The numerical finite-difference verification approximates a half-line with a distant reflecting truncation boundary and therefore does not alone certify the continuum result; no claim of computational proof of infinite-dimensional exactness is made.
- Prior literature contains the exact instantaneous-absorption delay; only invariance of that delay under arbitrary independently refreshed contact-threshold laws is assessed as an additional result.
- No independent audit or external validation has been performed.
