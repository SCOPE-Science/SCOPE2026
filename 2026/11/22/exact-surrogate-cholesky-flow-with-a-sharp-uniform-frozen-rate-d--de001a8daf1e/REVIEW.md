# Scientific review

## Correctness — PASS

The theorem fixes the entire domain \(\alpha\ge0\), \(s\ge\alpha\), \(s>0\), \(T>0\) and differentiates the purported exact coefficient against the non-autonomous linear ODE. The elementary logistic representation controls \(\alpha T\le pT\le\alpha T+1/2\). Strict log-convexity of the Laplace integral gives the global sharp ratio, with a strictly positive-pivot sharpness sequence. The standard Schur complement plus the bound \(\alpha g^2<1\) proves recursive positive semidefiniteness, including the zero-pivot case. Deterministic checks reproduce scalar ODE integration and matrix examples; finite checks are not substitutes for the global proof.

## Originality — PASS, subject to historical-priority risk

The cited primary full text gives the same surrogate ODE but evaluates its off-diagonal coefficient by freezing the terminal diagonal; the exactly integrated coefficient and the sharp \(q=2(1-e^{-1/2})\) comparison are not stated there. The paper's positive-definite well-definedness proof applies to the frozen version; the present proof establishes a different PSD-safe update. Searches for aliases such as the exact non-autonomous logistic off-diagonal solution, frozen-rate error and coefficient bias, as well as published findings on pivoted and incomplete Cholesky, did not reveal a statement implying the sharp bound. Searches alone cannot establish priority, and comprehensive historical coverage is not asserted.

## Value — PASS

The correction replaces one scalar evaluation rather than introducing numerical ODE solves. The sharp possible \(21.31\%\) relative coefficient deficit, \(38.07\%\) rank-one update deficit and the PSD guarantee identify an operationally meaningful finite-time modeling bias, particularly at nearly singular pivots, which are a central motivation for the underlying numerical algorithm. This does not claim whole-matrix error improvement or numerical backward stability.

## Source comparison and limitations

Closest primary source: Manavalan and Schönlieb, *Finite-time Cholesky factorization*, arXiv:2611.09706v2, Section 2.2, Algorithms 1–2 and Section 2.3. Its frozen coefficient is not the exact solution of the time-varying surrogate unless the diagonal remains constant. Related published randomized-pivot and incomplete-factorization work has different mathematical objects. The residual risk is unindexed equivalent analysis of this scalar linear equation or its particular algorithmic consequences.

Self-review: passed. Independent audit: not yet performed.
