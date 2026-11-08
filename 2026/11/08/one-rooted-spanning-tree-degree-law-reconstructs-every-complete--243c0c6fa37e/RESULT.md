# One rooted spanning-tree degree law reconstructs every complete multipartite graph

## Finding

**Theorem (exact one-vertex reconstruction).** Fix an integer \(N\ge2\). Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple connected complete multipartite graph with \(r\ge2\), \(n_j\ge1\), and \(\sum_{j=1}^{r}n_j=N\). Choose *any* vertex \(v\), without revealing which part contains it, and let \(T\) be uniformly distributed over the spanning trees of \(G\). The probability law of the single integer \(D_v=\deg_T(v)\), together with \(N\), uniquely determines the unordered multiset \(\{n_1,\ldots,n_r\}\), hence the isomorphism class of \(G\). An explicit reconstruction uses only the multiplicities of the integral roots of \(P_v(z)=\mathbb E[z^{D_v}]\).

In particular, even a single rooted marginal law, rather than a joint collection of degrees, suffices throughout this graph family.

## Assumptions and scope

All edges are unweighted; each spanning tree has equal probability. The total vertex count \(N\) is *known*. There are at least two nonempty parts, so the host graph is connected. No knowledge of the part containing \(v\) is required. The claim concerns the exact probability law, not a finite sample or an arbitrary host graph.

For a polynomial \(P\), write \(\operatorname{ord}_{\alpha}P\) for the multiplicity of its zero at \(\alpha\), interpreted as zero when \(P(\alpha)\ne0\).

## Proof

Let \(V_j\) be the parts, let \(v\in V_i\), and put \(N=\sum_jn_j\). The weighted complete-multipartite tree identity is
\[
\sum_{T\text{ spanning}}\prod_{u\in V(G)}x_u^{\deg_T(u)}
=\left(\prod_{u\in V(G)}x_u\right)
\left(\sum_{u\in V(G)}x_u\right)^{r-2}
\prod_{j=1}^{r}\left(\sum_{u\notin V_j}x_u\right)^{n_j-1}.
\tag{1}
\]
This is the classical multivariate spanning-tree enumerator for complete multipartite graphs, obtainable by the weighted Matrix-Tree Theorem or the multipartite tree/function bijection; it is used as a prior identity, not asserted as new here. Its normalization at all \(x_u=1\) is the standard spanning-tree count \(N^{r-2}\prod_j(N-n_j)^{n_j-1}\).

Set \(x_v=z\) and \(x_u=1\) otherwise in (1), and divide by the value at \(z=1\). Precisely,
\[
P_v(z)=z\left(\frac{N-1+z}{N}\right)^{r-2}
\prod_{j\ne i}\left(\frac{N-n_j-1+z}{N-n_j}\right)^{n_j-1}.
\tag{2}
\]
Every exponent is a nonnegative integer, and the bases have positive denominators because \(r\ge2\).

We give the reconstruction explicitly. The zero \(z=-(N-1)\) cannot come from any of the factors indexed by \(j\ne i\), since \(n_j\ge1\), and it does not coincide with \(z=0\). Hence
\[
r=2+\operatorname{ord}_{-(N-1)}P_v.
\tag{3}
\]
For each integer \(t\) satisfying \(2\le t\le N-1\), define
\[
c_t=\frac{\operatorname{ord}_{-(N-t-1)}P_v-\mathbf1_{\{t=N-1\}}}{t-1}.
\tag{4}
\]
The subtraction for \(t=N-1\) removes the mandatory factor \(z\). Factorization (2) shows that \(c_t\) is *exactly* the number of parts of size \(t\) other than \(V_i\), even when \(v\) lies in an otherwise unique part of that size. Parts of size one leave no visible factor. Thus the number of singleton parts other than \(V_i\) is
\[
c_1=r-1-\sum_{t=2}^{N-1}c_t.
\tag{5}
\]
The size of the part containing \(v\) is the positive integer
\[
n_i=N-c_1-\sum_{t=2}^{N-1}t c_t.
\tag{6}
\]
Equations (3)--(6) produce the complete multiset consisting of one part of size \(n_i\), \(c_1\) singleton parts, and \(c_t\) parts of size \(t\) for each \(t\ge2\). Since the construction depends only on \(N\) and \(P_v\), no two nonisomorphic connected complete multipartite graphs of the same order have the same rooted uniform-spanning-tree degree law. This includes the two-vertex edge, complete graphs, and stars. \(\square\)

