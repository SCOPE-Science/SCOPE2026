# Sharp two-input path-variation sensitivity of convex least-squares regression

## Finding
For each integer \(n\ge2\), let \(Q_n\) be Euclidean projection onto the cone of discretely convex real sequences at equally spaced sites. Define
\[
\mathcal C_n=\{x\in\mathbb R^n:x_i-2x_{i+1}+x_{i+2}\ge0\ (1\le i\le n-2)\},\qquad
V_n(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|.
\]
The **two-input** sharp variation coefficient is
\[
K_n=\sup_{V_n(y-z)>0}\frac{V_n(Q_ny-Q_nz)}{V_n(y-z)}.
\]
Its values through eight sites are exactly, with attainment by distinct finite-distance input pairs,

| Number of sites | \(2\) | \(3\) | \(4\) | \(5\) | \(6\) | \(7\) | \(8\) |
|---|---|---|---|---|---|---|---|
| \(K_n\) | \(1\) | \(1\) | \(6/5\) | \(4/3\) | \(7/5\) | \(28/19\) | \(11/7\) |

In particular, **four sites are necessary and sufficient for variation amplification**. At eight sites the factor \(11/7\) is already strictly larger than the asymptotic \(3/2\) first-variation factor of projection onto the affine sequences alone. All dimensions admit the exact finite formula in the proof below. The constants are nondecreasing in dimension: \(K_{n+1}\ge K_n\) for every \(n\ge2\).

## Assumptions and scope
Data and fitted values are real; observations have equal least-squares weights and equally spaced design points. Convexity is a condition on consecutive second differences; no positivity or monotonicity condition is imposed on data. The minimizing objective is the Euclidean squared distance, while the sensitivity is measured in **unweighted open-path first variation**. Since adding a constant to either input adds that constant to its convex projection, the quotient is well defined on sequences modulo constants. It is not the coordinate-maximum or Euclidean Lipschitz norm.

## Proof
**1. Attainable active-face matrices.** Let \(B\) be the \((n-2)\)-by-\(n\) matrix whose row \(i\) has entries \((1,-2,1)\) at successive sites. Its rows are independent: prescribe arbitrary successive curvatures and the first two coordinates, then solve the recurrence. For a subset \(A\subseteq\{1,\ldots,n-2\}\), let \(B_A\) denote the corresponding row submatrix and define
\[
H_A=I_n-B_A^\top(B_AB_A^\top)^{-1}B_A,
\qquad H_\varnothing=I_n.
\]
Each \(H_A\) is an orthogonal projection and fixes constant sequences. Every subset \(A\) is realized on an open region where \(Q_n\) equals \(H_A\): choose a sequence \(x\) whose second differences are zero precisely on \(A\) and one elsewhere, and let \(y=x-B_A^\top\mathbf1\). Then \(Q_ny=x\) by the KKT conditions; all active multipliers are strictly positive, and all remaining curvatures have strict slack. These conditions persist under sufficiently small perturbations, and the local projection is \(H_A\). The same argument with strictly positive curvatures handles the empty set.

**2. Exact all-dimensional reduction.** Let \(D\) be the first-difference matrix, \((Dz)_i=z_{i+1}-z_i\), and let \(J\) be the cumulative step matrix, \(J_{kj}=\mathbf1_{k>j}\) for \(1\le j<n\). Then \(DJ=I_{n-1}\), and every input difference equals a constant plus \(Jd\), where \(d\) is its first-difference vector. On an active cell, the gradient response is the matrix \(DH_AJ\) acting on \(d\). Its induced \(\ell^1\)-norm is the largest absolute column sum. A generic line segment between two inputs meets finitely many active cells; piecewise linearity, integration along the segment and continuity give the global upper bound. Conversely, the strict KKT construction makes every face locally attainable; choosing the step perturbation corresponding to a maximizing column attains that column's absolute sum for a sufficiently small **positive** distance. Therefore
\[
\boxed{K_n=\max_{A\subseteq\{1,\ldots,n-2\}}\ \max_{1\le j<n}\sum_{i=1}^{n-1}|(DH_AJ)_{ij}|.}\tag{1}
\]
This formula is an exact finite rational algorithm for every \(n\); it does not assume smoothness or exclude nongeneric input pairs.

**3. Complete sharp first dimensions.** For \(n=2\), the map is the identity. For \(n=3\), either no constraint is active or the two neighboring slopes are replaced by their arithmetic mean. Both slope maps have \(\ell^1\)-norm one. For \(n=4\), the four possible active sets give factors \(1,7/6,7/6,6/5\), respectively (the singleton active sets already amplify variation, but less than the jointly active face). In the all-active case,
\[
DH_{\{1,2\}}J=\frac1{10}
\begin{pmatrix}3&4&3\\3&4&3\\3&4&3\end{pmatrix},
\]
whose largest column sum is exactly \(6/5\). A completely explicit witness is
\[
y=(-1,1,1,-1),\quad h=(0,0,1,1),\quad
Q_4(y)=0,\quad Q_4(y+\varepsilon h)=\frac{\varepsilon}{10}(-1,3,7,11)
\]
for \(0<\varepsilon\le1/100\). The input difference has variation \(\varepsilon\) and the output difference has variation \(6\varepsilon/5\).

For \(n=5,6,7,8\), all \(2^{n-2}\) active sets are exhaustively enumerated with **exact rational arithmetic** by the standalone verification program. Every matrix \(H_A\), all its step columns and each absolute column sum are reconstructed; the following attainers are thereby certified. Active constraints are numbered from one, and step \(j\) means the input perturbation is zero through site \(j\) and one afterward.

| \(n\) | Attaining active set | Step \(j\) | Exact column \((DH_AJ)_{\cdot j}\) |
|---|---|---|---|
| \(5\) | \(\{2\}\) | \(2\) | \((1/6,1/2,1/2,-1/6)\) |
| \(6\) | \(\{2,3\}\) | \(2\) | \((3/10,3/10,3/10,3/10,-1/5)\) |
| \(7\) | \(\{1,3,4\}\) | \(3\) | \((3/19,3/19,6/19,6/19,6/19,-4/19)\) |
| \(8\) | \(\{2,3,4,5\}\) | \(4\) | \((-1/7,9/35,9/35,9/35,9/35,9/35,-1/7)\) |

The positive-distance witnesses are produced in the checker: for an active set, choose zero curvature on active rows and unit curvature otherwise, set all active KKT multipliers to one, and perturb the designated step by \(\varepsilon=1/100\). The checker verifies positivity of every active multiplier and inactive curvature for both inputs, and checks the exact quotient. The 127 active sets over all dimensions \(2\) through \(8\) comprise a genuinely exhaustive finite calculation, not a sample or an extrapolation to higher dimensions.

**4. Persistence and monotonicity in all dimensions.** Embed any \(n\)-site active set into the first \(n\) sites of an \((n+1)\)-site problem, making the additional curvature inequality inactive. The active projector is \(H_A\oplus[1]\), and its cell is attained by Step 1. For an \(n\)-site step perturbation, extend its final value to site \(n+1\). Then the output differences on the first \(n-1\) edges are exactly the original gradient column, and the additional edge contributes a nonnegative amount to the output variation. The new input's variation is unchanged. Thus every face's column gain persists or increases, proving \(K_{n+1}\ge K_n\). Consequently \(K_n\ge6/5\) for all \(n\ge4\), and \(K_n\ge11/7>3/2\) for all \(n\ge8\). For comparison, the all-active affine regression face has slope-response to step \(j\) equal to \(6j(n-j)/[n(n^2-1)]\), so its induced variation norm is \(6\lfloor n^2/4\rfloor/[n(n+1)]\), approaching \(3/2\) from below. Thus the eight-site factor exceeds even the limiting affine-face factor. This argument proves lower bounds, not exact formulas beyond eight sites.

## Verification
Execute `python3 verify_convex_bv.py` with Python 3.9 or newer; the source uses only the standard library. The program constructs second-difference Gram matrices, inverts them over rational numbers, checks all idempotence and constant-preservation identities, calculates every \(\ell^1\) column norm for all 127 active subsets in dimensions \(2\)–\(8\), and checks explicit primal, dual, and finite-distance perturbation certificates at each maximizing face. Recorded values match the table exactly. The all-dimensional reduction and monotonicity arguments are analytical; no finite computation is asserted to certify an unbounded census.

## Relationship to prior work
Meyer's 2008 shape-restricted regression spline paper supplies the geometric context of cone projections and active faces, but not sharp input-difference first-variation constants. Seijo–Sen (2010) formulate convex regression least squares and its constrained optimization structure; Chen–Wellner (2014) analyze statistical rates under convexity rather than deterministic two-input variation norms. The two closely related published convex-sequence projection findings compute \(\ell^\infty\)-to-\(\ell^\infty\) sensitivity and identify a five-site interior extremizer. Their sharp values and conclusions cannot imply the constants here because \(V_n\) is the \(\ell^1\)-norm **of first differences** on a quotient by constants; the exact active-face norm is \(\|DH_AJ\|_{1\to1}\), not \(\|H_A\|_{\infty\to\infty}\). Yang–Barber's isotonic contraction theorem concerns first-difference order constraints, rather than second-difference convexity. The precise first expansive dimension, all-dimensional variation formula, monotonicity, and exact values through eight sites were not found in the inspected statements.

## Limitations
The computed table is exhaustive **only through eight observations**. The all-dimensional formula is an exact exponentially sized active-face maximum, not a closed form in sample size; no optimal asymptotic limit is claimed. The result does not cover uneven design spacing, weighted observations, weighted path variation, cyclic data, or multivariate convex regression. An unindexed historical source could contain an equivalent statement; independent validation and an exhaustive priority determination have not been performed.

## References
1. M. C. Meyer, *Inference using shape-restricted regression splines*, original public preprint arXiv:0811.1705v1, 2008-11-11. https://arxiv.org/abs/0811.1705
2. E. Seijo and B. Sen, *Nonparametric Least Squares Estimation of a Multivariate Convex Regression Function*, arXiv:1003.4765v1, 2010-03-24. https://arxiv.org/abs/1003.4765
3. Y. Chen and J. A. Wellner, *On Convex Least Squares Estimation when the Truth is Linear*, arXiv:1411.4626v1, 2014-11-17. https://arxiv.org/abs/1411.4626
4. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852v1, 2017-06-06. https://arxiv.org/abs/1706.01852
5. *Five-point nonlocal instability and a persistent lower bound for convex least-squares projection*, published published-finding corpus finding, 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-five-point-nonlocal-instability-and-a-persistent-lower-bound-for--45dce1453393
6. *First interior worst-case amplification in five-point convex regression*, published published-finding corpus finding, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-first-interior-worst-case-amplification-in-five-point-convex-reg--5b2e2c46bf91
