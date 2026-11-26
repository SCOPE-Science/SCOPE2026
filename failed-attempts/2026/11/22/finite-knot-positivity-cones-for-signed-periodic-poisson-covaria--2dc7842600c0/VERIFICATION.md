---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

With 0<r<1 and positive integers k,d, the signed Fourier convolution is the geometric Green function applied to sources at the specified knots. Its homogeneous recurrence between knots has the claimed two endpoint weights (strictly positive at interior integer positions); after dk it is a decaying geometric tail. The coarse-grid precision formula gives the three inverse rows including the reflected left boundary and the right endpoint, also for d=1. Bochner then identifies the cone with the orthant. The ray supports give ranks 2k-1 and 4k-2 for the first and inner rays, respectively, and the final ray has an infinite tail. If u_d=0 the spectrum is finite; if u_d>0 a consecutive block from the tail gives an invertible Vandermonde matrix on any finite set of distinct sites. Uniform RKHS density is equivalent to full Fourier support, because characters with positive coefficients lie in the RKHS and each missing coefficient is detected by a continuous Fourier functional. Independent rational round-trip, interpolation and ray checks passed 21,660 assertions at three radii, k=1–4 and d=1–5; the supplied code was inspected, not run. The finite checks supplement the all-parameter proof.

## originality

FAIL

The frozen statements are correct, but the complete single-radius classification is a routine corollary of the classical tridiagonal Kac–Murdock–Szegő (AR(1) covariance) inverse, applied on the full lattice and on the coarse signed interval. No exact printed duplicate of the signed-mask wording is required for this implication. The companion non-point mixture is a genuine overlap but is not the reason for failure.

## value

FAIL

The signed-mask question is natural and the formulas are usable, but the claimed package is fully determined by the standard nearest-neighbor geometric Green function. The listed ranks count modes between adjacent sources and the two density notions separate as soon as the standard geometric tail is read off. No substantive new invariant or nonroutine boundary result survives that reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
