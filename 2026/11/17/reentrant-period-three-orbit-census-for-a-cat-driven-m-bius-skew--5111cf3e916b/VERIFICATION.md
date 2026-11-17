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

# Reproducible checks and limits

The included `verify.py` uses only the Python 3 standard library. Execute `python3 verify.py` in a directory containing the standalone file. It checks all sixteen third-iterate cat-map fixed points by rational arithmetic and confirms that they comprise one fixed point and five primitive three-cycles. It exactly expands all three-step SU(1,1) traces as integer Laurent polynomials and checks the nonzero off-diagonal expression for the same-sign itinerary. It prints `CAT_DRIVEN_PERIOD_THREE_EXACT_CENSUS_OK` on success. Representative floating-point evaluations check the strict threshold order and trace signs but are not evidence for all parameters.

The universal conclusion rests on the determinant-fixed-point count, explicit algebraic monodromy, elementary threshold inequalities, and the standard circle-Möbius fixed-point trichotomy as explained in `RESULT.md`. The computations do not certify priority, other periods, broken-symmetry persistence or independent validation.
