# Scientific review: occurrence-weighted palindromic subsequences

## Correctness — PASS

The embedding-count lemma is a bijection between index tuples and weak compositions of residual period increments. For a pattern \(v\), every weak descent requires moving to a new copy of the permutation period; all other period changes are arbitrary nonnegative increments. The palindrome weak-descent statistic is proved separately for odd and even lengths. Counting equality patterns of the half-word and summing the resulting binomial multiplicities yields the exact coefficient formulas; formal series summation yields the rational generating function. The extremal bound follows from the minimum possible weak-descents, and the equality case has one embedding. The actual standalone checker passed 36 complete finite occurrence profiles, 314 length comparisons, and 2,992 rational-series coefficient identities.

## Originality — PASS (best-knowledge, non-certifying)

The closest comparable invariant is distinct scattered-palindrome counting in Mahalingam–Pandoh (2021). Its \(SP_\ell\) counts a word once whenever any embedding exists, whereas the current claim sums all position tuples. The older arbitrary-prefix support theorem for permutation cycles also determines only the nonzero support of the embedding counts, not their actual values. Torres-Jimenez et al. (2017) provide a generic occurrence-counting algorithm, which is computationally capable of calculating any fixed coefficient, but do not claim the explicit bivariate rational formula and extremal multiplicity classification for permutation powers. Müllner–Ryzhikov (2019) study bounds for longest palindromic subsequences, not lengthwise embedding counts. published-finding corpus searches on palindromic embeddings, periodic permutation words, weak-descent closed formulas and aliases found no explicit equivalent. General-purpose algorithms are not treated as novelty of the computation itself. Residual risk: an unindexed paper could contain the same generating-function specialization.

## Mathematical value — PASS

The object is the exact occurrence-weighted refinement of a standard scattered-palindrome statistic: the number of index selections, which matters in subsequence frequencies, weighted sampling, and multiplicity-sensitive counting. The result simultaneously handles all alphabet sizes \(q\ge3\), all positive repetition counts and all palindrome lengths, and collapses an exponentially large positional search to an explicit binomial spectrum and rational bivariate generating function. The distinction from presence-only counts is substantive even for a small example: \((012)^2\) has six one-letter embeddings but only three different one-letter strings. The theorem also sharply identifies the only lengths attaining the maximum and proves unique occurrence of every longest palindrome. It is an exact, structural infinite-parameter classification, not a routine numerical table.

## Closest evidence and limitations

The full 19-page Mahalingam–Pandoh arXiv:2108.02729v1 and full 8-page NIST manuscript of Torres-Jimenez et al. were inspected. The shorter full Müllner–Ryzhikov arXiv:1901.07502v1 was also inspected. Lack of a bibliographic match is not proof of priority. The proof applies only to permutation periods, not arbitrary repeated run patterns. The finite checker does not establish the infinite theorem by itself.

Self-review: passed. Independent audit: not yet performed.
