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

The theorem assumes a bounded multiplier and the stated root-plus-edge norm. On a locally finite connected graph the edge difference of a little-space function is in c0(E), since only finitely many edges meet any given ball. The root value and differences give an isometric embedding into the scalar plus c0 space. Hahn–Banach and the summable edge coefficients in its dual show that bounded root/edgewise-null sequences are weakly null; their continuous inclusion gives the same in the big space. For a selected escaping edge at minimum radius r, the distance-to-edge tent of height r−ceil(sqrt(r)) is 1-Lipschitz, vanishes on every fixed ball eventually, and has equal values at the two endpoints. Its root value is zero and an edge leaving the plateau gives norm one. The product jump divided by r times the symbol jump tends to one; compact operators kill the weakly null tents in norm. Escaping singleton indicators give the A lower bound by the same argument. B is finite and the two radius conventions agree: testing the multiplier on min(d(a,·),r), which is constant outside a finite ball and has norm one, bounds r|Δψ| for edges of minimum radius r. Thus a radius difference of one incurs an error tending to zero. Independently checked the A=0 upper bound: multiply by a radial cutoff η that vanishes through R, ramps at slope 1/R to radius 2R, and is 1 thereafter; M_ψ−M_(ηψ) has finite rank. On an edge oriented from larger radius v to smaller radius w, the three product-rule contributions for a unit f are bounded by A_R, B_R and 2A_R respectively (|f(w)|≤d(a,w) whenever the cutoff contributes, and d(a,w)≤2R on a ramp edge). The root contribution is zero. This yields the asserted equality by taking R→∞ when A=0, consistent with Proposition 8.3. The ladder distances are k+i; the horizontal jump times radius tends to 2, the vertical jump vanishes, and the symbol tends to zero. Boundedness follows directly by the edge product rule from bounded amplitude and weighted jumps, also on the little space since little-space f obeys |f(v)|/d(a,v)→0 by summing along root geodesics. This proves the exact sharpness claim and its positive scalar multiples. The checked finite-ladder script was inspected but not executed; it is not used as proof.

## originality

PASS

The supported distinct claim is the B coefficient-one lower bound on arbitrary locally finite connected graphs on both spaces, and the corresponding A=0 exactness including cyclic graphs. The A lower bound and the restriction of the A=0 identity to previously covered tree spaces are not new. Best-of-knowledge comparison, not a priority certificate.

## value

PASS

This closes the explicitly identified missing B-dependent lower-bound question in the all-graph framework, with best possible coefficient. In particular the B term can entirely determine the essential norm while amplitude tends to zero, a case the previously known amplitude lower estimate cannot distinguish. The edge-centered witness works on graphs with cycles and against all compact operators on both spaces, not just compact multipliers or approximants in a tree coordinate system. The ladder demonstrates the resulting nonzero sharp invariant on a cyclic graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
