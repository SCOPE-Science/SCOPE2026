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

For every direction the four facet inequalities give the two radial endpoints; signed permutations preserve full chord length and give 48 equal-area chambers. In a chamber with x≥y≥z≥0 the two denominators are x+y±z, so in the stated angular coordinates L=2A√(1+q²)/(A²−q²). This increases for q>0, and the factored polynomial in the proof bounds the maximum at the upper chamber corner. The lower corner gives the stated minimum; continuity on S² gives the full interval as support. Solving the quadratic in q² and rationalizing matches q_* with the angular cap, and integrating the area element gives 12/π with no positive-area equality levels. The minimum chart works across the adjacent sign/order chambers: its even quadratic form has coefficients 1/√2 and √2, hence area π per unit deficit. At the maximum the nonnegative homogeneous leading deficit is −6 min(a,b,c) on the tangent plane, positive off the origin and comparable to the Euclidean norm; its unit sublevel is the triangle of side 1/√2 and area √3/8. For each extremum, the rescaled sets lie in a fixed compact disk, their indicators converge off null boundaries, and the smooth area Jacobians converge uniformly to one; normalized densities converge in L¹. The symmetry-equivalent oriented marks carry equal weights. Multiplicities 12 and 8 divided by 4π yield the two stated asymptotic constants, not exact finite-deficit identities. The frozen NumPy/SciPy check.py and recorded diagnostics were inspected, not executed; they do not establish the continuum limits.

## originality

PASS

The supported claim is the regular tetrahedron's orientation-only centroidal chord distribution and its two marked limits, not the already classical intersect distribution of the same body. The strongest same-body match is documented by the author's later full-text treatment as the tetrahedron covariogram calculation. The same-ensemble records on other bodies and the origin-symmetric upper-tail theorem do not cover this tetrahedron. The 2005 full paper could not be read, so this remains a best-of-knowledge assessment with a named access risk.

## value

PASS

The regular tetrahedron is a canonical simplex and the fixed-centroid law is a natural counterpart to the classical translated-line statistic. An evaluable exact CDF plus a smooth quadratic minimum and a piecewise-linear maximum with explicit and distinct directional limits is useful beyond merely listing support endpoints. The contribution is scoped to this body and orientation measure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
