# Critical angular-chirp smoothing of Gaussian Fock localization

## Finding
For a continuous angular profile \(f\) on the unit circle, a bounded Gaussian Fock-space Toeplitz symbol with radial angular chirp \(a(re^{i\theta})=f(\theta-\beta r^{\gamma})\) has three distinct regimes, separated at \(\gamma=1\). Up to a concrete diagonal-unitary conjugation and a compact remainder, the operator is the Hardy Toeplitz operator with symbol \(f\) for \(0<\gamma<1\), the Hardy Toeplitz operator with the circle-heat-smoothed symbol \(H_{\beta^2/8}f\) for \(\gamma=1\), and the scalar \(f_0 I\) for \(\gamma>1\). This yields exact essential spectra, essential norms and Fredholm indices. For nonconstant \(f\), the centered operator is compact exactly when \(\gamma>1\).

## Assumptions and scope
Let \(\mathcal F^2\) be the Hilbert space of entire functions with norm
\[
\|F\|_{\mathcal F^2}^2=\pi^{-1}\int_{\mathbb C}|F(z)|^2e^{-|z|^2}\,dA(z),\quad e_n(z)=z^n/\sqrt{n!},\quad n\ge0.
\]
Choose \(f\in C(\mathbb T)\) complex-valued, \(\beta\in\mathbb R\setminus\{0\}\), \(\gamma>0\). Write \(f_k=(2\pi)^{-1}\int_0^{2\pi}f(e^{i\theta})e^{-ik\theta}\,d\theta\), \(f_0\) for its mean. Define \(a_{\gamma,\beta,f}(re^{i\theta})=f(e^{i(\theta-\beta r^\gamma)})\) for \(r>0\), with any value at the origin. Let \(T_a=P_{\mathcal F^2}M_a|_{\mathcal F^2}\). Identify the basis \(e_n\) with \(z^n\) in \(H^2(\mathbb T)\), and denote its ordinary Toeplitz operator with symbol \(g\) by \(T_g^H\).

For \(t>0\) define \(H_t f=\sum_{k\in\mathbb Z}e^{-tk^2}f_ke^{ik\theta}\), the circle heat convolution. Set \(S_0=0\), \(S_n=\sum_{j=1}^n j^{\gamma/2}\), and \(U_{\gamma,\beta}e_n=e^{-i\beta S_n}e_n\). Let \(K\) denote some compact operator (which depends on the parameters).

**Operator classification.** In this normalization,
\[
T_{a_{\gamma,\beta,f}}=\begin{cases}
U_{\gamma,\beta}T_f^H U_{\gamma,\beta}^*+K,&0<\gamma<1,\\
U_{\gamma,\beta}T_{H_{\beta^2/8}f}^H U_{\gamma,\beta}^*+K,&\gamma=1,\\
f_0 I+K,&\gamma>1.
\end{cases}
\]
Consequently define \(g_\gamma=f\) for \(\gamma<1\), \(g_1=H_{\beta^2/8}f\) for \(\gamma=1\), and \(g_\gamma\equiv f_0\) for \(\gamma>1\). For all choices as above,
\[
\sigma_{\mathrm{ess}}(T_a)=g_\gamma(\mathbb T),\quad
\|T_a\|_{\mathrm{ess}}=\max_{\theta}|g_\gamma(e^{i\theta})|.
\]
For \(\lambda\notin g_\gamma(\mathbb T)\), the Fredholm index is \(-\operatorname{wind}(g_\gamma-\lambda,0)\). In particular \(T_a-f_0I\) is compact if \(\gamma>1\); conversely, if \(f\) is nonconstant and \(0<\gamma\le1\), it is not compact.

## Proof
**Exact Fourier matrix.** For a single mode \(f(e^{i\theta})=e^{ik\theta}\), \(k\in\mathbb Z\), the only possibly nonzero coefficient from \(e_n\) to \(e_{n+k}\) (where \(n+k\ge0\)) is
\[
\langle T_a e_n,e_{n+k}\rangle=
\frac{1}{\sqrt{n!(n+k)!}}\int_0^\infty 2r^{2n+k+1}e^{-r^2}e^{-i\beta kr^\gamma}\,dr.
\]
Put \(\alpha_{n,k}=n+k/2+1\). With \(X_{n,k}\sim\operatorname{Gamma}(\alpha_{n,k},1)\), \(R_{n,k}=\sqrt{X_{n,k}}\), the last coefficient is
\[
A_{n,k}\,\mathbb E[e^{-i\beta k R_{n,k}^\gamma}],\qquad
A_{n,k}=\frac{\Gamma(\alpha_{n,k})}{\sqrt{n!(n+k)!}}\longrightarrow1.
\]
The convergence of \(A_{n,k}\) is the fixed-shift Gamma-ratio asymptotic, valid also for negative fixed \(k\).

**Gaussian shell limit.** Define \(Y_{n,k}=R_{n,k}-\sqrt n\). Its density on \(( -\sqrt n,\infty)\) is
\[
p_{n,k}(s)=\frac{2(\sqrt n+s)^{2n+k+1}e^{-(\sqrt n+s)^2}}{\Gamma(n+k/2+1)}.
\]
For each fixed real \(s\), Stirling's formula and Taylor expansion of \(\log(1+s/\sqrt n)\) give \(p_{n,k}(s)\to\sqrt{2/\pi}e^{-2s^2}\). Since both sides are probability densities, Scheffé's lemma upgrades this to \(L^1(ds)\) convergence. In particular \(Y_{n,k}\) is tight and converges to a centered Gaussian of variance \(1/4\).

