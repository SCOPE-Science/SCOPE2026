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

Run `python3 verify.py` to reproduce an independent exact rational dynamic program on labeled \(K_{2,b}\) for each \(1\le b\le9\), comparing all degree probabilities to the conditional-binomial expression. It also checks total mass and all stochastic tail inequalities against the labeled uniform spanning-tree law. The mathematical proof of the infinite \(b\)-limit is analytic in `RESULT.md`; finite computations do not certify an infinite assertion. No independent audit has been performed.
