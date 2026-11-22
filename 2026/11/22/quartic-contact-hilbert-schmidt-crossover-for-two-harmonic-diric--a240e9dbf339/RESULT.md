# Quartic-contact Hilbert–Schmidt crossover for two-harmonic Dirichlet composition

## Finding
Let \(a>0\), \(b>0\), and \(\delta>0\). Define
\[
m(a,b)=\begin{cases}-a+b,&b\le a/4,\\-b-a^2/(8b),&b>a/4,\end{cases}
\quad
\varphi_{\delta,b}(s)=\tfrac12-m(a,b)+\delta+a2^{-s}+b4^{-s}.
\]
On the Hardy space \(\mathcal H^2\) of square-summable Dirichlet coefficients, let \(F_a(\delta,b)=\|C_{\varphi_{\delta,b}}\|_{\mathcal S_2}^2\), where \(C_\varphi f=f\circ\varphi\). Then
\[
F_a(\delta,b)=\frac1{2\pi}\int_{-\pi}^{\pi}\zeta\bigl(1+2\delta+2g_b(\theta)\bigr)\,d\theta,
\qquad g_b(\theta)=a\cos\theta+b\cos2\theta-m(a,b).
\tag{1}
\]
For every fixed \(a,b>0\), as \(\delta\downarrow0\),
\[
F_a(\delta,b)\sim\begin{cases}
\displaystyle\frac{\delta^{-1/2}}{2\sqrt{2(a-4b)}},&0<b<a/4,\\[5pt]
\displaystyle2^{-7/4}a^{-1/4}\delta^{-3/4},&b=a/4,\\[5pt]
\displaystyle\frac{\delta^{-1/2}}{2\sqrt{2b(1-a^2/(16b^2))}},&b>a/4.
\end{cases}\tag{2}
\]
The critical behavior has a sharp two-parameter unfolding. Fix any \(\kappa\in\mathbb R\) and put \(b_\delta=a/4-\kappa\sqrt\delta\), which is positive for sufficiently small \(\delta\). With \(\kappa_-=\max\{-\kappa,0\}\),
\[
\boxed{\lim_{\delta\downarrow0}\delta^{3/4}F_a(\delta,b_\delta)
=\Phi_a(\kappa)
=\frac1{4\pi}\int_{\mathbb R}
\frac{dz}{1+2\kappa z^2+(a/8)z^4+8\kappa_-^2/a}}
\tag{3}
\]
and the integral is explicitly
\[
\Phi_a(\kappa)=\frac{1}{4\sqrt{1+8\kappa_-^2/a}\,\sqrt{2\kappa+2\sqrt{\kappa_-^2+a/8}}}.
\tag{4}
\]
The denominator is strictly positive. In particular \(\Phi_a(0)=2^{-7/4}a^{-1/4}\). At \(\delta=0\), no member of this one-prime family is Hilbert–Schmidt. The finding is the exact transition and unfolding, not the existence of quartic boundary contact, which is present in earlier literature.

## Assumptions and scope
The Hilbert space is \(\mathcal H^2=\{f(s)=\sum_{n\ge1}c_n n^{-s}:\sum_{n\ge1}|c_n|^2<\infty\}\). The map \(\varphi_{\delta,b}\) is analytic on the open right half-plane and takes values in the half-plane \(\operatorname{Re}w>1/2\), because \(m(a,b)\) is the minimum of its boundary trigonometric polynomial and \(\delta>0\). Thus the standard characteristic-zero composition-operator criterion applies. The parameter \(a\) is fixed and positive. Equations (2) and (3) use different limits: the first fixes \(b\); the second varies \(b\) on the critical \(\sqrt\delta\) scale with fixed \(\kappa\). No uniformity as \(|\kappa|\to\infty\), \(a\to0\), or \(b\to0\) is asserted.

