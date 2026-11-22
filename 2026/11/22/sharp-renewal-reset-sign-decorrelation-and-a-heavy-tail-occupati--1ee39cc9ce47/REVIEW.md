# Scientific assessment

## Correctness — PASS

The stationary-renewal age/residual formula is normalized by \(m=\mathbb EW\). The free-cycle sign kernel follows from the known generalized last-zero Beta law and the sign-symmetric strong Markov property, with no hidden independence assumption across zero crossings. Conditioning on no intervening reset yields the exact \(C_W(t)\). The pathwise convexity computation, Jensen equality case, Tonelli triangle integral, covariance-to-occupation identity, and regularly varying heavy-tail integration independently establish every displayed implication. The beta prefactor \(Q_{\mu,\beta}\) and borderline \(\beta=2\) logarithm are checked algebraically and numerically. No finite experiment is used as an infinite proof; no distributional central-limit theorem is claimed for non-Poisson clocks. The standalone checker passed all implemented comparisons.

## Originality — PASS (with priority limitations)

The generalized free last-zero law and the Poisson resetting occupation variance are established in the papers cited below, and the Poisson incomplete-Gamma sign formula is treated only as a consistency check. The new theorem concerns *all independent finite-mean stationary renewal reset clocks*, a sharp simultaneous all-lag fixed-mean minimizer, and a precise heavy-tail variance transition with coefficients. Primary full-text comparisons with the 2026 reset papers, the 2024 free-arcsine paper and the 2023 alternating-renewal correlation paper did not show the combined result or stronger coverage. The closest indexed sources concern position covariance of Brownian reset gases, fixed-mean occupancy at a spatial point, and threshold-reset sluggish excursion variance; neither implies this stationary binary-sign comparison without a new kernel and convexity argument. Similar generic regenerative-process and renewal-reward methods are known; the claim is deliberately not that such methods are new. An unindexed general theorem could supersede the result, and database coverage cannot certify absolute priority.

## Value — PASS

A binary sign is a natural low-information measurement of slow diffusion. This finding prescribes an exact optimal reset-time distribution when the reset budget fixes the mean interval, not merely an improved numerical point. It also establishes the exact moment of the reset-time distribution that controls integrated sign memory and the threshold at which empirically measured occupation fractions cease to have the usual inverse-time variance scaling. Sharp coefficients allow direct model comparisons and distinguish power-law clocks from Poisson and periodic protocols. The scope excludes trajectory-dependent clocks, which would require separate analysis.

## Closest literature and limits

- Frimpong, Bresque and Roldán, arXiv:2610.21962 (2026), Sec. 6: Poisson- and threshold-reset occupation statistics; no all-renewal-clock binary-sign theorem.
- Frimpong, arXiv:2610.34568 (2026), Sec. 5: free last-zero law and Poisson reset Gamma distribution; both credited.
- Del Vecchio Del Vecchio and Majumdar, arXiv:2410.22097 (2024): generalized free sluggish-walk arcsine laws, a key input.
- Akimoto, arXiv:2306.00359 (2023), Secs. V–VI: alternating-renewal correlations and occupations, with different externally imposed sign dynamics.
- Indexed nearby results on threshold resetting, Brownian two-time position correlations, and fixed-mean reset occupancy have materially different observables and hypotheses.

Self-review: passed. Independent audit: not yet performed.
