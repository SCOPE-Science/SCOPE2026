---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The standalone standard-library program `verify.py` independently tests the condition by constructing each clockwise geodesic arc of length three through \(\lfloor n/2\rfloor\) and checking whether an edge set places three selected edges within an arc. It does not use the gap characterization to decide feasibility.

For all \(3\le n\le18\), the program exhaustively tests all \(524280\) subsets, finds \(3441\) valid edge-general-position sets and \(1076\) inclusion-maximal ones, and matches every coefficient of the face and facet polynomials. It also compares the triple and quadruple gap predicates for every feasible set and checks the criterion for triple extendability by explicitly testing one-edge additions.

For \(19\le n\le26\), it independently tests an additional \(351654\) subsets of cardinality three, four or five and agrees with both closed forms and the five-set impossibility claim. On execution it prints `VERIFY_OK` or raises an assertion error.

The computations establish only these finite instances. The general formulas follow from the cyclic-gap equivalence, the summation bound ruling out five edges, inclusion-exclusion for triples and four-gap composition counting. The literature comparison supports only a provisional claim of publication priority, not an independent originality certification.
