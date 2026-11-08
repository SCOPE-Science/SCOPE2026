# Review of strict negative dependence between extreme-key depths

## Correctness
**PASS.** The claimed domain is the uniformly permuted insertion tree with \(n\ge2\) and edge depths. The ancestor-as-record identity yields the Bernoulli marginal law. Conditional on the root's uniform rank, the two extreme-key depths are independent; their conditional expectations are the harmonic numbers of the two complementary subtree sizes. The reversed Chebyshev inequality proves strict negative dependence for all nonconstant increasing transforms. The second derivative of the binomial-series coefficient at exponent two yields the exact mixed moment and covariance. The independent Gaussian limit follows from a uniform-in-central-root-splits triangular-array CLT, with the omitted root-split tails vanishing as the central restriction expands. All 796 exact standalone checks pass; finite checks are not substitutes for the analytic infinite statements.

## Originality
**PASS, with priority risk.** Closest literature: Seidel–Aragon (1996) supplies the random-priority model and marginal analysis; Devroye–Neininger (2004) supplies record representations and normal limits for ranks/path lengths; Panholzer–Prodinger (2004, arXiv math/0405292) supplies marginal moments of randomly chosen spanning-tree sizes and a related harmonic-square coefficient identity. The inspected material does not give a negative-quadrant theorem for the fixed smallest/largest depths or the displayed bivariate covariance. Unlike randomly selected pairs, the two extreme keys are fixed ranks. The derivation draws on familiar tools, and an earlier unstated consequence of multivariate treap formulas cannot be ruled out without an exhaustive historical audit.

## Value
**PASS.** Search costs at opposite ends of an ordered key universe are natural jointly observed operations. The general dependence ordering supplies inequalities for every increasing cost transformation, not merely a single moment, while an exact strictly decreasing covariance and an independent bivariate Gaussian limit distinguish persistent unnormalized dependence from asymptotic decorrelation. These joint statements are not consequences of the two separate marginal normal laws.

## Limits
Uniform random insertion only; no claims for biased trees or arbitrary key pairs. No negative-regression claim and no independent external audit. The finite checker covers the stated ranges only.

Self-review: passed. Independent audit: not yet performed.
