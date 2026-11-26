---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An adjacent unequal swap changes just the order of its two symbols, reversing inversion parity. Swapping the first unequal fixed position-pair is an edge involution on the complement of the paired-letter residue, separately in every composition. Every residual word is even: distinct doubled blocks contribute 0 or 4 inversions and the final singleton contributes an even number. Any independent set takes at most one endpoint per involution edge, plus the unmatched vertices; the even parity class attains that bound. Counting residual words gives U_p as stated, with no odd multiplicity for even length or one for odd length, and q^ceil(n/2) across all words. The argument allows unused symbols and n=1 and concerns detection only. The supplied code and VERIFICATION.md were inspected, not executed; independent counts confirm 22 parameter cases, 6689 vertices, and 309 composition profiles. No finite check is needed for the general proof.

## originality

FAIL

The central matching is a specialization of an already published adjacent-pair involution for linear extensions. In Stanley, Promotion and Evacuation, arXiv:0806.4717v2, proof of Theorem 3.1, p. 13, w′ swaps the rightmost pair (p−2i−1,p−2i) permitting that adjacent transposition to remain a linear extension, and w″=w. Represent multiset words by the linear extensions of a disjoint union of chains of lengths p_j: lift each occurrence of a symbol to the next element of its chain. A swap stays a linear extension exactly when the letters differ. Conjugating the published right-to-left involution by reversal of the multiset words gives exactly the frozen matching, including the placement of the odd-length singleton. Its unmatched words and their parity give the full sharp upper and lower bounds by the elementary matching argument. This is actual coverage by a more general prior construction, not just knowledge of the sign imbalance or the binary theorem.

## value

FAIL

The size of a one-swap detecting code is a natural exact invariant. Here, however, the optimum and its explicit parity construction are immediate once the published domino involution is applied to disjoint symbol chains. The remaining counts are a multinomial and a free choice per position-pair; no new invariant beyond this already covered consequence is established. The presentation is useful exposition, not independent mathematical value under the exact-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
