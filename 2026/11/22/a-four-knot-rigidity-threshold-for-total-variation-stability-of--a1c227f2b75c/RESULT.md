# A four-knot rigidity threshold for total-variation stability of convex least-squares regression

## Finding

Let \(n\ge2\), let \(x_1<\cdots<x_n\) be arbitrary real knots, and let \(m_i>0\) be arbitrary observation masses. Write \(Q\) for weighted least-squares projection of real nodal data onto the cone of convex sequences:
\[
 Q(y)=\arg\min_{z:\,(z_{i+2}-z_{i+1})/(x_{i+2}-x_{i+1})\ge(z_{i+1}-z_i)/(x_{i+1}-x_i)}\sum_{i=1}^n m_i(z_i-y_i)^2.
\]
Use **unweighted discrete total variation** \(V(z)=\sum_{i=1}^{n-1}|z_{i+1}-z_i|\), and define the sharp two-input seminorm coefficient
\[
 K=\sup_{V(y-v)>0}\frac{V(Q(y)-Q(v))}{V(y-v)}.
\]
Set \(L=x_n-x_1\), \(\bar x=\sum_i m_i x_i/\sum_i m_i\), \(S=\sum_i m_i(x_i-\bar x)^2\), and, for \(1\le j<n\),
\[
 c_j=\frac{\sum_{i=j+1}^{n}m_i(x_i-\bar x)}{S}>0.
\]
The following **complete nonexpansivity classification** holds:

1. For \(n=2\), \(K=1\).
2. For \(n=3\), the *exact attained sharp coefficient* is \(K=L\max(c_1,c_2)\ge1\). In particular, \(K=1\) precisely when \(m_1(x_2-x_1)=m_3(x_3-x_2)\).
3. For every \(n\ge4\), every knot configuration and **every strictly positive choice of observation masses**, \(K\ge L\max_jc_j>1\). Every displayed lower bound is attained as a local two-input gain by an arbitrarily small single-jump perturbation about a fully active affine-regression face. Thus no such convex-regression projector is globally nonexpansive in unweighted discrete variation.
4. On four equally spaced knots with equal masses, the complete sharp coefficient is \(\boxed{K=6/5}\). For all equally spaced equal-mass grids, the more general constructive bound is
\[
 K\ge\frac{6\lfloor n^2/4\rfloor}{n(n+1)},\qquad \liminf_{n\to\infty}K\ge\frac32.
\]
The last inequality is a lower bound, not an assertion of the exact asymptotic norm.

## Assumptions and scope

All data and knots are real; \(n\) is any finite integer at least two, knots are strictly ordered, and each \(m_i\) is finite and strictly positive. The fitted sequence is required only to be convex, not monotone or nonnegative. There is no constraint on the endpoints and no penalty besides squared error. The seminorm is the sum of unweighted nodal absolute increments, not slope variation, not weighted residual error and not \(\ell^\infty\). Since \(Q\) commutes with addition of constant vectors, the two-input quotient is well-defined modulo constant perturbations. The theorem concerns the *difference of two fitted sequences*: it does not claim an analogous one-input decrease of \(V(Qy)\).

## Proof

**1. The affine face exists on an open input region.** Put \(h_i=x_{i+1}-x_i>0\), and let \(C\) be the full-row-rank \((n-2)\times n\) matrix whose row \(i\) computes
\[
 (Cz)_i=\frac{z_{i+2}-z_{i+1}}{h_{i+1}}-\frac{z_{i+1}-z_i}{h_i}.
\]
Write \(M=\operatorname{diag}(m_1,\ldots,m_n)\) and \({\bf1}\) for the vector of \(n-2\) ones. For \(n\ge3\), let
\[
 b=-M^{-1}C^T{\bf1},\quad G=CM^{-1}C^T,\quad P=I-M^{-1}C^TG^{-1}C.
\]
The matrix \(G\) is positive definite. The weighted projection of \(b\) onto the cone \(Cz\ge0\) is zero: the optimality equations for the objective \(\tfrac12(z-b)^TM(z-b)\) at \(z=0\) have strictly positive multipliers \({\bf1}\). For any perturbation vector \(v\), the affine candidate \(P(b+tv)=tPv\) has zero curvature and multipliers \({\bf1}-tG^{-1}Cv\), strictly positive for sufficiently small \(|t|\). Hence it is the unique constrained least-squares projection in an entire neighborhood of \(b\), and \(P\) is its local linear operator. In other words every affine-face directional gain can actually be witnessed by *two feasible finite inputs*; there is no assumption that an arbitrary active pattern is realizable.

