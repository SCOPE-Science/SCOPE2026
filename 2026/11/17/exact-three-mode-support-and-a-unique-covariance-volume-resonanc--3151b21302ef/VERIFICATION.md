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

# Verification and scope

The exact symbolic checker `check_covariance.py` is included and needs Python plus SymPy. It reconstructs the complete rational covariance matrix, its determinant, the critical derivative, the support-gap factorization and the exact section-volume integral. It also tests positive definiteness for six rational positive switching rates and support-gap signs at rational sections.

Reproduction: `python check_covariance.py`.

Observed replay: `THREE_MODE_TELEGRAPH_EXACT_OK determinant=1 derivative=1 support=1 volume=1 rational_cases=6`.

The uniqueness of the optimum is proved using one sign change in the quartic and the intermediate-value theorem, not inferred from sampling. The topological-support reverse inclusion relies on positive-probability approximation by finite switching histories and is proved in the main result, not delegated to this script. The proof concerns closed reachable supports and does not certify smoothness or global optimization for other decay spectra. No independent external validation was performed.
