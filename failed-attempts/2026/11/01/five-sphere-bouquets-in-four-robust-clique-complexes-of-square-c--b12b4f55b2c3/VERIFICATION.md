---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For an admissible set, choosing one private vertex per occupied petal bounds the support by three. The at-most-two-support subcomplex is a hub cone: a new independent set containing the hub uses only private middle vertices, so has size at most three. With three occupied petals, the private set in each is a clique of the path P3. For each triple, the join of the three clique complexes of P3 is a 5-ball (join of three subdivided intervals), and its boundary consists exactly of faces missing some middle vertex. These are precisely the faces of that join in the hub star. All non-star faces belong to one such ball and distinct balls meet only in the star. Collapsing the contractible hub star, a simplicial subcomplex, gives a wedge of these 5-balls modulo boundary, including the contractible m<3 cases. Independently, exact reconstruction of the submitted three-petal certificate gave 537 faces including empty, 268 valid pairs, all 2,130 oriented incidences acyclic, and sole unmatched mask 876. On excluding the empty face the hub also becomes critical. Thus the finite Forman step and the frozen all-m low-support quotient argument both work.

## originality

FAIL

The earlier Resultary record 746320ce0145 already proves and explicitly states the identical all-m five-sphere wedge including its binomial multiplicity, under the same independence-number convention. It proves the stronger all-k≥4 formula for exactly the same bouquet family.

## value

FAIL

An unknown integral wedge theorem for one-hub graph bouquets would be useful, but this exact infinite-family classification was already available in a broader result. The finite matching and specialized gluing proof do not furnish a new invariant, stronger range, or additional structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
