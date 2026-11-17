# Logarithmically slow high-variance saturation of predator invasion under bounded Ornstein–Uhlenbeck refuge noise

## Finding

**Theorem (sharp strong-noise saturation).** Fix \(0<p<1\), \(0<\varepsilon<\min\{p,1-p\}\), and strictly positive \(a,\beta,c,k,\gamma\). Let \(N\) be standard normal, \(s>0\), and
\[
q=\frac{2\varepsilon}{\pi},\qquad
\Phi(v)=\frac{c\beta k v}{1+akv},\qquad
\Lambda(s)=-\gamma+\mathbb E\bigl[\Phi(p+q\arctan(sN))\bigr].
\]
These are the stationary-standard-deviation parametrization and ergodic predator invasion exponent for the bounded random-refuge model in Reference [1]. Set
\[
\Lambda_\infty=-\gamma+\frac{\Phi(p-\varepsilon)+\Phi(p+\varepsilon)}2,
\qquad
A=\frac{\varepsilon}{\pi}\bigl[\Phi'(p-\varepsilon)-\Phi'(p+\varepsilon)\bigr]>0.
\]
For \(t\ge0\), define
\[
Q(t)=\frac{\Phi(p+q\arctan t)+\Phi(p-q\arctan t)}2
       -\frac{\Phi(p+\varepsilon)+\Phi(p-\varepsilon)}2
\]
and the finite, parameter-dependent constant
\[
B=\int_0^1Q(t)\,dt+\int_1^\infty\left[Q(t)-\frac At\right]dt.
\]
Then, as \(s\to\infty\),
\[
\boxed{\Lambda(s)-\Lambda_\infty
=\frac{\sqrt{2/\pi}}s\left[A\log s+B+\frac A2(\log2-\gamma_{\rm E})\right]
+o\!\left(\frac1s\right),}
\]
where \(\gamma_{\rm E}\) is the Euler–Mascheroni constant. In particular,
\[
\boxed{\lim_{s\to\infty}\frac{s[\Lambda(s)-\Lambda_\infty]}{\log s}
=\frac{2\varepsilon}{\pi\sqrt{2\pi}}
\left[\frac{c\beta k}{(1+ak(p-\varepsilon))^2}
-\frac{c\beta k}{(1+ak(p+\varepsilon))^2}\right]>0.}
\]
Consequently, the finite-variance predator-invasion reversal-window width in Reference [1] approaches its maximal width with the same sharp positive logarithm-over-standard-deviation deficit. The result supplies a rate and a finite-part constant, not merely the endpoint limit.

## Assumptions and scope

The environmental forcing is the stationary Ornstein–Uhlenbeck process with mean-reversion rate \(\kappa>0\) and diffusion coefficient \(\sigma>0\), so \(s=\sigma/\sqrt{2\kappa}\) is its stationary standard deviation. The accessible prey fraction is \(p+(2\varepsilon/\pi)\arctan z^*(t)\); the band restriction ensures it remains strictly between zero and one. The biological model has logistic prey with carrying capacity \(k\), Holling-II attack and saturation coefficients \(\beta,a\), positive predator conversion \(c\), and mortality \(\gamma\). The prey intrinsic growth rate may be any positive value; it does not appear in the prey-only invasion exponent. No assumption is made about the sign of \(\Lambda(s)\) or \(\Lambda_\infty\). All limits hold for each fixed admissible parameter tuple, not uniformly over degenerate zero-amplitude or zero-saturation limits.

The statement is about the **ergodic exponent**, and therefore about a marginal Gaussian expectation, not about the convergence rate of individual environmental trajectories, random attractors, or finite-time estimates of the exponent. The independent effect of correlation time at fixed stationary standard deviation is not claimed.

## Proof

