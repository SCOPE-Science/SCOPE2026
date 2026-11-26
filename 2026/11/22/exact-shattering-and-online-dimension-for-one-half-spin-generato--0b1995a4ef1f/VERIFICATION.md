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

An all-positive trace makes the support totally singular, and excluding one point while including the others rules out linear dependence. At n independent points the span of any n−1 lies in exactly one generator of the chosen system, ruling out that one-negative trace. For an independent orthogonal support of size ≤n−1 I independently reconstructed sufficiency without a fixed-system transitivity assumption: extend representatives to one side e_1,…,e_n of a hyperbolic basis (Witt extension, valid also in characteristic two for this split nonsingular quadratic form). Use e_i for desired positives and f_i from the paired basis for desired negatives; use e_i on unused pairs except on one spare pair where either choice is allowed. The two candidate generators share an (n−1)-space, so they belong to opposite systems. This realizes the label in either fixed system and verifies the universality asserted by the source's incidence-avoidance argument. The count of projective singular points in rank r follows by counting vectors according to x=0 or x≠0, removing zero and dividing by q−1. A quotient point lifts to q^j points after j independent orthogonal choices, giving the product with division by k!. Every face extends to size n−1. Along an all-positive branch of a complete online tree, each queried point must add one independent direction to allow the negative branch; after n−1 labels only one concept survives. Static shattering provides the matching depth. The e_1,f_1,e_1+e_2 nonface pattern violates matroid parallelism; three points on a singular line give a missing triangle. In rank three the Klein quadric identifies adjacency with intersecting lines, and two nonadjacent points span a hyperbolic plane whose split orthogonal complement supplies a common singular neighbor. Thus the graph is connected and is a wedge of E−V+1 circles with the stated counts. My own bounded `/tmp/opencode/frozen-review-repro.py polar` parameterized binary generators by their x-projection and an alternating form, then counted actual trace-fiber shattering in both families, exhaustively in ranks 2–4; counts match all binary examples. The source's finite programs were inspected, not executed. The q=3 example follows by substitution, and the general field/rank theorem uses the geometric proof rather than enumeration.

## originality

PASS

Classical polar incidence, the ruling split and the rank-three Klein identification are input. The distinct assertion is the full Boolean trace description and its sharp online cutoff for one prescribed ruling, and the resulting face invariants. The strongest inspected symplectic result changes both the concept family and the terminal rank condition.

## value

PASS

Choosing one ruling is canonical and costs a direction for both static and adaptive learning despite availability of full-rank totally singular frames. The support theorem, coefficients and complex structure make that distinction explicit for all field sizes and ranks, and the rank-three topology uses the dimension cutoff rather than merely reciting the Klein correspondence. Higher-rank homology is outside the claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
