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

For k=q−1, there are qk vertices of each nonzero-diagonal type A and B and k strictly upper-triangular nonzero vertices C. The product coordinates (ad,ae+bf,cf) give A_t→B_{−t}, B→A,C and C→A,C with its own loop deleted. Those arcs prove strong connectivity, also at q=2. Independent contrasts within A and B slope fibers are killed, and the contrast on C is acted on by −I. On fiber constants the B-slope contrasts map isomorphically, by k times slope reversal, to the A-slope contrasts, which are killed. Since the decomposition into contrasts and constants is direct over C, this gives q−1 length-two zero blocks and 2q(q−2) length-one zero blocks. The remaining uniform quotient has rows (0,k,0), (qk,0,k), (qk,0,k−1); its polynomial is the stated cubic, with P(0)=−qk² and P(−1)=1−q. To verify simplicity independently of the discriminant expansion, for q≥4 use P(−2)=q(k²−4)>0 and the signs at −∞, −1 and +∞ to separate three roots. For q=3, P(−2)=0 and P′(−2)=4, so there is a positive value just to the right of −2 and the two other roots are separated by −1. For q=2, z³−2z−2 and 3z²−2 have no common zero. The nonzero spectrum contributes q+1 to every power rank and the length-two zero chains contribute q−1 only to rank A. An independent replay by exact triple enumeration, polynomial and power-rank calculations for q=2,3,5 gave (rank A, rank A², rank A³)=(4,3,3),(6,4,4),(10,6,6). The supplied checker and saved q=2,3,4,5 output were inspected but not executed; q=4 output is recorded evidence only. The invariant decomposition, not any finite replay, proves the universal result.

## originality

PASS

The directed graph structure itself is established prior work. The supported distinct claim is the loopless adjacency's all-q complex Jordan decomposition, especially the length-two zero chains invisible to the cubic quotient. The closest accessible spectral comparisons are symmetric matrices for different graph conventions, and no inspected earlier theorem supplies the complete directed block counts or stabilized ranks.

## value

PASS

This gives a complete invariant of a standard directed ring graph, not just a quotient spectrum or a small-order table. Despite quadratic vertex count and strong connectivity, the adjacency has linear rank, a quantified nonsemisimple part, and stabilization of rank at its second power. Knowing only the polynomial would miss that behavior. The formulas resolve such questions uniformly, including nonprime finite fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
