# Reentrant aspect-ratio instability in two-window Gaussian localization

## Finding

A balanced pair of reciprocal squeezed-Gaussian windows exhibits a shape instability that is absent for an isotropic single Gaussian. For a fixed phase-plane area \(A>0\), define an axis-parallel rectangle with sides \(a=\sqrt A e^u\) and \(b=\sqrt A e^{-u}\), and denote by \(\mathcal H_s(A,u)\) the squared Hilbert–Schmidt norm of the associated mixed-state localization operator (precise definitions below).

**Theorem.** For every fixed squeezing \(s>1\), the square \(u=0\) is a strict local maximizer of \(u\mapsto\mathcal H_s(A,u)\) when \(A>0\) is sufficiently small, and again when \(A\) is sufficiently large. Nevertheless, for every sufficiently large \(s\), the same square is a strict local *minimizer* at the intermediate area \(A=1\). In particular, at \(A=1\) such an \(s\) has at least two distinct nonsquare globally maximizing rectangles with reciprocal aspect ratios. For every sufficiently large \(s\), the square's aspect-ratio Hessian changes sign at least twice as \(A\) increases from zero to infinity.

The signs follow from the quantitative laws
\[
\partial_u^2\mathcal H_s(A,0)=-\frac{\pi}{3}(s+s^{-1}+2\kappa_s^2)A^3+O_s(A^4)\quad(A\downarrow0),
\]
\[
\partial_u^2\mathcal H_s(A,0)=-\frac{\sqrt A}{2\pi}\big(\sqrt{s}+s^{-1/2}+2\kappa_s^{-1/2}\big)+o_s(\sqrt A)\quad(A\to\infty),
\]
\[
\partial_u^2\mathcal H_s(1,0)=\frac1{2\sqrt s}+O(s^{-1})\quad(s\to\infty),
\qquad \kappa_s=\frac2{s+s^{-1}}.
\]
The result asserts **at least** two area crossings, not exactly two, and at least a reflection-related pair of global maximizers, not uniqueness of that pair.

## Assumptions and scope

Use the Fourier/STFT normalization \(\pi(x,\xi)f(t)=e^{2\pi i\xi t}f(t-x)\). For \(r>0\), let the normalized squeezed Gaussian be \(g_r(t)=(2r)^{1/4}e^{-\pi rt^2}\). Fix \(s>1\) and define the positive trace-one operator
\[
\rho_s=\tfrac12\big(|g_s\rangle\langle g_s|+|g_{s^{-1}}\rangle\langle g_{s^{-1}}|\big).
\]
For the centered rectangle \(\Omega_{a,b}=[-a/2,a/2]\times[-b/2,b/2]\) with \(ab=A\), define the trace-class mixed localization operator
\[
L_{s,a,b}=\int_{\Omega_{a,b}}\pi(z)\rho_s\pi(z)^*\,dz,
\quad \mathcal H_s(A,u)=\|L_{s,\sqrt A e^u,\sqrt A e^{-u}}\|_{\mathrm{HS}}^2.
\]
All integrals are Lebesgue integrals. The theorem concerns the real aspect coordinate \(u\in\mathbb R\), the squared Schatten-two norm, and a balanced *incoherent* two-window mixture. It makes no assertion about a coherent sum of the two Gaussians or the operator norm.

For \(c,t>0\) write
\[
J_c(t)=\int_0^t\int_0^t e^{-\pi c(x-y)^2}\,dx\,dy
=\frac{t}{\sqrt c}\operatorname{erf}(\sqrt{\pi c}\,t)-\frac{1-e^{-\pi c t^2}}{\pi c}.
\]
The exact, all-parameter squared-norm formula is
\[
\boxed{\mathcal H_s(A,u)=\frac14\Big[J_s(a)J_{s^{-1}}(b)+J_{s^{-1}}(a)J_s(b)+2\kappa_sJ_{\kappa_s}(a)J_{\kappa_s}(b)\Big],}
\]
where \(a=\sqrt A e^u\), \(b=\sqrt A e^{-u}\), and \(\kappa_s=2/(s+s^{-1})\). In particular \(\mathcal H_s(A,u)=\mathcal H_s(A,-u)\).

