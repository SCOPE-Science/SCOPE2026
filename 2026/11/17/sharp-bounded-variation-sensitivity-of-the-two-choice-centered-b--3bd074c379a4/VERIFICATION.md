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

Run `python VERIFY.py` with Python 3 from the extracted directory; it uses only Python's standard library and exact rational arithmetic.

The executable checks exhaustive binary branch masks for radii \(1\le r\le7\), matches each maximal jump norm to \(1+4\lfloor r^2/4\rfloor/(2r+1)\), solves finite rational systems to construct strictly realized optimal activation patterns and nonnegative attaining input pairs for radii \(1\le r\le8\), and performs 150 rational two-input tests per radius for \(1\le r\le7\). Its successful terminal line is `ALL_TWO_CHOICE_BV_CHECKS_PASS`.

Those experiments do not certify infinitely many radii or all inputs. The unrestricted claim follows from: (i) positive-part secant representation and jump decomposition; (ii) the explicit variation formula for the two reflected ramps; (iii) the nonadjacent weighted descent maximum; and (iv) invertibility of the finite principal box-averaging defect to realize the sharp masks. These proof steps, their domain, and the finite-dimensional positivity energy identity are supplied in `RESULT.md`.

This package contains no external independent audit.
