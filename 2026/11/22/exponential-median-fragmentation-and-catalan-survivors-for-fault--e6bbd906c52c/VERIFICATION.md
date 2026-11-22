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

# Verification evidence and boundaries

`verify_exhaustive.py` exhaustively tests 918 bounded grid/fault instances and checks 360652 ordered connected-route distances by explicit graph search. In each instance it verifies the independent sign-fiber partition, interval boundaries and shortest-distance identity.

`verify_diagonal.py` uses a different dynamic-programming representation to check the exact Catalan survivor counts through twelve blocked-diagonal sites, and checks all 1024 independently chosen signatures in the ten-site construction.

The infinite theorem is established by the proofs in `RESULT.md` (sign invariance, lattice interval closure, ideal toggle geodesics, explicit signature witnesses, and Catalan generating functions). The programs are finite reproducibility checks, not a computer-assisted substitute for the arbitrary-grid or arbitrary-fault proofs. No external audit or certification has been performed.
