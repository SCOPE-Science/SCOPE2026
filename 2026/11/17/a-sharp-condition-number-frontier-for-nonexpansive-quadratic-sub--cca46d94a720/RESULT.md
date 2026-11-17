# A sharp condition-number frontier for nonexpansive quadratic subgradient projections

## Finding

Let \(d\geq2\), and let \(A\) be a real symmetric positive-definite \(d\times d\) matrix. The classical subgradient projector of the quadratic function \(f(x)=x^{\mathsf T}Ax\) is
\[
G_A(x)=\begin{cases}x-\dfrac{x^{\mathsf T}Ax}{2x^{\mathsf T}A^2x}Ax,&x\ne0,\\[3pt]0,&x=0.\end{cases}
\]
Write \(\kappa=\lambda_{\max}(A)/\lambda_{\min}(A)\). Then the following are equivalent:

1. \(G_A\) is nonexpansive in the Euclidean norm on all of \(\mathbb R^d\), meaning \(\|G_A(x)-G_A(y)\|_2\le\|x-y\|_2\) for all \(x,y\).
2. \(\kappa\le 2+\sqrt3\).

Moreover, \(G_A\) has global Lipschitz modulus strictly below one if and only if \(\kappa<2+\sqrt3\). At equality its global modulus is exactly one; above this threshold some pair of distinct points is strictly expanded. At the critical value, a norm-one derivative occurs in a plane spanned by eigenvectors for the smallest and largest eigenvalues. For every positive-definite \(A\), regardless of \(\kappa\), every nonzero \(x\) satisfies \(\|G_A(x)\|_2<\|x\|_2\): radial contraction toward the fixed point is strictly weaker than pairwise nonexpansiveness.

## Assumptions and scope

The ambient space is finite-dimensional real Euclidean space, \(d\ge2\). The matrix is real symmetric and strictly positive definite; no eigenvalue multiplicity restriction is imposed. The projector is for \(f(x)=x^{\mathsf T}Ax\), not for the square-root ellipsoidal gauge and not for the metric projection onto a quadratic sublevel set. It equals the Polyak subgradient projection \(x-f(x)\nabla f(x)/\|\nabla f(x)\|^2\), where \(\nabla f(x)=2Ax\). The only feasible point is the origin. The threshold is independent of dimension and of the magnitudes of the eigenvalues under common scaling.

## Proof

**1. Reflection of the Jacobian.** For \(x\ne0\), put
\[
 u=\frac{Ax}{\|Ax\|_2},\quad t=\frac{x^{\mathsf T}Ax}{x^{\mathsf T}A^2x}=u^{\mathsf T}A^{-1}u,\quad P=I-uu^{\mathsf T},\quad R=I-2uu^{\mathsf T}.
\]
The matrix \(R\) is an orthogonal reflection. Direct differentiation of the homogeneous quotient gives \(\nabla t=2(u-tAu)/\|Ax\|_2\) and
\[
 DG_A(x)=P-\frac{t}{2}RA,\qquad RDG_A(x)=P-\frac{t}{2}A=:S.
\]
The symmetric matrix \(S\) has \(S\preceq P\preceq I\), and multiplication by \(R\) preserves the Euclidean operator norm. Therefore
\[
 \|DG_A(x)\|_2\le1 \quad\Longleftrightarrow\quad S\succeq-I
 \quad\Longleftrightarrow\quad 4I-tA-2uu^{\mathsf T}\succeq0.\tag{1}
\]
Every unit vector \(u\) occurs because one may take \(x=A^{-1}u\). Thus (1) for all unit \(u\) is an exact global differential condition.

**2. Reduction from arbitrary spectra to their extreme eigenvalues.** A positive scalar multiple of \(A\) leaves \(G_A\) invariant, so normalize \(\lambda_{\min}(A)=1\), \(\lambda_{\max}(A)=k\). If \(k=1\), then \(G_A(x)=x/2\) and the assertion is immediate. Assume \(1<k<4\). Since \(1/k\le t\le1\), the matrix \(4I-tA\) is strictly positive. The rank-one Schur complement reduces (1) to
\[
 2u^{\mathsf T}(4I-tA)^{-1}u\le1.\tag{2}
\]
Let \(h\) range through the reciprocals of the eigenvalues of \(A\), with probability weights given by the squared spectral coordinates of \(u\). Then \(h\in[1/k,1]\) and its mean is \(t\). The left side of (2) divided by two equals the expectation of
\[
 \phi_t(h)=\frac{h}{4h-t},\qquad \phi_t''(h)=\frac{8t}{(4h-t)^3}>0.
\]
For fixed mean \(t\), a convex function lies below the affine chord through its values at \(1/k\) and \(1\). Consequently the largest possible left side of (2) at that mean is attained by a spectral vector supported only on the smallest and largest eigenspaces, with weights
\[
 w_{\min}=\frac{t-1/k}{1-1/k},\qquad w_{\max}=\frac{1-t}{1-1/k}.
\]
Both extreme eigenspaces exist. Substitution yields the exact identity
\[
 1-2\!\left(\frac{w_{\min}}{4-t}+\frac{w_{\max}}{4-kt}\right)
 =\frac{Q_k(t)}{(4-t)(4-kt)},\qquad
 Q_k(t)=3kt^2-4(k+1)t+8.\tag{3}
\]
The denominator is positive for \(1/k\le t\le1\), \(k<4\).

