---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For generator DΔ and resets to the initial point, write f(s) for the unreset Laplace transform of survival. Then S̃_λ(s)=f(s+λ)/(1−λf(s+λ)); analyticity around zero follows from the killed bounded-domain survival tail. Differentiating first in λ gives f′+f² at zero reset. Mean is S̃_λ(0), second raw moment is −2 S̃′_λ(0), so the two slopes are respectively m₁²−m₂/2 and −2m₁³+3m₁m₂−2m₃/3. Independently, set a=R²/D and write the unreset exit transform as H(a x s)/H(a s), where the first three nonconstant coefficients of H(t) are b₁=1/(2d), b₂=1/[8d(d+2)], b₃=1/[48d(d+2)(d+4)]. The ratio in t=a s has coefficients c₁=(x−1)b₁, c₂=(x²−1)b₂−b₁c₁, c₃=(x³−1)b₃−b₂c₁−b₁c₂. Thus the mean slope divided by a² is c₁²−c₂ and the variance slope divided by a³ is 2c₁³−6c₁c₂+4c₃. These factor to the displayed formulas including the stated normalization. P_d strictly decreases, has values d(d+12) and −96 at the endpoints, and at q_d is −32d²/(d+4)². This proves the unique root, the ordering, and the three strict sign regimes for every d≥1. At d=3 the factorization is −3(13x−5)(x+3); at large d rescaling by d(1−x_d) gives the simple positive root 2√33−6 of c²+12c−96, with O(1/d) error in that rescaled variable. The sign-to-finite-change conclusion is pointwise in the radius as λ→0; no uniform rate, boundary behavior beyond immediate absorption, second-order sign, or global optimum is asserted. Inspected the supplied CHECK.py and verification note without running them.

## originality

FAIL

The variance threshold and shell are not expressly stated in the inspected prior passages, but are mechanically recoverable from the analyzed same-model exact transform, not merely from a generic reset framework. Chen–Huang's Eqs. (10) and (15) already give the analytic survival transform for the identical absorbing ball, diffusion normalization, arbitrary d, initial/reset point and reset rate. Apply one reset-rate derivative to Eq. (10), then take the constant and linear coefficients in the Laplace variable. The first three standard Bessel-series coefficients in Eq. (15) give the two polynomials by the finite coefficient recurrence in correctness. Strict monotonicity and substitution of their already-known mean boundary then give the shell. This is an explicit same-object corollary, not an assertion that Chen–Huang printed the polynomial or studied the mean–variance tradeoff.

## value

FAIL

Contrasting variance and mean under resetting is a legitimate motivation, and the shell can be useful as an explanatory example. As a standalone narrow exact finding on this process, however, the new-looking boundary is just the combination of low Taylor coefficients from an explicit same-model law and an elementary quadratic sign computation. Neither the 3D example, nor the large-d root expansion, nor the first-order shell interpretation removes that mechanical dependence or adds a separately nonroutine result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
