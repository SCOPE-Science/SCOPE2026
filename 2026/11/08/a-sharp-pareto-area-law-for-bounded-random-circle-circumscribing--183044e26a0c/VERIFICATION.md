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

# Reproducibility and boundaries

Run `python3 verify_tail.py` with Python 3.9 or later. Only standard-library modules are used. The script checks exact rational simplex-cap probabilities and analytic coefficient identities for \(3\le n\le12\). It then samples independently normalized exponential spacings (giving the uniform Dirichlet law) for \(n=3,4,6\), with 720,000 samples each and area threshold 160.

Actual execution output:

```
EXACT_OK n=3..12 Dirichlet simplex translated cap identity, strip coefficient, boundedness
SIMULATION_OK threshold=160 samples_per_n=720000 (n, bounded_fraction, t_joint_tail, exact_limit, exceedances)
[(3, 0.250312, 1.008444, 0.95493, 4538), (4, 0.500254, 0.952667, 0.95493, 4287), (6, 0.812099, 0.597556, 0.596831, 2689)]
```

The observed \(t\Pr(B_n,A_n>t)\) at finite threshold differs from its asymptotic value; this is expected and is not an estimate of a rigorous error term. Finite experiments, rational arithmetic on selected dimensions, and source searches cannot prove an all-dimensional/asymptotic claim or establish publication priority. The **analytic derivation** in `RESULT.md` proves the theorem for each fixed \(n\ge3\). No independent mathematical audit has been performed.