**2. Exact affine-face variation gain.** The range of \(P\) consists of all nodal values of affine functions \(a+\beta x_i\). Weighted normal equations give
\[
 \beta(v)=\frac1S\sum_{i=1}^n m_i(x_i-\bar x)v_i
      =\sum_{j=1}^{n-1}c_j(v_{j+1}-v_j).
\]
The second equality is summation by parts using \(\sum m_i(x_i-\bar x)=0\). Every \(c_j>0\): the weighted mean of the largest \(n-j\) knots is strictly greater than the global mean. Since \(V(Pv)=L|\beta(v)|\), it follows that
\[
 \sup_{V(v)>0}\frac{V(Pv)}{V(v)}=L\max_jc_j.
\]
The upper bound follows by the triangle inequality; equality is achieved by taking the perturbation \(v_i={\bf1}_{\{i>j\}}\) at an index maximizing \(c_j\). Such a step has \(V(v)=1\), and Step 1 realizes exactly the corresponding ratio for \(Q(b+tv)-Q(b)\) for every sufficiently small positive \(t\).

**3. Why four knots are a universal obstruction.** Applying the identity for \(\beta(v)\) to the special vector \(v_i=x_i\) gives
\[
 \sum_{j=1}^{n-1}h_jc_j=1.
\]
Therefore \(L\max c_j\ge1\), with equality if and only if all \(c_j=1/L\). But consecutive coefficients satisfy
\[
 c_j-c_{j-1}=-\frac{m_j(x_j-\bar x)}S\quad(2\le j\le n-1).
\]
With positive masses, all the \(c_j\) can be equal only if **every interior knot equals \(\bar x\)**. This is impossible when \(n\ge4\), because there are at least two distinct interior knots. Thus Step 2 gives strict expansion on every grid with at least four knots, regardless of masses. For three knots, equality is equivalent to \(\bar x=x_2\), or \(m_1h_1=m_3h_2\).

**4. Exact coefficients at two and three knots.** For two knots the cone is all of \(\mathbb R^2\), so \(Q=I\) and \(K=1\). For three knots there is just one convexity inequality. On its inactive side the projection is the identity, and on its active side it is precisely the affine operator \(P\) from Step 1. The projection is continuous and piecewise linear. Integrating these two Jacobians along the segment between any inputs (or approximating a boundary segment by generic segments) proves \(K\le\max\{1,L\max(c_1,c_2)\}=L\max(c_1,c_2)\). Step 2 supplies equality, including the stated nonexpansivity criterion.

**5. Four uniform knots: exhaustive sharpness.** In the equal-mass, unit-spaced four-site case, let \(D\) map a four-vector to its three successive differences, and \(E\) map a three-vector of differences to the four-vector with first entry zero. There are exactly two convexity constraints. On each region of fixed active set \(A\subseteq\{1,2\}\), the Jacobian is the Euclidean projector \(P_A=I-C_A^T(C_AC_A^T)^{-1}C_A\), with \(P_\varnothing=I\). The induced variation norm is the maximum absolute column sum of \(DP_AE\). Direct exact-rational calculation gives

| Active set | Norm of \(DP_AE\) in \(\ell^1\) |
| --- | --- |
| None | \(1\) |
| First only | \(7/6\) |
| Second only | \(7/6\) |
| Both | \(6/5\) |

A continuous polyhedral metric projection is piecewise linear with these local matrices; dividing any input segment into finitely many active-set regions gives the global upper bound \(6/5\). The all-active affine-face construction in Steps 1–2, with the unique middle step, attains \(6/5\), proving sharpness. An explicit finite pair is \(b=(-1,1,1,-1)\) and \(y=(-1,1,2,0)\). Their projections are respectively \(Q(b)=(0,0,0,0)\) and \(Q(y)=(-1/10,3/10,7/10,11/10)\), with positive active multipliers \((1,1)\) and \((9/10,11/10)\). Thus \(V(y-b)=1\) but \(V(Q(y)-Q(b))=6/5\).

