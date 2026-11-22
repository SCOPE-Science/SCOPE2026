# Scientific review: balanced ternary two-deletion codes

## Correctness — PASS

The proof gives a complete 90-source reduction to a finite compatibility graph, a unique-increasing-index enumeration of every clique, and an explicit legal four-word witness. Two independent implementations respectively use exact deletion-shadow intersections and LCS dynamic programming; both determine 1164 compatible pairs, 1788 triples, 144 four-codeword optima, and no five-codeword optima. The symmetry action is exact and the 14-orbit census sums to 144. Exact rational primal/dual witnesses independently establish the fractional optimum five. These computations were rerun from the packaged scripts, without third-party solver assumptions. The check is finite and does not purport to generalize by experimental induction.

## Originality — PASS (historical qualification)

Farnoud–Milenkovic (arXiv:1312.2163v1) treat regular multipermutation Ulam codes and general bounds, not the precise 90-vertex maximum-four shadow code or its exhaustive equality census. The already published balanced ternary length-six one-deletion study addresses a weaker channel and is not an implication of this two-deletion optimum. Published binary two-deletion and unordered multiset-deletion results differ in alphabet or output semantics. Semantic research comparisons did not reveal a dominating claim. A directly relevant 2014 conference paper by Sala–Gabrys–Dolecek was available as an abstract only; its full text remained inaccessible, leaving a genuine historical-priority risk. A failed search does not prove novelty, and this is a self-review, not an independent priority certificate.

## Value — PASS

The fixed composition \((2,2,2)\) is the smallest uniformly repeated ternary multipermutation space and is a natural finite benchmark for unordered-position deletion synchronization where output order matters. The exact two-deletion capacity, all equality configurations and fractional-to-integral gap answer complementary optimization questions with explicit future use as benchmark instances for short-word code design and polyhedral bounds. The result is more than routine substitution: the LP has optimum five, so a nontrivial integral obstruction excludes five codewords.

## Scientific limitations and closest sources

All assertions are for six positions and exactly two deletions; no claim is made about different compositions, longer lengths, burst deletions, or Kendall adjacent-swap errors. The exact exhaustive enumeration is replayable, not independently audited. Relevant literature: https://arxiv.org/abs/1312.2163 ; https://doi.org/10.1109/ISIT.2014.6875338 (full text unavailable); https://arxiv.org/abs/1507.07628 ; and the already published one-deletion study linked in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