Let \(q=\gamma/2\). If \(0<\gamma<1\), on every bounded \(s\)-interval one has \((\sqrt n+s)^\gamma-n^q\to0\). Tightness then gives
\[
e^{i\beta kn^q}\,\mathbb E[e^{-i\beta kR_{n,k}^\gamma}]\to1.
\]
If \(\gamma=1\), the same ratio instead tends to \(\mathbb E[e^{-i\beta kY}]=e^{-\beta^2k^2/8}\) where \(Y\sim N(0,1/4)\). If \(\gamma>1\) and \(k\ne0\), for fixed \(M\) replace \(p_{n,k}\) on \([-M,M]\) by its \(L^1\)-limit, then integrate by parts against the oscillatory phase \(\beta k(\sqrt n+s)^\gamma\). Its derivative has modulus asymptotic to \(|\beta k|\gamma n^{(\gamma-1)/2}\to\infty\) uniformly for \(|s|\le M\), and its reciprocal has derivative uniformly tending to zero. Thus the compact-interval integral tends to zero. The remaining tails are uniformly small by tightness, so the entire expectation tends to zero. When \(k=0\), the matrix is exactly \(I\).

**Compact reduction.** For any fixed integer \(k\), if \(0<\gamma\le1\),
\[
S_{n+k}-S_n=kn^{\gamma/2}+o(1)
\]
as \(n\to\infty\). Therefore the diagonal-unitary ratio \(e^{-i\beta(S_{n+k}-S_n)}\) matches the limiting oscillatory coefficient for each fixed Fourier mode. In the subcritical case the comparison has weight \(1\); at criticality it has weight \(e^{-\beta^2 k^2/8}\). For \(\gamma>1\), each fixed nonconstant Fourier mode has weights tending to zero. Two finite-band weighted shifts whose diagonal weights differ by a sequence tending to zero differ by a compact operator. Hence the asserted operator classification holds for every trigonometric polynomial \(f\).

For general \(f\in C(\mathbb T)\), choose trigonometric polynomials uniformly approximating \(f\). The Fock Toeplitz map, ordinary Hardy Toeplitz map, and circle heat convolution are all contractions in the supremum norm, and the compact operators are norm-closed. Thus the same classification holds for every continuous \(f\).

**Essential consequences.** A continuous-symbol Hardy Toeplitz operator has essential spectrum exactly the range of its symbol, essential norm its supremum norm, and Fredholm index the negative winding of the symbol minus \(\lambda\). These properties survive unitary conjugation and compact perturbation. For \(\gamma>1\), the statement is immediate for a scalar plus a compact operator. Finally if \(f\) is nonconstant then \(f-f_0\) and \(H_{\beta^2/8}(f-f_0)\) are nonzero continuous functions (the heat Fourier multipliers never vanish); their Hardy Toeplitz essential norms are positive, proving the claimed sharp compactness boundary.

## Verification
The included standalone `verify.py` uses only Python 3 standard libraries. It evaluates the exact Gamma-shell Fourier coefficients by high-resolution Simpson quadrature for Fourier modes \(k=1,2\), dimensions \(n=64,256,1024\), and powers \(\gamma\in\{1/2,1,2\}\). At \(\gamma=2\) the exact identity is
\[
\mathbb E[e^{-i\beta kR^2}]=(1+i\beta k)^{-(n+k/2+1)},
\]
providing an independent normalization check. The program also checks nine Gamma-ratio bounds. The universal compactness and spectral claims are proved above, not inferred from numerical experiments.

Run from a directory containing the artifact: `python3 verify.py`.

## Relationship to prior work
Fulsche (2024, arXiv:2405.15496), especially Theorem 2.4, gives the general limit-operator description of essential spectra for Fock Toeplitz operators; that description alone does not compute these explicit diagonal gauges, radial angular-power thresholds, heat smoothing, or winding indices. Wu and Zheng (2021, arXiv:2103.03458) study Fourier representations, boundedness, and compactness criteria for Fock Toeplitz operators but do not identify the three regimes here. Dewage and Olafsson (2021, arXiv:2107.01465) provide spectral analysis for quasi-radial symbols, whereas the present symbols have nontrivial angular-frequency modulation and are not quasi-radial. Classical continuous-symbol Hardy Toeplitz Fredholm theory is used as an established tool, not claimed as new.

## Limitations
The result requires a fixed nonzero \(\beta\) and a continuous angular profile; discontinuous or merely measurable profiles are not covered. It establishes equivalence modulo compact operators and exact essential information, but not the full operator spectrum, finite-dimensional eigenvalues, quantitative compact approximation rates, or uniform limits when \(\gamma\to1\). Historical priority is subject to the possibility of a broader unlocated result yielding the same concrete three-way phase transition.

## References
1. R. Fulsche, *Essential positivity for Toeplitz operators on the Fock space*, arXiv:2405.15496 (first posted 2024-05-24), https://arxiv.org/abs/2405.15496.
2. S. Wu and D. Zheng, *Toeplitz operators on the Fock space via the Fourier transform*, arXiv:2103.03458 (2021-03-05), https://arxiv.org/abs/2103.03458.
3. V. Dewage and G. Olafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (2021-07-03), https://arxiv.org/abs/2107.01465.
