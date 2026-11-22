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

# Reproduction

The C++17 source `quotient.cpp` constructs the labeled Möbius–Kantor graph, independently exhausts its 96 adjacency-preserving permutations, enumerates 1,090 nonempty independent faces, and canonicalizes every strict face chain under the full group. Its 24,875 regular orbit cells are tested for unique maximal cofaces before each of 12,114 elementary collapses. It writes the actual pair certificate to `quotient_certificate.txt` and the remaining exact signed boundaries to `residual_cells.txt`.

Run in a directory with all provided files:

```
g++ -std=c++17 -O3 quotient.cpp -o quotient
./quotient quotient_certificate.txt
python3 fundamental_group.py
python3 homology.py
```

The last command needs SymPy; the other Python command uses the standard library. The expected success signatures are `MK_ORBIT_CELL_COLLAPSE_OK`, `MK_FUNDAMENTAL_GROUP_OK`, and `MK_INTEGRAL_HOMOLOGY_OK`. The remaining cell counts are (14,83,214,240,96) in dimensions zero through four. The exact boundary ranks are (13,70,144,96), with a single nonunit Smith factor two in the fourth boundary. The 70 one-skeleton generators are all killed by the triangular relators.

All computations are integer or exact finite enumeration. Neither a finite test of different graphs nor an external expert audit is claimed. The chain and group calculations concern the explicit ordinary orbit complex, not a homotopy quotient. The certificate is independently reproducible by its source; its mere presence is not treated as an argument without the checks and derivation given in `RESULT.md`.
