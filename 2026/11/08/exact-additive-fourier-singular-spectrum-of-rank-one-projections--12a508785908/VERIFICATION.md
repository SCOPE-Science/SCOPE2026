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

The exact cyclotomic checker in `CHECK.py` performs exhaustive frequency checks over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_9\). It independently evaluates character-count vectors of the defining idempotent sum and compares them with the rational-eigenline prediction. For each field it verifies the singular strata and rank against the derived closed multiplicity formulas. The script requires only Python 3's standard library.

The universal statements instead follow from the exact eigenline transform, rational similarity-class classification and trace-fibre counting in `RESULT.md`. No external certification or independent validation has been performed.
