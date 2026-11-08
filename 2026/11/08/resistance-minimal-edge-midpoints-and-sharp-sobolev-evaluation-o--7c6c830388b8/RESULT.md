# Resistance-minimal edge midpoints and sharp Sobolev evaluation on vertex-transitive metric graphs

## Finding

Let \(G=(V,E)\) be any finite connected **simple vertex-transitive** graph, with \(N=|V|\ge3\), degree \(d\), and \(m=|E|=Nd/2\). Turn each edge into a unit-length interval, with ordinary unweighted arclength \(ds\). Let \(\mathscr H(G)\) consist of continuous real edgewise-\(H^1\) functions with \(\int_G f\,ds=0\), equipped with energy \(\int_G|f'|^2ds\). Define the squared sharp endpoint constant
\[
\mathcal K(G)=\sup_{0\ne f\in\mathscr H(G)}\frac{\|f\|_\infty^2}{\int_G|f'|^2\,ds}.
\]
Write \(L\) for the **discrete, unweighted** graph Laplacian, \(L^+\) for its Moore–Penrose inverse, and
\[
R_{uv}=(\mathbf e_u-\mathbf e_v)^\top L^+(\mathbf e_u-\mathbf e_v),\qquad
\mathrm{Kf}(G)=\sum_{\{u,v\}\subset V}R_{uv}.
\]
Here the last sum runs over unordered *distinct* vertex pairs. If \(x=(e,t)\) lies a fraction \(0\le t\le1\) along the unit edge \(e=uv\), then the **exact squared point-evaluation norm** is
\[
\boxed{\mathcal Q_G(e,t)=\frac{\mathrm{Kf}(G)}{N^2}+\frac{1}{12m}+
\left(1-\frac1m-R_{uv}\right)t(1-t).}\tag{1}
\]
In particular, if \(d\ge3\), set \(R_{\min}=\min_{uv\in E}R_{uv}\). Then
\[
\boxed{\mathcal K(G)=\frac{\mathrm{Kf}(G)}{N^2}+\frac{1}{12m}+
\frac14\left(1-\frac1m-R_{\min}\right).}\tag{2}
\]
The last parenthesis is **strictly positive**. Every maximizing evaluation point is *exactly the midpoint of an edge having minimum effective resistance*, and every such midpoint maximizes. There are no maximizing vertices or other interior points. Every nonzero extremizing function is a scalar multiple of the unique mean-zero Green representer of evaluation at one of these midpoints.

For \(d=2\), the graph is a cycle, (1) is independent of \(e,t\), and \(\mathcal K(G)=m/12\) with every point maximizing. The connected degree-one graph is \(K_2\): its sharp constant is \(1/3\), attained only at its endpoints. If all physical edge lengths are a common \(\ell>0\), multiply every displayed squared sharp constant and point-evaluation norm by \(\ell\).

**Hypercube consequence and a dimension-four peak.** Let \(Q_n\) denote the unit-edge metric graph of the \(n\)-dimensional Boolean cube. For all \(n\ge2\),
\[
\boxed{\mathcal K(Q_n)=\frac14-\frac{1}{2n}
+\frac{1}{2^{n+1}}\sum_{k=1}^n\frac{\binom nk}{k}
+\frac{1}{6n2^n}.}\tag{3}
\]
Also \(\mathcal K(Q_1)=1/3\). The largest constant over **every** integer dimension \(n\ge1\) is uniquely attained at \(n=4\):
\[
\boxed{\mathcal K(Q_4)=\frac{19}{48},\qquad \mathcal K(Q_3)=\frac{113}{288},\qquad \mathcal K(Q_{n+1})<\mathcal K(Q_n)\ (n\ge4).}\tag{4}
\]
For \(n\ge3\), all cube-edge midpoints, and only those points, maximize. The constants approach \(1/4\) from above, with
\[
\mathcal K(Q_n)=\frac14+\frac{1}{2n}+\frac1{n^2}+O(n^{-3}).\tag{5}
\]

**Non-edge-transitive selection.** In the circulant graph with vertex set \(\mathbb Z/7\mathbb Z\) and edges of increments \(\pm1\) and \(\pm2\), the two edge-orbit resistances are \(38/91\) and \(40/91\), respectively. Although the graph is vertex-transitive, its only norming evaluation points are the **seven midpoints of increment-one edges**. Its sharp constant is \(181/546\), and an increment-two edge midpoint has a sharp squared-norm deficit \(1/182\).

## Assumptions and scope

The graph is finite, connected, loopless, without parallel edges, vertex-transitive, and each combinatorial edge receives the same positive physical length. Graph automorphisms act on vertices; **edge transitivity is not assumed**. Functions are continuous at vertices, have ordinary one-dimensional \(H^1\) regularity along edges, have zero **arclength** integral, and are real. The derivative energy is the **unnormalized** sum of squared derivatives. The zero-mean condition eliminates the constant-function kernel. Equations (1)–(4) are sharp for every graph and dimension in their stated domains; no finite computation is needed to extend their quantifiers.

## Proof

**1. Orthogonal decomposition.** First set the common edge length to one. On every edge \(e=uv\) choose a coordinate \(s\in[0,1]\), and write a continuous function uniquely as
\[
f_e(s)=(1-s)b_u+sb_v+g_e(s),\qquad g_e\in H^1_0(0,1).
\]
Modulo an additive constant, choose the vertex vector \(b\) so that \(\sum_{v\in V}b_v=0\). Integration by parts, using \(g_e(0)=g_e(1)=0\), gives the **exact orthogonal energy splitting**
\[
\int_G|f'|^2ds=b^\top Lb+\sum_e\int_0^1|g'_e(s)|^2ds.
\]
Vertex transitivity implies regularity, so \(\sum_e\int_0^1((1-s)b_u+sb_v)\,ds=(d/2)\sum_v b_v=0\). Consequently the unique zero-arclength-mean representative is
\[
f_e(s)=(1-s)b_u+sb_v+g_e(s)-\frac1m\sum_{h\in E}\int_0^1g_h(r)\,dr.
\]
This realizes the zero-mean energy space as the orthogonal sum of the discrete zero-sum vertex-energy space and \(m\) independent Dirichlet interval spaces. Completeness follows from the finite direct sum and the usual completeness of \(H^1_0(0,1)\).

**2. Exact evaluation on one edge.** On the vertex-energy summand, the squared dual norm of \(b\mapsto(1-t)b_u+tb_v\) is
\[
((1-t)\mathbf e_u+t\mathbf e_v)^\top L^+((1-t)\mathbf e_u+t\mathbf e_v).
\]
Every diagonal entry of \(L^+\) is equal, since vertex automorphisms commute with \(L^+\). Furthermore \(\mathrm{Kf}(G)=N\operatorname{tr}(L^+)\), obtained by expanding the unordered pair resistance sum and using \(L^+\mathbf1=0\). Thus this vertex contribution is
\[
\frac{\mathrm{Kf}(G)}{N^2}-R_{uv}t(1-t).
\]
The Green kernel of \(H^1_0(0,1)\) for derivative energy is \(D(s,t)=\min(s,t)-st\). Its three relevant integrals are
\[
D(t,t)=t(1-t),\qquad \int_0^1D(t,s)\,ds=\frac{t(1-t)}2,
\qquad \int_0^1\!\int_0^1D(s,r)\,ds\,dr=\frac1{12}.
\]
The Dirichlet contribution to evaluation on edge \(e\) is \(g_e(t)-m^{-1}\sum_h\int g_h\), whose squared dual norm therefore equals
\[
\left(1-\frac1m\right)t(1-t)+\frac1{12m}.
\]
Adding the two orthogonal squared norms establishes (1), including both endpoints.

**3. A minimum-resistance edge must dominate.** The identity
\[
\sum_{uv\in E}R_{uv}=\operatorname{tr}(LL^+)=N-1
\]
is Foster's sum rule in this unit-edge setting: expand \(L=\sum_{uv\in E}(\mathbf e_u-\mathbf e_v)(\mathbf e_u-\mathbf e_v)^\top\). Averaging the coefficients \(c_e=1-1/m-R_{uv}\) in (1) gives
\[
\frac1m\sum_e c_e=1-\frac Nm=1-\frac2d.
\]
For \(d\ge3\), at least one \(c_e\) is strictly positive. Since \(t(1-t)\) uniquely maximizes at \(t=1/2\) and the coefficient is largest precisely when \(R_{uv}=R_{\min}\), (2) and its *complete* maximizing-location classification follow. Cauchy–Schwarz in the energy Hilbert space gives the sharp global embedding and the unique (up to scalar) evaluation Green representer equality cases. For \(d=2\) the graph is a cycle; elementary series-parallel resistance yields \(R_{uv}=(m-1)/m\) on every edge. The coefficient vanishes, and the standard circle mean-zero Green diagonal equals \(m/12\). For \(K_2\), the interval Green diagonal under the mean constraint is \(s^2-s+1/3\), with endpoint maximum \(1/3\). A uniform rescaling of all physical lengths by \(\ell\) multiplies this squared embedding constant by \(\ell\).

**4. Hypercube spectrum and strict dimension maximum.** The unit-edge \(n\)-cube has \(N=2^n\), \(m=n2^{n-1}\), and discrete Laplacian eigenvalues \(2k\) of multiplicity \(\binom nk\), for \(0\le k\le n\). The cube is edge-transitive, so Foster's rule gives \(R_{uv}=(N-1)/m\). Substituting into (2) yields (3) for \(n\ge3\); the same expression also evaluates to \(1/3\) at \(n=2\), where every point maximizes rather than only midpoints.

Set \(A_n=2^{-n-1}\sum_{k=1}^n\binom nk/k\). Pascal's identity and \(\binom{n+1}k-\binom nk=\binom n{k-1}\) yield the exact recursion
\[
A_{n+1}=\frac{A_n}{2}+\frac{1-2^{-(n+1)}}{2(n+1)}.
\]
For \(n\ge2\), equation (3) consequently gives
\[
\mathcal K(Q_{n+1})-\mathcal K(Q_n)
=\frac12\left(\frac1n-A_n\right)
-\frac1{3\cdot2^{n+1}}\left(\frac1n+\frac1{n+1}\right).
\]
The exact base is \(A_4=103/384>1/4\). If \(A_n>1/n\), the recursion implies \(A_{n+1}>1/(n+1)\), since \(2^{n+1}>n\). Hence the last display is strictly negative for all \(n\ge4\). Direct substitution gives \(\mathcal K(Q_1)=\mathcal K(Q_2)=1/3\), \(\mathcal K(Q_3)=113/288\), and \(\mathcal K(Q_4)=19/48=114/288\); these verify the unique maximum in (4). Finally, for \(X\sim\mathrm{Binomial}(n,1/2)\), \(A_n=\frac12\mathbb E[1_{X>0}/X]\). Expand \(1/X\) around \(n/2\) on \(X\ge n/4\), use \(\mathbb E(X-n/2)^2=n/4\), and bound the complementary binomial tail exponentially. This gives \(A_n=1/n+1/n^2+O(n^{-3})\), proving (5).

**5. An edge-orbit symmetry-breaking witness.** In \(C_7(1,2)\), solving the discrete unit-current Kirchhoff equations (or diagonalizing its circulant Laplacian) gives effective resistances \(R_1=38/91\) and \(R_2=40/91\) for increments one and two. The Kirchhoff index is \(126/13\). In (2) use \(N=7\), \(m=14\), and \(R_{\min}=38/91\), giving \(\mathcal K=181/546\). The two edge-midpoint evaluation norms differ by exactly \((R_2-R_1)/4=1/182\), so only the seven first-orbit midpoints maximize.

## Verification

The independent computational route in `verify.py` uses exact fractions and **does not substitute formula (1) into its continuum evaluator**. It inserts the observation point as a new vertex, solves a weighted discrete Kirchhoff system for the continuous Poisson load \(\delta_x-ds/m\), restores the exact quadratic curvature on each subedge, and subtracts the exact arclength mean. It compares those point-evaluation energies with a separate electrical resistance calculation. The executed test covered 565 exact pointwise comparisons on cycles, complete graphs, cubes, non-edge-transitive circulants, and prism graphs; it also checked the hypercube formulas and monotonicity algebra. The universal quantifiers are proved above and do not rely on this finite testing.

To replay, run `python3 verify.py` from the directory containing this document and the checker, using the Python standard library. In particular, the test prints the exact \(C_7(1,2)\) resistances and the exact sharp constant.

## Relationship to prior work

Baker and Faber's metrized-graph treatment provides the electrical-resistance framework, the \(j\)-function, and Foster's identity; those are **prior ingredients**, not claimed here as new. Liu–Cao–Pan–Elaiw calculate the discrete hypercube Kirchhoff index but do not derive the continuum arclength mean-zero point-evaluation norm, its edge-orbit optimizer classification, or the dimension-four maximum. Usman's compact metric-graph Sobolev paper addresses isoperimetric and Cheeger-type inequalities, not this sharp endpoint evaluation law. Earlier explicit Sobolev evaluations on particular graph families (including multipartite graphs, prisms, wheels, ladders and cacti) are special-family results and do not imply the assertion for *every* vertex-transitive graph, particularly the non-edge-transitive circulant witness. The contribution here is the universal resistance-minimization principle and its sharp hypercube classification, not the pre-existing resistance identity or spectrum.

## Limitations

The result is for **finite simple vertex-transitive, unit-edge** metric graphs (with a direct common-length rescaling), real functions, ordinary arclength mean, and first-order derivative energy. It does not cover arbitrary nonregular or only edge-transitive graphs, nonuniform edge lengths, additional vertex masses, complex-valued boundary conditions, or general \(L^p\) norms. An equivalent theorem might be implicit in older Green-function literature without being explicitly indexed; no claim of exhaustive bibliographic uniqueness is made. Independent mathematical auditing has not occurred.

## References

1. M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428, first submitted 2004-07-25, https://arxiv.org/abs/math/0407428 . See sections 5–7 for graph Laplacians, effective resistance, and Foster's theorem.
2. J. Liu, J. Cao, X.-F. Pan, and A. Elaiw, *The Kirchhoff Index of Hypercubes and Related Complex Networks*, *Discrete Dynamics in Nature and Society* (2013), article 543189, https://doi.org/10.1155/2013/543189 . See theorem 9 and section 3; first published 2013-12-12.
3. M. Usman, *Sobolev type inequalities for compact metric graphs*, *Journal of Inequalities and Applications* (2018), article 271, https://doi.org/10.1186/s13660-018-1872-y . See theorems 2.1, 2.3, and 4.3 for inequalities of a different type.
