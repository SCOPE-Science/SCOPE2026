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

# Reproducibility and limits

The exact scripts `verify_peo.cpp` and `verify_cycles.py` use different definitions of chordality (successive simplicial deletion versus explicit induced-cycle exclusion). Both enumerate the complete binary graph cubes. The C++ program uses an exact integer Walsh–Hadamard transform; the Python program computes signed sums of all 34 five-vertex orbit representatives directly. The accompanying CSV tables give the 34 signed orbit counts and the six-vertex edge-count histogram.

Run `g++ -O2 -std=c++17 verify_peo.cpp -o verify_peo`, followed by `./verify_peo 5`, `./verify_peo 6`, and `python3 verify_cycles.py`. In the checked output, the count of chordal graphs is 822 at five vertices and 18154 at six; the five-vertex Walsh zero count is 120, and the six-vertex count is zero. The sharp six-vertex witness has mask 639 and signed value 2. Parseval totals are respectively 841728 and 594870272.

The computations are exhaustive for the stated finite orders only. The modulus-four argument is exact for all six-vertex frequencies. No unverified larger-order inference or independent external validation is claimed.
