# A sharp even-order Taylor positivity window for sparse-core clique joins

## Finding
Let \(H\) be any finite simple graph on \(m\ge1\) vertices, with maximum degree \(\Delta\). For an integer \(k\ge1\), form the unit-edge graph join \(G=K_k\vee H\) on \(n=k+m\) vertices and let \(L\) be its combinatorial Laplacian. For every even integer \(p\ge2\), put
\[
F_p(z)=\sum_{j=0}^{p}\frac{(-z)^j}{j!},
\]
and let \(\beta_p\) be the unique strictly positive real solution of \(F_p(\beta_p)=1\). If
\[
\boxed{\quad n\ge\beta_p(k+\Delta),\quad}
\]
then the completed order-\(p\) Taylor heat step has the **exact** entrywise-positivity window
\[
\boxed{F_p(hL)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad 0\le h\le\frac{\beta_p}{n}.}
\]
For every \(h>\beta_p/n\), all entries joining a vertex of the clique \(K_k\) to a vertex of \(H\) are strictly negative. At the endpoint, those entries are zero. Every valid step is row-stochastic, and at every positive valid step the entire \(H\)-by-\(H\) block is strictly positive.

The result includes **arbitrary** sparse residual graphs: paths, cycles, disjoint mixtures, and graphs with no nontrivial symmetry. In particular, all fan graphs \(K_1\vee P_m\) and wheel graphs \(K_1\vee C_m\) with \(m\ge8\) have the exact RK4 threshold \(\beta_4/(m+1)\), because \(\Delta=2\) and \(\beta_4<3\). This conclusion is not a statement about positivity of intermediate Runge--Kutta stages.

## Assumptions and scope
The graph \(H\) is unweighted, loopless, undirected, finite and simple; it need not be connected. The join \(G\) has every possible edge between the \(k\) clique vertices and the \(m\) vertices of \(H\), and all edges within \(K_k\). The inequality between matrices is entrywise. The function \(F_p\) is a scalar polynomial evaluated at the symmetric Laplacian through ordinary matrix substitution, including the entire final Taylor polynomial. No assertion is made about arbitrary weighted joins, odd orders, or joins that violate the displayed degree condition.

