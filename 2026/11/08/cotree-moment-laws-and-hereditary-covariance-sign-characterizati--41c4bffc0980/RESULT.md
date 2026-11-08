# Cotree moment laws and hereditary covariance-sign characterization of cographs

## Finding

Let \(G\) be any finite nonempty simple cograph on the labeled vertex set \(V\), with \(n=|V|\). Its standard stable-set polytope is
\[
 P_G=\operatorname{conv}\{\mathbf 1_S:S\subseteq V\text{ is stable in }G\}\subseteq\mathbb R^V.
\]
It is full-dimensional because it contains the origin and every coordinate unit vector. Let \(X\) be uniform with respect to normalized \(n\)-dimensional Lebesgue volume on \(P_G\), and for every nonnegative integer multiindex \(\alpha\) put
\[
 M_G(\alpha)=\mathbb E\prod_{v\in V}X_v^{\alpha_v},\qquad
 |\alpha|=\sum_{v\in V}\alpha_v.
\]
Use the rising factorial \((t)_j=t(t+1)\cdots(t+j-1)\), including \((t)_0=1\).

**Exact all-degree moment and volume recursion.** Every cograph has a binary cotree with singleton leaves and internal disjoint-union or graph-join nodes. At a singleton leaf \(G=K_1\),
\[
 \operatorname{Vol}(P_G)=1,\qquad M_G((a))=\frac1{a+1}\quad(a\ge0).
\]
For two nonempty vertex-disjoint cographs \(A,B\), put \(a=|V(A)|\), \(b=|V(B)|\), \(N=a+b\), and let \(\alpha_A,\alpha_B\) be the restrictions of \(\alpha\). At a disjoint-union node,
\[
 \begin{aligned}
 \operatorname{Vol}(P_{A\sqcup B})&=\operatorname{Vol}(P_A)\operatorname{Vol}(P_B),\\
 M_{A\sqcup B}(\alpha)&=M_A(\alpha_A)M_B(\alpha_B).
 \end{aligned}
\]
At a graph-join node,
\[
 \boxed{\begin{aligned}
 \operatorname{Vol}(P_{A\vee B})&=\frac{a!b!}{N!}\operatorname{Vol}(P_A)\operatorname{Vol}(P_B),\\
 M_{A\vee B}(\alpha)&=\frac{(a+1)_{|\alpha_A|}(b+1)_{|\alpha_B|}}{(N+1)_{|\alpha|}}
 M_A(\alpha_A)M_B(\alpha_B).
 \end{aligned}}
\]
These recurrences evaluate every mixed polynomial moment as an exact rational number using the cotree, with no vertex enumeration or triangulation required.

**Sharp covariance signs.** Put \(\mu_v=\mathbb E X_v>0\). For every distinct pair \(v,w\),
\[
 \boxed{\begin{array}{ll}
 vw\in E(G): & \displaystyle\mathbb E[X_vX_w]\le\frac{n+1}{n+2}\mu_v\mu_w<\mu_v\mu_w,\\[3pt]
 vw\notin E(G),\;v,w\text{ in the same connected component}: & \mathbb E[X_vX_w]>\mu_v\mu_w,\\
 v,w\text{ in distinct connected components}: & \mathbb E[X_vX_w]=\mu_v\mu_w.
 \end{array}}
\]
The edge bound is sharp for every \(n\ge2\), for example on \(K_n\). Consequently, the strict negative off-diagonal covariance entries identify precisely the edges, the positive entries precisely the nonedges inside connected components, and the zero entries precisely pairs in different connected components.

**Sharp hereditary boundary.** A finite simple graph \(G\) is a cograph if and only if, for **every nonempty** induced subgraph \(H\) of \(G\), the negative off-diagonal covariance entries of the uniform measure on \(P_H\) are exactly the edges of \(H\). The necessity is witnessed by the four-vertex induced path: for the path \(1-2-3-4\), its nonadjacent endpoints satisfy
\[
 \boxed{\operatorname{Cov}_{P_{P_4}}(X_1,X_4)=-\frac{11}{3750}<0.}
\]

