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

The standalone `checker.py` replays the actual sampled Armijo comparisons in exact rational arithmetic for both correction signs and all validation strings of the indicated finite sizes. It compares the resulting counts with the closed binomial-tail formula; the checker also makes finite normal-tail spot checks.

The general theorem for arbitrary sample size is proved analytically by the two-point quadratic expansion, binomial counting, the central limit theorem, and Hoeffding concentration. Finite tests do not certify a limit or complete the infinite proof. Confidence-margin-corrected acceptance and multidimensional multilevel behavior are not tested.
