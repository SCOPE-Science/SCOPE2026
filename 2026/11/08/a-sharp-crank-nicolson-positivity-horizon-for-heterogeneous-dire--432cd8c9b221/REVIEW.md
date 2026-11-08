# Scientific review

## Correctness — PASS
For positive rates and any integer \(n\ge3\), exact cyclic resolvent summation reduces every diagonal of the Crank–Nicolson matrix to a rational function with positive denominator. Newton log-concavity for the elementary symmetric polynomials makes the polynomial numerator have at most one coefficient sign variation; a stationary-weight sign computation of its leading term and Descartes' rule prove existence, uniqueness, simplicity and no reentrance. Ordering of diagonals by exit rate identifies the sole active constraint, and monotonicity of the cycle product proves the sharp rate envelope. A standalone exact-rational matrix checker independently confirms the algebra on 1,020 matrices, 33,830 diagonal/stochastic identities and 1,020 threshold comparisons. Finite verification supplements the universal symbolic proof and is not presented as exhaustive proof.

## Originality — PASS, subject to specialist publication-priority risk
The closest published published-finding corpus result, *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026/10/4, identifier ending d475df91cd2a), was read in full. Its general Cayley identity and diagonal test already apply to **any** Markov generator and are not claimed as novel. Its single-crossing result instead assumes detailed balance and expressly says that the nonreversible case is not classified. Directed one-way cycles of length at least three are nonreversible and are not its corollaries. The present result adds a nonreversible universal one-crossing proof, rate-order invariance, exact elementary-symmetric threshold polynomial, and sharp rate-extremum characterization.

The full relevant sections of Horváth–Song–Terlaky (2014), Fallat–Tsatsomeros (2002), Hadjimichael–Ketcheson–Lóczi (2021) and Higueras–Roldán (2023) were inspected, including their stated rational-method, Cayley, upwind and tridiagonal scopes. They do not supply the new claim on arbitrary heterogeneous directed cycles. A specialized treatment under cyclic M-matrix, Markov resolvent, uniformization or implicit upwind terminology might still be prior coverage; this is the principal residual originality risk. No negative search result is treated as a proof of uniqueness.

## Mathematical value — PASS
The arbitrary-rate directed cycle is a natural finite-volume upwind transport generator and an irreducible nonreversible Markov model. Its sharp positivity step is not supplied by the global absolute-monotonicity radius or the general diagonal-resolvent test. The result gives a complete all-length characterization, a one-root algorithm despite an arbitrary number of rates, a non-obvious invariance under rate rearrangement, and the sharp best/worst horizon for fixed maximal rate. These give a useful, reproducible design and stability fact rather than an arbitrary numerical slice.

## Limitations
No result is asserted for general nonreversible networks, other rational integrators or nonlinear stage positivity. Numerical spot checks cannot establish the infinite-parameter theorem; those steps are supplied by the polynomial argument. Specialist coverage risk remains, and independent scholarly review has not occurred.

Self-review: passed. Independent audit: not yet performed.
