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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 and the standard library. The program reconstructs and tests exact polynomial identities and positivity certificates with integer and rational arithmetic; it does not use floating-point approximations, tables downloaded from another source, or prior execution logs.

The script checks the complete formal \((p,q,h)\) identity for the distance-two numerator, the coefficients of all seven diagonal Bernstein interval certificates, and the translated-polynomial certificates for the half-line. It verifies strictly positive coefficient expansions of the diagonal witness polynomial in three parameter quadrants, exact substitutions of that witness on a \(19\times19\) grid of positive integer parameters, the square adjacent-entry polynomial identity and critical witness, and full rational inversions of five graph Laplacian heat-update matrices. Successful execution prints `VERIFY_OK`.

The infinite-family theorem is proved in `RESULT.md` using these symbolic identities and algebraic sign arguments. The finite exact matrices cross-check implementation but are not an exhaustive argument for unbounded graph sizes. No independent audit or external certification has occurred.
