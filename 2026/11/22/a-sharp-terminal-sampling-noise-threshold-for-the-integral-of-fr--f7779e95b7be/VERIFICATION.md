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

Run `python verify.py` after installing the versions specified in `requirements.txt`. The recorded replay succeeded on 18 November 2026 (UTC): exact SymPy differentiation and limits, exact rational inequalities, 25 independently integrated covariance comparisons, 6,307 supplementary endpoint-grid comparisons and 6 interior checks. Those calculations are not exhaustive continuous-domain proofs. The global claims follow from the analytical inequalities in `RESULT.md`; the code verifies their inputs and sample values only. A negative result of a finite numerical search would not establish global impossibility.

The result is a self-review, not an externally or independently audited theorem. Historical priority is uncertain, especially for inaccessible older sampling literature. No proof is supplied for a unique interior design below the stated threshold, or for sufficiency of the general-H necessary noise barrier.
