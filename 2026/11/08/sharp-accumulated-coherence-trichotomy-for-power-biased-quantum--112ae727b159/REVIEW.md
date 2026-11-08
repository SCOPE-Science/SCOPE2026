# Scientific review: accumulated coherence under power-biased history resetting

## Correctness — PASS

The ensemble-history integral equation uniquely reduces each Hamiltonian spectral block to a Kummer equation. For each nonzero Bohr gap, the real parts of both Euler-integral beta parameters are strictly positive, so the integral representation and endpoint asymptotics are legitimate. The slowest active gap controls the unique smallest decay exponent; all other finitely many modes are lower-order. At criticality the slowest modes integrate into a rotating complex power of unit magnitude and all remaining contributions have a convergent residual; strict triangularity gives a nonzero Hilbert–Schmidt circle. Above criticality all active modes are absolutely integrable, and an explicitly convergent beta integral yields the rational response and its negative real part. The separate finite-dimensional `verify.py` completed 151 bounded deterministic checks. Those checks are corroboration, not a substitute for steps 1–5 of the mathematical proof. Scope includes spectral degeneracies but excludes continuous spectra and state-dependent reset kernels.

## Originality — PASS, with identified residual risks

The August 3, 2026 quantum-history study [1] develops **uniform** past-time sampling and log-periodic algebraic relaxation; its text states the nonuniform quantum kernel is left open. The 2024/2025 classical preferential-relocation study [2] **already gives the exact Kummer scalar equation for power-history sampling and arbitrary positive real relaxation eigenvalue** in its Section 5.1, equations (44)–(50). The scalar Kummer equation and a straightforward complex-frequency substitution are therefore not claimed as new. The present claim instead classifies the **finite-dimensional Hermitian accumulated quantum coherence operator** over all power kernels, including an initial-state-dependent sharp threshold, exact nondegenerate critical circle, absolute-integrability dichotomy and a signed rational operator sum rule. These are not supplied by the inspected classical real-spectrum conclusions or the inspected uniform-kernel quantum theorem. The earlier real-spectrum formula is a clear derivational predecessor and limits the originality claim. A more general, unidentified complex-mode or quantum-susceptibility theorem could still subsume the present conclusion. Matching titles or unsuccessful searches alone do not certify originality.

The relevant source comparison used the actual accessible full arXiv text of [1] and [2], the main general-history analysis of [3], and contextual information from [4]. Semantic research-record queries included the exact paper identifier, the power-biased history kernel, logarithmic circle behavior, and integrated coherence. No equivalent claim was identified among the inspected closest records; search incompleteness remains a limitation.

## Value — PASS

Time-integrated deviation \(\int_0^T(\rho(t)-\rho_\infty)dt\) is the natural finite-time accumulated response to linear quantum observables, rather than an arbitrary statistic or a reparameterization of pointwise relaxation. The threshold is controlled by the smallest **initially excited** Bohr gap and distinguishes three experimentally and mathematically different response regimes: divergent magnitude, bounded nonconvergence on an explicit circle, and a finite response. The finite-response branch has an unexpected universal negative coherence self-overlap, giving additional information not supplied by the algebraic decay exponent alone. This is a complete, motivated classification for a natural nonuniform-history family; no claim of large-device feasibility or downstream theorem is needed.

## Closest literature, methods and limits

[1] G. de Mauro, M. Kulkarni, S. N. Majumdar, *Quantum resetting with memory*, arXiv:2608.02297 (2026-08-03), https://arxiv.org/abs/2608.02297 — finite-dimensional quantum master equation for uniform history, and a stated nonuniform-kernel direction.

[2] D. Boyer, M. R. Evans, S. N. Majumdar, *Diffusion with preferential relocation in a confining potential*, arXiv:2411.00641 (2024-11-01), https://arxiv.org/html/2411.00641 — classical power-history Kummer solution, Section 5.1.

[3] D. Boyer, M. R. Evans, S. N. Majumdar, *Long time scaling behaviour for diffusion with resetting and memory*, arXiv:1611.06743, https://arxiv.org/abs/1611.06743 — nonuniform classical memory and real diffusive mode exponents.

[4] F. Carollo, S. Wald, *Stochastic resetting induces quantum non-Markovianity*, arXiv:2601.13367, https://arxiv.org/abs/2601.13367 — discrete-time stochastic quantum resetting; only its accessible abstract and context were relied upon, not a whole-document absence claim.

The proof does not cover infinite-dimensional, gapless, time-dependent-Hamiltonian or feedback-controlled systems. It is a mathematical consequence of the stated ensemble-history law; no laboratory realization or independent priority certification is asserted.

Self-review: passed. Independent audit: not yet performed.