## Proof
**1. Minimum and positive gap.** Let \(x=1+\cos\theta\in[0,2]\) and \(\eta=a/4-b\). Completing the square in the quadratic polynomial in \(\cos\theta\) yields the exact nonnegative identity
\[
 g_b(\theta)=4\eta x+2b x^2+\frac{2\eta_-^2}{b},
\qquad\eta_-=\max\{-\eta,0\}.
\tag{5}
\]
For \(\eta\ge0\) its sole minimizing point on the circle is \(\theta=\pi\); for \(\eta<0\) the two minimizing points satisfy \(x=-\eta/b\), equivalent to \(\cos\theta=-a/(4b)\). Evaluating the minimum gives exactly the displayed \(m(a,b)\).

**2. Exact Hilbert–Schmidt identity.** The canonical basis of \(\mathcal H^2\) is \(e_n(s)=n^{-s}\). Writing \(c=1/2-m(a,b)+\delta\), we have
\[
 C_{\varphi_{\delta,b}}e_n(s)
=n^{-c}\exp[-a(\log n)2^{-s}-b(\log n)4^{-s}].
\]
Expanding the exponential in powers of \(2^{-s}\), the coefficients occupy only the powers of one prime; Parseval on the single circle gives
\[
\|C_{\varphi_{\delta,b}}e_n\|^2
=\frac{n^{-2c}}{2\pi}\int_{-\pi}^{\pi}
\exp[-2(\log n)(a\cos\theta+b\cos2\theta)]\,d\theta.
\]
Summing over \(n\ge1\) and using Tonelli proves (1), since the total exponent is \(1+2\delta+2g_b(\theta)>1\). In particular the symbol induces a Hilbert–Schmidt operator when \(\delta>0\).

**3. Uniform reduction to a rational singular integral.** The function \(\zeta(1+t)-t^{-1}\) extends continuously to \(t=0\) and is bounded on each compact subset of \([0,\infty)\). For fixed \(a\) and \(b\) in a compact positive neighborhood of \(a/4\), the gap \(g_b\) is uniformly bounded. Thus, uniformly for small \(\delta\),
\[
F_a(\delta,b)=\frac1{4\pi}\int_{-\pi}^{\pi}\frac{d\theta}{\delta+g_b(\theta)}+O_a(1).
\tag{6}
\]
The same relation holds with \(b\) any fixed positive value, with a constant that may depend on \(b\).

**4. Three fixed-parameter regimes.** If \(b<a/4\), around the unique circle minimum \(\theta=\pi\), (5) gives
\(g_b(\pi+q)=\tfrac12(a-4b)q^2+O_{a,b}(q^4)\).
For \(b>a/4\), there are two separated minima \(\theta_\pm\), each with
\(g_b(\theta_\pm+q)=2b(1-a^2/(16b^2))q^2+O_{a,b}(q^3)\).
At \(b=a/4\), the unique minimum instead has
\(g_b(\pi+q)=(a/8)q^4+O_a(q^6)\).
Split the integral (6) into disjoint small neighborhoods of minima and their compact complement. The latter contributes \(O(1)\). Rescaling \(q=\sqrt\delta\,z\) in each quadratic well and \(q=\delta^{1/4}z\) in the quartic well, and using
\(\int_{\mathbb R}(1+z^2)^{-1}dz=\pi\) and
\(\int_{\mathbb R}(1+z^4)^{-1}dz=\pi/\sqrt2\), gives exactly the three constants (2). Restricting (6) to these neighborhoods at \(\delta=0\) proves the non-Hilbert–Schmidt endpoint assertion.

