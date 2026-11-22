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

PASS. The Bruhat subword property for either bipartite Coxeter word (each simple reflection appears once) gives 2^{n-1} distinct permutation vertices; all are exposed as vertices of the full permutohedron and remain exposed in this subpolytope. Splitting the word into two commuting parity batches, the pre-second-swap coordinate pairs have entries (t−a,t+1+b). Exhausting the binary indicators shows inner-pair squared distance ≤18, attaining 18 exactly when both adjacent first-layer moves occur in both vertices and the final parity swap indicators disagree; if a corresponding first-layer move differs between vertices the block falls to ≤13. At boundary blocks only one adjacent first-layer move exists, yielding a sharp ≤8 and ≤5 under discrepancy. These local losses outweigh any singleton endpoint gain of ≤1, even at n=3 and n=4. Summing blocks gives odd 9n−19 for both orientations; for even n, odd-first gives 9n−18, even-first gives 9n−20. Equality simultaneously in all blocks forces first parity batch full in each vertex and complementary second parity choices; unordered extremizers count 2^{#second−1}. Euclidean squared norm is strictly convex in each variable, so no nonvertex pair maximizes. Independently enumerated every subword pair for n=3..10 in both orientations, including the exact predicted diametral pairs and Euclidean norms, and checked local indicator inequalities. Source verifier's large n sampling is supplementary, not proof of all n.

## originality

PASS

Best-of-knowledge PASS for the complete extrinsic Euclidean diameter and all extremizers in two alternating Coxeter orientations, especially the two-unit even-n inverse-element gap. Tsukerman–Williams's Bruhat interval polytope diameter is the diameter of the 1-skeleton graph (maximal Bruhat chain/shortest graph paths), not Euclidean coordinate distance. Gaetz's one-skeleton poset structure also addresses combinatorial edges. These established statements neither fix the orientation-dependent Euclidean outer shell nor the complete diameter matching. Euclidean diameter is embedding/convention dependent, a meaningful reason the graph result cannot imply it.

## value

PASS

PASS. For polytopes with the same Boolean vertex count and identical combinatorial graph diameter, a sharp Euclidean two-unit squared-diameter separation between inverse Coxeter orientations and a complete exponentially sized extremal-pair matching is a natural metric/combinatorial distinction. It cannot be recovered by substituting a parameter into the previously known 1-skeleton diameter theorem. The all-order equality conditions carry structural information beyond a small n table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
