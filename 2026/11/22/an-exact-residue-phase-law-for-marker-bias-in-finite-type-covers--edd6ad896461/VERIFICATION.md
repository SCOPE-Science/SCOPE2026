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

# Reproducibility and limits

`check.py` is a standalone standard-library Python program. Execute `python check.py` and compare its final line with `check_output.txt`. Its 125-digit Decimal computations implement the renewal series in closed rational form for eventually periodic sets, solve both limiting and cover roots by bisection, test exact local language membership against an independently specified finite-state presentation, and compare graph Perron roots and asymptotic coefficients. Five nontrivial periodic sets are examined.

An asymptotic theorem over all eventually periodic sets requires the analytic Taylor estimates in `RESULT.md`; the finite checks do not establish infinite quantifiers. The historical literature comparison is limited to the sources expressly named in `RESULT.md` and `AUDIT.json`. Independent audit has not been performed.
