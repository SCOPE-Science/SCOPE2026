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

# Verification of exact gcd spectra of rationally coupled polynomial floors

The standalone `verify.py` (Python standard library only) was run against the files in this package. It returned `DEPENDENT_FLOOR_GCD_CHECK_OK`, with 496 exact local CRT checks, 3500 rational identities confirming the Möbius transformation, and illustrative fully integer-exact finite tests for \(f(n)=\sqrt2\,n^2\). The latter use `math.isqrt` to evaluate the required floors without floating-point rounding and compare coprime frequencies at five denominator values. They are diagnostics, not proofs of asymptotic limits.

The infinite theorem is proved from an exact integer-gcd reduction, Weyl equidistribution on fixed arithmetic progressions, and the published large-prime estimate for \(\gcd(m,\lfloor f(bm)\rfloor)\) (Holdridge, Theorem 1.3 for nonlinear polynomials; the known linear case cited therein). The total-variation estimate is a finite Möbius identity plus elementary absolutely convergent series bounds. Those analytic premises cannot be certified by the finite verifier.

The source's first public date is the arXiv v1 posting date, 2026-11-01. All novelty judgments remain provisional to independent literature review. No independent audit or independent validation has been carried out.
