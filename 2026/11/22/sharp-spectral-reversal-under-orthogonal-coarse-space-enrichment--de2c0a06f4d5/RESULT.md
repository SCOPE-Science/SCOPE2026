# Sharp spectral reversal under orthogonal coarse-space enrichment for a contractive Jordan smoother

## Finding
For an explicitly contractive nonsymmetric smoother, adding a Galerkin coarse-space direction can *strictly increase* the asymptotic two-grid convergence factor even when the enlarged space contains the original one and both coarse corrections are orthogonal. The exact boundary is \(t\sin(2\theta)=2\rho\). The deterioration factor is unbounded as the small Jordan eigenvalue tends to zero at fixed shear.

## Assumptions and scope
Consider the real symmetric positive-definite linear system \(Ax=b\) with \(A=I_3\). The stationary linear update has error-propagation matrix
\[
S=\begin{pmatrix}0&0&0\\0&\rho&t\\0&0&\rho\end{pmatrix},\qquad \rho>0,\quad t>0,\quad \rho^2+t<1.
\]
Such an update is realized by the linear residual correction \(x\mapsto x+(I-S)(b-x)\). It is an abstract nonsymmetric stationary smoother, not asserted to arise from an additive-Schwarz decomposition. Its spectral norm is
\[
\|S\|_2=\frac{t+\sqrt{t^2+4\rho^2}}{2}<1.
\]
Take the nested *proper* coarse spaces \(U=\operatorname{span}\{e_1\}\) and
\[
V_\theta=\operatorname{span}\{e_1,\cos\theta\,e_2+\sin\theta\,e_3\},\quad 0\le\theta\le\pi/2.
\]
Their exact Galerkin corrections are the Euclidean orthogonal projections \(P_U\) and \(P_{V_\theta}\) because \(A=I_3\). Use one presmoothing step and one postsmoothing step. The corresponding error maps are \(E_W=S(I-P_W)S\), and \(\operatorname{spr}\) denotes spectral radius (not Euclidean operator norm).

## Proof
Let \(c=\cos\theta\), \(s=\sin\theta\), and \(z=-s e_2+c e_3\). Since \(e_1\) is annihilated by \(S\), the original two-grid operator is \(E_U=S^2\), whose lower two-dimensional block is
\[
\begin{pmatrix}\rho^2&2\rho t\\0&\rho^2\end{pmatrix}.
\]
Hence \(\operatorname{spr}(E_U)=\rho^2\).

Since \(V_\theta^\perp=\operatorname{span}\{z\}\), the enlarged error operator has the rank-one factorization
\[
E_{V_\theta}=Szz^TS=(Sz)(z^TS).
\]
Its only potentially nonzero eigenvalue is \(z^TS^2z=\rho^2-2\rho t sc=\rho^2-\rho t\sin(2\theta)\); its other two eigenvalues are zero. Thus
\[
\operatorname{spr}(E_{V_\theta})=\rho\lvert\rho-t\sin(2\theta)\rvert.
\]
For \(q=t\sin(2\theta)\ge0\), comparison with \(\rho^2\) gives strict deterioration exactly when \(\lvert\rho-q\rvert>\rho\), equivalent to \(q>2\rho\). There is strict improvement when \(0<q<2\rho\), and equality when \(q=0\) or \(q=2\rho\). Since \(\sin(2\theta)\le1\) with equality at \(\theta=\pi/4\), a harmful enrichment exists precisely for \(t>2\rho\).

At \(\theta=\pi/4\) the deterioration factor is \(\lvert1-t/\rho\rvert\). For any fixed \(0<t<1\), the condition \(\rho^2+t<1\) holds for all sufficiently small positive \(\rho\), and that factor tends to infinity. This does not imply divergence of either iteration: both spectral radii tend to zero. The Euclidean one-step norms can also be compared exactly:
\[
\|E_U\|_2=\rho\bigl(t+\sqrt{t^2+\rho^2}\bigr),\qquad
\|E_{V_{\pi/4}}\|_2=\frac{\rho^2+(t-\rho)^2}{2}.
\]
For fixed \(t\in(0,1)\) and \(\rho\downarrow0\), the first tends to zero and the second tends to \(t^2/2\). Finally, in dimension two there cannot exist two distinct nested nonzero proper subspaces; dimension three is minimal for this comparison.

## Verification
The attached standalone `verify_jordan_enrichment.py` performs 4,003 exact-rational identity checks, including the rank-one characteristic identity and squared singular-norm formula, and a rational contractive test at \(\rho=1/20\), \(t=1/2\), \(\theta=\pi/4\). There the original spectral radius is \(1/400\), the enriched spectral radius is \(9/400\), and the enriched Euclidean norm is \(41/400\). Separate floating-point matrix-eigenvalue and singular-value calculations were performed for four parameter pairs and five angles each. The proof above, not finite sampling, establishes the all-parameter assertions.

## Relationship to prior work
Bao, Cui, and Li (2026) define the nonsymmetric smoothed Galerkin two-grid error map and consider learned coarse spaces, unequal reliable target ranks, and perturbation diagnostics. Their results motivate comparing nested subspaces but do not give this exact orthogonal-enrichment Jordan spectral boundary. Nabben and Rooch (2026) give a distinct nonmonotonicity example for nonorthogonal coarse corrections and prove monotonicity for orthogonal corrections under additional normality conditions; the present smoother is nonnormal, and both projectors here are orthogonal. Notay (2020) provides a general nonnormal two-grid convergence framework, but no matching angle-shear phase diagram was identified in the material inspected. The broad lesson that spectral radius can misrepresent transient performance is established prior art, not claimed here.

## Limitations
This result is an exact-arithmetic, three-dimensional stationary-iteration model, not an assertion about every additive Schwarz smoother, PDE grid, Krylov solver, or learned coarse space. A large *ratio* of spectral radii does not mean that the enriched method diverges. The example quantifies a missing monotonicity guarantee; it does not establish prevalence of harmful enrichment in numerical practice. Relevant unindexed specialist results and variants of the general nonnormal two-grid theory remain possible priority risks. Independent validation has not been performed.

## References
- C. Bao, C. Cui, R. Li, *Learning Coarse Spaces for Two-Grid Methods from Smoothed Errors with Applications to High-Contrast Porous Media Flow*, arXiv:2611.05837v1 (first public 2026-11-04), https://arxiv.org/abs/2611.05837 . Sections 2.3, 5.1–5.2.
- R. Nabben, L. Rooch, *Norm-based convergence bounds for nonsymmetric algebraic V-cycle multigrid methods*, arXiv:2604.21815 (2026), https://arxiv.org/abs/2604.21815 . Section 3.2, Example 3.26 and Theorem 3.28.
- Y. Notay, *Analysis of two-grid methods: The nonnormal case*, Mathematics of Computation 89 (2020), 807–827, https://doi.org/10.1090/mcom/3460 .
