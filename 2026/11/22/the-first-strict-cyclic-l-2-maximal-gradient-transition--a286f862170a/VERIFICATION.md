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

Here V₂ is the ℓ² norm of first cyclic differences, not a second derivative. Replacing complex f by |f| only decreases the denominator and preserves the numerator; constant modulus gives zero numerator. For nonconstant modulus, subtracting its minimum within the nonnegative cone and rescaling are legitimate because all averages shift equally and the variation kills constants. At C₃ the maximal values at (u+v,v,0) reduce to the two cases in the proof; symbolic expansion verifies the energy identities, including equality for u≥v. At C₄ rotation and reflection place a maximum 1 at zero and a minimum 0 either adjacent or opposite, covering ties as well. An independent exact calculation generates averages from intervals in a doubled list, obtains the active cells by intersecting pairs of supporting lines and testing all constraints, and minimizes the quadratic deficit over vertices, all feasible vertex-to-vertex segments, and feasible positive-definite critical points. Only closures of full-dimensional cells are needed by continuity, since nonidentical affine ties lie on finitely many lines. An interior stationary point with an indefinite Hessian cannot be a minimum; if the Hessian is positive semidefinite but singular, a null line carries the same minimum value to the boundary. Linear or concave edge restrictions take a minimum at an endpoint. Thus the candidate list is exhaustive, not a grid scan. The replay gives six and seven cells with respective minima −1/12+5√13/156>0 and 0, and directly verifies the active witness averages and the squared ratio (7+√13)/36>1/4. Hence both constants are sharp in the stated domain.

## originality

PASS

The nearest distinct records share the graph or the seminorm, and the line results share first differences and uncentered averaging, but none of the compared theorems gives the sharp first-difference ℓ² ratio on the full family of uncentered cyclic arcs at these sizes. Credit is for those sharp constants and their strict transition, not for the general maximal-variation program.

## value

PASS

The sharp cyclic first-difference ratio is a natural stability quantity for uncentered maximal averaging. The first nontriangle cycle changes the arrangement of contiguity and creates a provable strict increase, with a non-indicator optimizer that improves on all indicators. The globally sharp algebraic constant and realizing pattern distinguish a genuine cyclic and amplitude effect from the previously studied centered, vertex-norm or indicator results. This is an independently useful exact small-cycle benchmark, not a claim about arbitrary cycle sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
