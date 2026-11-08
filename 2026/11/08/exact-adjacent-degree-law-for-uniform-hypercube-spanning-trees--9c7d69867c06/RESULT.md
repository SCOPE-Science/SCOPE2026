# Exact adjacent-degree law for uniform hypercube spanning trees

## Finding
For every integer \(d\ge3\), let \(Q_d\) be the unit-conductance Boolean hypercube with vertex set \(\{0,1\}^d\). Let \(T\) be uniformly distributed among its spanning trees. Fix two adjacent vertices \(u,v\), and put \(D_u=\deg_T(u)\), \(D_v=\deg_T(v)\). Define
\[
q=2^{-d},\quad m=d-1,\quad p=\frac{2(1-q)}d,\quad c=\frac{1-p}{d-1},
\quad a=p-2c,\quad b=\frac{d-4+2(d+2)q}{d(d-1)(d-2)},
\]
\[
\beta=p-c=\frac{1-2q}{d-1},\qquad \delta=a-b=\frac{1-2dq}{(d-1)(d-2)},\qquad h=a+(d-2)b.
\]
For independent formal variables \(x,y\), set
\[
K_d=\begin{pmatrix}
p&mc&-mc\\
c&p+(m-1)c&h\\
-c&h&p+(m-1)c
\end{pmatrix},\qquad
Z=\operatorname{diag}(xy-1,x-1,y-1).
\]
**Theorem (exact bivariate probability-generating function).** For all \(d\ge3\),
\[
\boxed{\mathbb E[x^{D_u}y^{D_v}]=\det(I_3+K_dZ)\left((1+\beta(x-1))(1+\beta(y-1))-\delta^2(x-1)(y-1)\right)^{d-2}.}
\]
The determinant is only \(3\times3\), so the law at every dimension is specified by a cubic-size factor and a repeated quadratic factor. In particular, both marginals equal \(x(1+\beta(x-1))^{d-1}\). The exact covariance is
\[
\boxed{\operatorname{Cov}(D_u,D_v)=\frac{(1-2dq)(d-4+2(d+2)q)}{d(d-1)(d-2)}>0,}
\]
and \(d^2\operatorname{Cov}(D_u,D_v)\to1\). These consequences are part of the stated joint law, not separate novelty claims.

## Assumptions and scope
The graph is the finite unweighted undirected simple hypercube; the tree is sampled uniformly over *all* spanning trees, not from a random edge-order greedy process. Degrees count incident tree edges. Vertices \(u,v\) must be adjacent in the ambient cube, and \(d\ge3\); the displayed rational parameters are not specified at \(d=2\). The formula is an exact identity of bivariate polynomials, not just an asymptotic or a moment identity. All variables are ordinary formal polynomial indeterminates.

## Proof
Orient and label the \(2d-1\) distinct edges incident to either endpoint of a fixed cube edge as follows. Take \(u=0\), \(v=e_1\). Let \(s=(0,e_1)\), let \(U_i=(0,e_i)\) and \(V_i=(e_1,e_1+e_i)\) for \(2\le i\le d\), all edges oriented in the displayed direction. The standard transfer-current theorem says that their inclusion indicators form a determinantal process with matrix \(\mathcal K\), and, on assigning weights \(xy\) to \(s\), \(x\) to all \(U_i\) and \(y\) to all \(V_i\),
\[
\mathbb E[x^{D_u}y^{D_v}]=\det(I_{2d-1}+\mathcal K\operatorname{diag}(xy-1,(x-1)I_m,(y-1)I_m)). \tag{1}
\]
This identity also follows directly from the matrix-tree theorem applied to the weighted Laplacian, so it does not presume independence of incident edges.

For a coordinate edge \((z,z+e_i)\) oriented from its initial endpoint, the Walsh characters \(\chi_S(z)=(-1)^{\sum_{j\in S}z_j}\) diagonalize the cube Laplacian with eigenvalue \(2|S|\). Consequently, for two oriented coordinate edges in directions \(i,j\) based at \(z,w\),
\[
\mathcal K_{(z,i),(w,j)}=\frac2{2^d}\sum_{\substack{\varnothing\ne S\subseteq[d]\\i,j\in S}}\frac{\chi_S(z)\chi_S(w)}{|S|}.\tag{2}
\]
The formula includes \(i=j\) and is obtained by inserting the Walsh spectral expansion of the Moore–Penrose Laplacian inverse in the transfer-current bilinear form. Use \(1/k=\int_0^1 t^{k-1}\,dt\) to sum the finite subsets. The diagonal value is \(p=2(1-2^{-d})/d\). For distinct edges within either star the value is \(c\); between \(s\) and an edge \(U_i\) it is \(+c\), whereas between \(s\) and \(V_i\) it is \(-c\). The opposite-star entry \(\mathcal K_{U_i,V_j}\) equals \(a\) when \(i=j\) and \(b\) otherwise. These follow explicitly from
\[
p=2^{1-d}\int_0^1(1+t)^{d-1}\,dt,\quad
c=2^{1-d}\int_0^1t(1+t)^{d-2}\,dt,
\]
\[
a=2^{1-d}\int_0^1(1-t)(1+t)^{d-2}\,dt,\quad
b=2^{1-d}\int_0^1t(1-t)(1+t)^{d-3}\,dt.\tag{3}
\]
Elementary integration gives the stated rational forms, including \(a=p-2c\), \(\beta=p-c\), \(\delta=a-b\), and \(h=a+(m-1)b\). Hence the exact transfer kernel, in edge order \(s,U,V\), is
\[
\mathcal K=\begin{pmatrix}
p&c\mathbf1^\top&-c\mathbf1^\top\\
c\mathbf1&(p-c)I_m+cJ_m&(a-b)I_m+bJ_m\\
-c\mathbf1&(a-b)I_m+bJ_m&(p-c)I_m+cJ_m
\end{pmatrix}.\tag{4}
\]
Split each \(\mathbb R^m\) into its constant-vector line and its orthogonal \((m-1)\)-dimensional mean-zero subspace. On each of the \(m-1=d-2\) matching two-dimensional mean-zero modes the transfer matrix is \(\left(\begin{smallmatrix}\beta&\delta\\\delta&\beta\end{smallmatrix}\right)\). On the three-dimensional constant sector (the shared edge plus two star averages), its matrix is similar to the displayed rational matrix \(K_d\): using the unnormalized constant-star basis gives off-diagonal entries \(mc,c\) and \(-mc,-c\). The weight perturbation in (1) is scalar on each invariant sector and therefore respects this decomposition. Taking determinants proves the claimed factorization for every \(d\ge3\).