## Proof

**1. The overlap and the exact formula.** Completing the square in the Gaussian integral yields, for any \(r,t>0\) and \((x,\xi)\in\mathbb R^2\),
\[
|\langle g_r,\pi(x,\xi)g_t\rangle|^2
=\frac{2\sqrt{rt}}{r+t}\exp\!\left(-\frac{2\pi}{r+t}(rtx^2+\xi^2)\right).
\]
For the two diagonal pairs this kernel is respectively \(e^{-\pi(sx^2+s^{-1}\xi^2)}\) and its coordinate swap. For the off-diagonal pairs \(r=s,t=s^{-1}\), the kernel is \(\kappa_s e^{-\pi\kappa_s(x^2+\xi^2)}\). Tracing the square of \(L_{s,a,b}\) and using covariance of time-frequency shifts gives the integral over two copies of \(\Omega_{a,b}\) of these four overlap kernels with coefficient \(1/4\). Their Cartesian products factor, proving the boxed formula and evenness in \(u\).

**2. Exact Hessian.** Introduce logarithmic derivatives \(D=t\partial_t\) and
\[
Q_c(t)=DJ_c(t)=\frac{t}{\sqrt c}\operatorname{erf}(\sqrt{\pi c}\,t),\qquad
R_c(t)=D^2J_c(t)=Q_c(t)+2t^2e^{-\pi ct^2}.
\]
Differentiate the exact formula twice in \(u\) at \(u=0\), with \(t=\sqrt A\). One obtains
\[
\begin{aligned}
\partial_u^2\mathcal H_s(A,0)
={}&\tfrac12\big[R_s(t)J_{s^{-1}}(t)+J_s(t)R_{s^{-1}}(t)-2Q_s(t)Q_{s^{-1}}(t)\big]\\
&+\kappa_s\big[J_{\kappa_s}(t)R_{\kappa_s}(t)-Q_{\kappa_s}(t)^2\big].
\end{aligned}
\]
The functions are analytic in positive parameters; the Hessian is continuous in \(A>0\).

**3. Small areas.** For each fixed \(c>0\), a Taylor expansion of the defining integral gives
\[
J_c(t)=t^2-\frac{\pi c}{6}t^4+O_c(t^6).
\]
Substituting \(a^2=Ae^{2u}\), \(b^2=Ae^{-2u}\), uniformly for \(u\) in a compact interval about zero, gives
\[
\mathcal H_s(A,u)=\frac{1+\kappa_s}{2}A^2
-\frac{\pi}{24}(s+s^{-1}+2\kappa_s^2)A^3(e^{2u}+e^{-2u})+O_s(A^4).
\]
Taking the second derivative gives the first stated asymptotic and its strictly negative sign for small positive \(A\).

**4. Large areas.** At fixed \(c>0\), the Gaussian tail and the error-function formula give, with all fixed-order logarithmic derivatives,
\[
J_c(t)=\frac{t}{\sqrt c}-\frac1{\pi c}+O_c(e^{-\pi c t^2/2}),\qquad t\to\infty.
\]
Use this in each product in the exact formula, locally uniformly in \(u\) around zero. The result is
\[
\mathcal H_s(A,u)=A-\frac{\sqrt A}{2\pi}
(\sqrt s+s^{-1/2}+2\kappa_s^{-1/2})\cosh u+C_s+o_s(1),
\]
where \(C_s\) is independent of \(u\), and the remainder and its second \(u\)-derivative are exponentially small for fixed \(s\). The stated large-area Hessian follows, and is strictly negative.

**5. Intermediate-area destabilization.** Set \(A=1\). As \(s\to\infty\), the large-parameter error-function estimates yield
\[
(J_s(1),Q_s(1),R_s(1))
=(s^{-1/2},s^{-1/2},s^{-1/2})+O(s^{-1})
\]
componentwise. The small-parameter Taylor expansions give
\[
(J_{s^{-1}}(1),Q_{s^{-1}}(1),R_{s^{-1}}(1))=(1,2,4)+O(s^{-1}).
\]
Since \(\kappa_s=2s^{-1}+O(s^{-3})\), the last (cross-window) bracket in the exact Hessian is \(O(\kappa_s)\), and its prefactor makes this an \(O(s^{-2})\) contribution. The first bracket is \(s^{-1/2}+O(s^{-1})\). This proves the positive \(\frac1{2\sqrt s}+O(s^{-1})\) law, hence strict local minimality of the square for all sufficiently large \(s\).

