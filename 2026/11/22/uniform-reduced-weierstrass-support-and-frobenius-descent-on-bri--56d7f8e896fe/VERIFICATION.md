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

## Reproducibility

Run `python3 verify.py` in the directory containing these files. The script uses only Python's standard library. It reconstructs the cubic discriminant, enumerates splitting possibilities for primes below 1000, constructs actual finite fields of sizes 49 and 1331 and the prime field of size 43, and enumerates all 60 candidate Weierstrass supports from the ordered-root construction. Every candidate is checked against the three defining power-sum equations; finite-field Frobenius orbits are computed directly.

Observed results: characteristic seven has 30 cycles of length two; characteristic eleven has 20 cycles of length three; characteristic 43 has 60 fixed points. The successful output ends with `BRING_WEIERSTRASS_P_GE_7_ORDERED_ROOT_SUPPORT_VERIFIED`.

## Mathematical limits

Finite arithmetic tests do not establish the universal theorem. The proof is the independent algebraic argument via the six fixed points per transposition, tame involution action on canonical differentials, the classical Wronskian weight budget, and Frobenius action on ordered roots. No independent audit has been performed.
