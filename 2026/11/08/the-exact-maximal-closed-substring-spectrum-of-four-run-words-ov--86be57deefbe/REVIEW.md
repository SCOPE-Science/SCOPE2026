# Self-review

## Correctness — PASS

The proof specifies a closed occurrence by its proper border and counts maximality by one-character extensions. Exhaustion of all possible repeated border configurations in four maximal runs yields four whole-run occurrences, the unique repeated-run bridge families and, only for alternating run labels, one nonunary bridge. The two exceptional indicators record exactly those unary bridges subsumed by a closed extension. Independence of run-length-pair summations then yields the stated rational generating function for arbitrary alphabet size and word length. The embedded standard-Python enumerator checks 17,484 direct interval classifications and every generating-function coefficient for alphabet sizes 2–5 through length 14. Finite checking is additional evidence rather than an all-length proof. Remaining risk is a hidden border case not captured by the four-run exhaustive structural argument.

## Originality — PASS with explicit residual risk

Compared with the primary full text of Umezaki et al., arXiv:2607.02838v1, and Fischer–Köppl, arXiv:2610.38114v1, the already-known valid-pair and output-sensitive algorithms generate maximal closed occurrences for any given run-length-encoded input. That general coverage is acknowledged. The new claim is the exact **global coefficient distribution over every word with four runs**, uniformly in alphabet size, with its rational generating function and explicit alternating boundary terms; no equivalent all-parameter enumeration was located in those sources or targeted indexed mathematical searches. A generic algorithm can compute individual instances but does not by itself state these all-input coefficients. Residual risk: the explicit formula might be derivable or present as an unindexed specialization of prior enumerative work. An older indexed result on closed-rich maxima is for all closed factors, a different statistic; an indexed result on binary de Bruijn MCS counts concerns particular long words, not the four-run distribution.

## Value — PASS

The number of MCS occurrences is precisely the output size governing output-sensitive algorithms. Four-run words are the first bounded-run family accommodating two separate repeated transition types and a genuinely nonunary maximal border. The result identifies the entire finite-length output-size histogram for every alphabet, including sharp finite-size changes at run-length equalities and linear output even for fixed run-count. This is a natural complete classification rather than an arbitrarily selected small example; it does not claim a new algorithm or general asymptotic bound.

## Limits and closest sources

Primary literature: Umezaki et al. (2026), arXiv:2607.02838v1, and Fischer–Köppl (2026), arXiv:2610.38114v1; related framework: Kosolobov (2024), arXiv:2410.00209v1. The current work counts occurrences, not distinct contents or all closed factors, and covers exactly four runs. An independently conducted mathematical audit and definitive publication-priority confirmation have not occurred.

Self-review: passed. Independent audit: not yet performed.
