# Log-Gamma spectral smoothing at the critical winding of weighted Bergman boundary spirals

## Finding

Fix real \(\alpha>-1\), \(\beta\ne0\), and \(\gamma>0\). In the probability-normalized weighted Bergman space \(A^2_\alpha(\mathbb D)\), define the bounded angular-spiral symbol
\[
a_{\gamma,f}(re^{i\theta})=f\!\left(e^{i(\theta-\beta[1+\log(1/(1-r^2))]^\gamma)}\right),\qquad 0<r<1,
\]
for any \(f\in C(\mathbb T)\); assign any value to the symbol at \(z=0\), a null set for the area measure. There is an explicit unitary diagonal gauge \(D_\gamma\) (defined below), independent of \(f\), such that the gauged Bergman Toeplitz operator is a compact perturbation of the Hardy Toeplitz operator with the following effective circle symbol:
\[
F_\gamma(e^{i\theta})=\begin{cases}
f(e^{i\theta}),&0<\gamma<1,\\[2pt]
\displaystyle \frac1{\Gamma(\alpha+1)}\int_0^\infty f(e^{i(\theta+\beta\log u)})u^\alpha e^{-u}\,du,&\gamma=1,\\[5pt]
f_0,&\gamma>1,
\end{cases}
\]
where \(f_0=(2\pi)^{-1}\int_0^{2\pi}f(e^{i\theta})\,d\theta\).

In particular, for every \(\lambda\in\mathbb C\), the Fredholm essential spectrum is exactly \(F_\gamma(\mathbb T)\), the essential operator norm is \(\|F_\gamma\|_\infty\), and \(T_{a_{\gamma,f}}-\lambda I\) is Fredholm exactly when \(\lambda\notin F_\gamma(\mathbb T)\); then its index is \(-\operatorname{wind}(F_\gamma-\lambda,0)\). For every nonconstant \(f\), \(T_{a_{\gamma,f}}-f_0I\) is compact **if and only if** \(\gamma>1\).

For the angular character \(f(e^{i\theta})=e^{i\theta}\), the exact essential norm is \(1\) below criticality, \(|\Gamma(\alpha+1+i\beta)|/\Gamma(\alpha+1)\) at criticality, and \(0\) above it. In the unweighted case \(\alpha=0\), the middle value is \(\sqrt{\pi|\beta|/\sinh(\pi|\beta|)}\).

## Assumptions and scope

Write \(d\mu_\alpha(z)=(\alpha+1)\pi^{-1}(1-|z|^2)^\alpha\,dx\,dy\). The Toeplitz compression \(T_a=P_\alpha M_a|_{A^2_\alpha}\) is bounded whenever \(a\in L^\infty(\mathbb D)\). The normalized monomials are
\[
e_n(z)=\frac{z^n}{\sqrt{q_n}},\qquad q_n=(\alpha+1)B(n+1,\alpha+1),\quad n=0,1,\ldots .
\]
Let \(J:A^2_\alpha\to H^2(\mathbb T)\) be the unitary sending \(e_n\) to \(z^n\). Define \(h_0=0\) and \(h_n=-\beta\sum_{j=1}^n(1+\log j)^\gamma\) for \(n\ge1\), and let \(D_\gamma e_n=e^{ih_n}e_n\). The exact normal form is
\[
D_\gamma^*T_{a_{\gamma,f}}D_\gamma-J^*T^{H^2}_{F_\gamma}J\in\mathcal K(A^2_\alpha).
\]
The parameters \(\alpha,\beta,\gamma\) are fixed; the symbol \(f\) is continuous but may be complex-valued. Essential spectrum means the spectrum in the Calkin algebra, equivalently the complement of Fredholm shifts.

## Proof

