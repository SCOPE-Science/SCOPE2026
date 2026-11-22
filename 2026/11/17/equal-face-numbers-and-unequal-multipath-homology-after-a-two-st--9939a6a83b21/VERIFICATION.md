---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For a=0,1 on n=7, orient all tournament edges increasingly except a+2->a. Every directed cycle must include the reversed arc followed by an increasing a-to-(a+2) path, forcing the unique a,a+1,a+2 triangle. An arc subset forms a directed linear forest iff each tail and head appears at most once and the triangle is not all selected. I independently enumerated faces via direct combinations of the 21 arcs, sorted into simplicial levels, and calculated exact augmented GF2 boundary ranks with bitset Gaussian elimination. For a=0 and a=1 both full face vectors are (1,21,142,370,351,93,3); boundary ranks are respectively (1,20,122,242,90,3) and (1,20,122,248,90,3), yielding reduced betti a=0 beta2=6,beta3=19 and a=1 beta3=13 alone. For every n=3..6 and every admissible two-step reversal, independently enumerated exact same face vector and reduced bettis within that order: n3 (1,3,3), beta1=1; n4 (1,6,9,3), beta1=1; n5 (1,10,27,21,3), acyclic; n6 (1,15,67,102,45,3), beta2=7. This exhausts the specified finite family, not all digraphs, and the mod-two discrepancy proves non-homotopy equivalence.

## originality

PASS

PASS best-of-knowledge. The structural directed-forest/conflict-hypergraph characterization is prior work and not new. The earlier transitive-tournament and extremal-edge-reversal computations provide Euler characteristic or wedge results for different arcs; a previously published Wagner-vs-cube fully bidirected equal-face-vector example illustrates similar philosophy, but cannot imply the two specific one-edge-reversed tournaments and their distinct mod-two boundary ranks. This is a new exact natural seven-vertex witness within a motivated proximity-to-transitive family, not a general all-digraph minimality claim.

## value

PASS

This small but natural counterexample proves that the entire f-vector and the number of directed triangles fail to determine multipath homology even among almost-transitive tournaments, and identifies the first size within the precise two-step-reversal family where reversal location matters. The exact rank separation β2=6/0 and β3=19/13 is a substantive invariant, not merely a negative type/normalization test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