**1. Symmetric reduction.** Since \(N\) is symmetric, let
\[
H(t)=\tfrac12\{\Phi(p+q\arctan t)+\Phi(p-q\arctan t)\},\qquad t\ge0.
\]
As \(\arctan t\to\pi/2\), \(H(t)\to H_\infty=\frac12[\Phi(p+\varepsilon)+\Phi(p-\varepsilon)]\). Therefore a change of variables \(t=s|N|\) yields the exact identity
\[
\Lambda(s)-\Lambda_\infty
=\frac{2}{s\sqrt{2\pi}}\int_0^\infty
Q(t)e^{-t^2/(2s^2)}\,dt.
\tag{1}
\]
The first derivative \(\Phi'(v)=c\beta k/(1+akv)^2\) is strictly decreasing on the entire admissible interval. Thus
\[
H'(t)=\frac{q}{2(1+t^2)}\{\Phi'(p+q\arctan t)-\Phi'(p-q\arctan t)\}<0
\]
for \(t>0\). This also verifies \(Q(t)>0\) for every finite \(t\ge0\) and \(A>0\).

**2. The critical \(1/t\) tail.** From the elementary expansion
\[
\frac\pi2-\arctan t=\frac1t+O(t^{-3})\qquad(t\to\infty)
\]
and twice continuous differentiability of \(\Phi\) on the compact band, Taylor expansion at both endpoints gives
\[
\begin{aligned}
\Phi(p+q\arctan t)&=\Phi(p+\varepsilon)-\frac{q\Phi'(p+\varepsilon)}t+O(t^{-2}),\\
\Phi(p-q\arctan t)&=\Phi(p-\varepsilon)+\frac{q\Phi'(p-\varepsilon)}t+O(t^{-2}).
\end{aligned}
\]
Consequently
\[
Q(t)=\frac At+O(t^{-2}),\qquad
A=\frac q2\{\Phi'(p-\varepsilon)-\Phi'(p+\varepsilon)\}>0.
\tag{2}
\]
Define \(R(t)=Q(t)-A\mathbf1_{\{t\ge1\}}/t\). By (2), \(R\in L^1([0,\infty))\); hence \(B=\int_0^\infty R(t)dt\) is absolutely well-defined. Splitting (1) gives
\[
\Lambda(s)-\Lambda_\infty=\frac{2}{s\sqrt{2\pi}}\left[
\int_0^\infty R(t)e^{-t^2/(2s^2)}dt
+A\int_1^\infty \frac{e^{-t^2/(2s^2)}}t dt\right].
\tag{3}
\]
Dominated convergence proves the first integral tends to \(B\).

**3. Exact Gaussian boundary-layer constant.** Set \(u=t/s\) in the second integral of (3). Its value is
\[
J(s)=\int_{1/s}^\infty\frac{e^{-u^2/2}}u du
=\frac12 E_1\!\left(\frac1{2s^2}\right),
\]
where \(E_1(x)=\int_x^\infty e^{-v}dv/v\). Splitting this integral at one and integrating the convergent Taylor series of \(e^{-v}-1\) over \((0,1)\) gives
\[
E_1(x)=-\gamma_{\rm E}-\log x+O(x)\quad(x\downarrow0).
\]
Thus
\[
J(s)=\log s+\frac12(\log2-\gamma_{\rm E})+O(s^{-2}).
\tag{4}
\]
Insert dominated convergence and (4) in (3). Since \(2/\sqrt{2\pi}=\sqrt{2/\pi}\), the stated two-term expansion follows. Its leading coefficient is strictly positive, proving the sharp logarithmic rate.

**4. Invasion-reversal window.** In Reference [1], equation (8.7), the interval of mortality rates for which deterministic invasion and random extinction disagree is
\[
\mathcal W(s)=(\mathbb E\Phi(p+q\arctan(sN)),\,\Phi(p)).
\]
Its length is \(w(s)=\Phi(p)-\mathbb E\Phi(p+q\arctan(sN))\), and its limiting length is \(w_\infty=\Phi(p)-H_\infty\). Therefore \(w_\infty-w(s)=\Lambda(s)-\Lambda_\infty\), identically, giving precisely the same asymptotic expansion. This is a consequence of the single exponent theorem, not an independent dynamical stability classification.

## Verification

All critical steps are analytic. The provided `check.py` independently evaluates the two endpoint derivatives and the Gaussian integral at several standard deviations, uses quadrature for the finite part \(B\), and checks that the scaled difference from the two-term prediction decays. These finite tests are supplementary; only the estimates and integrability argument in the proof establish the asymptotic claim for all admissible parameters.

As an exact parameter benchmark, choose \(p=1/2\), \(\varepsilon=1/4\), and \(a=\beta=c=k=1\). Then
\[
A=\frac{96}{1225\pi},\qquad
\lim_{s\to\infty}\frac{s[\Lambda(s)-\Lambda_\infty]}{\log s}
=\frac{192}{1225\pi\sqrt{2\pi}}=0.01990331118\ldots.
\]
The leading and next-order coefficients are independent of the mortality rate \(\gamma\), which cancels from the difference of exponents.

## Relationship to prior work

Reference [1], Section 2.4 and Proposition 8.6, gives the exact Gaussian integral, strict monotonicity as a function of \(s\), and its two-point infinite-variance limit. Section 8.1 defines the mortality reversal window. It does not state the logarithm-over-standard-deviation convergence rate, explicit derivative coefficient, or finite-part constant computed here. Those earlier results are assumptions and inputs, not new claims.

Reference [2] introduces bounded transformations of Ornstein–Uhlenbeck forcing for logistic and Lotka–Volterra-type population systems. Reference [3] studies bounded transformed forcing in chemostat dynamics with Monod/Haldane functions and extinction/persistence conditions. Neither is the same predator-invasion Gaussian average as Reference [1], and their inspected model and theorem sections do not supply this strong-noise rate. The boundary-layer proof itself follows elementary Gaussian integration; generic facts about slowly decaying kernels and Laplace transforms remain background, not a claim of newly invented machinery.

## Limitations

The asymptotic is pointwise in fixed biological parameters; the constants may become small as \(\varepsilon\to0\) or \(a\to0\), and the formula is not asserted to be uniform in such joint limits. It treats the infinite-time ergodic invasion exponent and the length of its already-known mortality window. It does not calculate a finite-time extinction probability, a pathwise convergence rate, or an attractor convergence rate. The finite-part constant \(B\) is given by absolutely convergent one-dimensional integrals rather than elementary closed form. Priority relative to unindexed Gaussian integral tables or general regular-variation theorems is not exhaustively settled.

## References

1. E. F. Cruzado-Quispe, J. López-de-la-Cruz, and P. N. Seminario-Huertas, *Forward and pullback attraction under worst-case and ergodic exponents in a predator–prey model with bounded random refuge*, arXiv:2611.11026v1, first posted 2026-11-07, https://arxiv.org/html/2611.11026v1. Relevant exact formulas: (2.18), (2.21), (8.7), Proposition 8.6.
2. T. Caraballo, R. Colucci, J. López-de-la-Cruz, and A. Rapaport, *A way to model stochastic perturbations in population dynamics models with bounded realizations*, Communications in Nonlinear Science and Numerical Simulation 77 (2019), 239–257, https://arxiv.org/pdf/2401.06934.
3. T. Caraballo and J. López-de-la-Cruz et al., *Chemostat models with Monod and Haldane consumption functions and random environmental fluctuations*, Mathematical Methods in the Applied Sciences, https://doi.org/10.1002/mma.9061.
