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

# Reproduction and limits

The standalone program `check.py` uses only Python 3 standard-library `fractions` and `math`. Running `python3 check.py` returned:

```
VERIFY_OK exact_rational_orbit_checks=2300 integer_parameters=23
return_probabilities, mean, variance: exact rational checks
entropy_formula: finite numerical cross-check
```

The checker reconstructs the original planar dynamics and evaluates four rational interior points on each of the \(2d-1\) branches for every \(2\le d\le24\); it checks roof weights and moment formulas in exact rational arithmetic and compares the entropy result to numerical evaluation. These are finite corroborations only. The complete proof uses affine identities valid for every integer \(d\ge2\), full-branch Bernoulli coding, Abramov's formula, and the renewal counting CLT. An independent scientific audit has not been performed.
