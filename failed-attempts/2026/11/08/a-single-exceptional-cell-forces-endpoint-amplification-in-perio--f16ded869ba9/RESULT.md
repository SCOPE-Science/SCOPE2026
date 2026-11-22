# A single exceptional cell forces endpoint amplification in periodic linear-spline projection

## Finding

Fix \(r>0\). For every even integer \(N\ge 6\), form a circle from \(N\) consecutive intervals of lengths \(r,1,\ldots,1\), with indices chosen so that the exceptional interval joins knots \(0\) and \(1\). Let \(P_{N,r}\) be real \(L^2\)-orthogonal projection onto the continuous piecewise-linear periodic splines, with the same arc-length measure used for input and output. Normalizing the total measure does not change the projector. Put
\[
\Lambda(r)=\lim_{\substack{N\to\infty\\N\ \mathrm{even}}}\|P_{N,r}\|_{L^\infty\to L^\infty}.
\]
This limit exists. With \(z=\sqrt3\), define the positive quantities
\[
E_-(r)=\frac{r(1-r)(r+1)}{3(r+z/3)^2(r+z)}\quad(0<r<1)
\]
and
\[
E_+(r)=\frac{(4-2z)(r-1)(r+1)(r+z/2)\bigl(r^2+(5z/3-1)r+1\bigr)}{3(r+z/3)^2(r+z)\bigl(r^2+(2+2z/3)r+z\bigr)}\quad(r>1).
\]
Then
\[
\Lambda(1)=2,\qquad
\Lambda(r)\ge 2+E_-(r)>2\quad(0<r<1),\qquad
\Lambda(r)\ge 2+E_+(r)>2\quad(r>1).
\]
Consequently, the asymptotic uniform-mesh endpoint norm \(2\) is a strict, isolated minimum within this one-defect family. The displayed bounds are rigorous **local evaluation witnesses**, not assertions of an exact formula for \(\Lambda(r)\). In particular,
\[
\liminf_{r\to\infty}\Lambda(r)\ge\frac{10-2\sqrt3}{3}>2.
\]

## Assumptions and scope

The operator acts on real measurable functions on a circle with the ordinary arclength inner product. The periodic spline space has one nodal hat per knot, is continuous across every knot, and is affine on each interval. The number of intervals is even, at least six, and tends to infinity at fixed \(r>0\). The claim does not concern a defect ratio that changes with \(N\), higher-order splines, or arbitrary nonperiodic boundaries.

## Proof

Write \(h_0=r\), \(h_j=1\) for the other edge lengths, and let \(\phi_j\) be the nodal hats. Direct integration gives the Gram matrix \(G_N\):
\[
6(G_N)_{jj}=2(h_{j-1}+h_j),\qquad
6(G_N)_{j,j+1}=h_j,
\]
with all other entries zero (indices cyclic). Set \(A_N=6G_N\). As \(N\) is even, conjugation by the diagonal sign matrix \(D_{jj}=(-1)^j\) gives \(B_N=D A_ND\), with negative off-diagonals. Its diagonal is twice the sum of adjacent edge lengths, so \(B_N\) is an irreducibly diagonally dominant Stieltjes matrix and its inverse is strictly positive. Let \(u_j=(B_N^{-1})_{kj}\). At the evaluation knot \(k\), the projection kernel has values \(6(-1)^{k+j}u_j\) at consecutive knots \(j\); the signs strictly alternate. The integral of the absolute value of a line segment with opposite-sign endpoints \(6u_j\) and \(-6u_{j+1}\) is therefore
\[
3h_j\frac{u_j^2+u_{j+1}^2}{u_j+u_{j+1}}.
\]
Thus the knot evaluation norm is exactly
\[
\mathcal L_{N,k}=3\sum_{j\bmod N}h_j\frac{u_j^2+u_{j+1}^2}{u_j+u_{j+1}}.
\tag{1}
\]
At a point inside an interval, its kernel is a convex combination of the two endpoint kernels. Convexity of the \(L^1\) norm shows that \(\|P_{N,r}\|=\max_k\mathcal L_{N,k}\).

For fixed \(r\), the matrices \(B_N\) and their bi-infinite analogue \(B\) are uniformly coercive and strictly diagonally dominant. Indeed, writing \(B_N=D_0(I-R)\), the nonnegative matrix \(R\) has row sum \(1/2\). The Neumann expansion \(\sum_{m\ge0}R^mD_0^{-1}\) gives an exponentially decaying bound in graph distance, uniform in even \(N\), and proves convergence of every fixed-index inverse entry to the corresponding bi-infinite entry. Combining this with (1) and dominated convergence gives \(\mathcal L_{N,k}\to\mathcal L_k\) for each fixed defect-relative index \(k\). A resolvent identity for the rank-two perturbation supported at sites \(0,1\) shows that rows whose distance from these sites diverges approach the all-unit-mesh evaluation norm, uniformly. Consequently \(\Lambda(r)=\max\{2,\sup_{k\in\mathbb Z}\mathcal L_k\}\) exists.

For the bi-infinite all-unit mesh, put \(q=2-\sqrt3\) and \(c=1/(2\sqrt3)\). The inverse signed Gram matrix has entries \(cq^{|i-j|}\). The geometric identity \((1+q^2)/(1-q^2)=2/\sqrt3\) in (1) gives the value \(2\). This proves \(\Lambda(1)=2\).

