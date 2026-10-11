# Parity-sharp arbitrary-coordinate divergence liftings
## Finding
Let \(\Gamma\) be any nonempty index set and let \(n\ge 2\), \(2\le q<\infty\), and \(1\le p\le q\). Write \(p'\) for the conjugate exponent, \(G_{m,n}=(\mathbb Z/(2m\mathbb Z))^n\), and \(\Sigma_n=\{-1,1\}^n\). With Wang's operators
\[
(D_{\rm long}F)(x,j)=F(x+me_j)-F(x),\qquad
(D_{\rm sgn}F)(x,\epsilon)=F(x+\epsilon)-F(x),
\]
the following parity dichotomy holds for \(\ell_\infty(\Gamma)\)-valued divergence data.

If \(m\ge4\) is even and \(n\le m^q\), every
\[
g\in L_{p'}(G_{m,n}\times[n];\ell_\infty(\Gamma))
\]
admits
\[
h\in L_{p'}(G_{m,n}\times\Sigma_n;\ell_\infty(\Gamma))
\]
with
\[
D_{\rm sgn}^*h=\frac{n^{1/q}}mD_{\rm long}^*g,
\qquad \|h\|\le22\|g\|.
\]
For every \(\varepsilon>0\), the lifts can be chosen by one continuous odd positively homogeneous map \(\Phi_\varepsilon\) satisfying
\[
\|\Phi_\varepsilon(g)\|\le22(1+\varepsilon)\|g\|.
\]
For every odd \(m\), by contrast, there is a datum \(g\) for which the normalized divergence equation has no solution.

## Assumptions and scope
All Banach spaces are real. The positive statement assumes \(m\ge4\) even and \(n\le m^q\), exactly the sharp-scale hypotheses under which the cited \(L_1\) metric-cotype estimate is available. The negative statement requires only \(n\ge2\) and odd \(m\). No assertion is made that the numerical constant \(22\) is optimal, nor that the continuous selector is Lipschitz. The conclusion concerns arbitrary index sets \(\Gamma\), including nonseparable \(\ell_\infty(\Gamma)\).

## Proof
Set \(X=\ell_1(\Gamma)\), so \(X^*=\ell_\infty(\Gamma)\) isometrically. Cheng, Wang, and Xiang prove their sharp torus inequality for mappings into arbitrary \(L_1\)-spaces. Wang's parity-coset argument for Corollary 1.5 uses only that the range is an \(L_1\)-space, followed by a Banach-valued comparison between doubled ternary increments and sign increments. Therefore the identical argument applies to \(X=\ell_1(\Gamma)\), not only to finite-dimensional \(\ell_1^N\), and yields
\[
\left\|\frac{n^{1/q}}mD_{\rm long}F\right\|_{L_p(G_{m,n}\times[n];X)}
\le22\|D_{\rm sgn}F\|_{L_p(G_{m,n}\times\Sigma_n;X)}.
\]
Wang's quotient-duality theorem and its normalized lifting corollary are stated for every Banach space \(X\). Applying them to \(X=\ell_1(\Gamma)\) gives, for every datum \(g\), a lift \(h\) with the displayed divergence identity and \(\|h\|\le22\|g\|\).

It remains to choose the lift continuously. Let
\[
U=L_{p'}(G_{m,n}\times[n];\ell_\infty(\Gamma)),\quad
V=L_{p'}(G_{m,n}\times\Sigma_n;\ell_\infty(\Gamma)),
\]
and put \(A=D_{\rm sgn}^*:V\to W\) and \(B=(n^{1/q}/m)D_{\rm long}^*:U\to W\), where \(W=L_{p'}(G_{m,n};\ell_\infty(\Gamma))\). The closed relation
\[
R=\{(g,h)\in U\times V:Ah=Bg\}
\]
is a Banach space for the norm
\[
\|(g,h)\|_R=\max\{\|g\|,\|h\|/22\}.
\]
The projection \(P:R\to U\), \(P(g,h)=g\), is a bounded linear surjection. The pointwise \(22\)-bound shows \(B_U\subseteq P(B_R)\), while the definition of the norm gives \(P(B_R)\subseteq B_U\). Hence the Banach constant of \(P\) is exactly \(1\). The quantitative Bartle--Graves theorem gives, for every \(\varepsilon>0\), a continuous positively homogeneous right inverse \(S:U\to R\) with
\[
\|Sg\|_R\le(1+\varepsilon)\|g\|.
\]
Writing \(Sg=(g,\psi(g))\) and setting
\[
\Phi_\varepsilon(g)=\frac{\psi(g)-\psi(-g)}2
\]
produces a continuous odd positively homogeneous selection. Linearity of \(A\) and \(B\) preserves the lifting identity under this symmetrization, and the same \(22(1+\varepsilon)\) norm bound survives.

For odd \(m\), choose \(0\ne u\in\ell_1(\Gamma)\) and define
\[
F(x)=(-1)^{x_1+x_2}u.
\]
Every sign increment changes \(x_1+x_2\) by an even integer, so \(D_{\rm sgn}F=0\). Translation by \(me_1\) reverses the sign because \(m\) is odd, hence \(D_{\rm long}F\ne0\). Let \(A_0=D_{\rm sgn}\) and \(B_0=(n^{1/q}/m)D_{\rm long}\). Since \(B_0F\ne0\), Hahn--Banach provides a datum \(g\in U\) with \(\langle B_0F,g\rangle\ne0\). If some \(h\in V\) satisfied \(A_0^*h=B_0^*g\), then
\[
\langle B_0F,g\rangle=\langle F,B_0^*g\rangle
=\langle F,A_0^*h\rangle=\langle A_0F,h\rangle=0,
\]
a contradiction. Thus the odd-\(m\) obstruction is failure of solvability itself.

## Verification
The proof uses only three externally supplied ingredients: the sharp \(L_1\) metric-cotype estimate at \(n\le m^q\); Wang's quotient-duality equivalence between the forward difference estimate and the adjoint lifting estimate; and the quantitative Bartle--Graves right-inverse theorem. The first source explicitly ranges over arbitrary \(L_1\)-spaces, so \(\ell_1(\Gamma)\) is legitimate for every index set \(\Gamma\). The second source is stated for arbitrary Banach spaces. The Bartle--Graves bound is applied to the closed graph relation with a weighted norm whose projection has Banach constant exactly \(1\). The odd-parity witness is checked directly and does not use a finite experiment.

## Relationship to prior work
Wang's Corollary 1.5 states the dimension-free nonlinear lifting bound only for finite-dimensional targets \(\ell_\infty^N\), while Proposition 1.6 assumes finite-dimensional \(X\) when constructing continuous odd positively homogeneous selections. Wang also proves that the regular linear factorization is impossible for odd \(m\), using the same parity character in the forward problem, but does not state the resulting failure of nonlinear adjoint solvability. The present result combines the arbitrary-\(L_1\) scope of the sharp metric-cotype inequality, Wang's all-Banach-space duality, and a quantitative Bartle--Graves graph selection to obtain arbitrary-coordinate continuous liftings for even \(m\), together with an unsolvable datum for odd \(m\).

## Limitations
The constant \(22\) is inherited from the published ternary-to-sign comparison and is not proved optimal. The selector is continuous and positively homogeneous but is not asserted to be Lipschitz. The even-side theorem requires \(m\ge4\) and \(n\le m^q\). The result is for real Banach spaces, matching the focal source. An equivalent parity-solvability observation or graph-selection lemma could exist under different terminology; no such covering statement was found in the searches recorded in the audit.

## References
1. Y. Wang, *Divergence Liftings and Regular Factorizations for Metric Cotype*, arXiv:2609.32589v1, 2026.
2. Q. Cheng, Y. Wang, and B. Xiang, *Sharp Metric Cotype Inequalities for \(L_1\) via Nonlinear Cut Smoothing*, arXiv:2609.08749v2, 2026.
3. M. Ivanov, J. A. Jaramillo, S. Lajara, and N. Zlateva, *Continuous Selections and Invertibility of Nonsmooth Maps Between Banach Spaces*, Journal of Optimization Theory and Applications 206 (2025), Article 41.
4. R. G. Bartle and L. M. Graves, *Mappings between function spaces*, Transactions of the American Mathematical Society 72 (1952), 400--413.
