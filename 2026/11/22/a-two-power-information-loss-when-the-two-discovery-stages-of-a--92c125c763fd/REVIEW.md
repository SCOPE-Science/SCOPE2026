# Scientific assessment: two-stage coupon inference

## Correctness — PASS

The experiment is defined by two independent zero-based geometric waiting times with success probabilities \(\theta\) and \(\theta(m-1)/m\). The generating-function identity and first two moments give exact inversion. Holding the total mean fixed defines a legitimate pair of alternative nuisance rates. The full labeled stage likelihood is regular in the contrast \(\zeta=(2m-1)^{-1}\), but the total likelihood is even in \(\zeta\) and regular in \(\eta=\zeta^2\). Exact score calculations give Fisher information \(2/a\) for labeled stages and \(1/(3a^2)\) for totals, with \(a=1-1/h\). Adjacent sizes differ by order \(m^{-2}\) in \(\zeta\) and by order \(m^{-3}\) in \(\eta\). Exponential-tail bounds justify the local log-likelihood expansions and KL lower bounds; empirical-moment midpoint tests attain the corresponding Gaussian errors and prove the matching supercritical results. The standalone standard-library checker passed 6,029 exact-fraction identities, but finite checks are not proofs of limit laws.

## Originality — PASS, qualified

The Jan 2022 O'Neill preprint (arXiv:2201.03122; journal text https://doi.org/10.1007/s11009-022-09966-x) explicitly gives convolution-of-geometric waiting times and moments. The Sep 2022 O'Neill preprint (arXiv:2209.02220; journal text https://doi.org/10.1007/s11009-023-10053-y) gives the occupancy Markov-chain and recursion framework. In the accessible relevant full-text sections neither supplies this two-point nuisance-rate testing construction, stage-label information contrast, or critical error probabilities. A directly inspected later record, *A signed negative-binomial correction for heterogeneous geometric sums*, establishes a signed correction in total variation; it does not address estimation of coupon alphabet size, the two observation schemes, or their exact local testing constants. Classical likelihood asymptotics supply the mathematical tool, not the specific inverse-problem conclusion. Searches across title, underlying model, invariant, sample-rate exponents, and equivalent geometric-sum parametrizations found no directly covering theorem. This is a best-knowledge originality assessment, not a historical uniqueness certificate: general coupon-population inference or subtle implications of broad asymptotic information theory could still overlap.

## Value — PASS

Recovering an unknown number of possible types when individual coupon observations are suppressed is a natural inverse problem for the published negative-occupancy model. The total count remains identifiable, but a statistician paying for repeated experiments incurs a sharp transition from fourth- to sixth-power replication cost if stage labels are not recorded. The result gives exact efficient Gaussian critical errors, rather than only consistency or a variance comparison. The precise powers and constants inform which data recording protocol retains statistically usable information.

## Scope and limitations

The theory concerns the two-distinct-type stopping rule, independent replicated experiments, and a fixed compact-interior nuisance parameter family. The strong lower bound compares adjacent alphabet sizes on a particular equal-mean path; a known fixed success probability is a different experiment. Generalizations to larger occupancy targets and unknown time-varying survival probabilities are not proved. Historical priority and independent mathematical validation are outstanding.

Self-review: passed. Independent audit: not yet performed.
