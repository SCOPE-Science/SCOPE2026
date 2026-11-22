# Scientific review

## Correctness — PASS

The argument derives the Laguerre step coefficients from exact integration, invokes Pythagoras for the orthogonal projection, and reduces the operator norm on real finite-variation data to single-jump residuals using the variation measure. It then differentiates a polynomial-exponential residual and exactly enumerates all its critical points for degrees zero through five. The finite proof relies on explicit rational sign-change brackets for every root of the auxiliary degree-\(2n\) polynomial and rigorous exponential Taylor remainder intervals, not on sampling or a floating-point optimizer. Every stationary value is enclosed and the winner is strictly separated from every competitor. The singleton maximizing location forces a unique jump form for every nonconstant extremizer. The embedded `CHECK.py` executes successfully with standard Python 3.

## Originality — PASS, with historical-priority risk

The closest published Laguerre bounded-variation result optimizes the absolute value of one generalized-Laguerre coefficient, not the \(L^2\) norm of the full spectral tail after orthogonal projection. Its Sonin-envelope classification therefore does not cover the stated global branch relocation for the total residual. Tang–Zhou (2014) investigate random evaluation stability of Gamma/Laguerre polynomial expansions, not the sharp variation-ball truncation error. Published comparisons for other orthogonal systems do not cover an exponential Laguerre projection-tail classification. Literature searches compared coefficient, residual, Heaviside and gamma-chaos aliases. The possibility of an unindexed historical exact residual result cannot be excluded.

## Value — PASS

The first global relocation of an extremizing jump at degree five is a natural structural threshold in a canonical, nested approximation scheme rather than an arbitrary coefficient evaluation. Degrees three and four already have competing local maxima, yet the hard-edge branch still wins; degree five is the first point where the interior branch wins, despite the strictly decreasing overall projection error. The exact classification provides a reproducible worst-case benchmark for low-degree Gamma polynomial-chaos truncation of discontinuous data. The small margin makes rigorous rather than numerical certification essential. The contribution does not claim a high-degree asymptotic theorem.

## Scientific limitations

Only degrees zero through five and the ordinary exponential law are covered. No higher-degree optimizer classification, generalized-Gamma parameter theorem or independent validation is asserted. The cited Laguerre coefficient paper was materially inspected; other possible historical treatments not indexed in the searches remain a priority risk.

Self-review: passed. Independent audit: not yet performed.
