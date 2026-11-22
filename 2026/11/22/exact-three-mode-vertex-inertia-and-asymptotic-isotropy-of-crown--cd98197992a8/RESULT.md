# Exact three-mode vertex inertia and asymptotic isotropy of crown three-matching polytopes

## Finding
Let \(n\ge4\). Delete the diagonal perfect matching from the complete bipartite graph \(K_{n,n}\), obtaining the crown graph \(\mathrm{Cr}_n\). Let \(P_{n,3}\subset\mathbb R^{n(n-1)}\) be the convex hull of incidence vectors of all matchings of exactly three edges. Sample a vertex \(X\) uniformly and let \(\Sigma_n=\operatorname{Cov}(X)\) in the natural edge-coordinate Euclidean metric.

Write
\[
 m=n(n-1),\quad d=n^2-3n+3,\quad D=n^2-5n+8,\quad K=dD-2(n-1),\quad T=\frac{mK}{6},\quad p=\frac3m.
\]
The integer \(T\) is precisely the number of vertices. The **complete covariance spectrum** consists of four eigenvalue levels:
\[
\begin{array}{c|c|c}
\text{eigenvalue}&\text{multiplicity}&\text{eigenspace}\\\hline
0&1&\text{constant matrices}\\
\lambda_- =p+\frac{(1-n)D+n}{T}&n-1&\{x_{ij}=u_i-u_j:\ \sum_i u_i=0\}\\
\lambda_+=p+\frac{(3-n)D-(n-2)}T&n-1&\{x_{ij}=u_i+u_j:\ \sum_i u_i=0\}\\
\lambda_0=p+\frac{D}T&n^2-3n+1&\{x:\ \sum_{j\ne i}x_{ij}=\sum_{j\ne i}x_{ji}=0\ \forall i\}.
\end{array}
\]
For every \(n\ge4\), the three positive eigenvalues are strictly ordered \(0<\lambda_-<\lambda_+<\lambda_0\). In particular \(P_{n,3}\) has affine dimension \(n(n-1)-1\), and its intrinsic vertex-covariance condition number simplifies **exactly** to
\[
\boxed{\kappa_n=\frac{\lambda_0}{\lambda_-}=1+\frac{2n}{(n-3)(n-2)}.}
\]
Hence \(\kappa_n\) strictly decreases from \(5\) at \(n=4\) to \(1\), with \(\kappa_n=1+2/n+O(n^{-2})\). This is a quantitative asymptotic isotropy statement for the vertex cloud within its affine hull. The exceptional boundary \(n=3\) has precisely two vertices, covariance rank \(1\), and sole positive eigenvalue \(3/2\).

## Assumptions and scope
All graphs are simple, labelled and bipartite with distinct left/right copies of \([n]\). Edge coordinates are indexed by ordered pairs \((i,j)\) with \(i\ne j\), but graph edges are undirected connections from left label \(i\) to right label \(j\). A three-matching selects three edges with pairwise different left and pairwise different right endpoints. A binary incidence vector is necessarily a vertex of the convex hull of the binary incidence vectors: a convex combination representing it forces coordinatewise equality of all summands. Thus uniformly sampled vertices are exactly uniformly sampled three-matchings, not uniformly sampled interior points or all matchings of arbitrary size.

The covariance matrix is the population covariance \(\mathbb E[(X-\mathbb EX)(X-\mathbb EX)^\mathsf T]\). Nonzero eigenvalues are evaluated on the affine-hull tangent space with the inherited Euclidean metric. In particular the eigenvalue zero in the fixed-size all-ones direction is excluded from \(\kappa_n\).

## Proof
**1. Count three-matchings and paired edge incidences.** Put \(E=\{(i,j):i\ne j\}\), with \(|E|=m\). For a fixed edge \(e=(i,j)\), a compatible second edge \(f=(k,l)\) must satisfy \(k\ne i\), \(l\ne j\), \(k\ne l\), yielding \(d=(n-1)^2-(n-2)=n^2-3n+3\) possibilities. Among the \((n-2)^2\) possible third edges with new left/right endpoints, exactly \(n-u\) diagonal pairs are excluded, where \(u\) is the number of distinct numeric labels among \(i,j,k,l\). Since the two chosen edges are off-diagonal and nonattacking, \(u=4-\mathbf1_{i=l}-\mathbf1_{j=k}\). Hence the number of completions of a compatible ordered edge pair is exactly
\[
 t(e,f)=D-\mathbf1_{i=l}-\mathbf1_{j=k},\qquad D=n^2-5n+8.
\]
Each indicator sum counts \(n-1\) compatible second edges: these have respectively right endpoint \(i\) and left endpoint \(j\). Therefore for fixed \(e\), the sum of \(t(e,f)\) over compatible \(f\) is \(K=dD-2(n-1)\). Every three-matching has six ordered pairs of selected edges, so \(T=mK/6\) is the exact number of vertices. By simultaneous label symmetry every edge occurs with probability \(p=3/m\).

