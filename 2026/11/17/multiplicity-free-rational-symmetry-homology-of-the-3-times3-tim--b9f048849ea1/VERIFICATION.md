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
# Exact verification instructions and limitations

Run `python3 verify_equivariant_334.py` in a Python 3 standard-library environment. The checker reconstructs all \(30,992\) augmented faces and \(178,704\) cover incidences, verifies an acyclic matching leaving \(96\) four-vertex critical faces, computes the rational Lefschetz character on all \(9\times5=45\) conjugacy classes in two independent integer combinatorial ways, and performs exact 45 irreducible-character inner products. The run completed successfully and printed:

```
MORSE {'faces_including_empty': 30992, 'matching_pairs': 15448, 'critical_faces_of_size_four': 96, 'directed_covers': 178704, 'acyclic': True}
CHARACTER_ROWS [[96, 14, 4, 0, 4], [0, 6, 12, 0, 0], [6, 2, -2, 0, -2], [12, 2, 0, 0, 0], [0, 0, 0, 0, 0], [-3, -1, 1, 0, 1], [-30, -4, -2, 0, -2], [0, -2, -4, 0, 0], [-3, -1, 1, 0, 1]]
VERIFIED_FULL_334_SYMMETRY_CHARACTER
```

The Python executable uses only exact integer and bitset operations for the mathematical checks. No other data file, external resource, cached intermediate calculation or private path is required. Finite exhaustive verification concerns only this precise 36-point complex. Quotient rational acyclicity uses the standard finite-group rational transfer argument; the program does **not** calculate integral homology of the orbit quotient. No independent external audit has been performed.
