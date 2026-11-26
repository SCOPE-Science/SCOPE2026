---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The compact fixed-sum simplex admits a maximum; shifting stock from a positive coordinate to a zero coordinate strictly improves it by f′(0)>f′(x). Equal marginal returns and the decrease then increase of f′ around 2 restrict an asymmetric stationary point to 1<a<2<b. Exchange of stock between two large coordinates has positive curvature, so exactly one b is possible at an optimum. Equating f′(a)=f′(b) gives u=a−1=d/(exp(d)−1) and b−1=d/(1−exp(−d))>1. The positive u″ follows from d>2tanh(d/2). Thus S′_m rises strictly from 1−m/2 to 1. With v=b−1, f′ matching gives dv/du=−[(1−u)/u]/[(v−1)/v]; the fixed-sum exchange curvature has sign of m−1+dv/du, opposite S′_m since u′<0. When m≥3 this excludes the descending asymmetric branch. At the fold the equal vector strictly wins: H′=[f′(a)−f′(S/m)]S′ with positive bracket for a<S/m<2 forces H to decrease from 0 up to the fold. It then strictly increases up to the positive root d₂ of S_m(d)=2m. At S=2m the cubic coefficient e^(−2)[(m−1)³−(m−1)]/6 for the displayed perturbation is strictly positive; the surviving candidate wins and H(d₂)>0. This establishes a unique tie with one strictly positive gap, and for S>2m equality has positive constrained second variation. For m=2, S₂ is strictly increasing from 4, so the equality and asymmetric ranges and continuity follow separately. Independent numerical replay `python /workspace/review_replay.py 5` gives S_c(3)=5.774313471725124760…, d_c=1.397499519593884473…, a_c=1.458937984043746762…, b_c=2.856437503637631236…, consistent with the displayed rounded figures. This is not a field calibration or proof by experiment. Supplied checker inspected, not run; the separately reported multistart comparisons were not independently reproduced.

## originality

FAIL

A distinct Resultary record states the same global optimizer theorem and unique crossing under an exact change of physical interpretation, with no mathematical change in objective, feasible set, or parameters. The same repository date, 2026-11-22 UTC, does not resolve temporal priority, and no chronology or copying is inferred; the failure is demonstrable mathematical overlap, not a priority judgment. A second distinct record already covers the continuous/discontinuous split in the spawning-stock formulation. No substantive distinct mathematical claim remains in the frozen result.

## value

FAIL

The underlying threshold is an interesting invariant of the constrained optimization, but the only difference supported here after the exact comparison is a change from irradiance to spawner density. No new mathematical invariant, useful sharpened bound, or validated fishery conclusion follows from that reinterpretation under identical hypotheses. The displayed three-patch values are evaluations of the already identified scalar crossing. No valuable distinct remainder is established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
