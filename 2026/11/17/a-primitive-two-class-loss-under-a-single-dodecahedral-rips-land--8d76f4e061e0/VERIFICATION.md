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

# Verification steps and limitations

The `verification.py` file uses only Python 3 standard-library facilities, with integer graph distances and bit-mask faces. Run `python3 verification.py`. It enumerates the exact dodecahedral graph via the generalized Petersen model, certifies rotation and an explicit outer-to-inner automorphism, checks every pairwise graph distance, generates all three face sets, and checks three complete acyclic discrete-Morse matchings by exhausting every Hasse cover and topologically sorting all directed arrows. The output matches `verification_output.txt`.

Only one deletion representative is enumerated, because the two explicitly verified graph automorphisms make the action vertex transitive. The reported complex is the induced subcomplex using the original distances; no distance recomputation is made after deleting the point. Finite exhaustive verification proves this fixed finite graph calculation, not any generalization to arbitrary spaces. The integral inclusion conclusion comes from the written long exact sequence, not a mod-prime numerical experiment.
