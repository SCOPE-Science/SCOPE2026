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

The 13 points, three fixed double conditions and moving quadruple yield 29 rational jet rows on 28 degree-six monomials. A bounded independent reconstruction at Q0=(-31:-9:15) gave rank 27, the affine singular eliminant y(5y+3)^5/3125, and specialized x-gcds x and (15x+31)^3/3375. The full gradient at the four roots at infinity detects only P1 and P3. Exact local degrees 2,2,2,4 and nonzero tangent discriminants give ordinary singularities, not just assigned vanishing. The finite singular support implies the sextic is reduced. If reducible, a component of degree e<=3 has at most 7 total intersection multiplicity with its complement (at most 4 at the quadruple and 1 at each node), excluding e=2,3 by Bezout. A line must pass through Q0, and exact substitution excludes the four lines through it and the roots at infinity. Independent replay: /workspace/branches/879fc365-80e6-4920-92fe-ac890fd3bb44/independent_check_record3.py; the supplied script was inspected, not executed. Malara's generic rank result lets the solution form a kernel line on the rank-27 open containing Q0. Blowing up the four disjoint sections and dividing by their specified exceptional powers gives a relative hypersurface. At the witness it is smooth, including at exceptional intersections, by the reduced tangent cones. The relative nonsmooth locus is closed and its image is closed by properness, so after shrinking it misses every fiber. Squarefree cones and geometric integrality are also open here. The full basket therefore holds generically, not at every Q. Arithmetic genus 10 minus delta 3+6 is 1; in characteristic zero the ordinary-point polar contributions are 3(2)+4(3), so the dual has degree 12. No origin or exceptional-parameter classification is required. The citation heading is Section 6.1/Proposition 6.1, not a numbered Example 6.1.

## originality

PASS

The scheme, generic one-dimensional interpolation and geometric irreducibility are prior or follow directly from Malara's witness and openness. The supported distinct result is the complete generic ordinary-singularity census; genus and dual degree are its classical consequences, not separately novel genus/class formulas.

## value

PASS

The sextic is a concrete originating example of a mixed fat scheme, and its uniqueness and irreducibility left room for additional or nonordinary singularities. Verifying the full generic basket identifies its normalization and dual geometry. This is an exact geometric description of the motivated family, not a recomputation of the known Hilbert-function result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