For illustration, take \(G=K_{1,2,2,3}\), \(N=8\), and observe a vertex in the three-vertex part. Formula (2) gives
\[
P_v(z)=z\left(\frac{7+z}{8}\right)^2\left(\frac{5+z}{6}\right)^2.
\]
The multiplicity two at \(-7\) gives \(r=4\). The multiplicity two at \(-5\) gives two other parts of size two. Exactly one of the remaining three other parts is a singleton; the residual part has size three.

## Verification

The standalone \(\texttt{verify.py}\) independently constructs each graph and evaluates Kirchhoff cofactors after multiplying edges incident with a chosen vertex by an integer \(z\). It compares this **separate matrix computation** with (2), reconstructs the part multiset by rational polynomial interpolation and integer-root division, and checks that distinct part multisets never share a tested rooted law. For every integer \(2\le N\le9\), every unordered positive partition into at least two parts, and each part chosen as the root type, all 2,892 evaluated determinant-to-formula comparisons and all 336 reconstruction tests pass. This is finite corroboration; the theorem for all \(N\) follows from the preceding algebraic proof.

Run using \(\texttt{python3 verify.py}\) in the same directory as this document. The checker uses the Python standard library only.

## Relationship to prior work

The weighted complete-multipartite spanning-tree identity (1) is background mathematics, associated with the multipartite tree bijections of Eğecioğlu--Remmel and the multivariate spanning-tree framework of Remmel--Williamson (2002); it is not presented as a new enumerator. Rapoport (arXiv:2312.14992, first public 2023-12-22) treats joint uniform-spanning-tree degree probabilities on general finite graphs. Fita Sanmartín--Schnörr--Hamprecht (arXiv:2409.13472, first public 2024-09-20) obtain general node-degree moment and covariance formulas. Li--Chen--Yan (2023) give fixed-forest containment counts for multipartite graphs with three or four parts. These forward enumeration and moment methods are compatible with the theorem and supply some of its ingredients; the particular all-parameter *inverse uniqueness and constructive root-multiplicity recovery from one marginal law* is the assessed statement. It is not implied by merely identifying a degree formula for a single fixed host without proving cross-host injectivity.

## Limitations

The reconstruction requires an exact probability law and the known integer \(N\). It makes no finite-sample accuracy, robustness, statistical efficiency, or identifiability claim outside the connected complete multipartite class. Without a known order, leaves in stars of different sizes all have the same deterministic law \(D_v=1\), so that hypothesis matters. Existing multivariate enumerators offer strong prior coverage, and an uncatalogued earlier inversion result remains a historical-priority risk. No external mathematical audit has been performed.

## References

1. J. B. Remmel and S. G. Williamson, *Spanning Trees and Function Classes*, Electronic Journal of Combinatorics **9** (2002), R34. https://doi.org/10.37236/1650 (first published 2002-08-12).
2. A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992 (first public 2023-12-22). https://arxiv.org/abs/2312.14992.
3. E. Fita Sanmartín, C. Schnörr and F. A. Hamprecht, *Expectation and Variance of the Degree of a Node in Random Spanning Trees*, arXiv:2409.13472 (first public 2024-09-20). https://arxiv.org/abs/2409.13472.
4. D. Li, W. Chen and W. Yan, *Enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, Journal of Graph Theory **104** (2023), 160--170. https://doi.org/10.1002/jgt.22954 (first public 2023-03-30).
5. C. Pozrikidis, *Node degree distribution in spanning trees*, Journal of Physics A **49** (2016), 125101. https://doi.org/10.1088/1751-8113/49/12/125101.
