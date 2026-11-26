# Independent mathematical audit

## correctness

PASS

Independently checked by tilting with X_j²: E[X_j² H] equals α_j(α_j+1)/[A(A+1)] times the mean entropy for Dirichlet(α+2e_j). At that shift, the local numerator contribution α_j ψ(α_j+1) increases by 2ψ(α_j+1)+2+1/(α_j+1). In the sum over j, subtracting E[H]E[Q] and using ψ(A+3)-ψ(A+1)=1/(A+1)+1/(A+2) gives the stated negative rational term and the stated negative weighted digamma covariance term. The pairwise covariance sum is nonnegative, and is zero exactly for equal parameters since all weights are positive and ψ is strictly increasing. A²-S₂=2∑_{i<j}α_iα_j>0 for k≥2, so negating gives strict positivity for G=1-Q. Substitution gives the symmetric formula; positive Dirichlet posterior parameters require no new argument.

## originality

FAIL

Distinct indexed results already cover the entire assessed identity, strict sign and equality case at the time of this review. In particular, the finite-asymmetric identity and sharp bound in 5d2816799bb7 coincide term by term using 2κ=A²−S₂ and Cov(H,1−Q)=−Cov(H,Q); 6373915567bd repeats the identity and adds a local fixed-total symmetry transition. The dated paths for these matches are later than the frozen path, so this is a finding of equivalent existing coverage, not a finding that any of them has historical priority or that the frozen proof depends on them. The earlier symmetric and Poisson–Dirichlet works alone would not establish full coverage.

## value

PASS

As a mathematical result, a distribution-wide sharp sign and explicit heterogeneity term for joint uncertainty in two natural diversity summaries is useful. It is not a deterministic ordering: Shannon entropy and concentration can both increase between two points of the three-simplex. The bound identifies precisely how heterogeneity affects this covariance beyond its rational baseline. This scientific usefulness does not supply originality credit for the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
