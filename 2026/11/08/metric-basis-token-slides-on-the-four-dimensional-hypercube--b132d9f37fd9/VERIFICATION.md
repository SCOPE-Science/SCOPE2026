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

The exact C++17 and Python 3 sources are included at `verification/check_direct.cpp` and `verification/check_signed.py`, with their actual standard outputs in the matching `_output.txt` files. Both were compiled or executed from the standalone attached source files without third-party dependencies. The C++ program examines all 560 three-subsets and 1820 four-subsets, directly compares every profile, enumerates every legal single-bit landmark slide, checks edge symmetry, and performs exhaustive breadth-first searches from all 928 configurations. The Python program independently checks the 80 nonzero signed displacement vectors, verifies the determinant equivalence over all 1820 four-subsets, enumerates the full bit-translation/coordinate-permutation symmetry action, and checks all orbit eccentricities. Both passed assertions for state and edge counts, connectivity, degrees, radius and diameter. The eight orbit representatives, populations, degrees and eccentricities are in the Python output. All computations are exact integer calculations. This is finite exhaustive verification, not a proof of any higher-dimensional statement.
