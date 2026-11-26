# Independent mathematical audit

## correctness

PASS

The first-hit walk reaches F almost surely on the finite positive-conductance graph. Each failed excursion returns to N and is erased. At departure route i has probability w_i/sum_j w_j, and at its first interior vertex the harmonic function j/ell_i gives success probability 1/ell_i because both interior edge weights are w_i=1+A_i. Conditioning the first successful excursion gives the exact stated transition. Independent unit-start pure birth processes at per-particle rates 1/ell_i embed that chain. The total rate at population z is at most z/m, which gives nonexplosion; the finite superposition has infinitely many births. For each process the scaled nonnegative martingale converges almost surely and the scaled geometric law converges to Exp(1), so its almost-sure limit has this law. Independence of processes gives independent limits. At the nth total birth, e^(-tau_n/m)(n+k) converges to the sum S of only the fastest exponential limits. Dividing each coordinate by that identity to the appropriate power yields the joint almost-sure statements; subtracting one from each population does not affect their limits. The shortest ratios form a Dirichlet vector (degenerate when h=1). The longer amplitudes are all positive and share S, not independent in general. Conditional on S=t, their marginal survival probabilities are exp(-x t^r_i); the negative Gamma moment is finite exactly when r_i q<h, with logarithmic divergence at equality.

## originality

FAIL

The exact limits are covered by the deterministic diagonal specialization of Janson's prior triangular-urn theory after an exact change of variables, not just by a heuristic similarity. Set lambda_i=1/ell_i and Z_i=lambda_i(A_i+1). The frozen excursion identity chooses color i proportional to Z_i and adds exactly lambda_i to that chosen coordinate: Janson's unit-activity diagonal urn starting at x_i=lambda_i. Example 14.2, (14.6), gives independent scaled continuous-time limits G_i distributed as Gamma(1,lambda_i) (shape and scale). With all log exponents zero, the normalization in (5.11)–(5.12) and (5.17) is X_0=(1/lambda_max) sum_(j:lambda_j=lambda_max) G_j=sum_(j in I) E_j for E_j=G_j/lambda_j. Dividing the resulting discrete limit for Z_i by lambda_i gives the exact frozen joint vector for all i, including tied shortest routes. The CDF and moment formula are immediate functionals of that known joint law; the two-color moment threshold is already explicitly treated in (14.9).

## value

FAIL

The exact graph-specific laws are useful descriptive facts, but for the claimed contribution the only bridge to the already solved diagonal urn is the elementary conductance of a disjoint uniform route, w_i/ell_i, obtained by one-dimensional gambler’s ruin (or direct tree factorization). Once the route chain is written in the matching coordinates, the entire joint law and its marginal moments follow routinely from the prior exact law. The record neither treats non-disjoint networks nor supplies an unresolved quantity such as finite-n error or moment asymptotics. There is no independent nonmechanical remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
