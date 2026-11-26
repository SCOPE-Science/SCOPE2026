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

The Laplacian is invertible on the zero-sum hyperplane and has precisely the hub-versus-rim eigenvector with eigenvalue m+1 together with the nonconstant cycle frequencies 3−2cos(2πk/m). The two squared projected pseudoinverse column norms are as in (1); barycentric gradients give each facet area as m times volume times the corresponding norm. For the volume, the standard coordinate simplex lies in the sum-one hyperplane (the phrase ‘inside 1-perp’ in the proof should read ‘translated into 1-perp’); its volume is √(m+1)/m!, unaffected by this translation. The determinant of the restriction is (m+1) times the tree count; replacing each cycle factor by ρ⁻¹(1−ρz)(1−ρ/z) for z an m-th root of unity gives ρ⁻ᵐ+ρᵐ−2. Summing facet-distance inequalities gives the unique insphere. The squared lengths m(m+1), 12 and hub-rim product −(m+1) give the common circumradius at the stated t_m. This center has all barycentric weights strictly positive (also at m=4); the weighted squared-distance identity proves global minimum and uniqueness over all centers, without assuming an axial solution. The rim norm tends to √(3/(5√5)) by the periodic Riemann sum, evaluating the integral by differentiation in its constant term. Since ma_m→1 and t_m→1/2, all limits in (6)–(7) follow. A reviewer-written bounded check used exact Gram determinants and a full circumcenter linear system for m=4,5,6. The frozen checker was inspected, not run.

## originality

PASS

The supported distinct result is the wheel family's coupled area/contact asymptotic and its explicit finite-size certificate, not an originality claim for tree counts, normalized simplex volume, general pseudoinverse normals, or a single small wheel. The plausible close matches inspected give a different polytope, hypothesis, or measure. The complete-multipartite comparison needs the finite-case qualification W4≅K1,2,2; even potential coverage of that case does not cover the family asymptotic.

## value

PASS

Wheels are a canonical non-vertex-transitive Laplacian family with one exceptional vertex. The exact distinction between a hub-opposite facet with only order m⁻² of total area and a hub vertex with half the minimum-ball support weight is a usable quantitative demonstration that the two boundary measurements need not track each other. The positivity and uniqueness certificate makes the distinction intrinsic, rather than a choice among support weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
