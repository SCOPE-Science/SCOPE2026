# Sharp endpoint norms of complete multipartite electrical gradient projections

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite, simple, unweighted complete multipartite graph, with \(r\ge2\), positive integer part sizes and \(N=\sum_{i=1}^r n_i\ge2\). Give its edges arbitrary orientations. Let \(B:\mathbb R^V\to\mathbb R^E\) be the signed edge-gradient matrix, \(L=B^{\mathsf T}B\), and
\[
P=BL^+B^{\mathsf T},
\]
the Euclidean orthogonal projection of edge fields onto gradient fields. Define, for \(1\le s\le N-1\),
\[
h_N(s)=\frac{N^2-2N-s^2+2}{N(N-s)}.
\]
The exact endpoint norms are
\[
\boxed{\|P\|_{\ell_\infty(E)\to\ell_\infty(E)}
=\|P\|_{\ell_1(E)\to\ell_1(E)}
=\max_{1\le i<j\le r}\bigl(h_N(n_i)+h_N(n_j)\bigr).}
\]
In particular, the sharp maximum over all complete multipartite graphs with \(N\) vertices is
\[
\boxed{\mathcal M_N=
\begin{cases}
1,&N=2,\\
\frac43,&N=3,\\
\frac32,&N=4,\\
\frac{26}{15},&N=5,\\
3-\frac{8(N-1)}{N^2},&N\ge6\text{ even},\\
3-\frac8{N+1},&N\ge7\text{ odd}.
\end{cases}}
\]
Up to graph isomorphism, maximizers are \(K_{1,1}\) for \(N=2\); \(K_{1,1,1}\) for \(N=3\); \(K_{1,1,1,1}\), \(K_{2,1,1}\) and \(K_{2,2}\) for \(N=4\); \(K_{2,2,1}\) for \(N=5\); \(K_{3,4}\) and \(K_{3,3,1}\) for \(N=7\); and the balanced complete bipartite graph \(K_{\lfloor N/2\rfloor,\lceil N/2\rceil}\) alone in every other case \(N\ge6\). Thus \(\|P\|<3\) always, and the constant \(3\) cannot be lowered uniformly over this graph family.

## Assumptions and scope
The vertex space and edge space are real, with counting-measure Euclidean inner products defining the pseudoinverse and the orthogonal projection. The endpoint operator norms use the ordinary maximum absolute edge coordinate and sum of absolute edge coordinates; they do not use the Euclidean norm, for which \(\|P\|_2=1\). Every undirected edge occurs exactly once. Orientation changes conjugate \(P\) by a diagonal sign matrix and do not alter these norms. All parts are nonempty, and at least two parts are present; in particular, \(G\) is connected. The claim holds for every allowed part size and every \(N\ge2\).

## Proof
**1. A dipole-potential formula.** Fix an edge \(e=uv\) with \(u\) in a part \(A\) of size \(a\), and \(v\) in a different part \(C\) of size \(b\). Set
\[
\alpha=\frac1{N(N-a)},\qquad
\beta=\frac1{N(N-b)}.
\]
After choosing the sign of the source dipole \(\delta_u-\delta_v\), define the vertex potential
\[
\phi(x)=
\begin{cases}
(N-1)\alpha,&x=u,\\
-\alpha,&x\in A\setminus\{u\},\\
-(N-1)\beta,&x=v,\\
\beta,&x\in C\setminus\{v\},\\
0,&x\notin A\cup C.
\end{cases}
\]
Its sum over \(A\) is \(1/N\), its sum over \(C\) is \(-1/N\), and its total sum is zero. For a vertex \(x\) belonging to a part \(D\) of size \(d\), the Laplacian identity is
\[
(L\phi)(x)=(N-d)\phi(x)+\sum_{y\in D}\phi(y),
\]
because the total sum is zero. Substitution gives \(L\phi=\delta_u-\delta_v\). By mean-zero uniqueness, \(\phi=L^+(\delta_u-\delta_v)\).

**2. Absolute transfer-current row sum.** The \(e\)-row of \(P\), up to orientation signs, consists of the edge differences \(\phi(x)-\phi(y)\). All edges between parts other than \(A\) and \(C\) contribute zero. Set \(c=N-a-b\). Between \(A\) and \(C\), the four types of edges contribute respectively
\[
\begin{aligned}
& (N-1)(\alpha+\beta)&&\text{(the edge between }u\text{ and }v),\\
& (b-1)((N-1)\alpha-\beta)&&\text{(edges between }u\text{ and }C\setminus\{v\}),\\
& (a-1)((N-1)\beta-\alpha)&&\text{(edges between }A\setminus\{u\}\text{ and }v),\\
& (a-1)(b-1)(\alpha+\beta)&&\text{(remaining edges).}
\end{aligned}
\]
All displayed factors are nonnegative: for example, \((N-1)\alpha\ge\beta\) is equivalent to \((N-1)(N-b)\ge N-a\), which follows from \(N-b\ge a\ge1\). The edges meeting the other \(c\) vertices contribute
\[
c(N+a-2)\alpha+c(N+b-2)\beta.
\]
On collecting terms, the \(\alpha\)-coefficient becomes \(N^2-2N-a^2+2\), and the \(\beta\)-coefficient becomes \(N^2-2N-b^2+2\). Therefore the absolute row sum is
\[
\sum_{f\in E}|P_{ef}|=h_N(a)+h_N(b).
\]
The maximum absolute row sum is precisely the \(\ell_\infty\) operator norm. Since \(P\) is symmetric, its maximum absolute column sum (the \(\ell_1\) norm) is the same.

