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

The cyclic spectrum, orientation convention and fixed weight are consistent. More precisely than the opening sentence of Step 1, the complement of a window containing all three ones lies inside the interior of one gap; a shortest such window uses the complement of the interior of a largest gap and has length n−max(g)+1. A three-one factor fixes two ordered step gaps and hence the third. Without such a factor, a fixed two-one pattern at step distance d<k occurs once for each gap d; its outside marker cannot appear in the window. For every fixed one position, the preceding and following marker exclusions are disjoint; the all-zero count sums max(g−k,0). Thus the spectrum depends only on the gap multiset and records the multiplicities of all gaps <k. At K=floor(2n/3) the bound H=n−K is strictly below K and 3H−n≤2, forcing a repeat in each triple-free gap multiset. At k0=K−1 the deficits from H=n−k0 sum to 3, 5 or 4 by residue; partitioning these totals into three distinct nonnegative parts gives exactly the stated gap lists, with the listed positivity condition. The short-gap counts recover the multiset at k0 for n=6 or n≥8 because H≤k0 (unseen gaps, if any, equal k0). At n=7, if two gaps are unseen they both equal 3 by their sum bound; if one is unseen its value is determined by the total, and three unseen gaps are impossible. This excludes cross-multiset boundary collisions everywhere. Prefixing each factor proves monotonicity in k. The n=3,4 domains are singletons and the n=5 gap multisets {1,1,3} and {1,2,2} have different 11 counts at k=2. Independently enumerated literal cyclic factor counters for n=6..80 agreed with the threshold boundary and every listed doubleton and reversal pairing. Replay: python3 /workspace/branches/8d9ee999-be9e-4c97-abdd-2e565058f112/independent_factor_deck_check.py --min-n 6 --max-n 80 --set-variant; output in the same directory as independent_factor_deck_check.out. This check is finite; no set-valued theorem is inferred. The frozen verify.py was inspected, not executed.

## originality

FAIL

The earlier 2026/10/26 indexed record covers the identical channel, gives the same worst-case threshold and gap lists, and proves the pointwise threshold, mirror collisions and truncated-gap recovery. The exact predecessor fibers follow from those statements, even without the separate notation B(n). A second distinct same-day record has the same threshold and pairwise-distinct gap reversal mechanism; no ordering is inferred between same-day records. The earlier overlap is decisive.

## value

FAIL

The sharp transition and exact surviving ambiguous necklaces would be useful for understanding this observation model. But the same threshold and extremal structures are already given by a more detailed result, and the fiber count follows immediately from its pointwise thresholds and truncation lemma. The frozen claim supplies no independent additional exact phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
