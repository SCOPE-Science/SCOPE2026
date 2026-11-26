---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a pointed isomorphism h:M→N, atomic agreement and element moves use h and its inverse; identity witnesses give bitotality. An inclusion i:M→M′ is matched by i∘h⁻¹ into the same M′ on the embedding side. For an embedding ρ:N→N′, adjoin a genuinely disjoint copy of N′\ρh[M] to the unchanged underlying set of M and pull the structure back along the bijection extending ρh. This makes M a literal substructure of the new copy, which belongs to the class by isomorphism closure, and the bijection commutes on all old parameters. The infinitary modal conclusion follows from Adam-Day’s Theorem 21. This proof works for arbitrary signatures and cardinalities under the stated embedding convention. The included artifacts/verify_replete_bisimulation.py was inspected, not run: its loops check the transport for bounded simple graphs only, and the reported assertion count is not independent evidence for the theorem.

## originality

FAIL

Adam-Day’s stronger ambient result already implies the full equivalence on every isomorphism-closed subclass, not just on classes axiomatized by theories. Apply Theorem 28 with the empty theory in the same language. In Definition 18 every related pair of worlds is isomorphic; every matched arrow has an isomorphic target. Restrict both systems to the worlds in the given class: bitotality and both arrow clauses survive, since any matching world automatically belongs to the class and the subsystems retain all arrows between retained worlds. This also works for the specific relation of all pointed isomorphisms: for any desired h:M→N, choose a witness ξ:M→N₀ in the restricted iso-bisimulation and use the isomorphism h∘ξ⁻¹:N₀→N to precompose the embedding-side moves or their matches as appropriate. The commuting squares then give target isomorphisms with the desired transported tuples. Neither non-elementary classes nor arbitrary cardinal spectra require a new argument beyond this restriction and reindexing.

## value

FAIL

The statement is a convenient concise formulation, but an induced restriction retaining every isomorphic matching target is a routine consequence of the prior result. Exact cardinalities and arbitrary spectra illustrate it without adding a new obstruction, classification, or independent invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
