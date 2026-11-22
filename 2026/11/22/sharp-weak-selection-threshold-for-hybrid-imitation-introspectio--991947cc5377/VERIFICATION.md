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

# Verification and boundaries

The mathematical claim is an exact finite-population first-order stationary perturbation formula. It is proved by explicit neutral spin-correlation equations, differentiation of transition rates, and summed stationarity, without a mean-field approximation.

Run the included `verify_hybrid.py` with Python 3 and no external packages. The program independently enumerates the finite transition matrix, solves its stationary equations, and compares finite differences with the derived coefficient. It also solves an eight-state perturbation system over exact rational numbers and verifies the exact zero-mutation single-introspector threshold formula.

Recorded checks: four exact eight-state rational comparisons; 90 finite-state numerical derivative comparisons (population sizes 2–5, varied rule mixes, positive contributions, return rates, and mutation including zero); 19 exact rational identities for populations 2–20. All passed. A finite enumeration is not a proof of a claim quantified over all population sizes; the general derivation is in `RESULT.md`.

The expansion is local as sensitivity tends to zero with other parameters fixed, and does not imply a global strong-sensitivity threshold or equality at the first-order boundary. Historical priority and the complete literature census have not been independently validated.
