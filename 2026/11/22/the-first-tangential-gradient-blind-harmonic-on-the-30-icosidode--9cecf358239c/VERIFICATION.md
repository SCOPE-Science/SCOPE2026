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

The normalized midpoints are (u+v)/(2φ) for v·u=φ, with squared length one. On homogeneous degree-ℓ polynomials the tangential gradient in ambient coordinates is ∇H(w)−ℓH(w)w. A fresh reconstruction selects the edges exactly, checks the 30 distinct reduced unit nodes, forms denominator-cleared harmonic bases and reduces via φ→23 in F₁₀₁. Since φ²−φ−1 vanishes at 23 and 2φ is invertible there, the ranks (3,5,7,9,11,12) give characteristic-zero lower bounds by lifting nonzero minors. Degrees 1–5 reach their full dimensions. The sextic is a sum of solid zonal harmonics and is invariant by vertex permutation. Half-turns about the midpoint directions fix the nodes and act as −I on the respective tangent planes, forcing zero tangential gradients. Directly, with q=φ+2, the sums of t_v²,t_v⁴,t_v⁶ at e₁ are 4q, 12q²/5, 8q³/5; hence F₆(e₁)=−132q³/5≠0 (85 mod 101). Thus the degree-six rank is at most 12 independently of reduction; equality and the claimed kernel line follow.

## originality

PASS

The 30-node geometry and degree-six icosahedral invariant are established background. Its gradient vanishing on this orbit also follows directly from known symmetry and is not credited as an independent novelty. The distinct contribution is the derivative-only rank profile: all five preceding positive degrees are injective and exactly one line is lost at six. The strongest distinct same-node sampling record concerns scalar values, not these differential measurements.

## value

PASS

The orbit is a standard symmetric sampling grid and the observable is natural for derivative-only reconstruction. Despite many more nominal tangent measurements than harmonic dimensions, the first invariant degree has a blind direction. Identifying the full kernel and confirming that earlier degrees really are injective gives a useful exact sampling boundary, stronger than observing symmetry-forced failure at six alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
