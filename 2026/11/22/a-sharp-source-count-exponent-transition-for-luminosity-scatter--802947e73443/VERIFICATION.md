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

Conditioning on luminosity and capping the inverse-square visibility radius at R gives the capped-power expectation with α=q/2. The −t/2 log shift fixes the arithmetic mean, not the log mean. Gaussian truncation and differentiation give S′=α[(α−1)M−p_t(0)]/2, with M the lower truncated moment and p_t(0)>0. This is strictly negative at and below α=1. For α>1 and d=log x≥0, H=M/p_t(0)<1/b<1/(α−1), so the derivative is still negative, including x=1. For d<0, independently integrating the first two moments of the H integrand gives I₁=t−(bt+d)H and I₂=tH−(bt+d)I₁, hence 2t²H′=2dI₁+I₂, yielding the stated ODE. With c=α−1, the integrating-factor derivative of H−1/c has sign of (b/2)t²+(1+cd)t−d². This quadratic has one positive zero. The transformed difference increases to zero from below after that zero, is strictly decreasing before it, and is positive for sufficiently small t (integrate over a neighborhood of u=−d). This proves one, strictly sign-changing root. Bounded payoff and convergence in probability give continuity at t=0 and limit zero at infinity. At t=2h+s, expansion under the integral on bounded s gives H=1/c−[s/c²+2/c³]/(4h)+O(h⁻²); the remainder is controlled by polynomial moments against a decaying exponential. Bracketing s proves the stated optimum expansion. At the root, M=p_t(0)/c and the normal tail on the positive side is asymptotic to p_t(0) by its density ratio tending to exp(−u). The identity (h+t/2)²/(2t)=h+(t−2h)²/(8t) confirms the yield coefficient. Independent split Gaussian quadrature and direct scalar search give t≈2.151163 and S≈0.048969789 for q=3, x=0.1. The proof can be replayed in RESULT.md lines 31–66; inspected verify.py was not executed, and numerical diagnostics do not certify the universal statement.

## originality

PASS

Best-of-knowledge pass for the full fixed-arithmetic-mean classification, strict unique maximizing variance in the interior regime, and faint-mean asymptotics. The standard count law, selection integral, lognormal truncation, and concave-payoff monotonicity principle are not the contribution. Equivalent portfolio-payoff terminology leaves a real priority risk, but neither the available primary expressions nor the indexed comparisons were found to imply the optimizing theorem.

## value

PASS

The exact count exponent q=2 distinguishes a universal scatter penalty from an interior optimum when the mean lies below the finite survey edge. This resolves a natural selection question that neither a local Jensen argument nor the integrated counts at prescribed scatter can answer. The optimizer equation and faint-source scale give quantitative analytic benchmarks and expose why fixing arithmetic rather than log mean matters. This is a mathematical model of an ideal survey, not an empirical prescription for changing source scatter or a claim about the actual radial exponent of the universe.

The dated certificate retains the supplied scientific assessment, sources and limitations.
