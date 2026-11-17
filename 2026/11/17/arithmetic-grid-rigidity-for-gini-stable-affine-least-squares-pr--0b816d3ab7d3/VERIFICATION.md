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

The analytic proof reduces the projected dispersion to a single mean-zero linear functional, proves its sharp Gini dual norm by binary level-set decomposition, classifies norm-one designs by the unique differentiable supporting functional at a strictly ordered design, and obtains the local two-sided expansions by exact differentiation.

Run `python code/check_exact.py` from the root of the extracted files. The code uses only the Python standard library and `fractions.Fraction`. Executed checks cover exact rational binary-cut operator norms and ternary input inequalities on 28 design instances, an irregular four-site witness, and 28 directions of first-order perturbations.

Finite tests are not a replacement for the all-real, all-dimensional proof. The program checks no irrational perturbation, infinite design family, or weighted-regression extension. The literature comparison remains subject to independent historical review.
