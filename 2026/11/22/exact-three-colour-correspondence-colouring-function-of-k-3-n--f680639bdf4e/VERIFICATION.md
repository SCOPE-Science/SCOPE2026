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

Completing each edge matching to a permutation only removes colorings, so minimizing over full covers is exact. Relabeling each right fibre normalizes its u_0 edge, and then the two other left fibres normalize any one chosen right vertex to type (id,id); the other types can be sorted. Fixed left representatives forbid exactly the three listed images, counted as a set, and right choices multiply. For an independent replay I did not normalize the first right vertex: I enumerated all weakly increasing n-multisets of the 36 types after normalizing the u_0 edges alone. For each type form bit masks U,V on the 27 left triples for which it allows one or two choices. Start with all bits in G_0; adjoining that type replaces G_k by (G_k AND U) OR (G_(k-1) AND V), with nonexistent G_j zero. Sum 2^k times popcount(G_k) to count a cover. The exact numbers of evaluated covers for n=1..6 were 36, 666, 8436, 82251, 658008, 4496388 (=binom(35+n,n)); minima were 24,18,14,6,5,0. This bypasses dependence on the frozen anchor normalization or on the implementations in verify.cpp and verify.py (both inspected). For all n>=6, the six types of cyclic shifts given in RESULT.md line 46 block every left triple: choose a first shift 0 or 1 to avoid the first chosen color, then the second shift to hit the third residue. Extra vertices cannot restore a blocked assignment. This establishes the exact result for all n>=1, not just the finite census, and makes no claim about counting cover isomorphism classes.

## originality

PASS

The complete table adds the exact n=3,4,5 positive minima to known or immediate cases. In particular the n=2 entry is already an exact corollary of Kaul–Mudrock–Sharma–Ullyot by exchanging the bipartition shores, n=1 is the standard tree count, and the zero tail is known. These entries are not credited as novel. The examined evidence does not cover 14, 6, and 5 as exact minima for n=3,4,5, respectively.

## value

PASS

The DP color function is a standard quantitative worst-cover invariant. The last three positive cases just before the independently known uncolourability threshold are a natural cutoff, not an arbitrary selection of graphs. In particular the exact 14-to-6-to-5 descent supplies sharp benchmarks where positivity alone leaves the number of available extensions undetermined. The value rests on those distinct minima, not on recomputing the tree, the two-vertex shore, or the zero tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
