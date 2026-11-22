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

Run `python3 verify.py` with Python 3 and its standard library, in the directory containing this document and `RESULT.md`. The checker computes the cyclic Fourier sums directly for real and integral powers, checks exact inertia signatures for 480 parameter/grid cases in the sufficient concavity interval, and examines 12 additional grid/damping tests against low-harmonic quadrature signs (492 total cases). The tests involve floating-point arithmetic and are intentionally secondary to the proof, which is complete for the stated infinite parameter ranges.

**Correctness boundary.** The proof needs absolutely continuous first derivative, integrable second derivative, a nonzero signed Fourier endpoint coefficient and absolute Fourier series convergence; all are established for every fixed real exponent greater than one. Cyclic aliasing is exact and the parity condition requires an even sample count. The signs at finite continuum zero coefficients come from nonzero alias tails. The all-even-N assertion uses a sufficient concavity bound, including its endpoint. No assertion is made for odd sample counts, nonuniform sites or arbitrary powered-exponential covariance constructions.

**Originality and coverage boundary.** The source comparisons are best-knowledge and do not constitute a proof of historical uniqueness. In particular Wood's 1995 truncated-covariance paper was not fully accessible. No independent mathematical audit is reported.
