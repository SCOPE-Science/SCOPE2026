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

The included `verify_duads.py` and `verify_symplectic.cpp` both executed successfully. Their exact recorded outputs are included as `duad_results.txt` and `symplectic_results.txt`. The Python program enumerates and checks the ten symmetry orbits; the C++ program independently performs shortest-path enumeration from every one of 6,540 optimum configurations using a second incidence representation. All twenty counts in the ten-level locality-excess comparison (two programs times ten levels), together with minimum size, optimum count, movement-edge totals, degree distributions and eccentricity distributions, agree exactly.

The proof is an exhaustive finite computation over all candidate subsets of cardinalities zero through four, with bounded observation propagation and shortest-path BFS on an explicitly constructed finite adjacency graph. A 13-move geodesic is printed with its endpoint labels; minimality is verified by exact BFS. These computations do not prove analogous statements for any other graph and are not independent mathematical audit.

Reproduction:

```sh
python3 verify_duads.py
c++ -O3 -std=c++17 verify_symplectic.cpp -o verify_symplectic
./verify_symplectic
```
