# Scientific review

## Correctness — PASS

The statement concerns exactly one deletion from ordered ternary four-letter words with at most two distinct source words per received triple. The exact upper certificate is the inequality \(\sum_{y\in D(w)}\lambda(y)+\mu(w)\ge1\) for all \(81\) source words, checked by ten explicitly reported symmetry-orbit cases. Its sums are \(75/8\) and \(21/8\), yielding \(171/8<22\). The explicit \(21\)-word code hits each of the \(27\) outputs twice. The independent standard-library verifier checks all \(81\) inequalities and all \(27\) incidences; the three-word conflict triangle is also verified. No infinite conclusion rests on these finite checks.

## Originality — PASS against inspected evidence

Kiah–Wei–Zeng (arXiv:2609.21395, first public 2026-09-18; revised 2026-11-01), Theorem 28, is an actual finite-length generic bound, but at these parameters its best direct specialization is \(30\), not \(21\). Lin (arXiv:2609.26650, 2026-09-22) states asymptotic **binary** bounds. The closest publicly indexed ternary length-four optimum is the **unique-decoding** value \(11\), not list size two. Binary two-list and ternary covering records likewise do not imply the result. Equivalent deletion-incidence packing, perfect twofold covering, and nondecomposable-code aliases were searched. An unindexed equivalent finite table remains a live priority risk. Relevant parts of the first preprint were inspected in full public PDF text; several related full texts were unavailable and are not claimed to have been examined.

## Mathematical value — PASS

The exact optimum is a natural fixed-alphabet, short-block benchmark for list decoding. Its fractional shadow certificate establishes a strict one-codeword gap below twice the uniquely decodable ternary maximum, while the attaining code is a perfect twofold output cover whose conflict graph is not two-colorable. This separates the list constraint from simple aggregation of uniquely decodable codes. The result is deliberately finite and makes no promise of asymptotic coding-rate gains.

## Limits and nearest comparisons

The result does not extend the exact count to longer words or other alphabets. The strongest directly inspected general finite-length converse fails to settle this case; associated small-block historical tables may be incomplete or unindexed. The second preprint and relevant published code tables were inspected at summary level only, not in full. Independent verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
