---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

The proof computes the full order of each principal-unit group and the cardinality of its image under the p-th power map, and proves that the p²-th power map is trivial. These three facts determine the abstract p-group. The top standard monomial determines the Loewy lengths. The argument does not depend on a finite experiment or on a general monomial unit-group theorem.

The supporting Python 3 script `verify_units.py` includes finite illustrations for the pairs. In particular its coefficient-support check in characteristic three gives counts 1, 59048, 118098 for units of orders 1, 3, 9 respectively in each principal-unit group. These are examples only; the proof covers every odd prime and extension degree.
