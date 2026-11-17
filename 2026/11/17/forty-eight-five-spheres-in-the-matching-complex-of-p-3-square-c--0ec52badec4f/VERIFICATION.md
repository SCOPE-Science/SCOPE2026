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

# Executable verification

From the extracted package root with Python 3 and SymPy (version specified in `proof/requirements.txt`), execute:

```text
python3 proof/verify_cylinder.py proof/morse_boundary_58x10.csv
```

The script constructs the 18-vertex/30-edge graph, enumerates every matching, checks its complete 57,535-face census, constructs the deterministic 28,733-pair gradient matching, and checks acyclicity by a topological sort of 318,474 directed Hasse incidences. It independently computes the original mod-two simplicial boundary ranks for cardinalities two through nine. It calculates all signed Morse gradient paths in degree five and verifies the complete 58-by-10 boundary against the embedded CSV. Exact SymPy integer Smith reduction returns ten unit factors. The JSON result must match `proof/verification_output.json`, including its `CYLINDER_3X6_MATCHING_EXACT_PASS` status.

The original face-poset counts and global acyclicity certificate are exhaustive for this finite graph. They do not imply an infinite family. The mod-two check corroborates ranks only; the integral classification uses Smith reduction and the homotopy meaning of the attaching maps.

The stored CSV is determined by the sorted graph-edge order, sorted critical face masks and critical six-cell order specified in the executable. The SHA-256 of its canonical compact JSON array of integers is `21a50aeefce77d5459b5448290216fb593395e4fab14aba6b7d64317aff6c4ea`.

No independent mathematical audit or external certification is asserted.
