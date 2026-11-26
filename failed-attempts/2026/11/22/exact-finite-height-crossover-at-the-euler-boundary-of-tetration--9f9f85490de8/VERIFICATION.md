---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The change z=t y turns one tower step into g_t(z)=t exp(-z). Centering two steps at w=W(t) gives multiplier w^2=1+a/k+O(k^(-2)) and neutral cubic coefficient -1/6. The odd orbit starts at g_t^2(0) and increases below w. At t=e the two-step orbit increases to 1, since exp(v)-1 < -log(1-v) for 0<v<1 by the series coefficients. Continuity of finitely many iterates and subsequent monotonicity give uniform entry into any fixed small negative neighborhood of the centered origin for bounded a. For r_j=u_j^(-2), expansion gives r_(j+1)=(1-2a/k)r_j+1/3+epsilon_j. For small |u_j| a coarse bound is r_(j+1)<=(1+C/k)r_j+C, hence r_j=O(k) after bounded entry. The error sums to o(k): its bound reduces after r_j=O(k) to C|u_j|+O(1/k), with the mean |u_j| going to zero uniformly. The geometric sum then gives r_k/k tending to (1-exp(-2a))/(6a), with continuous value 1/3 and uniformity on compact parameter sets. Recover the negative square root for u_k and divide by t; w/t differs from 1/e by O(1/k). The static branch has no two-cycle for t<=e: for a two-cycle its parameter is log(t)=log(s/sinh(s))+s*coth(s), strictly increasing from 1 as s>0 (derivative 1/s-s/sinh(s)^2). For t>e the interior fixed point cannot attract the increasing odd orbit from below, and expansion of the two-cycle parameter gives log(t/e)=s^2/6+O(s^4). This proves the uniform square-root branch and the subtractions giving the error and probability-window laws. Independent direct one-step numerical replay shows approach from both detuning signs (at k=25000, 0.354721 vs 0.356503 for a=-1 and 0.966138 vs 0.969075 for a=1); those samples are not a proof.

## originality

FAIL

The leading moving-parameter profile is already covered by universal cubic finite-time scaling after a regular local change of coordinate and the two-step return. The inspected prior sources do not print a tetration CDF formula; it is the implication, rather than verbatim identity, that is decisive. The frozen result gives a correct map-specific proof but does not retain a distinct leading asymptotic beyond this transfer. The static branch follows from the same local coefficients and established tetration two-cycle geometry, and the remaining formulas are CDF differences.

## value

FAIL

The Euler-window question is natural and the proof is useful as a worked application. For a separate exact finding, however, the asserted finite-height profile and its normalization are mechanically supplied by existing cubic scaling once the tower is written as a second iterate; compact uniformity follows from CDF monotonicity, and the local mass identity is an endpoint difference of that profile. Even the exact static coefficient is fixed by the same cubic branch balance. There is no surviving claim of a new correction term, density scaling or other independent quantitative invariant that would justify treating the routine specialization as a distinct finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
