# A sharp degree-covariance envelope for uniform multipartite spanning trees

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph on \(N=\sum_i n_i\ge3\) labeled vertices, with \(r\ge2\) and positive integer part sizes. Choose a spanning tree \(T\) uniformly from all spanning trees of \(G\), and write \(D_v=\deg_T(v)\). For any two *distinct* vertices \(u,v\), the exact covariance is

\[
\operatorname{Cov}(D_u,D_v)=-\frac{r-2}{N^2}-\sum_{i:\,u,v\notin V_i}\frac{n_i-1}{(N-n_i)^2}.
\]

Consequently the **sharp all-multipartite-host envelope** is

\[
-\left(\frac{N-3}{4}+\frac1{N^2}\right)\le \operatorname{Cov}(D_u,D_v)\le 0.
\]

The lower bound is attained **if and only if** the host is \(K_{1,1,N-2}\) (up to part permutation) and the two marked vertices are its singleton-part vertices. The upper bound is attainable, for instance, at vertices in different sides of any complete bipartite host. In the unique lower-extremal configuration, the correlation \(\rho_N=\operatorname{Corr}(D_u,D_v)\) satisfies \(N^2(1+\rho_N)\to4\): these degrees become nearly perfectly anticorrelated.

The known complete-multipartite tree enumerator is used as an input; novelty is claimed for the **sharp extremal covariance statement, unique optimizer, and its near-perfect anticorrelation rate**, not for the existence of the classical enumerator.

## Assumptions and scope

The host is finite, simple, connected, and complete multipartite. Each of the \(n_i\) is a positive integer; \(r\ge2\), \(N\ge3\); the tree is chosen uniformly, not by a weighted sampling convention. The marked vertices are labeled and distinct; their parts need not differ. Degrees are ordinary undirected degrees. The exact covariance and finite sharp bounds hold without asymptotic assumptions. The correlation limit applies only to the unique lower-extremal family with \(N\to\infty\).

For \(N=3\), the extremal host is \(K_3=K_{1,1,1}\), and any two distinct vertices constitute a lower-bound pair. Zero covariance occurs for two vertices in opposite part classes of a bipartite host. No claim is made that the lower-bound host is the only one attaining the upper bound.

## Proof

**1. A multivariate degree-generating identity.** Associate a positive indeterminate \(x_w\) with each vertex and write \(S=\sum_w x_w\) and \(S_i=\sum_{w\in V_i}x_w\). The classical complete-multipartite spanning-tree enumerator has the weighted form

\[
\sum_{T}\prod_{w}x_w^{\deg_T(w)}=
\left(\prod_w x_w\right)S^{r-2}\prod_{i=1}^{r}(S-S_i)^{n_i-1}.
\tag{1}
\]

Here is a direct reconstruction. Orient each tree toward a root \(w\) and weight the arc \(v\to u\) by \(x_u\). Its directed Laplacian has diagonal \(S-S_{i(v)}\), off-diagonal \(-x_u\) across parts, and zero within parts. Its right nullvector is \(\mathbf1\), its left nullvector is \((x_v)_v\). The nonzero eigenvalues are \(S\) with multiplicity \(r-1\), and \(S-S_i\) with multiplicity \(n_i-1\) for every part. The matrix-tree cofactor at \(w\) therefore equals

\[
x_w S^{r-2}\prod_i(S-S_i)^{n_i-1}.
\]

A root-oriented tree weight times \(\prod_vx_v/x_w\) is precisely \(\prod_vx_v^{\deg_T(v)}\). This proves (1) at positive \(x\), hence as a polynomial identity.

Setting all \(x_w=1\) gives \(N^{r-2}\prod_i(N-n_i)^{n_i-1}\) labeled trees. Dividing (1) by this count and removing the deterministic factor \(\prod_w x_w\) gives the joint probability-generating function

\[
\mathbb E\prod_w t_w^{D_w-1}=
\left(\frac{\sum_wt_w}{N}\right)^{r-2}
\prod_i\left(\frac{\sum_{w\notin V_i}t_w}{N-n_i}\right)^{n_i-1}.
\tag{2}
\]

Thus the excess-degree vector has the distribution of the sum of \(r-2\) independent one-hot vectors uniformly allocated over all vertices and, independently, \(n_i-1\) one-hot vectors uniformly allocated over vertices *outside* \(V_i\), separately for every part \(i\). This is an equivalent probabilistic reading of the classical enumerator, not an assertion of novelty.

**2. Two-vertex covariance.** A one-hot vector with categorical probabilities \((p_w)_w\) has covariance \(-p_up_v\) between two different coordinates. The global allocations in (2) contribute \(-(r-2)/N^2\). For each part \(i\), the \(n_i-1\) outside-part allocations contribute \(-(n_i-1)/(N-n_i)^2\) if and only if both marked vertices are outside \(V_i\). Summing independent contributions proves the exact formula. All terms are nonpositive.

**3. A sharp graph-and-pair optimization.** For real \(1\le s\le N-2\) define

\[
f(s)=\frac{s-1}{(N-s)^2},\qquad g(s)=f(s)+\frac1{N^2}.
\]

The function \(f\) is strictly increasing and strictly convex over its domain, \(f(1)=0\), and \(f(2)=1/(N-2)^2>1/N^2\) when \(N\ge4\). For positive integers \(a,b\) with \(a+b\le N-2\), convexity gives

\[
f(a+b)-f(a)-f(b)\ge f(2)>\frac1{N^2},
\]

