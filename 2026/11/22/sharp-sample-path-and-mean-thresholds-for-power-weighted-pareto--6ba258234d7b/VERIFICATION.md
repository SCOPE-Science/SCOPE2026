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

# Verification

The mathematical assertions are established by exact Pareto density integration, Tonelli's theorem, explicit local asymptotics at the singular boundary, and a separable-Hilbert central limit theorem. The computation `check.py` (Python standard library) was executed on the packaged contents and passed 83 checks: 36 exact rational comparisons, seven independent numerical quadrature comparisons, 30 density-to-truncated-moment comparisons, and 10 variance-positivity checks. An analytical proof is required for the uncountable parameter ranges; the computational checks are corroborative only.

The null has known Pareto shape and unit lower endpoint. No independent audit or experimental corroboration of statistical power has been performed. No claim of completeness against every earlier article is made.
