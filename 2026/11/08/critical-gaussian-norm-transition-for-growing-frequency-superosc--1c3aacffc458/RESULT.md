# Critical Gaussian-norm transition for growing-frequency superoscillations

## Finding

Consider the standard bounded-frequency superoscillatory sequence
\[
F_n(x,a)=\bigl(\cos(x/n)+ia\sin(x/n)\bigr)^n,
\qquad n\in\mathbb N,\quad x\in\mathbb R.
\]
Let the target oscillation parameter grow with degree, rather than remain fixed: for every fixed \(c>0\), set \(a_n=\sqrt{1+cn}\) and
\[
\psi_{n,c}(x)=\pi^{-1/4}e^{-x^2/2}F_n(x,a_n),\qquad
S_n(c)=\|\psi_{n,c}\|_{L^2(\mathbb R)}^2.
\]
These are finite superpositions of Gaussian-windowed Fourier modes whose frequencies remain in \([-1,1]\). Their Segal–Bargmann transforms have exactly the same squared norm \(S_n(c)\). The following three-regime law and associated mass-distribution transition hold **for every fixed** \(c>0\) as \(n\to\infty\):
\[
\boxed{
S_n(c)\sim
\begin{cases}
(1-c)^{-1/2},&0<c<1,\\
\dfrac{2^{-3/4}\Gamma(1/4)}{\sqrt\pi}\,n^{1/4},&c=1,\\
\sqrt{\dfrac{2c}{c-1}}\exp\!\left[-\dfrac{(c-1)^2}{3c^2}\right]
\exp\!\left[n\!\left(\log c-1+\dfrac1c\right)\right],&c>1.
\end{cases}}
\]
Here \(f_n\sim g_n\) means \(f_n/g_n\to1\); in the first regime the statement is convergence to the indicated constant. The critical exponent \(1/4\), the exponential rate above criticality, and the multiplicative constant in that exponential regime are sharp.

Normalize the spatial intensity to a probability measure \(d\mu_{n,c}(x)=|\psi_{n,c}(x)|^2\,dx/S_n(c)\). In the subcritical regime, \(\mu_{n,c}\) converges in total variation to the density \(\sqrt{(1-c)/\pi}\,e^{-(1-c)x^2}\). At \(c=1\), the pushforward under \(x\mapsto x/n^{1/4}\) converges in total variation to the probability density
\[
\frac{e^{-u^4/2}}{2^{-3/4}\Gamma(1/4)}\,du.
\]
For \(c>1\), the pushforward under \(x\mapsto x/\sqrt n\) converges weakly to
\[
\frac12\delta_{\sqrt{(c-1)/c}}+\frac12\delta_{-\sqrt{(c-1)/c}}.
\]
Thus the Gaussian-scaled norm changes from bounded to quartically critical to exponentially growing exactly at \(c=1\), and its spatial mass switches from one centered profile to two macroscopically separated peaks.

## Assumptions and scope

The integer degree satisfies \(n\ge1\); \(c\) is a fixed positive real number independent of \(n\). The Gaussian and Lebesgue normalizations are as displayed. All asymptotics are pointwise in \(c\), not claimed uniformly as \(c\) varies through the critical value. The coherent-state interpretation uses the ordinary unitary Segal–Bargmann transform from \(L^2(\mathbb R)\) onto the analytic Bargmann–Fock Hilbert space, in which the norm is preserved. This theorem is about global squared Hilbert norms and normalized intensity distributions; it is not a statement about optimal approximation rates in an arbitrary superoscillation region.

## Proof

**Exact norm identity.** For every real \(\theta\) and \(a\),
\[
|\cos\theta+ia\sin\theta|^2=1+(a^2-1)\sin^2\theta.
\]
Consequently, with \(a=a_n\),
\[
S_n(c)=\frac1{\sqrt\pi}\int_{\mathbb R}
 e^{-x^2}\bigl(1+cn\sin^2(x/n)\bigr)^n\,dx. \tag{1}
\]
Each integral is finite because its integrand is bounded by \(e^{-x^2}(1+cn)^n\). The Fourier expansion of \(F_n\) consists only of frequencies \(1-2j/n\) for integers \(0\le j\le n\). Unitarity of the Segal–Bargmann transform identifies its Fock-space norm with (1).

