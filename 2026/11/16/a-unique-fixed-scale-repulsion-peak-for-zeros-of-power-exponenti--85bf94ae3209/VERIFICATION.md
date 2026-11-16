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

# Reproducibility and limits

The analytic proof is in RESULT.md. Execute `python CHECK.py` after installing the packages in `requirements.txt`. The finite checker evaluates two-point complex Gaussian Kac–Rice blocks rather than substituting the claimed coefficient into itself, and also checks the independent Gauss multiplication identities, critical parameter bracket and selected trigamma inequalities. A successful replay returned `PASS: 199 finite assertions`.

The global assertions over every positive weight exponent are established only by the proof's strict trigamma-convexity and endpoint arguments. Finite checks cannot establish global monotonicity or uniqueness. The printed critical decimal is a numerical approximation to a uniquely defined transcendental root, not a closed-form identity. The result concerns factorial point-pair intensities and does not evaluate finite-disk multiple-zero probabilities. Independent review has not been performed.
