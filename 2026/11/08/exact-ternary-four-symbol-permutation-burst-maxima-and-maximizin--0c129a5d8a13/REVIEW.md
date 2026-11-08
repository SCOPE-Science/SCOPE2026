# Scientific review: ternary four-symbol permutation-burst maxima

## Correctness

**PASS.** The exact output partition by unique first/last changed positions produces formula (1) of RESULT.md with no double counting. The endpoint-permutation formula uses ordinary multiset inclusion-exclusion. The alphabet-symmetric five-class transition table explicitly determines both the suffix-maxima and their tie counts. The displayed three-phase polynomial identities and the initial length-four values establish the claimed maximum and maximizing-center count for **all** integer lengths \(n\ge4\) by induction; no step extrapolates from a finite experiment. The reproducibility program performs an independent symbolic recurrence check using exact fractions and direct channel enumeration for all \(88{,}533\) words at lengths \(4\)–\(10\). The proof depends on the specified nonwrapping, exactly-four-position channel definition.

## Originality

**PASS against accessible evidence; residual priority risk remains.** The closest direct source is Chen–Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1 (2026-10-11). Its Section II gives a binary first-changed-position counting method; the manuscript explicitly restricts itself to binary symbols and does not state a ternary length-four all-length optimum or maximizing-center census. A general multiset-permutation sphere formula is not a substitute for this ternary constrained global optimization. A prior analysis of ternary **cyclic rotations** of four-position windows also has a smaller operation set (identity and three rotations), not arbitrary permutations, so its optimum cannot provide the present result. The related Kovačević–Kiah–Goyal study arXiv:2509.06692v3 (first public 2025-09-08) treats disjoint adjacent swaps, and hence a different channel. Relevant indexed literature and established formulas about binary four-window extrema, general per-word sphere volumes, and nonbinary short-window statistics were compared at the implication level. None supplies the displayed ternary maximum or its complete optimizer count. A differently named or unindexed prior statement could still exist; no claim of exhaustive priority certification is made.

## Value

**PASS.** The ternary alphabet is the first alphabet below the four-symbol window width where the pairwise-distinct-window maximization argument for larger alphabets is impossible, and it is genuinely different from the binary case. An exact worst-case output-sphere size is a natural local ambiguity invariant for permutation-burst channels, while the complete maximizing-center count measures the extremal structure, not merely its value. The period-three optimizer law holds at every length and is a substantive finite-state rigidity conclusion. The result provides sharp benchmarks for channel geometry, but no coding-rate or packing theorem is claimed.

## Closest literature and scientific limits

- Y.-P. Chen and O. Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1, https://arxiv.org/html/2610.15701v1 .
- M. Kovačević, H. M. Kiah, and K. Goyal, *Bounds on Codes Correcting Adjacent Transpositions*, arXiv:2509.06692v3, https://arxiv.org/html/2509.06692v3 .

Only one nonwrapping four-symbol permutation is considered, over exactly three symbols. The result is not a classification of optimizer words as a language, a code-size theorem, or an extension to other channel models. Remaining uncertainty is historical priority beyond indexed and inspected sources, not the finite certificate's arithmetic.

Self-review: passed. Independent audit: not yet performed.