**6. Quantitative equal-grid family.** For \(x_i=i-1\) and \(m_i=1\), direct summation yields
\[
 c_j=\frac{6j(n-j)}{n(n^2-1)},\qquad L=n-1,
\]
so the all-active lower bound reduces to \(6\lfloor n^2/4\rfloor/[n(n+1)]\). Its limit is \(3/2\). The argument does not assert that the all-active face maximizes the nonlinear projector's norm beyond the four-site case.

## Verification

Run `python3 verify_convex_bv.py` using the standard library. It uses exact rational arithmetic throughout. It verifies the three-knot formula and the mass-spacing nonexpansivity equivalence for 1,600 positive rational parameter combinations; enumerates the four active-face matrices and their norms exactly; constructs and checks an attained four-site \(6/5\) witness with positive Karush–Kuhn–Tucker multipliers; verifies the affine-face witness and strict greater-than-one gain for 150 independently chosen positive rational irregular knot/mass configurations of sizes four through nine; and checks the equal-grid coefficient identity through size 39. This finite testing is supplementary: the proofs of the all-size statements are the exact Steps 1–3 and 6.

## Relationship to prior work

Shape-restricted convex least squares and cone projections date back at least to Hildreth and Dykstra. Meyer (2008) treats shape-restricted regression splines and their constrained least-squares construction; Guntuboyina and Sen (2013) treat convex-regression squared-risk and adaptive behavior, including the special role of affine projected fits for concave data. None of these inspected materials states the general two-input unweighted-variation stability threshold for arbitrary knots and positive masses. The later work of Yang and Barber concerns contraction criteria for *isotonic* (first-difference constrained) regression, which is a different cone; its results do not transfer through a variation-isometric map that preserves the least-squares metric. Published finite convex-regression results giving exact \(\ell^\infty\) Lipschitz constants for four or five points likewise do not imply the asserted variation-norm constants, the three-knot mass condition, or the all-grid strict obstruction. The original full texts of some earlier algorithms remain a historical-priority risk.

## Limitations

No exact global two-input coefficient is claimed at \(n\ge5\), nor for general weights at \(n=4\). The strictly greater-than-one theorem does not give a mesh- and mass-independent positive gap when the observation masses can degenerate. The quantity measured is unweighted first-difference variation, even though data fitting is observation-weighted. Multidimensional shape constraints, other norms of differences, and higher-order shape restrictions lie outside the theorem. The mathematical assessment is same-model only; independent assessment is unperformed.

## References

1. M. C. Meyer, *Inference using shape-restricted regression splines*, arXiv:0811.1705v1, publicly posted November 11, 2008. https://arxiv.org/abs/0811.1705
2. A. Guntuboyina and B. Sen, *Global risk bounds and adaptation in univariate convex regression*, arXiv:1305.1648v1, publicly posted May 7, 2013. https://arxiv.org/abs/1305.1648
3. E. Seijo and B. Sen, *Nonparametric least squares estimation of a multivariate convex regression function*, arXiv:1003.4765v1, publicly posted March 24, 2010. https://arxiv.org/abs/1003.4765
4. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852v1, publicly posted June 6, 2017. https://arxiv.org/abs/1706.01852
5. R. L. Dykstra, *An Algorithm for Restricted Least Squares Regression*, JASA 78 (1983), 837–842, doi:10.1080/01621459.1983.10477029. https://doi.org/10.1080/01621459.1983.10477029
6. Published published-finding corpus record, *Five-point nonlocal instability and a persistent lower bound for convex least-squares projection*, November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-five-point-nonlocal-instability-and-a-persistent-lower-bound-for--45dce1453393
7. Published published-finding corpus record, *Cyclic-cover rigidity of weighted-variation stability for isotonic regression*, November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclic-cover-rigidity-of-weighted-variation-stability-for-isoton--c6a0693fe803
