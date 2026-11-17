---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For A,K SPD 2x2, the Nyström residual is PSD rank one, Cayley–Hamilton gives tr residual=det(A)(g^Tg)/(g^TAg), and isotropic Gaussian polar coordinates reduce the expectation to E_u[uu^T/(u^TCu)]=(C+sqrt det C I)^{-1}. The circle integral and two moment relations yield exactly the trace/determinant covariance formula, including repeated eigenvalues. Rotation gives tr(AK)=ac+bd−(a−b)(c−d)sin²θ, strictly increasing risk with angle when spectra distinct. Writing t=sqrt r yields a rational worst-angle risk F(t) whose derivative has at most one interior maximum, so minimization occurs at t=1 or t=∞; their equality iff tan²(vartheta)=sqrt(a/b) produces vartheta_c=atan((a/b)^(1/4)). Critical finite anisotropy is strictly worse. Expanding risk at r→∞ and θ→0 gives r^−1/2 plus θ² errors and θ~r^−1/4 crossover. Independently integrated the exact Gaussian circle ratio numerically (50,000 angular points): A=diag(4,1),K diag(9,1) gives 10/7; opposite alignment 14/5; rotated noncommuting example gives 3.1560941221641 in both expressions. These finite integrals corroborate the exact proof.

## originality

PASS

Published covariance-informed randomized Nyström literature primarily gives general expectation/error bounds; the checked published planar rotating fixed-column rangefinder theorem concerns deterministic Frobenius worst parameter error, not PSD Nyström trace residual under a designed correlated Gaussian covariance. The claimed sharp angle-dependent minimax switch, exact covariance rational risk and two-scale concentration/angular law were not found as consequences of these distinct formulas. Best-of-knowledge O with a particularly explicit full-text access caveat.

## value

PASS

Shows exactly when a spectral direction estimate warrants a maximally anisotropic sketch rather than isotropy in a transparent nontrivial 2D Nyström benchmark, with a sharp information-quality switch and precise noise-versus-orientation tradeoff. These are natural matrix-design invariants and actionable structural limits, not a merely arbitrary integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
