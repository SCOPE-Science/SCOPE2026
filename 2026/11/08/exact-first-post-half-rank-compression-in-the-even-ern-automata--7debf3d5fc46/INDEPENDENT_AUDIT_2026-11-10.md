# Independent mathematical audit

## correctness

PASS

For Černý C_{2m} with r:i→i+1 and d:0→1, each rank drop requires an effective d and at least two r between consecutive effective drops, giving baseline s+2(s−1)=3m+1 at s=m+1. If a word had ≤3m+2 letters, after trimming redundant ends either all d are effective with total n or n+1 rotations (cumulative hole differences wrap to 0 or 1 modulo n and forbid effectiveness), or exactly one d is ineffective and only n rotations (forced two-r gaps; the ineffective letter is deletable or prevents following effective d). Thus additional two letters necessary. Explicit d r³ d (r²d)^{m−2} r³d has all m+1 effective steps; cumulative shifts 0,3,5,...,n−1,n+2 avoid forbidden differences 0,1 mod n. Independent BFS on image subsets confirms λ_{2m}(m+1)=12,15,18,21,24,27,30 for n=6,8,...,18. The finite checks corroborate proof, not unbounded n. No s>m+1 claim.

## originality

PASS

Earlier published exact Černý deficiency profile proves 3s−2 only for s≤ceil(n/2), and explicitly leaves the first post-half value unclassified. The submitted 3m+3 threshold is not the forbidden linear extrapolation 3m+1 and supplies a nontrivial wraparound obstruction; targeted published comparisons did not establish prior coverage. PASS with priority risk for older subset automata literature.

## value

PASS

The first failure of a sharp linear compression law in a canonical synchronizing automaton is an intrinsic, motivated structural cutoff. A two-letter gap caused by cyclic holes is a meaningful rank transition rather than an arbitrary numerical slice, even without classifying deeper ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