**1. Exact weighted monomial matrix.** Let \(f(e^{i\theta})=\sum_{k\in\mathbb Z}f_ke^{ik\theta}\) initially be a trigonometric polynomial. For each fixed integer \(k\) and \(n\ge\max(0,-k)\), angular orthogonality and the substitution \(s=r^2\) give
\[
\langle T_{a_{\gamma,f}}e_n,e_{n+k}\rangle=f_kJ_{n,k}^{(\gamma)},\quad
J_{n,k}^{(\gamma)}=\frac{\displaystyle\int_0^1s^{n+k/2}(1-s)^\alpha e^{-ik\beta[1+\log(1/(1-s))]^\gamma}\,ds}{\sqrt{B(n+1,\alpha+1)B(n+k+1,\alpha+1)}}.
\]
For \(k=0\), this coefficient is exactly \(1\). In particular, the matrix is banded for trigonometric \(f\).

**2. Radial boundary layer.** Put \(u=n(1-s)\), \(L_n=1+\log n\), and let \(w_{n,k}\) be the positive density factor resulting from the last integral, with no phase. For every fixed \(k\),
\[
w_{n,k}(u)\longrightarrow w_\alpha(u)=\frac{u^\alpha e^{-u}}{\Gamma(\alpha+1)}\quad\text{in }L^1(0,\infty).
\]
Indeed, \(B(n+1,\alpha+1)\sim\Gamma(\alpha+1)n^{-\alpha-1}\). On the support \(0<u<n\), the densities converge pointwise, and for all sufficiently large \(n\) they are dominated by a constant times \(u^\alpha e^{-u/2}\). Thus the convergence is in \(L^1\), also when \(-1<\alpha<0\).

**3. The sharp phase trichotomy.** The remaining oscillatory factor equals
\[
\exp\{-ik\beta[(L_n-\log u)^\gamma-L_n^\gamma]\}.
\]
When \(0<\gamma<1\), its exponent tends to zero for each fixed \(u>0\), so dominated convergence gives the limiting coefficient \(1\). When \(\gamma=1\), it is exactly \(u^{ik\beta}\), with limiting integral
\[
m_k=\int_0^\infty u^{ik\beta}w_\alpha(u)\,du
=\frac{\Gamma(\alpha+1+ik\beta)}{\Gamma(\alpha+1)}.
\]
When \(\gamma>1\) and \(k\ne0\), split the integral at \(u=\varepsilon\) and \(u=M\), keeping the tails arbitrarily small by uniform \(L^1\) control. On \([\varepsilon,M]\), the derivative of the phase has absolute size comparable to \(|k\beta|\gamma L_n^{\gamma-1}/u\), and has no zeros. Integration by parts gives an \(O(L_n^{1-\gamma})\) bound; the density and its first derivative are uniformly bounded on this compact interval. Consequently the coefficient tends to zero. (The case \(k=0\) remains one.)

**4. Remove the rotating scalar phase.** For any fixed \(k\), the diagonal unitary satisfies
\[
h_n-h_{n+k}=k\beta L_n^\gamma+o(1),\qquad n\to\infty.
\]
Thus the \((n+k,n)\) matrix entry of \(D_\gamma^*T_{a_{\gamma,f}}D_\gamma\) tends to \(f_k\), \(f_km_k\), or \(f_k\mathbf1_{k=0}\), respectively. For trigonometric \(f\), the difference from the corresponding constant-diagonal Hardy Toeplitz matrix is a finite sum of weighted shifts whose weights tend to zero; each such shift is compact by finite-rank truncation.

For general \(f\in C(\mathbb T)\), approximate uniformly by trigonometric polynomials. The Bergman compression has norm at most \(\|f\|_\infty\); the limiting circle-symbol map has the same contractive bound because the critical map is averaging against the probability density \(w_\alpha\). Compact operators are norm closed. The exact normal form therefore holds for every continuous \(f\).

**5. Spectral and sharpness consequences.** The standard continuous-symbol Hardy Toeplitz extension identifies its Calkin symbol with \(F_\gamma\). Its essential norm is \(\|F_\gamma\|_\infty\); its Fredholm essential spectrum is \(F_\gamma(\mathbb T)\), and the Fredholm index outside that set is minus the winding number. Unitary conjugation and compact perturbations preserve these assertions. Finally, for \(\gamma=1\), every Fourier multiplier \(m_k\) is nonzero because the Gamma function has no zeros. Thus \(F_1\) is nonconstant exactly when \(f\) is nonconstant. The same holds for \(0<\gamma<1\). A nonconstant Hardy Toeplitz symbol cannot represent the zero element in the Calkin algebra, proving the stated compactness dichotomy. For the explicit character example use \(|\Gamma(1+it)|^2=\pi|t|/\sinh(\pi|t|)\).

