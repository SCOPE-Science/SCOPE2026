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

# Computational checks and proof limits

The standard-library script `verify.py` directly solves the augmented and rim gauging equations with partial-pivot Gaussian elimination. It tests all stated exact relationships and strict bounds in 52 distinct finite configurations spanning dimensions two through seven, checks constant potentials and reports the sharp mean-chord constants in selected dimensions. Command: `python3 verify.py`.

These calculations are finite falsification checks, not a completeness certificate and not an infinite proof. The full argument is the analytic proof in `RESULT.md`; it uses the established strictly negative type of Euclidean distances, a geometric convex decomposition, the Fourier representation of the norm kernel, and explicit sharpness families. The cited literature establishes the two external theoretical inputs. No independent audit has been performed.
