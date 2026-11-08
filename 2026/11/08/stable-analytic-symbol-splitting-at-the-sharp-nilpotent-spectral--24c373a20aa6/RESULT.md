# Stable analytic-symbol splitting at the sharp nilpotent spectral-set constant

## Finding
Let \(J=\begin{psmallmatrix}0&2\\0&0\end{psmallmatrix}\), whose numerical range is the closed unit disk. Let \(F:\mathbb D\to\mathbb C^{p\times q}\), where \(p,q\ge1\), be analytic and contractive: \(\sup_{|z|<1}\|F(z)\|_{\mathrm{op}}\le1\). Define the rectangular amplified functional-calculus value
\[
\mathscr J(F)=\begin{pmatrix}F(0)&2F'(0)\\0&F(0)\end{pmatrix}:\mathbb C^{2q}\longrightarrow\mathbb C^{2p},
\qquad \delta(F)=2-\|\mathscr J(F)\|_{\mathrm{op}}.
\]
The following hold simultaneously, with no dependence of the constants on \(p\) or \(q\).

**Exact extremizers.** \(0\le\delta(F)\le2\), and \(\delta(F)=0\) if and only if there are constant unitary bases in \(\mathbb C^q\) and \(\mathbb C^p\) in which the entire analytic function splits as
\[
F(z)=\begin{pmatrix}z&0\\0&G(z)\end{pmatrix},\qquad z\in\mathbb D,
\]
with a contractive analytic \((p-1)\times(q-1)\) remainder \(G\). Empty blocks are permitted.

**Dimension-free symbol stability.** For every such \(F\) there exist constant input and output unitary bases and a contractive analytic remainder \(G\) such that
\[
\frac1{2\pi}\int_0^{2\pi}
\left\|F(e^{i\theta})-\begin{pmatrix}e^{i\theta}&0\\0&G(e^{i\theta})\end{pmatrix}\right\|_{\mathrm{HS}}^2\,d\theta
\ \le\ 4\delta(F).
\]
Boundary values are understood in the standard almost-everywhere radial sense. Equivalently, the matrix Hardy \(H^2\) distance to a split symbol is at most \(2\sqrt{\delta(F)}\). Consequently, at each \(0<r<1\), the matrix operator-norm deviation of the analytic functions at every \(|z|\le r\) is at most \(2\sqrt{\delta(F)}/\sqrt{1-r^2}\).

