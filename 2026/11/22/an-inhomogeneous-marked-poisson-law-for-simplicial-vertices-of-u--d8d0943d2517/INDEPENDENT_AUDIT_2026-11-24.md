# Independent mathematical audit

## correctness

PASS

Two disjoint neighbors of a tagged interval yield an interior right endpoint before an interior left endpoint, and the converse follows from the same ordering (their owners are necessarily distinct). Partitioning by the last interior left endpoint gives the proposed finite formula; the two exclusions for any other interval cannot coexist. At distinct tagged positions each fresh interval contributes a single local endpoint with the stated marginal first-order rate, with all multiple-endpoint contributions O(n^-2). The independent endpoint Poisson limits thus give the conditional factorization and the last-left-point formula for f. The bounded-window factorial moments converge by dominated convergence; on a compact set of endpoint-mark volume v they are bounded by (2v)^k, so the Laplace-functional factorial expansion also converges absolutely and proves the Poisson law. The two separated endpoint subwindows bound the long-mark contribution by a uniformly vanishing exponential tail. Integration gives the precise interior log-odds means. In the harmonic calculation setting s=1-a and 1-b=su gives the integral of (1-u^(2n))/(1-u^2); the expected overlap is one by uniform matching of endpoint ranks. The attached check.py was read, not executed; its finite checks are supplementary to this reconstruction.

## originality

PASS

The marked intensity, count law and tagged exact probability were not supplied or implied by the strongest inspected published comparisons. This is an evidence-bounded assessment, not certification of historical priority.

## value

PASS

The result identifies a sparse, geometrically interpretable statistic in a standard dense random graph model, with nonconstant spatial intensity and location-dependent mark law. It yields local counts, joint independence and finite-size probabilities without conflating interior limits with global boundary behavior; the logarithmic global lower bound shows why that distinction matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
