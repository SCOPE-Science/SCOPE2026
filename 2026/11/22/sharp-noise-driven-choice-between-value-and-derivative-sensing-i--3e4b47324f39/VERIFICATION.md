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

The target J has Brownian stochastic-integral kernel (1−u)²/2 and variance 1/20. Taking inner products with (t−u) on [0,t] and with 1 on [0,t] gives C=t²(t²−4t+6)/24 and D=t(t²−3t+3)/6, respectively. The observation denominators are t³/3+η and t+η; the conditional mean minimizes MSE, so the squared-covariance gains are the correct objectives, with zero gain at deterministic time zero. For t>0 the derivative of the value gain is positive below x_0 and has the sign of η−H(t) on [x_0,1], apart from the zero at x_0 in the noiseless case. In H', the signed quartic after substitution u=1−t is 5u⁴+8u³+9u²−2u−2; it is negative for 0≤u≤0.3 because the positive terms total at most 1.0665. Thus H'>0 and the unique value optimum hits 1 exactly at η=1/24. For the derivative gain the sign before t=1 is that of η−L(t); it is positive below y_0, and L'=1/[3(1−t)³]−5/6>0 on [y_0,1) since y_0>1/3. The derivative optimum is unique, below 1. Relative to endpoint-value gain 1/[64(η+1/3)], every fixed derivative site y>1/3 has a strictly increasing ratio in η, and all maximizing derivative sites satisfy that restriction. Comparing at the earlier optimizer makes the optimized ratio strictly increasing; its limit is 64D(1)²=16/9. At η=1/24 the exact derivative gain upper bound 120207456/2998046875 falls short of the endpoint value gain 1/24 by 113067931/71953125000. Hence there is a single crossing above endpoint activation, and all smaller η are won by the value modality even before its endpoint is optimal. At stationarity G=D(y)(1−y)²; substitution in the equality with the endpoint gain gives the sextic without introducing roots in (y_0,1). The unique crossing thus consists of precisely the two stated sites in their respective modalities.

## originality

PASS

The inspected work covers standard conditioning, derivative-enhanced inference, or genuine modality switches for different targets, sensor budgets, or priors. It does not give or imply the specific freely timed one-reading, equal-variance switch for this integrated-Wiener linear integral, with its exact locations and crossing constant.

## value

PASS

When the target is the linear integral of an integrated-Wiener path, a value reading has better low-noise efficiency but the derivative covariance permits more variance reduction in the high-noise regime. Optimizing sites as well as instrument type is necessary to see the endpoint activation and the later, unique modality switch. The exact constants distinguish these two events, resolve the tie globally, and quantify the large-noise advantage in reduction rather than in total risk. This is useful for the specified single-reading calibrated design beyond a generic posterior formula or a pointwise modality comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
