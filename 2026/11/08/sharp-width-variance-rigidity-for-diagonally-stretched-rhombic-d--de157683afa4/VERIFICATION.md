---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

From the sixteen endpoint sums of four sign generators t_i=(±1,±1,±1), the rhombic dodecahedron equals Σ[-t_i/2,t_i/2]. Thus W(u)=Σ|<diag(a,b,c)t_i,u>|. The spherical first moment of each summand is √S/2 and the second cross moment equals 2SΦ(ρ)/(3π). Pair correlations ρ_a,ρ_b,ρ_c each occur twice, yielding EW=2√S and EW²=4S/3+8S/(3π)ΣΦ(ρ). Since Σρ_i=−1, Φʺ(t)=1/√(1−t²)≥1 gives unique Jensen minimizer ρ_i=−1/3 and the stated stability coefficient via strong convexity. Since Φ(t)<π/2 for −1<t<1, Var(W)<4S/3 with equality approached only as axes degenerate. Independent exact numerical evaluation for a=b=c, (1,2,3), (.1,.1,1) matched the closed regular value 0.067918113012 and had positive stability residuals; program verifies vertex support and Monte Carlo but not infinite quantifiers.

## originality

PASS

Best of knowledge: prior exact random-width and FCC-cell work does not imply the complete fixed-S diagonal shape moment profile, all-parameter unique variance optimizer, and sharp anisotropy stability. Earlier central-plane section probability is not directional width variance.

## value

PASS

Directional width anisotropy of the FCC Voronoi cell is a natural geometric statistic; the all-scale explicit second moment, unique isotropic minimizer, sharp nonattained degeneracy limit, and stability inequality supply a nontrivial quantitative shape rigidity result beyond standard Gaussian integration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
