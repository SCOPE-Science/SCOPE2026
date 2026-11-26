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

The reduced Świątkowski complex in weight 3 has no degree-4 term; its top homology is the integral kernel, with exactly 14080 columns and 31680 rows in the top differential. A cycle's fundamental chain is the sum of its incoming-to-outgoing half-edge differences. By naturality from the disjoint union of the three circles with one particle per component, the signed tensor product represents the actual geometric torus, not merely an abstract closed vector. Independent exact replay: run python3 /workspace/audit-evidence/1/recompute.py with the co-located frozen BASIS_CERTIFICATE.json as its argument. The replay builds the graph from two pentagons and two poles, checks the frozen edge set, enumerates cycles by subsets and permutations (20,30,72,240 at lengths 3–6), obtains all 700 triples, checks the listed 110-element minor has determinant +1, reduces every short torus against the first 100 rows over the integers, and independently obtains mod-2 rank 13970 using a different local anchor and row order. Mod-2 rank is a lower bound for rational boundary rank, so the kernel has rank at most 110. The unit minor gives a primitive subgroup of the chain group of rank 110, hence all of the kernel. Its first 100 generators are exactly the triangle triples and are saturated already, with quotient Z^10. No cycle in a disjoint triple can exceed length 6 on 12 vertices. Neither the supplied verifier nor a numerical rank result was used as a substitute for this check.

## originality

PASS

The exact graph-specific integral basis and minimal cycle-length threshold were not found in the inspected coverage. Distinct same-day results treat other graphs; general methods and product-generation results do not supply this rank, saturation and sharp threshold together.

## value

PASS

The icosahedron is a natural highly symmetric graph, and short disjoint cycles give geometrically localized commuting-travel motions for three particles. A Betti number alone cannot say which such motions account for the full integral lattice. The computed threshold and primitive short sublattice distinguish the 100 triangle products from the ten necessarily longer generators and give reusable exact data for comparing graph geometry and product generation. It is a motivated finite cutoff, not a general graph theorem or a table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
