# Midpoint refinement reverses sharp affine-projection stability at four arms

## Finding
Let \(S_d\) be the metric star with \(d\geq2\) arms, each of length \(2\), endowed with uniform arclength measure. Let \(P_d^{(0)}\) project real \(L^2(S_d)\) orthogonally onto continuous functions affine on each whole arm. Let \(P_d^{(1)}\) project onto continuous functions affine separately on the two length-\(1\) halves of each arm. Both projectors are considered as bounded operators from real \(L^\infty(S_d)\) to itself.

The **sharp refined norm**, its complete set of norming evaluation locations, and its comparison with the coarse norm are
\[
\boxed{\|P_d^{(1)}\|_{\infty\to\infty}=\frac{1552d^2+928d+19}{9(4d+3)(20d+1)},\qquad \|P_d^{(0)}\|_{\infty\to\infty}=\frac{7d+3}{3(d+1)}.}
\]
Exactly the \(d\) outer endpoints of the refined star are norming locations. All middle nodes, the central hub, and all edge-interior points have strictly smaller evaluation norms. **Uniform midpoint refinement makes the sharp projection norm larger for \(d=2,3\), but smaller for every integer \(d\geq4\)**; equality never occurs. Both norms increase strictly with \(d\), and
\[
\lim_{d\to\infty}\|P_d^{(1)}\|_{\infty\to\infty}=\frac{97}{45},\quad
\lim_{d\to\infty}\|P_d^{(0)}\|_{\infty\to\infty}=\frac73,\quad
\lim_{d\to\infty}(\|P_d^{(1)}\|-\|P_d^{(0)}\|)=-\frac8{45}.
\]

## Assumptions and scope
Each arm is an isometric copy of \([0,2]\), glued at its left endpoint. The graph has no atoms at vertices; the measure is ordinary arclength. All functions and Hilbert spaces are real. The refined spline space consists of continuous functions linear on \([0,1]\) and \([1,2]\) of every arm. The coarse spline space consists of continuous functions linear on \([0,2]\) of every arm. There are no boundary conditions. The norm is the essential-supremum operator norm of an \(L^2\)-orthogonal projection, not its Hilbert-space operator norm (which equals one).

## Proof
**1. Gram matrix and exact kernel.** Index the refined nodes by hub \(c\), midpoints \(u_i\), and leaves \(v_i\), \(1\leq i\leq d\). In their hat-function basis the mass matrix is \(M=A/6\), where
\[
A=\begin{pmatrix}2d&\mathbf1^\top&0\\\mathbf1&4I_d&I_d\\0&I_d&2I_d\end{pmatrix}.
\]
It is positive definite, because nodal hat functions are linearly independent in \(L^2\). Set \(R=6A^{-1}=M^{-1}\). By solving the five symmetry-reduced equations, the row of \(R\) for evaluation at each of the three node types has the following entries (\(u_1,v_1\) belong to the evaluated arm; \(u_j,v_j\) mean any other arm):

| evaluation | \(c\) | \(u_1\) | \(v_1\) | \(u_j\), \(j\ne1\) | \(v_j\), \(j\ne1\) |
|---|---|---|---|---|---|
| hub | \(7/(2d)\) | \(-1/d\) | \(1/(2d)\) | \(-1/d\) | \(1/(2d)\) |
| \(u_1\) | \(-1/d\) | \(2(6d+1)/(7d)\) | \(-(6d+1)/(7d)\) | \(2/(7d)\) | \(-1/(7d)\) |
| \(v_1\) | \(1/(2d)\) | \(-(6d+1)/(7d)\) | \((48d+1)/(14d)\) | \(-1/(7d)\) | \(1/(14d)\) |

For the hub row the distinguished and other arms are identical. Direct multiplication by \(A\) verifies each stated row of \(R\). For node evaluation at \(z\), the associated integral kernel is \(K_z(s)=\sum_w R_{zw}\phi_w(s)\). Therefore, at the two endpoints of a unit edge, its kernel has the two corresponding row entries. In every row above, each edge joins two entries of **opposite signs**. For \(p,q>0\) define
\[
\Phi(p,q)=\int_0^1|(1-t)p-tq|\,dt=\frac{p^2+q^2}{2(p+q)}.
\]
Thus the \(L^\infty\) norm of evaluation at each node equals the sum of \(\Phi\) over all edges using the absolute values of its two kernel coefficients.

