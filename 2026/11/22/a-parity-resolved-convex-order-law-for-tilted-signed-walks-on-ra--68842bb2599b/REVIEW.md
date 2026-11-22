# Scientific review

## Correctness — PASS
For fixed walk time, rooted signed neighborhoods concentrate around an independently marked infinite regular tree. Exponential tilting changes precisely its root-adjacent signs. Radial parity and one-step flux provide the mixture coefficients, and a finite-difference identity proves strict convex order. The equal means, exact variance gap and return-asymptotic constant follow from these constructions. The standalone exact-rational checker passed 5,400 assertions. Risks: the asymptotic is sequential (first graph order, then time); no uniform two-parameter statement follows.

## Originality — PASS against examined literature
Louvaris and Trevezas, arXiv:2611.17118, Theorem 1 and Example 1, concern start-versus-later stochastic order and a one-step conditional-mean bias. They do not state the paired actual-score distribution, convex-order reversal, variance gap or decay. Hazra, den Hollander and Parvaneh, arXiv:2502.17724, concern multi-level degree biases, without signed-score time-marginal pairs. Related work on regular-tree returns supplies ingredients, not the combined conclusion. Semantic similarity searches and source comparisons found no equivalent or stronger covering result. Residual risk: unindexed random-scenery or signed-network work could contain an implicit generalization; this is not an independently established priority claim.

## Value — PASS
The motivating general dominance principle controls only comparisons with time zero and explicitly leaves between-time comparisons open. This theorem establishes a sharp obstruction: consecutive times can have equal expected signed score yet fail to be ordered stochastically, while admitting strict convex ordering and an exact asymptotic variance gap. The full laws identify the entire mechanism, with a controlled decay scale, rather than a numerical isolated counterexample. This is a structural and testable boundary for interpreting multistep sampling bias.

Self-review: passed. Independent audit: not yet performed.
