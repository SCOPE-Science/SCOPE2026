# Independent mathematical audit

## correctness

PASS

Uniform insertion of each new maximum as a contiguous r-run into r(k-1)+1 equiprobable gaps uniquely enumerates r-Stirling words. If selected older labels are still intact, exactly (r-1)c_k(S) disjoint internal gaps destroy at least one; multiplication gives exact joint survival product. For a pair i<j, factorizing the joint product into marginals and R_{n,j}=product_{k>j}(1-2h_k)/(1-h_k)^2 gives negative covariance and local n^-1 limit -beta^2*a^beta*b^beta*(1/b-1). Summing diagonals yields single integral, offdiagonals double integral; uniform bound |cov(X_i,X_j)|<=C_r/max(i,j) controls near-origin pairs after n^-1 scaling. The proof text describes this discarded region as O(delta), but its explicit sum is O(delta+delta*log(1/delta)) and still tends to zero; this imprecise rate does not affect the convergence claim. Direct independent exact inclusion tests on all subsets for r,n=(2,5),(3,4),(4,3) and generated word histories passed. Full finite tests cannot prove n->infinity; harmonic estimates and dominated Riemann sums do.

## originality

PASS

Haglund–Visontai (2012) already construct stable multivariate Eulerian polynomials tracking value-indexed plateaux, implicitly encoding the full finite joint distribution and strong negative-dependence structure. That substantive prior is acknowledged; no novelty is assigned to labelled plateau statistics or generic negative correlations. The submitted exact insertion product directly produces an explicit two-parameter birth-prefix scaling covariance kernel, local 1/n covariance law, and closed all-t variance curve; no inspected primary theorem gives these explicit quantitative limits. Janson/Janson–Kuba–Panholzer cover aggregate and occurrence-indexed plateaux; Acan–Hitczenko concerns outdegree classes, not birth-age prefixes.

## value

PASS

A covariance kernel indexed by every pair of birth-age fractions provides a natural and precise second-order description of a canonical growing permutation/tree model, distinguishable from aggregate plateau variance. It can support later process-limit analysis without claiming a CLT; the explicit age structure is a mathematically useful invariant rather than a random finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
