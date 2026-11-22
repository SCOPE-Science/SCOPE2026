# Self-review

## Correctness

**PASS.** The normalized expected-information model follows from a Gaussian measurement with calibrated variance and an independent Poisson no-hit probability. Each mode's unique time maximum follows from an explicitly strictly decreasing logarithmic derivative. The exact quadratic numerator controlling the difference of the two derivative curves has one positive root when the sum and product rankings oppose each other. The envelope derivative and its two rigorously derived endpoint asymptotics prove exactly one optimized-mode crossing, including the strict preferred-duration ordering at the tie. The analytic single-mode mean-hit-time condition and the optimality bound for mixed cycles are derived separately. The standalone diagnostic checker passed 29,265 finite assertions; finite checks are not used as a proof for arbitrary positive parameters.

## Originality

**PASS relative to searched and materially inspected literature, with residual historical uncertainty.** Fixsen et al. (2000) analyze cosmic-ray damage and nonlinear readout processing, while Regan and Stockman (2001) give a numerical optimization framework for multiple read modes under specified radiation and detector characteristics. These are the closest inspected works; the latter is substantially related and is not treated as unrelated merely because its mathematical variables differ. Neither inspected text supplies an exact all-radiation-rate classification for two independently optimized readout modes, the necessary-and-sufficient opposing sum/product ranking criterion, or the discontinuous optimum-duration change. General single-mode optimization formulas do not imply the one-crossing theorem without the extra quadratic-sign and envelope argument. Unindexed sources or alternate detector models might contain a stronger statement; priority has not been independently certified.

## Value

**PASS.** Comparing two detector readout modes while allowing each mode's exposure time to reoptimize is a natural decision within astronomy. A pairwise comparison at one hazard does not determine if repeated preference reversals are possible as space-radiation conditions vary. The theorem gives a complete no-switch / one-switch classification and proves a genuine jump in preferred exposure duration; it also reveals the interchangeable roles of overhead and read-noise-equivalent time in this idealized information objective. The result is a precise benchmark for protocol analysis, not practical advice to override instrument constraints or software capable of recovering partly damaged exposures.

## Limitations and closest literature

The exact analysis assumes known stationary Gaussian noise variance, independently flagged whole-exposure losses, common radiation hazard and background across modes, unlimited repeated cycles, and no additional mode-change costs. Actual HST/JWST read ramps, photon-counting and saturation constraints can violate these hypotheses. The closest historical comparison is Regan and Stockman (2001), *Optimum Integration Times for Different Read Modes*, section 4 and Figures 2–4. Fixsen et al. (2000), arXiv:astro-ph/0005486, provides the most relevant earlier open full-text discussion of cosmic-ray loss versus detector read noise. Anderson and Gordon (2011), arXiv:1109.2626, studies more sophisticated cosmic-ray detection but was assessed from an abstract rather than a complete text. Independent historical-priority review remains necessary.

Self-review: passed. Independent audit: not yet performed.
