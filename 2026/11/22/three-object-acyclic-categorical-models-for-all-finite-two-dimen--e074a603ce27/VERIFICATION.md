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

Collapse a maximal tree in the finite connected 1-skeleton (a contractible CW subcomplex), and replace each attaching loop by a based finite edge word up to homotopy; homotopic attaching maps give equivalent cofibers. With no loop generators, a cancelling loop/disk pair allows even a constant relator to be written nonemptily. The composition table defines all pairs on the three strictly ordered objects, and no triple of nonidentities is composable. Every nondegenerate triangle is a cone on its a-edge at the sink; its two edges to the sink are glued along the b-arrow and the composite. This proves the stated graph mapping cone, including parallel edges for one-letter relators. The link graph is precisely the common-root bouquet of subdivided relator loops with private degree-one leaves; retaining both edges of each bigon is necessary. Its path from c_{r,j−1} through the occurrence to c_{r,j} projects to a_i a_0⁻¹ for a positive letter and a_0 a_i⁻¹ for a negative one. Retracting leaves and collapsing the edge a_0 in the base preserve the homotopy cofiber. Collapsing the cone segment over the common root is a quotient by a contractible subcomplex and gives one disk for each loop with exactly its signed word as boundary. Thus the entire homotopy type, not just π₁ or homology, is realized. At most two objects yield a graph; one yields a point. Every finite-rank connected graph type has the two-object parallel-arrow realization, proving the exact minimum trichotomy. The verifier is illustrative; its sample named free_circle_plus_sphere has two circle generators, as its asserted ranks indicate, not one. This naming detail does not affect the theorem or the asserted sample ranks.

## originality

PASS

The sink lemma, two-object case and several sharp families are known. The supported distinct claim is the universal three-object upper bound for arbitrary finite two-complex homotopy types, through a table realizing arbitrary systems of signed attaching words; the exact trichotomy follows with the known dimension obstruction. Neither a finite acyclic model with unbounded object count, a truncated approximation, nor a monoid realizes this same claim.

## value

PASS

The object-count invariant gives a natural sharp problem. Parallel arrows and full compositions carry all arbitrary attaching maps with no growth in object count. The result goes beyond realizing a fundamental group or a family of surfaces: it determines the minimum for all connected finite two-dimensional CW homotopy types, with an explicit construction even for relators having the same abelianization but different words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
