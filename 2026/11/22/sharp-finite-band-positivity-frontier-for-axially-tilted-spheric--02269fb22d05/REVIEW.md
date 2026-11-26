# Independent mathematical audit

## correctness

PASS

On the finite double compression, D^{-1/2} congruence reduces D+epsilon(MD+DM) to I plus epsilon times an azimuthal block matrix. Sphere probability normalization leaves the normalized latitude recurrence unchanged. The (ell,m) edge is a_(ell,m) times sqrt(d_ell/d_(ell+1))+sqrt(d_(ell+1)/d_ell), giving 2 a_(ell,m) cosh(t(ell+1)). Nonzonal blocks are bounded strictly below the zonal top eigenvalue by comparison with proper principal subpaths, including the one-vertex zero blocks. Perron simplicity and sign reversal on alternating vertices give top and bottom eigenvalues plus/minus Lambda_L, each simple; increasing L strictly raises Lambda_L by proper extension. The largest edge alone tends to infinity. For epsilon!=0 infinitely many edges with left endpoints 3j give disjoint negative directions (no interpair coupling); trace-class self-adjointness and min–max yield infinite negative index. Continuous quadrature of a smooth negative form gives a finite negative Gram witness, while an equator diagonal gives a positive form. Pointwise positivity for |epsilon|<1/2 does not contradict this. For q=e^(-t), the half-line operator is compact by norm truncation, with a positive simple extremizing eigenvector by the recurrence. A three-vertex top Rayleigh value sqrt(1+q^2) can be increased by extending towards vertex 3. The inequality 2|u_j u_(j+1)|<=|u_j|^2+|u_(j+1)|^2 gives the row-sum upper bound 1+q strictly at the positive top vector, since e.g. row 0 is smaller. Reverse the finite edges and normalize by w_(L-1): for j<=L/2 the angular ratio differs from 1 by O((j+1)L^-3), by differentiation of (1-1/(4k^2))^(-1/2); the cosh ratio is q^j times 1+O_t(e^(-tL)). All later and omitted edges are O(q^(L/2)). This gives O_t(L^-3) in uniform edge error and in operator norm (at most twice the sup edge error). The largest eigenvalue of the normalized matrix is rho(q)+O_t(L^-3). The reciprocal last edge is sqrt(1-1/(4L^2))/cosh(tL), giving 2e^(-tL) and relative coefficient -1/8. The result fixes t>0, and neither the proof nor numerical samples justify joint small-t scaling. The frozen checker was inspected, not executed. Independent reproduction python3 /workspace/independent_checks.py 4 computes latitude entries by associated-Legendre quadrature for t=0.1,0.45,1.1 and L=1,3,5, and separately compares scaled edge spectra at L=128,256,512: at t=0.15 the scaled correction tends from -0.127010 to -0.125494, and at t=1 from -0.125247 to -0.125061. These are finite floating-point corroborations; the norm proof supplies the error order.

## originality

PASS

The distinct quantitative result is the heat high-band spectral law: the geometrically weighted outer-edge limit, the prefactor in the heat cutoff, and the -1/8 relative correction with controlled remainder. General axial coefficient criteria and the common harmonic reduction are prior machinery. The exact finite threshold as an inverse Jacobi norm is structurally anticipated by that machinery (and by the earlier Poisson threshold); the qualitative full-heat obstruction is explicitly covered by the same-day half-order criterion, with no within-day priority inferred. These overlaps do not establish the heat-specific asymptotic.

## value

PASS

The double harmonic compression is a natural finite-band covariance check. The exact cutoff shows how an apparently admissible finite-band model can fail in the full kernel, and the sharp geometric prefactor and next term quantify the resolution at which this happens. Those terms separate the heat case from the qualitatively known obstruction and from the finite Poisson analogue, rather than only evaluating a few matrices numerically.

The dated certificate retains the supplied scientific assessment, sources and limitations.
