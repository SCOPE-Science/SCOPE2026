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

Every h_j is positive because the combined beneficial subtraction is bounded by 2P. Multiplication of the model's conditional survival probabilities makes maximizing survival equivalent to minimizing the sum of h_j; the 0-to-T interaction and baselines are constant. With z=|t−T/2| the derivative for z>0 has the sign of sinh(βz)/sinh(αz)−(α/(qβ))exp((β−α)T/2). This ratio is strictly increasing since u coth(uz) increases with u>0 (differentiate and use sinh x cosh x>x). Its limiting value at zero and its outer endpoint value give q_c and q_e, respectively. At equality the derivative has strict sign on the open half interval, proving exactly the claimed minimizers; otherwise the unique interior root is a strict half-interval minimum and reflection gives both minima. The derivative of ln q_e is α/(exp(αT)−1)−β/(exp(βT)−1)>0, and q_e increases from (α/β)² to α/β, whereas q_c increases to infinity and always exceeds q_e. Inverting the expansion of the ratio in z², coefficient (β²−α²)/6 after normalizing by β/α, proves z²=3(T−T_c)/(α+β)+O((T−T_c)²). For the persistent interior branch z→∞ as T→∞; writing the ratio as exp((β−α)z)(1−exp(−2βz))/(1−exp(−2αz)) gives t=T/2−z→ln(qβ/α)/(β−α), including zero at q=α/β. The sample thresholds also follow algebraically (at α=1,β=3, q=1/5 the endpoint root obeys 1+e^−T+e^−2T=5/3). The supplied checker is a grid and identity check inspected as text, not run; it is not a proof of global minima or an empirical validation.

## originality

FAIL

A distinct indexed result states the identical signed two-exponential optimization and complete fixed-horizon phase diagram, including the split onset and a stronger minimum-separation version. In its notation set a=α, b=β, A=P, B=D, r=A/B=1/q. Its maximized G is exactly −F_T; its cutoffs r_0, r_1 are exactly 1/q_c and 1/q_e. The optimal sets, equality cases and unique interior root coincide. At fixed q, r/r_0(T)=exp((β−α)(T−T_c)/2), so the expansion of the same root at r/r_0=1 gives the stated fixed-q onset, including the error order by analytic inversion in z². The horizon-order cases and the far-horizon limit are direct monotonicity and exponential-limit readings of the same two cutoff functions and root, not a different optimization theorem. Dates alone do not establish precedence; the decision is exact mathematical coverage of the claimed classification and routine implications, not a claim about who published first.

## value

FAIL

The fixed-endpoint three-regime problem is a recognizable toy mathematical model of competing relaxation rates. However, the complete optimizer and its onset are unchanged in a covered signed-exponential problem, with the remaining horizon readings following routinely from the explicit thresholds and unique root. No additional empirical result or independently useful unknown mathematical invariant is established by the new interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
