# Independent mathematical audit

## correctness

PASS

For Brownian motion on (0,infinity) killed at 0, diffusion generator D d²/dx², start and instantaneous Poisson reset point a>0, I reconstructed the killed resolvent G_q=(exp[-sqrt(q/D)|x-a|]-exp[-sqrt(q/D)(x+a)])/(2D sqrt(q/D)) and absorption transform phi(q)=exp[-a sqrt(q/D)]. Conditioning on first reset/absorption gives the exact joint transform; differentiating yields E C=B1/phi, Var C=B2/phi+(B1/phi)², E T=(exp(gamma)-1)/r, Var T=(exp(2gamma)-1-gamma exp(gamma))/r² and Cov(T,C)=E C [(exp(gamma)-1-gamma/2)/r - d_q log B1(q)|_{q=r}], where B_j(q)=r int c(|x-a|)^j G_q dx, with r held fixed in q derivative. The covariance is strictly positive for every r>0 when the nonnegative cost has positive finite second resolvent integral. The exact left/right resolvent split, Karamata-Laplace/Potter bounds for c^j and one weighted k derivative give B_j(r)~gamma c(sqrt(D/r))^j Gamma(j beta+1) and -r d_q log B1(r) -> (beta+1)/2 for every measurable locally bounded eventually positive regularly varying cost with beta>=0. Thus Var T~gamma/r², Var C~gamma c(sqrt(D/r))² Gamma(2beta+1), Cov~(gamma/r)c(sqrt(D/r))(beta+1)Gamma(beta+1)/2. The universal limiting Pearson ratio follows without inferring an infinite theorem from numerical tests. The sharp unique maximum at beta=1 follows from Lprime(1)=0 and Lsecond=-1/(beta+1)²+[trigamma(beta+1)-trigamma(beta+1/2)]/2<0 on beta>=0. I separately wrote and executed a high-precision independently cross-differentiated renewal-transform checker: 24 covariance comparisons across 12 (a,D,beta) settings and two rates, with positive covariance and convergence samples. These are finite corroborations only.

## originality

PASS

Best-of-knowledge qualified PASS. The 2023 Sunil–Blythe–Evans–Majumdar paper gives the general joint cost-time Laplace renewal transform and is explicitly acknowledged; the source therefore already determines all fixed-rate moments in principle. Its inspected 26-page primary text, power/linear/quadratic cost sections and appendices do not state a regularly varying weak-reset Pearson correlation law or unique optimal growth exponent. The exact normalized singular limit and strict gamma-ratio optimization require substantial additional asymptotic and special-function reasoning, not an instantaneous substitution in a published table. Other inspected full-text papers concern physical return clocks, discrete walks, or other path functionals; the Resultary search produced the assigned paper itself as top match and other records with different observables. A 2026 thesis by the 2023 author is an important inaccessible plausible source; only its abstract was read, so no whole-thesis negative assertion or unqualified priority claim is made.

## value

PASS

The joint dependence of random search duration and cumulative reset-displacement cost is a motivated risk diagnostic separate from minimizing either mean. The theorem resolves a mathematically natural observable for every regularly varying cost of index beta>=0, not merely a fitted special case; the scale-independent gamma-function class profile and exact unique optimum at linear growth give a clear structural distinction. The strict positivity at all fixed rates is a useful complementary sign theorem. A future researcher comparing reset-cost growth laws and first-passage risk could need precisely this universal correlation; no assertion of a general physical-work, higher-dimensional, or finite-rate cap is made. The known joint transform is credited as input; the new all-class asymptotic and sharp inequality provide more than repeating the transform.

The dated certificate retains the supplied scientific assessment, sources and limitations.
