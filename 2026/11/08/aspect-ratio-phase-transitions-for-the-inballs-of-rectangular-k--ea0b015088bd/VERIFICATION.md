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

The proof in `RESULT.md` establishes the statements for every admissible integer pair and rank. Run `python verify.py` from the extracted package with Python 3, NumPy, and SciPy installed. The script creates the proper Euclidean tangent space for each rank, solves 175 independent small Chebyshev linear programs, checks active-normal codimensions at the symmetric center, and verifies two threshold equalities exactly with integer arithmetic. The run prints `RECT_ASSIGNMENT_INBALL_CHECKS_PASSED` on success.

The finite numerical tests are not exhaustive over unbounded parameters and do not certify mathematical priority or constitute an independent external audit. In particular, the complete incenter locus in the theorem follows from equality of averaged constraints and from the strictly positive uniform point, not from linear-programming solver output.
