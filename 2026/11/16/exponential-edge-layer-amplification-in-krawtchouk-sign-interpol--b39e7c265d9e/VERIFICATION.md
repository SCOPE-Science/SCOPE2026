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

# Reproducibility and boundaries

Run `python3 checker.py` using Python 3's standard library. The program computes exactly the sign interpolant using both barycentric Lagrange and the separately constructed paired nodal-product formula at rational non-node evaluations; verifies the alternating central-binomial first-moment identity for 100 sizes; and checks two finite-edge normalized coefficient trends at three sizes each. It reports 202 completed checks.

The infinite mathematical result is established analytically, not inferred from tests. The key uniform bound is obtained using the smooth cutoff of Gamma-ratio weights, a third-derivative integral estimate and two exact finite-difference summation steps. Stirling's formula then converts this to the edge law. The asymptotic is a statement about a moving boundary coordinate; it is neither a finite-precision maximum estimate nor a claim about the complete norm's leading term. No independent audit or external verification is represented.
