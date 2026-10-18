# A sharp three-mode positivity threshold for MINRES on a diagonal Stieltjes system
## Finding
Consider exact-arithmetic MINRES for \\(Ax=b\\) from \\(x^{(0)}=0\\). For every symmetric positive definite matrix \\(A\\) and every \\(b\\ge 0\\), the first iterate is componentwise nonnegative. If, in addition, \\(A\\) is a Stieltjes matrix and its dimension is at most two, every MINRES iterate that is produced is componentwise nonnegative.

This low-dimensional statement is sharp in both dimension and iteration. For
\[
A=\\operatorname{diag}(1,2,4),\\qquad b_\\varepsilon=(1,1,\\varepsilon)^{\\mathsf T},\\qquad \\varepsilon>0,
\]
the second MINRES iterate is
\[
x^{(2)}=\\left(
\\frac{1+76\\varepsilon^2}{1+100\\varepsilon^2},
\\frac{1+118\\varepsilon^2}{2(1+100\\varepsilon^2},
\\frac{\\varepsilon(50\\varepsilon^2-1)}{2(1+100\\varepsilon^2}
\\right)^{\\mathsf T}.
\]
Hence its third coordinate is negative exactly when \\(0<\\varepsilon<1/\\sqrt{50}\\), vanishes at \\(\\varepsilon=1/\\sqrt{50}\\), and is positive above that threshold. The exact solution is
\[
x^\\star=\\left(1,\\frac12,\\frac{\\varepsilon}{4}\\right)^{\\mathsf T}>0.
\]
At \\(\\varepsilon=1/10\\), one has
\[
x^{(2)}=\\left(\\frac{22}{25},\\frac{109}{200},-\\frac1{80}\\right)^{\\mathsf T},\\qquad
x^\\star=\\left(1,\\frac12,\\frac1{40}\\right)^{\\mathsf T}.
\]
The sign loss is not an artifact of reducibility. With
\[
\\widetilde A=
\\begin{pmatrix}
1&-1/20&0\\\\
-1/20&2&-1/20\\\\
0&-1/20&4
\\end{pmatrix},\\qquad
\\widetilde b=\\left(1,1,\\frac1{10}\\right)^{\\mathsf T},
\]
all leading principal minors are positive and the off-diagonal graph is connected, so \\(\\widetilde A\\) is irreducible SPD Stieltjes. Its exact second MINRES iterate has third coordinate
\[
-\\frac{900492530}{220852842849}<0,
\]
while \\(\\widetilde A^{-1}\\widetilde b\\) is strictly positive.

## Assumptions and scope
The method is the exact-arithmetic minimum-residual Krylov method of Paige and Saunders, with no preconditioner and zero initial guess. For symmetric matrices this is the exact residual-minimizing iterate in \\(\\mathcal K_k(A,b)\\). The Stieltjes convention used here is real symmetric positive definite with nonpositive off-diagonal entries; reducibility is allowed in the diagonal threshold family, and an irreducible witness is supplied separately.

The theorem is about componentwise signs of iterates, not residual monotonicity, error monotonicity, finite-precision behavior, or constrained variants of Krylov methods.

## Proof
At the first step, \\(x^{(1)}=\\alpha b\\), where residual minimization gives
\[
\\alpha=\\frac{b^{\\mathsf T}Ab}{b^{\\mathsf T}A^2b}>0.
\]
Thus \\(b\\ge0\\) implies \\(x^{(1)}\\ge0\\).

If the dimension is one, MINRES is exact after at most one nontrivial Krylov step. If the dimension is two, MINRES is exact after at most two Krylov steps. For a Stieltjes matrix, \\(A^{-1}\\ge0\\) entrywise, so the exact solution \\(A^{-1}b\\) is componentwise nonnegative. Together with the first-step formula this proves nonnegativity of every produced iterate in dimensions at most two.

For the diagonal three-dimensional family, write the second iterate as
\[
x^{(2)}=c_0b_\\varepsilon+c_1Ab_\\varepsilon.
\]
Residual minimization is equivalent to the normal equations
\[
\\begin{pmatrix}m_2&m_3\\\\m_3&m_4\\end{pmatrix}
\\begin{pmatrix}c_0\\\\c_1\\end{pmatrix}
=
\\begin{pmatrix}m_1\\\\m_2\\end{pmatrix},
\\qquad
m_j=b_\\varepsilon^{\\mathsf T}A^jb_\\varepsilon.
\]
Here
\[
m_1=3+4\\varepsilon^2,\\quad m_2=5+16\\varepsilon^2,\\quad
m_3=9+64\\varepsilon^2,\\quad m_4=17+256\\varepsilon^2,
\]
and the determinant is \\(4(1+100\\varepsilon^2)>0\\). Cramer's rule gives
\[
c_0=\\frac{3(1+62\\varepsilon^2)}{2(1+100\\varepsilon^2)},\\qquad
c_1=-\\frac{1+34\\varepsilon^2}{2(1+100\\varepsilon^2)}.
\]
Substituting into \\(c_0b_\\varepsilon+c_1Ab_\\varepsilon\\) yields the displayed closed form for \\(x^{(2)}\\). Its first two coordinates are positive for every \\(\\varepsilon>0\\); the third has the sign of \\(50\\varepsilon^2-1\\), proving the exact threshold.

Iteration one cannot exhibit sign loss under the stated hypotheses, and dimensions one and two cannot exhibit it at any produced MINRES iterate. The three-dimensional witness therefore proves joint minimality of dimension three and iteration two. The irreducible perturbation is verified exactly in the accompanying checker.

## Verification
The standalone checker `verify.py` symbolically reconstructs the four moments, the normal-equation determinant, the two Krylov coefficients, and all three coordinate formulas. It then checks the exact witness at \\(\\varepsilon=1/10\\). Finally it verifies the leading principal minors, the exact second MINRES iterate, and the positive exact solution for the irreducible tridiagonal witness. Successful execution prints `VERIFY_OK`.

The universal parts of the theorem are analytic. The computation is a replay of algebraic identities and exact rational witnesses, not a finite enumeration standing in for an infinite proof.

## Relationship to prior work
Paige and Saunders define the minimum-residual method by minimizing the Euclidean residual over Lanczos Krylov spaces and call the resulting method MINRES. Their inspected full text develops residual minimization, stability, and numerical behavior, including positive-definite examples, but no componentwise nonnegativity theorem or three-mode sign threshold was located in the inspected material. Saunders, Simon, and Yip later derive unsymmetric analogues in the same lineage; their SIAM record lists MSC \\(65\\mathrm{F}10\\), which supplies the primary classification used here.

The closest semantic database result found was a theorem about Euclidean solution-error amplification of symmetric GMRES(1). That result concerns repeated one-dimensional residual-minimizing steps and norm amplification, whereas the present result concerns the unrestarted two-dimensional Krylov iterate, componentwise cone violation, and an exact diagonal-family threshold. Separate published work on nonnegative quadratic programming uses active-set logic precisely because unconstrained Krylov solves need not enforce inequalities, but it does not imply the formula above.

## Limitations
The closed-form threshold is proved only for the specified diagonal spectrum \\(\\{1,2,4\\}\\) and right-hand-side family. The minimality statement is for exact-arithmetic MINRES with zero initial guess on SPD Stieltjes systems and nonnegative right-hand sides. It does not classify all three-dimensional Stieltjes matrices, all spectra, preconditioned MINRES, finite-precision implementations, or constrained minimum-residual methods.

The literature search cannot prove absolute novelty. Residual risk remains that an older treatment of conjugate residual or minimum-residual iterations contains an equivalent componentwise statement under different terminology.

## References
C. C. Paige and M. A. Saunders, “Solution of Sparse Indefinite Systems of Linear Equations,” SIAM Journal on Numerical Analysis 12(4), 617–629 (1975), DOI 10.1137/0712047. The publisher record gives an exact online-publication date of 2006-07-14.

M. A. Saunders, H. D. Simon, and E. L. Yip, “Two Conjugate-Gradient-Type Methods for Unsymmetric Linear Equations,” SIAM Journal on Numerical Analysis 25(4), 927–940 (1988), DOI 10.1137/0725052. The publisher record lists MSC \\(65\\mathrm{F}10\\) and an exact online-publication date of 2006-07-14.

Stanford Systems Optimization Laboratory, “MINRES: Sparse Symmetric Equations,” method and software description, https://web.stanford.edu/group/SOL/software/minres/ .
