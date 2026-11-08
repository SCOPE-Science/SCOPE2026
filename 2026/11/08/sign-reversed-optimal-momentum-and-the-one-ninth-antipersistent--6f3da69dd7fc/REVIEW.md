# Scientific review: sign-reversed optimal momentum

## Correctness — PASS

The full augmented-state covariance equation is explicitly given and solved in RESULT.md. Direct Schur–Jury stability, rational factorizations, and differentiation establish the global sign result. The positive decomposition, compactness of minimizer rescalings, and uniform asymptotic expansion establish the sharp \(1/9\) limit and square-root approach. The standalone symbolic verifier solves the actual Lyapunov equation, checks the two factorizations and leading singular expansion, and evaluates exact rational examples. Critical boundaries \(|q|=1\) and \(\beta\in\{-1/2,1\}\) are excluded as unstable/nonstationary, not included by continuity.

## Originality — PASS, with publication-precedence risk

Kühn and Rosenow (arXiv:2306.05300, Theorem 4.3, Appendix C and J) obtain stationary heavy-ball relations for a different, finite-epoch anticorrelation law and restrict momentum to the nonnegative range; those results do not imply the sign reversal across the full negative-momentum stable interval or the sharp AR(1) optimal boundary layer. Dang et al. (arXiv:2401.06738) and Pan et al. (arXiv:2312.14567) study accelerated stochastic heavy ball in other noise regimes. Xie et al. (arXiv:2103.17182) use a distinct two-buffer positive-negative optimizer. Searches of published mathematical results and accessible earlier claim statements exposed no equivalent. An unindexed classical ARMA/control-theory variance-minimization formula remains a specific precedence risk, and independent comparison is not complete.

## Value — PASS

The question is motivated by measured temporal anticorrelation in epoch-based stochastic optimization, which can change stationary risk. The result gives a full global sign rule, not a local perturbation; it proves the unexpectedly finite universal ninefold improvement ceiling in the extreme anticorrelation regime and a sharp square-root tuning law. It directly distinguishes positive from negative momentum on a canonical quadratic benchmark and quantifies the penalty for selecting the wrong sign. This is a structural optimization conclusion, not an isolated numeric example.

## Scientific limitations

AR(1) is a simplified stationary colored-noise benchmark rather than the exact without-replacement epoch covariance. The exact matched-step scalar assumptions are necessary in the stated theorem. No finite-horizon or nonquadratic guarantees, practical tuning guarantee, or globally unique fixed-correlation minimizer are asserted. General linear-filter theory may contain an equivalent result that was not located. The symbolic checks support, but do not replace, the analytical minimizer argument.

Self-review: passed. Independent audit: not yet performed.