**Subcritical domain \(0<c<1\).** Since \(|\sin t|\le|t|\) and \(\log(1+t)\le t\) for \(t\ge0\),
\[
0\le e^{-x^2}\bigl(1+cn\sin^2(x/n)\bigr)^n
\le e^{-(1-c)x^2}. \tag{2}
\]
At each fixed \(x\), \(cn\sin^2(x/n)=cx^2/n+O_x(n^{-3})\), so \(n\log(1+cn\sin^2(x/n))\to cx^2\). Dominated convergence in (1), using (2), gives
\[
S_n(c)\longrightarrow\frac1{\sqrt\pi}\int_{\mathbb R}e^{-(1-c)x^2}\,dx=(1-c)^{-1/2}.
\]
The same majorant gives \(L^1\)-convergence of the unnormalized intensities, hence total-variation convergence of the normalized measures. Indeed, the pointwise limit density is \(\pi^{-1/2}e^{-(1-c)x^2}\).

**Critical domain \(c=1\).** Substitute \(x=n^{1/4}u\) in (1) and write the rescaled exponent as
\[
E_n(u)=-\sqrt n\,u^2+n\log\bigl(1+n\sin^2(u/n^{3/4})\bigr).
\]
For every fixed \(u\), the expansions \(n\sin^2(u/n^{3/4})=u^2/\sqrt n+O_u(n^{-2})\) and \(\log(1+t)=t-t^2/2+O(t^3)\) show that \(E_n(u)\to-u^4/2\).

For global domination put \(t=u^2/\sqrt n\). The inequalities \(|\sin v|\le|v|\) and
\[
t-\log(1+t)\ge\frac{t^2}{2(1+t)},\qquad t\ge0, \tag{3}
\]
(where (3) follows by differentiation, with equality at zero) give
\[
E_n(u)\le -n\bigl(t-\log(1+t)\bigr)
\le-\frac{u^4}{2(1+u^2/\sqrt n)}
\le-\frac{u^4}{2(1+u^2)}. \tag{4}
\]
The last upper bound has an integrable exponential on \(\mathbb R\). Dominated convergence therefore yields
\[
\lim_{n\to\infty}n^{-1/4}S_n(1)
=\frac1{\sqrt\pi}\int_{\mathbb R}e^{-u^4/2}\,du
=\frac{2^{-3/4}\Gamma(1/4)}{\sqrt\pi}. \tag{5}
\]
The same convergence in \(L^1(du)\), after dividing by the nonzero integral (5), proves the asserted total-variation convergence of the rescaled critical intensity measures.

