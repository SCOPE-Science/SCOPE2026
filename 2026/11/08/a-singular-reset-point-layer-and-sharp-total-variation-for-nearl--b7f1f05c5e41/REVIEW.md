# Self-review

## Correctness — PASS
The distributional second derivative of a Laplace density is \(p_0''=\lambda^2p_0-\lambda^2\delta_0\), with total-variation norm \(2\lambda^2\). This produces the sharp global \(L^1\) upper bound after averaging centered independent residual displacements, while tail events outside a fixed positive radius yield the matching lower limit. The stationary perpetuity, locally uniform inner and outer profiles, bounded smooth-test signed limit, and unique logarithmic-scale density crossing are derived analytically in `RESULT.md`. All quantifiers and limits are parameter-appropriate. The executable finite checker independently exercises the main formulas but does not substitute for the infinite-dimensional proof.

## Originality — PASS, with qualified priority
Pierce (2022), Di Bello et al. (2023), and Biroli et al. (2024) already derive stationary proportional-reset laws, their characteristic products, and in Biroli et al. the fixed-contraction peak shape. They are foundational prior coverage and are not claimed as new. Pierce gives a qualitative strong-reset exponential limit and an \(O(c)\) approximation, not the sharp stationary \(c^2\) total-variation asymptotic. Biroli et al.'s small-rescaling Appendix A treats first-passage time. The asserted extension is a singular parameter-layer theorem, a unique logarithmic-scale sign crossing, and their matched global TV coefficient. Kolb and Wübker (2026) study convergence to stationarity *in time*, not stationary-law variation with the multiplier. Existing exact formulas do imply these limits after analysis, and possible earlier derived expansions remain a concrete residual priority risk.

## Mathematical value — PASS
The result identifies how a physically incomplete reset approaches a complete reset in the stringent probability-metric sense, not merely pointwise in a plotted density. The singular central mass redistribution and its exact sharp coefficient matter when comparing nearly complete resetting protocols from spatial observations. The unique optimal distinction region and its logarithmic crossing scale, together with the layer and signed-mass structure, explain why a fixed-position expansion misses the most informative boundary region.

## Reproducibility and limits
The bundled `verify.py` executes standard-library diagnostics on exact finite convolutions. The claims are confined to drift-free one-dimensional Brownian motion with Poisson proportional resets, keeping diffusivity and reset rate fixed as the multiplier tends to zero. There is no claim of independence, certification, time-relaxation results, or a new fixed-parameter stationary density.

Self-review: passed. Independent audit: not yet performed.
