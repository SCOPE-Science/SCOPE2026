# Scientific review

## Correctness

PASS. The proof establishes a complete trace invariant \((u,r)\), necessary and sufficient linear and cyclic gap constraints, exact weighted enumerators for projected words, and formal geometric-series summations. The cyclic boundary is explicitly treated, including empty words and single non-marker symbols. A direct intersection with \(a^*b^*\) proves both trace closures nonregular. The standalone program checks the formulas independently against finite brute-force original-word counts. No finite experiment is treated as an infinite proof.

## Originality

PASS relative to inspected evidence. De Colnet–Meel–Mathur (arXiv:2512.00314, first posted 2025-11-29) prove general complexity and approximation results for counting traces meeting regular languages; even their h=2 independence example uses a different accepted language, and its example counts no all-parameter proper-word traces. Maarand–Uustalu (CONCUR 2019) provide reordering-derivative tools and general examples of nonregular trace closures, without these specific exact linear and circular quotient enumerators. Published-index searches for proper words, adjacent-distinct constraints, star-shaped independence, trace quotients, and rational counting series found no explicit equivalent all-parameter result. Classical trace-monoid sources could contain implicit derivations; this remains a residual priority risk.

## Value

PASS. The example gives exact trace-counting benchmark sequences for a natural finite-state *local avoidance* constraint and a natural cyclic boundary variant, under a standard partial-commutation model from concurrency. The complete rational formulas quantify trace reduction where simply counting DFA words overcounts executions, while both trace closures are provably nonregular. The result is an infinite, all-alphabet structural classification, not a small numerical improvement or one-off lookup.

## Limits

The result does not imply new worst-case complexity bounds, a general trace-counting algorithm, regularity of the trace closures, or definitive novelty across every historical source.

Self-review: passed. Independent audit: not yet performed.
