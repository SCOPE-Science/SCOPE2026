---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The monomial basis yields the diagonal entries e^(−delta n)F(epsilon n); since the operator is normal and compact their absolute values give precisely the positive singular values with multiplicity. On the epsilon grid the profiles converge locally uniformly with an exponential envelope from min(t_j)>0, including when delta/epsilon tends to zero. Mesh sums of p-th powers therefore converge for every p>0, and compact convergence plus uniform tail control justifies grid suprema. For the moving strict indicators at s>0, all significant grid points stay in a common compact interval; sandwich between the limiting indicators at s±eta and let eta decrease to zero. The squared limiting profile is real analytic and nonconstant (it decays and is not identically zero), so equality at s is a null set even at a profile maximum. In the separated regime the Taylor quotient F(y)/y^m has a continuous extension and is bounded on the positive half-line. On the delta grid the scaled entries then tend to a constant times x^m e^(−x) with the same shape as an integrable bound. The Gamma integral and maximum give the constants, with m=0 handled at x=0. Lagrange interpolation proves the barycentric cancellation vector and the maximum possible order N−1. The beta integral and peak in the three-rate example follow by u=e^(−x).

## originality

PASS

Pass is for the coupled boundary/coalescence classification with arbitrary fixed finite exponential-polynomial profile, positive-level counting at finite ratio, and a matching moment-order law across Schatten exponents and the operator norm. Neither basic diagonalization, exact Hilbert–Schmidt traces, the polynomial–exponential separated shape by itself, nor the Vandermonde interpolation identity is treated as a distinct new result.

## value

PASS

This gives a quantitative failure mode for fixed-symbol control in a natural limit: at finite contraction-to-separation ratio the entire exponential-polynomial shape persists, and at large ratio only one moment remains visible. The change yields sharp multipliers for quantities sensitive to very different parts of the spectrum, including the quasi-Schatten traces and positive-level counts. Its usefulness is the combined classification, not another membership characterization or the known quadratic Gram computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
