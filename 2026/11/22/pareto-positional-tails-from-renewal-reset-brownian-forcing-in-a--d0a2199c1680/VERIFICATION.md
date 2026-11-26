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

Frozen line 35 is false as an unqualified strict inequality: take T1=2+U with P(U>t)=(1+t)^(−7/4) for t≥0, and T2=T1 plus an independent equiprobable sign. The clocks differ, are positive with the same finite mean, and form a convex-order pair by conditional Jensen, but both spatial variances are +infinity (both positional means exist here). For Pareto index at most 3/2, the symmetric position does not even have a Lebesgue mean. The complete repairs/5/RESULT.md and SLOGAN.txt consistently optimize the extended second moment, with strict convex-order inequality for distinct clocks only when the lower second moment is finite. This is proved by integrating the continuous, ordered call functions against g''(u)=2(1−e^(−μu))>0; distinct finite-mean laws have different call functions. Rechecking the unchanged tail: stochastic Fubini gives variance h(a)∼(2D/μ²)a, with h(a)≤2Da/μ². The reset-epoch affine series converges and has a moment of order q strictly between max{1,2(α−1)} and 2α, by geometric L^q summation. At stationary time the length bias of the current interval does not affect the preceding-epoch position Q, because the interval is fresh. Its damped tail is negligible by the q-moment; the age survival is the integrated clock survival divided by m, and multiplying h(A) by independent Z² gives the claimed Gamma-factor constant. Tail integration settles every moment, including the endpoint. Independently, E Q²=E h(T)/(1−E exp(−2μT)) is finite for every finite-mean clock, and renewal reward and conditional Gaussian centering give E X²=m⁻¹ E[h(T)/(2μ)+∫₀ᵀ h(a)da] as an extended expectation. The bracket is exactly D g(T)/μ², by differentiation from zero. This verifies the finite formula and the infinite case without assuming finite force covariance. Strict Jensen still gives the deterministic clock as the unique minimizer, and positive two-point clocks at fixed mean make the finite values unbounded.

## originality

PASS

The repaired distinct claim is the force-only model's full continuous-time tail (including retained earlier position) and its Brownian all-renewal second-moment identity and fixed-mean optimizer. The general Kesten recursion, deterministic/Poisson cases, direct-reset analogue of the Gamma amplitude, and an analogous convex-order principle for binary propulsion are prior content. The corrected strictness qualifications assert no new general convex-order principle. The compared sources do not cover this combination in the stated model.

## value

PASS

Even with a positive trap, continuous position driven by renewed Brownian force can have a stationary law lacking finite spread, or even a first moment. The scientifically useful distinction is between observation within a long interval and observing at a reset: the full calibrated positional tail includes memory from all previous intervals and shows it is negligible only at the leading heavy-tail scale. The exact all-clock spread formula and sharp optimizer provide a separate protocol comparison on the same dynamics. Correcting strictness does not remove either conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
