---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

Crown adjacency is [[0,J-I],[J-I,0]]. Because 2 is invertible in characteristic 3, change to sum/difference shores gives B=J-I and -B, and J^2=nJ. For n divisible by 3, J has a nontrivial rank-one nilpotent J2; the corresponding ±1 adjacency blocks lift to J4 at the temporal eigenvalue ±1, accompanied by J2 pairs. For n=1 mod3, the constant lines have spatial eigenvalue zero and produce two irreducible quadratic X^2+1 blocks of order 4. For n=2 mod3 all temporal pieces are J2(±1). Taking fixed dimensions min(size,3^v3(t)), conditioned on parity and divisibility by four, gives each of the three source formulas and exact minimal orders; invertibility provides immediate periodicity and Mobius populations. Independently built matrices and checked every time through the asserted order over F3 for n=5,...,9. All n and field extensions follow from the algebraic decomposition, not finite testing.

## originality

PASS

A crown graph is the matching-deleted K_{n,n}, equivalently the bipartite double cover of a clique. Klee–Stamps Proposition 8 computes its Laplacian characteristic polynomial over ordinary characteristic, but not the exceptional characteristic-three Jordan time dynamics. Existing exact finite-field wave statements for full bicliques and cycles intersect only different or excluded graph sizes; none implies the displayed all-size time census.

## value

PASS

Deleting a single matching from a complete bipartite graph sharply changes reversible-wave clocks and creates a genuine three-residue modular Jordan trichotomy. Full fixed-iterate dimensions and primitive orbits are natural exact graph dynamical invariants, useful for classifying finite reversible linear cellular rules, without asserting arbitrary-graph generality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
