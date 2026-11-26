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

For paths of one or two edges let s=p/2, A=1−s, q=1−s². Complementing both indicators preserves covariance; the common failure marginal is Aq^(n−2). Each external vertex contributes a factor independent of the others and of endpoint edges: 1−2s² for reverse/chain (opposite arc demands), 1−2s²+s³ for a fork (one shared arc), q² for disjoint requests. Endpoint reverse failure requires no edge; a fork needs just its two direct failures. For the chain, conditioning on the two direct failures makes the two interior witnesses have probabilities s²/A each and overlap s³/A², giving endpoint factor A²−2As²+s³. For the disjoint case the two direct failures leave four candidate two-step paths; two witness pairs conflict, two have probability s³ and two have probability s⁴, and every triple contains a conflicting pair. Its endpoint factor is A²(1−4s²+2s³+2s⁴). The chain deficit relative to A²q² is s³[1−2s+s(1−s)²]>0; the disjoint conditional surplus relative to q⁴ is s³[2(1−2s)+s³(4−s²)]>0. Reverse strictness follows from 1−2s<A², and fork strictness already holds on three endpoints (q<1). These checks cover the minimum vertex counts and p=1; p=0 is degenerate and identical requests have positive variance for p>0. Independently counted all orientations/absences for n=2,3,4,5 using adjacency bit sets and integer counts by number of edges, and compared joint laws and signs at p=0,1/9,1/2,5/7,1: python /workspace/branches/twohop_replay.py (3, 27, 729, 59049 configurations respectively). This is corroboration, not the all-order argument. Theorem 2.1 of Alm–Janson–Linusson establishes the stated unrestricted asymptotic contrast, including fixed p=1.

## originality

PASS

The evidence distinguishes the exact annealed classification for reachability in at most two steps from both unrestricted small-subgraph correlation theorems and biased biclique count results. No examined distinct result supplies the finite all-order sign pattern or its polynomial joint laws. The positive unrestricted side of the contrast is explicitly prior work.

## value

PASS

The five symmetry classes form a natural complete classification, with exact probabilities as well as strict signs down to the smallest allowed order. The all-density negative chain law gives a specific threshold-horizon contrast with the known unrestricted result: short competing witnesses are insufficient for the positive high-density correlation. No priority or value is claimed for the unrestricted theorem itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
