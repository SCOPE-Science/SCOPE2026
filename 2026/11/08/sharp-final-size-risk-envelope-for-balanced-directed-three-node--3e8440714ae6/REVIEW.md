# Scientific review

## Correctness — PASS
The full row/column-balanced, zero-self-loop contact family is uniquely parameterized by a clockwise weight \(p\). Conditional exponential competing risks give an exact final-size distribution, and the only two nontrivial tail probabilities prove first-order stochastic ordering. A derivative has one positive critical point and vanishing boundary values, yielding the unique global cross-strength maximum. The independent CTMC generator reconstruction in `CHECKER.py` verifies the hitting probability and the exact derivative, with no extrapolation from samples.

## Originality — PASS (with risk)
The motivating 2026 network SIR study provides the Markov generator and next-generation matrix but no weighted directed triangle exact risk envelope. The 2016 exact small-network results **already cover** the undirected equal-edge triangle and are explicitly attributed: the new assertion is the all-balanced-directed fixed-reproduction ordering and maximized gap. Inspected directed message-passing literature does not provide the same cyclic-network result, while exact tree results do not apply. Multiple named searches of relevant research records, the current body of accessible prior findings, the primary full texts and the closest undirected table did not find a dominating claim. The closest-source supplementary Appendix B was not independently retrieved, and a latent equivalent general finite-network theorem cannot be excluded. A failed search alone is not novelty evidence.

## Mathematical value — PASS
The question is natural because networks with the same spectral epidemic threshold may differ substantially in final-size risk, and three nodes are the smallest balanced loopless class allowing directional choice. A complete distribution and sharp stochastic order over all such matrices, plus a universal exact gap attained at a non-obvious rate ratio, give a finite, interpretable boundary example for network-vulnerability comparisons. This is not offered as a broad all-network theorem and does not rely on numerical novelty alone.

## Sources and limitations
Primary comparison: Ueki–Thompson–Banaji, arxiv:2601.13730 (model, architecture, approximations); McCulloch–Roberts–Laing, DOI 10.1017/S1446181116000043 (undirected triangle and other small-network exact final sizes); Wilkinson–Ball–Sharkey, DOI 10.1007/s00285-017-1123-8 (directed stochastic SIR framework); Hall–Siebert, DOI 10.1007/s00285-022-01854-9 (exact trees and general bounds). The stated theorem is only for three equal individuals and independent Markov SIR infections/recoveries. All source comparisons are subject to the listed residual indexing/supplement risks.

Self-review: passed. Independent audit: not yet performed.
