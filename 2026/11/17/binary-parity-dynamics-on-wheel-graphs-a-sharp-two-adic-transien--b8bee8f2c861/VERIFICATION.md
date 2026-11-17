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

# Verification record

The exact all-size proof is in `RESULT.md`. Two separate executable verifiers use only the Python standard library.

`python3 verify_wheel.py` computes GF(2) wheel adjacency powers and ranks through rim size 32 and independently enumerates actual temporal trajectories for selected small rims.

`python3 verify_direct_wheel.py` implements the local XOR rule directly, without reusing the rank routine, and exhaustively enumerates the first periodic-entry time for all configurations of every wheel with 3 through 11 rim vertices.

The captured reproducible outputs are `verification/rank_and_enumeration.txt` and `verification/direct_enumeration.txt`; both end in an explicit passed check. The only claim made for experiments is finite-size corroboration. In particular no exhaustive enumeration of every rim size, independent external certification, or exact census of temporal cycle lengths is asserted.