**3. Exact witnesses.** For any edge \(e\) maximizing that row sum, prescribe an edge input \(z\) by \(z_f=\operatorname{sgn}(P_{ef})\) when \(P_{ef}\ne0\), and choose arbitrary values in \([-1,1]\) otherwise. Then \(\|z\|_\infty=1\) and \(|(Pz)_e|=\sum_f|P_{ef}|\). Conversely, equality for a unit maximum-norm input requires, for at least one row maximizing the row sum, equality in every nonzero term of the triangle inequality; hence the signs of all its nonzero coordinates agree with, or all oppose, that row's signs. For \(\ell_1\), the unit vector supported on a maximizing edge yields equality by symmetry.

**4. Extremal graph structure.** For any two distinct parts of sizes \(a,b\), put \(c=N-a-b\ge0\) and \(p=ab\). Algebra yields
\[
\begin{aligned}
h_N(a)+h_N(b)
&=3-\frac cN-\frac{2(N-1)(N+c)}{N(Nc+p)}\\
&\le F_N(c):=3-\frac cN-\frac{8(N-1)}{N(N+c)},
\end{aligned}
\]
since \(p\le (N-c)^2/4\), with equality in this last bound only when \(a=b\). Also
\[
F_N'(c)=-\frac1N+\frac{8(N-1)}{N(N+c)^2}.
\]
For \(N\ge7\), this is negative on \(c\ge0\). When \(N\) is even, the balanced two-part graph has \(c=0\) and achieves \(F_N(0)=3-8(N-1)/N^2\); it uniquely maximizes for every even \(N\ge8\). For \(N=6\), \(F_6\) decreases on \(c\ge1\) and \(F_6(1)<F_6(0)\), so the same conclusion holds.

For odd \(N\ge7\), the balanced bipartite graph has \(c=0\) and \(p=(N^2-1)/4\), attaining \(3-8/(N+1)\). Every \(c\ge1\) obeys
\[
F_N(c)\le F_N(1)=3-\frac8{N+1}+\frac{7-N}{N(N+1)}.
\]
For \(N\ge9\), this is strictly smaller than the balanced bipartite value; for \(N=7\), equality occurs exactly at \(c=1\), \(a=b=3\), which forces the additional graph \(K_{3,3,1}\). Directly listing the integer partitions for \(N=2,3,4,5\) gives the stated exceptional finite cases. The displayed formulas imply \(\mathcal M_N<3\) for every finite \(N\), while \(\mathcal M_N\to3\) as \(N\to\infty\).

## Verification
The standalone `verify.py` constructs the projection through the inverse of the **grounded Laplacian**, not through the asserted dipole-potential formula. With exact rational arithmetic it compares 2,926 individual row sums and sign witnesses on 128 complete multipartite graphs of orders two through ten. It independently enumerates all integer partitions through order eighteen to check the graph-extremizer classification. Run `python3 verify.py` with SymPy available. The recorded output ends with `ALL_EXACT_MULTIPARTITE_HODGE_ENDPOINT_CHECKS_PASSED`. These are finite diagnostics; the proof above establishes all orders.

## Relationship to prior work
Brandes and Fleischer (2005) develop the Laplacian-potential formulation of electrical currents and current-flow centrality. Jiang, Lim, Yao and Ye (initial arXiv version November 7, 2008) develop the Euclidean graph-gradient projection for ranking flows. Schild, Rao and Srivastava (2017) study precisely the \(\ell_1\) length of edge-to-edge electrical flows and the absolute transfer-current matrix, proving general asymptotic upper bounds rather than an exact multipartite family formula. These works provide the established operator and its motivation, but the precise two-part-size row sum, all-partition extremal classification, and sharp universal limiting value here require the additional explicit calculations above. The bipartite subfamily is also the classical two-way additive matrix least-squares projection, which is an important equivalent formulation and a potential independent literature route to the same special-case constant.

## Limitations
All results here concern the standard Euclidean projection on the real edge space of *unweighted* complete multipartite graphs. They do not determine optimal projection constants among all projections, weighted-graph variants, nonlinear \(\ell_1\) regression, or graph families with missing interpart edges. The explicit endpoint formula is algebraically derivable from classical Laplacian methods and is not claimed to establish historical priority. An older formulation through additive-model projection norms or electrical-network current lengths may predate the comparison sources. Independent audit has not been performed.

## References
- U. Brandes and D. Fleischer, *Centrality Measures Based on Current Flow*, STACS 2005, LNCS 3404, pp. 533–544. https://doi.org/10.1007/978-3-540-31856-9_44 ; freely accessible author PDF: https://www.uni-konstanz.de/algo/publications/bf-cmbcf-05.pdf .
- X. Jiang, L.-H. Lim, Y. Yao and Y. Ye, *Statistical Ranking and Combinatorial Hodge Theory*, arXiv:0811.1067, first submitted November 7, 2008. https://arxiv.org/abs/0811.1067 .
- A. Schild, S. Rao and N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632, first submitted August 4, 2017. https://arxiv.org/abs/1708.01632 .
