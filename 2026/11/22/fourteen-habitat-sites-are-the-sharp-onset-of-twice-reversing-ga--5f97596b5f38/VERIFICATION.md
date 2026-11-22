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

Execute `python3 check_gate_reversals.py` with Python 3 (no dependencies). It prints the exact integer pair count \(3056\), the witness network size \(14\), and `VERIFY_OK`. The checker verifies all ordered-composition profiles up to total size 13, all transformed binomial coefficients and their sign changes, and an independently rebuilt directed witness. The exact proof also requires the stated uniqueness-of-directed-path reduction and Descartes' rule; numerical tests would not replace either argument.

# Scope and limits

Exact finite exclusion is for two root gateway choices on directed trees with a fixed occupied source. The witness factorization proves two interior reversals and no additional ones for that witness. The code does not exhaust all possible 14-vertex trees, nor model realistic dispersal. The completeness claim depends on the mathematical bijection between nonempty depth profiles and ordered compositions, proved in `RESULT.md`. No external independent audit has been performed.
