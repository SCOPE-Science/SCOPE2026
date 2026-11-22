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

# Reproducibility

Execute `python3 verify_closed_places.py` using Python 3 and SymPy. The verified script constructs the finite fields using bitwise polynomial reduction and checks irreducibility by monic trial factors of bounded degree, normalizes and enumerates every projective point, constructs Frobenius orbits, confirms an exact order-five projectivity and the four projective Groebner unit ideals, and computes the first six zeta-numerator coefficients from the counted extension points. The output statuses are `SMOOTHNESS_AND_ORDER_FIVE_IDENTITIES_VERIFIED` and `LOW_DEGREE_CLOSED_PLACE_SPECTRUM_VERIFIED`.

The arithmetic computation is exact and exhaustive for extensions of degrees at most six. The universal classification relies on the separately cited one-orbit theorem, not on a second enumeration of every embedded curve. The full zeta function and higher-degree closed places are not established. Independent mathematical audit has not been performed.
