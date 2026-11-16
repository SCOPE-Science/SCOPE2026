# A sharp linear separation cusp for four-mode Fourier observation on two arcs

## Finding

Let \(0<\alpha<\pi/2\). Among all unions of two equal, nonoverlapping circular arcs of angular half-width \(\alpha\), the antipodally separated pair maximizes the worst-case squared observation norm on \(V=\operatorname{span}_{\mathbb C}\{1,e^{it},e^{2it},e^{3it}\}\). Its optimal value is
\[
\Lambda_\alpha=\frac{2\alpha-\sin(2\alpha)}{\pi}.
\]
The distinguishing result is **quantitative**. If the shorter separation of the arc centers is \(\theta\in[2\alpha,\pi]\), and \(\lambda_\alpha(\theta)\) is the least observation eigenvalue, then
\[
\boxed{\ \Lambda_\alpha-\lambda_\alpha(\theta)\ \ge\ \frac{2\sin^3\alpha}{3\pi}\cos^4\!\left(\frac{\theta}{2}\right).\ }
\]
Equality is possible only at antipodal separation \(\theta=\pi\). Moreover the optimal value has the **sharp one-sided linear cusp**
\[
\boxed{\ \Lambda_\alpha-\lambda_\alpha(\theta)
=\frac{2\sin^3\alpha}{\pi}(\pi-\theta)+O_\alpha((\pi-\theta)^2),\quad\theta\uparrow\pi.\ }
\]
The minimizing coefficient subspace at antipodal separation is exactly \(\{(u,v,u,v):u,v\in\mathbb C\}\), of complex dimension two. The global maximizing value alone follows also by interlacing from the earlier sharp three-character two-arc theorem; the new content is the explicit global stability bound, the exact cusp coefficient, and the multiplicity mechanism.

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with Haar probability \(dt/(2\pi)\). The observation set \(E_{\alpha,\theta}\) is the union, modulo \(2\pi\), of \([\theta/2-\alpha,\theta/2+\alpha]\) and \([-\theta/2-\alpha,-\theta/2+\alpha]\). For \(2\alpha\le\theta\le\pi\) its interiors are disjoint. A coefficient vector \(a=(a_0,a_1,a_2,a_3)\) represents \(f_a(t)=\sum_{j=0}^3a_j e^{ijt}\). Then \(\|f_a\|_{L^2(\mathbb T)}^2=\|a\|_{\ell^2}^2\), and
\[
\lambda_\alpha(\theta)=\inf_{\|a\|_2=1}\int_{E_{\alpha,\theta}}|f_a(t)|^2\frac{dt}{2\pi}.
\]
No assertion concerns unequal arc lengths, overlapping arc interiors, or bands with five or more characters. Rotation and center exchange do not change the eigenvalues, so shorter separation suffices.

## Proof

Put \(m=2\alpha/\pi\), \(A=2\sin\alpha/\pi\), \(c=\cos\alpha\), \(x=\cos(\theta/2)\), and \(B=Ac=\sin(2\alpha)/\pi>0\). Direct integration gives the real symmetric Toeplitz Gram matrix \(G=(b_{|j-k|})_{0\le j,k\le3}\), with
\[
b_0=m,\quad b_1=Ax,\quad b_2=Ac(2x^2-1),\quad
b_3=\frac A3(4c^2-1)(4x^3-3x).
\]
At \(x=0\), the only nonzero off-diagonal entries are \(b_2=-B\). Thus \(\operatorname{spec}G=\{m-B,m-B,m+B,m+B\}\). Its lower eigenspace is precisely \(a_0=a_2\), \(a_1=a_3\).

