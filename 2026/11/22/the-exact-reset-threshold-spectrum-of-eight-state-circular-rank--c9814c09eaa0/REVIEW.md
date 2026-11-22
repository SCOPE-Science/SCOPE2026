# Scientific review

## Correctness — PASS

The result is a finite complete census with a rigorous exhaustive search invariant: every reachable nonempty image subset is represented by a mask, and breadth-first search returns a minimal reset word length or proves none exists. Two independently coded enumerations and image-transition routines agree on all 31 spectrum coefficients. The count of input maps is proved analytically as \(\binom86 6!S(8,6)=5{,}362{,}560\), and Burnside's lemma independently checks the orbit count via the exactly \(2{,}304\) half-turn-invariant maps. Independent Python state-search reconstructs the unique orbit's 36-step witness. The full scripts are embedded; they terminate and produce the stated results. This does not prove an infinite-family statement.

## Originality — PASS, with historical uncertainty

The closest direct published finding is the all-rank-seven circular eight-state table. It is a different input family and does not imply any coefficient or the new 36-step maximum. Earlier experiments with all small automata addressed general Černý bounds and selected critical counts, not this rank-six conditional spectrum. Full text was inspected where available, and searched equivalences include defect-two, rank-six cyclic, and one-cycle-plus-map descriptions. No exact covering source was located. An independently produced but unindexed historical rank-six census remains a specific risk; database absence is not a uniqueness proof.

## Value — PASS

The rank of the nonpermutation letter is a natural compression parameter in synchronizing automata. Complete classification of the first defect-two step adjacent to the published eight-state defect-one census is an exact, motivated benchmark. It establishes the sharp maximum 36, uniqueness of its rotational class, a 32–34 threshold gap, the complete distribution of achievable reset lengths, and the precise half-turn failure obstruction, useful for benchmarking exact reset algorithms and comparisons along the rank hierarchy. This is more than a random narrow slice or routine instance of a general existing formula.

## Known limitations and literature

The classification is for a specified binary eight-state class only. No historical priority beyond inspected sources is guaranteed. Closest material: https://arxiv.org/abs/2207.05495 (full HTML manuscript), https://arxiv.org/abs/1607.04025 and https://arxiv.org/abs/1609.06853 (full PDF sections), and the published rank-seven result at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-reset-threshold-spectrum-for-eight-state-circular-defec--d2476f0a726f.

Self-review: passed. Independent audit: not yet performed.
