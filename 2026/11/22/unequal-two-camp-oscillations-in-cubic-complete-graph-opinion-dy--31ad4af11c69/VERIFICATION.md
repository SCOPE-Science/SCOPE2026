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

PASS applies to repairs/2/RESULT.md, not the original unrestricted assertion about strict instability beyond the upper bound. In the original Finding (line 25), take N=3, blocks (1,2), β=3/4. Then β>β_c=2/3 but the only within-block quotient multiplier of the one-step Jacobian is −1, and the difference multiplier is 1/2. The two-step quotient spectrum {1,1/4} has no unstable multiplier. The repair supplies the exact boundary classification. Independent reconstruction: F(v)=v−νPv+k(Pv)^∘3 with the uniform projection removed by P; block deviations are (ℓ/N)d and −(m/N)d. Their cubic difference has coefficient k(m³+ℓ³)/N³=kD/N²; their contribution to mean drift is kmℓ(ℓ−m)d³/N³. Sign reversal forces kd²D/N²=β and the initial drift sets the unique antipodal mean to −H/2. The two phase Jacobians coincide by evenness of the squared deviations. The within-block zero-sum modes and the difference mode diagonalize the quotient, yielding the squared return multipliers from −1+βN(2ℓ−m)/D, −1+βN(2m−ℓ)/D and −1+2β, with absent singleton modes removed. Writing M and q for larger and smaller block sizes, the M-mode forbids strict contraction at M≥2q and is unstable if M>2q. For M<2q both within-block modes are present and the q-mode first hits +1 at β_c≤1; equality is nonhyperbolic and β>β_c unstable there. For M=2q the M-mode stays at −1; the q-mode, if present, hits +1 at 2/3, and if absent the difference mode first hits +1 at 1. In the stable region contraction on the quotient makes the smooth two-step mean drift summable, giving a common translate. Direct rational substitution gives the five-agent orbit and the stated spectrum, with N=3 ruled out for strict attraction. The frozen checker was inspected but not run; its 65 partitions use β=1/4, so the recorded PASS does not test the instability boundary counterexample. The correction preserves the strict-attraction theorem and proof witnesses.

## originality

PASS

The repaired contribution is the exact unequal-size attraction criterion at fixed uniform complete-graph weights, including the odd-size witness and the correct scope of boundary instability. The known balanced interval and general block linearization techniques are not credited as new. No inspected matching primary theorem establishes the unequal-size frontier. The nearest unavailable manuscript remains a scope risk, not negative evidence.

## value

PASS

The strict stability barrier translates population imbalance into a quantified loss of attraction under perturbations that split a homogeneous camp. It resolves the first odd population size in the original uniform model rather than in a perturbed graph and correctly identifies the neutral mean and singleton exception. This is an exact local structural classification, not extrapolation from the five-agent example or a balanced-parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
