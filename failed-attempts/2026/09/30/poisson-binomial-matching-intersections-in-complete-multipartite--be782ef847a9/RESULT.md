# Poisson-binomial matching intersections in complete-multipartite uniform spanning trees
## Finding
Let \(G=K_{n_1,\ldots,n_s}\) be a complete multipartite graph with \(s\ge2\), partite classes \(X_1,\ldots,X_s\), and \(N=\sum_{h=1}^s n_h\). Fix distinct \(i,j\), and let \(M\) be any matching of size \(m\), \(1\le m\le\min\{n_i,n_j\}\), whose edges all join \(X_i\) to \(X_j\). Let \(T\) be a uniformly random spanning tree of \(G\), and define
\[
\sigma_{ij}=\frac{1}{N-n_i}+\frac{1}{N-n_j},
\qquad
\beta=\sigma_{ij}\left(1-\frac{m}{N}\right).
\]
Then
\[
\mathbb E\!\left[z^{|T\cap M|}\right]
=
\left(1+\sigma_{ij}(z-1)\right)^{m-1}
\left(1+\beta(z-1)\right).
\]
Equivalently, \(|T\cap M|\) has the same distribution as the sum of \(m-1\) independent Bernoulli variables with parameter \(\sigma_{ij}\) and one independent Bernoulli variable with parameter \(\beta\).

More generally, for every \(q\)-edge subset \(F\subseteq M\),
\[
\Pr(F\subseteq T)
=
\left(1-\frac{q}{N}\right)\sigma_{ij}^{q}.
\]
Consequently, if \(\tau(G)\) is the number of spanning trees of \(G\), then
\[
|\{T:F\subseteq T\}|
=
\tau(G)\left(1-\frac{q}{N}\right)\sigma_{ij}^{q},
\]
where the classical complete-multipartite tree count is
\[
\tau(G)=N^{s-2}\prod_{h=1}^s (N-n_h)^{n_h-1}.
\]
For two distinct edges \(e,f\in M\),
\[
\operatorname{Cov}(\mathbf 1_{\{e\in T\}},\mathbf 1_{\{f\in T\}})
=
-\frac{\sigma_{ij}^{2}}{N^{2}}.
\]

## Assumptions and scope
Graphs are finite, simple, and connected. A uniformly random spanning tree means each spanning tree is selected with probability \(1/\tau(G)\). The matching \(M\) is fixed in advance and is contained entirely in the complete bipartite cut between two specified partite classes.

The Bernoulli interpretation is valid for every admissible \(m\). If \(m\ge2\), then \(N-n_i\ge m\) and \(N-n_j\ge m\), hence \(0<\sigma_{ij}\le1\) and \(0\le\beta\le1\). If \(m=1\), the first factor is absent and \(\beta\) is exactly the inclusion probability of the single edge, so again \(0\le\beta\le1\).

## Proof
Orient every edge of \(M\) from \(X_i\) to \(X_j\). For an oriented edge \(e=(u,v)\), write \(b_e=\mathbf e_u-\mathbf e_v\). The transfer-current theorem says that for any distinct edges \(e_1,\ldots,e_q\),
\[
\Pr(e_1,\ldots,e_q\in T)
=
\det\!\left[b_{e_a}^{\mathsf T}L^+b_{e_b}\right]_{a,b=1}^{q},
\]
where \(L^+\) is the Moore-Penrose inverse of the graph Laplacian.

Put \(d_i=N-n_i\) and \(d_j=N-n_j\). Fix \(e=(u,v)\in M\) and solve \(L\phi=b_e\) with \(\sum_x\phi(x)=0\). Direct substitution in the complete-multipartite Laplacian gives
\[
\phi(u)=\frac{N-1}{N d_i},
\qquad
\phi(x)=-\frac{1}{N d_i}\quad(x\in X_i\setminus\{u\}),
\]
\[
\phi(v)=-\frac{N-1}{N d_j},
\qquad
\phi(y)=\frac{1}{N d_j}\quad(y\in X_j\setminus\{v\}),
\]
and \(\phi=0\) on all other partite classes. These values sum to zero, and substituting them into \(L\phi\) yields \(+1\) at \(u\), \(-1\) at \(v\), and \(0\) elsewhere.

