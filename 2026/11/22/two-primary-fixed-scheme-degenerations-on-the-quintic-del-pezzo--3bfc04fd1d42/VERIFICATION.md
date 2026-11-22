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

The exact checker `check_2primary_fixed.py` checks both group laws, two lifted blow-up coordinate transformations, the fixed-ideal elimination, invertibility of excluded denominators, the factorization of the interior fixed polynomial, the characteristic-two square-zero witness, and all boundary intersection possibilities. It checks ten prime fields directly; the general finite-field statements are proved symbolically in the result.

The checker requires SymPy and prints `EXACT_TWO_PRIMARY_FIXED_SCHEMES_VERIFIED` on success. No external mathematical review or independent validation is claimed. The characteristic-two nonreduced structures are essential; rational-point counts alone cannot certify them.
