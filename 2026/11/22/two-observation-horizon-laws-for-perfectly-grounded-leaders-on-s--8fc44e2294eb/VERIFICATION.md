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

Use Python 3 with NumPy installed. Place `verify.py` alongside this file and run:

```bash
python3 verify.py
```

The computed output for the supplied code is:

```text
VERIFIED 21043 matrix, transient, and stationary comparisons
```

The program builds grounded Laplacians from the original star adjacency; compares their actual numerical eigenvalues with the analytic spectra for every integer \(2\le m\le32\) and exact budget \(1\le k\le m\); checks both heat-trace and integrated-trace formulas at seven positive horizons; brackets both kinds of transition; verifies their relative order and the persistent-sign regimes; and rechecks the exact stationary difference through \(m=59\). The symbolic spectrum, full uniqueness proof, exact budget boundary, and asymptotic convergence are derived in `RESULT.md`, and are not inferred from finitely many tests.

The substantive modeling restrictions are unit-conductance spokes, perfect leaders, a full original-degree grounded Laplacian, unit-isotropic follower white noise, zero initial covariance, and real positive finite time. The package does not claim any independent audit, general-graph extension, or exhaustive publication search.
