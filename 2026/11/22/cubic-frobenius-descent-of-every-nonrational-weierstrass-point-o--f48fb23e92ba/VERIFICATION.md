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

# Exact reproducibility and limits

Execute `python3 verify_weierstrass.py` in the same directory with Python 3. Its final output must include `WEIERSTRASS_SUPPORT_540_RATIONAL_96_CUBIC_VERIFIED`. The code proves the required fourth- and twelfth-power identities in a concrete, irreducible six-degree finite-field quotient, checks all six primitive ninth roots, confirms the two three-cycles and their minimal Frobenius periods, and checks 540 rational plus 288 geometric nonrational Weierstrass points by the established formula.

The finite-field equalities are exhaustive symbolic computations in a specified finite ring, not Monte Carlo tests or extrapolations. Classification of which points are Weierstrass relies on Lemma 3.11, Theorems 4.6 and 5.2, and Proposition 5.4 of Beelen--Montanucci--Vicino (2023). No independent validation, Weierstrass weights, or universal result for other characteristics is claimed.
