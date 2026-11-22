# Scientific review: two-node periodic Fourier minimax quadrature

## Correctness — PASS

The theorem quantifies over every integer \(m\ge1\), every joint Borel law of individually Haar-uniform circle variables, and every real zero-mean Fourier polynomial supported on frequencies \(1,\ldots,m\). Normalized sine/cosine testing lower-bounds worst-direction cross-correlation by the largest cosine moment of the relative displacement. The nonnegative square of a geometric sum forces that largest moment to be at least \(-1/m\), and therefore forces risk at least \((m-1)/(2m)\). The exhibited independent random nonidentity root shift has all first \(m\) complex Fourier moments equal to \(-1/m\), which implies exactly isotropic risk and proves attainment. Equality in the kernel also forces any optimal pair's difference onto the nonidentity roots; positive Fejér weights force every cosine moment to equal \(-1/m\). The two-frequency double-angle argument proves the claimed constant-offset rigidity. Every use of positivity and every endpoint is covered, including \(m=1\).

A standalone finite checker passed 2,341 supplementary checks, including periodic phase integration, exact triangular sums and Fourier cancellation. It is a stress test rather than a certificate for unrestricted couplings.

## Originality — PASS, subject to historical-priority qualification

Kritzer–Kuo–Nuyens–Ullrich (2017) study random-number-of-nodes rank-one lattice algorithms and smoothness-space rates; Dick–Goda–Suzuki (2021) study component-by-component randomized rank-one lattice construction, and Casarin–Craiu–Frattarolo–Robert (2021) develop general antithetic-dependence constructions and application comparisons. Their inspected abstract, introduction, theorem statements and relevant sampling sections do not state the equal-marginal, exactly-two-observation, all-coupling finite-Fourier minimax constant and its displacement-support necessity. Their broader frameworks do not alone imply the exact \((m-1)/(2m)\) result without a frequency-specific Fejér/duality argument. Searches for equivalent root-of-unity and antithetic spectral formulations did not locate a directly dominating statement; absence of a search result is not proof of novelty.

Residual risk: both the Fejér kernel and classical cyclic sampling are established mathematics. A general harmonic moment or group-based antithetic minimax result could cover this as a corollary even without matching terminology. No independence or peer validation is claimed.

## Mathematical value — PASS

Two uniform marginal sampling sites with free dependence form a natural exact-design question. The solution is a complete, bandwidth-uniform minimax value over all joint laws, not merely a better example than iid sampling. Its attaining construction makes all \(2m\) target directions equally difficult and the equality argument forces every optimal relative shift into a finite algebraic support. The sharp fact that a single constant shift ceases to be optimal at bandwidth three distinguishes ordinary shifted lattices from randomized mixtures at fixed evaluation budget. The fractional variance saving \(1/m\) is substantive for small bandwidth and becomes small as \(m\) grows; no broad speedup claim is made.

## Closest literature and scope

- Kritzer, Kuo, Nuyens, Ullrich (2017), https://arxiv.org/abs/1706.04502 : randomized lattice convergence rates with a random number of nodes, not fixed-budget copula minimax.
- Dick, Goda, Suzuki (2021), https://arxiv.org/abs/2109.11694 : rank-one lattice construction and smoothness-space worst-case/rms rates, not two-node arbitrary-coupling exact value.
- Casarin, Craiu, Frattarolo, Robert (2021), https://arxiv.org/abs/2110.15124 : general antithetic designs, dependence order, simulations, and integration applications; no inspected exact bandlimited minimax theorem.
- Roach and Wright (1977), https://doi.org/10.1080/00949657708810144 : general antithetic sampling-plan optimization framed as a transportation assignment for a given model; only its abstract and bibliographic record were accessible, so overlap with a broad equivalent formulation remains a priority risk.

Limitations include equal weights, exact uniform marginals, no observation noise, and no guarantee outside the designated bandwidth. The historical-priority caveat remains material.

Self-review: passed. Independent audit: not yet performed.