## Verification

At the critical exponent, there is also an **exact finite-degree formula**, not only an asymptotic:
\[
J_{n,k}^{(1)}=e^{-ik\beta}\frac{B(n+k/2+1,\alpha+1+ik\beta)}{\sqrt{B(n+1,\alpha+1)B(n+k+1,\alpha+1)}}.
\]
The standalone script `check.py` evaluates this identity by independent numerical quadrature for positive and negative angular shifts and two weights, compares finite-degree dephased coefficients across the three regimes, and checks the unweighted Gamma-modulus identity. Execute `python check.py` with `mpmath` installed; the observed output was `BERGMAN_SPIRAL_BETA_GAMMA_CHECKS_PASS 15`. These 15 finite tests do not certify the limiting theorem, which is proved above by boundary-layer convergence and nonstationary phase.

## Relationship to prior work

Quiroga-Barranco (2021, arXiv:2106.01980) develops monomial matrix formulas for quasi-homogeneous Toeplitz symbols and a representation-theoretic algebra framework. This supplies context for the exact matrix approach but no explicit nonlinear boundary-spiral threshold, log-Gamma angular convolution, or sharp three-way essential spectrum. Esmeral, Maximenko and Vasilevski (2015) diagonalize purely angular Toeplitz operators on weighted Bergman spaces over the **upper half-plane** and characterize slowly oscillating spectral functions; their dilation-invariant symbol family and unitary representation are not the disk's radius-dependent, phase-gauged, angular winding problem. Hagger (2017) proves general Fredholm and essential-spectrum descriptions in terms of limit operators on Bergman balls; that abstract framework does not calculate the present critical Mellin multipliers. Taskinen (2025) treats periodic **planar domains** through Floquet fibers, not logarithmically winding disk symbols. In comparison to Gaussian Fock-space shell asymptotics, the boundary layer here is Gamma rather than Gaussian, producing an asymmetric wrapped log-Gamma filter rather than a heat multiplier; there is no reduction between the two weighted holomorphic spaces that preserves this family of symbols.

## Limitations

The comparison supports a concrete new explicit classification but does not establish priority against every unpublished or unindexed result. Strong general limit-operator principles may be applicable after independent computation of limit operators. The statement concerns Fredholm essential spectrum and essential norm, not the full spectrum, isolated eigenvalues, uniform convergence in \(\gamma\) near one, or stability for discontinuous \(f\). The gauge depends on the winding parameters, and all limits fix \(\alpha,\beta,\gamma\) and each angular Fourier index.

## References

1. R. Quiroga-Barranco, *Toeplitz operators, \(\mathbb T^m\)-invariance and quasi-homogeneous symbols*, arXiv:2106.01980 (first posted 2021-06-03), especially Theorem 7.3 and Corollary 7.4. https://arxiv.org/abs/2106.01980
2. K. Esmeral, E. A. Maximenko, N. Vasilevski, *\(C^*\)-algebra generated by angular Toeplitz operators on the weighted Bergman spaces over the upper half-plane*, Integral Equations Operator Theory 83 (2015), 413–428, especially (1.4), Theorem 4.9. https://doi.org/10.1007/s00020-015-2243-4
3. R. Hagger, *The essential spectrum of Toeplitz operators on the unit ball*, arXiv:1705.04553 (2017), Theorem A and the essential-spectrum corollary. https://arxiv.org/abs/1705.04553
4. J. Taskinen, *On Bergman–Toeplitz operators in periodic planar domains*, Trans. London Math. Soc. 12 (2025), e70006, Theorems 4.1 and 5.1. https://doi.org/10.1112/tlm3.70006
5. Standard Hardy-space Toeplitz extension and index theorem (continuous symbols), e.g. R. G. Douglas, *Banach Algebra Techniques in Operator Theory*, Springer.
