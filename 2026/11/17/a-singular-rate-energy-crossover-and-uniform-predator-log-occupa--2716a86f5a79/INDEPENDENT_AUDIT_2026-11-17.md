# Independent mathematical audit

## correctness

PASS

For u,v>0, x=log u,y=log v, E=λ^(−1)f(x)+λ f(y), f(z)=e^z−z−1 is proper strictly convex; each E>0 is a compact regular Hamiltonian oval. Under λ=cE, M=λ E=cE² and g(y)=1−c f(y) on [y−,y+] where f(y±)=1/c, the inverse x branches solve f(x)=Mg(y). Exact original-time branch densities λd±(Mg(y))dy use d−=1/(1−e^s−),d+=1/(e^s+−1). Near simple endpoint zeros of g, d±=O(h^(−1/2)); for large h, d−−1 decays exponentially while d+=O(h^(−1)). Hence integrals of d−−1 and d+ are O(1/M) and O(log M/M), yielding T=cE(y+−y−)+O_c(log E/E). Exact negative-branch identity |−s−(h)−h|≤1 gives uniform first-coordinate fold error 1/M; small positive-branch mass and bounded support yield W1 original-time occupancy to law (1−cf(Z),Z) with Z uniform [y−,y+] at O_c(log E/E²). The supplied check_lv_crossover.py reconstructs LambertW inverse branches and quadratures for finite c/E (inspected, not relied on as proof); analytical estimates justify infinite limit.

## originality

PASS

Classical finite-energy exact Lotka–Volterra quadratures, fixed-rate large-energy periods and fixed λ=1 straight-line log-occupation theorem are acknowledged prior. The simultaneous λ=cE→infinity/E→infinity regime has a finite nonzero predator-log excursion and nonlinear fold time-law, with a new coefficient and uniform W1 bound, not furnished by fixed-λ asymptotics or static quadrature alone.

## value

PASS

The simultaneous rate-energy regime produces a qualitatively different time-sampling geometry from fixed-rate Lotka–Volterra oscillations: uniform predator log coordinate with nonlinear fold coupling and an explicit c-dependent physical-time period. Quantitative O(log E/E²) transport convergence is a natural nontrivial invariant for singular highly asymmetric cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
