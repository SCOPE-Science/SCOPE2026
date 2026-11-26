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

With X∼N(d,s), O=(L−|X|)₊ and positive overlap iff |X|<L, the two metrics are Gaussian smoothings of a tent and an interval indicator. The tent's distributional second derivative is δ₋L−2δ₀+δ_L, yielding F′=φ_s(d)[exp(−L²/(2s))cosh(dL/s)−1]. With z=L²/(2s) and a=2d/L this gives the sign of H_a(z)=log cosh(az)−z. For a≤1 it is strictly negative for z>0, including a=0. For a>1, H_a starts at zero with slope −1, is strictly convex and grows to +∞, giving one positive crossing and a unique maximum in s. At a↓1, H_a(C)→H_1(C)<0 for each C>0, so z_F→∞; (a−1)z_F=log 2−log(1+exp(−2az_F)) proves the claimed onset. F is continuous at zero. Differentiating Gaussian interval mass gives the difference of the two weighted densities in the record, with one positive zero at the stated s_P when d>L and strictly negative derivative when d≤L. At d=L the mass tends to 1/2 as s↓0 but the deterministic positive-overlap probability is zero. For d>L, layer cake expresses F as the integral of the narrower interval probabilities with half-width u∈(0,L). Their maximizing variances are q(u)=d²(u/d)/artanh(u/d), strictly between q(L)=s_P and d². Their derivatives are strictly positive at s_P and negative at d²; integration proves the strict ordering. An independent root bisection and split-at-zero quadrature give σ_F=0.6081417030881335, F=0.32447563410484603 and P=0.657492697428084 in the printed example. The supplied checker was read, not run.

## originality

PASS

The distinct claim is the paired global variance classification: different exact duration and occurrence thresholds, the onset law for the positive duration optimum, and strict ordering of the two optima when they coexist. Gaussian interval-mass calculus, heat smoothing, option-payoff representations, and qualitative nonlinear responses to phenological variation are not credited as novel. The strongest available neighbouring statements treat different parameters or metrics and do not establish this joint result.

## value

PASS

Expected overlap and probability of any overlap are both natural measurements but are not interchangeable. The interval L/2<d<L has opposite initial responses for these two metrics in the same model. The touch discontinuity, distinct variance optima and strict comparison establish more than a generic nonmonotonic effect. The sharp offset thresholds and quantitative onset tell a researcher exactly when the qualitative distinction matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
