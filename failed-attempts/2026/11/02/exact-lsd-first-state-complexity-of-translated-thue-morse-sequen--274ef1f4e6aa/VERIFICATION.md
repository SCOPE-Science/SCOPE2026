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

The carry/parity pair after a prefix of length L with value p is (floor((c+p)/2^L), t((c+p) mod 2^L)), so a continuation of value x sees precisely the claimed shifted/complemented residual. If distinct positive translations gave equal or complementary tails, Thue–Morse would have an eventual period; repeatedly halving an even period and applying the recursions to an odd period makes the tail constant, which is impossible. The reachability intervals at quotient q and overflow q+1 have exactly the stated parity counts. For c>=4 there are six low-quotient states including the exceptional split recovery of the quotient-two states at c=5. All high quotients from distinct positive lengths are disjoint since q_j >= 2q_{j+1} > q_{j+1}+1 whenever both layers can contribute high quotients. The initial state is distinct. The four small shifts give 2,3,5,6. Equality in the block bounds for k>=3 is forced at the top digit layer for the minimum, and at every layer from j=2 onward for the maximum. The latter conditions are equivalent to upper-half membership and c=2 mod 4; there are 2^(k-3) such shifts. The binary 2-kernel is exactly the collection of prefix residuals. Independent finite replay (`python3 /workspace/audit-evidence/replay.py 1`) obtained the expected residual signature counts for shifts 0–127 and the stated extremizer sets in blocks k=3–6; this corroborates the proof, not a substitute for it.

## originality

FAIL

Distinct Resultary record 11fc25e0cd30 gives the exact same function for every shift under the same empty-word and trailing-zero conventions, and the same dyadic bounds. Although that Finding gives only examples of extremizers, both complete equality loci follow directly from its explicit per-residue contributions; the claimed exact kernel cardinalities are the same invariant. This establishes coverage, not discovery priority or dependence.

## value

FAIL

Exact shift complexity is a natural automata invariant, but the original record repeats the complete exact count and dyadic bounds, including the residual approach. Its extra extremizer and kernel wording consists of routine residue maximization and the defining residual correspondence. The frozen claim supplies no independently valuable remainder beyond the already indexed count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
