# Independent mathematical audit

## correctness

PASS

Divide the scalar resolvent sum F_m(λ) by √λ; each term becomes (4/π)sech((8ℓ−log λ)/2). The infinite lattice sum is periodic in log λ with period 8. The angular Fourier transform of sech(u/2)/(2π) is sech(πω), by the beta integral with substitution t=e^u, so its periodization has exactly the stated Fourier coefficients. The positive and alternating series give R_+>1>R_->0. All phases and finite truncations are bounded above by C*=1+4/(e^(π²/4)−1)<√2. The resolvent equals the positive Neumann series for an inverse of (2m²+t)I−m²(S+Sᵀ); every pair is linked by a walk, so each resolvent has strictly positive entries. This makes the off-diagonal B_m entries negative. B_m annihilates constants, and its diagonal is bounded by F_m(4m²)≤2mC*<4m by spectral positivity and monotonicity of F_m. This proves strict stochasticity. The CFL uses the nodal diagonal 2m², not the maximal eigenvalue 4m²; F_m(2m²)/(4m)≤(√2/4)C*<1/2 agrees with the cited pure-diffusion restriction. The Nyquist eigenvalue is 4m², and the sinc truncation error there is O(m e^(−4m)); rounding the two mesh sequences preserves limiting phases 0 and 4. Thus m_j^+ gives 0.31588529… and m_j^− gives 0.65514027…, versus the target forward-Euler multiplier 1/2. The printed numerical pair follows the order R_−,R_+, not m_j^+,m_j^−; the displayed equations give the correct correspondence. Inspection of checker.py and a separate bounded calculation of the sums and j=1,…,6 support the constants, not the all-mesh proof. The result is not an inconsistency claim for fixed smooth data or for refined quadrature.

## originality

PASS

The resolvent scheme, sufficient maximum-principle restriction and general sinc accuracy estimates are prior work. The distinct assertion is the witness within that restriction: one fixed-spacing positive periodic discretization with explicit meshes converging to opposite Nyquist damping biases. The closest checked aliasing records analyze other operators or sampling mechanisms.

## value

PASS

This supplies a useful numerical benchmark with a clear distinction: a strict maximum principle and mass conservation can coexist with a mesh-persistent high-frequency accuracy defect of either sign. The standard periodic linear-element setting and explicit signed damping constants permit a direct test of a positivity-preserving discretization. It is not a claim against methods that refine their quadrature spacing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
