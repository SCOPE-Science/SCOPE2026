# Independent mathematical audit

## correctness

PASS

Re-audited /workspace/repairs/5/. The original maximality argument for a proper bridge asserted incompatible phases after extension, but p-apart starts can share a phase; it is the insufficient length of any putative mixed border that prevents closedness. The repair proves both extensions stay in same-letter runs. Every unary border of either extension has length at most t, occurs twice or more in its enlarged end-run and at least once at the other end. A mixed witness must have starts exactly p apart, by its unique phase and the intervening-copy argument, so its length would be 2t+1−ℓ≤t and it would be unary when this length is positive. For t=ℓ one can add a following 1 to a zero bridge or a preceding 0 to a one bridge, yielding a complete return to a mixed border at shift p. Mixed-border witnesses at shift p extend wherever available, leaving only the full word; unary maximal factors are exactly the full runs. The three disjoint families therefore give (k−1)p+3. For a cut inside a run of length ℓ at offset u, incoming and outgoing same-symbol bridge contributions are bounded by ℓ−1−u and u−1, leaving room for that run's unique crossing occurrence. At a run boundary no run crosses and at most one pair per symbol can contribute. The whole interval contributes one at every cut, and both symbols' full bridge families cross each c=mp, attaining p−1. This includes unit runs (no same-symbol bridges) and finite word endpoints; the all-k result is symbolic. Independent corroboration: python /workspace/branches/mcs_independent.py (216 instances with 1≤a,b≤6 and 2≤k≤7). It computes the longest proper border by the prefix function and checks for an earlier overlapping repeat before the suffix. This suffices: any shorter border has an extra occurrence ending at the end of a longer proper prefix border. Frozen scripts and logs were inspected, not run.

## originality

PASS

PASS for the narrowed contribution: the exact uniform internal-cut maximum p−1 on equal-block powers with k≥3, including equality at each block junction. The unary bridge representation is directly covered by the broader RLE Lemma 4 after substituting equal heights, and the remaining families and total count are a short periodic specialization, not a separate novelty claim. The repair expressly credits this coverage and uses the list to prove the distinct local cut statistic.

## value

PASS

Uniform equal-block powers are a natural compressed input model for internal reporting. The sharp worst local output depends on the period alone, independent of k, while the total grows linearly in k; this contrast and the equality locations give a distinct structural benchmark not supplied by the generic n-dependent bound. The local bridge/run tradeoff, rather than merely re-running an enumerator or counting known families globally, is the point of the repaired contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
