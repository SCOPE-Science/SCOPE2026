# Self-review

## Correctness — PASS

For the flat-rank input, the first nonstopping Gaussian sketch has full column rank almost surely and spans the exact range. The second lookahead is therefore zero, but its Gaussian coefficients are independent row energies with exact chi-square laws. The pruning rule drops at least one row precisely when their minimum falls below the tolerance, and each omission incurs unit squared Frobenius projection error. Conditioning on the first nonstopping branch yields the exact product of chi-square probabilities. Stirling's formula and a controlled endpoint Laplace estimate establish the sharp square-root-logarithmic threshold and the centered Gumbel window. Numerical reconstruction and simulations corroborate the identities; they are not substitutes for the proof.

## Originality — PASS, with priority uncertainty

Smith--Do--Chen (arXiv:2607.06758v1, Sections 3.2--3.3) supply the Gaussian row-energy proxy, its unbiasedness and individual variance; they do not state an exact collective-minimum under-pruning failure probability or the sharp block-size phase. Yu--Gu--Li (arXiv:1606.09402) use explicit coefficient energies; Pearce--Chen--Dong--Martinsson (arXiv:2310.09417) analyze LU-based adaptive interpolation; Gorman et al. (arXiv:1810.04125) derive tail bounds for projected Frobenius stopping indicators. Those statements do not imply this event and window without analyzing Algorithm 4's pruning. Earlier unpivoted QB over-retention with exact rows is a different phenomenon: it does not assert this adjoint-free under-retention or its all-block-size law. Standard chi-square extreme-value theory is not claimed as a new probability theorem. Other unseen or older specializations remain a historical-priority risk.

## Mathematical value — PASS

The work exposes a concrete calibration limitation in an advertised fixed-tolerance numerical procedure. Individual row estimators become more accurate with block size, yet a growing number of minimum-based pruning decisions can make the true tolerance fail with probability tending to one inside a sharp near-threshold window. The exact finite-block law permits quantitative risk budgeting. This is not a claim of typical performance on all spectral shapes.

## Restrictions and independent validation

The full distribution conditions on reaching the defined second-lookahead branch. The first-stop event is explicitly accounted for in the unconditional joint-event probability, but the behavior of a procedure invoked before a basis exists is not assigned. All statements assume exact arithmetic and independent real Gaussian blocks. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
