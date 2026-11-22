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

# Verification of the central-kernel phase diagram

The supplied `VERIFY.py` requires Python 3 with SymPy, runs with `python VERIFY.py`, and performs exact symbolic checks of: (i) the degree-five moment-reciprocal generating series and its quartic numerator; (ii) the Cayley half-plane polynomial; (iii) the complete quartic Routh first column; (iv) the absence of nonzero imaginary-axis roots; (v) the two exact simple boundary zeros; and (vi) the Routh sign-change counts at three rational representative parameters. The output was `PASS: generating-function numerator, Cayley polynomial, Routh identities, imaginary-axis exclusion, simple boundary crossings and region counts` (on two lines).

The proof in `RESULT.md` supplies the all-real-parameter argument. The script is not a substitute for the Routh theorem, nor an exhaustive finite sweep of parameter values. The verified claim is an axial zero count and its consequent sufficient obstruction to global zero-freeness; it does not assert a global equivalence.
