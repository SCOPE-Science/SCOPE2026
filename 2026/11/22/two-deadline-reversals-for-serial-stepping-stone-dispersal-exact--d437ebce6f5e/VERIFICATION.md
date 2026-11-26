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

The Erlang and exponential CDFs are correct under independent stage clocks and constant independent viability. With x=γT, the preference is the sign of R−q. For r≤1 stochastic dominance yields R<1; for r>1 the derivative has the sign of U=Bh−A, where h=A′/B′ is proportional to x^(k−1)exp(−(r−1)x). Since U′=Bh′, U increases from zero and then decreases strictly to −1; its only positive zero is simple. Thus R rises from 0 to a nondegenerate maximum above its terminal limit 1 and then decreases to 1. At each r>1 the finite maximum is smooth and strictly increasing, because ∂rR>0 and the maximizer has negative second derivative. The limit at r=1 uses compact convergence including the removable endpoint x=0 and R≤1/(1−exp(−x)) in the tail; x=r^(−1/2) proves divergence at infinity. This gives the three crossing regimes and transversality, and the square-root coefficient follows by substituting r−r_c=s², x=x_c+sy, dividing by s² and applying the implicit function theorem at the two distinct roots of the resulting quadratic. For the speed limit one can even sandwich M_k(r)/r between c_k and c_k+1/r by 1/u≤1/[r(1−exp(−u/r))]≤1/u+1/r. The derivative numerator of G_k(u)/u increases from zero to a positive value at k−1 and decreases to −1, giving u_k>k−1 and c_k≤1/(k−1); the LLN at u=k(1+ε) gives the matching lower limit for kc_k. The slower-mean example was rechecked exactly. Replay: python /workspace/audit-evidence/frozen2.py independently checks the rational Taylor certificate 1139/1200000 and probes the splitting at k=3,q=1.5; the numerical probe does not certify the universal theorem. The frozen check.py was inspected, not executed; its actual finite probes do not include the integration and finite-difference benchmarks described in the result's verification prose. This does not affect the analytic proof.

## originality

PASS

Credit the known quotient-monotonicity method, generic fold behavior, and the genuine overlap with the same-day fish-passage result. Exponential tilting turns the latter's common independent exponential death clock into a fixed-viability CDF pair: for equal means before mortality and z=μτ, take r=(2+z)/(1+z) and q=(2+z)^2/[4(1+z)]. Thus for z>0 it compares a specific k=2 curve within the frozen frontier, not an independent confirmation of novelty for the two-reversal phenomenon. The distinct supported contribution is the entire k,r,q frontier, its model-specific local coefficient, and the sharp large-q and k limits. The sources inspected do not establish equivalent or broader coverage of that package, and a same-day date does not establish priority.

## value

PASS

The threshold answers when a slower-mean serial route with lower eventual viability can beat the direct route, and exactly when that advantage disappears. The global impossibility of further reversals and the sharp speed/stage scaling give reusable benchmarks for the specified completion-time model. The generic fold alone would not justify acceptance, and this is not an empirically calibrated dispersal recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
