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

# Reproduction of the finite verification

Two distinct exact exhaustive implementations are provided as `visibility_polynomial.py` and `visibility_direct.cpp`. The former builds the 4-point nonedge obstructions, checks every one of the 65,536 possible vertex subsets, and verifies both optimum symmetry orbits and the absence of single-vertex optimum exchanges. The latter constructs both adjacency matrices independently, uses breadth-first search to compare original and avoidance distances for every selected pair in every subset, and checks every polynomial coefficient. It does not call the obstruction method.

Commands from the directory containing the embedded files:

```
python3 visibility_polynomial.py
g++ -std=c++17 -O2 -Wall -Wextra visibility_direct.cpp -o visibility_direct
./visibility_direct
```

The exact terminal text from both executions is embedded as `EXACT_OUTPUT.txt`. The first program finishes in `VISIBILITY_EXACT_PY_OK`, and the second in `VISIBILITY_DIRECT_CPP_OK`. Each program compares complete coefficient vectors with the claims; the first also checks membership-bitstring hashes and symmetry orbit equality. The proof of the quartet reduction in `RESULT.md` proves that the first enumeration is exhaustive, while the second independently implements the original geodesic definition. No attempt to infer an infinite theorem from finite cases is made.

The group-orbit enumerations verify constructed automorphism families rather than presupposing the full automorphism groups. External mathematical auditing remains unperformed. Unindexed identical prior coefficient tables cannot be ruled out by a finite literature search.
