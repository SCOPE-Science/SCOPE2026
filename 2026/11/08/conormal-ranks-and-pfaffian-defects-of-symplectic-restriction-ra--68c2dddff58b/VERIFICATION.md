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
# Verification scope

Use `python3 verify.py` to replay the packaged exact-arithmetic consistency tests. The program checks conormal-composition rank preservation for explicit surjective pairings, alternating block ranks, determinant/Pfaffian identities, and the Hilbert numerator degree identity in finite sizes. The general result requires the geometric local normal-slice proof, the rank-stratum dimension calculation, and the classical codimension-three Pfaffian free resolution stated in RESULT.md. Neither numeric tests nor citations constitute an independent mathematical audit.
