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

Independently reconstructed the two regression covariances (RESULT.md 48–65): for input K_S x and target Cx they are (r²/2)D I and (r²/2)C E[K_S]^T. The smallest possible D is cos²(θ/2)>0 on 0<θ<π, so the optimizer over all matrices is unique. Subtracting its explained energy from 2r²(1−cos θ)/h² leaves 4r²v(1−cos θ)²/(h²D). This gives the stated exact residual and radial sign, including all deterministic laws. At fixed h the angular derivative of h times the fitted frequency has numerator (1−2q)cos θ+2q and positive denominator D², giving the unique fold or the increasing deterministic-midpoint endpoint case. For a fixed offset law and fixed true ω>0, the radial coefficient starts with (μ−1/2)ω²h; the angular h² and h⁴ coefficients are (q−1/6)ω³ and (q²−q/4+1/120)ω⁵. Thus the full-matrix order criterion, −1/180 coefficient, residual expansion and 2π/3 fold follow. Read VERIFICATION.md and the finite checker without executing it; the checked analytic proof suffices. The fold refers only to the fitted angular coefficient, not identification from all data.

## originality

PASS

The supported contribution is the exact arbitrary-law statistical classification: full optimizer and irreducible risk, with the necessary and sufficient moments for simultaneous conservative fourth-order recovery and the resulting fold. Velocity-matching interpolation, the general bias–variance viewpoint, and the compact-difference angular family (not just its uniform instance) are prior; they do not identify the fitted full matrix and residual or tie these to feasible offset laws. No matching joint result was established in the comparisons below.

## value

PASS

The motivated question is how to choose collocation offsets to recover conservative oscillatory dynamics, not how to maximize a known trigonometric symbol. Deterministic midpoint gives zero risk and no fold but only second-order frequency accuracy; fourth order fixes the variance, gives nonzero irreducible loss and forces a fold within the sampling range. This separates three practically different targets by exact, usable population conditions. The interpretation is limited to the specified noiseless linear model and the angular statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
