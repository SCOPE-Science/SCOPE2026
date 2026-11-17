# Four-point onset and asymptotic near-doubling of variation sensitivity in convex regression

## Finding
For every integer \(n\ge2\), let \(Q_n\) be the ordinary Euclidean projector onto the cone of real convex sequences at \(n\) equally spaced sites. Write
\[
V_n(h)=\sum_{i=1}^{n-1}|h_{i+1}-h_i|,\qquad
C_n=\sup_{V_n(x-y)>0}\frac{V_n(Q_nx-Q_ny)}{V_n(x-y)}.
\]
The first nine sharp two-input coefficients, **all attained by distinct finite input pairs**, are
\[
\begin{array}{c|rrrrrrrrr}
n&2&3&4&5&6&7&8&9&10\\\hline
C_n&1&1&6/5&4/3&7/5&28/19&11/7&11/7&5/3.
\end{array}
\]
Thus four sites are the first dimension with variation amplification, and the coefficient exhibits an exact eight-to-nine-site plateau followed by a strict increase at ten sites.

For all even \(n\ge6\) and all odd \(n\ge7\), respectively,
\[
\boxed{C_n\ge 2-\frac3{n-1}\quad(n\text{ even}),\qquad
C_n\ge 2-\frac3{n-2}\quad(n\text{ odd}).}
\]
In particular, \(\liminf_{n\to\infty}C_n\ge2\). This **does not** assert \(C_n\le2\) or convergence to two; an exact all-dimensional upper bound is not established.

## Assumptions and scope
The observation space is \(\mathbb R^n\) with equal positive least-squares weights and the nonperiodic site order \(1,\ldots,n\). The convex cone is
\[
\mathcal C_n=\{z\in\mathbb R^n:z_i-2z_{i+1}+z_{i+2}\ge0\ (1\le i\le n-2)\}.
\]
The estimator \(Q_nx\) uniquely minimizes \(\sum_i(z_i-x_i)^2\) over \(\mathcal C_n\). The seminorm \(V_n\) ignores additive constants, but the estimator is translation-equivariant, so its sharp quotient is finite. There are no monotonicity, nonnegativity, or endpoint constraints.

## Proof
**1. All face derivatives are attainable.** Let \(D\) be the \((n-2)\)-by-\(n\) matrix of second differences, with row \(j\) equal to \((1,-2,1)\) on coordinates \(j,j+1,j+2\). Its rows are independent. For a subset \(A\) of row indices, write \(D_A\) for those rows and
\[
H_A=I-D_A^{\mathsf T}(D_AD_A^{\mathsf T})^{-1}D_A,
\]
with \(H_\varnothing=I\). If the active curvatures are precisely \(A\), strict positive KKT multipliers and strict inactive curvature slack make the Euclidean projection locally affine with derivative \(H_A\).

Every \(A\) is realizable: choose a convex \(z\) whose second differences are zero on \(A\) and one off \(A\) (possible because \(D\) is surjective), choose multipliers \(\lambda_j=1\) for \(j\in A\), and define \(x=z-D_A^{\mathsf T}\lambda\). Then \(z=Q_nx\) by stationarity and complementary slackness, and all strict inequalities persist under small perturbations. For \(A=\varnothing\), choose strictly convex \(z=x\). As this is a continuous polyhedral projection, a generic segment between inputs crosses finitely many affine regions. Thus the global Lipschitz quotient in any translation-invariant seminorm equals the maximum of the norms of these \(H_A\), and a perturbation inside an open region gives finite attainment.

**2. A one-jump reduction.** Each \(H_A\) fixes constant vectors. Every real \(h\) has the decomposition
\[
h=h_1\mathbf1+\sum_{k=1}^{n-1}(h_{k+1}-h_k)s^{(k)},\qquad
s^{(k)}_i=\mathbf1_{\{i>k\}},
\]
and \(V_n(s^{(k)})=1\). The triangle inequality and the reverse test on a single step give the exact finite formula
\[
\boxed{C_n=\max_{A\subseteq\{1,\ldots,n-2\}}\ \max_{1\le k<n} V_n(H_As^{(k)}).}
\]
This formula is a finite characterization, not an assumption that every input is a step. Its extrema are attained by actual finite two-input pairs using the open regions from Step 1.

