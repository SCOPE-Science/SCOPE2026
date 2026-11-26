---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On the punctured ordinal interval, let r send each successor to its predecessor and fix each nonzero limit. At a limit λ and for any γ<λ, input points in (γ+1,λ] go to (γ,λ]; this works without a countable local base. Thus r is continuous. If a compact superlevel set of f lies in [0,β], the corresponding nonzero-coordinate superlevel set of f∘r lies in [1,β+1] and is closed therein; β+1<τ. Extending by zero at the isolated point 0 defines a positive linear map U on C_0. Every f-coordinate is copied to its successor, so U is isometric. Adding e_0 on its separate support makes T affine, order preserving, and sphere-valued on the ball. A fixed point would equal 1 at 0 and all successors by the equation, and at all limits by continuity and transfinite induction, violating vanishing at infinity. Convex averaging preserves the ball and is nonexpansive with the same fixed points. For x_n=T_θ^n(0), successive differences are θ[(1−θ)I+θU]^n e_0. As Ue_k=e_{k+1} for finite k, their supremum norm is θ times the Bin(n,θ) mode probability; the usual tied modes are harmless. For fixed 0<θ<1 the mode differs from nθ by O(1), so Stirling gives exactly the stated equivalent. The residual is that of successive iterates (divide by θ for ||T x_n−x_n||), not a universal sharp bound. The supplied rational checker was inspected, not run; its finite coordinates cannot certify the transfinite step.

## originality

PASS

The literature already proves failure of the ball fixed point property, with a close earlier ordinal isometric shift using nonlinear envelopes. The surviving distinct claim is the positive affine construction on every ordinal C_0 ball, including at uncountable cofinality, with the explicit relaxed orbit for that map. The finite-coordinate binomial law is a standard shift calculation; this pass does not assign independent priority to the ordinary c_0 law or to asymptotic regularity bounds.

## value

PASS

An order-preserving affine isometric witness is considerably more constrained than an arbitrary map failing BFPP. The ordinal construction gives a direct witness with no cofinal-sequence assumption and shows on that witness that an exactly quantifiable vanishing residual does not imply a fixed point. The uncountable-cofinality case requires the full transfinite compatibility; the familiar finite shift and binomial mode alone would not have this force.

The dated certificate retains the supplied scientific assessment, sources and limitations.
