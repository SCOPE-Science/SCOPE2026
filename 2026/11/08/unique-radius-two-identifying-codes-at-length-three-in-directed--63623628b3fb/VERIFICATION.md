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

# Reproducibility checks

The finite tests are standalone Python 3 programs using only the standard library. Run `python3 checks/verify_outballs.py` and `python3 checks/verify_inballs.py` from the extracted package root. The corresponding recorded stdout is in `checks/outballs_output.txt` and `checks/inballs_output.txt`.

The outgoing verifier constructs all vertices and outgoing arcs, computes distance-at-most-two balls by BFS expansion, and checks unique identifying signatures for \(3\le q\le9\). It separately checks the singleton symmetric difference that forces every endpoint-different word into every code. In the binary case it exhaustively enumerates all 256 subsets and confirms exactly two seven-word optimal codes.

The incoming verifier independently generates all predecessor arcs and full predecessor radius-two balls, checks the same unique signatures for \(3\le q\le7\), and verifies every forced-witness symmetric difference.

These tests verify finite cases, code orientation, and the exceptional boundary. They are not exhaustive over unbounded alphabet size; the written argument in `RESULT.md` proves the universal statement. Reproducibility does not constitute independent scholarly validation.