**3. Exact small-dimensional classification.** The accompanying standard-library checker `verify_convex_bv.py` forms each \(D_A\), inverts \(D_AD_A^{\mathsf T}\) by exact rational Gaussian elimination, and evaluates the expression in Step 2 for every one of \(2^{n-2}\) active sets and every one of \(n-1\) jump positions, for each \(2\le n\le10\). Thus it is an exhaustive, not sampled, finite certificate. The successive values are exactly those in the table. The maximizing active row sets (zero-indexed) and jump locations for dimensions four through ten are, respectively,
\[
\begin{array}{c|c|c}
n&A&k\\\hline
4&\{0,1\}&2\\
5&\{1\}&2\\
6&\{1,2\}&2\\
7&\{0,2,3\}&3\\
8&\{1,2,3,4\}&4\\
9&\{1,2,3,4\}&4\\
10&\{1,2,3,4,5,6\}&5.
\end{array}
\]
For example, at four sites the all-active face is affine least-squares regression. Its image of the central step \((0,0,1,1)\) is \((-1/10,3/10,7/10,11/10)\); its variation is \(6/5\). Finite-pair KKT witnesses for each maximum are checked rationally in the standalone script.

**4. Near-doubling construction.** Choose the face where only the first and last second differences are inactive. Its affine subspace consists of **independent endpoint values** and a least-squares straight-line fit on the \(m=n-2\) interior sites. For a central unit step with \(a\) interior sites on the left and \(b=m-a\) on the right, the fitted interior line has slope
\[
\beta=\frac{6ab}{m(m^2-1)}
\]
and left fitted value \(\alpha=b/m-\beta(m-1)/2\). The two endpoints remain at zero and one. Consequently the variation is exactly
\[
|\alpha|+(m-1)\beta+|1-\alpha-(m-1)\beta|.
\]
For \(n\ge6\), take \(a,b\) as balanced as possible; then \(\alpha\le0\) and \(\alpha+(m-1)\beta\ge1\), giving \(2(m-1)\beta-1\). If \(m\) is even this is \(2-3/(m+1)\), and if \(m\) is odd it is \(2-3/m\). Those are exactly the two lower bounds above. The face is realizable by Step 1, so every lower bound comes from finite perturbations, not a formal derivative outside the nonlinear projector's domain.

## Verification
Run `python3 verify_convex_bv.py` using Python 3 with no third-party packages. The script verifies all 511 face matrices across dimensions two through ten, their full single-jump maxima, exact strictly feasible two-input KKT witnesses for every displayed coefficient, and the boundary-spline identities for dimensions six through one hundred. The all-dimensional inequalities in Step 4 follow by the algebraic calculation, not extrapolation of the finite checks.

## Relationship to prior work
Meyer (2008) develops shape-restricted regression spline cone projections and facewise least-squares structure. Chatterjee, Guntuboyina and Sen (2013) analyze risk and statistical dimensions of shape-constrained projections, explicitly including convex sequences. Mazumder and coauthors (2015) study numerical convex regression and a Lipschitz *constraint on the regression function*, rather than the two-input path-variation stability of its projector. Two earlier published finite-dimensional convex-projection records provide sharp **coordinate maximum-norm** and **complete-pair Gini** sensitivity for the same cone; neither their numerical statements nor their operator-norm conclusions imply the adjacent-variation values and lower bounds here without additional analysis. The facewise-projection method is standard and not claimed as novel; the claim is the distinct sharp variation classification and near-doubling construction.

## Limitations
The exact \(C_n\) is not determined for \(n\ge11\), and the true asymptotic value or growth is unknown here. No universal upper bound two is proved. Equal spacing, ordinary Euclidean loss, and open-ended real paths are essential to the stated computation. The work has only self-review; historical priority remains conditional on additional human assessment of unindexed literature.

## References
1. M. C. Meyer, *Inference using shape-restricted regression splines*, 2008, public preprint 2008-11-11, arXiv:0811.1705. https://arxiv.org/abs/0811.1705
2. S. Chatterjee, A. Guntuboyina and B. Sen, *On risk bounds in isotonic and other shape restricted regression problems*, public preprint 2013-11-15, arXiv:1311.3765. https://arxiv.org/abs/1311.3765
3. R. Mazumder, A. Choudhury, G. Iyengar and B. Sen, *A Computational Framework for Multivariate Convex Regression and its Variants*, public preprint 2015-09-28, arXiv:1509.08165. https://arxiv.org/abs/1509.08165
4. *Five-point nonlocal instability and a persistent lower bound for convex least-squares projection*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-five-point-nonlocal-instability-and-a-persistent-lower-bound-for--45dce1453393
