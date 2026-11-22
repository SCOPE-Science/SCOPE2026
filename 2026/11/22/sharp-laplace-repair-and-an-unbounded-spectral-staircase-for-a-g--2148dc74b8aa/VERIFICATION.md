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

**Exact analytic checks.** The normalized cosine coefficient of \(e^{-a|	heta|}\) was obtained by integrating on \([0,\pi]\). Applying \(1-a\partial_a+(a^2/3)\partial_a^2\) gives the smooth Matérn coefficient, and symbolic differentiation of the rational primitive reproduces the displayed formula. All nonzero even Fourier coefficients reduce exactly to \(I_{2m}[b-L-cx_m+hx_m^2]/(1+b)\). Consecutive differences are \(h(x_m-x_{m+1})(2x_*-x_m-x_{m+1})\), and the logarithmic derivative of the crossing ratio is strictly negative for every \(a>0\). These analytic identities cover infinitely many harmonics; see RESULT.md for proof.

**Executable finite diagnostics.** Run `python checker.py` with Python 3, SymPy and mpmath. The program performs 500 finite assertions: one symbolic coefficient identity, high-precision direct cosine quadrature, 39 ordered mode-transition comparisons, and sample positivity/sharpness/asymptotic tests. All 500 assertions passed. The checks are finite and do not themselves certify general quantifiers or exhaustive originality.

**Scope and remaining limitations.** The claim concerns exactly one unit geodesic circle, one positive range parameter, and a nonnegative mixing ratio. At the sharp boundary one or two nonzero even modes have zero coefficients; strict positive definiteness on distinct sites follows from the analytic Vandermonde proof, not from finite grids. This repair does not retain Matérn-5/2 differentiability. A related source may have escaped the bounded published-literature comparison.
