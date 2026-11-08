# Scientific review of the opposing-tail covariance transition

## Correctness

**PASS.** The stationary common Poisson clock gives an exponential age, and conditioning turns the particle classification into an exact three-cell multinomial. The pair covariance and the exact finite-population sign condition follow directly. A uniform small-level error-function expansion isolates a logarithmically divergent truncated negative-first age moment and fixes its coefficient. A radial Bessel-kernel integral and dominated corner asymptotics fix the large-level prefactor. The mesoscopic limit then follows algebraically. The code checks 42 numerical identities and representative inequalities from two independent integral representations. The exact proof, not numerical extrapolation, supports the limits. Boundaries \(N\ge2\), \(b>0\), stationary regime, and no asserted uniqueness of distance crossing are explicit.

## Originality

**PASS, with priority risk.** The 2022 Brownian-gas paper gives the exact underlying joint density and a single-interval full counting distribution (main Eq. (4), supplementary Section IV). The 2023 conditional-i.i.d. paper generalizes that mixture mechanism, and its own application section treats positions, sums, and order statistics. Neither inspected statement classifies the sign of opposing-tail count covariance, the nonanalytic small-distance population threshold, or the universal critical \(N\log N\) window. This is a further, nontrivial asymptotic extraction from known distributions, not a new stationary joint distribution. A published complete joint-density formula logically permits the calculation, so independent literature checking is essential before any claim of publication priority. No exact equivalent was found among the retrieved named sources or relevant semantic-search results.

## Mathematical value

**PASS.** Opposite tails are disjoint for each particle and therefore compete negatively at fixed reset age, while the common reset clock positively couples their total occupancies. Their exact balance identifies when collective fluctuations overwhelm exclusion. The critical physical distance is anomalously of order \(1/\sqrt{N\log N}\), and the universal constant \(\pi\) and a full limiting covariance emerge, rather than a chosen numerical example. These predictions distinguish shared-clock correlated gases from independent-clock gases and are suitable for finite-population observations.

## Sources, scope, and risks

Primary source arXiv:2211.00563, original public posting 2022-11-01: main Eq. (4), supplementary FCS Eqs. (45)-(48). Broader framework arXiv:2307.15351: introductory conditional-i.i.d. structure, Section IV.A stationary gas, and conclusions. Different first-passage observable arXiv:2303.18012. The main residual scientific risk is an unidentified equivalent two-region covariance asymptotic in related exchangeable-mixture, resetting-gas, or spatial-count literature. The model assumes a stationary shared Poisson clock and identical Brownian diffusivities; no proof of uniqueness in the distance variable is claimed.

Self-review: passed. Independent audit: not yet performed.
