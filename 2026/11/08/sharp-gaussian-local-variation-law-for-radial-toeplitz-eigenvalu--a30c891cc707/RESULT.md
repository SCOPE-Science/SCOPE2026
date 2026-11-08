# Sharp Gaussian local-variation law for radial Toeplitz eigenvalues on power-log Fock spaces

## Finding
For every real \(\alpha>1\), define the radial weight \(h_\alpha(r)=\frac12(\log_+ r)^\alpha\), where \(\log_+r=\max\{\log r,0\}\), and the Hilbert space \(\mathcal F_\alpha=\{f\text{ entire}:\int_{\mathbb C}|f(z)|^2e^{-2h_\alpha(|z|)}dA(z)<\infty\}\). For every bounded radial symbol \(\varphi\), write \(\lambda_m(\varphi)\) for the eigenvalue of \(T_\varphi\) on the monomial \(z^m\). Let \(\Phi\) denote the standard normal cumulative distribution function and put
\[
 u_m=\left(\frac{2(m+1)}{\alpha}\right)^{1/(\alpha-1)},\qquad
 s_m=\bigl[\alpha(\alpha-1)u_m^{\alpha-2}\bigr]^{-1/2}.
\]
For any integer-valued sequence \(q_m\ge0\) with \(q_m=o(m)\) and \(q_ms_m\to\eta\in[0,\infty]\), the **sharp, symbol-uniform Gaussian crossover** is
\[
 \boxed{\lim_{m\to\infty}\sup_{\substack{\varphi\text{ bounded radial}\\\|\varphi\|_\infty\le1}}
 |\lambda_{m+q_m}(\varphi)-\lambda_m(\varphi)|
 =4\Phi(\eta)-2.}
\]
By convention \(\Phi(\infty)=1\). In particular, for \(\alpha>2\) the critical degree scale is \(m^{\beta_\alpha}\) with \(\beta_\alpha=(\alpha-2)/(2(\alpha-1))\): every bounded radial symbol has asymptotically equal eigenvalues across \(o(m^{\beta_\alpha})\) gaps, while gaps of order \(m^{\beta_\alpha}\) have the explicit Gaussian crossover. For \(\alpha=2\), the optimal adjacent-index difference tends to \(4\Phi(1/\sqrt2)-2\). For \(1<\alpha<2\), that adjacent-index difference tends to \(2\).

The failure of the square-root index metric can always be realized by **one smooth symbol**: for every \(\alpha>1\) there is a real, radial \(\varphi\in C^\infty(\mathbb C)\), \(|\varphi|\le1\), with each positive-order real partial derivative tending to zero as \(|z|\to\infty\), and integer pairs \(m_j<n_j\) for which
\[
 \sqrt{n_j}-\sqrt{m_j}\to0,\qquad
 \lambda_{m_j}(\varphi)\to1,\qquad
 \lambda_{n_j}(\varphi)\to-1.
\]
Thus the strongest possible defect \(2\) is achieved in the limit by a single regular symbol, not merely by symbols optimized separately for each degree pair.

## Assumptions and scope
The parameter \(\alpha>1\) is fixed. The weight is continuous and nonnegative; its moments of every polynomial degree are finite. No global smoothness of the weight at \(|z|=1\) is assumed. Toeplitz operators are compressions of multiplication by bounded symbols to the closed entire-function subspace. Monomials form an orthogonal basis by the radial norm and Taylor expansion. All norms in the supremum are essential \(L^\infty\) norms, and the supremum is over **all** complex-valued bounded radial symbols; it is unchanged if restricted to real-valued symbols. The asymptotic statement requires integer gaps \(q_m=o(m)\). The maximizing symbol in the finite-index supremum may depend on the index; the final smooth-symbol assertion is a separate single-symbol construction.

