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

# Reproduction and scope of verification

Run `python3 check.py` using Python 3 standard library only. The script independently computes the angular and radial data for the four cubic polynomial examples, tests strict contraction on sampled angles, checks the exact angular factorization at several offsets, and integrates the exact original-time inverse-radial equations using fourth-order Runge–Kutta steps. The observed scaled clocks match their proved asymptotic constants within stated explicit diagnostic tolerances; a successful run prints `VERIFY_OK`.

The scientific proof is analytic and appears in `RESULT.md`, including uniform radial positivity, the precise initial-coordinate and measure normalization, first-crossing asymptotics, pushforward survival laws, moment tests, and polynomial-degree bounds. The numerical diagnostic does not certify continuous positivity, the uniqueness of all possible equilibria, infinite limits, or the novelty of the theorem. These are respectively supported by the written analytic inequalities, credited prior classification, and targeted source comparisons. Independent audit status is not performed.
