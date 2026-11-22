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

The package contains `verify.py`, runnable with `python3 verify.py` and no nonstandard dependencies. The included `verify-output.txt` reports 316 exact rational checks of the interior slope equations, rational-grid witnesses, reflection-symmetric feasibility endpoints and sharpness tests. The analytic proof in `RESULT.md` supplies the uncountable sign certificate for every positive data triple at contrast at most four and the strict mesh-optimality comparison for every positive symmetric mesh ratio. Sampling or finite checks alone do not prove that universal result. No independent validation has been performed.
