---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The minimum edge dominating sets of size k in K_(2k+1) are exactly near-perfect matchings: k disjoint edges leave one uncovered vertex. A legal replacement attaches its free vertex to an old matched endpoint. In M symmetric-difference N there is a unique alternating path plus disjoint alternating cycles. Path moves each take one flip per old edge, and each nontrivial r-atom cycle requires r+1 (lower potential k-|P cap N|+cycle_count changes by at most one). Atom cycles on r>=2 labeled reference pairs have 2^(r-1)(r-1)! orientations/orderings and one path has 2^r r!, yielding the displayed labeled EGF, correct F0=1 and all k. For k even maximum distance k+k/2 requires only 2-atom cycles, giving (2h)!/h!. For k odd two extremal structures (h pairs of cycles and one-atom path, or one 3-atom cycle and h-1 pairs) give (2h+1)!(4h+6)/(3h!). The n=3/k=1 boundary is 2 antipodes. Independent graph construction/BFS produced k=1..4 profiles (1,2), (1,4,8,2), (1,6,24,54,20), (1,8,48,204,464,208,12); code is supplementary, not all-k proof.

## originality

PASS

The distance metric t+c and flip connectivity are already accessible through matchings geometry. The final claimed novelty is the full sphere distribution and antipodal counts, whose cycle/path marked exponential formula is not supplied by inspected flip-distance or Hamiltonicity results. Searches returned same current Resultary record and other graph families (e.g. sliding near-perfect bipartite matchings), not an implication-dominating enumeration. This is a bounded best-of-knowledge judgment, not an absolute novelty certificate.

## value

PASS

Distance spheres and farthest-state multiplicities are canonical reconfiguration invariants, genuinely new information beyond connectivity, diameter, and a distance formula. An exact EGF uniformly determines random-pair distances in an infinite natural family and supplies exact sampling/transport benchmarks. The object and exact invariant are intrinsically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
