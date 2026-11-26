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

Independently substituting the affine unit-sphere parameterization gives the strictly concave distance quadratic with vertex t_c=a(m−c)/(b²−a²). In the pole branch, −r<δ<r implies a>0 and a+δ>0, a<r, and b²−a²=3a(a+δ). The small ball has t_s=−1/3 and maximum r² from 16a²+16aδ+3δ²=3r². The larger ball has F_0(1)=R² and vertex at least 1 exactly when R−δ≥sqrt(δ²+3r²); the positive side permits squaring to give s≤s_c. Also s_c≥R+r iff R≥3r, and s_c>R−r for R>r. In the two-latitude branch, putting u²=T and v=−1/(3u) gives R²=B+Ju², r²=B+Jv², and s=J(u−v)/sqrt(B+J). The denominator factors in the squared equation are positive on R/(3r)<T≤1; the ratio (3T+1)/(3T−1) decreases and the bracket increases. The endpoint squared separations are (R+r)² and s_c², proving unique solvability. The distance maxima then occur at u,v, tending to 1,−1/3 at the transition. The equal-radius candidate has maximum squared distance a²+2as/sqrt(3)+s²/4=R² and latitudes ±1/sqrt(3). In each case weights −v/(u−v),u/(u−v) give mean zero and axial variance −uv=1/3, hence both transverse variances are 1/3 as well. John's criterion proves unrestricted unique maximality, including at the degenerate pole and at the transition, so the branch limits coincide. This is an analytic check, not a sample-to-continuum inference from the supplied checker.

## originality

FAIL

The unequal 3D result is demonstrably covered at the level of formulas and proof by the distinct indexed unequal-ball lens record a3a1efb8f067. Its formal main theorem is scoped to dimensions m≥4, so citing that statement alone as a corollary would be incorrect. But it explicitly notes that the formulas admit lower dimensions, and its full finite-dimensional proof Steps 1–4 applies verbatim at m=3. Those steps derive both branches, global uniqueness, contact orbits and the transition; the dimension restriction belongs to the stated scope, not to any inference in those steps. The equal-radius result is explicitly covered earlier. This is an equivalent-coverage decision, not a claim about which of the two same-day records came first or which result is the comparator's unnamed earlier 3D reference.

## value

FAIL

The geometric question itself is worthwhile: the complete contact transition matters for an unrestricted John ellipsoid. As a distinct contribution this record reduces to the dimension-three substitution of the available finite-dimensional classification and proof, writing the tip quadratic in radicals, and appending a known congruent-ball formula. No independent dimension-three phenomenon or additional cutoff remains beyond that specialization. Rewriting the scalar parameter or improving the presentation does not supply a scientific remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
