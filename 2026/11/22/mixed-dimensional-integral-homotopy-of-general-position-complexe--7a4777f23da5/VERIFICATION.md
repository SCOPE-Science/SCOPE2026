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

Two points in one arm and a third vertex always make a forbidden triple. A hub with a vertex of its own arm or with the other hub likewise cannot occur in a face of size at least three. With no hub, all selections of at most one point per arm are allowed; with one hub, all selections of at most one point per opposite-side arm are allowed. In each converse, a path between selected endpoints passes through no other selected vertex. Thus the join J_U*J_V and the two hub cones contain every larger face and all vertices; the only omitted edges are the intra-arm pairs, the hub-to-own-arm pairs and the hub-to-hub edge, exactly E. Each cone inclusion is already null in the full join by coning from any opposite-side arm vertex, so the second stays null after the first attachment. These cofibrations give the join and the two suspended factors as a wedge. Iterating the discrete-set join formula yields ranks alpha and beta for J_U and J_V in degrees p-1 and q-1, with contractibility if an arm has length one. Joining the two factors gives the alpha*beta family in degree p+q-1; this also follows from the suspension of their smash product. The join and attached cones are connected, so each of the E maximal edges attaches by a null map from S^0 and supplies one circle. The freshly enumerated p=2,q=3, all-length-two case has 12 vertices, 294 nonempty faces, and mod-two Betti ranks 16,1,1,1 in degrees 1–4. Integrality and all parameter cases follow from the attachment proof, not the finite checks.

## originality

PASS

The all-tree multivariate antichain theorem does cover the face predicate and gives a general combinatorial presentation that recovers the face pieces in this family. It does not give their homotopy attachment analysis, the resulting nullhomotopies, or the mixed-degree wedge. The closest actual topology results cover either a single hub or a different, cyclic family. The two-hub result adds two suspended terms and their joint product term by analyzing how the pieces attach, not by reading off the face polynomial or substituting parameters in an existing wedge theorem.

## value

PASS

A uniform homotopy classification for a natural two-branch tree family goes beyond face counts and single-center classifications. The adjacent centers generate a product-rank sphere family separately from the two hub-cone families and the maximal-edge circles. The four-distinct-degrees witness, explicit integral torsion-freeness, and degeneration when some arms have length one give concrete information useful for comparisons with general tree results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
