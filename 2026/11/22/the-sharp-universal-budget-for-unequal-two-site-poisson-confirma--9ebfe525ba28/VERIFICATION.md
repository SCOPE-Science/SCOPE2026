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

Independent presences and encounter streams give the stated failure product. With y=B/2, t=|x-y| and a=(1-p)e^y/p, the scaled product has difference from t=0 of t^2(2aF_y(t)-1). The even power series for F_y has coefficients (y-2k+1)/(2k)!; for y<=3 it is strictly decreasing, and for y>3 division of its derivative by the last positive monomial gives a strictly decreasing function on t>0. Thus every interior F_y(t) strictly exceeds the smaller endpoint value. For G(y)=F_y(y)-F_y(0), y<=3 gives strict negativity (including y=3); differentiating under the closed formula gives the stated y^4G'' and the lower bound ((y-2)^2+2)cosh(y)-2y-6>0 on y>=3. Strict convexity from a negative initial value and divergence to positive infinity force a unique root there. When G<=0, either the equal split is at least as good as concentration and all intermediate t are strictly worse, or the negative difference from t=0 at concentration is multiplied by a strictly smaller t^2/y^2 in the interior lower bound, again excluding an interior optimum. For y<=1, F_y(y)<F_y(0)<=0 so concentration alone wins. When G>0, take a small positive t with 0<F_y(t)<F_y(y) and choose a strictly between their reciprocal doubled values in the specified order; neither candidate endpoint can minimize and some unequal interior optimum exists by compactness. This uses a potentially different p at each B. For each fixed p, eventually strict concavity of -log q_p and its finite increasing limit exclude every bounded small coordinate, then force equal division. Independent rational arithmetic in audit-checks/poisson.py (alternating small-argument exponential bounds raised to the 16th power) certified both root signs, also bracketing B_* between 8.4020630239297547240 and 8.4020630239297547250, and certified the asymmetric failure probability strictly below both controls.

## originality

PASS

Credit the earlier-indexed or same-date evidence of asymmetric globally optimal splits in this exact model. The supported distinction is only the sharp universal boundary, including existence of some p at each supercritical B, not the model, S-shaped reformulation, or occurrence of asymmetry itself. Relevant general theory could facilitate a proof, but the inspected exact-model theorem and accessible comparisons do not establish the model-dependent sign test, its unique crossing, or the two sides of this universal boundary. Access risks remain for the closest historical general theory.

## value

PASS

The same model can favor concentration, equal allocation or strictly unequal allocation. An exact sharp boundary universal in the unknown occupancy probability is a natural design invariant: it certifies that testing concentration and balance suffices below it, and that this restricted policy can fail at every larger budget. The fixed-p return to balance also distinguishes the universal statement from a monotone phase claim. This is materially more informative than the already established isolated counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
