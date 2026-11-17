# Independent mathematical audit

## correctness

PASS

Conditioning on all exogenous rule choices fixes total T_n=T0+cn+delta sum xi and makes V_n/J_n a martingale with J_n=prod(1-2b xi_j/(T_(j-1)+a+b)) positive since a>=b>=1. Weighted centred Bernoulli sums converge almost surely by square-summable variance; Hoeffding bounds give T_j=cj+delta kappa j/log(j)^theta plus controlled error. Taking logarithms of J isolates 2b/c sum xi/j and -2b delta kappa/c² sum xi/[j(log j)^theta]; latter diverges as kappa log log n only when theta=1/2. The remainder multiplied by switches is summable for 3theta>1, resulting in J_n R_(n,theta)-> K(xi)>0. Martingale increments O(1/(nJ_n)) have square-summable conditional variances because J_n^-1=n^o(1). Pólya steps have positive draw variance, so the conditional limit is nondegenerate. Independently reproduced exact finite one-step drift for unequal totals in six rational parameter/state combinations. No claim for theta<1/2 or other replenishment dynamics.

## originality

PASS

Prior published quenched harmonic criterion for balanced total c=a+b settles qualitative equalization when sum p_n/n diverges, not unbalanced sharp normalization and not the delta kappa² log-log term. Resultary October 18 logarithmic-time Dirichlet crossover uses balanced additions and triangular arrays with constant per-row p_N, not a single nonstationary urn. Another critical Ornstein-Uhlenbeck window is a balanced fixed-increment triangular array, and existing fixed positive probability Pólya-Friedman urn CLTs do not cover the regime. The nondegenerate a.s. amplitude and exact theta=1/2 correction survive these comparisons. General stochastic approximation coverage remains residual risk.

## value

PASS

Slowly vanishing opposite-colour reinforcement interpolates between classical random Pólya limits and deterministic equalization. The sharp multiplicative normalization, half-logarithmic boundary and sign-sensitive unbalanced-total logarithmic correction quantify a natural martingale rate not supplied by a convergence-only criterion; exact nondegenerate amplitude helps distinguish pathwise from Gaussian regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
