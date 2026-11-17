# Pinching invariance of sharp mean-zero Sobolev constants for parallel-edge and rose metric graphs

## Finding
Let \(r\ge2\) and let \(L_1,\ldots,L_r>0\). The **parallel-edge graph** \(B\) has two distinct endpoints joined by \(r\) edges of lengths \(L_i\); the **rose graph** \(R\) is obtained from \(B\) by identifying its endpoints, producing \(r\) loops of the same lengths. Give both graphs ordinary arclength and continuous edgewise-\(H^1\) functions. Put
\[
T=\sum_{i=1}^r L_i,\qquad c=\sum_{i=1}^r L_i^{-1},\qquad C=\frac{\sum_{i=1}^rL_i^3}{12T^2},\qquad M=\max_i L_i.
\]
Despite the different vertex topology and cycle ranks, the sharp squared embedding constants coincide exactly:
\[
\boxed{\mathcal K(B)=\mathcal K(R)=C+\frac{M(T-M)}{4T}.}
\]
Here \(\mathcal K(G)\) is the smallest constant such that every real continuous edgewise-\(H^1\) function with \(\int_G f\,ds=0\) satisfies
\[
\|f\|_{L^\infty(G)}^2\le\mathcal K(G)\int_G|f'|^2\,ds.
\]
On the \(i\)-th edge or loop, parametrized by \(s\in[0,L_i]\), the **complete point-evaluation diagonals** are
\[
\begin{aligned}
Q_R(i,s)&=C+\left(\frac1{L_i}-\frac1T\right)s(L_i-s),\\
Q_B(i,s)&=Q_R(i,s)+\frac1c\left(\frac{s}{L_i}-\frac12\right)^2.
\end{aligned}
\]
Thus pinching strictly lowers individual squared evaluation norms away from the edge midpoints but **does not lower their maximum**. If \(r\ge3\), the norming points on both graphs are exactly the midpoints of all longest edges, and no other points. If \(r=2\), every point of \(B\) is norming (it is a circle of circumference \(T\)); on \(R\), exactly the two loop midpoints are norming. In this exceptional case both constants equal \(T/12\). Every nonzero function attaining the embedding inequality is a scalar multiple of the centered Kirchhoff Green representer of evaluation at one of these points. At every norming midpoint, the Green representers on the two graphs agree edge by edge.

