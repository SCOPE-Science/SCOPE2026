# Self-review

## Correctness: PASS
The statement quantifies over all integers \(w\ge2\), ranks \(1\le r\le w\), and plateau lengths \(1\le\ell\le w\). A common candidate value must lie in the intersection of the windows. Equality of the rank at all times forces each leaving and entering pair to have identical exceedance status; this characterizes **all** successful patterns without overlap. Exact beta integration yields the finite factorial sum. A stationary subtraction yields the entry-conditioned lifetime law and a telescoping identity its expectation. Rational asymptotics with uniform smooth remainder at interior fractions and a separate exact endpoint calculation establish the limit, including the exceptional atom. The standalone checker passed 1,678 exact assertions with exhaustive permutations for small widths. No finite computation is used as the sole justification of an infinite assertion.

## Originality: PASS within inspected evidence
The rank-one duration formula was already known and is acknowledged. The motivation in Bücher–Haufs analyzes overlapping top-two order statistics for estimator theory and does not establish finite exact plateau lifetime distributions. Raykov's full paper is algorithmic and not a probabilistic exact run-law. Other searched records on sliding window extrema, run lengths, and kth-order records addressed distinct objects. No inspected source states or implies the all-rank finite lifetime formula or the endpoint-atom discontinuity for fixed higher ranks. This remains a best-knowledge assessment, not absolute historical priority; a general unlocated rank-pattern enumeration identity is a real residual risk.

## Value: PASS
A complete distribution-free classification for each rank of a classical moving-order-statistic process is natural and motivated by the use of overlapping top-two blocks in extreme-value inference. Unlike a routine change of normalization or a small numerical gain, the theorem uncovers a rank transition in the limiting topology of the law: only the maximum has a surviving mass at a full-window plateau, whereas all higher fixed ranks have a continuous distribution. It also gives exact waiting-time means and finite cutoff probabilities useful for understanding dependence among overlapping order-statistic observations. No estimator efficacy or independence of successive plateaus is claimed.

## Closest sources and limitations
Bücher–Haufs, arXiv:2502.15036, Sections 4.2 and B.2; Raykov, doi:10.4230/LIPIcs.ICDT.2023.5, abstract, introductory and algorithm sections; prior rank-one sliding-maximum result `704d29c1-2dc2-4668-a533-b867764fe7c2`. Continuous iid sampling and fixed rank are essential for the stated conclusions; earlier unseen combinatorial literature could contain equivalent enumeration.

Self-review: passed. Independent audit: not yet performed.
