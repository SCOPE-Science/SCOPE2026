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

# Verification of rational trace enumerators

The all-length proof is in `RESULT.md`. Run `python3 checker.py` with Python 3's standard library; no external datasets or packages are required. The program independently compares direct original-word trace signatures, gap-condition enumeration, and integer recurrences from the two formal generating functions. It prints `PASS` only if all comparisons hold.

The mathematical premise that trace classes have unique projected-word-and-marker-count coordinates follows directly from the specified commutation relation, not from numerical experiments. The closed-walk eigenvalue calculation supplies the circular weighted enumerator. The nonregularity proof uses intersections with a two-letter regular language and is not a software result.

Computational comparisons check a finite range; they do not prove the generating-function identities for arbitrary word lengths or alphabet sizes. Historical priority and external independent validation remain unresolved.
