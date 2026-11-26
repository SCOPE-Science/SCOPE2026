# Independent mathematical audit

## correctness

PASS

For a given periodic set of size k, its permutation contributes k!, and the complete-graph rooted forest determinant for the other vertices is k*n^(n-k-1) (one forest when k=n). This gives k*(n)_k/n^(k+1) and the telescoping tail (n)_k/n^k. Exchangeability gives independent uniform cyclic sets conditional on their sizes. The logarithm of the tail at k asymptotic to x*sqrt(n) tends to -x^2/2; the Gaussian tail bound ensures all fixed rescaled moments are uniformly integrable. For the fixed-size conditional array, selecting all distinct witnesses gives exactly (n)_L times the product of (m_i)_(d_i)/(n)_(d_i), with the claimed Poisson factorial limit. Any cross-pair collision forces one witness to demand at least three distinct memberships, giving a loss of at least n^(-1/2); there are only finitely many witness partitions for each fixed moment. A single intersection has factorial moments bounded by (m_i*m_j/n)^a, hence Hölder gives a joint exponential-moment bound when the sizes are O(sqrt(n)). This justifies Poisson moment convergence. Conditional convergence along every deterministic sequence with positive size limits and weak convergence of the size vector (or a Skorokhod coupling of the sizes) gives the claimed Rayleigh mixing for fixed q. For the empty probability, the Rayleigh double integral factors using r+s and r/(r+s), giving 1/3. Independently, summing the exact probability of disjoint sets of sizes a,b gives a*b*(n)_(a+b)/n^(a+b+2); collecting terms by a+b yields (E[K^2]-1)/(6*n), confirming 1/3 by moment convergence. Given the shared map's cyclic set, adjacent overlaps are independent with common conditional expectation K_i*E[K]/n, giving the asserted covariance, while disjoint pairs use independent maps. The mean and variance of the one-pair mixed Poisson follow from E[R]=sqrt(pi/2) and E[R^2]=2.

## originality

PASS

The one-map cyclic law and general Poisson approximation are classical, and the single deterministic pair is a hypergeometric special case. The checked sources do not give the random-mapping joint overlap array, its shared-map Rayleigh mixing and its exact empty probability. Strong approximation techniques can replace the proof of conditional Poisson asymptotics, with a model-specific comparison; neither the one-map distribution nor a Poisson approximation with deterministic means alone supplies the mapping array and its dependence.

## value

PASS

The overlap is a natural recurrence observable for independently chosen dynamics on the same labels. Each periodic set has vanishing relative size, yet common periodic vertices have limiting probability 2/3. The array resolves information lost by a one-pair Poisson heuristic: triple label coincidences vanish while overlaps sharing a map remain positively dependent because of its fluctuating cyclic-set size. This distinction and exact existence constant give useful benchmarks, not just a first-moment calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
