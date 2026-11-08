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

# Reproducibility

Use Python 3.10+ with standard library only:

```sh
python verify.py
```

The exact finite checks enumerate independent bond configurations and every uniform infection origin, independently of the analytical formula, for all small paths within the script's limits. Further exact rational checks compare the complete placement enumeration with the greedy allocation by gap marginals, including strict and tied endpoint cases. At packaging the script reported `PASS: 6546 assertions/diagnostics`.

# What the checks establish

The exact enumerations establish agreement for the tested finite path sizes and probabilities; they do not constitute an infinite proof. The universal statements, including uniqueness of the nontrivial threshold and its quadratic asymptotic, are established by the explicit analytical argument in RESULT.md. Numerical bisection diagnoses, but does not prove, the large-parameter asymptotic.

# Unverified extensions

No model with heterogeneous, directed, time-dependent or correlated edge transmission is covered. No external or independent verification has been performed.
