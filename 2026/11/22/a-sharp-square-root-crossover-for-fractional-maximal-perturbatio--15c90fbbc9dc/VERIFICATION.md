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

The analysis is self-contained in `RESULT.md`: exhaustive graph-ball formulas, an upper Jacobian norm estimate on every piece, a strict feasible branch with explicitly attaining perturbations, and an asymptotic squeeze. This constitutes the mathematical proof for all admissible integer sizes and fractional exponents. The checker `check_star_fractional_crossover.py` can be executed by `python check_star_fractional_crossover.py` with standard Python 3; it independently evaluates 40 local strict activation witnesses, 4,000 seeded real and complex input pairs and three large-size critical-window approximations.

Floating-point tests verify sample arithmetic and branch feasibility only, not claims quantified over infinitely many graphs or all exponents. No external or independent audit has been performed; the review is same-model only. The exact finite-size optimum, a complete extremizer list and extension to other graph families are not established.
