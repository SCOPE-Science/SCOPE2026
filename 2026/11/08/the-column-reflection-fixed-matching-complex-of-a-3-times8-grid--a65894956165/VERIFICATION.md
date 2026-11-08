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

# Executable finite certificate

Run `python3 verify.py` (Python standard library). The program reconstructs the \(3\times8\) grid, its column involution and every edge orbit; builds a separate \(3\times4\) grid with one pendant edge on each of three boundary vertices; compares all 190 pairs of orbit vertices. It then enumerates the full augmented matching-complex face poset and creates deterministic pairs using the 20-element pivot order printed in RESULT.md. Full Hasse-direction topological sorting verifies acyclicity, leaving the critical 0/4-cell pattern that proves the integral homotopy type by discrete Morse theory.

Independent mod-two boundary-matrix ranks corroborate the four-dimensional rank four and vanishing otherwise. The recorded verifier output is `verification_output.txt`. The proofs of the geometric fixed-point triangulation and the Morse consequence are in RESULT.md. No external independent audit has been conducted. The primary 2026 preprint's full text could not be inspected, so an unindexed overlap remains possible.
