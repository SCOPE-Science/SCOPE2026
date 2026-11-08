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

## Reproducibility
Install dependencies from `requirements.txt` and run `python VERIFY.py`. The script constructs the exact Hermitian sixteen-equation correlation system, differentiates its analytic solution, verifies the displayed rational identity by exact symbolic cancellation, verifies coefficient positivity, and cross-checks against an independently constructed complete four-spin Lindblad steady state. All checks passed when run on the embedded script.

The independent full-spin calculations sample finitely many parameter values and therefore serve only as normalization diagnostics; the general right-derivative formula and the unique threshold follow from exact elimination and the algebraic positivity proof. This does not establish any global optimum in finite dephasing, or a unique maximizer of the threshold in contact strength. No external independent audit has been performed.
