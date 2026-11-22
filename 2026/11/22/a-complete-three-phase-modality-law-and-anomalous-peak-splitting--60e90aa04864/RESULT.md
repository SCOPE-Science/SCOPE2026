# A complete three-phase modality law and anomalous peak splitting for a finite-tumble active particle

## Finding

For the one-dimensional three-state run–tumble particle in a harmonic trap, the entire stationary position-density mode diagram is determined by two dimensionless rates. Write \(R=\gamma_R/b>0\) for the run-to-rest rate divided by trap relaxation, \(T=\gamma_T/b>0\) for the rest-to-run rate divided by trap relaxation, and normalize position to \(x=bX/v\in(-1,1)\). The unique stationary marginal density \(p_{R,T}\) is even. **It has at most one critical point on each open half-support**, with exactly the following alternatives:

1. If \(0<R<1\) and \(0<T<R+1\), there is precisely one strict **minimum** \(x_*\in(0,1)\). The center is a local maximum (possibly divergent), and both outer support endpoints are divergent maxima. Thus the terminal profile is trimodal, with two interior valleys.
2. If \(1<R<2\) and \(T>R+1\), there is precisely one strict **maximum** \(x_*\in(0,1)\), and its negative counterpart. The center is a strict local minimum and the density vanishes at the outer support endpoints: the profile is bimodal.
3. In every other positive-rate case the density is strictly monotone on \((0,1)\), except at \((R,T)=(1,2)\), when it is exactly uniform. More precisely: it is strictly **increasing** if \(0<R<1,\ T\ge R+1\), or if \(R=1,\ T>2\); it is strictly **decreasing** if \(R=1,\ T<2\), or if \(R>1\) outside case 2.

On the special line \(T=R+1\) the already-known density simplifies exactly to
\[
p_{R,R+1}(x)=\frac{\Gamma(R+1/2)}{\sqrt\pi\,\Gamma(R)}(1-x^2)^{R-1}.
\]
The contribution here is **the global classification for every strictly positive rate pair**, not that previously established line or the known formula for the stationary marginal.

The two inner critical points are determined without ambiguity. Set \(c=R/2\), \(e=(T-R-1)/2\), \(u=1-x^2\). In case 1 or case 2, the unique root \(x_*\in(0,1)\) obeys
\[
(R-1)\,{}_2F_1(-e,c;2c;u)
=\frac{e u}{2}\,{}_2F_1(1-e,c+1;2c+1;u).
\]
The extrema split from the center with a non-square-root law: for any fixed \(0<R<2\) with \(R\ne1\), as \(T\to R+1\) **from its nonmonotone side**,
\[
\boxed{\quad
x_*^{\,2-R}\sim
\frac{\pi\,|T-R-1|}{2|R-1|\sin(\pi R/2)\,B(R/2,R/2)}.
\quad}
\]
Here the nonmonotone side means \(T\uparrow R+1\) for \(R<1\), or \(T\downarrow R+1\) for \(1<R<2\). The peak/valley opening exponent is \(1/(2-R)\).

## Assumptions and scope

A particle obeys \(\dot X_t=-bX_t+v S_t\), with \(b,v>0\) and a continuous-time Markov state \(S_t\in\{-1,0,+1\}\). From either \(\pm1\), the motor enters state \(0\) at rate \(\gamma_R>0\). From \(0\), it enters each running direction at rate \(\gamma_T/2\); the choice after each rest is independent of its previous sign. There is no translational thermal noise, interaction, or direct running-direction flip. The unique invariant position law is supported on \([-v/b,v/b]\), with an even positive density on the interior. Stationary state rather than finite-time positions is considered. Modes at the support endpoints mean one-sided local maxima (which can be infinite); all interior critical points are located in \((-1,1)\).

## Proof

**1. Exact positive integral, explicitly separating source and extension.** Sun, Ye and Podgornik established the stationary one-dimensional characteristic function and density for all \(R,T>0\) (their Eq. 38–39). Their even moments equal
\[
\mathbb E[x^{2k}]=\frac{(1/2)_k(T/2)_k}{((R+1)/2)_k((R+T)/2)_k},\qquad k=0,1,\ldots.
\]
This implies a positive beta-product representation: let \(U\sim\operatorname{Beta}(T/2,R/2)\) and \(V\) independently have even density \((1-v^2)^{R/2-1}/B(1/2,R/2)\) on \((-1,1)\); then \(x\) has the same law as \(\sqrt U\,V\). Indeed all even moments agree, all odd moments vanish, and both measures have compact support. This representation of the **known forward law** has previously appeared in published follow-up work and is not claimed as new.

