# Scientific review

## Correctness
PASS. Complete exhaustive coverage of all \(\sum_{e=0}^{8}\binom{32}{e}\) transition masks establishes the sharp absence below eight. Both independent C++17 implementations replayed and obtained \(5{,}808\) full-reach eight-edge relations and \(56{,}544\) full-minimal relation/final-set pairs. Partition refinement and independent pairwise distinguishability agree, including the distribution over all final masks. The eight-edge witness is explicit. This finite certificate does not establish any all-state-size theorem.

## Originality
PASS relative to material inspected. The exact four-state eight-edge census is not stated or implied by the general parameterized bounds of Baburin–Cotterell (2026), the foundational subset-construction theory, or their 2025 analysis. A prior three-state enumeration does not reach this four-state transition-budget threshold. Exact table matches remain possible in unindexed work, and no independence or priority guarantee is claimed.

## Value
PASS. The fewest labeled transition edges needed for maximal deterministic blowup is a natural resource invariant; the four-state cutoff is a complete meaningful next finite boundary, not an arbitrary selection of partial examples. The result distinguishes reachable powerset blowup from language-minimal blowup and gives a full extremal census as a benchmark for sparsity-sensitive determinization bounds.

## Limitations
Fixed states, binary alphabet, fixed start state, and at most eight edges; counting is with labels. Finite computation is exhaustive, but is not a general theorem in state count.

Self-review: passed. Independent audit: not yet performed.