## Proof
**1. Diagonalization and exact statistical reduction.** Polar coordinates followed by \(u=\log r\) give
\[
 \lambda_m(\varphi)=\int_{\mathbb R}\varphi(e^u)\,d\mathsf P_m(u),\quad
 d\mathsf P_m(u)=\frac{e^{F_m(u)}}{Z_m}\,du,\quad
 F_m(u)=2(m+1)u-(u_+)^\alpha,
\]
with \(u_+=\max(u,0)\) and \(Z_m=\int_{\mathbb R}e^{F_m(u)}du\). The portion \(u\le0\) contributes \(1/[2(m+1)]\), while \(Z_m\) grows much faster. Consequently
\[
 \sup_{\|\varphi\|_\infty\le1}|\lambda_{m+q}(\varphi)-\lambda_m(\varphi)|
 =\int_{\mathbb R}|d\mathsf P_{m+q}-d\mathsf P_m|,
\]
by the sign of the signed density. This is **twice** the usual total variation distance between probability measures (the convention is important for the constant).

**2. A local Gaussian law with controlled tails.** The unique maximizer of \(F_m\) is \(u_m\), and the curvature scale at the maximum is \(s_m\). For \(u>0\), setting \(v=u/u_m\) gives the exact identity
\[
 F_m(u)-F_m(u_m)=-u_m^\alpha\bigl[v^\alpha-\alpha v+(\alpha-1)\bigr].
\]
The bracket is nonnegative, vanishes only at \(v=1\), has second derivative \(\alpha(\alpha-1)\) there, and grows at both far ends in the sense needed for Laplace's method. Since \(u_m\to\infty\) and \(s_m/u_m\to0\), the densities of \((U-u_m)/s_m\) under \(\mathsf P_m\) converge in \(L^1(\mathbb R)\) to \((2\pi)^{-1/2}e^{-x^2/2}\). Explicitly, Taylor expansion yields pointwise Gaussian convergence on compact standardized intervals; outside a fixed neighborhood of \(u_m\), the displayed strictly positive bracket gives exponentially negligible integrals, and inside it the quadratic lower bound supplies an integrable Gaussian majorant. The negative half-line has negligible relative mass. These arguments also give tightness of every standardized family.

**3. Neighboring-degree crossover.** Write \(n=m+q_m\). Differentiating the center shows
\[
 \frac{du_m}{dm}=2s_m^2,\quad
 \frac{s_n}{s_m}\to1,\quad
 \frac{u_n-u_m}{s_m}=2q_ms_m(1+o(1))
\]
whenever \(q_m=o(m)\). If \(q_ms_m\to\eta<\infty\), then after the same affine change of variable \(x=(u-u_m)/s_m\), the densities of \(\mathsf P_m\) and \(\mathsf P_n\) converge in \(L^1\) to normal densities \(\gamma(x)\) and \(\gamma(x-2\eta)\), respectively. Their \(L^1\) distance equals \(4\Phi(\eta)-2\), by splitting at their unique crossing \(x=\eta\).

If \(q_ms_m\to\infty\), the standardized centers separate by \(2q_ms_m(1+o(1))\) while their scale ratio tends to one. Select a window of width \(K_ms_m\) about \(u_m\) with \(K_m\to\infty\) but \(K_m=o(q_ms_m)\). By tightness it carries \(\mathsf P_m\)-mass tending to one and \(\mathsf P_n\)-mass tending to zero. Hence the total variation distance tends to one, and the \(L^1\) distance tends to two. The case \(q_m=0\) is exact. This establishes every \(\eta\in[0,\infty]\).

**4. Transition and smooth sharpness witness.** From the definitions,
\[
 s_m\asymp m^{-\beta_\alpha},\qquad
 \beta_\alpha=\frac{\alpha-2}{2(\alpha-1)}<\frac12.
\]
For any \(\alpha>1\), choose \(\max\{0,\beta_\alpha\}<\kappa<1/2\), choose a sufficiently rapidly growing integer sequence \(m_j\) (for instance a tail of \(\lceil e^{j^2}\rceil\)), and set \(n_j=m_j+\lfloor m_j^\kappa\rfloor\). Then \((n_j-m_j)s_{m_j}\to\infty\), while \(\sqrt{n_j}-\sqrt{m_j}\sim(n_j-m_j)/(2\sqrt{m_j})\to0\). The center separation \(\Delta_j=u_{n_j}-u_{m_j}\) satisfies \(\Delta_j/s_{m_j}\to\infty\). Choose \(h_j=\sqrt{s_{m_j}\Delta_j}\); then \(h_j/s_{m_j}\to\infty\), \(h_j/\Delta_j\to0\). Enlarging the starting index and thinning the already rapidly growing sequence makes the intervals of radius \(2h_j\) about all centers disjoint and contained in \((1,\infty)\).

