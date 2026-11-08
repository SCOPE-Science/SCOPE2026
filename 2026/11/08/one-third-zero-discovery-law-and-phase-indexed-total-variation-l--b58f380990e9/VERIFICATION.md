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

Run `python3 verify_one_third.py` using only the Python standard library. The script completed successfully with 120 grouped checks: an exact integer-polynomial factorization; exact rational finite-sample retained-alphabet occupancy events; direct finite first-hit products and telescoping identities at six positive time parameters; and finite approximations to phase-law moments and void probabilities at five phases. The computation is a finite consistency check, not a proof of the all-integer total-variation bound or historical originality. Those are established analytically in `RESULT.md` and compared with identified prior primary literature.

The unbounded count of categories is handled in the proof by absolute summability and a coupling tail of exactly exp(-n). Fixed-draw Poissonization error uses Chebyshev and a proved O(1/u) discovery intensity bound, not a simulation estimate. No independent audit has been performed.
