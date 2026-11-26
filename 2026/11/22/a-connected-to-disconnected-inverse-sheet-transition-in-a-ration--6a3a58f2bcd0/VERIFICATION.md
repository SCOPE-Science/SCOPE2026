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

Assessed the readable complete finding in /workspace/repairs/3/RESULT.md. Frozen RESULT.md contained 11 form feeds, three carriage returns and seven tabs where TeX commands had been interpreted as control escapes, and a split w≠0 condition. The repair restores the equations, specifies the fold condition and excludes the ordinary Whitney cusp interpretation. For c≠0 the affine changes reduce the map to (w,H), with the source and target coordinate changes of opposite orientation, so the original determinant is -H_y. A fibre is exactly the zero set of the cleared monic cubic (the clearing factor never vanishes for real y). Bounded image forces bounded w, so an escaping subsequence would have |x|,|y|→∞ and unbounded first image coordinate. The strict convexity in the proof is Q''>0, not the self-audit's Q>0. Together with Q(0)<0 it gives two simple roots of opposite signs, and H''≠0 there proves ordinary folds. The monotonicity intervals give the whole 1/2/3 classification and Jacobian signs (+,-,+) or (+), hence degree +1. Interpolating between ordered folds gives the one strip. At a=-1 the two fold values are 0 and q(w)^3/2 with q^3+3q=2w, so there is one connected open region over each sign of w and none over zero. At the pinch the cubic is y^3 and the differential of the determinant vanishes, which rules out an ordinary Whitney cusp. The expansions give width 4|w|^3/27+O(|w|^5) at the pinch and 4δ^(3/2)/(3√3)+O(δ^(5/2)) for the opening on w=0. I checked the repaired control bytes (none remain) and independently used symbolic differentiation/expansion and exact root isolation in SymPy; the seven explicit rational cases and expected multiplicities are reproduced in the corrected finding, using Poly(P,y).intervals() after substituting those triples. These sample fibres are not the general proof. The source checker was inspected, not executed.

## originality

PASS

Best of knowledge for the corrected a≤−1 theorem. The map, standard cubic and fold methods, and an inverse study in the complementary a>−1 regime are antecedents. The surviving contribution is the global three-preimage topology on and below the singular parameter and its two exact width laws; it is not a claim to have introduced the map or cubic root classification.

## value

PASS

This is a global inverse ambiguity classification for a concrete map already studied at and on both sides of the parameter boundary. It tells a reader exactly which targets have multiple distinct backtraces and where the fold curves cease to bound a single strip. The critical point is degenerate, so a routine ordinary-cusp description would miss the exact two-component geometry and the different cubic target and 3/2 parameter scalings. No downstream result for entire basins or forward chaotic dynamics is presumed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
