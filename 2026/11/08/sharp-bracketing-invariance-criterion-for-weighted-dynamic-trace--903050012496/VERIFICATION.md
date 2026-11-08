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

Execute `python3 nmatrix_trace_checker.py` from the same directory as this document. The program uses only the Python 3 standard library and independently enumerates legal outputs of the explicit three-valued truth table.

The completed execution produced `All checks passed: 29537`. It checked every full binary tree through five leaves using an independent direct history enumerator; all tree shapes through seven leaves for equal true/error weights in a finite integer grid; both deterministic boundary faces through seven leaves; 125 four-leaf weight triples against direct enumeration and the exact polynomial defect; 19,683 tests of the general three-vector associator; and every one of the 27 possible input triples for ordinary set-hyperassociativity. In the unit-weight case the first seven root-count vectors were `(1,1,1)`, `(1,5,5)`, `(1,21,21)`, `(1,85,85)`, `(1,341,341)`, `(1,1365,1365)`, `(1,5461,5461)`. The four-leaf balanced-minus-comb result at weights `(1,2,3)` was `-6`.

The unrestricted statements are proved algebraically in `RESULT.md`; these finite checks do not certify unbounded cases by enumeration. In particular, a failure of an algorithm is never used as evidence of impossibility. The code assumes no unprovided data or external services.
