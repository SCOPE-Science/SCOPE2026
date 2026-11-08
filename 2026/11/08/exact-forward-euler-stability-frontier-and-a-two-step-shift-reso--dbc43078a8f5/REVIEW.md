# Scientific review

## Correctness — PASS
The discrete FSBP operator satisfies the exact two-point interpolation equations and the diagonal SBP identity. Applying standard upwind numerical flux produces a block-circulant amplification symbol with an explicitly computed quadratic characteristic polynomial. The degree-two Schur criterion reduces all-phase stability to two algebraic inequalities; both necessary boundary/small-frequency obstructions are reconstructed, not inferred from simulation. The optimal parameter and the exceptional two-step shift follow by exact hyperbolic identities and Cayley--Hamilton. An independently assembled full-ring matrix was compared against Fourier diagonalization, and an executable checker reproduces the algebra and exact shift within floating-point tolerances. No inference from finite tests to infinite phase coverage is used.

## Originality — PASS, historically qualified
The closest primary source, arXiv:2610.30272v1, proves conservation, entropy properties and accuracy for FSBP flux differencing; its Section 5 specifies high-order, SSP and relaxation Runge--Kutta integrators without a two-node exponential forward-Euler sharp all-wavenumber classification. The original FSBP source arXiv:2203.05479v2 develops the general operator theory and uses SSPRK(3,3) for advection, without the claimed Fourier frontier or two-step shift. Older polynomial DGSEM dispersion results cover the limiting spatial framework rather than this exponential parameter and resonance. published-finding corpus and published-literature statement/alias searches did not expose a covering claim. Residual priority risk: a broader pre-existing exponential-fitting DG stability treatment not indexed or not inspected in full may entail the identity.

## Value — PASS
A stable semidiscrete method need not be stable under forward Euler; for the natural exponential fitting family, the exact admissible step displays a sharp switch between long-wave and fast-mode obstructions. The polynomial limit has no positive *grid-uniform* Euler CFL, an exponential fit creates one, and at the unique maximal step the otherwise dissipative method becomes an exact undamped two-step lattice shift. This is a structural, parameter-complete stability classification for an expressly proposed nonpolynomial discretization family, with a directly operational time-step threshold and a caution against equating modal stability with physical accuracy.

## Scientific limitations and remaining risks
Only scalar periodic constant-speed transport, two endpoint degrees per cell, fixed common shape parameter, a standard upwind interface, and modal stability of forward Euler are established. The result is not a full high-order FSBP time-step theorem, a monotonicity guarantee, or a claim that the resonant time step is accurate. Historical completeness and independent proof checking remain open.

Self-review: passed. Independent audit: not yet performed.
