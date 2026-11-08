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
# Reproducibility

The theorem is finite and algorithmically decidable. All three checkers are standalone, and the two exhaustive enumerators use distinct adjacency constructions. The complete state/transition list is `q4_flip_graph.tsv`, whose first column is a hexadecimal bitmask for the \(16\) edges of one Hamilton cycle out of \(32\) cube edges, and whose second column is a comma-separated list of its square-switch neighbors (hexadecimal masks).

Run `python3 check_faces.py` and compare with `check_faces.out`. Run `g++ -O2 -std=c++17 check_inversions.cpp -o check_inversions && ./check_inversions` and compare with `check_inversions.out`. Finally run `python3 verify_certificate.py` and compare with `verify_certificate.out`. The Python checkers require only the standard library. Use the working directory containing all packaged artifacts.

The face checker verifies enumeration, complete square-face switching, unique large component, radius, diameter, eccentricity counts, nine automorphism orbits and each orbit's neighbor-vector invariance. The C++ implementation separately produces the same counts using cyclic tour inversion. The certificate checker verifies each of the \(1344\) bitmasks is a Hamilton cycle, reconstructs all valid face switches, then repeats complete BFS distance calculations. A finite certificate does not establish any result for larger cube dimensions, and independent external validation remains unperformed.
