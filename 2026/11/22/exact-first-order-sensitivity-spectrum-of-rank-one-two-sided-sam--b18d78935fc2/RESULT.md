# Exact first-order sensitivity spectrum of rank-one two-sided sampled Galerkin updates

## Finding
For any integers \(m,n\geq2\), any unit vectors \(a,u\in\mathbb R^m\), \(b,v\in\mathbb R^n\) with \(a^\top u\ne0\), \(b^\top v\ne0\), and any \(\sigma>0\), set \(A_*=\sigma ab^\top\). The fixed-increment rank-one two-sided basis-update-and-Galerkin map is
\[
\mathcal B(B)=P_{Bv}\,B\,P_{B^\top u},\qquad
P_w=\frac{ww^\top}{w^\top w},
\]
whenever \(Bv\) and \(B^\top u\) are nonzero. Write the two old-basis alignment losses as
\[
\alpha=\frac{\|(I-aa^\top)u\|}{|a^\top u|},\qquad
\beta=\frac{\|(I-bb^\top)v\|}{|b^\top v|}.
\]
Then \(\mathcal B\) is differentiable at \(A_*\), \(\mathcal B(A_*)=A_*\), and its real Fréchet derivative between Frobenius spaces has the **complete singular-value multiset**
\[
\boxed{\sqrt{1+\alpha^2+\beta^2}\ (1),\quad
\sqrt{1+\alpha^2}\ (n-2),\quad
\sqrt{1+\beta^2}\ (m-2),\quad
1\ (2),\quad 0\ ((m-1)(n-1)).}
\]
Parentheses specify multiplicities; coincident values are merged. In particular the **sharp infinitesimal worst-case error amplification** is
\[
\boxed{\lim_{\epsilon\downarrow0}\ \sup_{0<\|E\|_F\le\epsilon}
\frac{\|\mathcal B(A_*+E)-A_*\|_F}{\|E\|_F}
=\sqrt{1+\alpha^2+\beta^2}.}
\]
This is independent of the nonzero singular value \(\sigma\) and of the matrix dimensions. It equals one precisely when *both* old bases are aligned with their target singular directions. For every nonzero misalignment, a concrete perturbation direction attains the displayed factor asymptotically.

## Assumptions and scope
Matrices and vectors are real. The old basis vectors \(u,v\) remain **fixed** while the completed target matrix \(B=A_*+E\) varies. The map is the same-increment, unaugmented, rank-one version of the two-sided BUG update in Zhang [1, equation (2.1)], not a theorem about the independently integrated original BUG subproblems or the nonlinear time-stepping dynamics. The strict nonzero-overlap hypotheses ensure both sampled vectors are nonzero in a neighborhood of \(A_*\). Only local perturbations \(E\to0\) are covered; the statement does not assert a finite-error global bound with the displayed constant. The singular-value list is the spectrum of the derivative as a linear map \(\mathbb R^{m\times n}\to\mathbb R^{m\times n}\) with Frobenius inner product.

## Proof
**Step 1: differentiability and derivative.** Put \(P=aa^\top\), \(Q=bb^\top\), \(s=b^\top v\ne0\), and \(t=a^\top u\ne0\). At \(B=A_*\), the two sampled vectors are \(A_*v=\sigma s a\) and \(A_*^\top u=\sigma t b\). The normalization-independent projector formula shows that the map is smooth near \(A_*\). Differentiating the two rank-one projectors gives
\[
D\mathcal B(A_*)[E]=PEQ+(I-P)Ev\,b^\top/s+a\,u^\top E(I-Q)/t.\tag{1}
\]
The terms proportional to \(\sigma^{-1}\) from the projector derivatives cancel the factor \(\sigma\) in \(A_*\), explaining the scale independence.

**Step 2: tangent-normal block form.** Resolve the matrix into mutually orthogonal Frobenius blocks relative to \(\mathbb Ra\oplus a^\perp\) on the left and \(\mathbb Rb\oplus b^\perp\) on the right:
\[
E=\begin{pmatrix}e_{11}&e_{12}\\e_{21}&Z\end{pmatrix},\quad
p=\frac{(I-P)u}{t}\in a^\perp,\qquad
q=\frac{(I-Q)v}{s}\in b^\perp.
\]
Here \(e_{12}\) is a row, \(e_{21}\) a column, and \(Z\in\mathbb R^{(m-1)\times(n-1)}\). Substitution into (1), with \(v=s b+s q\) and \(u=t a+t p\), yields the exact linear operator
\[
\boxed{D\mathcal B(A_*)[E]
=\begin{pmatrix}
e_{11}&e_{12}+p^\top Z\\e_{21}+Zq&0
\end{pmatrix}.}\tag{2}
\]
Note that \(\|p\|=\alpha\), \(\|q\|=\beta\). Thus the derivative is the identity on the \((m+n-1)\)-dimensional rank-one tangent space plus an explicit map from the \((m-1)(n-1)\)-dimensional normal block into the two tangent off-diagonal blocks.

