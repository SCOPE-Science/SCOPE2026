# Independent mathematical audit

## correctness

PASS

For positive dampings and switch rates a,b,c,d,p,q and independent positive diffusivities, the stationary OU convolution exists uniquely. Conditioned on the complete shared environment, X1,X2 are independent centered Gaussians; Cov(X1,X2)=0 and their mixed fourth cumulant equals Cov(V1,V2) of conditional variances. Generator equations for state-weighted first moments U,T and product moment Z are exact invertible 2x2 systems with determinants K1,K2,K12>0. Algebraic elimination yields numerator p*q*(a-b)*(c-d)*N, N a sum of strictly positive parameter monomials, proving the necessary-and-sufficient sign/zero classification. Independently derived the full expression by symbolic 2x2 inversions and factored Cov(V1,V2) into precisely 4D1D2pq(a-b)(c-d)N/[(p+q)^2 K1 K2 K12], for unconstrained symbolic positive parameters; no reliance on finite samples. The sign vanishes exactly when a=b or c=d.

## originality

PASS

Best-of-knowledge PASS with serious broader-recursion precedent: Huang et al. 2014 derive conditional Gaussianity and multicomponent stationary mixed-moment recursion for arbitrary shared Markov environment, which includes this two-particle two-state model but does not explicitly state the global sign factorization or iff-zero frontier. Biroli et al. 2023 study identical trap responses (necessarily same-direction positive squared correlation), not counter-switching negative response. Resultary semantic queries found related 4th-cumulant and same-environment studies but no prior explicit heterogeneous two-state sign law. An unindexed application of the 2014 recursion may contain it; absence of a search hit does not establish priority.

## value

PASS

PASS: Independent particles may have exactly zero positional covariance but strictly negative squared-position covariance if the shared environment stiffens one while softening the other. The exact rate-uniform sign factorization and no-accidental-zero criterion are a meaningful structural classification of fluctuations in a well-motivated stochastic model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