**3. Sharp threshold.** The quadratic \(Q_k\) has vertex \(t_*=2(k+1)/(3k)\). For \(1<k\le2\), the vertex lies at or to the right of one and the minimum on \([1/k,1]\) is \(Q_k(1)=4-k>0\). For \(2\le k<4\), the vertex is inside the admissible interval, and
\[
 \min_{1/k\le t\le1}Q_k(t)=\frac{4(4k-k^2-1)}{3k}.
\]
This is nonnegative precisely when \(k\le 2+\sqrt3\); it is strictly positive below the threshold and negative above it. At \(k_*=2+\sqrt3\), choose a unit vector \(u\) in the extreme-eigenvalue plane with squared component in the \(k_*\)-eigenspace
\[
 w_{\max}=\frac{k_*-2}{3(k_*-1)},\qquad
 w_{\min}=\frac{2k_*-1}{3(k_*-1)}.
\]
This gives \(t=t_*\), equality in the spectral chord bound, and a zero eigenvalue of \(4I-tA-2uu^{\mathsf T}\). Since \(S\preceq I\), the corresponding Jacobian has norm exactly one. For \(2+\sqrt3<k<4\), the same extreme-spectrum construction at the vertex gives \(\|DG_A\|_2>1\).

At \(k=4\), take \(A=\operatorname{diag}(1,4)\) on an extreme-eigenvector plane and \(u=(\sqrt7/3,\sqrt2/3)\), so \(t=5/6\); the determinant of \(4I-tA-2uu^{\mathsf T}\) on that plane equals \(-1/3\), proving expansion. For \(k>4\), choose \(u\) as a unit eigenvector for eigenvalue one, so \(t=1\) and \(S\) has eigenvalue \(1-k/2<-1\) along any eigenvector for eigenvalue \(k\). This proves the converse for all \(k\).

**4. From Jacobians to the global inequality.** The mapping is continuous at the origin, positively homogeneous, and differentiable away from the origin. A uniform bound on \(\|DG_A(x)\|_2\) for \(x\ne0\) implies the corresponding global Lipschitz bound by integrating along a line segment, splitting it at the origin if necessary. The converse follows by taking arbitrarily small displacements along a norm-maximizing derivative direction. For \(k<k_*\), (1) is uniformly strict on the compact unit sphere; hence the global modulus is strictly smaller than one. At \(k=k_*\), the critical derivative has norm one, while the upper bound is one. Above the threshold some derivative has norm greater than one.

**5. Strict radial contraction for every condition number.** Expanding the square of the defining formula gives
\[
 \|G_A(x)\|_2^2=\|x\|_2^2-\frac{3(x^{\mathsf T}Ax)^2}{4x^{\mathsf T}A^2x}<\|x\|_2^2\quad(x\ne0).
\]
All terms are defined because \(A\) is strictly positive definite. This establishes the announced separation.

## Verification

A standalone Python verifier (`verify.py`) checks the differentiated reflection identity exactly at 30 rational test instances; verifies algebraically the spectral-chord identity, convexity and discriminant calculation; checks the rational \(k=4\) expansion witness and the exact critical spectral equality; and numerically tests the planar transition on both sides of the threshold. It prints `ALL_NEW_QUADRATIC_SUBGRADIENT_CHECKS_PASS` when these checks succeed. The all-dimensional spectral reduction, global integration, and necessity cases are proven above; finite checks are not offered as proofs of universal claims.

## Relationship to prior work

Bauschke, Chen and Wang (2013), Example 4.9, define the classical subgradient projector and establish quasi-Bregman nonexpansivity relative to its fixed points; this is not pairwise nonexpansivity between arbitrary inputs. Bauschke, Wang, Wang and Xu (2014), Proposition 7.1, explicitly identify subgradient projectors of powers of quadratic forms, including the present formula, and Section 8 studies nonexpansiveness, but its stated tests there are one-dimensional or concern other examples. Pauwels (2014 preprint of a 2012 manuscript), Section 3.2.2, gives general Lipschitz tests/bounds without a spectral classification for this positive-definite quadratic family. This result supplies a sharp, dimension-free criterion not implied by those statements without additional nontrivial spectral optimization. The underlying operator and its fixed-point contraction property are classical; only the specific quantitative criterion and sharp boundary are asserted as a candidate new contribution.

## Limitations

This is a finite-dimensional, Euclidean, real SPD quadratic result; it makes no claim for semidefinite operators with nontrivial nullspaces, indefinite forms, other nonquadratic convex functions, or non-Euclidean operator norms. It does not give a closed formula for the exact Lipschitz modulus for every condition number, only the sharp threshold distinguishing contraction, nonexpansion, and expansion. Historical priority is provisional: general subgradient-projector literature is extensive, and related unindexed results remain a possibility. This is a mathematical proof subject to independent review, not an independent certification.

## References

1. H. H. Bauschke, J. Chen and X. Wang, *A Bregman projection method for approximating fixed points of quasi-Bregman nonexpansive mappings*, arXiv:1309.6402v1 (public 25 September 2013), particularly Example 4.9. https://arxiv.org/html/1309.6402v1
2. H. H. Bauschke, C. Wang, X. Wang and J. Xu, *On subgradient projectors*, arXiv:1403.7135v1 (public 27 March 2014), especially Proposition 7.1 and Section 8. https://arxiv.org/html/1403.7135v1
3. B. Pauwels, *Subgradient Projection Operators*, arXiv:1403.7237v1 (public 27 March 2014), especially Section 3.2.2. https://arxiv.org/abs/1403.7237
