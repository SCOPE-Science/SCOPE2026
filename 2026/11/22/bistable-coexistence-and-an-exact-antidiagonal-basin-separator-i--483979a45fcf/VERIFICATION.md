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

On the invariant antidiagonal T(x)=f_a(x)-2bx is odd. The primitive antipodal-cycle equation is h(s)=(s−1)e^(−s)=(1−2b)/a, s=r²; the stated strict band is exactly 0<(1−2b)/a<e^(−2), with two branches separated by s=2. For 0<r≤1 the modulus contracts. On r≥1 the radius map is increasing because G′=2b−a e^(−s)(2s²−5s+1)>1−a(e^(−2)+8e^(−3))>0. Its displacement sign, monotonicity and continuity give all three claimed limit cases, in particular no overshoot and convergence from arbitrarily large finite radii. At the antipodal points the same Jacobian occurs twice by evenness of f′; eigenvalues of the return map are the squares of the symmetric and antisymmetric one-step factors. The displayed bounds give a contracting symmetric factor, with antisymmetric factor below −1 at the inner branch and in (−1,0) at the outer branch. Both origin factors a and a−2b have modulus below one. This is the endomorphism sink criterion, allowing a zero multiplier. The sinks have ambient open basins; the exact partition concerns only the antidiagonal. For the endpoints, h″(2)=−e^(−2) yields the stated fold coefficient. For the outer large root g(s)=s−log(s−1)=L, the trial s=L+log L gives residual O(log L/L) while g′ is bounded away from zero there, justifying the stated error. The contents of verify.py were inspected; finite cases are diagnostics, not the proof.

## originality

PASS

The supported distinct claim is the exact antidiagonal basin partition on the full real line in the strict low-gain band, with its full-plane period-two Floquet split and coexistence with the origin sink. The frozen record already excludes the shifted fixed-point root count and fold as independent novelties. The positive-detuning escape-clock record cites this very frozen result for the outer-cycle scale, rather than providing independent earlier coverage of the basin partition. The distinct same-day fixed-point theorem proves material root/fold overlap, not the positive-coupling dynamics.

## value

PASS

The exact sink/saddle split and full antidiagonal basin separator answer a dynamical question left open by compact absorption and numerical stability charts: which attractor is approached from every amplitude along the invariant line, with two genuinely attracting objects in the plane. A stable two-cycle arbitrarily remote as b approaches the endpoint is a structural complement to parameter-by-parameter absorption. The value does not rest on reparameterizing a Lambert-W equation or on interpreting the line separator as the whole planar basin boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
