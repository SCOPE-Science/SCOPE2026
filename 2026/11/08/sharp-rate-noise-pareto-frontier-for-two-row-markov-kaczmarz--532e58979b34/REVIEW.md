# Scientific review

## Correctness — PASS
The independent-innovation assumptions, conditional stationary covariance recursion and two-state time-reversal equality yield unique tangent second moments. The joint stationary law exists by strict contraction at row switches; the finite-state irreducible chain switches infinitely often. The two-by-two positive transfer matrix yields the exact synchronous squared-error Perron factor. Under a fixed row frequency the switching intensity optimizes at its admissible maximum, and the resulting monotone one-variable spectral constraint gives the closed-form sharp risk frontier. Full parameter boundaries, equal-noise degeneracy, and periodic-row nonmixing are explicitly separated. The standard-library verifier checks 4,500 exact rational configurations and the sharp benchmark; analytic arguments prove the continuum.

## Originality — PASS (qualified)
Patel–Jahangoshahi–Maldonado (2019, arXiv:1904.11919) treat arbitrary dependent sampling of randomized linear solvers but do not state this stationary *fresh-noise* Markov risk frontier. Bergou et al. (2023, arXiv:2308.16904) analyze different noisy linear-system models, without the coupled two-row transition-probability minimax formula. Agaskar–Wang–Lu (2014) optimize IID Kaczmarz sampling under a noise-free exact-MSE model, so its results do not imply this fresh-heteroscedastic-noise Markov optimization. Relevant public research records concern noiseless cyclic overrelaxation or different stochastic algorithms, and the accessible prior ledger has an IID Gaussian Kaczmarz stationary-law characterization; none of the compared statements subsumes this Markov rate–noise result. Remaining risk: an older specialist Markov-switching projection or noisy Kaczmarz paper could already contain the same specialization; the full 2014 publisher PDF comparison was limited by retrieval throttling, and broad searching cannot prove uniqueness.

## Value — PASS
The theorem supplies the complete naturally parameterized convergence-versus-noise frontier for a canonical noisy row-action method: it distinguishes a design choice that changes convergence speed *without altering the asymptotic noise floor*, proves a unique optimal schedule when noise is heterogeneous, and quantifies the irreducible trade-off between speed and deliberately oversampling reliable measurements. This can calibrate row-scheduling heuristics and exact two-row testbeds, while not claiming generalized multirow or nonlinear transfer.

## Closest prior work and limitations
The sources and precise model distinctions are in RESULT.md. Scientific scope is two real dimensions, two nonorthogonal unit rows, fixed unrelaxed updates and independent fresh finite-variance measurement perturbations. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
