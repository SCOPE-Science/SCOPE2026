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

# Reproducible verification

Run `python3 verify.py` in the same directory; Python 3's standard library is sufficient. The code represents every affine quantity by an exact rational coefficient triple and constructs all feasible intersections between the original spread's three linearity regions and the two relevant child-ordering regions. It derives every polygon vertex by rational line intersection and verifies the global mixed-block spread estimate and one-step monotonicity at all vertices. This is an exhaustive piecewise-linear certificate, not random input sampling.

Actual output:

`VERIFY_OK rational_cells=31 vertex_checks=61 minimum_checks=122 one_step_width_checks=61 maximal_linear_gap=0 sharp_isosceles_cases=5`

The checker also verifies representative rational shapes that attain the asserted sharp ratio exactly. Proof of the convergence and tree-concentration consequences is provided analytically in `RESULT.md`. These calculations have not undergone independent scientific validation.
