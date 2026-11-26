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

A mean-zero scalar BV class is the integral of centered tail indicators v_s against its interior derivative μ. Integrating x v_s gives h(s), a positive covariance because the conditional mean above each interior s is strictly higher than the one below it. First-moment cancellation therefore puts equal positive h-mass B on the two Jordan parts of nonzero μ. Couple the probability measures h μ⁺/B and h μ⁻/B by their product. With weight B(1/h(s)+1/h(t)), the profile U=(h(t)v_s−h(s)v_t)/(h(s)+h(t)) integrates to the original function by cancellation of the coefficients upon taking each marginal; the weight integrates to |μ|. Each distinct-site pair is admissible with variation exactly one, using the opposite coefficient signs. The positive mixture bounds the full norm by the supremum of these profile norms, which each attain their own ratio. Covariance of nested tail indicators gives exactly the stated K. In the open diagonal limit v_s−v_t→0 in L² and h stays positive; at a side away from the corners one indicator norm vanishes and the coefficient on the other also vanishes; at all three corners both indicator norms vanish and coefficients are bounded. Thus K extends continuously by zero to the compact triangle and reaches a positive maximum in its interior. For the uniform law I verified by integrating the three constant levels that K=H(s)H(t)d(1−d)/(H(s)+H(t))². The exact deficit splits into the two displayed nonnegative squares and vanishes only at (1/4,3/4). Equality in the sharp bound forces the product coupling to concentrate on that unordered pair by equality in the integrated norm upper bound. The Jordan parts are mutually singular, so the derivative is a scalar multiple of the difference of its two atoms. Mean subtraction yields precisely the centered middle-half plateau, and its ratio is (|c|/2)/(2|c|)=1/4. Replay: python3 /workspace/reproductions/review_03_bv.py (SymPy, scalar integrals and deficit); the frozen exact-rational checker was read, not run, and counts finite test cases, not independent general assertions. Valid for interior distributional variation and the stated real-valued BV classes and positive continuous densities. The deficit is for the pair kernel, not arbitrary BV functions; equality for a general density is not classified.

## originality

PASS

The supported distinct result is the evaluated weighted covariance kernel and attained sharp maximum, with the uniform 1/4 value, complete plateau class and two-jump deficit. General moment sparsity and optimizing projected Heaviside norms are related methods, not credited as new here.

## value

PASS

Controlling the L² energy of an interval signal orthogonal to constant and linear trends by its interior variation is a natural sharp interpolation problem. The weighted result converts that infinite-dimensional norm problem to an attained two-site calculation, and the uniform result determines both amplitude efficiency and exact jump locations. The strict difference from the affine approximation norm shows why the additional structure is useful rather than a reformulation of a standard projection inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