To check the marginals, set \(y=1\) and observe that the remaining star kernel has eigenvalues \(1\) once and \(\beta\) with multiplicity \(d-1\), because \(p+(d-1)c=1\). Thus the marginal pgf is \(x(1+\beta(x-1))^{d-1}\), and similarly for \(x=1\). For covariance, write the two degrees as the shared-edge indicator plus their respective \(d-1\) remaining edge indicators. The determinantal covariance formula for distinct edges is \(-\mathcal K_{e,f}^2\); inserting the four entry types yields
\[
\operatorname{Cov}(D_u,D_v)=p(1-p)-2(d-1)c^2-(d-1)a^2-(d-1)(d-2)b^2,
\]
which simplifies to the displayed rational expression. Positivity holds because \(2^d>2d\) when \(d\ge3\), and \(d-4+2(d+2)2^{-d}>0\) for \(d=3,4\) directly and for \(d\ge5\) immediately. Taking the leading \(d\to\infty\) coefficients proves the limit.

## Verification
The standalone `VERIFY.py` uses only the Python standard library. Running `python VERIFY.py` independently evaluates the full weighted matrix-tree determinant on \(Q_d\) for \(d=3,4,5\) and a range of integer weights, checks the complete enumeration of all \(384\) spanning trees of \(Q_3\) against the formula, and checks all transfer-kernel entry types by direct exact Walsh summation for \(3\le d\le10\). The run reported `VERIFY_OK 86 assertions; Q3 trees 384`. All comparisons use integer or rational arithmetic; they are finite consistency checks, not the proof of the all-dimensional identity, which rests on equations (1)–(4).

## Relationship to prior work
Aldous (1990, Proposition 9 and the cube example following it) addresses the **single-vertex degree** on highly symmetric graphs, including \(Q_d\), and provides a limiting Poisson degree theorem. Nachmias and Peres (first released 2020-11-17) establish the universal high-degree **one-root local weak limit**. Neither statement evaluates the finite-dimensional **joint degree polynomial of two prescribed adjacent ambient vertices**. The standard transfer-current determinantal theorem already provides an unevaluated determinant on any finite graph. Here the scientific assertion is its special **closed rational three-dimensional plus repeated two-dimensional factorization** for neighboring hypercube stars. Prior exact two-edge covariance formulas on \(Q_d\) determine second-order edge moments, not this full all-order joint degree generating function. This distinction matters: no novelty is asserted for the general determinant identity, individual-vertex marginal law or individual-edge correlation formulas.

## Limitations
The result concerns only adjacent ambient hypercube vertices and unit conductances; it does not give the corresponding finite law for nonadjacent vertices, weighted cubes or general high-degree graphs. Finite checker output is not a general proof. The literature comparison is a best-knowledge assessment, not a guarantee of historical priority. An independent mathematical audit has not been performed.

## References
1. D. J. Aldous, *The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees*, SIAM J. Discrete Math. 3 (1990), 450–465, Proposition 9 and subsequent cube example; https://doi.org/10.1137/0403039 ; accessible manuscript https://paperzz.com/doc/6940148/the-random-walk-construction-of-uniform-spanning-trees-and .
2. A. Nachmias and Y. Peres, *The local limit of uniform spanning trees*, arXiv:2011.08833 (initial 2020-11-17); https://arxiv.org/abs/2011.08833 .
3. E. Archer, A. Nachmias and M. Shalev, *The GHP scaling limit of uniform spanning trees in high dimensions*, arXiv:2112.01203 (initial 2021-12-02); https://arxiv.org/abs/2112.01203 .
4. R. Burton and R. Pemantle, *Local characteristics, entropy and limit theorems for spanning trees and domino tilings via transfer-impedances*, Ann. Probab. 21 (1993), 1329–1371; https://doi.org/10.1214/aop/1176989111 .
