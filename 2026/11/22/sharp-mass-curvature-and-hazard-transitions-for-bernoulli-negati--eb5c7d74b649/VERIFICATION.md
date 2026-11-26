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

The convolution gives m_0=(1-q)^nu/(1+r) and m_k as stated. For an independent tail sign check, write d=(nu-1)q/(q+r)>-1. For k>=1 the ratio R_k/q factors into [1+(nu-1-d)/(k+d)] [1+d/(k+1)]. Both factors are positive; their corrections to one have the sign of nu-1, so both strictly decrease with k if nu>1, both increase if nu<1, and both equal one if nu=1. This agrees with the all-index difference in RESULT.md, whose tail range is k>=1, not k=0. Directly R_0=nu q+r and R_1=q nu[q(nu+1)+2r]/[2(nu q+r)]; subtracting gives the first-triple quadratic and positive root L. The convergent survival-to-mass sum compares term by term, with strictness from one-factor terms whenever the first compared ratios are distinct. For nu=1 this gives h_0=(1-q)/(1+r), h_k=1-q for k>=1. For nu<1, h_0>=h_1 reduces to r(r+nu q)<=1-(1-q)^nu-nu q, with strictly positive right side by the strict tangent inequality. The monotone quadratic gives D. At L the compared first factors tie but the two-factor term is strictly larger at k=1, proving h_0>h_1 and L<D. The stated example gives the curvature numerator 3/400 and hazard test 7/200<3/4-1/sqrt(2) by squaring. Replay: RESULT.md proof steps 1–5 and the factorization above. The supplied SymPy checker was inspected, not executed; its finite examples are not used for the universal statement.

## originality

PASS

Credit the previously known distribution, the general mass-ratio comparison, and the separate catalogue result on global log-concavity. The supported distinct contribution is the sharp global log-convexity and first-hazard thresholds, all-index hazard classification for 0<nu<1, and the strict separation of those boundaries. The two older convolution-power references concern a different property in the available material. Access limitations and potential priority overlap are recorded below.

## value

PASS

The family is already used as a count model and its shape affects reliability conclusions. The result decides every hazard comparison, distinguishes immediate decline from a single initial rise, and identifies a strictly nonempty band where the hazard decreases despite failure of global log-convexity. That complete separation is useful beyond detecting an erroneous blanket curvature claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
