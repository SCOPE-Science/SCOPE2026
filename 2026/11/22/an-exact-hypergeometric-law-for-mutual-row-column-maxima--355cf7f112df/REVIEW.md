# Scientific assessment: exact mutual row–column maxima law

## Correctness — PASS

The domain is every pair of positive integers \(r,c\) and iid atomless entries; a monotone probability-integral rank transformation reduces all ordering events to iid uniforms. The key nonstandard step is the exact joint-event integral for a prescribed nonattacking \(k\)-set: the \(k(r+c-2k)\) external row/column cells contribute individual powers, and the \(k(k-1)\) cross-cells contribute squared minima. Sorted-simplex integration gives \(1/(r+c-1)_{\underline k}\). Counting ordered matchings yields all factorial moments, identifying the *entire* hypergeometric distribution on its finite support. Row-column exchangeability gives the complete random matching-set law. The mean, variance, boundary cases and normalization follow from the identified distribution. Exhaustive, integer-exact checks cover eight boards through \(3\times3\); enumeration corroborates but does not replace the general proof.

## Originality — PASS, with residual priority risk

The closest directly matching square-rook model is Baldi–Rinott–Stein (1989), section 3, example 2; it gives the square-board expectation, variance and normal approximation, but no finite exact count law. Bhamidi–Dey–Nobel (2012), section 2.5 and Theorem 2.10, cover the square one-cell case and general submatrix maxima at the level of moments and central limits rather than the rectangular count and full labelled matching law. Mimun–Quattropani–Scarsini (2022) analyze correlated-payoff best-response dynamics, and Collevecchio et al. (2024) analyze equilibrium attraction basins; these primary results involve the identical-payoff interpretation but do not furnish the hypergeometric law. Searches for the exact law under row/column maxima, rook-graph local maxima, hypergeometric occupancy and common-interest equilibrium aliases found no direct implication or stronger covering theorem. Searches are not proof of historical priority; an unlocated prior exact enumeration remains possible.

## Value — PASS

The statistic is the entire set of mutual row/column optima of an iid array, also the pure equilibrium set of a random common-potential two-player game. Its random matching geometry is a natural object, and exact finite sample calibration of how many optima can coexist is not supplied by the published mean, variance and Gaussian asymptotics. The hypergeometric identification gives all finite probabilities, quantiles and the uniform conditional geometry without a limit; it complements rather than merely restates the known first- and second-moment formulas. It is not asserted as an algorithmic speedup or a claim about attraction basins.

## Limitations

Historical-priority review is not exhaustive. The result does not extend automatically to nonidentical or dependent scores, ties, two independent payoff arrays, or marked equilibrium heights. Verification uses a finite exhaustive checker in addition to a complete analytic argument. External expert review is outstanding.

Self-review: passed. Independent audit: not yet performed.
