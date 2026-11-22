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

Run `python3 verify.py` in a directory containing the included file, with Python 3.10 or later. The checker constructs inversion edges from permutation positions, tests two-connectivity by deleting each vertex, and compares the extremal permutations directly against the classified insertion family.

Observed verification results: exact exhaustive tests at odd orders \(3,5,7,9\) give respectively \(1,4,7,10\) extremizers, with \(1,2,3,4\) triangle-containing cases. Even-order uniqueness at \(4,6,8\) passed independently. All degree-two insertion cells, class sizes, triangle counts, and exceptional commutation identities passed for even ladder orders \(4,6,\ldots,50\). The program terminated with `VERIFY_OK`.

# Scope of the evidence

Exhaustive tests prove only their finite ranges. The unrestricted classification follows from the analytical anchored-ear induction and the symbolic insertion-cell calculation in RESULT.md, using the cited published general lemmas. The historical novelty comparison is necessarily provisional.
