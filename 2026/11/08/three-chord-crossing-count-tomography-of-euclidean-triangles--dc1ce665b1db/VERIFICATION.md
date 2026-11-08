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

# Verification of three-chord crossing-count tomography

The accompanying `verify_chord_tomography.py` is a standalone Python-standard-library verifier. To reproduce the check, run `python3 verify_chord_tomography.py` in the directory containing that file. It uses independent endpoint order comparisons, exactly excludes boundary-contained chords, and requires all checks to pass.

The analytical identity depends on three substantive steps: the conditional proper-crossing probability for a fixed chord joining successive edges; exact averaging of its square over ordered edge pairs; and the covariance identity between two indicators sharing one of three sampled chords. The second-moment computation is an integral of low-degree bivariate polynomials, independently checked with three-point Gauss-Legendre quadrature (sufficiently high degree to integrate those polynomials exactly apart from floating rounding).

Reproduction output:

```
case 0 histogram [63291, 38791, 12249, 5669] mean 0.669133 theory 0.666667 variance 0.708994 theory 0.705075
case 1 histogram [64984, 38105, 11545, 5366] mean 0.644108 theory 0.639178 variance 0.689949 theory 0.684586
case 2 histogram [67158, 37224, 10515, 5103] mean 0.613025 theory 0.6144 variance 0.667625 theory 0.665009
VERIFY_OK exact_rational_cases=5 independent_gauss_integrals=10 reconstructions=5 nonidentifiability_pair=1 three_chord_trials=360000
```

The rational checks use five admissible side-ratio triples. Two distinct triangles have exactly equal two-chord crossing parameters, proving the minimality example is not merely numerical. The random experiments check the count statistic in its original endpoint sampling model; they do not prove an infinite-family claim. No finite-sample inference guarantees, historical priority certification, or independent audit were performed.
