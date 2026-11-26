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

For a one-dimensional simplicial graph the descending link is a nonempty cone exactly when a vertex has a unique earlier neighbor. The all-order triangle enumeration gives four discrete non-hub atoms; requiring o to precede both leaves leaves two inward atoms, and prescribing its one earlier neighbor in that triangle leaves no non-hub atom there. Independent enumeration of the 24 square orders gives maximal non-hub pairs AB, AC, BF, CD, DE′, E′F. Requiring o to have no earlier square neighbor gives AB, AC, CD; prescribing u or w as its only earlier square neighbor gives respectively the singleton choices B,C,E′ or A,D,F. Because local orderings interleave independently on each side of o, these exactly determine the base and all hub links, not just upper bounds on faces. No face has two hub apices. For q≥2 each apex link contains a collapsible path as a join factor; lifting link-collapse pairs into the cone and removing its final apex-edge pair preserves the entire base. For q=1 the triangle apices still collapse, while the two remaining links have homotopy type of a wedge of two p-spheres. Their inclusions into the p-connected base are null, so their cone attachments add four (p+1)-spheres in total. Joins multiply the face polynomials, and each link and base is pure in the required dimension, giving all three polynomial terms and purity. Read supplied checker, verification note and output; did not execute the checker. Its finite mod-two ranks do not certify the integral theorem, which follows from the collapse and homotopy arguments.

## originality

PASS

Exact earlier cases (p,q)=(1,1) and (2,1), the one-type results, and the disjoint join theorem are credited. The all-positive-parameter mixed classification with its uniform relative collapse and polynomial is not supplied by the strongest material comparisons. Exact catalogue hit a32a0d575582 is the assigned record itself. Priority is not certified.

## value

PASS

This determines a natural integral homotopy invariant and an exact face enumerator of a named complex on a family where the ambient disjoint join theorem cannot be used. It explains why adding the second square changes the topology: each surviving square-apex link acquires a collapsible path factor, eliminating four sphere summands while shifting the top dimension. The result gives both a structural reason and an explicit collapse, rather than just additional finite Betti tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