**5. Critical unfolding.** Fix \(\kappa\in\mathbb R\). In (5) take \(\eta=\kappa\sqrt\delta\), \(b=a/4-\kappa\sqrt\delta\), and write \(\theta=\pi+\delta^{1/4}z\). Since \(x=1-\cos(\delta^{1/4}z)=\tfrac12\delta^{1/2}z^2+O(\delta z^4)\), we obtain, locally uniformly in \(z\),
\[
\frac{\delta+g_b(\theta)}\delta
\longrightarrow 1+2\kappa z^2+\frac a8 z^4+\frac{8\kappa_-^2}{a}.
\tag{7}
\]
The limiting polynomial is \(1+(a/8)z^4+2\kappa z^2+8\kappa_-^2/a\), strictly positive: if \(\kappa\ge0\), this is immediate; if \(\kappa<0\), it equals \(1+(a/8)(z^2+8\kappa/a)^2\). To justify passing to the full real-line integral, note that (5) completes to \(2b(x+\eta/b)^2\) when \(\eta<0\). For \(|\theta-\pi|\le\rho\) small and \(\delta\) small, \(x\) is comparable to \((\theta-\pi)^2\); outside \(\rho\), the gap is uniformly positive. Choose a sufficiently large fixed \(R\) depending on \(\kappa\). On \(R\delta^{1/4}\le|\theta-\pi|\le\rho\), the quartic positive term dominates the quadratic detuning, and the rescaled integrand is bounded by \(C/(1+|z|^4)\); on \(|z|\le R\), (7) provides a positive uniform lower bound. Dominated convergence, followed by \(R\to\infty\), proves (3). The standard quartic rational integral
\[
\int_{\mathbb R}\frac{dz}{A z^4+Bz^2+C}
=\frac{\pi}{\sqrt C\sqrt{B+2\sqrt{AC}}},
\quad A,C>0,\quad B>-2\sqrt{AC},
\]
applied to \(A=a/8\), \(B=2\kappa\), \(C=1+8\kappa_-^2/a\), proves (4). Its conditions hold strictly by the previous sum-of-squares observation.

## Verification
The supplied `checker.py` independently evaluates the exact angular-zeta norm, the fixed-parameter coefficients, the critical unfolding integral and its closed form, and the trigonometric minimum. Its finite tests corroborate the formulas; no finite grid establishes an infinite-dimensional limit. Run `python checker.py` with Python 3 and its listed SciPy dependency. Equations (1), (5), (6), and the dominated-convergence argument constitute the proof.

## Relationship to prior work
Bayart and Kouroupis (2023) give general Schatten criteria and even-Schatten trace methods for Hardy–Dirichlet composition operators. Bayart and Brevig (2015), particularly their treatment of one-prime quadratic symbols and fourth-order boundary contact, already identify the *possibility of quartic tangency* and develop compactness/approximation-number bounds; neither quartic contact nor the mere noncompactness at that endpoint is claimed as new here. The present result supplies the exact Hilbert–Schmidt mass for the **correlated one-prime two-harmonic symbol**, all three sharp fixed-parameter constants, and a normalized real-translation/critical-detuning crossover function. The 2026 published independent-prime Bessel Hilbert–Schmidt Abel law and two-prime Schatten-four cusp have different Gram structures, so their stated results do not imply (3) without the new single-circle analysis.

## Limitations
These statements concern this explicit degree-two one-prime symbol family, fixed positive \(a\), positive \(b\), and real positive translation. The crossover is pointwise in fixed \(\kappa\), not uniform over the entire real line. The existence of the quartic contact is known; the asserted contribution is the exact Hilbert–Schmidt crossover and coefficients. The argument invokes classical Parseval, the zeta Laurent expansion and rational quartic integration. Priority against every older specialized treatment has not been independently certified. Independent mathematical audit has not been performed.

## References
1. F. Bayart and A. Kouroupis, *Schatten class composition operators on the Hardy space of Dirichlet series and a comparison-type principle*, arXiv:2306.05733v1 (first public 2023-06-09), https://arxiv.org/abs/2306.05733.
2. F. Bayart and O. F. Brevig, *Compact composition operators with non-linear symbols on the Hardy space of Dirichlet series*, arXiv:1505.02944v1 (first public 2015-05-12), https://arxiv.org/abs/1505.02944.
3. O. F. Brevig and K.-M. Perfekt, *Norms of composition operators on the \(H^2\) space of Dirichlet series*, arXiv:1903.08886 (2019), https://arxiv.org/abs/1903.08886.
4. *A five-regime Abel boundary law for Bessel-weighted Dirichlet series*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-five-regime-abel-boundary-law-for-bessel-weighted-dirichlet-se--a15e83fc48f6.
5. *A sharp two-prime Schatten-four boundary cusp for Dirichlet composition operators*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-two-prime-schatten-four-boundary-cusp-for-dirichlet-comp--c52ca777e421.
