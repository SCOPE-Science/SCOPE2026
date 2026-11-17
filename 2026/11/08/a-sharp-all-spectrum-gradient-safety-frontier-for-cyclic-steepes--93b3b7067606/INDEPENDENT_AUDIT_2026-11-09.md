# Independent mathematical audit

## correctness

PASS

Normalize the SPD Hessian spectrum to [1,kappa] and weight gradient spectral coordinates by squared masses, with mean μ=1/alpha. The 2m-th power (1−λ/μ)^{2m} is convex, so endpoint chord replacement at equal μ proves exact two-extreme-eigenspace attainment for each fixed Hessian. The resulting ratio F_m(kappa,t)=(kappa−1)^{2m}(t+t^{2m})/((1+kappa t)^{2m}(1+t)) has two zero t-endpoints. For fixed t it grows strictly in kappa>1; at kappa=2 max<1 and at large kappa max>1, yielding unique kappa_m>2. Strict power-mean shows kappa_{m+1}<kappa_m. The upper/lower asymptotic sandwich h_m between U_m/(1+t*) and U_m+kappa^{-2m} yields kappa_m−2=[log m+log(4e)+o(1)]/(2m). Independent numerical maximization recomputed kappa_2=3.442815869257..., kappa_3=2.893404938161..., kappa_4=2.657498972144..., kappa_8=2.334440482558..., kappa_16=2.178028723860..., supplementary only.

## originality

PASS

Published two-step CSD objective monotonicity has sharp boundary kappa≈4.893733, but minimizes/maximizes the energy weighted by inverse eigenvalue rather than the Euclidean gradient norm. Its threshold neither implies nor equals gradient threshold kappa_2≈3.442816, and its statement is only m=2. Published cyclic-step convergence papers address asymptotic or almost-everywhere behavior, not worst-case cycle-boundary m-step gradient-norm safety and large-m frontier. No exact dominating published all-m statement identified.

## value

PASS

A full-dimension worst-case stability classification over all spectral mixtures, with extreme-mode reduction, a strict hierarchy across cycle lengths and log(m)/m transition scaling, is a meaningful structural condition-number boundary in numerical optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
