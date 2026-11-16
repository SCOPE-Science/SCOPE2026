# A sharp jump-representation transition for radial-power harmonic Dirichlet energies

## Finding

For every real \(\alpha\ge0\), consider the harmonic Poisson extension \(u=P[f]\) of boundary data on the unit circle, with weighted energy
\[
\mathcal E_\alpha(f)=\int_{\mathbb D}\bigl(|\partial_z u|^2+|\partial_{\bar z}u|^2\bigr)(1-|z|^2)^\alpha\,\frac{dx\,dy}{\pi}.
\]
There exists a **positive boundary jump measure** \(J\) on \((\mathbb T\times\mathbb T)\setminus\Delta\) representing this energy by
\[
\mathcal E_\alpha(f)=\frac12\iint_{\mathbb T^2}|f(\zeta)-f(\eta)|^2\,J(d\zeta,d\eta)
\]
for every trigonometric polynomial \(f\), **if and only if \(0\le\alpha\le1\)**. The assertion holds without assuming \(J\) is rotation invariant.

For \(0<\alpha\le1\), one explicit positive jump kernel is \(J(d\zeta,d\eta)=j_\alpha(\theta-\phi)\,dm(\theta)dm(\phi)\), where \(\zeta=e^{i\theta}\), \(\eta=e^{i\phi}\), \(dm(\theta)=d\theta/(2\pi)\), and
\[
 j_\alpha(\vartheta)=\int_0^1\frac{1-t^2}{1-2t\cos\vartheta+t^2}\,\frac{\alpha(1-\alpha t)}{(1-t)^{2-\alpha}}\,dt,\qquad 0<|\vartheta|\le\pi.
\]
At \(\alpha=0\), \(j_0(\vartheta)=2/|1-e^{i\vartheta}|^2\). These kernels all have Fourier jump symbol
\[
\psi_\alpha(n)=n^2 B(n,\alpha+1),\quad n\ge1,\qquad \psi_\alpha(0)=0,
\]
where \(B\) is the beta function and the symbol is even in \(n\).

The jump activity undergoes a sharp transition at the endpoint: \(\int_{\mathbb T}j_\alpha\,dm=+\infty\) for \(0\le\alpha<1\), but \(\int_{\mathbb T}j_1\,dm=1\). Thus the \(\alpha=1\) process is a rate-one compound Poisson process on \(\mathbb T\). Its probability jump density is the elementary function
\[
 j_1(\vartheta)=-1-\cos\vartheta\log\bigl(4\sin^2(\vartheta/2)\bigr)+(\pi-|\vartheta|)\sin|\vartheta|,
 \quad 0<|\vartheta|\le\pi.
\]
For \(0<\alpha<1\), the exact small-angle singular coefficient is
\[
\lim_{\vartheta\to0}|\vartheta|^{2-\alpha}j_\alpha(\vartheta)
=\frac{\pi\alpha(1-\alpha)}{\sin(\pi\alpha/2)}.
\]
For \(\alpha=1\), \(j_1(\vartheta)=2\log(1/|\vartheta|)-1+o(1)\). For every \(0\le\alpha\le1\), the positive spectral gap of the boundary generator is precisely \(\psi_\alpha(1)=1/(1+\alpha)\).

## Assumptions and scope

The disk \(\mathbb D\) carries normalized planar Lebesgue measure \(dA=dx\,dy/\pi\), and \(\mathbb T\) carries probability Haar measure \(dm\). Define \(\partial_z=(\partial_x-i\partial_y)/2\) and \(\partial_{\bar z}=(\partial_x+i\partial_y)/2\); in particular, \(|\partial_z u|^2+|\partial_{\bar z}u|^2\) is **half the squared Euclidean real gradient** for real-valued \(u\). All form normalizations above follow this convention. Fourier coefficients use \(f(e^{i\theta})=\sum_{n\in\mathbb Z}c_ne^{in\theta}\). Claims about positive measures hold first for trigonometric polynomials, and then extend to the form domain \(\{f\in L^2(dm):\sum_n\psi_\alpha(|n|)|c_n|^2<\infty\}\) by closure. No uniqueness of a positive jump measure is assumed or required.

When \(0<\alpha\le1\), define \(P_t(\vartheta)=(1-t^2)/(1-2t\cos\vartheta+t^2)\) for \(0\le t<1\). The mixing measure \(\nu_\alpha(dt)=\alpha(1-\alpha t)(1-t)^{\alpha-2}dt\) is positive in the asserted range. Its total mass is infinite for \(\alpha<1\) and equals one for \(\alpha=1\), but its first vanishing moment \(\int_0^1(1-t)\nu_\alpha(dt)\) is finite. The jump kernel is allowed to have an infinite singularity at the diagonal, which is excluded from the measure space.

## Proof

