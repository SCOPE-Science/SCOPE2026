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

Run `python3 verify.py` using standard-library Python 3. The script numerically integrates the derived joint densities, verifies total mass and the known first two width moments, checks ten direct angular-slice cases, and tests 350,000 independently generated spherical directions. For each direction it counts original cube edges whose endpoints straddle the section plane; this does not use the formula for the predicted polygon type. Twelve binned joint probabilities are checked against the analytical formulas.

The completed test reports `VERIFY_OK` if every numerical and combinatorial assertion passes. These checks supplement the exact proof in `RESULT.md` and do not certify universal propositions, historical uniqueness, or independent review.