For the defective mesh, the bi-infinite signed matrix has diagonal \(2(r+1)\) at sites \(0,1\), diagonal \(4\) elsewhere, off-diagonal \(-r\) between \(0,1\), and off-diagonal \(-1\) elsewhere. Solving its recurrence for the row \(k=0\), with decay at both infinities, yields
\[
u_j=a q^{-j}\ (j\le0),\qquad u_j=b q^{j-1}\ (j\ge1),
\qquad a=\frac{2r+\sqrt3}{(r+\sqrt3)(3r+\sqrt3)},\quad
b=\frac{r}{(r+\sqrt3)(3r+\sqrt3)}.
\]
The two geometric tails in (1) give
\[
\mathcal L_0=3\left[\frac{2}{\sqrt3}(a+b)+r\frac{a^2+b^2}{a+b}\right]
=2+\frac{r(1-r)(r+1)}{3(r+\sqrt3/3)^2(r+\sqrt3)}.
\tag{2}
\]
This exceeds \(2\) for \(0<r<1\).

For \(r>1\), inspect instead the knot \(k=2\), immediately outside the long edge. Define
\[
t=\frac{r}{2r+\sqrt3},\qquad H=2(r+1)-rt,\qquad
v=\frac{1}{(2+\sqrt3)H-1}.
\]
The recurrence gives \(u_0=tv\), \(u_1=v\), \(u_2=Hv\), \(u_{-j}=u_0q^j\) for \(j\ge0\), and \(u_{2+j}=u_2q^j\) for \(j\ge0\). Substitution into (1) yields
\[
\mathcal L_2=3v\left[\frac{2}{\sqrt3}(t+H)+r\frac{t^2+1}{t+1}+\frac{1+H^2}{1+H}\right].
\tag{3}
\]
Exact rationalization gives \(\mathcal L_2-2=E_+(r)\). Every factor of \(E_+(r)\) is positive for \(r>1\), because \(4-2\sqrt3>0\) and \(5\sqrt3/3-1>0\). Taking the limit in (3) gives \(\lim_{r\to\infty}\mathcal L_2=(10-2\sqrt3)/3\). The stated inequalities and strictness follow.

## Verification

Run `python check_defect.py` with Python, SymPy, and NumPy installed. The script verifies the exact Green recurrences, formulas (2) and (3), both factorizations, the uniform constant, the long-edge witness limit, and independent numerical inversions of finite cyclic Gram matrices for several values of \(r\) and \(N\). Symbolic identities are exact; finite-grid checks are supplementary, not a substitute for the Neumann-series convergence proof.

## Relationship to prior work

The signed inverse-Gram integral formula (1) is the periodic counterpart of a general identity already given by Ciesielski and Kamont (2004, equation (2.12)); it is used as background, not claimed as new. Ciesielski and Kamont also derive the uniform-interval limit \(2\) and analyze a Franklin-mesh family with two contiguous interval scales; their published sharp constant \(2+(2-\sqrt3)^2\) concerns that specified family, not one exceptional interval of an arbitrary ratio in an otherwise uniform periodic mesh. Kayumov (2004) treats mesh-independent bounds for second-order \(L\)-spline projectors, not this defect asymptotic. Oswald (2006) gives a higher-dimensional unboundedness construction. Gawlik and Lew (2014) prove supercloseness of projections of sufficiently smooth functions for nearby finite-element spaces; they do not determine endpoint operator norms on arbitrary bounded inputs. Passenbrunner (2016) establishes general periodic uniform boundedness and convergence, not a sharp one-defect lower law. The isolated-cell result is different from the previously obtained *alternating two-periodic* mesh asymptotic, in which the limiting norm is below \(2\) for unequal adjacent lengths.

## Limitations

The inequalities are **witness lower bounds** for \(\Lambda(r)\), not a closed-form determination of that supremum or a classification of its maximizing knots. No claim is made about odd numbers of intervals, variable defect ratios, other spline orders, or all locally perturbed meshes. An exact coincidence with an older unindexed spline literature result cannot be excluded without independent priority review. The proofs and checks have not undergone independent audit.

## References

1. Z. Ciesielski and A. Kamont, *The Lebesgue constants for the Franklin orthogonal system*, Studia Mathematica **164** (2004), 55–73, DOI: 10.4064/sm164-1-4, https://www.impan.pl/shop/en/publication/transaction/download/product/90654.
2. A. Kayumov, *Least-squares approximation by second-order L-splines*, public preprint posted 2004-08-30, arXiv:math/0408418, https://arxiv.org/abs/math/0408418.
3. P. Oswald, *A counterexample concerning the L2-projector onto linear spline spaces*, arXiv:math/0611573 (posted 2006-11-19), https://arxiv.org/abs/math/0611573.
4. E. S. Gawlik and A. J. Lew, *Supercloseness of Orthogonal Projections onto Nearby Finite Element Spaces*, arXiv:1408.4104 (posted 2014-08-18), https://arxiv.org/abs/1408.4104.
5. M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720 (first posted 2016-08-24), https://arxiv.org/abs/1608.06720.
