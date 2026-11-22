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

# Verification of the dual homotopy calculation

The self-contained file `CHECK.py` is executable with a standard Python 3 interpreter and no dependencies. Its output in `CHECK_OUTPUT.txt` comes from running the enclosed file, not from a previously saved calculation.

The program exhaustively classifies all connected induced quadruples in \(H(3,3)\), then all higher dual faces by codimension-one membership. It confirms the face cardinalities \((27,351,2925,1593,324,54,0)\), constructs all 1,877 matched pairs and checks all 17,793 oriented Hasse cover relations for acyclicity. The critical cells are one 0-cell, 1,398 2-cells and 121 3-cells.

Exact signed gradient-boundary recursion produces a 1,398-by-121 integer Morse matrix with 264 nonzero entries. Fraction-based rank elimination gives 12, and integer Bareiss elimination on the specific 12-by-12 minor in `RESULT.md` gives determinant \(-1\). Therefore all nonzero Smith invariants are units; the calculation is not merely over a finite field. The raw uncollapsed simplicial complex is independently checked over \(\mathbb F_2\), with boundary ranks \((26,325,1214,270,54)\), agreeing with the resulting integral ranks. Direct Euler-characteristic agreement provides an additional test.

To replay: place `CHECK.py` in the working directory and execute `python3 CHECK.py`. Compare stdout to `CHECK_OUTPUT.txt`. No external computations or hidden input files are required. This checks the exact finite numerical certificate; the passage to homotopy uses the standard acyclic-matching theorem, the integer degree classification of maps to wedges of 2-spheres, and combinatorial Alexander duality. Independent validation has not been performed.