For an arbitrary separation the reversal symmetry \(a_j\mapsto a_{3-j}\) splits the matrix into two Hermitian \(2\times2\) blocks
\[
G_+=\begin{pmatrix}m+b_3&b_1+b_2\\b_1+b_2&m+b_1\end{pmatrix},\qquad
G_-=\begin{pmatrix}m-b_3&b_1-b_2\\b_1-b_2&m-b_1\end{pmatrix}.
\]
Subtract \(\Lambda_\alpha=m-B\) from each block and denote their determinants by
\[
D_+=(B+b_3)(B+b_1)-(b_1+b_2)^2,\qquad
D_-=(B-b_3)(B-b_1)-(b_1-b_2)^2.
\]
An exact polynomial identity, obtained by substituting the three Fourier coefficients, is
\[
\frac{D_++D_-}{2}=B^2+b_1b_3-b_1^2-b_2^2
=-\frac43 A^2\sin^2\alpha\,x^4.
\]
For \(x>0\) at least one shifted block therefore has determinant at most \(-\frac43A^2\sin^2\alpha\,x^4<0\), so it has one negative and one positive eigenvalue. Each shifted block has maximum absolute row sum at most \(4A\): this uses \(B\le A\) and \(|b_1|,|b_2|,|b_3|\le A\) (the last inequality follows from \(|\sin 3\alpha|\le3\sin\alpha\)). If its eigenvalues are \(\mu_-<0<\mu_+\), then \(\mu_+\le4A\) and
\[
-\mu_-=\frac{|D_\pm|}{\mu_+}\ge\frac{\frac43A^2\sin^2\alpha\,x^4}{4A}
=\frac A3\sin^2\alpha\,x^4.
\]
Consequently \(\Lambda_\alpha-\lambda_\alpha(\theta)\ge A\sin^2\alpha\,x^4/3\), exactly the asserted universal stability bound. For \(x>0\), in fact \(\mu_+<4A\), since \(|b_1|=Ax<A\); hence the bound is strict unless \(x=0\). The negative determinant proves uniqueness of antipodal placement.

To obtain the **sharp** local rate, expand near \(x=0^+\): \(b_1=Ax\), \(b_2=-B+O_\alpha(x^2)\), \(b_3=-A(4c^2-1)x+O_\alpha(x^3)\). At \(x=0\), both \(G_+\) and \(G_-\) have simple smallest eigenvalue \(m-B\), with respective normalized eigenvectors \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\). The usual derivative formula for a simple Hermitian eigenvalue gives slopes \(+2A\sin^2\alpha\) and \(-2A\sin^2\alpha\), respectively. All other eigenvalues remain separated by the positive gap \(2B\). Hence
\[
\lambda_\alpha(\theta)=m-B-2A\sin^2\alpha\,x+O_\alpha(x^2).
\]
Because \(x=\sin((\pi-\theta)/2)=(\pi-\theta)/2+O((\pi-\theta)^3)\), the cusp formula follows, with coefficient \(A\sin^2\alpha=2\sin^3\alpha/\pi\). This also proves that the linear exponent is optimal.

## Verification

The standalone `verify_two_arcs.py` uses symbolic polynomial simplification to prove the determinant identity and independently computes the full four-by-four Gram matrices by Gauss-Legendre quadrature. It compares the exact eigenvalues, checks the stated uniform bound at 246 admissible parameter pairs, and tests the cusp coefficient at six aperture widths. The checker prints `TWO_ARC_FOUR_MODE_PASS`; its finite numerical tests support rather than replace the analytic proof.

## Relationship to prior work

The Fourier concentration and Slepian literature analyzes eigenvalues of restricted Fourier transforms, including nonconvex observation domains. Marceca, Romero and Speckbacher (2023) provide nonasymptotic bounds for intermediate spectra of general concentration operators, but neither this exact four-character two-arc maximization nor its separation stability law. Abreu and Speckbacher (2026) optimize the **largest** Fourier concentration eigenvalue over arbitrary measurable observation sets; that optimization and its complementary minimization are logically distinct from **maximizing** the smallest eigenvalue over equal-length two-arc configurations. An earlier three-character two-arc result already yields the *unquantified* four-character optimal value via eigenvalue interlacing; it does not imply the present quantitative deficit or sharp cusp. The Fourier coefficient integration and Hermitian perturbation formula are standard and are not asserted to be new.

## Limitations

The bound is globally positive away from antipodal separation but is not claimed sharp there; the cusp constant is sharp only in the stated one-sided limit. Historical priority of this particular stability formulation has not been independently established. The proof concerns exactly four consecutive complex Fourier characters, equal arc widths and normalized Haar measure. There is no extrapolation to higher bandwidth or unequal windows.

## References

- F. Marceca, J. L. Romero, M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685, first public January 27, 2023; see Sections 1 and 4 on nonconvex Fourier concentration.
- L. D. Abreu, M. Speckbacher, *Optimal concentration in the Paley-Wiener space*, arXiv:2607.19192, July 21, 2026; see Theorems 1.1 and 2.1, concerning the maximal eigenvalue and interval extremality.
- The classical Slepian–Landau–Pollak concentration-operator formulation (background); standard Fourier-series orthogonality and finite-dimensional Hermitian perturbation theory are used directly in the proof.