## Assumptions and scope
Each edge is a genuine interval of positive length, all are oriented from the first endpoint to the second before pinching, and there are no vertex atoms or edge weights. The arclength integral is **unnormalized**, and the energy is \(\int_G|f'|^2\,ds\). The mean-zero energy space is Hilbert because the graphs are connected; the continuity of evaluation follows from one-dimensional trace estimates. The domain includes all real continuous edgewise-\(H^1\) functions, not only functions satisfying pointwise Kirchhoff derivative conditions. Those conditions arise for the evaluation representer. A self-loop is a circle whose two ends are identified at the rose hub. The result is for every integer \(r\ge2\), every ordered positive length vector and every point of both graphs.

## Proof
**1. Interval Green decomposition.** On \([0,L]\), the zero-endpoint Dirichlet energy reproducing kernel is
\[
D_L(s,t)=\min(s,t)-\frac{st}{L},\quad D_L(s,s)=\frac{s(L-s)}L,\quad
\int_0^L D_L(s,t)\,dt=\frac{s(L-s)}2,
\]
and \(\int_0^L\int_0^L D_L(s,t)\,ds\,dt=L^3/12\). These follow either by two integrations or by solving \(-u''=\delta_s\) with zero boundary values.

**2. Rose point evaluation.** A function on \(R\) has a unique representation \(f_i(t)=a+g_i(t)\), with \(g_i\in H_0^1(0,L_i)\). Its mean-zero condition forces \(a=-T^{-1}\sum_j\int g_j\), and its energy equals \(\sum_j\int|g_j'|^2\). Evaluation at \((i,s)\) is therefore \(g_i(s)-T^{-1}\sum_j\int g_j\). Applying the interval Green identities to the squared norm of this functional gives precisely
\[
Q_R(i,s)=\frac{s(L_i-s)}{L_i}-\frac{s(L_i-s)}T+C.
\]
For later reference its centered reproducing kernel is explicitly
\[
G^R_{(i,s),j}(t)=C-\frac{s(L_i-s)}{2T}+\frac{t(t-L_j)}{2T}+\mathbf1_{j=i}D_{L_i}(t,s).
\]
This function has zero total integral and satisfies \(\int (G^R_{(i,s)})'f'=f_i(s)\) for every mean-zero \(f\) on \(R\).

**3. Parallel-edge point evaluation.** Every function on \(B\) has a unique orthogonal energy decomposition
\[
f_j(t)=m+d\left(\frac{t}{L_j}-\frac12\right)+g_j(t),\qquad g_j\in H_0^1(0,L_j),
\]
with common endpoint values \(m-d/2\) and \(m+d/2\), and energy
\[
\int_B|f'|^2=cd^2+\sum_j\int_0^{L_j}|g_j'|^2.
\]
Since the linear term has zero integral on every edge, the mean-zero condition again says \(m=-T^{-1}\sum_j\int g_j\). Evaluation at \((i,s)\) is the rose functional from step 2 plus \(d(s/L_i-1/2)\), in a one-dimensional energy direction orthogonal to all \(g_j\). The squared norm is therefore
\[
Q_B(i,s)=Q_R(i,s)+c^{-1}(s/L_i-1/2)^2.
\]
The explicit parallel-edge Green representer is
\[
G^B_{(i,s),j}(t)=G^R_{(i,s),j}(t)+\frac{s/L_i-1/2}{c}\left(\frac{t}{L_j}-\frac12\right).
\]
The additional mode vanishes exactly when the observed point is an edge midpoint, proving equality of both representers there.

**4. All pointwise maxima.** Write \(z=s(L_i-s)\). Because \((s/L_i-1/2)^2=1/4-z/L_i^2\),
\[
Q_B(i,s)=C+\frac1{4c}+\beta_i z,\quad
\beta_i=\frac1{L_i}-\frac1T-\frac1{cL_i^2}.
\]
Set \(T_i=T-L_i\) and \(c_i=c-L_i^{-1}\). Direct simplification gives
\[
\beta_i=\frac{T_ic_i-1}{T(1+L_ic_i)}.
\]
For \(r=2\), \(T_ic_i=1\), so \(Q_B\) is constant along the entire circular graph. For \(r\ge3\), Cauchy--Schwarz gives \(T_ic_i\ge(r-1)^2>1\), so \(\beta_i>0\) and the **unique** maximizer on each parallel edge is its midpoint. On the rose, \(1/L_i-1/T>0\) for every \(r\ge2\), and each loop also has its unique midpoint maximum. At the midpoint both diagonal values coincide and equal
\[
Q_B(i,L_i/2)=Q_R(i,L_i/2)=C+\frac{L_i(T-L_i)}{4T}.
\]
For any indices \(i,j\),
\[
L_i(T-L_i)-L_j(T-L_j)=(L_i-L_j)(T-L_i-L_j).
\]
When \(r\ge3\), the second factor is strictly positive. Thus the midpoint maximum strictly increases with edge length; only longest edges can be global norming points. When \(r=2\), the midpoint values coincide independently of lengths, and the above constant simplifies to \(T/12\). This proves the formula and classification in all cases, including both shared vertices and every interior point.

**5. Sharpness and equality functions.** In each mean-zero energy Hilbert space, the point-evaluation representer \(G_x\) has \(G_x(x)=\int|G_x'|^2=Q(x)>0\). Cauchy--Schwarz gives \(|f(x)|^2\le Q(x)\int|f'|^2\). Taking the maximum over all \(x\), and choosing \(f=G_x\) at any global maximizing point, proves both sharpness and attainment. Equality in Cauchy--Schwarz forces \(f\) to be a scalar multiple of such a representer, giving the claimed complete list. At a maximizing midpoint, \(s/L_i-1/2=0\), so the explicit formulas show that these equality functions agree under endpoint identification.

## Verification
The standalone file `banana_bouquet_green_check.py` independently constructs the nodal stiffness matrix of the metrized graph after inserting the observation point as a vertex, solves the exact rational Poisson system for \(-G''=\delta_x-ds/T\), and incorporates the edgewise quadratic particular solution. It does not use the claimed diagonal formulas in its solver. Across seven rational length families and both graph types, it verified \(230\) exact pointwise diagonal identities, global inequalities, and attainment at longest-edge midpoints. Run `python banana_bouquet_green_check.py` with Python and SymPy; it prints `ALL_BANANA_BOUQUET_SHARP_CONSTANT_CHECKS_PASSED`. Finite checks supplement, but are not a proof of, the quantified theorem. As a numerical exact-rational illustration, for three edges of lengths \((1,2,3)\) both squared constants equal \(11/24\), and the unique norming point is the midpoint of the edge of length \(3\).

## Relationship to prior work
Solomyak's 2002 preprint develops Sobolev embeddings and approximation on metric graphs with graph-independent sharp estimates; it does not give the particular mean-zero Green diagonal or this topology comparison. Baker and Faber (2004) establish the metrized-graph Laplacian and electrical-network framework used here. Cinkir (2011, Proposition 2.28 and Proposition 8.3) treats both rose and banana graphs for the **canonical-measure tau constant**, not for the present arclength-mean-zero sharp embedding. His formulas show that, for \(r\ge3\), the tau constants actually differ:
\[
\tau(R)=T/12,\qquad \tau(B)=T/12-(r-2)/(6c)<T/12,
\]
whereas the sharp Sobolev constants here are identical. The distinction between spectral/tau invariance and maximized arclength Green diagonals is part of the motivation. The point-evaluation formulas could also be obtained from general resistance identities, but the all-length pinching invariance, classification and identical norming kernels are the specific claim. The checked literature does not establish their priority conclusively.

## Limitations
No assertion is made for only one edge, nonconstant arclength densities, vertex atoms, complex-valued equality-case classification, higher-order energies, or additional boundary conditions. The prior literature may imply the identity through specialization of general graph Green formulas; absent a comprehensive bibliographic guarantee, originality is assessed against the inspected statements and implications. The separated pointwise diagonals depend on the graphs' different vertex identifications, so the comparison of a point \((i,s)\) is by its common edge coordinate, not by an isometry of graph metric spaces.

## References
1. M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, first public arXiv submission 23 June 2002, `arXiv:math/0206235`, https://arxiv.org/abs/math/0206235.
2. M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, first public arXiv submission 25 July 2004, `arXiv:math/0407428`, https://arxiv.org/abs/math/0407428.
3. Z. Cinkir, *The tau constant of a metrized graph and its behavior under graph operations*, *Electronic Journal of Combinatorics* **18** (2011), P81, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v18i1p81/pdf/.
