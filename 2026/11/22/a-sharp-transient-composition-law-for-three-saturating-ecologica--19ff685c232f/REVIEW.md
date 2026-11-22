# Scientific review

## Correctness — PASS

All parameters are explicit: positive plateaus \(a,b,c\), ordered positive rates \(0<\lambda_1<\lambda_2<\lambda_3\), positive deployment time, and a fixed integer read depth. Cancelling the common slow-rate factor reduces the middle marker's compositional share to two generalized geometric sums. The ratio of their derivatives is a strictly increasing upper-tail mean under a positive weight, so the scalar threshold function increases exactly from zero to \(\Theta=r(r-m)/(m-1)\). This proves the unique interior optimum if and only if \(a/c<\Theta\), with the correct monotone boundary case at equality. Direct endpoint algebra verifies the equal-composition locus, and a large fast-rate family approaches but never reaches the sharp amplification factor \(m=\lambda_2/\lambda_1\). A two-class monotone-ratio argument proves minimality. The standalone standard-library checker passes 19,007 numerical/algebraic assertions, which are corroboration and not a substitute for the proof.

## Originality — PASS on inspected material

Ledger et al. (2024, https://doi.org/10.1002/edn3.70030) consider experimentally calibrated compositional metabarcoding mixtures and PCR bias, not capture curves parameterized by deployment duration. Courtaillac et al. (2024, https://doi.org/10.1002/edn3.70023) compare eDNA sampling and pooling practices, not relative-share maxima under three exponential saturations. Gloor et al. (2017, https://doi.org/10.3389/fmicb.2017.02224) establish the general compositional-data warning rather than this sharp theorem. The indexed near neighbors on abundance/sampling variance, transient birth–death dynamics and delayed Bateman inputs concern different observables, stochastic models and quantifiers. No inspected result implies the unique three-rate criterion, equal-endpoint amplification bound or two-class minimality. This is a bounded evidence assessment, not a claim that the entire literature has been exhausted. Theoretical passive-sampler preprint material and a later experimental paper could not be fully inspected; these remain historical-priority risks.

## Value — PASS

Sequencing records relative marker fractions, but laboratory intake is an absolute accumulation process. The theorem identifies a rigorously bounded, potentially arbitrarily large change in the intermediate marker's apparent share even when its physical amount rises continuously and both endpoint compositions match. It provides a mathematical explanation for a timing-related interpretation risk, a precise condition to test in simple calibration systems, and a sharp minimal class-count boundary. It neither promises clinical/ecological field calibration nor claims that all eDNA uptake follows this idealization.

## Scientific scope and risks

The claim excludes variable read depth, substrate competition, loss/degradation, time-varying ambient supply and cross-taxon detection bias not absorbed into fixed coefficients. The zero-time shares are positive-time limits conditional on an ideal read-depth experiment; they are not claims of actual sequence recovery at zero duration. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