Therefore the transfer-current entry for \(e\) itself is
\[
b_e^{\mathsf T}L^+b_e
=
\frac{N-1}{N}\sigma_{ij},
\]
while for a different matching edge \(f=(x,y)\) disjoint from \(e\),
\[
b_f^{\mathsf T}L^+b_e
=
-\frac{1}{N}\sigma_{ij}.
\]
Hence the transfer-current matrix for any \(q\)-edge subset of \(M\) is
\[
\sigma_{ij}\left(I_q-\frac1N J_q\right).
\]
Its eigenvalues are \(\sigma_{ij}\), with multiplicity \(q-1\), and
\[
\sigma_{ij}\left(1-\frac qN\right),
\]
with multiplicity one. Taking the determinant proves the joint-inclusion formula.

Now let \(X=|T\cap M|\). Expanding the product of edge indicators gives
\[
\mathbb E[z^X]
=
\sum_{F\subseteq M}
\Pr(F\subseteq T)(z-1)^{|F|}.
\]
Grouping by \(q=|F|\) and using the joint-inclusion formula,
\[
\mathbb E[z^X]
=
\sum_{q=0}^{m}\binom mq
\left(1-\frac qN\right)
\sigma_{ij}^{q}(z-1)^q.
\]
The binomial theorem and its derivative reduce this to
\[
\left(1+\sigma_{ij}(z-1)\right)^{m-1}
\left(1+\sigma_{ij}\left(1-\frac mN\right)(z-1)\right),
\]
which is the claimed Poisson-binomial factorization.

Finally,
\[
\Pr(e,f\in T)=\left(1-\frac2N\right)\sigma_{ij}^{2},
\qquad
\Pr(e\in T)=\frac{N-1}{N}\sigma_{ij},
\]
and subtraction gives the covariance formula.

## Verification
A standalone exact checker independently verifies the joint-inclusion count by contracting each prescribed matching subset and applying the Matrix-Tree Theorem to the resulting multigraph. It checks every pair of partite classes and every admissible \(q\) for all \(58\) complete multipartite isomorphism types of orders \(2\) through \(8\), for \(394\) exact joint-count checks.

The checker also directly enumerates spanning trees for all complete multipartite types of orders \(2\) through \(6\) and compares the full distribution of \(|T\cap M|\) with the factorized probability generating function for every pair of partite classes, giving \(89\) full-distribution checks. These finite computations corroborate the proof but are not an independent audit.

## Relationship to prior work
Dong and Ge determined the number of spanning trees of a complete bipartite graph containing an arbitrary fixed spanning forest. Li, Chen, and Yan subsequently treated fixed spanning forests in complete multipartite graphs and obtained closed formulas for three and four parts. Wang and Ge later gave a determinant formula for an arbitrary fixed spanning forest in a complete multipartite graph.

Thus general fixed-forest enumeration is prior work. The contribution here is the matching-specific collapse of the transfer-current matrix to a rank-one perturbation for an arbitrary number of parts, together with the resulting closed joint-inclusion law, exact covariance, and the full Poisson-binomial distribution of the number of matching edges selected by a uniform spanning tree. In the bipartite case, the prescribed-submatching count is also obtainable by specializing Dong and Ge's fixed-forest formula.

## Limitations
The theorem concerns a matching contained between one fixed pair of partite classes. It does not claim the same factorization for matchings spread across several pairs of parts, for forests with adjacent edges, or for non-complete multipartite hosts. General fixed-forest determinant formulas already cover much broader inputs, but they need not reduce to this two-parameter distributional form.

The originality assessment is best-of-knowledge. The matching-count specialization is algebraically derivable from broader fixed-forest formulas; the novelty claim is restricted to the stated arbitrary-partite transfer-current simplification and Poisson-binomial intersection law. No independent audit, proof-assistant verification, or expert attestation has been performed.

## References
F. Dong and J. Ge, “Counting spanning trees in a complete bipartite graph which contain a given spanning forest,” arXiv:2103.05294, first public version 9 March 2021; Journal of Graph Theory 101 (2022), 79–94.

D. Li, W. Chen, and W. Yan, “Enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest,” Journal of Graph Theory 104 (2023), 160–170, DOI:10.1002/jgt.22954.

W. Wang and J. Ge, “On enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest,” arXiv:2602.03602, first public version 3 February 2026.

Y. Tang, F. Dong, and T. Tian, “Enumeration of spanning trees containing a perfect matching in saturated non-covered graphs,” Discrete Applied Mathematics 389 (2026), 126–134, DOI:10.1016/j.dam.2026.03.054.
