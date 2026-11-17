# Independent mathematical audit

## correctness

PASS

Uniform sampling from all matching incidence vertices of P_n for n>=4 is the uniform random involution law. For any edge e, P(e)=a=T_(n-2)/T_n; disjoint e,f have P(e,f)=b=T_(n-4)/T_n, and incident edges never co-occur. This produces covariance in the span of I, line-graph adjacency A, J. The Johnson line graph J(n,2) has 3 orthogonal invariant subspaces: all-ones (dim1), vertex-star contrasts (n-1), unsigned incidence kernel (n(n-3)/2). Inserting A eigenvalues 2(n-2),n-4,-2 yields exactly the three claimed lambda formulas. The telephone ratio recurrence proves strict lambda_size<lambda_star<lambda_cycle; two-step expansion T_n/T_(n-1)=sqrt(n)+1/2+O(n^-1/2) gives lambda_size~1/(2 n^(3/2)), lambda_cycle~1/n, hence ratio 2sqrt(n)+O(1). Independent exact enumeration of n=4..8 matchings, full covariance construction and eigenvalues confirms all spectra, including n4 (3/50,1/10,3/10) and n8 (1367/72962,13/382,43/382).

## originality

PASS

PASS best-of-knowledge. Standard matching/involution counts and line-graph Johnson eigenspaces are credited as ingredients, but the inspected matching-polytope primary literature focuses on skeleton regularity/degree, facets or fixed-size matchings and does not give the vertex-uniform second-moment spectrum with strict ordering and sharp square-root condition-number coefficient. Resultary counterpart for complete-bipartite partial-permutation vertices has a similar three-mode asymptotic but is NOT the complete-graph matching polytope (different edge-coordinate representation and incidence constraints). No verified stronger theorem implying exactly these complete-graph values was located.

## value

PASS

The entire covariance ellipsoid of the natural vertex-uniform matching polytope is explicitly diagonalized, identifies least- and most-variable combinatorial directions and computes sharp sqrt(n) anisotropy. This is a meaningful full spectrum and asymptotic, not merely a routine substitution into known telephone counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
