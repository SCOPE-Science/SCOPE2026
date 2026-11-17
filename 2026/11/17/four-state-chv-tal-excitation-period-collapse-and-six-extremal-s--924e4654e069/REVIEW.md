# Review of: Four-state Chvátal excitation: period collapse and six extremal symmetry classes

## Correctness — PASS

Both supplied complete-state C++ implementations enumerate exactly \(4^{12}=16{,}777{,}216\) labelled \(q=4\) GHM states on the stated Chvátal adjacency. The indegree-peeling functional-graph proof and independent path-memoization algorithm give identical 21 (entry,period) classes and periods only 1 and 4, sharp entry 12 attained by 48 states. A third exhaustive local-coloring checker counts exactly 118408 successor-supported four-colorings; a rigorous connected-graph lemma equates these with nonzero period-four states. An independent exhaustive automorphism backtracking script proves 8 graph automorphisms and six size-8 orbits on the 48 maximal states. Finite enumeration proves only this fixed finite-graph claim; no asymptotic extrapolation is involved.

The graph and update are fully specified, with \(4^{12}\) finite states. The `census.cpp` and `independent.cpp` outputs agree on every joint count; `phase_coloring.cpp` verifies 118408 direct rotating configurations. `symmetry_check.py` checks the full graph automorphism group and all six extremal classes. Critical proof steps, finite bounds and reproducibility commands appear in `RESULT.md`. No untested infinite claim is asserted.

## Originality — PASS (best available evidence)

Comparison with published mathematical records and accessible prior results found the same-graph prior census only for three colors, with a distinct six-period spectrum, and four-state results on nonisomorphic graph families. Gravner–Lyu–Sivakoff and Doba treat finite-graph three-valued excitation; Durrett–Griffeath provide general multistate lattice context. The \(q=3\) results do not imply \(q=4\) periods, entrance cutoff, or extremal symmetry. Full \(q=4\) Chvátal priority remains subject to possible unindexed literature.

Most relevant inspected materials: the complete available same-graph three-state RESULT.md; Gravner–Lyu–Sivakoff, arXiv:1610.07320v1, including Theorem 3 and §6.1; Doba (2018), §§2–7; the lawful opening of Durrett–Griffeath's 1993 model study. Related four-state complete tripartite results do not include a four-chromatic Chvátal graph. Source-specific implication comparisons and risks are recorded in `AUDIT.json`. Failure to find an equivalent paper is not a proof of absolute priority.

## Mathematical value — PASS

Chvátal is the smallest triangle-free 4-regular 4-chromatic graph, making four-state excitation a natural test case near a graph/color threshold. Increasing refractory length from three to four states deletes all prior \(q=3\) period-11 and other non-4 oscillations, yet raises the sharp first-entry time from 10 to 12; this nonmonotone spectral-versus-transient response is supported by the exact recurrent-state and basin census. Six distinct maximal symmetry classes and a structural local coloring criterion give reusable finite combinatorial data and test cases rather than arbitrary isolated numbers.

## Scope and limitations

The result concerns one labelled twelve-vertex graph and one fixed deterministic update rule. Computer-assisted exhaustiveness and independent C++ algorithmic agreement do not constitute independent expert certification. The comparison with the three-state result describes a mathematical contrast, not a theorem of monotone dependence on color count. The accessible research record may not exhaust all historical sources.

Self-review: passed. Independent audit: not yet performed.
