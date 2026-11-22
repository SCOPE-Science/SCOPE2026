# Self-review

## Correctness

PASS. In a balanced three-parameter harmonic regression, integration multiplies each quadrature by the exact sinc factor and leaves the columns orthogonal; the Fisher information rate reduces to a single variable. The proof identifies a unique first-lobe stationary point, excludes later lobes by a strict global bound, and handles zero overhead and asymptotic boundaries. The asymptotic prefactors and dimensions were separately reconstructed and numerically checked. The checker supplements rather than substitutes for the proof.

## Originality

PASS, provisionally. Watson–Dhillon (2001) establish velocity-smearing motivation; Price–Rogers (2014) already link finite integrations, photon noise and readout time to information; Morello et al. (2022) already give the exact sinusoidal sinc attenuation. The proposed result is not any of those ingredients, but the all-duration unique optimum with its monotone root, exact ceiling, and cube-root overhead law. Searches and mathematical comparisons did not identify that full theorem, although its elementary source ingredients make historical priority uncertain. An unindexed equivalent or a one-line reduction from a broader general optimization theorem remains possible.

## Value

PASS within the idealized scope. The result supplies a closed scalar rule for selecting exposure length and a universal maximum fraction of an orbital period, while the fractional-power law quantifies the cost of small nonzero instrument overhead. These concrete benchmarks are relevant to phase-curve survey design, for which cadence, smearing and overhead are coupled. Unlike merely calculating a sinc attenuation, the result optimizes a specified information-per-charged-time objective over all positive exposures and explicitly excludes alias lobes. It is not an empirical scheduling prescription.

## Limitations and closest prior work

The model assumes a single known frequency, phase-balanced opportunities, independent Gaussian shot noise and known overhead, excluding calendar waiting, read noise and real instrument constraints. Morello et al. (2022), Price and Rogers (2014), Watson and Dhillon (2001), and Kipping (2010) are the principal related literature. Existing generic optimization theory may cover the scalar root under a change of variables; that residual historical uncertainty is not removed by unsuccessful searches.

Self-review: passed. Independent audit: not yet performed.
