# Scientific review

## Correctness (C): PASS
The theorem specifies all binary words, every positive alternating-pattern length, positional subsequences modulo two, a complete prefix-output Moore model and explicit transitions. Generalized-binomial reflection identities reconstruct the full counter update; periodicity follows from characteristic-two truncation. The repeated `01` suffix gives reachability and the Lucas-mask least-period argument gives the matching state lower bound, not merely a reachable upper bound. The two supplied programs check a separate literal-count oracle (98,292 comparisons) and complete prefix-vector orbit plus Moore partition refinement for lengths 1–90. The mathematical argument is all-length; these finite tests do not constitute that proof.

## Originality (O): PASS with documented priority limits
Richomme (arXiv:2510.07159) treats integer two-binomial classes; Fazekas–Huang–Mercaş (arXiv:2610.06717) treat fixed Parikh-matrix class universality and subsequence probabilities; Golafshan–Rigo–Whiteland (arXiv:2412.18425) treat factor complexity of generalized Thue–Morse words; and Černý (2010) gives a general representation framework. The directly closest published exact modular Moore-state result for `010` already covers the case of pattern length three and modulus two (four states); that special case is not asserted to be new. The prior result does not establish a general growth law or two-reflection machine for all lengths. A two-run binary pattern theorem likewise does not imply the alternating patterns with several changes. Semantic and textual comparisons are detailed in AUDIT.json. A plausible 2011 trie-automaton source could not be compared in full; an unindexed equivalent remains an explicit historical-priority risk.

## Value (V): PASS
Instead of a generic exponentially large vector of prefix counts, the result determines exact minimal memory across all pattern lengths and explains it by a cyclic action of two reflections. The exact power-of-two staircase and suffix-based minimality furnish structural information beyond the already-known length-three case. This all-length classification is a natural streaming formal-language invariant, not a narrow numerical specimen.

## Limits
Modulus two only; exact alternation only; no claim for arbitrary target patterns. Published and accessible literature was compared to the extent reported; historical priority and mathematical validity have not been independently audited. The external source not read in full is a residual originality risk, not a claimed noncoverage proof.

Self-review: passed. Independent audit: not yet performed.
