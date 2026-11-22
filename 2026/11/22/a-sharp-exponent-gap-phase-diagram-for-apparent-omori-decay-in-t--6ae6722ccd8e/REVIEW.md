# Self-review

## Correctness — PASS

Reconstructed the dimensionless logarithmic slope and its exact derivative, checked the stationary-curve bijection \(y=g(u)\), the monotonicity and endpoint limits of \(u/g(u)^\delta\), and the critical double root. For \(p=1\), \(q=3\), exact rational evaluation gives the sharp ratio \(81/169\) and the polynomial factorization; standalone `checker.py` passed 3,668 supplementary deterministic assertions. The derivation covers all positive amplitudes, offset and exponents with \(p<q\). Numerical sampling alone is not used as a proof.

## Originality — PASS, subject to the stated priority risks

Statement-level comparison: the historical 1995 additive two-power formula has exponent gap exactly one and does not imply the strictly greater-than-one two-turn threshold; Sornette and Sornette (1999) analyze branching-convolution power-law regimes, not this explicitly summed curve; Lolli et al. (2009) compare other aftershock decay model classes. The closest indexed mathematical result for nonmonotone apparent Omori slopes varies **offsets with common exponent**, whereas here **one offset is fixed and the exponents vary**. No searched publication was found to establish the same sharp threshold. Generic work on mixtures and historical priority beyond inspected material remains a substantive residual risk, so novelty has not been independently certified.

## Value — PASS

The sharp threshold distinguishes a common-offset, two-component decay that merely steepens or relaxes its apparent log-time slope from one with two opposing slope transitions. It gives an exact mechanism by which a monotonically decreasing rate can have reentrant apparent decay, and a sharp negative criterion for the historically used first-plus-second inverse powers. The result directly clarifies potential misinterpretation of local slopes, without asserting any empirical mechanism.

## Limitations and closest literature

Utsu, Ogata and Matsu’ura (1995), https://doi.org/10.4294/jpe1952.43.1 ; A. and D. Sornette (1999), https://arxiv.org/abs/cond-mat/9905314 ; Lolli, Boschi and Gasperini (2009), https://doi.org/10.1029/2008JB005614 . The historical review was materially inspected in Sections 2 and 4.1 (historical additive powers and secondary sequences), not exhaustively. Stochastic inference and physical validation are absent. The underlying formula shares the shape of other positive mixture problems, whose possible stronger theory is unresolved.

Self-review: passed. Independent audit: not yet performed.