**6. Bifurcation and global existence.** For each fixed \(s>1,A>0\), the formula shows \(\mathcal H_s(A,u)>0\) and \(\mathcal H_s(A,u)\to0\) as \(u\to\pm\infty\): every product has one width tending to zero, and the other tending to infinity, giving \(J_c(a)J_d(b)=O_{s,A}(e^{-|u|})\). Thus a global maximum exists. When \(A=1\) and \(s\) is sufficiently large, it cannot occur at the strict local minimum \(u=0\). Evenness gives at least two distinct global maximizers \(\pm u_*\), both nonsquare. Since the Hessian is continuous in \(A\), negative for all sufficiently small or large \(A\), and positive at \(A=1\), it has at least one zero below \(1\) and another above \(1\). This concludes the theorem.

## Verification

The companion file `check_mixed_rectangles.py` independently evaluates the Gaussian overlap by one-dimensional complex quadrature, the rectangle convolution by direct double quadrature, and the closed-form Hessian by a separate centered finite difference. It also tests both instability and return to stability. Running `python check_mixed_rectangles.py` with standard-library Python prints `MIXED_SQUEEZE_RECTANGLE_PASS` on success. For illustration (not as an infinite-parameter proof), at \(s=100,A=1\) the exact-expression evaluation gives \(\mathcal H_s(1,0)\approx0.057949841761\), \(\mathcal H_s(1,2)\approx0.121454638959\), and Hessian \(\approx0.040653106987>0\). The rigorous conclusions for unbounded \(s\) and all sufficiently small/large areas come from the analytic asymptotics above, not from these samples.

## Relationship to prior work

The problem combines the general mixed-state localization-operator framework developed by Luef and Skrettingland with Hilbert–Schmidt shape optimization of time-frequency localization studied by Nicola and Riccardi. The latter source assumes one *isotropic Gaussian* analysis window, with a radial kernel and a ball as global optimizer. Here the state is a rank-two reciprocal-squeeze mixture and its overlap kernel is a *sum of incompatible anisotropic Gaussians*, so that the radial rearrangement theorem does not imply the present square instability or reentrance. Nicola and Tilli study sharp **operator-norm** inequalities for a single Gaussian-window localization operator with constrained symbols, not this mixed-state Schatten-two rectangular shape problem. The mixed-state framework itself does not select the optimal aspect ratio or exhibit area-dependent sign changes of its Hessian.

## Limitations

The theorem guarantees at least two curvature sign changes for sufficiently large \(s\); it neither counts all crossings nor determines exact critical areas, the smallest destabilizing squeezing, or the number/locations of all global optimizers. It does not prove the square is globally optimal in the small- or large-area regimes (only strictly locally optimal). The mixed window is an incoherent equal-weight density operator; the result is not an assertion about a coherent superposition, a single Gaussian window, an unrestricted shape class, or operator norm. Earlier equivalent results under other terminology cannot be definitively excluded by the literature checks.

## References

1. F. Nicola and F. Riccardi, *The quantitative isoperimetric inequality for the Hilbert–Schmidt norm of localization operators*, first public version 2024-01-09, arXiv:2401.04659. Primary MSC2020: 42B10. https://arxiv.org/abs/2401.04659
2. F. Luef and E. Skrettingland, *Mixed-state localization operators: Cohen's class and trace class operators*, first public version 2018-02-07, arXiv:1802.02435. https://arxiv.org/abs/1802.02435
3. F. Nicola and P. Tilli, *The norm of time-frequency and wavelet localization operators*, first public version 2022-07-18, arXiv:2207.08624. https://arxiv.org/abs/2207.08624
4. S. Halvdansson, *Quantum harmonic analysis on locally compact groups*, first public version 2022-10-15, arXiv:2210.08314. https://arxiv.org/abs/2210.08314
