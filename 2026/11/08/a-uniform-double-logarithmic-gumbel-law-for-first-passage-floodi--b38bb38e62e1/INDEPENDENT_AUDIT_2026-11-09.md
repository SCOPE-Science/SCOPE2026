# Independent mathematical audit

## correctness

PASS

The final claim is hub-rooted flooding on B_{m,k}=K_1 vee (m K_k) with independent Exp(1) edges, m->infinity and EVERY sequence k=k_m>=2. A hub path cannot profit from traversing another petal. Within one K_{k+1}, successive exploration waits are independent Exp(i(k+1-i)/k) after multiplying flood time by k. Exactly the first and last rates equal one; the internal exponential tilt has exact residue product A_k=(k-1)^2, mean mu_k=2kH_{k-2}/(k-1), uniformly bounded centered variance and exponential moment. The gamma-two survival function and exponential tilt yield m P(kR_k>b+x)=e^{-x}[1+(log log m+x+1+delta_k)/log m]+O_x(m^(-1/12)/log m), delta_k=2log(k-1)-mu_k bounded uniformly in k. Independence across m petals produces the Gumbel and marked Poisson limits; the first/last independent rate-one waits have uniform ratio independent of completion time. k=1 is treated separately as a maximum of m Exp(1) edges. The critical computations were rederived for representative k from the source rate formula and the infinite uniform bound follows analytically, not by finite simulation.

## originality

PASS

Prior SCOPE clique-bouquet theorem (November 2, 2026) proves EXACT SAME hub flooding and Gumbel centering only when the petal order is fixed as m grows; its extra nonhub-start penalty is distinct. Asimit–Jones (2007, Proposition 1) treats maxima of fixed finite-dimensional phase-type laws with repeated dominant pole. The final contribution is the dimension-uniform second-order survival remainder for every oscillating/unbounded k_m plus an independent uniform endpoint-ratio mark and Poisson point process. These stronger quantifiers are not implied by the fixed-parameter results without a uniform-in-k estimate. Best-of-knowledge originality, not a priority certificate.

## value

PASS

A changing-petal-size first-passage model is natural: a hub links many dense modules, and neither the number of modules nor the within-module size must stay fixed. A size-uniform second-order extreme-value estimate and marked Poisson process require a nontrivial tilted-concentration mechanism and distinguish otherwise identical fixed-k approximations. The result provides a reusable exact distributional boundary and quantitative error; the earlier finite-size factorization alone does not give the desired arbitrary growth regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
