# Scientific review

## Correctness — PASS
The claim concerns the exact non-repeating-edge model. The count of unused \(k\)-sets gives an exact hypergeometric transition for isolated-vertex losses, including the exhaustion convention. The centered contrast \(D_t=I_t-rN_t\) has negative linear drift; bounded innovations, fourth-moment control and a martingale triangular-array CLT yield the explicit covariance matrix. Its positive definiteness follows from nondegenerate binomial edge sampling. The pure-Python checker passed 1,412 exact assertions; additional seeded simulation matched the theory within 1.6% for three tested examples. Finite verification does not replace the analytical argument.

## Originality — PASS against inspected evidence
The closest source, Krapivsky's full 2026 preprint, gives average cluster densities but explicitly leaves fluctuation variances of isolated vertices uncomputed. Betken's full 2019 paper studies preferential attachment with per-vertex edge choices rather than independent uniform hyperedge creation. Related fixed-edge hypergraph isolation-covariance results and an earlier note on repeat hyperedge selections do not imply the asserted joint Gaussian limit or its coefficient. Targeted searches found no equivalent theorem. Residual risk: earlier general stochastic approximation or dynamic random-graph work might contain a sufficiently broad result.

## Value — PASS
Isolated vertices are a natural extensive statistic in the growing uniform hypergraph, with fluctuations explicitly identified as an open quantitative gap in the motivating analysis. The theorem provides the sharp \(\sqrt t\) scale, the complete covariance with the random vertex population, and the exact positive limiting variance on both sides of a nonstandard giant-component transition. No additional conjectural downstream consequence is asserted.

## Scope and verification limits
Fixed \(k\ge3\), fixed interior \(p\), finite initial hypergraph; no finite-time error bound, no varying-parameter limit, and no independent mathematical assessment.

Self-review: passed. Independent audit: not yet performed.
