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

# Reproducible checks and scientific limits

Run `python3 verify_dodeca_robust4.py` using Python 3 with its standard library only. `verification_output.txt` records the actual successful output. The code reconstructs all graph edges, all 1,048,576 subsets and their clipped independence numbers, all 12,217 nonempty faces, all 6,031 Morse matching pairs, and all 57,940 nonempty Hasse covers. An exhaustive topological sort verifies global acyclicity with 12,217 visited nodes. The only unmatched nonempty faces are one vertex and 154 five-simplices, certifying the integral homotopy type through the discrete-Morse theorem.

The code also computes complete mod-two boundary ranks 19, 171, 969, 2,366, 2,266, 240 in degrees one through six, purely as a corroboration. A separate exact backtracking search produces all 120 adjacency-preserving automorphisms; signed fixed-simplex Lefschetz sums produce the complete rational trace table. An explicit commutation check recognizes the central involution, and averaging the traces confirms invariant dimension zero.

Checks apply to the defined 20-vertex dodecahedral graph only. No claim of a symbolic infinite-family proof or independent external validation is made. The finite acyclic matching, rather than a finite-field rank test, proves the integral wedge statement.
