# Scientific review

## Correctness: PASS

The exact innovation recurrence \(v_{j+1}=(1-p_j^2)v_j+p_j(1-p_j)\), \(v_2=0\), follows from conditional total variance. Orthogonality gives the variance series for the already established centered path-length limit. Uniform bounds \(p_j=j^\alpha(1+O(2^\alpha))\), \(v_j=O(2^\alpha)\) in the extreme old-age regime isolate the index-three contribution \(18^\alpha\), the index-four contribution \(32^\alpha\), and a tail of order \(O(50^\alpha)\). The correction of the first term is \(O(36^\alpha)\), which is smaller than \(32^\alpha\). The remaining martingale tail is negligible in squared standard-deviation units, while the leading Bernoulli innovation is activated with probability tending to zero. This establishes the weak collapse without incorrectly inferring second-moment convergence. The independent checker passed 49 exact and numerical assertions; these supplement, not replace, the analytic argument.

## Originality: PASS, with residual historical risk

Gałązka--Wdowicka (2026), arXiv:2610.00614v1, proves the fixed-parameter martingale limit and exact variance recurrence, but its open-problems discussion specifically identifies asymptotics of the variance coefficient as an outstanding question. The two explicit extreme-parameter terms and the unit-variance weak collapse are not reported there. The 2022 insertion-depth literature concerns one-vertex marginals, not the cross-vertex global correction. Searches for the same variance asymptotics, rare-event degeneration, equivalent global statistics, and stronger weighted-tree statements did not produce a directly covering theorem. The exact recurrence is acknowledged as existing input; the asymptotic passage requires a new uniform parameter argument. A broader as-yet-unlocated theorem could still subsume the claim, and older insertion-depth full text was not completely inspected.

## Value: PASS

The variance coefficient is a natural invariant of total path length and its exponent dependence is expressly singled out in the motivating paper. The explicit bases \(18\) and \(32\) identify which two earliest random choices dominate a global observable in the strong old-age regime. The second conclusion shows that variance-normalization gives a degenerate weak limit, clarifying why ordinary Gaussian approximations fail in this parameter limit. This is a meaningful boundary description of a natural stochastic tree family, not an arbitrary finite numerical computation.

## Scope and limitations

All tree-size limits occur at fixed \(\alpha<-1\) before the extreme-parameter limit. Nothing is asserted about arbitrary simultaneous \(n\)-and-\(\alpha\) limits. Independent mathematical verification and exhaustive historical-priority checking have not been performed.

Self-review: passed. Independent audit: not yet performed.
