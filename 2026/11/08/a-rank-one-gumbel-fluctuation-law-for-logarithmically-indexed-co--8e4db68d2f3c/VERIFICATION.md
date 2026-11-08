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

# Verification and reproducibility

The theorem has an analytic, infinite-parameter proof in `RESULT.md`; the finite checker is an independent consistency test, not a certification of the functional limit or publication priority.

Run the standalone file with `python verification_check.py` in the same directory as these documents. The checker requires only Python 3.10 or later and the standard library. On the package assembled here it printed:

```
PASS: 87 exact/numerical assertions; finite-size diagnostic MAE=0.057100
Limitation: numerical tests do not prove the functional limit or originality.
```

Its checks include exact rational finite-state Markov expectations for \(2\le N\le4\) and \(2\le j\le6\) versus independent alternating-subset formulae, polynomial derivative identities for Poisson CDFs, finite local Poisson approximations, and an independent seeded continuous-time coupon simulation. The empirical-process bound uses the standard Dvoretzky–Kiefer–Wolfowitz inequality, not a finite enumeration. The maximum-first-arrival law and exponential spacing identity give the required Gumbel limit and uniform fourth moments. The compensated total-Poisson martingale yields the exact second-moment transfer bound \(\mathbb E[(T_N/N-C_N)^2]=H_N/N\); these analytical components are indispensable.

Not established: historical uniqueness, an independent mathematical audit, a second-order fluctuation theory, nonuniform coupon distributions, or uniformity in growing \(x\)-windows.
