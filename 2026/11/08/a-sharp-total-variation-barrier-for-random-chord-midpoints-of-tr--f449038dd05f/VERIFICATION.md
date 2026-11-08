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

# Reproduction and limitations

Run `python3 verify_midpoint.py` with Python 3.9 or later (standard library only). The verifier independently generates two uniform boundary points using side selection followed by uniform normalized edge coordinates; it classifies their midpoint by barycentric coordinates. It also recomputes rational formulas with `fractions.Fraction` for multiple exact triangle side triples and confirms the sharp equilateral and thin-isosceles benchmark cases.

Execution produced:

`VERIFY_OK exact_cases=6 exact_mass_relations=7 per_case monte_carlo_trials=35000 total_trials=175000`

The exact proof in `RESULT.md` is the mathematical justification for all nondegenerate triangles. Finite test cases and simulations are supporting checks only. Prior literature comparisons are provisional; no independent scientific audit has been performed.
