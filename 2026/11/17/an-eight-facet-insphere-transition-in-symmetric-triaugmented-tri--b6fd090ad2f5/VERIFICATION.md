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

The complete statement and proof are in `RESULT.md`. In a Python environment with NumPy, SciPy, and SymPy, execute `python checker.py`; the program constructs the actual nine vertices for each parameter, checks all fourteen supporting planes and their three-point contact sets, independently computes convex hulls and linear-programming inballs, and checks claimed center configurations.

Expected output is `PASS: 466 checks; transition r=0.717869821226245, h=0.696177362295413` followed by the independent volume-optimizer parameter and radius. The symbolic computation also verifies the exact sign-comparison identity after clearing positive denominators.

The universal result is not inferred from these parameter samples. The critical analytic ingredients are: complete facet identification; the convex averaging argument placing some maximal inball at the symmetry center; monotonicity and the sign identity for the three facet distances; and a strict inequality validating the full vertical center segment. The parameter interval is strictly open at both ends. The numerical root printed by the program is an approximation to the uniquely characterized algebraic number.

No external independent audit has been performed; these reproducibility checks do not constitute external certification.
