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
# Reproducibility and verification

The exact domain is the 32768 possible 15-edge frequency masks of the six-vertex complete graph. The first checker evaluates the forest indicator with disjoint-set union and a full integer Walsh-Hadamard transform. The second recognizes forests using DFS back-edge detection, evaluates the signed sum directly for all 32768 frequencies, and calculates the Fourier projection norm by direct sums over 156 six-vertex graph isomorphism orbits.

Run `python3 verify_walsh.py`, compile `g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct`, and run `./verify_direct` from the directory containing the source files. Both must report success, and their `SIGNED_LEVELS=` lines must match (ignoring an optional trailing semicolon). The scripts use only standard Python/C++ facilities and exact integer arithmetic.

Checks established: 2932 forest masks; complete 49-value signed spectrum; 3105 Fourier zeros in ten vertex-relabeling orbits; zero support distribution 180,1080,1800,45 at support 5,7,9,11; positive multiplier gcd and gap both 4; Parseval sum of squares 96075776; Fourier projection integer numerator 1210058 and reduced endpoint norm 605029/16384. On n=3,4,5, all coefficients are nonzero.

These are exhaustive finite computations supporting a mathematical derivation of each operator invariant, not a proof for larger vertex orders or an independently performed audit. Search coverage and historical-priority uncertainty are discussed in `REVIEW.md`.
