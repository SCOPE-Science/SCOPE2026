# Independent mathematical audit

## correctness

PASS

The model is independent Poisson resetting for identical starts, not a shared clock. Conditioning on reset times gives the convolution series and response H=q*q-uq; in Laplace space q transforms to (1-exp(-sqrt(s)))/s, so the integrated erfc transforms give the stated elementary H. The convolution bound sums to u^(-1/2) exp(-rho u) F(rho sqrt(u)), where F(z)=1/sqrt(pi)+z exp(z^2)(1+erf(z)); differentiating gives uniform q_rho=O(u^-1/2) and partial_rho q_rho=O(1+sqrt(u)) on the tail for 0<=rho<=1/2. The order-statistic derivative is integrably dominated by u^(-(N-k-1)/2) when N-k>3. The dimensional derivative acquires d^4/D^2. The binomial derivative and the Jacobian -q'=a give exactly Beta(N-k+1,k); G behaves as -2/(pi^2 x^4) at zero and is bounded near one (0<H<=u(1-q) for small u). H''/a is first positive, then negative, then positive because y-3/2+2 exp(-3y) has precisely two positive roots. Since H' starts at zero, is negative at large u and tends to zero from below, it crosses exactly once from positive to negative. H therefore crosses zero once, with strictly negative slope, since H(0+)=0 and H tends to minus infinity. The density ratios for lowering k or increasing N increase strictly in x; subtracting their value at the crossing makes their product with the signed G strictly positive in the comparison integral. This proves sign ordering, not monotonic magnitudes. For k=N phi_*+c at bounded c, beta mean drift and variance give the two terms of order N^-1; a signed third moment of order N^-2 and fourth moment of order N^-2 bound the Taylor remainder. Endpoint tails are exponentially small even after shifting the first beta shape by four to bound the x^-4 singularity. Evaluating the expansion at c_* plus and minus a fixed multiple of N^-1 traps the unique continuous zero by the strict sign ordering. Independent high-precision convolution and direct time-integral checks, including opposite signs at (N,k)=(20,6),(20,7), reproduced u_*, phi_*, the derivative ratio and c_* to the stated precision. Replay: python /workspace/branches/f39ae6a2-daf0-460f-881b-85c61671c7e8/brownian_rank_sensitivity_reproduce.py (mpmath). The numerical checks do not establish the asymptotic error or a global resetting optimum.

## originality

PASS

The finite-N mean law, single-searcher response, first-rank population crossover and leading critical fraction are established prior coverage. The supported distinction is the exact two-axis ordering for the admissible general-rank local sign, and especially the explicit nonzero order-one correction for the continuous critical rank. The inspected results do not state or directly give that correction.

## value

PASS

The sign tells whether weak resetting improves the expected time of a specified hit, and the exact two-axis law constrains how that answer can change with the target rank or the population. The correction is on the scale of physical integer ranks: it shifts the continuous decision boundary by roughly two required arrivals relative to the limiting fraction. These are useful distinctions for the finite-population model and do not assume global rate optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
