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

## Mathematical reconstruction

The proof determines the complete rank trichotomy via elementary affine geometry. For the spherical middle case it separates off-center sources, whose log-spatial differences are nonzero and yield the puff age from two known clock readings, from the exact circumcenter where all those differences vanish. The two exact scalar identities needed there are (1) strict monotonicity of the shifted harmonic-mean integral for equal known-mass readings and (2) at-most-one-turning-point behavior of the two-age log profile ratio for unknown-mass three-time readings. For one-time and two-time lower bounds, the unimodal Gaussian response and folded time-shift ratio produce positive distinct exact parameter pairs. The proof covers all positive masses and diffusivities as assumed (diffusivity fixed and known), all dimensions, all postrelease observation times, and every finite fixed sensor array.

## Executed reproductions

Run \(\texttt{python3 checker.py}\) with the Python 3 standard library. The checker was executed before final review and returned:

```text
PASS: 34099 deterministic numerical/exact assertions; analytic bounds in RESULT.md
```

It checks exact rational ranks, hyperplane reflection and spherical geometry for dimensions one through five, then recreates raw Gaussian readings from synthetic sources and recovers unknown mass, location and age from one nonspherical round or two spanning-sphere rounds for noncentral sources. It also exercises central-source mass/age ambiguity, nonlinear branch inequalities, and monotonic derivative signs at multiple dimensions and parameter choices. Random cases are deterministic by the fixed internal seed. Assertions are supplementary finite evidence, not a proof of injectivity for continuously many sources.

## Scope of verification

No external data, paid software, internet, or third-party libraries are required to run the checker. The exact mathematical statements and derivations are in RESULT.md, and the primary literature comparisons are in REVIEW.md. Independent validation of this claim has not yet been performed. This package does not verify transport-model realism, sensor calibration, or statistical robustness.