**1. The exact Fourier symbol.** For a mode \(f(e^{i\theta})=e^{in\theta}\), its Poisson extension is \(r^{|n|}e^{in\theta}\). For \(n>0\) this is \(z^n\); for \(n<0\) it is \(\bar z^{|n|}\). In either case the complex-gradient integrand is \(n^2r^{2|n|-2}\). Orthogonality in \(\theta\), followed by \(s=r^2\), gives
\[
\mathcal E_\alpha(f)=\sum_{n\ne0}\psi_\alpha(|n|)|c_n|^2,
\quad \psi_\alpha(n)=n^2\int_0^1s^{n-1}(1-s)^\alpha ds=n^2B(n,\alpha+1).
\]
This also verifies the normalization at \(\alpha=0\), where \(\psi_0(n)=n\).

**2. Positive Poisson-mixture representation.** Fix \(0<\alpha\le1\). A direct beta-function calculation, valid for every integer \(n\ge0\), yields
\[
\begin{aligned}
\psi_\alpha(n+1)-\psi_\alpha(n)
&=\alpha\int_0^1 t^n(1-\alpha t)(1-t)^{\alpha-1}\,dt\\
&=\int_0^1t^n(1-t)\nu_\alpha(dt).
\end{aligned}
\]
For completeness, the first expression evaluates to \(\Gamma(\alpha+1)\Gamma(n+1)[1+n(1-\alpha)]/\Gamma(n+\alpha+2)\), the same as the difference of consecutive \(n^2B(n,\alpha+1)\) values (taking \(\psi_\alpha(0)=0\)). Summing from \(0\) to \(n-1\) gives
\[
\psi_\alpha(n)=\int_0^1(1-t^n)\nu_\alpha(dt).
\]
Since \(\int_\mathbb T P_t(\theta)\,dm=1\) and \(\int_\mathbb T P_t(\theta)\cos(n\theta)\,dm=t^n\), Tonelli's theorem implies
\[
\int_\mathbb T(1-\cos(n\theta))j_\alpha(\theta)\,dm(\theta)=\psi_\alpha(n).
\]
For any trigonometric polynomial, expand the squared difference, integrate the rotation-invariant kernel and use Fourier orthogonality. The result is precisely the required \(\frac12\iint\) boundary formula. Monotone nonnegative spectral truncations and density give equality of closed forms, not merely equality on individual modes.

At \(\alpha=0\), the standard trigonometric identity
\[
\int_\mathbb T\frac{2(1-\cos(n\theta))}{|1-e^{i\theta}|^2}\,dm(\theta)=n
\]
provides the same representation. It follows, for example, by integrating the square modulus of \(1+e^{i\theta}+\cdots+e^{i(n-1)\theta}\).

**3. Impossibility above the threshold, even for asymmetric measures.** Suppose \(\alpha>1\) and some positive \(J\) gives the claimed formula for all trigonometric polynomials. Push \(J\) forward by \((e^{i\theta},e^{i\phi})\mapsto e^{i(\theta-\phi)}\); this gives a positive measure \(\mu\) on \(\mathbb T\setminus\{1\}\), with no rotation-invariance assumption. Testing the modes \(e^{in\theta}\) forces
\[
\psi_\alpha(n)=\int_{\mathbb T\setminus\{1\}}(1-\cos(n\vartheta))\,\mu(d\vartheta).
\]
But the gamma-ratio asymptotic gives \(\psi_\alpha(n)\sim\Gamma(\alpha+1)n^{1-\alpha}\to0\), while \(\psi_\alpha(1)=1/(\alpha+1)>0\). At every fixed nonzero angle,
\[
\lim_{N\to\infty}\frac1N\sum_{n=1}^N(1-\cos(n\vartheta))=1.
\]
Fatou's lemma therefore gives
\[
\mu(\mathbb T\setminus\{1\})\le\liminf_{N\to\infty}\frac1N\sum_{n=1}^N\psi_\alpha(n)=0,
\]
contradicting \(\psi_\alpha(1)>0\). This proves the strict converse independently of general uniqueness theorems for Lévy symbols.

