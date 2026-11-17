# Independent mathematical audit

## correctness

PASS

Reconstructed sharp upper bound: the undeleted power P^k is not Lyndon because suffix P^(k-1) is also a prefix, so any optimal length is at most kp-1. For a single deletion, the first or final cycle lexicographically dominates comparisons at its altered run; all interior-copy deletions retain a suffix equal to the initial P and fail. Minimum-letter internal suffixes and terminal-run shortening are treated. At every nonterminal run, exactly one of ascent/descending cases qualifies, giving p positions and q distinct Parikh vectors. Independent literal suffix-checking verified all predicted winning positions on 232 exhaustive small parameter profiles (q=2..4, run lengths=1..2, k=2,3), including nonmonotone letter permutations.

## originality

PASS

General longest-Lyndon-subsequence algorithms and a special case of unique-symbol words do not imply the explicit complete output classification for repeat-run powers: kp-1 length, p positions, q distinct optimizers, ascent/descent switch. Published results on longest run-constrained subsequences and shortest consecutive Lyndon substrings have different predicates. Best-of-knowledge PASS, not priority certification.

## value

PASS

Complete optimizer classification on a natural infinite family of a recognized scattered-subsequence optimization problem. Position- and word-count invariants differ: p potentially many winning positions but exactly q distinct maximizing words, with decisive boundary ascent/descent rule. These exact closed forms and explicit witnesses make a mathematically useful test family not obtained from generic polynomial-time algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
