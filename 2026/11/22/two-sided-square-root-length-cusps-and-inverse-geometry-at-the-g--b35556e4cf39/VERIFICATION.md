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

The two signed z branches at angle t have speed sqrt(r²+(dr sin t)²/Q), where Q=R²−(d+r)²+2dr(1−cos t), and only finitely many overlapping points. This gives the stated nodal length by the half-angle substitution. For the delicate moving endpoint in the frozen proof use the exact local coordinate h=2 sin(t/2), not the leading angular approximation in line 71. With λ²=|R²−(d+r)²|/(dr) and h=λu, the admissible endpoint is exactly |u|=1 on the plus side. The square of the speed becomes r²+dr(1−λ²u²/4)u²/(u²±1), with plus in the denominator for d below critical, and dt/dh=(1−h²/4)^(−1/2). On a fixed small h-cutoff the speed difference from the nodal integrand is bounded by C(ε+u^(−2)) for |u|≥2. The ε term integrates to O(ε/λ) in rescaled units, and near the endpoint the bound is C(1+(|u|−1)^(−1/2)). Outside the cutoff the change is O(ε), and λ/sqrt(ε) tends to sqrt(2R/(rd*)). This supplies the endpoint justification without a false uniform bound anchored to the limiting endpoint in the unstraightened coordinate. After subtracting the missing rescaled interval, the two dimensionless limits are −2F(m) and −2F(1−m): differentiation gives respectively −K(m) with value 0 at m=0 and K(1−m) with value −2 at m=0, the latter using w=sqrt(u²−1). The prefactor counts both sheets. F'=K/2 and its endpoint values 0,1 verify the inverse bijection and positivity. For outer contact set t=π+w, qmax=R²−(d−r)² and use sin(w/2)=sqrt(qmax/(4dr)) sin θ, z=sqrt(qmax) cos θ. This parametrizes the full small loop; recentered and divided by sqrt(ε), it converges in C¹ on the entire θ-circle to the ellipse with semiaxes sqrt(2Rr/(R+r)) and sqrt(2R). This gives the reported perimeter coefficient. Independent Simpson integration of the elliptic integrals also agrees with the listed examples; neither that diagnostic nor the frozen checker proves the limits. The laws apply pointwise for fixed R>r, not uniformly near degenerate radius ratios.

## originality

PASS

The qualified contribution is the explicitly complementary elliptic pair of moving-offset Euclidean arclength cusp coefficients and the aspect/scale reconstruction from their ratio and the nodal length, with the outer-contact law. The classical geometry and fixed nodal-length cases are not independent novelty; in particular an inspected same-day hippopede record gives the exact generalized nodal-length formula after scaling. The strongest structurally similar cusp-and-inverse result has a different curve model and does not imply these coefficients.

## value

PASS

The sharp constants at the natural topology-change parameter distinguish the two sides quantitatively, pick out the classical aspect as the unique symmetry threshold, and give an exact two-observable geometric inverse. This is useful beyond recognizing the square-root singularity, and does not rely on the fixed-curve length alone being new. The outer coefficient separately quantifies extinction at external tangency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