## Assumptions and scope

The graph is finite, simple, and labeled; there are no weights. Coordinates are the canonical \(0/1\) stable-set indicator coordinates. Volumes are ordinary Euclidean coordinate volumes and probability distributions are uniform on the full-dimensional interior, not uniform on vertices or sampled stable sets. Pairwise covariance statements concern different coordinates. The hereditary converse requires the covariance-sign property of *all induced subgraphs*, not of the original graph alone.

## Proof

**1. Stable-set operations.** A stable set of \(A\sqcup B\) is an arbitrary union of a stable set from \(A\) and one from \(B\). Hence \(P_{A\sqcup B}=P_A\times P_B\) in orthogonal coordinate blocks. A stable set of the join \(A\vee B\) lies entirely in one of its two blocks. Since both stable-set polytopes contain the origin,
\[
 P_{A\vee B}=\operatorname{conv}((P_A\times\{0\})\cup(\{0\}\times P_B)).
\]

**2. The free-sum integration lemma.** More generally, let \(C\subset\mathbb R^a\) and \(D\subset\mathbb R^b\) be full-dimensional convex bodies containing the origin, and let \(K\) be the convex hull of their embeddings in complementary coordinate spaces. Denote their Minkowski gauges by \(p_C,p_D\). Then
\[
 K=\{(x,y):p_C(x)+p_D(y)\le1\}.
\]
Radial scaling gives \(\operatorname{Vol}(tC)=t^a\operatorname{Vol}(C)\), so in a uniform sample from \(C\), the gauge radius has distribution \(\operatorname{Beta}(a,1)\), independently of the normalized boundary direction under cone measure. The same holds for \(D\). In a uniform sample from \(K\), the two radial gauges and the unused slack have joint distribution \(\operatorname{Dirichlet}(a,b,1)\), independently of the two cone directions. In particular, if \(p=|\alpha_A|\) and \(q=|\alpha_B|\),
\[
 \mathbb E_K[X^{\alpha_A}Y^{\alpha_B}]
 =\frac{(a)_p(b)_q}{(a+b+1)_{p+q}}
 \frac{a+p}{a}M_C(\alpha_A)\frac{b+q}{b}M_D(\alpha_B).
\]
The identity \((a)_p(a+p)/a=(a+1)_p\) gives the stated join-moment formula, also when either degree is zero. Integrating the radial density over the simplex of allowed gauges yields
\[
 \frac{\operatorname{Vol}(K)}{\operatorname{Vol}(C)\operatorname{Vol}(D)}
 =ab\int_{t,s\ge0,\,t+s\le1}t^{a-1}s^{b-1}\,dt\,ds
 =\frac{a!b!}{(a+b)!}.
\]
All inputs are full-dimensional and all integer dimensions here are strictly positive, so the radial formulas and denominators are valid. The leaf, product, and join cases prove the all-degree recursion by induction over the cotree.

**3. An invariant controlling covariance signs.** For distinct vertices define
\[
 R_{vw}(G)=\frac{\mathbb E_G[X_vX_w]}{\mu_v\mu_w}.
\]
All first moments are positive. At a disjoint union, an internal pair keeps its \(R\), while a pair across the two factors has \(R=1\). At a join with factor sizes \(a,b\) and total \(N=a+b\), a cross-factor pair has exactly
\[
 R_{vw}(A\vee B)=\frac{N+1}{N+2}.
\]
For two vertices within the \(A\) block, the moment formula gives
\[
 R_{vw}(A\vee B)=\frac{a+2}{a+1}\frac{N+1}{N+2}R_{vw}(A).
\]
The multiplier is strictly greater than one because \(N>a\), and it maps the sharp edge threshold \((a+1)/(a+2)\) to \((N+1)/(N+2)\). The symmetric formula holds for the \(B\) block.

