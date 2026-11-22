# Scientific review

## Correctness — PASS

All dimensions \(n\ge3\), horizons \(K\ge1\), and correlations \(0<\rho<1\) are covered by a projection composition identity and a finite-sign expansion. The latter proves strict global balancing of the correlated pair for any fixed total pair mass. Balancing the orthogonal modes then yields the unique exact optimizer and sharp expected terminal-loss value, including probability-simplex boundaries. The included standalone checker passed 864 finite comparisons, which support but do not prove the universal assertions.

## Originality — PASS, with residual historical risk

The general batch-sampling framework of Xie–Yang (arXiv:2610.04685), Gower–Richtárik's sketch-and-project analysis (arXiv:1506.03296), and Rodomanov–Kropotov's fixed-volume method (arXiv:1904.04587) are examined. A published one-step optimal omission rule covers the case \(K=1\); a published fixed-volume analysis provides the transfer-matrix method for one chosen distribution. Neither statement, nor other retrieved near matches, asserts the all-horizon globally optimal static law or supplies the strict imbalance inequality required to derive it. The exact one-step optimizer and the idea of transfer matrices are not claimed separately new. Unknown prior equivalent formulations remain a risk.

## Value — PASS

Choosing one fixed batch distribution is a central practical question in randomized block descent. For a transparent, fully solvable and strongly convex instance, the best distribution depends strictly on the number of updates left even though all candidate blocks have equal size and cost. Reusing the one-step-optimal distribution incurs an exponentially increasing relative worst-case terminal expected-loss penalty. This establishes a meaningful distinction between one-step bound optimization and finite-horizon design; it does not extend to all dense systems or adaptive sampling.

## Limitations and closest sources

The source and related literature are linked in RESULT.md. The all-horizon claim is limited to one correlated column pair and exactly minimized all-but-one-coordinate blocks; priority remains subject to independent human mathematical review.

Self-review: passed. Independent audit: not yet performed.
