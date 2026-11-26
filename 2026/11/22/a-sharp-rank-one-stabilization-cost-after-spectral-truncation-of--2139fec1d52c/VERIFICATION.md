---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The scalar CARE on coordinate two is 2d−Kd²+1/K=0; on coordinate one the two terms cancel, all others vanish, and the closed-loop second eigenvalue is 1−Kd=−√2. Subtracting the equations of two putative stabilizing symmetric solutions gives the homogeneous Sylvester equation with Hurwitz coefficients and hence zero difference. For real K≥3, 0<d<1, so the unique best rank-one Frobenius truncation is e_1e_1ᵀ, with error d, residual norm 1/K, and closed-loop eigenvalue +1. For unrestricted orientation Y=zzᵀ, the feedback changes only row 2, so the eigenvalues are −1 with multiplicity n−1 and 1−Kz_2². Rank zero is excluded by this condition. Put y=z_2² and w=Σ_{j≥3} z_j². The exact squared error is (||z||²−1)²+d²+2(1−d)y+2w. Strict stability requires y>1/K, so the error is strictly above the claimed infimum. Unit z in span(e_1,e_2), with y decreasing to 1/K, proves sharpness and nonattainment at the marginal boundary. Dividing by d² gives (6−4√2)K+3−2√2, whose square root has the stated asymptotic. A relative cutoff that discards d leaves no actuation on the unstable mode; the example varies the gain and is not a uniform perturbation estimate at fixed coefficients.

## originality

PASS

Credit pre-existing low-rank CARE solvers, residual and stability safeguards, and the general observation that performance constraints matter in truncation. The distinct contribution is an exact sharp distance over all orientations of rank-at-most-one PSD approximants for this family, with an unattained minimum and an unbounded normalized price. The sources examined do not give that optimization result.

## value

PASS

The benchmark quantifies the stability cost of an approximation decision faced by low-rank solvers. Residual and best matrix error are O(K⁻¹), the exact solution's stability margin stays at least one, yet preserving stability at the same rank costs order K⁻¹ᐟ² in matrix error. Optimizing over oblique factors rules out the objection that the cost is only an artifact of requiring diagonal spectral factors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