**Optimal stability exponent.** The exponent \(1/2\) cannot be replaced by any larger exponent with a uniform constant, even for scalar disk automorphisms. In particular, \(F_b(z)=(z+b)/(1+bz)\), for real \(b\downarrow0\), has
\[
\delta(F_b)=\tfrac32 b^2+O(b^4),\qquad
\inf_{|\omega|=1}\|F_b-\omega z\|_{H^2}^2=2b^2.
\]
This is a complete analytic-symbol rigidity and stability assertion at the sharp amplified bound; it is not merely a classification of the finite jet \((F(0),F'(0))\).

## Assumptions and scope
All norms on matrices are spectral/operator norms except \(\|\cdot\|_{\mathrm{HS}}\), the Hilbert–Schmidt norm. The matrix Hardy \(H^2\) norm is the square root of the sum of squared Frobenius norms of Taylor coefficients, equivalently the displayed boundary integral. The dimensions \(p,q\) are arbitrary finite positive integers. The function \(F\) need not be inner, rational, continuous on the boundary, square or invertible. The Schur norm bound is on the open disk. The functional-calculus block is defined by the first jet, so no global analyticity beyond the disk is needed.

## Proof
Write \(F(z)=\sum_{n\ge0}F_nz^n\), \(B=F_0\), \(C=F_1\), and \(t=\|C\|\). Multiplication by \(F\) maps \(H^2(\mathbb C^q)\) contractively into \(H^2(\mathbb C^p)\). Compressing to the first two monomials and reversing their order gives the contraction
\[
U=\begin{pmatrix}B&C\\0&B\end{pmatrix},\quad \|U\|\le1.
\]
Since \(\mathscr J(F)=U+\begin{psmallmatrix}0&C\\0&0\end{psmallmatrix}\),
\[
\|\mathscr J(F)\|\le1+t\le2,
\quad\hbox{hence}\quad 1-t\le\delta(F).
\]
The inequality \(t\le1\) follows also from the coefficient-energy estimate for any unit input vector. Nonnegativity of \(\delta\) is established, and its upper bound is immediate.

Choose unit \(v\in\mathbb C^q\) with \(\|Cv\|=t\); if \(t>0\), put \(w=Cv/t\), and if \(t=0\) choose any unit \(w\in\mathbb C^p\). The contractivity of the Hardy multiplier and Parseval yield
\[
\sum_{n\ge0}\|F_nv\|^2\le1,
\qquad \sum_{n\ge0}\|F_n^*w\|^2\le1.
\]
The second inequality uses the adjoint boundary multiplier, whose values are contractions; it does not assert that \(F(z)^*\) is analytic. The coefficient of \(z\) in the column \(F(z)v\) has inner product \(t\) with \(w\), and the coefficient of \(z\) in the analytic row \(w^*F(z)\) has inner product \(t\) with \(v^*\). Consequently,
\[
\|F(\cdot)v-zw\|_{H^2(\mathbb C^p)}^2\le2(1-t),
\qquad \|w^*F(\cdot)-zv^*\|_{H^2((\mathbb C^q)^*)}^2\le2(1-t).
\]
Choose constant unitary bases sending \(v,w\) to the first standard basis vectors. The transformed symbol has the block form \(\begin{psmallmatrix}a&b\\c&G\end{psmallmatrix}\). Here \(G\) is contractive because it is a compression of \(F(z)\) at every \(z\). The first column and first row estimates are precisely
\[
\|a-z\|_{H^2}^2+\|c\|_{H^2,\mathrm{HS}}^2\le2(1-t),\qquad
\|a-z\|_{H^2}^2+\|b\|_{H^2,\mathrm{HS}}^2\le2(1-t).
\]
Adding and subtracting the double-counted \(\|a-z\|_{H^2}^2\) gives the exact total squared block error and bounds it by \(4(1-t)\le4\delta(F)\). Evaluation at any \(|z|\le r\) has norm at most \((1-r^2)^{-1/2}\) on scalar Hardy \(H^2\); summing matrix coefficients gives the pointwise assertion.

If \(\delta(F)=0\), the block error is zero, and equality of analytic functions forces the exact split. Conversely, any such split has \(\|\mathscr J(F)\|\ge\|\mathscr J(z)\|=2\), while the proved upper bound is two. This proves the if-and-only-if statement.

For optimality take \(F_b(z)=(z+b)/(1+bz)\). It is inner, \(B=b\), \(C=1-b^2\), and for real nonnegative \(a,c\) the norm of \(\begin{psmallmatrix}a&2c\\0&a\end{psmallmatrix}\) is \(c+\sqrt{a^2+c^2}\). Therefore
\[
\|\mathscr J(F_b)\|=(1-b^2)+\sqrt{b^2+(1-b^2)^2}=2-\tfrac32 b^2+O(b^4).
\]
Parseval and innerness give \(\|F_b\|_{H^2}^2=1\) and \(\langle F_b,z\rangle_{H^2}=1-b^2\), so the exact squared distance to the rotation orbit of \(z\) is \(2-2(1-b^2)=2b^2\). This rules out a stronger uniform power of the deficit.

## Verification
Running `python3 check_schur_jordan.py` exercises explicit rational Taylor-coefficient identities, an exact equality test, finite boundary modulus tests for the scalar automorphisms, and quantitative-deficit estimates. The checker is supplementary: the proof above establishes all dimensions and all contractive analytic matrix symbols without a finite-experiment inference. The numerical assertion count and execution result appear in `VERIFICATION.md`.

## Relationship to prior work
Åhag, Czyż, Perälä and Virtanen's 2026 complete Crouzeix dimension-three work proves the amplified constant and develops equality and stability for the **functional-calculus operator value**. The present result fixes the extremal two-dimensional nilpotent and instead identifies all rectangular Schur **analytic symbols** attaining equality, including an \(H^2\) estimate for the entire symbol, uniformly over matrix level. Equality and stability for scalar functional-calculus values, or for the ambient matrix \(A\), do not by themselves assert this conclusion for the full function \(F(z)\). The proof employs classical Hardy-space contractivity and coefficient-energy arguments, whose general scope means that earlier operator-valued Schwarz/Schur-class results may entail parts of the statement. Bickel and collaborators' 2020 survey provides the broader extremal-function setting; Bickel et al.'s 2024 compressed-shift work concerns norm inequalities rather than the stated uniform function-level splitting.

## Limitations
Only the two-dimensional square-zero nilpotent with numerical-range unit disk is covered, albeit at all finite rectangular coefficient levels. The \(H^2\) **exponent** is sharp but the constant two is not asserted optimal. No quantitative \(H^\infty\) convergence up to the circle is claimed; the pointwise estimate deteriorates as the radius approaches one. The current novelty assessment is best-knowledge, not a proof of global bibliographic uniqueness; an operator-valued Schwarz or matricial interpolation theorem under another formulation might imply the classification or estimate. No independent mathematical validation has been performed.

## References
1. P. Åhag, R. Czyż, A. Perälä, J. Virtanen, *Square Functions and the Complete Crouzeix Conjecture in Dimension Three*, first public preprint arXiv:2608.27346v1 (2026-08-27); inspected accessible later version, particularly Sections 1, 10 and 12. https://arxiv.org/abs/2608.27346
2. K. Bickel, P. Gorkin, A. Greenbaum, T. Ransford, F. L. Schwenninger, E. Wegert, *Crouzeix's Conjecture and Related Problems*, Computational Methods and Function Theory 20 (2020), 701–728. https://doi.org/10.1007/s40315-020-00350-9
3. K. Bickel and collaborators, *Crouzeix's conjecture, compressions of shifts, and classes of nilpotent matrices*, Complex Analysis and Operator Theory (2024). https://doi.org/10.1515/conop-2024-0004
4. J. A. Ball, M. Guerra Huamán, *Test functions, Schur–Agler classes and transfer-function realizations: the matrix-valued setting*, preprint arXiv:1109.3795 (2011), background on matrix-valued Schur classes. https://arxiv.org/abs/1109.3795
