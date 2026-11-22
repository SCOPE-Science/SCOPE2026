# Scientific assessment: finite-time freezing under conditional Gaussian shocks

## Correctness — PASS

The assessed mathematical statement is one linked theorem: almost-sure finite-time absorption of every finite population in the microscopic unprojected utility-weighted bounded-confidence chain, a uniform geometric tail and complete stationary-law description, together with an exact two-agent half-compromise lifetime. The original interaction equations directly give a movement of less than twice the confidence radius for each selected agent before noise. At any nonabsorbing configuration, the other \(N-2\) agents block at most \(N-2\) of \(N\) widely separated target locations. Two independently Gaussian shocks have a state-uniform positive chance of placing both selected agents into the two remaining target neighborhoods. The relocation preserves all previously isolated agents and isolates two more. At most \(\lfloor N/2\rfloor\) consecutive favorable selections therefore produce an absorbing configuration, and the Markov property gives the stated geometric tail and finite mean. Invariance then forces all stationary mass onto the absorbing configurations. For two agents at half-compromise, the exact disagreement identity cancels both utilities and the previous gap, leaving an independent Gaussian difference at each receptive attempt. The geometric law, complementary-error-function probability, and standard large-argument asymptotic follow exactly. Proof boundaries and strict versus nonstrict confidence inequalities were checked.

The standalone exact-rational and numerical sanity checker passed 3,611 checks in a first execution. It validates finite algebra and sampling geometry; it is not substituted for the all-state analytical argument.

## Originality — PASS, subject to literature coverage

The initiating 2026 paper explicitly conditions its Gibbs-like mean-field stationarity calculation on the persistence of a single opinion cluster. Its displayed microscopic rule makes rejected pairs inert but does not, in the examined main text and supplementary derivations, give an all-initial-condition absorption theorem, stationary-law classification, or two-agent exact Gaussian lifetime. A published finite-population analysis of the same model develops a weak-noise diffusion approximation and explicitly does not claim an exact microscopic invariant law. A distinct published noisy compromise result assumes a permanently interacting population. A published noiseless utility-weighted two-person calculation addresses asymmetric consensus overshoot without Gaussian innovations. The 2024 noisy bounded-confidence study uses bounded opinions and several alternative noise placements; the 2023 stochastic bounded-confidence paper treats a different interaction/noise structure. None of these inspected statements implies the claimed universal finite-population conditional-Gaussian absorption bound.

Residual risk: the general finite-state reachability/minorization method is standard, and an unindexed theorem covering all conditional-Gaussian bounded-confidence models might subsume this application. No claim of literature-exhaustive uniqueness or independent novelty certification is made.

## Mathematical value — PASS

The distinction between a conditional single-cluster Gibbs approximation and the exact finite-population, unprojected, infinite-time process is substantive. Rare Gaussian shocks eventually destroy every receptive edge, despite extremely long near-stationary observation windows. The theorem states this qualitative distinction with explicit uniform finite-time probabilities, an exhaustive invariant-law description, and a sharp exponential lifetime in the minimal test case. It identifies a model-design boundary: noise applied only upon receptive interactions can produce permanent fragmentation, whereas noise applied to all agents even after rejected encounters can remove these absorbing states. The result has direct theoretical value for interpreting stationary-looking simulations and choosing a microscopic stochastic convention; it does not purport to model empirical social behavior or to optimize general-population lifetime bounds.

## Relevant literature and limitations

- Siebenmorgen and Restrepo (2026), arXiv:2605.21844v1, exact interaction rule and conditional single-cluster diffusion approximation, https://arxiv.org/abs/2605.21844.
- Steiglechner and collaborators (2024), several distinct forms of noisy bounded confidence and bounded opinion values, https://doi.org/10.1098/rsos.231071.
- Shree, Chatterjee and Jagannathan (2023), finite-time results for alternative stochastic bounded-confidence interactions, https://doi.org/10.1109/TNSE.2023.3340255.
- Previously published finite-population Gibbs-exponent, non-Gaussian noisy-compromise, adaptive-confidence graph-stabilization, and noiseless utility-weighted pair analyses were compared by mathematical implication, not merely title. They do not have the same positive-noise conditional acceptance mechanism and theorem quantifiers.

A general-population mean-time **upper bound** is given; sharp many-person weak-noise asymptotics are not. The exact exponential lifetime is proved only for two agents at half-compromise. Opinions must be unprojected, Gaussian noise must have positive variance and be applied only after compatible contact, and the population size must remain finite.

Self-review: passed. Independent audit: not yet performed.