For \(c=R/2\), \(a=T/2\), and \(e=a-c-1/2\), the resulting density on \(0<x<1\), with \(z=x^2\), is
\[
p_{R,T}(x)=K_{R,T}(1-z)^{R-1}I_e(z),\qquad
I_e(z)=\int_0^1 t^{c-1}(1-t)^{c-1}\,[t+(1-t)z]^e\,dt,
\]
\[
K_{R,T}=\{B(a,c)B(1/2,c)\}^{-1}>0.
\]
(The integral at \(z=0\) is infinite exactly when the center density diverges; for \(z>0\), everything above is strictly positive and smooth.) Euler's beta-integral identity yields \(I_e(z)=B(c,c)\,{}_2F_1(-e,c;2c;1-z)\). This also proves the displayed critical-point equation.

**2. A differential-equation sign obstruction excludes additional extrema.** Gauss's hypergeometric equation, applied to \(f(u)=p_{R,T}(\sqrt{1-u})\) for \(0<u<1\), gives the exact ordinary differential equation
\[
\boxed{\quad
u(1-u)f''(u)+\left[2-R+\frac{2R+T-7}{2}u\right]f'(u)
+\frac{(2-R)(R+T-3)}4f(u)=0.
\quad}
\]
To verify, substitute \(f(u)=K B(c,c)u^{2c-1}F(u)\), \(F={}_2F_1(-e,c;2c;u)\), into the Gauss equation \(u(1-u)F''+[2c-(c-e+1)u]F'+ecF=0\); the coefficients above follow by collecting powers. At any interior critical point of \(f\), positivity of \(f\) shows
\[
\operatorname{sgn}f''=-\operatorname{sgn}\big((2-R)(R+T-3)\big)
\]
provided the product is nonzero. Hence **all critical points have the same strict type**, and there can be at most one: two strict maxima would require an intervening strict minimum and conversely. When the coefficient vanishes, the equation for \(f'\) is first order on \((0,1)\): it cannot have an isolated zero. The exceptional possibility of identically zero derivative is resolved below by the exact uniform density.

**3. Complete existence and sign classification.** When \(e\ge0\) and \(R<1\), both factors \((1-z)^{R-1}\) and \(I_e(z)\) are nondecreasing in \(z\), with the first strictly increasing; therefore \(p\) increases strictly on \((0,1)\). When \(e\le0\) and \(R>1\), both factors are nonincreasing and the first strictly decreases; therefore \(p\) strictly decreases. If \(R=1\), the first factor is constant and \(I_e'(z)\) has precisely the sign of \(e\), giving the asserted monotone directions and the uniform case \(e=0\), namely \((R,T)=(1,2)\). For \(R\ge2\), the independent factor \(V\) has a nonincreasing density on \((0,1)\), and the mixture of its scaled copies \(U^{-1/2}p_V(x/\sqrt U)\mathbf1_{\{U>x^2\}}\) is strictly decreasing for every \(x>0\); at \(R=2\) this follows strictly from the shrinking positive integration domain. This covers the high-run-rate region even when \(e>0\).

It remains to analyze the two mixed regions. Near \(x=1\), the integral \(I_e(z)\to B(c,c)\), so \(p(x)\sim K B(c,c)(1-x^2)^{R-1}\). The derivative toward the endpoint is positive for \(R<1\) and negative for \(R>1\).

Near the center, if \(0<T<1\) the density diverges there; for \(T=1\) it has a logarithmic divergence. If \(1<T<3\) and \(e\ne0\), differentiation of the positive integral followed by \(t=zs\) gives
\[
I_e'(z)\sim e B(c,1-c-e) z^{c+e-1}
\qquad(z\downarrow0),
\]
where \(c+e=(T-1)/2\in(0,1)\); the exponent is negative, so \(p_z\) has the sign of \(e\). At \(T=3\), the corresponding logarithm has the sign of \(e\). For \(T>3\), differentiating at zero is legitimate and gives
\[
\frac{p_z(0)}{p(0)}=-(R-1)+\frac{ec}{c+e-1}
=\frac{(2-R)(R+T-3)}{2(T-3)}.
\]
Consequently, if \(R<1\) and \(T<R+1\), the density decreases immediately to the right of the center, then increases toward its divergent outer endpoint; an interior minimum exists. The ODE coefficient there is strictly negative, so the minimum is unique. If \(1<R<2\) and \(T>R+1\), the density increases immediately right of the center and decreases to its zero outer endpoint; an interior maximum exists. The ODE coefficient there is strictly positive, so this maximum is unique. The preceding monotonicity arguments exhaust every remaining parameter pair.

**4. Sharp splitting at the boundary.** Fix \(c\in(0,1)\setminus\{1/2\}\) and let \(e\to0\) with \(e/(R-1)>0\). The unique critical point has \(z_*=x_*^2\to0\), since at \(e=0\) the strictly monotone density is proportional to \((1-z)^{R-1}\), and critical points cannot remain in a compact subinterval of \((0,1)\). The exact critical-point equation in integral form is
\[
(R-1)I_e(z_*)=(1-z_*)I_e'(z_*).
\]
At small \(z\), uniformly for sufficiently small \(|e|\), scaling \(t=zs\) in \(I_e'\) and applying dominated convergence yields \(I_e'(z)\sim e z^{c+e-1}B(c,1-c-e)\), while \(I_e(z_*)\to B(c,c)\). Hence
\[
z_*^{1-c-e}\sim\frac{e B(c,1-c-e)}{(R-1)B(c,c)}.
\]
Taking logarithms shows \(e\log z_*\to0\); letting \(e\to0\), using \(B(c,1-c)=\pi/\sin(\pi c)\) and \(2|e|=|T-R-1|\), proves exactly the stated opening law. This is an asymptotic for a fixed \(R\) away from \(1\) and \(2\); it is not asserted uniformly in those parameters.

## Verification

The standalone `check_modes.py` uses SymPy and mpmath. It checks the general symbolic hypergeometric-ODE coefficients; agrees with the exact stationary-generator even-moment recurrence for eight run rates, seven rest rates and six moment orders; verifies the beta-resonance density for seven rates and four positions; checks 21 high-precision second-order ODE residuals; brackets and bisects five distinct nonmonotone critical points; and checks both sides of the nonstandard near-boundary splitting coefficient. The delivered code completed **410 assertions**. The analytic ODE sign argument, not finite numerical sampling, proves the complete global mode count. Reproduce with `python check_modes.py` after installing `sympy` and `mpmath`.

## Relationship to prior work

The full stationary one-dimensional position density and hypergeometric characteristic function are **known**, not newly claimed: Sun, Ye and Podgornik (first available 2024-09-01), Section III. That source establishes some center/outer-endpoint singularity regimes and figures but does not classify all critical points for arbitrary independent positive rates or give the nonanalytic peak-splitting exponent. Basu et al. (2019), Sections 2–3, established a three-to-one shape transition on the narrower **equal-rate line** \(T=R\), not the complete two-rate diagram. Existing analyses of analyticity resonances, full state reconstruction, and two-moment inverse ambiguity for this same stationary law supply particular identities and special parameter curves but do not state a complete all-rate mode theorem or opening law; their directly covering special cases are explicitly credited and excluded from the novelty claim. Studies of other two-state saturating-speed processes and complete-graph switching have different generators and cannot imply the present mode count merely from similar peak labels. The proof requires the sign-type obstruction of the scalar Gauss ODE together with the sharp center and support-edge sign analysis.

## Limitations

The result is confined to the noiseless one-dimensional, three-state Markov run–rest model with independent fair choice of the next running direction. It does not address transient profiles, arbitrary switching networks, spatially varying trap forces, experimental sampling, or additive diffusion. Boundary maxima may be infinite rather than attained as finite values; such terminology means one-sided peaks of the stationary density on its compact support. The bifurcation law holds for each fixed \(R\in(0,2)\setminus\{1\}\) approaching \(T=R+1\) from the stated side, not uniformly at the marginal rates. The exact density and the resonance curve are prior work. Independent specialist validation and a comprehensive publication-priority determination have not been performed.

## References

1. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578v1 (first posted 2024-09-01), especially Section III, Eqs. (38)–(43); revised full HTML at https://arxiv.org/html/2409.00578v2 .
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083v1 (first posted 2019-10-22), Sections 2–3. https://arxiv.org/html/1910.10083v1 .
3. *Exact analytic-center resonance lines for a finite-tumble run-and-tumble particle*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-analytic-center-resonance-lines-for-a-finite-tumble-run-an--a0785c41aaa8 .
4. *State-resolved stationary reconstruction and a unique beta–binomial sector in a three-state active oscillator*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-state-resolved-stationary-reconstruction-and-a-unique-beta-binom--18a2152addfb .
5. *An exact two-moment inverse fold in a trapped run-and-tumble particle*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-exact-two-moment-inverse-fold-in-a-trapped-run-and-tumble-par--432388eb4847 .
6. *A sharp unimodal–trimodal–bimodal transition in a two-state run-and-tumble particle*, a distinct saturating-speed model, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-unimodal-trimodal-bimodal-transition-in-a-two-state-run--56f6c06bf21b .
