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

All four integral homotopy types are correct. I inspected the frozen proof, verification notes, verifier and expected transcript, without executing the submitted code. A separately written exact check (`python3 -B /workspace/branches/review3_check.py`) used cycle-order edges followed by antipodals, forbidden-star bit masks, and Kahn traversal of the oriented covers. The ordinary critical cells after unmatching the empty-face pair are {0:1,3:1}, {0:1,5:2,6:1}, {0:1,6:1,7:2}, and {0:1,8:3}; the two nonzero signed gradient matrices in this ordering are [-1,-1] and [2,-1]^T. The bases differ from the frozen verifier, but the primitive rank-one maps give the claimed cancellations over Z. In both two-degree cases the d-skeleton is a wedge of d-spheres and the attaching maps are classified by degrees (Hurewicz for d>=2). Unimodular changes are realized by equivalences of these wedges; the cofiber of a unit attachment cancels the corresponding wedge summand, so the calculation proves homotopy, not just homology. The separate duality argument below confirms all four cases.

## originality

FAIL

The exact four integral homotopy types are mechanically implied by the earlier Möbius-ladder independence-complex theorem, not merely similar results for different complexes. Here is the reduction. For a simple cubic graph G, let X=M_2(G) on E. Its minimal nonfaces are the stars at graph vertices. Its combinatorial Alexander dual on E is the union of simplices on E minus star(v). Each nonempty intersection is a simplex; a set J of star indices belongs to the nerve iff some graph edge has both endpoints outside J. Thus the nerve is exactly the combinatorial Alexander dual of Ind(G) on V. The nerve theorem and two applications of integral combinatorial Alexander duality give reduced H_i(X) isomorphic to reduced H_(i+|V|-|E|)(Ind(G)), with no field or Euler-characteristic reduction. Also X has complete one-skeleton, and each missing triangle (a star) bounds the cone on its loop using any outside edge: two different edges of the star have exactly one common vertex, so no cone triangle is a forbidden star. Consequently X is simply connected, since all triangle loops in the complete graph bound. When homology is free and concentrated in one positive degree d>=2, successive Hurewicz applications realize its basis by d-spheres, and the homology Whitehead theorem gives the wedge equivalence. Agarwal–Basak Main Theorem 1(a) gives S^0, S^1, S^2, and a wedge of three S^2 for n=3,4,5,6. In the cubic ladders |E|-|V|=n; shifting by n therefore proves exactly the frozen types. The same-day Wagner record moreover states the M_8 outcome verbatim with added equivariant information, although its order relative to this record is not established. This is a finding of prior implication, not a finding that the computations are wrong or that all four literal statements occur in the earlier paper.

## value

FAIL

The homotopy comparison is a natural invariant and the computations reproduce, but the first-four slice supplies no extra phenomenon beyond the all-size prior independence pattern transferred by elementary duality. The finite computation, including different Morse certificates, gives no additional claimed invariant. The same-size cube contrast is already documented on the cubical side and is not sufficient to rescue the mechanically implied four-case claim. No supported distinct remainder is identified for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
