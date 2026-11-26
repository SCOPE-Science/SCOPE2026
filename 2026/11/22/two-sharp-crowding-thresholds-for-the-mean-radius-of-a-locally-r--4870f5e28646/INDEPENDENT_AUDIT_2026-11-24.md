# Independent mathematical audit

## correctness

PASS

Grange's stationary flux equations and matching yield F=v rho/v_0, F'=-chi rho on x>0, F(0)=c, F(b)=1, with the selected low-density root on the gas side and b=log(c)/(mu chi)>0. The normalization is exact: integrating the flux slope with F(infinity)=0 gives mass c/chi per side. The flux itself gives a direct independent moment computation: P(|X|>x)=F(x)/c. In the tail integral for E|X|, change variable from x to z=F(x); the integrand after factoring out 1/(c chi) is z/rho(z). In the core rho=mu z, so the integral from z=1 to c is (c-1)/mu. In the gas z/rho(z)=(1+sqrt(1-4z/mu))/2, positive and bounded on [0,1], with the continuous limit at zero. Its integral is 1/2+(mu/12)[1-(1-4/mu)^(3/2)], equal to (1+q+4/q)/6 using mu=q^2/(q-1), q in (1,2). Differentiating gives dE|X|/dmu=[q(q+2)/6-(c-1)]/(c chi mu^2). Since q strictly decreases, q(q+2)/6 falls strictly from 4/3 to 1/2. This gives strict monotonicity even at c=3/2 and 7/3 (the endpoints are excluded), and a unique maximum with q_*=-1+sqrt(6c-5) otherwise. Using (c-1)=q_*(q_*+2)/6 in the moment gives the claimed height; q=2 and 1 give both endpoint limits. The half-width decreases directly at fixed c,chi. Independent flux-coordinate quadrature at 90 settings agreed to absolute error below 6.2e-10; the analytic derivative, not the grid, proves the classification.

## originality

PASS

The branch, mass relation, width and the necessary flux primitive are prior ingredients. The mean is directly computable from published profiles and recoverable on the pure-gas coexistence domain via the earlier W_1 difference and gas mean. The supported distinct contribution is the global exact response of this one branch as crowding varies at fixed rates and mass, with two mass-flux cutoffs and an optimizer across the full admissible domain.

## value

PASS

The normalized mean distance is a whole-distribution localization statistic, whereas the known shrinking core describes only one boundary. The core mass remains fixed as crowding changes, yet the increasing, peaked and decreasing global response regimes differ. The exact parameter cutoffs and peak location identify when the core width is a misleading proxy for spread. This is a complete parameter response across a natural branch, not a numerical counterexample or an isolated integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
