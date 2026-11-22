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

# Reproducible checks and limits

Run `python3 verify.py` with standard Python 3. The script recomputes the two-node kernel Gram projection and the diagonal closed formula exactly for selected rational sample points and dimensions; it also checks the one-axis tensor factorization and sharp known axis configuration. It reports 379 exact rational identities and 150 numerical root and monotonicity spot checks.

The general all-dimension assertions are proved by the explicit strict-convexity and derivative arguments in `RESULT.md`. The script does not establish novelty, prove exhaustiveness for a continuum of nodes, or replace the proof. The global optimum over all unrestricted two-node designs is not addressed. No independent audit has been performed.
