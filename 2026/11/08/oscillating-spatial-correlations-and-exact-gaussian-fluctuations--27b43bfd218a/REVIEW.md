# Scientific review: oscillating trimer-overlap correlations

## Correctness

PASS. The first-attempt representation follows because the earliest attempted trimer covering a site is necessarily accepted; subsequent attempts from a rejected center cannot change any occupancy. Thus each terminal multiplicity is a deterministic function of seven independent clocks, establishing the exact six-dependence. An exhaustive integer subset dynamic program proves the six pair probabilities and checks both one-site marginals. Distances one and two are additionally confirmed by independent brute-force enumeration of every complete arrival order. The finite covariance sum is positive and the independent-block Lindeberg argument proves the stated central limit theorem; finite enumeration is used only for finite coefficients.

## Originality

PASS, conditional on the inspected literature and accessible records. The nearest works are Krapivsky (2022/2023), arXiv:2209.03992, and Viot–Krapivsky (2024/2025), arXiv:2410.12373. The latter derives the already known single-site densities and selected close-neighborhood probabilities but identifies pair correlations as an interesting further problem in its discussion. It does not report the six-distance triple-occupancy covariance vector, its double sign reversal, or the exact macroscopic Gaussian variance. Searches of related mathematical research records and accessible prior claims did not show an equivalent result; absence from searched records is not a proof of global historical priority. General short-range CLTs alone also do not imply the exact variance constant.

## Value

PASS. Triple occupation is the rarest nonzero trimer saturation layer and its spatial clustering is not determined by its known one-point frequency. The exact positive/negative/positive correlation pattern quantifies short-distance clustering and medium-distance anticorrelation; its sharp cutoff and finite variance directly determine fluctuations of experimentally measurable saturation counts. The exact finite-size intercept and universal Gaussian normalization add information beyond the previous mean-density solution.

## Scope and risk

The model uses an infinite initially empty lattice, independent rate-one attempt clocks, fixed length-three trimers, and terminal multiplicity. The historical-priority comparison is limited to indexed material and inspected primary texts. Numerical diagnostics do not constitute independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.