**2. The three exact nodal norms.** Substitution and simplification give
\[
E_c=\frac{17}{9},\qquad E_u=\frac{76d+29}{9(4d+3)},\qquad E_v=\frac{1552d^2+928d+19}{9(4d+3)(20d+1)}.
\]
The differences factor as
\[
E_v-E_c=\frac{32(d-1)(6d+1)}{9(4d+3)(20d+1)}>0,
\quad E_v-E_u=\frac{2(16d^2+136d-5)}{9(4d+3)(20d+1)}>0
\]
for every integer \(d\ge2\). For evaluation at an interior point \(z_t\) of an edge joining nodes \(x,y\), the reproducing kernel is \((1-t)K_x+tK_y\) for \(0<t<1\). The triangle inequality gives its evaluation norm at most \((1-t)E_x+tE_y<E_v\). Consequently the outer leaves, and no other points, are norming. The norm is attained by an essentially bounded input equal almost everywhere to the sign of an outer-leaf evaluation kernel.

**3. Coarse norm on the same metric star.** Every coarse arm has length \(2\). The common length factor in its hat-function Gram matrix cancels from the kernel integral. In the coarse nodal mass matrix the dimensionless matrix is \(A_0=\begin{pmatrix}2d&\mathbf1^\top\\\mathbf1&2I_d\end{pmatrix}\). The hub evaluation row in \(6A_0^{-1}\) is \((4/d;-2/d,\ldots,-2/d)\). The row for a leaf is \((-2/d;3+1/d,1/d,\ldots,1/d)\). The absolute kernel integrations yield
\[
E_c^{(0)}=\frac53,\qquad E_v^{(0)}=\frac{7d+3}{3(d+1)},\qquad
E_v^{(0)}-E_c^{(0)}=\frac{2(d-1)}{3(d+1)}>0.
\]
All coarse edge-interior locations are strictly subnorming by the same convex-combination argument. This proves the coarse norm formula.

**4. The sharp refinement reversal.** Exact subtraction gives
\[
\|P_d^{(1)}\|-\|P_d^{(0)}\|=
-\frac{4(32d^3-104d^2-77d+2)}{9(d+1)(4d+3)(20d+1)}.
\]
The numerator cubic equals \(-312\) at \(d=2\), \(-301\) at \(d=3\); for \(d\ge4\), setting \(h=d-4\ge0\) rewrites it as \(32h^3+280h^2+627h+78>0\). This proves exactly the stated reversal, with no equality. Differentiating the refined rational expression (for real \(d>0\)) gives
\[
\frac{d}{dd}E_v=\frac{1568(16d^2+4d+1)}{9(4d+3)^2(20d+1)^2}>0;
\]
the coarse norm has derivative \(4/[3(d+1)^2]>0\). Their rational limits give the three asymptotic constants claimed above. This completes the proof.

## Verification
The included standalone file `verify_midpoint_star_projection.py` is runnable with Python 3 and SymPy. It independently assembles each full mass matrix and inverts it in exact rational arithmetic for every integer \(2\le d\le17\), integrates absolute signed edge kernels exactly, and compares every nodal norm against the claimed formulas and the coarse projector. SymPy verifies the universal rational identities, derivative, factorization, and limits; the proof above does not depend on treating a finite range as exhaustive. Command: `python verify_midpoint_star_projection.py`. Successful final marker: `ALL_MIDPOINT_STAR_PROJECTION_CHECKS_OK`.

## Relationship to prior work
Kayumov's 2004 work surveys the classical sharp uniform bound \(3\) for univariate piecewise-linear spline orthoprojectors and studies second-order \(L\)-splines on intervals. It does not evaluate the symmetric branched network with a midpoint in every arm. The 2020 Diening–Storn–Tscherpel work studies stability under refinement for simplicial domains and supplies broad motivation, but does not give this exact metric-star refinement law. The coarse star norm is a pre-existing calculation, used here only as the comparator; the new claim is the exact midpoint-refined norm, its norming-point classification, and the sharp degree reversal. The Boman 2006 weighted finite-element stability paper was accessible only at the abstract level; an equivalent result elsewhere cannot be excluded by the checked sources.

## Limitations
The theorem does not address unequal arm lengths, nonuniform subdivisions, unequal arclength densities, interior or vertex atoms, arbitrary metric trees, or spline degrees beyond one. This is an exact graph-family calculation, not a universal monotonicity or antimonotonicity theorem for mesh refinement.

## References
1. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first public version 2004-08-30, https://arxiv.org/abs/math/0408418.
2. L. Diening, J. Storn, T. Tscherpel, *On the Sobolev and Lp-Stability of the L2-projection*, arXiv:2008.01801, first public version 2020-08-04, https://arxiv.org/html/2008.01801v2.
3. M. Boman, *Estimates for the L2-projection onto continuous finite element spaces in a weighted Lp-norm*, BIT Numerical Mathematics **46** (2006), 249–260, DOI:10.1007/s10543-006-0062-3; full text not inspected.
4. C. de Boor, *A Bound on the L-infinity Norm of L2-Approximation by Splines in Terms of a Global Mesh Ratio*, Mathematics of Computation **30** (1976), 765–771, DOI:10.1090/S0025-5718-1976-0425432-1; abstract inspected.
