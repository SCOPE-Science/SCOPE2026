# A sharp uniform projector bound and an exact bipartite edge-deficit formula on metric graphs

## Finding

Let \(G=(V,E)\) be any finite connected undirected loopless graph with at least one edge; parallel edges are permitted. Represent each edge \(e\) as an interval of any positive geometric length, and equip it with a positive *constant* density having total edge mass \(w_e>0\). Each vertex \(i\) may additionally carry an atom of mass \(\alpha_i\geq0\). Write \(\mu\) for the resulting finite measure and \(S(G)\) for the continuous real functions that are affine on each edge. Let \(P:L^2(G,\mu)\to S(G)\) be the orthogonal projector, regarded also as an operator on \(L^\infty(G,\mu)\).

**Uniform sharp bound.** Every such projector satisfies
\[
  1\leq\|P\|_{L^\infty\to L^\infty}<3,
  \qquad \sup_{G,\,w,\,\alpha}\|P\|_{L^\infty\to L^\infty}=3.
\]
The strict inequality is for each *fixed* finite connected positive-edge graph; the supremum is not attained by a finite graph. The constant is sharp even without vertex atoms and when \(G\) is a path.

**Exact bipartite deficit.** Let \(d_i=\sum_{e\ni i}w_e\), and form the symmetric nodal mass matrix \(M\) with
\[
 M_{ii}=\alpha_i+\frac{d_i}{3},\qquad
 M_{ij}=\frac16\sum_{e\text{ joining }i,j}w_e\quad(i\ne j).
\]
When \(G\) is bipartite, set \(a_{vi}=|(M^{-1})_{vi}|\), which is strictly positive for every \(v,i\). The exact norm is
\[
\boxed{\displaystyle
 \|P\|_{L^\infty\to L^\infty}
 =3-\min_{v\in V}\left\{
 2\sum_{i\in V}\alpha_i a_{vi}
 +\sum_{e=\{i,j\}\in E}
  w_e\frac{a_{vi}a_{vj}}{a_{vi}+a_{vj}}
 \right\}. }
\]
This is a strictly positive, computable deficit at each vertex: one contribution comes from atoms and the other from sign cancellation across edges. In particular, the norming evaluation points are exactly the vertices attaining the minimum displayed deficit. At a norming vertex \(v\), all norm-attaining unit inputs are, up to a global sign and arbitrary values on a null set or where the kernel vanishes, the signs of the reproducing kernel \(K_v\).

**Quantitative sharpness witness.** For the path on vertices \(0,\ldots,n-1\), with \(n\geq3\), no atoms, and successive edge masses \(1,r,r^2,\ldots,r^{n-2}\), let \(\Lambda_0(n,r)\) be its kernel \(L^1\)-norm at the endpoint \(0\). Then
\[
 \boxed{\displaystyle \lim_{r\to\infty}\Lambda_0(n,r)
    =3-\frac{2^{4-n}}{3}. }
\]
Taking \(n\to\infty\) proves sharpness of the global bound. No assertion about the other norming vertices on each finite path is needed.

## Assumptions and scope

The graph is finite, connected, has no loops and has at least two vertices. Edges may have arbitrary positive lengths and arbitrary positive densities that are constant along each edge; only their total masses enter the formula. Vertex atoms are nonnegative and are included in \(L^2(G,\mu)\) and \(L^\infty(G,\mu)\). All functions and projections are real-valued. Positivity of all edge masses and connectedness ensure that the nodal mass matrix is invertible and that the edgewise affine range has dimension \(|V|\). Normalizing \(\mu\) to a probability does not change \(P\), its norm, or the formula. The exact deficit requires bipartiteness, while the universal sharp upper bound does not.

