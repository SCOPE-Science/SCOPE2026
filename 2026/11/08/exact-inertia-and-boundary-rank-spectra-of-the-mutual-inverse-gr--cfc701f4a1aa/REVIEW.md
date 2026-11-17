# Independent mathematical audit

## correctness

PASS

The rank-r map coordinates by interval partitions A and images B have p=binom(n-1,r-1) rows and q=binom(n,r) columns. Mutual inverse iff cross-transversality, so K(X)=R X^T R. The incidence matrix R has a unit triangular p-column minor indexed by the right endpoints; its SVD splits each i=j diagonal into a positive lambda_i, each i<j pair into +/-sqrt(lambda_i lambda_j), and leaves p(q-p) zeros. In rank 2 the Gram entries min(i,j)(n-max(i,j)) invert to n times the Dirichlet path Laplacian; in rank n-1 Gram is the path tridiagonal (2,1). These exact proofs cover n=1 and r=n and do not claim a closed intermediate-rank trigonometric spectrum. Independent computations checked all 20 strata n=2..6, row rank/inertia and both boundary Gram spectra; numerical checks only corroborate the proof.

## originality

PASS

Earlier Resultary 2026-10-26 SCOPE central-binomial rank-and-inertia theorem explicitly gives the identical block inertia p(p+1)/2,p(p-1)/2,p(q-p) and the same R X^T R factorization; this portion is fully prior and receives NO novelty credit. Its full RESULT.md also gives the generic SVD eigenvalue construction (including signed singular products). The surviving original component, not proved there, is the closed trigonometric individual eigenvalue lists at r=2 and r=n-1, their exact Gram determinants and rank-two spectral-radius asymptotic. These are formulas for a natural semigroup graph invariant not produced by the prior generic matrix factorization. Best-of-knowledge historical scope is limited; standard path Laplacian spectra are known methods, and a previously published application to these inverse graphs would cover the remainder.

## value

PASS

The finite isotone mutual-inverse graph is natural in semigroup theory; explicit spectra at two distinguished nontrivial Green ranks answer a precise missing quantitative invariant and show an n^3/pi^2 spectral-radius scale at rank two. The already-known inertia and generic SVD identities have no independent novelty or value here. Boundary eigenvalue evaluations are modest and use elementary tridiagonal tools but are not merely a renamed known table of this graph, and can be used in adjacency spectral study.

The dated certificate retains the supplied scientific assessment, sources and limitations.
