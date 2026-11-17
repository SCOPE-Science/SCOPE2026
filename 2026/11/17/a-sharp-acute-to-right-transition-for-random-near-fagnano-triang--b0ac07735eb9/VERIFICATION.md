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

The scientific proof is in `RESULT.md`. The program `verify_fagnano.py` independently evaluates the chord-distance Hessian, checks its determinant against the closed formula, and integrates small-excess events by scrambled Sobol cubature in coordinates adapted to the two local geometries.

Run with Python 3, NumPy, and SciPy:

```sh
python -m pip install -r requirements.txt
python verify_fagnano.py
```

Observed output on the reviewed package:

```text
equilateral det(H) 13.5 p0 1.5
  t 0.01 empirical_coefficient 3.2406218 predicted 3.2245322
  t 0.002 empirical_coefficient 3.2277898 predicted 3.2245322
  t 0.0004 empirical_coefficient 3.2251569 predicted 3.2245322
scalene acute det(H) 0.2683281573 p0 5.366563146
  t 0.01 empirical_coefficient 0.4264695 predicted 0.426191
  t 0.002 empirical_coefficient 0.4261575 predicted 0.426191
  t 0.0004 empirical_coefficient 0.4261695 predicted 0.426191
right t 0.004 empirical_coefficient 2.0907604 predicted 2.1949357 limit_integral 1.1967972
right t 0.001 empirical_coefficient 2.1462368 predicted 2.1949357 limit_integral 1.1967972
right t 0.0002 empirical_coefficient 2.1737848 predicted 2.1949357 limit_integral 1.1967972
FAGNANO_ACUTE_RIGHT_SMALL_EXCESS_DIAGNOSTIC_OK
```

Acute geometry: the independently calculated Hessian has strictly positive eigenvalues and the exact determinant identity; cubature uses \(2^{18}\) points per threshold. Right geometry: cubature uses \(2^{19}\) points per threshold in the singular rescaled coordinates. The finite-threshold values have truncation and numerical quadrature error; the program is not a symbolic proof of the \(t\downarrow0\) limit, is not exhaustive over triangles, and does not establish historical novelty or independent validation.
