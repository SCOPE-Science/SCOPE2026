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
The exact-arithmetic script `verify_double_bouquet.py` constructs piecewise-quadratic solutions of the Kirchhoff Green equation directly from weighted vertex Laplacians, without invoking effective-resistance integration formulas. Each input circle becomes two equal parallel semicircle edges; exact rational edge masses and the quadratic particular solution are retained. The script compares the resulting point-evaluation constants with the candidate formula for 135 generated rational networks, then checks the crossing at bridge length \(2/9\) for circle lengths \(3,3,3\) on one side and \(2\) on the other.

Run `python verify_double_bouquet.py` with a current SymPy installation. The successful output ends with `ALL_DOUBLE_BOUQUET_CHECKS_OK`. The finite computation does not prove the infinite-parameter theorem; the analytic derivation, strict local maxima and comparison identities are supplied in `RESULT.md`. No independent audit has been conducted.
