# Exact nonnegative linearization cone for four-point polynomial hypergroups

## Finding
For every \(0<x<y<1\) and \(0<r<1\), let \(d_0=0,d_1=x,d_2=y,d_3=1\) and take the row-stochastic Jacobi recurrence with \(a_i=1-d_i\), \(b_i=(1-r)d_i\), and \(c_i=rd_i\). The associated four-point orthogonal polynomial system has **nonnegative product linearization (property (P)) if and only if all three explicit inequalities**
\[
H=(1-x)(1-r)^2+r(1-x-y)\ge0,\qquad
K=(1-y)(1-r)^2+r(2-3y)\ge0,\]
\[
L=y(y-x)(1+r^2)+r\{1-x(1-y)-2y^2\}\ge0
\]
hold. At the endpoint \(r=1\), property (P) holds if and only if \(x+y\le1\).

Consequently the exact region of profiles with property (P) **for every ratio \(0<r\le1\)** is
\[
\boxed{x+y\le1\quad\text{and}\quad y\le\frac23.}
\]
This uniform-ratio region extends beyond the previously sufficient Newton-coefficient cone: the profile \(x=1/10\), \(y=3/5\) belongs to it, although the third Newton coefficient \(1-3y+3x=-1/2\) is negative. The three inequalities are genuinely needed for individual ratios: at \((x,y,r)=(7/10,4/5,1/5)\), \(H=23/250>0\) and \(K=6/125>0\) but \(L=-1/1250<0\).

## Assumptions and scope
The parameters are real and satisfy \(0<x<y<1\), \(0<r\le1\). Let \(R_0(t)=1\), \(R_1(t)=t\), and define the four-point system by
\[
tR_i(t)=(1-d_i)R_{i+1}(t)+(1-r)d_iR_i(t)+rd_iR_{i-1}(t),\quad i=1,2,
\]
and the terminal equation \(tR_3(t)=(1-r)R_3(t)+rR_2(t)\) at the spectral nodes. The irreducible tridiagonal stochastic matrix \(J\) of this recurrence is similar to a real symmetric Jacobi matrix with positive off-diagonal entries, so it has four distinct real spectral nodes, and these polynomials are orthogonal for a positive measure on those nodes. In the normalization \(R_i(1)=1\), define
\[
R_m(t)R_n(t)=\sum_{k=0}^3g(m,n;k)R_k(t)
\]
on the four nodes. Property (P) is the assertion that \(g(m,n;k)\ge0\) for every \(0\le m,n,k\le3\). This is a statement about finite orthogonal polynomial systems, not infinite recurrences or positivity for arbitrary nonconstant coefficient ratios.

## Proof
The matrix recurrence and the spectral identity imply \(g(m,n;k)=[R_m(J)]_{n,k}\). In particular, multiplication by \(R_1\) is governed by the nonnegative stochastic matrix \(J\). It therefore remains to check the products \((m,n)=(2,2),(2,3),(3,3)\). Put \(X=1-x>0\) and \(Y=1-y>0\). Direct polynomial division, using
\[
R_2(J)=\frac{J^2-(1-r)xJ-rxI}{X},\qquad
R_3(J)=\frac{(J-(1-r)yI)R_2(J)-ryJ}{Y},
\]
gives the following full coefficient rows (listed by \(k=0,1,2,3\)):
\[
(g(2,2;k))_{k=0}^3=
\left(\frac{r^2xy}{X},\frac{ry^2(1-r)}X,\frac L X,
\frac{(1-r)Y(1+y-x)}X\right),
\]
\[
(g(2,3;k))_{k=0}^3=
\left(0,\frac{r^2y}X,\frac{r(1-r)(1+y-x)}X,\frac H X\right),
\]
\[
(g(3,3;k))_{k=0}^3=
\left(\frac{r^3xy}{XY},\frac{r^2y(1-r)}{XY},\frac{rH}{XY},\frac{(1-r)K}{Y}\right).
\]
All omitted products are symmetric, the degree-zero products are tautological, and the degree-one products are nonnegative. Every other displayed coefficient is nonnegative by the parameter restrictions. Thus when \(0<r<1\), the only possible negative coefficients are precisely those proportional to \(L,H,K\), proving the three-condition equivalence. For \(r=1\), the coefficient involving \(K\) vanishes identically, \(H=1-x-y\), and \(L=1-x(1+y)\). If \(H\ge0\), then \(x\le1-y\) and hence \(L\ge y^2>0\), proving the endpoint classification.

If property (P) holds for all \(0<r\le1\), evaluating the \(H\) test at \(r=1\) yields \(x+y\le1\). The \(K\) test as \(r\to1^-\), where its multiplier is positive, yields \(2-3y\ge0\). Conversely, under \(x+y\le1\) and \(y\le2/3\), the displayed formulas show \(H,K\ge0\) for all \(0<r\le1\). Further,
\[
1-x(1-y)-2y^2\ge1-(1-y)^2-2y^2=y(2-3y)\ge0,
\]
so \(L>0\) throughout this region. This proves necessity and sufficiency of the sharp universal-ratio region, including both boundary segments.

For \(x=1/10,y=3/5\), the profile is in the universal-ratio region but the third Newton coefficient \(d_3-3d_2+3d_1-d_0\) equals \(-1/2\), showing that the all-ratio classification is not a mere restatement of nonnegative Newton-coefficient sufficiency.

## Verification
The accompanying `CHECK.py` uses exact symbolic matrix arithmetic to reconstruct all twelve nontrivial product coefficients and their sum-to-one identities, checks all degree-one products, and verifies the rational independence witness and the negative-Newton-coefficient example. It prints `PASS: 35 symbolic/exact checks` when run with the specified SymPy dependency. The analytic inequalities above establish the claims for continuously varying parameters; a finite computational test alone would not do so.

## Relationship to prior work
Polzer (2026) proves a sufficient log-concavity criterion for Newton coefficients and explicitly asks for the exact boundary of profiles with property (P) at every constant ratio. The four-point theorem above supplies that boundary at degree three and, with the three inequalities, the stronger complete ratio-dependent cone. Szwarc (2003) gives a general necessary-and-sufficient matrix criterion, but it does not present these explicit four-point inequalities. The companion finite-system papers give general positive classes and perturbation criteria rather than this two-parameter exact profile region. The negative-Newton-coefficient example proves the new region extends beyond the stated hypothesis of Polzer's sufficient theorem; this does not imply that a broader unpublished or older four-point formula is impossible.

## Limitations
The result is exact only for four spectral points and constant downward-to-total ratio, with \(0<x<y<1\). It does not classify systems with five or more points or nonconstant ratios. The theorem does not claim that Newton log-concavity is necessary in general. Historical priority is conditional on the inspected literature; an unindexed older finite-hypergroup calculation could give an equivalent four-point criterion. The self-review is not an independent audit.

## References
1. Leslie P. Polzer, *A log-concavity criterion for finite nonnegative linearization*, arXiv:2611.01561v1 (2026-11-01), https://arxiv.org/abs/2611.01561.
2. Ryszard Szwarc, *A necessary and sufficient condition for nonnegative product linearization of orthogonal polynomials*, *Constructive Approximation* **19** (2003), 565–573, https://doi.org/10.1007/s00365-002-0524-z.
3. *Increasing-ratio and perturbative criteria for finite nonnegative linearization*, companion texts `papers/p2.tex` and `papers/p3.tex`, https://github.com/skypher/szkraw.