## Proof
**1. Scalar facts.** For each even \(p\), the Taylor remainder formula for the exponential shows \(F_p(z)>e^{-z}>0\) for every \(z>0\), and \(F_p(0)=1\). Also \(F_p''(z)=F_{p-2}(z)>0\), so \(F_p\) is strictly convex on the nonnegative half-line. Its derivative \(F_p'(z)=-F_{p-1}(z)\) is strictly increasing, starts at \(-1\), and tends to \(+\infty\). Consequently \(F_p\) first decreases and then increases to infinity, and \(F_p(z)\le1\) exactly for \(0\le z\le\beta_p\). For any integer \(q\ge0\), \(F_q(s)\ge0\) whenever \(0\le s\le1\): for even \(q\), positivity follows from the even Taylor remainder; for odd \(q\), pair consecutive terms after \(1-s\) into nonnegative differences \(s^{2j}/(2j)!-s^{2j+1}/(2j+1)!\).

**2. Exact join block decomposition.** Index the \(k\) clique vertices first. Write \(J_{a,b}\) for the all-ones matrix of size \(a\) by \(b\). Then
\[
L=\begin{pmatrix}
nI_k-J_{k,k}&-J_{k,m}\\
-J_{m,k}&kI_m+L_H
\end{pmatrix}.
\]
The vector constant on all \(n\) vertices has eigenvalue zero. The orthogonal subspace whose coordinates on \(H\) sum to zero is invariant, and the restricted operator there is \(kI_m+L_H\). The remaining \(k\)-dimensional subspace orthogonal to the global constant has eigenvalue \(n\). Therefore, for \(z=F_p(nh)\), the three blocks of \(F_p(hL)\) are exactly
\[
\begin{aligned}
T_{KK}&=z I_k+\frac{1-z}{n}J_{k,k},\\
T_{KH}&=\frac{1-z}{n}J_{k,m},\\
T_{HH}&=F_p\bigl(h(kI_m+L_H)\bigr)+q(h)J_{m,m},\\
q(h)&=\frac{m+kF_p(nh)-nF_p(kh)}{mn}.
\end{aligned}
\]
All of these identities also hold at \(h=0\).

**3. Positive rank-one correction.** Since \(kh=(k/n)(nh)+(m/n)0\), convexity of \(F_p\) and \(F_p(0)=1\) give
\[
F_p(kh)\le \frac{k}{n}F_p(nh)+\frac{m}{n},
\]
whence \(q(h)\ge0\) for all \(h\ge0\), with strict inequality for positive \(h\), because \(k,m>0\) and \(F_p\) is strictly convex.

**4. Positive core block within the claimed interval.** Let \(A_H\) denote the adjacency matrix of \(H\), let \(d_i\) be its vertex degrees, and set
\[
B=\Delta I_m-L_H=A_H+\operatorname{diag}(\Delta-d_i)\ge0.
\]
Write \(s=h(k+\Delta)\). The degree condition and \(h\le\beta_p/n\) imply \(0\le s\le1\). By polynomial Taylor expansion about \(s\), using \(F_p^{(j)}(s)=(-1)^jF_{p-j}(s)\),
\[
F_p\bigl(h(kI_m+L_H)\bigr)=F_p(sI_m-hB)
=\sum_{j=0}^{p}\frac{h^j}{j!}F_{p-j}(s)B^j.
\]
Every matrix \(B^j\) and every scalar coefficient is nonnegative by step 1. Thus the first term of \(T_{HH}\) is nonnegative, while \(q(h)>0\) for \(h>0\); this proves strict positivity of that block. In addition \(T_{KK}\ge0\) since \(z>0\) and \(1-z\ge0\), and \(T_{KH}\ge0\). As \(L\mathbf1=0\) and \(F_p(0)=1\), the resulting matrix is row-stochastic.

**5. Sharpness and no later recovery.** For any \(h>\beta_p/n\), step 1 yields \(F_p(nh)>1\). Every cross-block entry is then \((1-F_p(nh))/n<0\), independently of \(H\). Hence the exact iff statement follows.

## Verification
The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It checks the block formulas against full \(n\)-by-\(n\) matrix-polynomial expansion, exact row sums, and strict cross-block failure just beyond rational certified brackets for \(\beta_p\). In a direct execution it passed **222 graph/order configurations** and **231,840 exact entry comparisons**, including even orders \(2,4,6,8,10\), graphs without symmetric cores, and joins with \(k=1,2,3,4\). The symbolic proof above establishes all quantifiers; the finite checks do not purport to prove an infinite statement.

The rational brackets for \(\beta_2,\beta_4,\beta_6,\beta_8,\beta_{10}\) are respectively \((1.999,2.001)\), \((2.785,2.786)\), \((3.553,3.554)\), \((4.313,4.314)\), and \((5.069,5.070)\). Their signs are checked exactly in the verifier.

## Relationship to prior work
Gottlieb, Shu and Tadmor (2001) give the general strong-stability-preserving framework; Horváth (2005) studies Runge--Kutta positivity thresholds on broad IVP classes; Horváth, Song and Terlaky (first public preprint 2014) give coefficient tests and general algorithms for Taylor-step invariance thresholds. None of their inspected relevant results states the exact \(\beta_p/n\) frontier for arbitrary sparse residual graph joins with a dominating clique. Here the scalar obstruction is necessary because of the clique-to-core block and sufficient because the residual degree bound makes a *different* polynomial expansion nonnegative.

The complete-multipartite and disjoint-clique-core special families already have related scalar-frontier descriptions and are not the novelty of the present theorem. The expansion to arbitrary residual graphs such as long paths and cycles, and to a clique of any positive size, is the claimed additional scope. The ordinary Taylor/SSP coefficient-shift technique itself is established prior work.

## Limitations
The degree condition is **sufficient, not claimed necessary**. Graphs violating it may still have the same exact frontier. The proof treats unweighted undirected graph joins and completed even Taylor heat maps, not general methods or intermediate RK stages. The finite verification is not exhaustive over all graphs, and unindexed specialized literature could contain equivalent statements; independent audit and publication-priority verification remain outstanding.

## References
1. S. Gottlieb, C.-W. Shu, E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review **43** (2001), 89–112, doi:10.1137/S003614450036757X. First publicly available electronically 2001-02-02. https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf
2. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics **53** (2005), 341–356, doi:10.1016/j.apnum.2004.08.026. Online 2004-10-27.
3. Z. Horváth, Y. Song, T. Terlaky, *Steplength Thresholds for Invariance Preserving of Discretization Methods of Dynamical Systems on a Polyhedron*, Discrete and Continuous Dynamical Systems **35** (2015), 2997–3013, doi:10.3934/dcds.2015.35.2997; first public arXiv version 2014-06-26, arXiv:1406.6755.