**2. The covariance operator.** On edge-indexed matrices \(x=(x_{ij})_{i\ne j}\), put \(S=\sum_{i\ne j}x_{ij}\), \(r_i=\sum_{j\ne i}x_{ij}\), and \(c_i=\sum_{j\ne i}x_{ji}\). Let \(A\) be the zero-one compatibility matrix of pairs of distinct nonattacking edges, and let \(B\) have entry \(\mathbf1_{i=l}+\mathbf1_{j=k}\) at a compatible pair \(e=(i,j)\), \(f=(k,l)\), and zero otherwise. Direct finite summation (including the possible reciprocal edge twice in \(B\)) gives
\[
 (Ax)_{ij}=S-r_i-c_j+x_{ij},\qquad (Bx)_{ij}=c_i+r_j.
\]
For different edges \(e,f\), the joint inclusion probability is \(t(e,f)/T\) when compatible and zero otherwise; for \(e=f\), it is \(p\). Consequently the complete operator identity is
\[
\boxed{\Sigma_n=pI+\frac{DA-B}{T}-p^2J,}
\]
where \(Jx\) is the constant matrix with entries \(S\). This derives the covariance from combinatorial counts, rather than inferring it from the line graph's adjacency spectrum alone.

**3. Orthogonal eigen-decomposition.** The constant matrices form one dimension, and have eigenvalue zero because every matching contains exactly three edges. For any \(u\in\mathbb R^n\) satisfying \(\sum_i u_i=0\), let \(x^+_{ij}=u_i+u_j\) and \(x^-_{ij}=u_i-u_j\). Both have total sum zero, and their row/column sums are
\[
 r_i(x^+)=c_i(x^+)=(n-2)u_i,\qquad r_i(x^-)=nu_i,\quad c_i(x^-)=-nu_i.
\]
Thus \(Ax^+=(3-n)x^+\), \(Bx^+=(n-2)x^+\), \(Ax^-=(1-n)x^-\), and \(Bx^-=-nx^-\). On the subspace \(U_0\) of zero row and column sums, also \(S=0\), so \(Ax=x\), \(Bx=0\). The four displayed subspaces are mutually orthogonal in the Frobenius product, and have respective dimensions \(1,n-1,n-1,m-2n+1=n^2-3n+1\). Their dimensions total \(m\), proving the complete spectrum and the asserted eigenvalue formulas.

**4. Strict positivity, order and condition ratio.** Elementary subtraction yields
\[
\lambda_+-\lambda_- =\frac{2(n-3)^2}{T}>0,\qquad
\lambda_0-\lambda_+=\frac{(n-2)(D+1)}T>0.
\]
Using \(K=(n^2-3n+3)(n^2-5n+8)-2(n-1)\), direct expansion and factorization give
\[
2T\lambda_-=K+2(1-n)D+2n=(n-3)(n-2)(n^2-5n+7)>0.
\]
Similarly \(2T\lambda_0=K+2D\), while \(2T(\lambda_0-\lambda_-)=2n(D-1)\). Cancellation with the last factorization proves
\[
 \frac{\lambda_0}{\lambda_-}=1+\frac{2n(D-1)}{(n-3)(n-2)(D-1)}=1+\frac{2n}{(n-3)(n-2)}.
\]
This formula is strictly decreasing on integral \(n\ge4\) since the derivative of the corresponding real function is \(-2(n^2-6)/[(n-3)^2(n-2)^2]<0\), and its expansion proves the asymptotic. In the smallest size \(n=3\) exactly two three-matchings exist, the two alternating perfect matchings of a six-cycle, yielding rank-one covariance with eigenvalue \(3/2\).

## Verification
`verify_crown_3match.py` is a standalone Python 3 standard-library verifier. It independently enumerates every three-subset of all off-diagonal rook positions for \(3\le n\le8\), retaining only nonattacking triples. Exact rational arithmetic compares every one-edge and two-edge inclusion probability against the formulas, evaluates covariance on explicit symmetric, antisymmetric and doubly centered eigenvectors, checks all eigenvalue orderings and verifies the trace identity \(\operatorname{tr}\Sigma_n=m p(1-p)\). Run `python3 verify_crown_3match.py`. Its successful final output is `CROWN_THREE_MATCH_PASS`. The infinite-family proof rests on the preceding symbolic identities; finite enumeration is corroboration, not a substitute for proof.

## Relationship to prior work
Torres, *Normality of k-Matching Polytopes of Bipartite Graphs* (arXiv:2306.11910v1, publicly posted June 20, 2023), defines these fixed-cardinality polytopes, proves their bipartite linear-inequality descriptions and normality, and does not supply their vertex covariance eigenvalues. Mirafzal, *The line graph of the crown graph is distance integral* (arXiv:2108.05223), studies a distance spectrum of the line graph, not the third-matching incidence covariance. Prior calculations of full matching polytopes of complete bipartite graphs (sampling **all** cardinalities) and crown **perfect** matching (derangement) assignment scores yield different ensembles, covariance kernels, and rank profiles: the latter has \(2n-1\) deterministic zero modes, whereas the present third-matching covariance has only one for \(n\ge4\). Neither specializes to the fixed-cardinality third-matching law above. The elementary combinatorial occupancy count and group-invariant decomposition are background; the new point is their exact spectral synthesis and the simplified decreasing condition ratio for this intermediate cardinality.

## Limitations
The assertions concern the uniform distribution on **three**-matching vertices in the standard Euclidean edge coordinates of the crown graph. They do not describe an arbitrary matching size, a weighted board, volume-uniform interior sampling, or a John/Löwner ellipsoid. Small-size \(n=3\) is exceptional; a separate proof is given. The usual historical priority caveat applies: an equivalent formula under a different assignment-statistics normalization or an unindexed treatment could predate this presentation. Independent mathematical validation has not been performed.

## References
- J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1 (June 20, 2023), https://arxiv.org/abs/2306.11910
- S. M. Mirafzal, *The line graph of the crown graph is distance integral*, arXiv:2108.05223v1 (August 10, 2021), https://arxiv.org/abs/2108.05223