Inductively, every edge in a cograph of order \(n\) has \(R\le(n+1)/(n+2)\); this is true for a join-crossing edge with equality, preserved at joins within a factor, and preserved (strictly if the order increases) at disjoint unions. Every nonedge has \(R\ge1\): a cross-union pair has \(R=1\), internal nonedges preserve this at unions, and the strict multiplier makes the ratio \(>1\) at any join above the pair. Therefore a nonedge has \(R=1\) exactly when its vertices belong to different final connected components; otherwise a join appears above the pair's least common cotree ancestor and forces \(R>1\). This proves all sharp signs and the edge bound. Since \(K_n\) is formed by joins of singletons, its pairs attain the edge threshold.

**4. Exact forbidden-path boundary.** The stable-set polytope of \(P_4\) is described by nonnegative coordinates and the three path-edge inequalities. Put \(s=x_2,t=x_3\). The domain of \((s,t)\) is the triangle \(s,t\ge0,\;s+t\le1\); conditionally, \(X_1\) and \(X_4\) are independent uniforms on \([0,1-s]\) and \([0,1-t]\). Their marginalizing weight is \((1-s)(1-t)\), whose integral is \(5/24\). Direct polynomial integration gives \(\mathbb E s=\mathbb E t=7/25\) and \(\mathbb E st=1/15\). Thus
\[
 \operatorname{Cov}(X_1,X_4)
 =\frac14\left(\frac1{15}-\frac{49}{625}\right)
 =-\frac{11}{3750}.
\]
But vertices \(1,4\) are nonadjacent. Every noncograph contains an induced \(P_4\), whereas every induced subgraph of a cograph remains a cograph. Therefore the sign characterization on **all induced subgraphs** holds if and only if the graph is a cograph.

## Verification

The accompanying standalone `checker.py` constructs stable-set indicator vertices independently of the cotree recursion, triangulates their convex hulls, and integrates the simplices by exact integer determinant and rational moment formulas. It compares volumes, first and second moments, the sharp edge bound, covariance signs, and cubic moments, and independently integrates the \(P_4\) boundary example. The tested finite configurations support but do not replace the induction and integral proof. Run `python checker.py` in an environment with Python, NumPy, SciPy, and SymPy.

## Relationship to prior work

The graph-theoretic cograph decomposition and induced-\(P_4\) characterization are standard; a modern primary account is Singh's *Cographs and 1-sums*. The standard stable-set indicator-polytope realization is given explicitly by Aliniaeifard–Benedetti–Bergeron–Li–Saliola, *Stable set polytopes and their 1-skeleta*. General rational formulas for moments of uniformly measured polytopes are developed by Kohn–Shapiro–Sturmfels, *Moment Varieties of Measures on Polytopes*. These sources provide background definitions or generic moment techniques; their examined results do not give the present cotree all-degree recursion or sharp hereditary covariance-sign characterization. Previously obtained moment formulas for complete multipartite stable-set polytopes follow as a restricted special case: those graphs are joins of independent sets. The new theorem covers arbitrary alternating cotrees, including cographs with induced four-cycles that are not complete multipartite graphs.

## Limitations

This is a self-contained analytic result for canonical full-dimensional stable-set polytopes of finite cographs. The negative-edge implication and nonedge-sign classification are not claimed for all graphs: already the induced \(P_4\) exhibits a negative covariance at a nonedge. The hereditary converse does not assert that a single covariance-sign matrix characterizes cographs without considering induced subgraphs. The proof establishes no result about uniform random stable sets (vertex measure), arbitrary affine images, or weighted graph variants. Historical priority of the combined recursion and sign theorem remains provisional pending independent literature review.

## References

1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (first posted 2018-04-02; examined revised manuscript), https://arxiv.org/abs/1804.00360.
2. J. Singh, *Cographs and 1-sums*, arXiv:2210.04139 (first posted 2022-10-09), https://arxiv.org/abs/2210.04139.
3. K. Kohn, B. Shapiro, B. Sturmfels, *Moment Varieties of Measures on Polytopes*, arXiv:1807.10258 (first posted 2018-07-26), https://arxiv.org/abs/1807.10258.
