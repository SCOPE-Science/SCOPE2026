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

# Verification record

The statement follows from exact conditioning on opposite hemisphere signs, linear interpolation, Gaussian-normalization convergence, orthogonality of independent uniform directions and a two-branch half-Cauchy change of variables. All formulas and quantifiers are presented in `RESULT.md`; the numerical checker is supplementary.

From the package directory, install `requirements.txt` and run `python check.py`.

The actual check passed with the following diagnostics:

```
NORMALIZATION_AND_MOMENTS_OK [1.0000000000001061, 0.6366197723675813, 0.42441318157828145]
HALF_CAUCHY_TRANSFORM_CHECK_OK
THREE_DIMENSION_BASELINE_OK (0.49862853446289207, 0.33205863783720946, 0.6016533333333334, 0.8010933333333333, 0.50004)
HIGH_DIMENSION_CROSSING_DIAGNOSTICS_OK (0.6369108629644196, 0.4252856041212047, 0.5300736842105264, 0.8366210526315789, 0.1119157894736842)
SPHERICAL_CHORD_EQUATORIAL_LIMIT_CHECKS_OK
```

The theoretical limiting \(\mathbb E[Q]\) is \(2/\pi\), and the simulated dimension-500 mean was approximately \(0.636911\). The empirical dimension-500 probabilities at squared radii \(0.6\) and \(0.8\) were respectively \(0.530074\) and \(0.836621\), compared with limit values \(0.535441\) and \(0.839139\). The probability below squared radius \(1/2\) is not zero at finite dimensions (about \(0.112\) here), consistent with a slow boundary-layer approach; the proof only states that this probability tends to zero. The dimension-three baseline also matches the familiar disk-uniform law.

Checks use seeded random experiments and deterministic midpoint quadrature. No finite experiment certifies the limit; analytic proof steps remain essential. The independent audit status is not performed.