**Supercritical domain \(c>1\).** Put \(x=\sqrt n\,y\). Equation (1) becomes
\[
S_n(c)=\sqrt{\frac n\pi}\int_{\mathbb R}e^{nf_n(y)}\,dy,
\qquad f_n(y)=-y^2+\log\bigl(1+cn\sin^2(y/\sqrt n)\bigr). \tag{6}
\]
The elementary sine inequality gives a global comparison
\[
f_n(y)\le f(y):=-y^2+\log(1+cy^2),\qquad y\in\mathbb R. \tag{7}
\]
The function \(f\) tends to \(-\infty\) at infinity, and
\[
f'(y)=2y\left(\frac c{1+cy^2}-1\right).
\]
Since \(c>1\), its only global maximizers are \(y_\pm=\pm\sqrt{(c-1)/c}\), its value at either maximizer is
\[
I(c)=f(y_\pm)=\log c-1+1/c>0,
\]
and \(f''(y_\pm)=-4(c-1)/c<0\). (Positivity of \(I(c)\) follows from \(I(1)=0\) and \(I'(c)=(c-1)/c^2>0\).)

Uniformly with two derivatives on a fixed compact neighborhood of either maximizer, Taylor expansion of the sine and logarithm gives
\[
f_n(y)=f(y)+\frac{q(y)}n+O(n^{-2}),
\qquad q(y)=-\frac{cy^4}{3(1+cy^2)}. \tag{8}
\]
At either maximum \(q(y_\pm)=-(c-1)^2/(3c^2)\). For \(y=y_\pm+v/\sqrt n\) with bounded \(v\), (8) gives
\[
n\bigl(f_n(y)-I(c)\bigr)
\longrightarrow-\frac{2(c-1)}c v^2-\frac{(c-1)^2}{3c^2}. \tag{9}
\]
This local limit is legitimate in the Laplace integral: on each small fixed neighborhood of a maximizer, strict nondegeneracy of \(f\), combined with (7), bounds the shifted integrand by a Gaussian in \(v\); off those neighborhoods the compact part obeys \(f_n\le f\le I(c)-\epsilon\); and for sufficiently large \(|y|\), \(f_n(y)\le f(y)\le-y^2/2\). Thus the distant tails are exponentially negligible and the local dominated Laplace theorem applies. The two peaks contribute equally, by evenness. Equation (6), using (9), yields
\[
\begin{aligned}
S_n(c)&\sim\sqrt{\frac n\pi}\,e^{nI(c)}
\cdot2\cdot\frac1{\sqrt n}
\exp\!\left[-\frac{(c-1)^2}{3c^2}\right]
\int_{\mathbb R}e^{-2(c-1)v^2/c}\,dv\\
&=\sqrt{\frac{2c}{c-1}}\exp\!\left[-\frac{(c-1)^2}{3c^2}\right]e^{nI(c)},
\end{aligned}
\]
which is the supercritical claim, including its nontrivial finite-size correction to the leading exponential. Finally the same two-peak Laplace estimates, tested against bounded continuous functions of \(y\), yield equal half-masses at \(y_+\) and \(y_-\), and therefore weak convergence of the stated rescaled measures.

## Verification

The companion program `verify_gaussian_norm.py` checks the relevant critical Taylor coefficient and supercritical saddle and correction identities using exact symbolic algebra, then evaluates (1) by high-precision numerical quadrature at several degrees for each of five parameter values on both sides of the transition and at criticality. For \(c=0.4,1,1.3,2,4\), the computed ratios of the exact integral to the displayed leading asymptotic formula at \(n=320\) are approximately \(0.999479837,1.012831506,1.017726852,1.001706943,1.000028826\), respectively. The script requires Python, SymPy and mpmath. These finite checks are only corroboration: the all-degree theorem and measure limits rest on the dominated-convergence and Laplace arguments above.

## Relationship to prior work

Alpay, Colombo, Diki, Sabadini and Struppa, *Superoscillations and Fock spaces* (arXiv:2304.11551v1, public 2023-04-23), define this very Gaussian-multiplied superoscillatory family in Section 3.1 and give an exact coherent-state expansion of its Bargmann transform (Theorem 3.5). Their asymptotic statements take a **fixed** oscillation parameter \(a>1\); they do not give the growing-frequency norm transition or the critical quartic and two-saddle profiles. Their exact finite superposition is fully consistent with (1) and can, in principle, be used to recover finite-degree norms; no novelty is claimed for that identity.

Alpay, De Martino, Diki and Struppa, *Short-time Fourier transform and superoscillations* (arXiv:2407.12502v1, public 2024-07-17), provide fixed-parameter STFT and Gabor-kernel identities, including an exact finite-sum squared norm (Proposition 4.7). Such finite identities hold for any substitution \(a=a_n\) but do not themselves supply the uniform singular asymptotic analysis needed here. This result classifies exactly the Hilbert-norm and spatial mass behavior along the critical growth scaling \(a_n^2-1=cn\), including the correction multiplying the exponential regime. In a separate broader superoscillation setting, Karmakar and Jordan (arXiv:2306.03963, first public 2023-06-06) study approximation and energy inside superoscillating regions, rather than the present full-line Gaussian Hilbert norm.

## Limitations

All limits hold for fixed \(c\); they do not establish a uniform crossover profile when \(c=c_n\to1\). The theorem does not optimize the coefficients of the superoscillatory sequence or prove noise robustness of a reconstruction method. The positive rate above criticality describes global Gaussian Hilbert energy; it is not a statement about pointwise convergence to a moving plane-wave target. No independent mathematical audit has been performed. Historical priority is provisional: an unlocated general theorem for Gaussian-weighted, degree-dependent superoscillations could contain these asymptotic laws.

## References

1. D. Alpay, F. Colombo, K. Diki, I. Sabadini, D. C. Struppa, *Superoscillations and Fock spaces*, arXiv:2304.11551v1 (2023-04-23), https://arxiv.org/html/2304.11551v1, especially Sections 2 and 3.1.
2. D. Alpay, A. De Martino, K. Diki, D. C. Struppa, *Short-time Fourier transform and superoscillations*, arXiv:2407.12502v1 (2024-07-17), https://arxiv.org/html/2407.12502v1, especially Sections 3 and 4 and Proposition 4.7.
3. T. Karmakar, A. N. Jordan, *Beyond Superoscillation: General Theory of Approximation with Bandlimited Functions*, arXiv:2306.03963 (2023-06-06), https://arxiv.org/abs/2306.03963.
