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

# Verification of fractional lattice-heat gradient crossover

The source file `check_fractional_lattice_crossing.py` is a reproducible finite numerical verification artifact. Run it using Python 3 with SciPy installed:

```sh
python check_fractional_lattice_crossing.py
```

The checker compares spectral moments against the exact gamma quotient, classical heat return probabilities against the modified Bessel function, and finite Fourier heat-kernel coefficients against the asserted symmetry/unimodality pattern. It also compares the integral of two semigroup multipliers to the difference of the distributions' Laplace integrals, brackets four representative positive time crossings, checks their orientations, and evaluates strict derivative signs of the rescaled difference at representative times.

The actual run finished with these messages:

```
MOMENT_GAMMA_AND_CLASSICAL_BESSEL_NORMALIZATION_PASS
FINITE_FOURIER_UNIMODALITY_AND_SHARP_GRADIENT_IDENTITY_PASS
CROSSOVER_SAMPLE_PASS 0.25 0.5 1.418656660926
CROSSOVER_SAMPLE_PASS 0.5 1.0 1.351743246075
CROSSOVER_SAMPLE_PASS 0.75 1.0 1.294242931795
CROSSOVER_SAMPLE_PASS 0.3 0.9 1.390737853437
CDF_LAPLACE_IDENTITY_AND_FOUR_CROSSINGS_PASS
RESCALED_TRANSFORM_DERIVATIVE_SIGN_SAMPLES_PASS
ALL_FRACTIONAL_LATTICE_CROSSING_CHECKS_PASS
```

The checker is **not** an exhaustive verification over a continuum of orders and times. It cannot replace the half-line positivity argument, Bochner subordination, strict Laplace sign-change proof, or asymptotic analysis in `RESULT.md`. Floating-point integration can produce finite accuracy errors, so only conservative numerical tolerances are asserted. There is no independent mathematical audit or external certification.
