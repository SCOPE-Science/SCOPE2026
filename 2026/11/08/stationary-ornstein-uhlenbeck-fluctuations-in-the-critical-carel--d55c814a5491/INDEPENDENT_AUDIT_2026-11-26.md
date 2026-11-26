# Independent mathematical audit

## correctness

PASS

Reconstructed the conditional binomial transition after the Bernoulli new draw. The affine regression gives μ_n=q_n/(1−a_n), n(1−a_n)=1+c−c/n, and the exact lag multiplier a_n^h. An independent shortcut checks the fluctuation scale: stationary total variance gives (1−a_n²)Var(K)=E V_n(K), and V_n≤c+1/4. Thus Var(K)=O(n), K/n concentrates at x=1/(1+c), and the bounded continuous-density variance formula gives E V_n→H=cx+x(1−x). Therefore Var(K)/n→H/[2(1+c)], agreeing with the subset recursion. The losses' binomial domination bounds fourth centered moments uniformly (use factorial moments up to order four); the scaled jumps vanish and the conditional Lindeberg sum tends to zero in L¹. Uniform-in-time bracket convergence follows by summing the stationary mean absolute variance errors. The bounded bracket rate controls the martingale increments at stopping times by O(δ+1/n); Doob and the linear drift give the needed supremum bound. Passing the martingale problem to continuous limits yields OU, whose initial law must be invariant: equality of its marginal with time zero for any single positive time in a finite horizon can be iterated by the OU semigroup. Uniqueness then gives the stated Gaussian and independence of the Brownian innovation. The explicit finite covariance kernel also converges directly. Independently checked n=2,p=1/2 by expanding the transition and verifying the invariant vector (5/12,1/2,1/12), mean 2/3, variance 7/18 and lag-one covariance 7/72. Frozen checker.py inspected, not executed; its finite checks do not establish process convergence. Replay RESULT.md:27–110.

## originality

PASS

For the frozen post-loss convention and p=c/n, the surviving contribution is the stationary path-space Gaussian limit with explicit parameters. The model, the density concentration, the stationary inclusion identities and algebraic consequences for the variance are not independent novelty; the general diffusion method is also prior. The closest inspected same-model results did not determine the stationary fluctuation process. This is a best-of-knowledge assessment against the passages below.

## value

PASS

The typical equilibrium dynamics at the critical loss scale are a natural question not answered by rare completion or macroscopic density concentration. The path law quantifies persistence of fluctuations on the n-step time scale and gives a usable Gaussian limit for repeated equilibrium observations. Its explicit noise law distinguishes the model from the independent-coupon surrogate despite the same mean density. This value attaches to the process-level result, not to recomputing the known stationary factorial recursion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
