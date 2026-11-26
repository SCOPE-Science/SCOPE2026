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

For W=AcB the only candidate parents are AA and BB, as a one-position deletion leaves at least one entire outer block. If both parents are distinct, B is a deletion from Ac and A from cB. Let r be the first differing position. The former deletion can be placed at r, since any earlier deletion leaves equality up to r−1 only by shifting an initial equal-letter run within the deletion interval. It follows that B_t=A_{t+1} for t≥r with A_{m+1}=c. The latter deletion must remove B_j with j≥r or A_r would equal B_r. Thus A_1=c and A_t=B_{t−1} up to r. Equality before r forces A_1 through A_r all to be c, so the shift relation holds throughout; W=AAa_1 with a_1=c. The converse uses end deletions, and nonconstant A gives two distinct parents. Count incidence using q(2m+1) insertion histories per codeword minus 2m run redundancies; this yields all three histogram cells and excludes higher multiplicity. The graph components have sizes d dividing m, in numbers P_q(d) by primitive period Möbius inversion. An even cycle has two alternating maximum sets; for odd d there is exactly one gap with two unselected vertices, whose freely chosen position gives d maximum sets. Handle d=1 and d=2 as a singleton and an edge. This proves the sum/product, and smaller periods contribute O_q(q^{m/2}) words. Independently enumerated received words for q=2 through m=6, q=3 through m=4 and q=4 through m=3; all histograms, parent identities and edges agree. Replay: /workspace/review-check-4.py; frozen checker inspected, not executed.

## originality

PASS

The general one-insertion pairwise overlap bound is known, and a closely related repeated-block deletion result gives orbit-based expurgation in a different regime. The inspected statements do not give the exact inverse-list law, the rotation adjacency criterion in this doubled family, or its two optimal-code formulas.

## value

PASS

The doubled code is a natural memoryless-alphabet repetition construction. Exact parent rigidity reduces a synchronization ambiguity problem to rotation orbits, making the complete ambiguity law and best corrected rate computable and giving both the optimal size and multiplicity. This is more than a general insertion-ball size bound or an unexplained finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