Write \(\varphi_i\) for the usual continuous nodal hat function, equal to one at vertex \(i\), zero at other vertices and affine on every edge. The arclength coordinate on an edge is rescaled to \([0,1]\) when evaluating elementary integrals. Define \(W_{ij}=\sum_{e:i\leftrightarrow j}w_e\) for \(i\ne j\), \(W_{ii}=0\), and \(D=\operatorname{diag}(d_i)\). Denote the vector of atom masses by \(\alpha\). Because all \(d_i>0\), the finite inverses below exist.

## Proof

### 1. Gram matrix, kernels, and reduction to vertices

On an edge \(e=\{i,j\}\) with mass \(w_e\), the two active hat functions are \(1-t\) and \(t\). Consequently, \(\int_e\varphi_i^2\,d\mu=w_e/3\), \(\int_e\varphi_i\varphi_j\,d\mu=w_e/6\), and \(\int_e\varphi_i\,d\mu=w_e/2\). An atom at \(i\) adds \(\alpha_i\) to the diagonal and to the hat-function integral. Thus
\[
 M=\operatorname{diag}(\alpha)+\frac{2D+W}{6},\qquad
 q_i:=\int_G\varphi_i\,d\mu=\alpha_i+\frac{d_i}{2}.
\]
The matrix \(M\) is symmetric positive definite because the hat functions are linearly independent in \(L^2(G,\mu)\). The orthogonal projector has the kernel
\[
 K_x(y)=\sum_{i,j\in V}\varphi_i(x)(M^{-1})_{ij}\varphi_j(y),
 \qquad Pf(x)=\int_G K_x(y)f(y)\,d\mu(y).
\]
Its operator norm is \(\sup_x\int_G|K_x(y)|\,d\mu(y)\): the upper bound is Hölder's inequality, while the lower bound is obtained by choosing the sign of the fixed kernel. For fixed \(y\), \(K_x(y)\) is affine in \(x\) on each edge, hence \(x\mapsto\int|K_x(y)|d\mu(y)\) is convex on each edge. Therefore its maximum occurs at a vertex. Write
\[
 \Lambda_v:=\int_G|K_v(y)|\,d\mu(y),\qquad \|P\|=\max_{v\in V}\Lambda_v.
\]
For all \(v\), the triangle inequality for the hat functions gives
\[
 \Lambda_v\leq\sum_{j\in V}|(M^{-1})_{vj}|q_j.
\]

### 2. A dimension-free majorant

Define the symmetric comparison matrix
\[
 B:=\operatorname{diag}(\alpha)+\frac{2D-W}{6}.
\]
Let \(A:=\operatorname{diag}(\alpha_i+d_i/3)\) and \(C:=W/6\). Then \(M=A+C\), \(B=A-C\), and the row sums of \(A^{-1}C\) are at most \(1/2\). In particular, both Neumann series converge absolutely and entrywise comparison yields
\[
 |M^{-1}|\leq B^{-1}=\sum_{k=0}^{\infty}(A^{-1}C)^kA^{-1}.
\]
The matrix \(B^{-1}\) has strictly positive entries: its convergent expansion is nonnegative, and connectedness supplies a positive matrix-walk contribution between every pair of vertices. Since
\[
 B\mathbf1=\alpha+\frac16D\mathbf1,
 \qquad q=3B\mathbf1-2\alpha,
\]
we obtain, componentwise,
\[
 \Lambda\leq |M^{-1}|q\leq B^{-1}q
 =3\mathbf1-2B^{-1}\alpha\leq3\mathbf1.
\]
If some vertex atom is positive, the inequality is strict at every vertex because \(B^{-1}>0\). If there are no vertex atoms but the graph is nonbipartite, its connectedness and an odd cycle imply that for every ordered vertex pair there are walks of both parities. In the alternating Neumann expansion of \(M^{-1}\), both parity subseries then have strictly positive entries, so the entrywise comparison \(|M^{-1}|<B^{-1}\) is strict, whence \(\Lambda_v<3\). The bipartite atom-free case is treated next and is also strict. Since \(P\mathbf1=\mathbf1\), its norm is at least one.

