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

The standalone `verify.py` uses only Python's standard library. Run it from the same directory as the accompanying output file, with `python3 verify.py`, and compare its output with `verification-output.txt`.

The verifier exhaustively enumerates the exact graph and each face, independently checks the defining disconnected-triple criterion, and tests the entire reversed Hasse diagram for acyclicity. It reconstructs the signed integral Morse boundary and verifies both rank and the unit Smith-minor condition. It directly evaluates signed fixed-simplex Lefschetz sums for all seventy-eight affine automorphisms. All loops have explicit finite bounds; no random sampling or numerical approximation is used.

A successful run prints `VERIFY_OK`. The conclusions are finite exact statements about this graph, not generalizations to other Paley primes. An independent external audit has not been performed.
