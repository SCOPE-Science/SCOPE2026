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

# Reproducibility and scope

Run `python3 CHECK.py` using Python 3 standard libraries. The program uses exact integer arithmetic. It verifies the matrix identity, four decisive binomial coefficient triples, recurrence orbit returns, exact distinct-value images modulo every \(2^k\) from \(k=1\) through \(k=12\), and all four normalized isometry branches at finite depths through eight. Expected terminal line: `CHECK_OK; exact matrices, four isometry branches, finite images through 2^12`.

The infinite proof is in RESULT.md. Computational enumeration cannot certify all levels, and no independent review has been performed.
