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

The exact local and symbolic calculations are implemented in `verify.py` using Python's standard library only. Command: `python3 verify.py`; observed output begins `VERIFY_OK`.

The script checks the four five-bit mismatches between a word and the composition of the two traffic maps, the forbidden-output four-edge matrix identity, and an exact symbolic determinant identity for the eight-state cyclic transfer matrix. It also exhaustively verifies the image characterization and full density coefficient table for every ring length from one to sixteen, inclusive. These finite enumerations complement rather than replace the all-length proof in `RESULT.md`.

No external independent mathematical audit has been undertaken. The full text of the closely relevant 2004 traffic de Bruijn study was unavailable, so its detailed priority implications remain uncertain.
