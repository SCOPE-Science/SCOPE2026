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

## Reproducible checks

Run `python3 bdfl2_phase_verifier.py` (Python standard library only). The recorded output was `PASS 11548 rational checks; boundary k=1/2,r=3/2 gives exact termination from n=2`. The checker verifies algebraic identities, sampled trajectories, forbidden-step negative witnesses and the nilpotent endpoint. Finite sampling is not a proof of the universal positivity statement; that follows from the root decomposition and sign cases in RESULT.md. No external or independent mathematical audit has been performed.
