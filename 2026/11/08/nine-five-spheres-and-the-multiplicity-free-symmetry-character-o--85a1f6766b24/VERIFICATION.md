---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS: Explicit labeled Franklin graph is cubic on 12 vertices with 18 edges, cyclic edges i-(i+1) and alternating long chords. Faces are exactly vertex subsets omitting every closed neighborhood N[v], i.e. complements of dominating sets; independent 4096-mask computation yields 2417 faces including empty, vector by dimension (-1 through 7) (1,12,66,220,483,696,612,276,51). Independent sorted-toggle Morse matching gives 1203 pairs, one critical 0-cell, nine critical 5-cells, with all 2416 nonempty face-poset vertices exhausted by full topological sort; hence integral homotopy wedge 9S5. Independent adjacency-preserving permutation enumeration finds 48 automorphisms, including central shift i→i+6. Direct signed fixed-face Lefschetz sums (the reduced empty-face sign included) give degree-five rational character multiset {-3:6,-1:24,1:9,3:8,9:1}, invariant dimension zero and central trace -1, thus 4+5 central eigenspaces. Inspected exact verifier checks the S4×C2 splitting via a 24-element kernel acting faithfully on its four Sylow-3 subgroups, verifies all 48² products, and yields exactly five distinct S4×C2 irreducibles with multiplicity one as claimed. This does not establish an integral equivariant wedge splitting.

## originality

PASS

PASS (best of knowledge): Earlier Marietti–Testa dominance-complex theorem covers forests, not this cyclic cubic Franklin graph; the general complement-neighborhood Alexander duality of Matsushita–Wakatsuki is a change of representation, not the nine-sphere count or full group character. Published Franklin results for its dissociation, matching and total four-cut complexes are different complexes. Resultary returned this current dominance complex exactly, not a prior specific full character.

## value

PASS

PASS: A natural well-known 12-vertex cubic graph and its intrinsic 48-element automorphism group lead to a nontrivial complete integral sphere-wedge calculation and complete rational representation decomposition. The multiplicity-free five-constituent character and zero invariant line are independent mathematical structure, not a routine renamed Betti count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
