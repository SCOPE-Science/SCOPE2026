# Independent mathematical audit

## correctness

PASS

The exact 4x4 conditional-moment Metzler generator commutes with swapping environment and population coordinates, so its Perron eigenvector lies in the paired-symmetric plane and gives Lambda_M=-a-kappa+sqrt((b+kappa)(c+kappa)). The determinant factorization (b+k)(c+k)-(a+k)^2=(b+c-2a)(k-k*) establishes the unique positive k*. For the sample paths, dual Perron vectors h_e=(sqrt(c+k),sqrt(b+k)) and transpose yield a multiplicative martingale whose log is M_t-k int(Z-1-log Z); bounded jump logarithms give M_t/t->0. Riccati ratio dynamics have a compact attracting invariant range and long exponential sojourns force a positive entropy frequency uniformly near k*, hence pathwise negative growth for a right-neighborhood despite positive first moments. The rational witness has k*=7/5, determinant 3/5000, Lambda_M<1/12000, entropy loss >=147/250000, so pathwise exponent upper < -1/2000. Independently checked these Fraction identities and the conservative inequality; these finite exact checks do not themselves establish the almost-sure strong laws, supplied by martingale/renewal arguments.

## originality

PASS

General differences between stochastic pathwise growth and ensemble mean growth are known (Tuljapurkar–Horvitz–Pascarella 2003) and Markov switching stability criteria are known (Ogura–Preciado 2015). The surviving original contribution is this particular symmetric transposed-recruitment continuous-time model with closed-form unique mean switch threshold, a provably nonempty positive-mean/negative-pathwise right interval, and an explicit rational almost-sure decay rate despite mean growth. A broad existing top-Lyapunov theorem could imply qualitative sign separation, but no inspected source states these sharp coordinates or quantitative witness.

## value

PASS

An explicit rigorous positive-expectation/negative-typical-growth interval exposes a genuinely motivated diagnostic failure in two-population switching models. The sharp mean threshold and rational certified almost-sure gap give usable benchmark data for random positive linear systems without asserting the known general mean/typical separation as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
