# Scientific review

## Correctness — PASS

The middle-coordinate weighted three-site isotonic fit has precisely four continuous affine branches. In every branch its Jacobian is a nonnegative tridiagonal row-stochastic matrix with left and right neighbor weights bounded by \(a/(a+b)\) and \(c/(b+c)\). Expressing consecutive output differences in input-difference coordinates gives three coefficients per input edge and the exact absolute-column upper bound \(K(a,b,c)\). Piecewise-affine segment integration establishes the two-input inequality. Two strictly decreasing, four-edges-separated cuts in an explicit alternating eight-site signal produce disjoint derivative packets of that exact norm; small finite perturbations realize equality, and the construction embeds in every longer cycle. The checker passed 5,000 exact-rational inequalities, 30 exact-rational finite-pair equalities, and four branch checks. The universal result is based on the proof, not enumeration.

## Originality — PASS, qualified

Kearsley (2006, fully inspected relevant sections) develops weighted globally ordered isotonic regression and PAV pooling; it does not analyze overlapping cyclic three-site center outputs or two-input variation amplification. Dubois (2010 posting; inspected introduction, interpolation definitions, selected variation estimates) gives a different conservative nonlinear interpolation/TVD framework. Harten (1983) and Tadmor (1988) contribute general incremental TVD conditions; those criteria explain an upper-bound mechanism but do not give this operator-specific exact unstable gain, geometric-mean threshold and attained examples. A published sharp weighted-chain isotonic variation theorem concerns one global fit on a directed chain, not overlapping local fits; published three-point running-median stability results use rank selection rather than weighted isotonic averaging. Statement/implication searches found no exact covering result. The Harten and Tadmor original texts were not fully read, and unindexed equivalent local-filter work is a residual priority risk. No independence of the historical-priority assessment is claimed.

## Value — PASS

The result gives a complete, exact and dimension-independent stability threshold for a natural nonlinear local shape-constrained smoother. The center weight must be at least the geometric mean of its outer weights for nonexpansivity in the difference-variation metric. If it is smaller, the precise amplification is attained by actual signals, not only by infinitesimal derivatives. This separates safe from unsafe weighting in overlapped isotonic smoothing and distinguishes a stronger two-input robustness requirement from one-signal variation diminution. The naturalness comes from classical weighted PAV regression and the standard adjacent-variation seminorm, not a chosen ad hoc parameter slice.

## Scope and residual limitations

The exact formula and attainment are established only for cyclic real signals with at least eight sites, fixed positive within-window weights, and a three-site nondecreasing local least-squares fit. Smaller-cycle constants, other window lengths and arbitrary graph neighborhoods remain open here. Full historical priority is not certified; older general TVD articles and unindexed overlapping-filter sources could contain equivalent conclusions.

Self-review: passed. Independent audit: not yet performed.
