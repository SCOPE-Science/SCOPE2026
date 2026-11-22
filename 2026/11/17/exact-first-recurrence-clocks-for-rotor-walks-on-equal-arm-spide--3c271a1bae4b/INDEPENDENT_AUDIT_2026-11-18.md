# Independent mathematical audit

## correctness

PASS

At a given arm, a first excursion meets the shallowest initially outward-pointing uncleared internal rotor at depth d, rotates it to parent and returns in exactly 2d moves; all shallower cleared pointers restore inward on return. With no blocker, excursion reaches the leaf and returns in 2L moves. For B=max_i b_i, the final blocker is in the last arm in the hub's cyclic scan with exactly B blockers; every prior arm completes B excursions, every later arm B−1, and the terminal arm contributes two times earlier blocker depths plus one last outward traversal. The first state with the walker on the unique rotor two-cycle, hence the first periodic state, occurs upon arrival at this last blocker, not after completing an entire Euler tour. This produces the stated exact τ sum. Bounding complete excursions by 2L and selecting B deepest terminal depths gives H(B)=2(k−1)BL+(B−1)(2L−B−2)+L−1; its strict successive increase proves max τ=(L−1)((2k−1)L−1) and exactly one maximizing rotor mask per hub pointer (k total). A recurrent tree rotor unicycle traverses each oriented edge once (primitive period 2kL). For iid fair pointers fixed L, the last all-blocker arm lies a tight geometric number of positions before the end; LLN for independent bounded E_i(L−1) with mean 3L(L−1)/4 gives τ/k→3L(L−1)/2 in probability and mean. Independent brute finite-state simulation reconstructed all 24,344 initial configurations across seven (k,L) pairs and verified exact entry time, primitive period, maximum and number of extremizers; the universal statements rely on excursion proof and LLN, not this enumeration.

## originality

PASS

General rotor-router literature gives Eulerian stabilization and nested exploration phases on arbitrary finite graphs; its broad O(mD) bounds neither state nor directly imply the exact blocker-depth spider first-recurrent-state formula or sharp labelled extremizers and typical limit. The closest published corpus includes related path/comb/cycle and bouquet first-entry clocks with different topology/starting conditions. Prior 'lock-in' sometimes denotes first completed Euler tour rather than first periodic state, so a title-level match is not coverage. No exact covering original theorem was found. Accessible author manuscript text for Bampas was limited, and unindexed rotor-router notes are a genuine residual priority risk.

## value

PASS

Exact first recurrence is a natural dynamical clock distinct from Euler tour completion. The complete configuration-level formula, sharp quadratic longest delay, exceptionally small maximizing set and fixed-length high-arm probability limit classify stabilization for a genuine infinite graph family and random initializations. This is more substantive than a tiny instance or an asymptotic bound and plausibly useful when comparing rotor-router exploration/lock-in definitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