### 3. Bipartite sign pattern and exact edge cancellation

Suppose \(G\) is bipartite, with a diagonal sign matrix \(S=\operatorname{diag}(\sigma_i)\), \(\sigma_i=\pm1\), whose signs alternate across edges. Then \(SMS=B\), so
\[
 M^{-1}=SB^{-1}S,
 \qquad |(M^{-1})_{vi}|=(B^{-1})_{vi}=a_{vi}>0.
\]
In particular, the nodal values of \(K_v\) have opposite signs across every edge. For positive \(a,b\), direct integration gives
\[
 \int_0^1|(1-t)a-tb|\,dt
 =\frac{a^2+b^2}{2(a+b)}
 =\frac{a+b}{2}-\frac{ab}{a+b}.
\]
Using this on each edge and including vertex atoms without cancellation gives
\[
 \Lambda_v
 =\sum_i\alpha_i a_{vi}
 +\sum_{e=\{i,j\}}w_e\frac{a_{vi}+a_{vj}}2
 -\sum_{e=\{i,j\}}w_e\frac{a_{vi}a_{vj}}{a_{vi}+a_{vj}}.
\]
The first two sums equal \(\sum_i a_{vi}q_i=(B^{-1}q)_v=3-2\sum_i\alpha_i a_{vi}\). This yields
\[
 \Lambda_v=3-2\sum_i\alpha_i a_{vi}
 -\sum_{e=\{i,j\}}w_e\frac{a_{vi}a_{vj}}{a_{vi}+a_{vj}}.
\]
Every edge term is strictly positive. Maximizing over \(v\) proves the claimed deficit, strictness, and the norming-vertex characterization. Equality in the \(L^\infty\)-to-pointwise Hölder inequality yields the asserted sign-kernel description of unit inputs that attain the norm.

### 4. Exact geometric-path asymptotics

For a path on \(n\geq3\) vertices numbered \(0,\ldots,n-1\), set \(w_{\{j,j+1\}}=r^j\) with \(r>1\), and omit atoms. Write \(a_j:=a_{0j}>0\). From \((2D-W)a=6e_0\), the first and last equations are
\[
 2a_0-a_1=6,\qquad a_{n-1}=a_{n-2}/2.
\]
All interior equations are
\[
 2(r^{j-1}+r^j)a_j-r^{j-1}a_{j-1}-r^ja_{j+1}=0.
\]
Set \(b_j=r^ja_j\) for \(0\leq j\leq n-2\). The equivalent finite linear system reads
\[
 2b_0-b_1/r=6,
\]
\[
 2(1+1/r)b_j-b_{j-1}-b_{j+1}/r=0
 \quad(1\leq j\leq n-3),
\]
\[
 (3/2+2/r)b_{n-2}-b_{n-3}=0.
\]
As \(r\to\infty\), its coefficient matrix tends to an invertible lower-triangular matrix. Hence the solutions converge, and forward substitution gives
\[
 b_j\longrightarrow\frac3{2^j}\quad(0\leq j\leq n-3),
 \qquad b_{n-2}\longrightarrow2^{4-n}.
\]
For every edge except the last, its contribution to the deficit at vertex \(0\) satisfies
\[
 0\leq r^j\frac{a_ja_{j+1}}{a_j+a_{j+1}}
 \leq r^ja_{j+1}=b_{j+1}/r\longrightarrow0
 \quad(0\leq j\leq n-3).
\]
The last-edge identity \(a_{n-1}=a_{n-2}/2\) makes its contribution exactly
\[
 r^{n-2}\frac{a_{n-2}a_{n-1}}{a_{n-2}+a_{n-1}}
 =\frac{b_{n-2}}3\longrightarrow\frac{2^{4-n}}3.
\]
The exact deficit formula thus proves \(\lim_{r\to\infty}\Lambda_0(n,r)=3-2^{4-n}/3\). Since \(\|P\|\geq\Lambda_0(n,r)\), first taking \(r\to\infty\) and then \(n\to\infty\) establishes the sharp universal supremum \(3\). There is no reliance on an exhaustive finite computation.

