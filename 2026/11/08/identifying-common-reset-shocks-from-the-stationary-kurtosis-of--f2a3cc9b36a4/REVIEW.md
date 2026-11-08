# Scientific assessment: common-clock identification in diffusing diffusivity

## Correctness — PASS

For nonnegative independent position-only, diffusivity-only and common Poisson intensities, with positive marginal intensities \(R,Q\) and independent Brownian drivers, the invariant two-variable Markov process exists and has finite fourth moments. Applied to five monomials, its explicit generator yields the exact triangular moment recurrences, including the **single** loss of the mixed moment under each common reset. Solving gives \(K=6(6R+Q)/(R+Q-c)\). An independently derived Gaussian-mixture/Poisson-survival integral reproduces the fourth moment; \(\partial K/\partial c>0\) proves strict order, sharp endpoints and inverse identification. The separate `checker.py` replayed exact symbolic identities and 680 independent integral and rational checks. Numerical checks supplement, but do not prove, the universal claim. Boundary cases \(r_x=0\), \(r_\omega=0\), \(c=0\), and the fully synchronized case are covered.

## Originality — PASS, qualified

Santra, Basu and Sabhapandit (arXiv:2205.00549, public 2022-05-01) give the same Brownian stochastic-diffusivity dynamics with a **single joint-reset clock**, and explicitly suggest separately resetting position or diffusivity in their conclusion. Their special synchronized model determines the \(c=R=Q\) endpoint but does not supply the three-clock coupling interpolation with \(R,Q\) held fixed, the \(21\)-to-\(42\) equal-rate contrast, or the exact inverse feasible range. The 2018/2019 Kuśmierz–Gudowska-Nowak continuous-time-random-walk study investigates complete versus partial resets in a different anomalous-diffusion mechanism and does not imply the Brownian-squared-volatility stationary mixed moment. Relevant open research-record searches returned distinct objects: Jacobi radial dynamics, Brownian covariance modeling, and fourth-order interactions without a three-Poisson-clock theorem. Their statements do not imply the result. The 2023 Olsen general moment construction resets all dynamical memory and therefore does not subsume the state-selective clock result. The 2024 Zhan–Wang ergodicity article was available only at abstract level, so a broad unindexed correlated-reset theorem remains a priority risk; absence of matching search records is not proof of novelty.

## Mathematical value — PASS

The motivating 2022 paper explicitly leaves the nonjoint reset protocols for future investigation. Determining whether two protocols with **identical** reset rates for each observable but **different common shocks** can be distinguished is a natural identifiability problem, not an arbitrarily sliced invariant. The exact sharp kurtosis interval and invertibility answer that question for the smallest nontrivial moment order in this model; for equal marginal intensities, all stationary second-order two-time covariances are unchanged but fourth moments differ by a factor of two. It gives an exact model-specific feasible-data criterion for distinguishing clock synchronization. No finite-sample performance or universal inference is claimed.

## Limits and priority risks

All conclusions are restricted to stationary sampling, independent Brownian noises, independent Poisson clocks, strictly positive total marginal rates and known \(\Lambda\) for parameter reconstruction. A broader uncatalogued result on correlated resetting may overlap; a plausible general diffusivity paper was not read in full. Independent assessment is still needed before any publication-priority assertion.

Self-review: passed. Independent audit: not yet performed.
