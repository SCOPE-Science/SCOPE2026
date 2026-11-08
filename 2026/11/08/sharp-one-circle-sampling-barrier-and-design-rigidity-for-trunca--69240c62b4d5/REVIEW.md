# Self-review

## Correctness — PASS

The coefficient Gram matrix has fixed diagonal \(e^{-x}x^k/k!\), independently of angles or positive weights. Rayleigh bounds give the universal lower bound on spectral conditioning. The strictly decreasing, then increasing two-piece expression for the ratio of the maximum and minimum of this log-concave sequence yields the unique radius; equality in Rayleigh pins the constant basis vector as an eigenvector and forces *every* angular moment to vanish. Those moments are also sufficient, and the square case follows from unitarity of the weighted Fourier matrix and Newton identities. Stirling's expansion gives the claimed exponential factor and polynomial prefactor. Edge cases \(n=2\), arbitrary \(m\ge n\), repeated angles, and positivity/normalization of weights were checked. Numerical tests are corroborative only, not proofs.

## Originality — PASS, provisional

The closest *same-object* precedent is Calixto–Guerrero–Sánchez-Monreal (2011), §3, which already provides both the coherent-state sampling model and the exact diagonal spectrum **for regular/equidistant angular points at arbitrary radius**. These are explicitly prior work. In the regular design, the radial minimax follows from their eigenvalues with a separate scalar argument; it is not independently claimed as a fundamentally new spectral fact. The final claim instead proves *global optimality among every positive weighted angular configuration, every observation count, and every common radius*, characterizes equality by circular Fourier designs, forces regular equal-weight geometry at critical sampling, and proves the sharp exponential barrier for arbitrarily large oversampling. No inspected primary source or retrieved mathematical record states this whole comparison or a stronger theorem that implies all of these conclusions. Kuian–Reichel–Shiyanovskii (2019), Theorem 10, gives equidistant-node scaling for fixed polynomial bases; Abreu et al. (2022), §5, treats a distinct quasi-periodic Gaussian frame setting. The argument substantially uses classical Fourier design rigidity and is priority-sensitive; an equivalent classical optimal-design theorem may exist under different terminology.

## Mathematical value — PASS

The jointly optimized sampling problem is a natural benchmark for Gaussian coherent-state tomography and finite Fock reconstruction: one circle is often chosen for phase-only acquisition, while both number of samples and sampling weights can be varied. It is mathematically substantive to prove that *no such extra acquisition effort improves spectral conditioning*, and to determine the exact optimal radius and **every** optimally weighted angular geometry, with a precise exponential rate and prefactor. Unlike a fixed-radius diagonalization, the theorem supplies a global impossibility barrier across arbitrarily many and nonuniform observations. It does not address multishell designs, noise models with fixed absolute precision, or adaptive measurements.

## Closest literature and remaining risk

Calixto et al., arXiv:1109.2171 (2011), is an especially strong precedent and is the source of the known equal-angle spectrum; Kuian et al., DOI 10.1137/19M1237272 (2019), contains related unit-circle Vandermonde norm structure. These are not represented as absent. An undiscovered general weighted circular quadrature optimality statement could subsume the result, and the scalar radius optimization is a short consequence once the spectrum is known. The complete *all-design* optimization, rather than that scalar subcase, is the reviewed claim. An independent mathematical audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
