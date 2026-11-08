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

# Computational verification and limits

Run `python verify.py` with Python 3 standard library. The program constructs the triangular graph from all two-element subsets of \([n]\), detects the three forbidden induced four-vertex configurations by their degree sequences, enumerates all admissible subsets by exact hereditary recursion, and tests every omitted vertex for an admissible extension. It independently evaluates the closed coefficient formula.

Actual execution on the supplied program:

```
n 3 eligible 8 maximal 1 size_counts [(3, 1)] forbidden_foursets 0
n 4 eligible 54 maximal 12 size_counts [(4, 12)] forbidden_foursets 3
n 5 eligible 341 maximal 40 size_counts [(4, 10), (5, 30)] forbidden_foursets 75
n 6 eligible 1992 maximal 240 size_counts [(5, 180), (6, 60)] forbidden_foursets 495
n 7 eligible 11166 maximal 840 size_counts [(5, 105), (6, 630), (7, 105)] forbidden_foursets 1995
n 8 eligible 60972 maximal 4368 size_counts [(6, 2520), (7, 1680), (8, 168)] forbidden_foursets 6090
VERIFY_OK n=3..8 eligible_sets=74533 maximal_sets=5501 formula_equality=true
```

A threshold graph cannot contain an induced \(P_4\), \(C_4\), or \(2K_2\); because this property is hereditary, a forbidden partial selection can be pruned without excluding any admissible extension. Therefore the listed search is exhaustive for these six orders. This is a finite cross-check and not an infinite certificate; the mathematical argument for all larger orders appears in `RESULT.md`. No external or independent audit was performed.
