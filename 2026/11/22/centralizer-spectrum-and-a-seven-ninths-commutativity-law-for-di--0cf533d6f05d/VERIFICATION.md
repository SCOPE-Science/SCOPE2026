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

# Reproduction and limitations

Run `python3 checker.py` using Python 3.9 or later; no third-party packages are needed. The script constructs the five-element transformation model, enumerates its two normal-form families for five positive leaf counts, and compares every element's predicted centralizer size against an independently computed multiplication table. It prints the stored `checker_output.txt` lines on success. The finite-domain checks do not prove the claims for all positive leaf counts; the inductive normal-form and commuting-table arguments in `RESULT.md` supply the general proof. No external independent validation has been performed.
