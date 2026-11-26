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

For the conservative sticky wall the backward equation has phi'(0)=nu(s/D)phi(0), and normalizing its two-term hyperbolic solution at L gives the stated transform. The duration of a renewal attempt is min(tau, Exp(r)), with expectation (1-phi_r)/r and success probability phi_r. Their quotient gives the mean. Writing a_y=y²/2+eta y and b_y=y^4/24+eta y³/6 in the kernel expansion yields the weak coefficient b_1-b_u-a_u(a_1-a_u)=-(1-u)P_eta(u)/24. The replay verifies this as a polynomial identity (`python3 -B /workspace/review_replay.py`, check 1). P_eta has a single positive root by its coefficient signs and opposite signs at 0 and 1. Each u in (0,1/sqrt(5)) has exactly one positive eta-crossing by the opposite signs of the leading and constant coefficients of P as a quadratic in eta; evaluating at an earlier root therefore forces the later root to be strictly smaller. At the initial root 1/sqrt(5) the coefficient of eta is positive, giving strict decrease from zero stickiness too. Bracketing P_eta(t/eta)/eta by its limit 24t-4 on either side of 1/6 gives the stated asymptotic. For fixed interior u and r>0, dividing numerator and denominator by eta gives the finite hyperbolic-sine limit while T_0 diverges. At u=0, the denominator remains 1 and the positive higher-order cosh terms show strict harm for every r>0, including eta=0. No uploaded checker was executed.

## originality

PASS

Pass for the sticky-strength-dependent sign boundary, its strict movement and sharp asymptotic, and the contrasting fixed-rate singular regimes. The unreset transform and moments and the general Poisson restart identity are prior ingredients, not new. Neither the different-boundary interval theorem nor the identified sticky active-particle renewal statement supplies this classification.

## value

PASS

Launch position and trapping strength are natural control parameters for resetting in this geometry. The critical-position law provides an explicit sign decision and a nontrivial boundary-layer scale 1/(6 eta), while the finite interior strong-trap limit and all-rate wall obstruction distinguish physical behaviors not visible in the unreset mean. These quantify a design question beyond computing a moment or quoting a known kernel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
