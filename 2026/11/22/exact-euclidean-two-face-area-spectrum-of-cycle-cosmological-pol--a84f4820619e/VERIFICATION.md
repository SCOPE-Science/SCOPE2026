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

The face criterion in Kühne–Monin gives exactly the doubled-index q_i,r_i triangles and the distinct-index triangles, excluding the two coherent triples at n=3, plus one degree-two node face per node. Independently, with the exposing maximum shifted to zero and a_i=-ell(x_i), b_i=-ell(y_i), the slacks require a_i>=0 and |a_i-a_(i+1)|<=b_i<=a_i+a_(i+1). With both a's positive, a tight p uses the upper endpoint, a tight single q or r imposes a strict order on the a's, and a tight q,r pair imposes equality and b_i=0. For triples the only ordering cycles are the two coherent n=3 choices. If a_i=0, its node square is forced; its opposite corners have midpoint x_i and its diagonals are orthogonal of squared length 8. Disjoint indices yield squared side 6, incident indices 4 or 8 according to the shared sign, and q_i,r_i have squared side 8. For n>=4 a triple of edge indices has 0, 1 or 2 adjacencies with counts n(n-4)(n-5)/6, n(n-4), n; respective triangle choices split 27; 15/12; and 8/14/5. Doubled edges yield 6n triangles of label 28 and 3n(n-3) of label 32, with label 4 area^2. At n=3, all agreements allow zero or one negative node (4 choices), all disagreements are exactly the 2 excluded cycles, and the total number of disagreements over the 27 assignments is 36; hence exactly 12 assignments have one disagreement and 9 have two. This recovers the three stated classes after adding the 18 doubled triangles. The face-count denominator, concentration coefficient and summed-area leading term agree with these counts, including absent classes at n=4,5.

## originality

PASS

The combinatorial classification and f_2 were already known in the same object. The distinct claim is the evaluated metric area multiset for all cycle sizes, including the low-order changes and concentration. The strongest comparisons were made in the common embedding; the inspected sources supply the inputs but not the weighted geometric enumeration.

## value

PASS

A complete Euclidean face-measure histogram naturally refines the published two-face count in the canonical realization. Its particular values distinguish local adjacency patterns and the exceptional triangular cycle; it quantifies density and area of the dominant shell instead of simply enumerating faces. This is a useful exact benchmark for metric questions about graph-defined polytopes without treating a sum of planar areas as a surface area or intrinsic volume.

The dated certificate retains the supplied scientific assessment, sources and limitations.
