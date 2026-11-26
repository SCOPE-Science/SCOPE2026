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

The weights are positive and bounded by a summable geometric sequence. Normalizers cancel in adjacent ratios. At fixed α, the log increment of the higher/lower rate ratio is (1+α)[F(n+1)−F(n)]−α(b−a), where F=log((1+e^(−ax))/(1+e^(−bx))). For an independent check of the turn, write F'=b/(1+e^(bx))−a/(1+e^(ax)). Its sign changes exactly once from positive to negative because (1+e^(bx))/(1+e^(ax)) rises strictly from 1 to infinity. If F'≥0, then b/(1+e^(bx))≥a/(1+e^(ax)); comparing their squares times e^(bx) and e^(ax) shows F''<0 there. Thus whenever d(x)=F(x+1)−F(x)>0, x is before the maximum of F, and F'(x+1)<F'(x) whether x+1 is before or after that maximum. Hence d decreases strictly while positive and cannot re-enter its positive region. The first step sets the full threshold by d(0)=H; every positive level has at most one downward crossing, giving the strict steps and tie cases. H/(b−a) is a strictly decreasing average as b increases, from (1+e^a)⁻¹ to 0, so c(a,b) decreases from e^(−a) to 0 and the claimed restoration rate is unique where it exists. At fixed θ, the positive unit decrements h_n of the strictly convex log(1+e^(−θx)) decrease to zero; the adjacent log masses are (1+α)h_n−αθ, yielding strict discrete log-concavity, all modes and the adjacent ties. The two witness ratios reduce to the stated exact rational inequalities; scalar bisection independently gives b_*≈2.19009277655 for the example.

## originality

PASS

Barbiero–Hitaj define the same sampled-density count model and note the possibility of positive modes, but the inspected generalization does not give its fixed-shape pairwise rate phase diagram. The strongest matching catalogue and published alternatives treat either a different discretization or a different family. An earlier single-turn theorem for two rates in the same continuous parent would imply much of the discrete result by sampling; no such comparison was identified in the accessible relevant passages, and the limits of the targeted search are recorded below.

## value

PASS

For a motivated count model, this identifies exactly when increasing rate orders the observations by likelihood ratio and when it instead gives a single ratio peak. At small shape it shows that increasing the second rate further can restore the stronger order after a small increase fails, and gives the exact unique restoration criterion. This provides a useful parameter comparison for monotone testing or modeling, beyond the existing observation that modes need not be at zero. The mode staircase supplements rather than carries the value case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
