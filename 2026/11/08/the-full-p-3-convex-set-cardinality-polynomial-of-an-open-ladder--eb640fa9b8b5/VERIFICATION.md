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

# Exact reproduction and limits

Run `python3 artifacts/verify.py` from the extracted package directory. Python 3.8+ and its standard library suffice.

The check constructs the ten row-swap orbits from first principles and then evaluates the exact Bareiss determinant of the quotient transition matrix at all 231 interpolation points. The determinant difference is a polynomial of degree at most ten in the ladder-length variable and twenty in the cardinality variable, so equality at the complete rectangular grid proves the symbolic determinant identity. Separately, direct sixteen-state integer-polynomial transfer reproduces the first ten polynomial coefficients and proves the claimed numerator using its degree-at-most-nine bound. The script also compares twelve scalar totals to the previously published baseline and exhaustively evaluates all vertex subsets for ladder lengths one through eight against the raw graph-neighborhood definition.

At package construction, the command completed with `EXACT_TEN_STATE_DETERMINANT_IDENTITY_OK`, `EXACT_GENERATING_FUNCTION_NUMERATOR_OK`, `UNWEIGHTED_BASELINE_OK`, `DIRECT_ALL_VERTEX_SUBSETS_OK`, and `VERIFY_OK`. These are exact checks of the mathematical certificate. The larger-ladder identity follows from the proved rational transfer representation and finite-degree interpolation, not from length-eight brute force.

Scientific scope: the theorem counts vertex-labelled convex sets on open width-two ladders only; it does not establish corresponding formulas for wider or cyclic ladders. The 2013 scalar count and 2018 scalar generating function are acknowledged prior results. No external or independent mathematical audit has been performed.
