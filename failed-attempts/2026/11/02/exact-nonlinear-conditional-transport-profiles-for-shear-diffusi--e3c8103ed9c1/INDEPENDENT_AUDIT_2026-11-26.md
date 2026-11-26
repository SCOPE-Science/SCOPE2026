# Independent mathematical audit

## correctness

PASS

The stationary exponential age and Gaussian bridge give X conditional on y,a mean gay/2 and variance 2Da+Dg²a³/6 (bridge integral variance a³/12 before the noise prefactor). Bayes gives the age density proportional to a^(-1/2) exp(-ra-y²/(4Da)), a GIG with index 1/2, with its Gamma boundary at y=0. For fixed y, differentiating the normalizer I=√(π/r) exp(-z) gives E[A^n|y]=(-∂r)^n I/I. The corresponding polynomials obey P_(n+1)=(2n+1+z)P_n-zP'_n; in particular Var(A|y)=(z+2)/(4r²). The total conditional variance sums the conditional Gaussian variance with (gy/2)² Var(A|y), yielding P3+3z²(z+2)=4z³+12z²+15z+15 in the shear term. This proves the formulas including y=0, zero shear, and monotonicity in |y| (right derivative at the origin). The age formula and Gaussian moment expansion prove the higher-moment claim. An independent numerical check using a=s² checked 45 nonzero-order age moment evaluations and 15 conditional mean/variance pairs across three parameter sets, with 2e-10 relative tolerance. Integrating over the exponential law of z also recovers the two known unconditional covariances. The frozen script was not run.

## originality

FAIL

The polynomials were not found printed as conditional profiles in the checked primary article, but are mechanical consequences of its stronger exact renewal solution, not of its perturbation or its unconditional covariances. At origin reset, completing the square in published Eqs. (2)–(3) gives exactly the age-conditioned Gaussian mean and variance above; normalizing Eq. (5) in x gives I and the posterior age density. The only evaluations are differentiating the elementary known I at fixed y, up to order three for the profiles, and taking Gaussian moments. This same rule determines the entire polynomial hierarchy. The distinct Resultary projection record has substantial overlap in the age-conditioned Gaussian covariance and states the exact transverse normalization; it need not have priority over the frozen record for the older primary article to establish the implication.

## value

FAIL

Conditional profiles and their nonlinear growth are meaningful observables for this model. But the asserted increment over existing mathematics is the routine exact moment evaluation of an already supplied kernel, with no additional independent structural result. That does not meet the narrow exact-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