**4. Exact activity and local singularity.** Integration of \(P_t\) against Haar measure shows that the activity equals \(\int_0^1\nu_\alpha(dt)\). For \(0<\alpha<1\), this is infinite because \(\nu_\alpha(dt)\sim\alpha(1-\alpha)(1-t)^{\alpha-2}dt\); at \(\alpha=1\), \(\nu_1=dt\), hence activity one. The Cauchy endpoint also has infinite activity. If \(0<\alpha<1\), set \(s=1-t\). As \(s,|\vartheta|\to0\),
\[
P_{1-s}(\vartheta)\sim\frac{2s}{s^2+\vartheta^2},\qquad
\nu_\alpha(dt)\sim\alpha(1-\alpha)s^{\alpha-2}ds.
\]
Indeed, for \(0<s\le1/2\) and \(|\vartheta|\le1/2\), the exact denominator \(s^2+2(1-s)(1-\cos\vartheta)\) is bounded above and below by fixed multiples of \(s^2+\vartheta^2\). Consequently the rescaled integrands are bounded by a fixed multiple of \(u^{\alpha-1}/(1+u^2)\), an integrable function for \(0<\alpha<1\), while the region \(s>1/2\) contributes a bounded term negligible after multiplication by \(|\vartheta|^{2-\alpha}\). After the rescaling \(s=|\vartheta|u\), dominated convergence and the classical beta integral
\[
\int_0^\infty\frac{u^{\alpha-1}}{1+u^2}\,du=\frac\pi{2\sin(\pi\alpha/2)}
\]
give the exact stated coefficient. For \(\alpha=1\), integrating \(P_t\) explicitly by elementary partial-fraction and logarithmic primitives yields the stated \(j_1\) formula and its logarithmic expansion. Its Fourier coefficients are \(\int_\mathbb Tj_1(\theta)e^{in\theta}dm=1/(|n|+1)\). Thus its jump operator is \(Qf(\theta)=\int f(\theta+\vartheta)j_1(\vartheta)dm(\vartheta)\), the generator is \(Q-I\), and the corresponding time-\(s\) semigroup is \(e^{-s}\sum_{k\ge0}s^kQ^k/k!\). This is the rate-one compound Poisson construction.

**5. Sharp gap.** The jump-mixture expression implies \(\psi_\alpha(n+1)>\psi_\alpha(n)\) for all integer \(n\ge0\) and every \(0<\alpha\le1\). At \(\alpha=0\), \(\psi_0(n)=n\). Hence the smallest nonzero eigenvalue of \(-\mathcal G_\alpha\) on \(L^2(\mathbb T,dm)\) is exactly \(\psi_\alpha(1)=B(1,\alpha+1)=1/(1+\alpha)\).

## Verification

The accompanying standalone `CHECK.py` verifies the rational beta-coefficient recurrence and first-mode normalization exactly using fractions over multiple admissible and inadmissible parameters. It checks the classical and critical endpoint spectra, and—with the optional installed `mpmath` dependency—compares the closed elementary critical jump density against high-precision quadrature and checks short-angle asymptotic ratios. The saved copy passed 674 finite assertions. These computations test formulas only: the universal sign, existence, nonexistence and asymptotic statements follow from the analytical argument above.

## Relationship to prior work

Bourabiaa, Elmadani, Hanine, Jamal, and Labghail (2026) formulate weighted Douglas representation, establish its existence for positive superharmonic weights, construct associated pure-jump Hunt processes, identify the constant-weight case with wrapped Cauchy motion, and explicitly ask for weight classification and descriptions of the jump generators and measures (their §5, Problems 1 and 4). This proof is a specialization to the canonical radial powers; the positive direction for \(\alpha\le1\) is compatible with their established superharmonic sufficiency. The **newly determined components** are the exact converse within the whole radial-power family, a closed Poisson-mixture jump kernel for every admissible exponent, sharp angular singularity, and the finite-activity compound-Poisson endpoint at \(\alpha=1\).

Bao, Göğüş, and Pouliasis (2018) examine superharmonic-weight Dirichlet spaces and explicitly mention radial powers \((1-|z|^2)^p\) with \(0<p<1\), but the inspected text does not classify positive boundary jump representations for all powers or identify the endpoint compound-Poisson law. Their general positive-superharmonic framework and the classical trigonometric Cauchy identity are taken as known, not claimed as new. The distinguishing quantitative formula is not implied just by naming a class of admissible weights: the explicit Fourier jump-law, endpoint activity and strict nonrepresentation require the additional calculations presented here. Exhaustive historical priority, particularly under alternate Lévy–Khintchine or Dirichlet-to-Neumann terminology, has not been independently established.

## Limitations

This is a **complete result only for the radial-power family** \((1-|z|^2)^\alpha\) with \(\alpha\ge0\); it does not classify arbitrary radial weights, perturbations, or general nonradial weights. A pointwise Lévy density is exhibited but uniqueness among all off-diagonal jump representations is not asserted. The construction is about harmonic Poisson boundary energies, not arbitrary analytic derivative norms with other normalizations. The existence of a pure-jump process for general Douglas weights is prior work. Reproducibility checks are finite and do not constitute an independent mathematical audit.

## References

1. J. Bourabiaa, Y. Elmadani, A. Hanine, A. Jamal, I. Labghail, *Douglas Weighted Dirichlet Spaces: Analytic and Probabilistic Aspects*, arXiv:2607.26870 (first posted 2026-07-29), §§2, 4–5, Appendix A. https://arxiv.org/abs/2607.26870
2. G. Bao, N. G. Göğüş, S. Pouliasis, *On Dirichlet Spaces With a Class of Superharmonic Weights*, Canad. J. Math. **70** (2018), 721–741; electronically published 2017-05-19. https://doi.org/10.4153/CJM-2017-005-1
3. Standard Fourier expansion of the Poisson kernel and elementary beta/gamma identities (used with derivations above).
