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

The included `verify_weighted_path.py` was run with Python 3, NumPy, and SciPy. It printed:

```
MATRIX_EXPONENTIAL_AND_LEAKAGE_PASS: 200
REAL_SIGNAL_BV_ERROR_BOUNDS_PASS: 4000
PHASE_TRANSITION_ASYMPTOTICS_PASS
r 0.25 crossing u 4.526327905993317
r 0.5 crossing u 2.1922782517260893
r 0.8 crossing u 1.0581218358273097
```

The checker independently computes the full four-by-four heat matrix using SciPy's matrix exponential and compares it with the two analytical cut expressions. It additionally samples real signals and checks the sharp global bound and its predicted winner. It tests both transition asymptotics in representative parameter regimes. These finite computations **are not** proof of the universal result. The analytic proof relies on a positive-convolution Laplace identity and strict log-concavity, which are proved in `RESULT.md`.

The source comparisons cover birth–death intertwining (Chafaï–Joulin, 2010 first public), birth–death spectral representations (Castro–Grünbaum, 2013), and a published weighted-four-path Lipschitz semigroup norm theorem. The result is limited to symmetric outer conductances on four vertices and does not establish priority over inaccessible sources.
