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

# Reproducibility and scope

Run `python verify.py` using Python 3.10+ with SymPy, NumPy, and SciPy. The script checks the determinant, trace, discriminant, eigenvector relations, critical quadratic coefficient and migration branch coefficient symbolically, and the rational example exactly. It performs supplemental finite integrations for three critical initial states, three positive equilibria approaching threshold, and two supercritical trajectories. The executed script ended with `VERIFY_OK: exact linearization/center coefficients, branch and finite trajectories`.

The proof of global convergence and the reciprocal-time limit is in `RESULT.md`. Numerical integrations have finite precision and finite horizon; they are not used to establish global uniqueness, impossibility of other recurrent states, or the infinite-time limit. No independent external audit has been performed.