Choose any smooth even cutoff \(\chi\) with \(0\le\chi\le1\), equal to one on \([-1,1]\), and supported in \((-2,2)\), and put
\[
 \Psi(u)=\sum_j\left[\chi\left(\frac{u-u_{m_j}}{h_j}\right)-\chi\left(\frac{u-u_{n_j}}{h_j}\right)\right],\quad
 \varphi(z)=\begin{cases}\Psi(\log|z|),&|z|>1,\\0,&|z|\le1.\end{cases}
\]
The sum is locally finite; its supports are disjoint, so \(|\varphi|\le1\). As \(h_j\) and the center positions are powers of \(m_j\), every derivative \(\Psi^{(k)}\) grows at most polynomially in the local logarithmic radius \(u\). Each \(k\)-th spatial derivative of \(\varphi\) includes a factor \(|z|^{-k}\) times such polynomial bounds, hence tends to zero at infinity. The function vanishes near the unit circle, so is globally smooth. Tightness from Step 2 and \(h_j/s_{m_j}\to\infty\), \(h_j/s_{n_j}\to\infty\) show that the corresponding probabilities concentrate where \(\varphi=+1\) and \(\varphi=-1\), respectively. Therefore \(\lambda_{m_j}(\varphi)\to1\) and \(\lambda_{n_j}(\varphi)\to-1\).

## Verification
The exact operator-to-probability identification, the \(L^1\) Gaussian limit, the center-spacing derivative, and the two-normal total variation formula provide a complete analytical proof. A separate numerical checker evaluates the two saddle-point probability densities by normalized quadrature in logarithmic coordinates and compares their \(L^1\) distance with \(4\Phi(qs_m)-2\) for representative large degrees and parameters. Those checks test normalization and constants but are not used to infer the general theorem. Run \(python3 CHECK.py\) with a standard Python 3 interpreter; the script uses only the standard library.

## Relationship to prior work
Bdarneh's 2026 work (arXiv:2609.20652, §9) gives the one-exponent \(\alpha=3/2\) failure of square-root-metric continuity using a bounded **piecewise-defined** radial symbol; its general radial eigenvalue formula is used as the starting point. The present result supplies an all-exponent quantitative Gaussian variation law, the sharp local degree scale (including a critical transition at \(\alpha=2\)), and a single globally smooth symbol attaining the maximal defect for every exponent. Esmeral--Maximenko (arXiv:1505.07906) proves square-root-metric uniform continuity for the classical Gaussian Fock weight, which is not the power-logarithmic weight here. Neither result states this variation law. Relevant published findings involving logarithmic spectral filters for smooth radial *Gaussian* Fock Toeplitz operators address logarithmic singular-value sums/Dixmier traces, not pairwise eigenvalue total variation in small Fock spaces. The relationship is by precise statements and hypotheses, not a claim of proved global novelty.

## Limitations
The Gaussian crossover concerns \(q_m=o(m)\), with the exponent \(\alpha\) fixed. It is an asymptotic optimal bound, not a finite-degree equality to the normal formula. The separate single-symbol construction is non-explicit only in choosing a smooth compactly supported cutoff and a sufficiently sparse index tail, and gives no monotone symbol. All operators and symbols are one-dimensional, radial, and based on the specified logarithmic weight. Publication priority may be affected by broader unstated results on exponential families or Fock Toeplitz algebras; no independent review has been conducted.

## References
1. Khalid Bdarneh, *Toeplitz \(C^*\)-algebras on Radially Weighted Fock Spaces: Commutativity and Spectral Representation*, first public September 17, 2026, arXiv:2609.20652, especially Theorem 9.1 and its proof, https://arxiv.org/abs/2609.20652.
2. Kevin Esmeral and Egor A. Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906 (2015), https://arxiv.org/abs/1505.07906.
3. Vishwa Dewage and Gestur Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (2021), https://arxiv.org/abs/2107.01465.
