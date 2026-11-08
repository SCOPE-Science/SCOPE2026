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

Two explicit hexadecimal feedback selectors in `witnesses.tsv` define the two codebooks. Run `python3 check_formula.py`; compile `check_graph.cpp` with a standard C++17 compiler and run it from the same directory. Both checks have been executed on the packaged inputs and reported the full 128 and 512 unique, nonempty signatures. The two independent calculations are: algebraic enumeration of all incoming paths of lengths zero through \(t\), and reverse breadth-first search in a directly constructed directed graph.

The lower bound is a separate mathematical argument: one sensor is needed from every pair of words sharing a prefix of length \(n-1\). The scripts check attaining upper bounds, and do not replace or assume that lower-bound proof. All finite loops are exhaustive over the asserted graph sizes and terminate; nothing is inferred for untested radii or alphabets. No independent third-party scientific audit was performed.
