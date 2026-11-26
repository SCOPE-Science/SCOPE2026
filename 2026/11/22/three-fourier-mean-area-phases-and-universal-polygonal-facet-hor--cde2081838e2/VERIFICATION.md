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

Off edge normals the chord spline is continuous with second derivative a finite signed mass, grouping coincident abscissae. Its Fourier transform is minus r^-2 times the finite exponential sum; the mean square of the latter is the sum of squared jumps. At p=4 the diagonal integral diverges logarithmically and the off-diagonal oscillatory integrals are bounded by integration by parts; the same separation gives the displayed p-up-to-4 residue. At a normal the nonzero endpoint jumps instead yield an r^-1 leading term with positive mean square, giving divergence from p=2. Uniform boundary decay O(1/r) proves boundedness and continuity below 2; above 4 divergence persists by comparison on r>=1. Writing alpha=4-p, expansion of the chord-spline energy using sum c=0 gives the fractional cosine identity, whose constant follows by Laplace representation and the beta integral. At alpha=2 the quadratic term vanishes since sum c*s=0; cancellation of the pole gives the stated logarithmic energy. For the horn, the diagonal edge contribution is 2 cos(theta)^2/sin(theta)^2 times the integral of (1-cos(r ell sin(theta))) r^(p-5). This yields exactly the stated coefficient after multiplying by p/A. For opposite parallel edges only their projection difference must be nonzero (individual projections may vanish by translation); after rescaling by |sin(theta)|, the product of the sinc factors times the weighted kernel is integrable, and the separated-edge cross term vanishes by oscillation. Nonparallel edges are uniformly O(r^-2); splitting at 1/|sin(theta)| makes their cross terms lower order. At p=2, below that split replacing the sinc products by 1 costs O(1), the separated-edge cosine integral against dr/r is bounded, and the tails above the split are O(1). Thus the diagonal logarithmic coefficient is correct. The power of the angular singularity in the radial square is less than one for 2<p<4; at 2 the logarithm is integrable and polar coordinates plus Plancherel give 4π². Positivity follows from uniform small-frequency positivity. The supplied example checker was inspected, not run, and is not needed for the general proof.

## originality

PASS

Distinct contribution: the full all-polygon finite-area range above two, the exact all-direction threshold at four, the supercritical-to-two and logarithmic horn coefficients, and the explicit chord-jump energies and directional residue. No originality credit for the known p=2 area, square thresholds already computed elsewhere, or the polygon-wide unboundedness at p>=2 also stated in a distinct same-day finding.

## value

PASS

A universal division among compactness, finite area with infinite rays, and complete divergence is useful for understanding Fourier mean sets just beyond the known critical-area identity. It requires distinguishing radial divergence from angular integrability and quantifies the effect of parallel supporting edges rather than just testing a few shapes. The finite chord-spline formula also permits directional evaluation without oscillatory quadrature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
