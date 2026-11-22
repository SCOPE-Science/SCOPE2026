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

# Reproduction and limits

Execute `python verify_five_node.py` (Python 3 with NumPy). The script compares independently solved five-by-five real Fourier-moment systems with the Lagrange constant-term formula for 1,250 deterministic-pseudorandom grid configurations (6,250 individual weight comparisons), checks all 16 extreme perturbation patterns at six radii not exceeding the critical value, verifies the algebraically defined critical radius numerically, and outputs examples on both sides of the transition. The script completed successfully during this review.

Exact support for the universal claim is the analytic derivation in RESULT.md, not a finite sample test. The uniqueness of Fourier quadrature follows from distinct circle nodes and the invertible degree-two trigonometric interpolation matrix; the sign criterion and uniform minimization are given in RESULT.md. No computer proof, symbolic completeness, or independent mathematical audit is asserted. The verified test concerns only the included current package; no external code or experiment is needed for the analytic argument.
