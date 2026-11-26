---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The compact simplex has a minimum of the log-denominator. Moving length into any zero gap from a positive gap strictly lowers that cost. Equal derivatives at an interior stationary point give equal or reciprocal gap lengths. Two long gaps have a negative transfer-direction curvature, so a nonuniform minimum has two short gaps x and one long gap 1/x. The mixed tangent direction (1,1,-2) excludes x>1/sqrt(2) on the two-short branch. At the merged branch the unequal denominator exceeds the equal one by 31/2916; at s=3 the unequal value is 125/16 against 8. On (sqrt(8),3), the stationary log-cost difference has derivative g'(a)-g'(s/3)<0 because 0<a<s/3<1. Beyond 3 the equal point has negative tangent curvature. These arguments account for all minimizers, including both endpoint values of the crossing bracket. For two gaps, the denominator is s^2+(uv-1)^2 and the attainable products range continuously from 0 to s^2/4, giving continuous onset at s=2. Independently, setting u=a^2 gives the crossing equation 729u^2(1+u)^3=(4u^2+13u+1)^3. Exact rational sign bisection on [1/4,1/2] reproduced 2.8475678593462526382177 and short gap 0.6294894794440552583894.

## originality

PASS

The supported distinct result is the global three-gap inverse-quadratic switch, its coexistence configurations, and the contrast with the continuous two-gap onset. The closest available connectivity and allocation statements do not supply the same objective or its global crossing. This is a bounded comparison, not a claim of absolute priority.

## value

PASS

Three is the first route length in this model where an unequal global optimum appears discontinuously while the equal solution remains a strict local optimum. This supplies an exact counterexample to using loss of local stability as the onset criterion in simple serial placement models. Giving the crossing, multiplicities and minimal number of hops makes the result useful as a benchmark; the significance is not an assertion about actual habitat design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