and therefore \(g(a+b)>g(a)+g(b)\). This strict superadditivity follows also by summing increasing first differences. The \(N=3\) case is checked directly below.

If the marked vertices occupy *different* parts, let \(s_1,\ldots,s_k\) be all other part sizes, with \(k=r-2\), and \(S_0=\sum_js_j\le N-2\). Then

\[
-\operatorname{Cov}(D_u,D_v)=\sum_{j=1}^{k}g(s_j)\le g(S_0)\le g(N-2).
\]

For \(k=0\) the covariance is zero. For \(k\ge1\), equality throughout holds exactly when \(k=1\), \(S_0=N-2\), forcing the two marked parts to be singletons and the third part to have size \(N-2\). The value is

\[
g(N-2)=\frac{N-3}{4}+\frac1{N^2}.
\]

If both vertices occupy the *same* part, that part has at least two vertices; there are \(r-1\ge1\) other parts, of total size at most \(N-2\). The exact formula gives

\[
-\operatorname{Cov}(D_u,D_v)=\sum_{j=1}^{r-1}g(s_j)-\frac1{N^2}
\le g(N-2)-\frac1{N^2}<g(N-2),
\]

so no same-part pair is a lower-bound optimizer. When \(N=3\), a direct check covers the only connected host types \(K_3\) and \(K_{1,2}\): \(K_3\) gives \(-1/9\), while opposite sides of \(K_{1,2}\) give zero and its two same-part vertices have covariance zero. This completes sharpness and uniqueness.

**4. Extremal anticorrelation.** Write \(K_{1,1,N-2}\) with the two singleton vertices marked. In (2) their nonconstant degrees can be generated as

\[
D_u=1+B+G_u,\qquad D_v=1+(N-3-B)+G_v,
\]

where \(B\sim\operatorname{Bin}(N-3,1/2)\) and independently \((G_u,G_v,G_0)\) is a single multinomial draw with probabilities \((1/N,1/N,(N-2)/N)\). Consequently,

\[
\operatorname{Var}(D_u)=\operatorname{Var}(D_v)=\frac{N-3}{4}+\frac{N-1}{N^2},
\quad \operatorname{Cov}(D_u,D_v)=-\frac{N-3}{4}-\frac1{N^2}.
\]

For \(N>3\), the correlation equals the covariance divided by the common variance (the same formula also holds for \(N=3\)). Thus

\[
1+\rho_N=\frac{N-2}{N^2\big((N-3)/4+(N-1)/N^2\big)},
\qquad N^2(1+\rho_N)\longrightarrow4.
\]

The binomial central limit theorem also yields

\[
\left(\frac{D_u-\mathbb ED_u}{\sqrt N},\frac{D_v-\mathbb ED_v}{\sqrt N}\right)
\xrightarrow{d}(Z/2,-Z/2),\qquad Z\sim N(0,1).
\]

## Verification

The standalone standard-library checker `verify.py` independently enumerates Prüfer-encoded trees on 40 selected labeled multipartite hosts up to eight vertices, compares their complete excess-degree generating polynomials against (2), compares all pair covariances against the stated formula, and independently checks both the sharp numerical envelope and its equality condition. The checked run reported 102,778 valid trees, 6,834 coefficient comparisons, and 646 pair-covariance comparisons, all passing. This is finite corroboration; the proof above establishes the infinite family.

To replay: `python3 verify.py` from a directory containing that supplied file. It has no nonstandard dependencies.

## Relationship to prior work

Complete-multipartite spanning-tree enumerators and degree-refined generating functions are classical; Egecioglu–Remmel (1994) and the spanning-tree/function-class treatment of Remmel–Williamson (2002) are directly relevant antecedents. Formula (1) and its derived allocation law (2) are not treated as original. The new claim optimizes the resulting *two-degree covariance over every host composition and marked pair*, identifies the unique extremal multipartite shape, and quantifies the singular negative-correlation rate in that extremal family. Results about multipartite tree enumerators imply formula (2), but a general generating function alone does not state the sharp uniform bound or unique optimizer without the convexity analysis. A later 2026 paper studies a Kirchhoff algebra for the same \(K_{1,1,m}\) host and is noted as a priority comparison, not as the archival source.

## Limitations

The theorem concerns uniformly chosen spanning trees of connected *complete multipartite* graphs, not all graphs; it does not cover weighted random tree measures or higher-degree joint cumulants. The uniqueness statement is about the covariance *minimum*, not about its attainable maximum zero. The complete 1994 Egecioglu–Remmel paper was not available for full-text inspection, leaving residual historical priority risk that its degree-refined identities implicitly or explicitly include the sharp envelope. Independent validation has not been performed.

## References

1. Jeffrey B. Remmel and S. Gill Williamson, *Spanning Trees and Function Classes*, Electronic Journal of Combinatorics **9** (2002), R34, published 12 August 2002. https://doi.org/10.37236/1650; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i1r34/pdf/
2. Ömer Egecioglu and Jeffrey B. Remmel, *A Bijection for Spanning Trees of Complete Multipartite Graphs*, Congressus Numerantium **100** (1994), 225–243. Archived abstract: https://sites.cs.ucsb.edu/~omer/personal/abstracts/multipartite.html
3. Yohji Akama, *Strong Lefschetz property of Kirchhoff algebra of \(K_{1,1,n}\)* (2026), https://arxiv.org/abs/2610.21217. Later comparison only.
