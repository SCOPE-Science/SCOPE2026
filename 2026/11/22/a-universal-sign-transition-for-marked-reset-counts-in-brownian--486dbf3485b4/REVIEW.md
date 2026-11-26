# Independent mathematical audit

## correctness

PASS

The bounded solution of the Brownian hitting-time Laplace equation Dg''=rg with g(0)=1 is g(x)=exp(−kx), k=√(r/D); by independence this is the probability of hitting before reset. If the initial excursion fails, sampled reset labels run until the first successful excursion. The failed labels have weights p_i(1−g_i) and the one terminal success label has weight p_i g_i. Summing over the number of failed labels gives the PGF, with the separate no-reset term g_0; the reset that starts the successful excursion is indeed counted. G>0 gives almost-sure absorption and a geometric tail. At the all-ones vector the derivatives give E N_i=(1−g_0)p_i/G and mixed moment (1−g_0)p_i p_j(2−g_i−g_j)/G², confirming the covariance and positivity of its prefactor. For a=x_i,b=x_j, the factorization with (1−e^(−ka))(1−e^(−kb)) proves strict positivity for x_0≤a+b. Otherwise δ=x_0−a−b>0, and multiplying by e^(k(a+b)) compares (e^(ka)−1)(e^(kb)−1) with 1−e^(−kδ). Their ratio starts at zero, diverges, and has logarithmic derivative >1/k by 1−e^(−u)<u<e^u−1. This proves the unique change of sign. Negative edges are a strict weight-sum threshold, and can only disappear as r grows. At equality x_0=a+b, the bracket is abk²+O(k³) instead of (a+b−x_0)k+O(k²); multiplied by 1−g_0 this verifies the r^(3/2) versus r asymptotics. Coincident spatial locations of distinct labels do not alter the argument. VERIFICATION.md and check_reset_counts.py were inspected, not executed. The diagnostic counter 3297 includes a fixed increment of 25 from the floating-point sign loop, not 3297 exact comparisons: one_case counts 3272 across its 184 rational instances. This bookkeeping overstatement in the diagnostic description is not relied on for the analytic result.

## originality

PASS

The evidence supports the exact all-rate covariance sign change and the mixture-invariant nested threshold graphs. Excursion renewal, geometric totals and marking a renewal law are not claimed as new methods. The closest two-site Brownian and pre-absorption count statements have different observables.

## value

PASS

The sign boundary answers a dependence question pooled reset counts cannot answer. It separates the geometry controlling which destinations are negatively correlated from the mixture weights controlling the size of covariance. The proof gives an exact criterion, the direction and uniqueness of every crossing, and an ordering of the resulting dependence graphs over rates. The marked renewal calculation alone would not justify the value assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
