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

The Finding is true. Over the algebraic closure, let g=0 be the conic and choose a cubic F whose section on the conic vanishes simply at the six points. This section exists by restriction of cubics to the conic; the cubic forms through the six points are spanned by g times the linears and F. At each basepoint g,F are transverse, so the blow-up resolves the anticanonical map. Its image in coordinates (Y,W) is g(Y)W=F(Y), birational by recovery of Y as the old plane coordinates away from the conic. At [0:0:0:1] the quadratic part is the smooth conic form, an ordinary node in odd characteristic. A singular point away from there would require g(Y)=F(Y)=0 and dependent plane gradients, contradicting transversality. Bézout with the conic gives anticanonical degree at least d for each other nonexceptional irreducible plane transform of degree d, so adjunction leaves only the fifteen secants and the six exceptionals as (−1)-curves. The strict conic is the sole (−2)-curve. A negative support's (−1)-curves must be disjoint by principal minors; adjoining the conic gives Schur complement −2+s, where s counts selected exceptional curves, so requires s≤1. For invariant S and ground-field ample A, solve P=A+Σ b_i C_i with P·C_i=0; without the conic b_i=A·C_i, and with it b_Q=(A·Q+Σ_E A·E)/(2−s), b_E=A·E+b_Q and b_L=A·L. All are positive, P is nef and P²=P·A>0. The reduced sum D_S descends, and A+kD_S for k>max b_i has negative support S, including the empty case with A alone. Independently enumerated by invariant exceptional sets (unions of marking cycles). On the remaining labels, pairwise-intersecting secant edges are empty, a single edge, a unique-centre star with at least two edges, or a triangle. For residual cycle counts f fixed points, d transpositions, t three-cycles and h cycles overall, the number is 1+binomial(f,2)+d+f(2^(h−1)−f)+binomial(f,3)+fd+t, with zero star term when f=0. Summing over exceptional cycle subsets and retaining Q exactly when allowed gave all eleven pairs, all support-size profiles, and both orbit decompositions (via fixed counts of the powers). Frozen proof line 62 omits the +1 from q^k+1 in Möbius inversion for the number of closed conic points. This affects only degree one; the Finding uses the correct q+1. At q=3 the counts in degrees 1 through 6 are 4,3,8,18,48,116, which suffice except for six singletons; for q≥5 monotonicity of the closed-point counts for d≤6, or the explicit formulas, supplies every partition. No repair package is warranted for this otherwise true but covered contribution.

## originality

FAIL

Distinct same-date record 709ff6674212 already gives all eleven total counts and a linked supplement tabulates each complete profile of supports containing the sole (−2)-curve. Summing the entries for each cycle type gives exactly the second column and certifies both the stated collision and the joint injection. Its complete chamber-cycle data also give both orbit patterns. This is exact coverage of the novel invariant calculation, not just the identity row or a similar title. The other Finding assumes characteristic at least five, whereas the assigned statement includes characteristic three. Its same labeled cycle computation applies there without change; the extra field realization is the elementary closed-point feasibility check on the conic, not a new chamber invariant. No relative priority is inferred from the shared date.

## value

FAIL

As invariants, the total and conic-refined chamber counts are natural and potentially useful; the problem is not that the counting family is finite. The assigned numerical table and its distinguishing implication are already available by inspecting and summing a stronger support profile, and field-three availability follows from the routine conic closed-point check without changing the action. This does not leave a substantive new exact invariant worth a separate repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
