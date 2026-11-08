# Scientific review

## Correctness: PASS

The Markov-chain state space and rates are given explicitly. The strictly positive rates ensure irreducibility, and the spin-reversal involution enforces mean \(N/2\). Applying the generator to \((i-N/2)^2\) yields an exact affine, environment-conditioned second-moment closure. The two-state linear system is invertible for every parameter in scope. Its solution, subtraction of the fast-switching value, factorization and first two derivatives all have explicit signs. The formula is also checked against exact stationary solutions for independently constructed finite generators by `verify.py` (84 rational equalities or inequalities). Those checks are a supplement, not a proof for all \(N\).

## Originality: PASS, with qualified priority

A full-text examination of Caligiuri–Galla, arXiv:2305.19096v2, including Sections II, III, IV, V and appendices, finds the precise model rates in Eq. (22), limits at slow and fast switching, and intermediate-switching simulations, but no exact finite-size one-pole variance or universal strict-speed monotonicity theorem. The source assumes symmetric environmental switching in its analysis; the present result includes arbitrary positive relative rates. Hufton et al. (arXiv:1512.00785v2) concerns PDMP/LNA for other population models, and the work of Herrerías-Azcué–Galla (arXiv:1903.09198) and Carro–Toral–San Miguel (doi:10.1038/srep24775) concerns non-modulated voter models. This precise joint implication was not identified in searches of the inspected literature or available scientific records. Exact moment closure is classical, so a previously published equivalent or straightforward unpublished calculation is a remaining priority risk.

## Value: PASS

The motivating paper finds coexisting bimodal, trimodal and unimodal regimes and uses simulation to bridge slow and fast environment limits. It is therefore meaningful to ask whether speeding up the environment *necessarily* reduces a well-defined polarization observable at finite population size. The exact, all-parameter answer provides a strict monotonicity theorem, the unique crossover scale, a quantified excess disagreement at each intermediate switching rate, and a sampling interpretation. This is not claimed to solve the full stationary distribution. The result is a reusable finite-size benchmark for Markov-modulated social contagion and stochastic population models.

## Closest work, scope and residual uncertainties

The initiating source covers the model and endpoint distributions but not the finite-speed variance result as stated. The 2015–2016 PDMP/LNA and 2016/2019 noisy-voter studies provide methodological context or results for different models. Remaining risks are unindexed literature, alternate terminology such as telegraph-modulated or random-environment Kirman models, and potential republication of an equivalent special-case identity. No independent audit was commissioned or performed.

Self-review: passed. Independent audit: not yet performed.
