---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For lines (a u_j+tJu_j,kt), orthogonal projection onto (Ju_j,k) yields the asserted point-to-line quadratic with first and second discrete Fourier harmonics. On n>=4 equally spaced samples, first harmonic is orthogonal to the sampled second, so coefficient -2ar vanishes only for r=0 (a>0). On n=3 samples cos2v aliases cos(3theta)cos v+sin(3theta)sin v; the independent first-harmonic coefficients give r cos 3theta=4aB and z=r sin3theta/(4k). Exactly three nonaxial components and the axis result. Averaging the squared distance and substituting gives a²[(4B-1)²+(8B(2B-1)+B/k²)tan²3t], strictly convex at each branch minimum. The axis has one minimum, no maxima; for R>0 the axis contributes 0/1/2 and three curves 0/1/2 each, giving 0,1,2,5,8 values. Independent direct line-projection numerical tests for a=1.3,k=0.8 and n=3,4,5 confirmed the branch equalities and axis normalizations; inspected check.py from actual source. Exact Fourier algebra, not samples, proves the all-parameter claim.

## originality

PASS

Best-of-knowledge originality: the exact claim is not mechanically implied by inspected primary or published related theorems. Known four real trisector branches alone gives no count for a prescribed radius: distance along each branch must be analysed. General bounds (at most 8 minima for general trisectors) also cannot imply the exact 4 minima and no maxima of this special family. Here the explicit averaged-distance quadratic in tan3t and positive Gamma determine the exact number 5 at threshold and 8 above. By Fourier orthogonality the extra centers disappear for n>=4. See explicit access and indexing risks; unsuccessful search is not proof of priority.

## value

PASS

A natural regularly spaced family of skew tangents has a sharp three-versus-four-site harmonic resonance and a complete exact radius-by-radius number of spheres tangent to every line. The transition at a(3+4k²) and complete four-minimum spectrum are useful model cases for multivariate Voronoi, exact tangency and algebraic geometry; this is more than rephrasing an existing cubic-plus-axis branch count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