## Verification

The standalone file `verify_graph_projection.py` uses Python standard-library rational arithmetic and independently constructs the full nodal mass matrix and inverse. It checks the strict bound on 560 seeded connected graphs (263 bipartite), with rationally weighted edges and some vertex atoms, and checks the exact bipartite deficit row by row. It separately tests geometric paths on nine orders with three large rational length ratios, verifies their approach to the analytical endpoint limit, and checks the exact single-edge value \(5/3\). The script must be run from the same directory with `python verify_graph_projection.py`.

These checks are finite consistency tests; the statements for all finite graphs and arbitrarily large path orders are established by the preceding analytical arguments. In particular, no finite test is used as evidence of noncoverage in the literature.

## Relationship to prior work

The sharp interval bound \(3\) for ordinary degree-one spline least-squares projections predates this result. Kayumov's 2004 preprint discusses the Ciesielski upper bound and the Oskolkov sharpness argument in the interval setting, while extending projection estimates to second-order \(L\)-splines. Oswald's 2006 preprint expressly contrasts one-dimensional uniform boundedness with unbounded norms for increasingly distorted triangulations in dimensions at least two. These works motivate asking whether arbitrary branching and cycles in a one-dimensional metric graph behave like a stable interval or an unstable planar mesh. The finding here addresses arbitrary finite connected metric graphs and adds a bipartite graph-specific formula with explicit atom and edge penalties; it does not rebrand the pre-existing interval constant as a new fact.

Hangelbroek, Narcowich, Sun, and Ward (2010) study uniformly bounded least-squares projectors for local stable kernel bases on smooth compact manifolds with quasiuniform centers; the present family permits arbitrary graph connectivity, arbitrary edge-mass ratios, and vertex atoms, with no mesh-ratio hypothesis. Boman's 2006 paper concerns weighted \(L^p\) bounds for finite elements, but a full text was unavailable in this inspection; possible stronger literature coverage remains a real originality risk. Earlier isolated exact graph-spline norm calculations for particular complete multipartite, tripartite, and subdivided-star graphs do not imply the graph-independent sharp bound or the bipartite defect identity. An indexed-search match or a failure to find one is not proof of novelty.

## Limitations

The result is for real degree-one edgewise-affine orthogonal projections and positive constant edge densities. Arbitrary nonconstant densities on individual edges, higher-degree splines, nonlinear projections, and a sharp graph-specific formula for nonbipartite graphs are not addressed. The global bound is sharp only as a supremum over graph families and edge weights; no fixed finite connected graph attains three. The exact bipartite formula is constructive but requires the finite inverse mass matrix. A relevant 2006 finite-element article was available only through bibliographic metadata and abstract, and independently established or unindexed graph-network formulations could reduce the originality of the result. No independent mathematical audit has been performed.

## References

1. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first publicly posted 2004-08-30. The interval theorem and its history are discussed in the abstract and introduction: https://arxiv.org/abs/math/0408418 .
2. P. Oswald, *A counterexample concerning the \(L^2\)-projector onto linear spline spaces*, arXiv:math/0611573, first publicly posted 2006-11-19. The introduction, mass-matrix analysis, and proof of the higher-dimensional counterexample were inspected: https://arxiv.org/pdf/math/0611573 .
3. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424, first publicly posted 2010-05-13. Introduction and Theorem 5.1 were inspected: https://arxiv.org/pdf/1005.2424 .
4. M. Boman, *Estimates for the \(L^2\)-projection onto continuous finite element spaces in a weighted \(L^p\)-norm*, BIT Numerical Mathematics 46 (2006), 249–260, DOI:10.1007/s10543-006-0062-3. Abstract and bibliographic metadata only.
