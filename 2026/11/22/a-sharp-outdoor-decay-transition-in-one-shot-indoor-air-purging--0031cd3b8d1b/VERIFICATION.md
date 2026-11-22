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

# Reproducibility and verification

The independent audit channel has not been performed. Analytic proof and parameter scope are in `RESULT.md`, with scientific review and qualified originality assessment in `REVIEW.md`. For numerical reproduction, run from this directory:

```sh
python3 check.py
```

The program requires Python 3 only. It integrates the piecewise scalar mass-balance solution independently of the closed saving formula, tests existence and uniqueness of the beneficial optimum over many parameters, checks strict interior placement, rate and horizon asymptotics, the exact equal-rate identity, and onset expansions. It printed `PASS 108524 numerical assertions` in the reported check. Finite numerical tests are not a proof of the universal quantifiers; the exact proof is algebraic, analytic and asymptotic. The computations do not establish physical model adequacy, historical novelty or independent mathematical validation.
