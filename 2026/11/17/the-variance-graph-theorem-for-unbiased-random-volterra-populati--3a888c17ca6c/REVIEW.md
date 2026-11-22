# Independent mathematical audit

## correctness

PASS

For every finite m>=2 and iid-in-time centered independent edge coefficients bounded |xi|<=rho<1, the simplex is invariant and all coordinates X_i are bounded martingales and hence converge a.s. Skew symmetry conserves total mass. Expanding H=sum_i X_i^2 gives exact conditional drift 2 sum_{ij in E} E[xi_ij^2] X_i^2 X_j^2, since cross-edge covariances vanish. Its expected sum is bounded by H<=1 and implies each edge endpoint product tends to zero a.s. Thus the limiting support is an independent set; every such face is pointwise fixed and all stationary measures on the compact simplex must be supported on these faces by zero integrated drift. Complete G iff only vertices survive for every starting x; winning law follows from E X_infty=x. For strictly positive initial x, on winner event I=i, the loser log-increments differ Cesaro-negligibly from iid log(1+xi_ji), giving negative exponent by strong law and Jensen. Complete multipartite part masses likewise martingales. Independent exact-rational two-edge example conditional drift 277/36450 matches formula; finite checks do not substitute for martingale theorem.

## originality

PASS

The published Jamilov–Scheutzow–Wilke-Berenguer random Volterra result requires nonzero chance of an extreme quadratic stochastic operator (Vx)_k=x_k^2; impossible here because all coefficients have magnitude strictly less than one, so their vertex-convergence theorem does not imply this result. Deterministic QSO propagation literature also lacks the independently fluctuating edge-variance graph classification. The sharp sparse graph invariant-law and complete-graph iff, with winner probabilities and almost-sure extinction rates, remain distinct under inspected statements.

## value

PASS

A graph-theoretic if-and-only-if for universal fixation, a complete stationary-measure classification on arbitrary sparse interaction structures, and exact winning/extinction laws are structural and useful in random competition dynamics. The correlated-versus-independent edge distinction produces qualitatively different stationary states despite the same unbiased mean, exceeding a routine parameter tweak.

The dated certificate retains the supplied scientific assessment, sources and limitations.
