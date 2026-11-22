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

Run `python3 check.py` with Python 3 standard-library support only. Compile and run the separate C++ program with `g++ -std=c++17 -O2 -Wall check.cpp -o check && ./check`. Both calculate the exact minimum ordinary dominating sets and full shattered-support distribution; the Python implementation separately computes the derived Cayley triangles and translated trace witnesses. The recorded output files are `python_output.txt` and `cpp_output.txt`.

The universe has exactly sixteen vertices; enumeration of all 65536 vertex subsets is exhaustive for this fixed graph, not an extrapolation. Python's finite-field boundary rank is a consistency check only. The integral homotopy identification is proven by the explicit quotient of the triangular tessellation in `RESULT.md`. Independent mathematical audit is not part of this verification.
