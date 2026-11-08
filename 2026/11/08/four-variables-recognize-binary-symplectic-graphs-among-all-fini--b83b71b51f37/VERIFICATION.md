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

The theorem is proved in `RESULT.md` by algebraic reconstruction and an unrestricted three-pebble game. Run `python3 verify.py` using Python 3 and its standard library; the output must match `verify_output.txt` byte for byte. The program constructs three binary symplectic graphs, independently applies the cited explicit switch, checks its parameters, binary rank, failure of row closure and all two-fixed-vertex extension patterns, and exhaustively checks every labelled simple graph of orders one through five. Finite checks do not prove the universal theorem or any assertion of infinite game length. Independent mathematical audit is not performed.
