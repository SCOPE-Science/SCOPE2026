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

Run `python3 verify.py` with a standard Python 3 interpreter. The script depends only on `math` and `random` from the standard library; no network, external datasets, or third-party modules are required. In the checked environment its output was:

```text
PASS 31536 numerical comparisons; example optimal time: 1.954697195672 exposure benefit: 0.235189905680
```

The checker evaluates 500 randomized positive parameter triples, examines 61 grid points for each resulting finite-horizon benefit and compares nearby times; for 30 cases it integrates the full three-variable state/exposure ODE with RK4 before and after instantaneous cleaning and compares the result to the matrix-exponential benefit. It also verifies modal-rate invariance under three different coefficient triples, short-horizon and long-horizon approximations, and the reproducible 12-hour illustration. Exact universal validity rests on the analytical proof in `RESULT.md`, not on a finite set of numerical trials. The RK4 comparisons have finite discretization error, and the grid checks cannot rule out critical points between grid locations without the strict-concavity proof. Independent third-party proof audit and field validation have not been performed.