**Step 3: all singular values.** On the off-diagonal tangent pair let
\[
L:Z\longmapsto(p^\top Z,Zq).
\]
In Frobenius coordinates the derivative is \([I,L]\) onto its tangent image and zero on the complementary output-normal space. Its squared nonzero singular values are therefore those of \(I+LL^*\). A direct adjoint calculation gives
\[
LL^*(x,y)=\bigl(\alpha^2x+q(p^\top y),\quad p(q^\top x)+\beta^2y\bigr),
\]
where \(x\in b^\perp\), \(y\in a^\perp\). On the coupled directions \((q,0)\), \((0,p)\), the matrix is
\[
\begin{pmatrix}\alpha^2&\alpha\beta\\\alpha\beta&\beta^2\end{pmatrix},
\]
with eigenvalues \(\alpha^2+\beta^2\) and zero. On the \(n-2\) row directions orthogonal to \(q\), it is \(\alpha^2 I\); on the \(m-2\) column directions orthogonal to \(p\), it is \(\beta^2 I\). The scalar \(e_{11}\) contributes one more singular value one, and the coupled zero eigenvalue contributes the other. The derivative has a kernel of dimension \((m-1)(n-1)\), consisting of coupled tangent and normal input perturbations rather than, in general, purely normal inputs. This proves the multiset, including limiting cases \(p=0\) and/or \(q=0\) by continuity.

**Step 4: sharpness.** The operator norm of \(L\) is \(\sqrt{\alpha^2+\beta^2}\), since
\[
\|LZ\|^2=\|Z^\top p\|^2+\|Zq\|^2\le(\alpha^2+\beta^2)\|Z\|_F^2,
\]
with equality for a rank-one normal block \(Z=\widehat p\widehat q^\top\) if both alignment losses are positive (with the evident one-sided choices otherwise). As the top singular value of \([I,L]\) is \(\sqrt{1+\|L\|^2}\), the infinitesimal norm is the claimed expression; a top right-singular vector gives a perturbation family attaining the limit. Differentiability ensures the remainder is \(o(\|E\|_F)\) uniformly as \(E\to0\).

## Verification
The accompanying standalone `verify_bug.py` reconstructs the derivative from equation (1) for dimensions \((m,n)=(2,2),(2,3),(3,2),(3,4),(4,3),(5,6)\), independently computes its complete singular spectrum, and compares the actual nonlinear BUG difference quotient to the derivative. It passed 1,563 deterministic matrix-spectral and finite-difference assertions, including exactly aligned old bases. This is a finite diagnostic, not the proof of the all-dimension statement; Steps 1–4 are the proof.

## Relationship to prior work
Zhang [1, equation (2.1)] defines this same-increment two-sided BUG map, and [1, Theorem 2.2] proves a **finite-error**, all-perturbation relaxed-exactness estimate. For the rank-one target of this note, the coefficient supplied by that theorem simplifies to \(\sqrt{2+\alpha^2+\beta^2}\). It does not state a derivative or its exact singular spectrum; the new sharp *local* coefficient is \(\sqrt{1+\alpha^2+\beta^2}\). These coefficients control different quantifiers and must not be conflated. In the perfectly aligned case the theorem permits \(\sqrt2\) while the exact local coefficient is one.

Epperly [2, Section 10.1, Proposition 10.1] describes the same algebraic two-sided sampled projector as a projection approximation and credits Stewart's earlier projection characterization. This is essential prior identification: the map itself is not new. That section proves optimality for a fixed sampled pair, not the derivative spectrum for sampled spaces that move with \(B\). Nobile and Riffaud [3] and Hauck, Kusch and Schotthöfer [4] develop and bound different BUG integration constructions; their inspected formulations do not supply the stated rank-one differential singular spectrum. Standard rank-one tangent-space geometry and matrix-projector differentiation are used as prior methods, not claimed as inventions.

## Limitations
The calculation is a sharp first-order perturbation result, **not** a claim of global error nonexpansiveness. Indeed the finite-error amplification may be larger than the local coefficient even with aligned bases. It assumes fixed sampled vectors, exact arithmetic, real matrices, and a nonzero rank-one target; no result is claimed for ranks two or above, roundoff, independently integrated BUG subproblems, nonlinear dynamics, rank-changing events, or near-zero overlaps at the reference target. The theorem's mathematical identity does not alone establish historical priority against unindexed matrix perturbation literature. Independent validation has not been carried out.

## References
[1] Shiheng Zhang, *Robust High-Order BUG Integrators without Basis Augmentation*, arXiv:2611.15175, first posted November 11, 2026. https://arxiv.org/abs/2611.15175 ; https://arxiv.org/pdf/2611.15175

[2] Ethan N. Epperly, *Make the Most of What You Have: Resource-Efficient Randomized Algorithms for Matrix Computations*, PhD thesis, California Institute of Technology, 2025, Section 10.1. https://tropp.caltech.edu/dissertations/Epp25-Making-Most.pdf

[3] Fabio Nobile and Sébastien Riffaud, *Robust high-order low-rank BUG integrators based on explicit Runge-Kutta methods*, arXiv:2502.07040, first posted February 10, 2025. https://arxiv.org/abs/2502.07040

[4] Cory D. Hauck, Jonas Kusch and Steffen Schotthöfer, *High-order robust basis-update & Galerkin integrators for dynamical low-rank approximation*, arXiv:2608.27749, first posted August 27, 2026. https://arxiv.org/abs/2608.27749
