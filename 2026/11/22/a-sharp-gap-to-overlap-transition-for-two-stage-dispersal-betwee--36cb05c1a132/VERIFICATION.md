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

Under independent uniform departure and two independent same-rate exponential stages, normalize x=λL and z=λd. The arrival density is [F(t)−F(t−x)]/x and the objective derivative is the difference of its values at z+x and z. There is zero probability for z≤−x and strict increase for −x<z≤0. On 0≤z≤x the derivative has sign H=F(z+x)−2F(z); g(z+x)/g(z)=e^(−x)(1+x/z) is strictly decreasing, so H begins positive and can cross zero only once, on its descending part. The sign at x is that of (1+2x)e^(−x)−1. In the tail the derivative has the sign of x(e^x+1)−(e^x−1)(1+z). These signs prove the unique global optimum, including the touching case at the unique positive root of e^x=1+2x. The tail derivative of the optimal phase is positive by sinh(x)>x, and the interior phase increases because H_z<0 and H_x>0 at the root. Continuity at the transition follows by taking limits in the interior-root equation, which has only z=x at the transition. The short-duration phase tends to 1; in the interior F(z_*)=F(z_*+x)/2<1/2 and tends to 1/2 at long duration. At synchrony the short-duration mean integrates the leading F(t)=t²/2+O(t³) to x²/6; at optimum the local density tends to g(1)=1/e and its mass is x/e+o(x). The one-stage phase is log(2−e^(−x))∈(0,x); the proof's incidental claim of positive derivative for all negative phases should read −x<z<0, since the objective is zero for z≤−x. This does not affect the result. VERIFICATION.md and checker.py were inspected, not executed; the reported 39007 finite assertions are supplementary.

## originality

PASS

The precise two-stage equal-window optimizer, sharp change from gap to overlap and short-duration synchrony penalty were not supplied by the inspected antecedents. Standard Erlang calculus, interval endpoint balancing, and the ecological relevance of timing are not the distinct claims.

## value

PASS

The idealized model distinguishes synchrony, overlap, touching and a strictly advantageous positive gap, with an exact crossover and unbounded relative cost of synchrony despite vanishing absolute success. The one-stage contrast identifies sequential transport as the mechanism within this family, rather than treating the threshold as an arbitrary calendar setting. This is an exact timing benchmark, not a field management or population-persistence prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
