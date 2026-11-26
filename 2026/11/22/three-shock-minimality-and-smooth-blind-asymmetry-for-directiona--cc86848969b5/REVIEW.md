# Independent mathematical audit

## correctness

PASS

For strictly positive normalized factors, conditioning on an exceedance selects an X-shock with limiting probability p_i (or a Y-shock with q_i); joint high shocks have probability of smaller order. The radius is independent standard Pareto in the limit. For two independent radii, the Laplace law of their log ratio gives discordance probability (1-K)/2, where K=min(r_i/r_j,r_j/r_i); ties have probability zero, also at coincident slopes. The resulting ordered quadratic forms give equality for two distinct weight pairs only when a(1-a)=b(1-b), hence a+b=1, making the factors swap under relabeling; equal weights and one factor give coincident margins, and exchangeability implies equality directly. Independent rational arithmetic confirms both coefficients 16/25, chi=7/10, and unequal exponent evaluations 16/5 and 33/10 for the three-factor witness. The smooth formulas follow by conditioning the Poisson representation on a single high point: changing from radial X to radial Y gives mark law z F(dz) and reciprocal slope; other points are negligible after scaling. The given lognormal mixture preserves mean one. Bounded kernel continuity and uniform integrability of the bounded-sigma products preserve opposite endpoint signs of the contrast (-1/324,7/1620), and the intermediate value theorem gives exact equality. Uniform L1 convergence preserves the exponent gap t/3>=1/12 at sigma=0, and chi stays positive since the slopes are positive. Analyticity and strict positivity are on the open slope or angular interval, not asserted at the endpoints; the angular density is f_Z(w/(1-w))/(1-w)^3. Replay: /workspace/branches/a9ac287e-ac2c-4e9d-8bbe-3a4319edec9b/independent_exact_check.py for the exact finite witness and family points only; the limiting and minimality arguments are mathematical. Frozen checker inspected, not executed.

## originality

PASS

The coefficient definition, general extremal-function formula and standard spectral representations are credited to prior work. Distinct supported content is the sharp factor threshold under strict positivity and normalization, the finite rational witness, and exact zero directional contrast for nonexchangeable laws with strictly positive interior analytic spectra. The closest inspected sources do not establish those conclusions; the decision is limited to the evidence available.

## value

PASS

Population directional tail concordance is an established asymmetry diagnostic. The result distinguishes precisely when its equal values do force exchangeability in small positive max-linear models, and shows the failure is not just an atomic or support artifact. That is an interpretable limitation of a natural summary, not a claim about finite-sample power or all spectral models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
