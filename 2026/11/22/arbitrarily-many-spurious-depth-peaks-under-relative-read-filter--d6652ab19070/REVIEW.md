# Self-review

## Correctness: PASS

PASS: conditioning gives an exact positive Poisson series; on the event that the Poissonized total stays within its nearest-integer margin the count-ratio test equals a Poisson integer threshold. Chebyshev supplies an explicit O(1/K) comparison at every noninteger effort; each positive jump of the limiting tail yields a strict finite-K interior peak, and analyticity makes it strict. The packaged outward-rounded standard-library checker establishes fourteen separated interval inequalities for the actual 0.1% cutoff, with a positive analytic truncation bound. No finite experiment is used as proof of arbitrarily many peaks.

The assumptions, strict-inclusive read threshold, positive-count guard, exact distribution, and distinction between limiting and finite cutoff cases were reconstructed. The seven-peak bound is proved by strict interval comparisons; the general arbitrary-peak result follows analytically and is not extrapolated from finite checks.

## Originality: PASS on inspected evidence

PASS on material inspected: primary metabarcoding papers empirically motivate relative-abundance filters; known binomial/Poisson exact-test sawtooth literature concerns discrete test-power critical values, not this continuous-effort two-Poisson ratio-tail probability and its rare-threshold limit. Related published mathematical findings concern singleton-richness or richness-variance peaks, not a dominating proposition. Historical priority is provisional due to broad potentially related statistical literature.

Closest prior work: Westerduin et al. (2023), Drake et al. (2022), Alberdi et al. (2018), Gentile and Sambucini (2023), and the classical sawtooth-power abstract of Chernick and Liu (2002). Comparison is by hypotheses and implications rather than by title matches. The Chernick–Liu full text was unavailable through inspected public access. Earlier general theories may yet cover or anticipate the mechanism; this is the main residual priority risk.

## Value: PASS

PASS: 0.1% relative abundance is directly used by a motivating ecological study, and the exact finite seven-peak certificate proves that repeated spurious acceptance peaks are not merely a scaling-limit artifact. Arbitrarily many maxima under decreasing cutoffs expose a counterintuitive limit to choosing sequencing depth from one unimodal error curve. The result is a motivated analytical boundary for fixed-fraction read filtering, not an arbitrary table recomputation or field recommendation.

The target is false retention of an individual nonlocal sequence in an idealized composition model, not a claim about any sampled locality or an empirical intervention. The mathematical result provides a concrete caution about inference from a one-peak model of filtering error across sequencing depth.

## Scientific limitations

The theorem assumes independent Poisson counts, fixed composition and a single spurious sequence; it excludes PCR amplification bias, tag jumping, clustering across samples, and overdispersion. The seven-peak result is a certified lower bound, not a full extremum census. Independent experimental verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
