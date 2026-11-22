# A tricritical one-third Gaussian threshold for mixed Hermite strip localization

## Finding
Let \(h_0(t)=\pi^{-1/4}e^{-t^2/2}\) and \(h_1(t)=\sqrt 2\,t h_0(t)\). For \(a>0\) and \(0<w<1\), define the *incoherent two-window localization operator* \(T_{a,w}\) by summing the strip energy of the short-time Fourier transforms with windows \(h_0,h_1\), with respective nonnegative weights \(w,1-w\). The strip is \(\{(x,\omega):|x|\le a\}\). Define \(\gamma=w/[2(1-w)]\) and \(a_c=\sqrt{1-\gamma}\) whenever \(0<\gamma<1\).

The operator is multiplication by the even, analytic function
\[
M_{a,\gamma}(t)=\frac1{\sqrt\pi(\gamma+1/2)}\int_{t-a}^{t+a}(\gamma+u^2)e^{-u^2}\,du.
\]
Its sharp norm is \(\max_{t\in\mathbb R}M_{a,\gamma}(t)\), and is not attained by any nonzero vector in \(L^2(\mathbb R)\).

The maximizing locations obey the following complete phase classification.

1. For \(w\ge2/3\), the sole maximizing location is \(t=0\), for every \(a>0\).
2. For \(1/3<w<2/3\), the maximizers are exactly two symmetric locations \(\pm t_+(a)\) for \(0<a<a_c\), and only \(t=0\) for \(a\ge a_c\). As \(a\uparrow a_c\),
   \[
   t_+(a)\sim\sqrt{\frac{3(a_c^2-a^2)}{4\gamma-1}}.
   \]
3. At \(w=1/3\), the same global transition occurs at \(a_c=\sqrt3/2\), but with the quartic-root displacement
   \[
   t_+(a)\sim [5(a_c^2-a^2)]^{1/4}.
   \]
   At the critical width, \(M_{a_c,1/4}(0)-M_{a_c,1/4}(t)\) has a strictly positive leading term of order \(t^6\).
4. For \(0<w<1/3\), there is a unique first-order transition width \(a_*(\gamma)>a_c\). Below it the maximizers are precisely \(\pm t_+(a)\); above it only \(0\) maximizes; at it, precisely \(0,\pm t_*\) maximize for some \(t_*>0\). The two positive unknowns \(a_*,t_*\) are uniquely determined by the pair
   \[
   2a_*t_*\coth(2a_*t_*)=a_*^2+t_*^2+\gamma,
   \qquad M_{a_*,\gamma}(t_*)=M_{a_*,\gamma}(0).
   \]
   The norm is continuous and has a nonzero one-sided derivative jump at the crossing.

The parameter \(w=1/3\) is thus an exact tricritical budget: across it the maximal-concentration location changes from a discontinuous jump to a square-root bifurcation, with a fourth-root law at the separating value.

## Assumptions and scope
The Hilbert space is \(L^2(\mathbb R,dt)\). Define \(V_hf(x,\omega)=\int_{\mathbb R} f(t)\overline{h(t-x)}e^{-i\omega t}\,dt\), and integrate time-frequency energy using \(dx\,d\omega/(2\pi)\). Each window has \(L^2\)-norm one. The two channel energies are added *incoherently*; this is not the energy of a coherent linear combination of windows. The strip is unbounded in frequency, and there are no finite-energy extremizing signals, although the operator norm is sharp. The theorem addresses every \(a>0\) and every strictly positive weight \(w<1\); the pure first-Hermite endpoint \(w=0\) has been described previously and is not claimed here.

## Proof
**1. Exact spectral reduction.** Plancherel in the frequency variable gives
\[
\int_{-a}^a\int_{\mathbb R}|V_h f(x,\omega)|^2\frac{d\omega}{2\pi}\,dx
=\int_{\mathbb R}|f(t)|^2\left(\int_{t-a}^{t+a}|h(u)|^2du\right)dt.
\]
Since \(w|h_0(u)|^2+(1-w)|h_1(u)|^2=(\gamma+u^2)e^{-u^2}/[\sqrt\pi(\gamma+1/2)]\), the asserted multiplier follows. Its maximum is attained as a function of \(t\), but its maximizing set is finite, and so no nonzero \(L^2\) signal attains the operator norm.

**2. A one-hump derivative principle.** Put \(p_\gamma(u)=(\gamma+u^2)e^{-u^2}/[\sqrt\pi(\gamma+1/2)]\). For \(t>0\),
\[
M'_{a,\gamma}(t)=p_\gamma(t+a)-p_\gamma(t-a),
\qquad \operatorname{sgn}M'_{a,\gamma}(t)
=\operatorname{sgn}\left(2at\coth(2at)-t^2-a^2-\gamma\right).
\]
Let \(h_a(t)=2at\coth(2at)-t^2\), with \(h_a(0)=1\). The classical partial-fraction expansion
\[
u\coth u=1+2u^2\sum_{k=1}^\infty\frac1{u^2+\pi^2k^2}
\]
implies
\[
\frac{h'_a(t)}{2t}=8a^2\sum_{k=1}^\infty\frac{\pi^2k^2}{(4a^2t^2+\pi^2k^2)^2}-1.
\]
The right-hand side decreases strictly in \(t\), starts at \(4a^2/3-1\), and tends to \(-1\). Hence \(h_a\) decreases strictly if \(a\le\sqrt3/2\), and otherwise increases to exactly one positive maximum before decreasing to minus infinity. Consequently the multiplier has at most two positive nonzero stationary locations: if there are two, the smaller is a local minimum and the larger is the sole off-center local maximum.

**3. Global control for sufficiently large widths.** For every \(a\ge\sqrt3/2\) and \(t>0\), one has the sharp enough bound
\[
h_a(t)-a^2<\frac14.
\]
Indeed set \(u=2at\). For \(0<u\le3/2\), the inequalities \(u\coth u<1+u^2/3\) and \(a^2+u^2/(4a^2)\ge3/4+u^2/3\) yield the claim. For \(u\ge3/2\), arithmetic-geometric mean yields \(a^2+u^2/(4a^2)\ge u\), whence \(h_a(t)-a^2\le 2u/(e^{2u}-1)\le3/(e^3-1)<1/4\). If \(\gamma\ge1/4\), the sign principle and the monotonicity for smaller widths now imply that the center is the unique maximizer whenever \(a\ge a_c\). For \(0<\gamma<1/4\), it implies at least that the center is a strict local maximum once \(a>a_c\). If \(\gamma\ge1\), the center is unique for every positive width; this also follows by the same derivative test below \(\sqrt3/2\).

**4. Continuous transitions.** If \(1/4\le\gamma<1\), then \(a_c\le\sqrt3/2\). For every \(a<a_c\), the function \(h_a\) is strictly decreasing from \(1>a^2+\gamma\), so the multiplier increases then decreases on the positive half-line, with one unique positive maximizer. At and above \(a_c\), the proof above gives only the center. The Taylor expansion
\[
h_a(t)=1+\left(\frac{4a^2}{3}-1\right)t^2-\frac{16a^4}{45}t^4+O_a(t^6)
\]
proves the square-root law when \(\gamma>1/4\), and, at \(\gamma=1/4\), gives \(h_{a_c}(t)-1=-t^4/5+O(t^6)\). Balancing against \(a_c^2-a^2\) gives the stated fourth-root law. Since \(M'\) is a strictly positive smooth factor times \(h_a(t)-a^2-\gamma\) for \(t>0\), integration yields sixth-order flatness at the tricritical point.

**5. Existence and uniqueness of the discontinuous transition.** Suppose \(0<\gamma<1/4\), hence \(a_c>\sqrt3/2\). Define
\[
K(a)=\max_{t\ge0}(h_a(t)-a^2),\qquad a\ge a_c.
\]
The maximum occurs at a unique positive \(t\), since \(h_a\) first increases then decreases. Set \(u=2at\) and \(k_a(u)=u\coth u-a^2-u^2/(4a^2)\). At its maximizing \(u\), differentiation yields
\[
\frac{u}{2a^2}=\coth u-u\operatorname{csch}^2u<1.
\]
The last strict inequality follows from \((1-e^{-2u})/2<u\). By the envelope theorem,
\[
K'(a)=-2a+\frac{u^2}{2a^3}<0.
\]
Moreover \(K(a_c)>\gamma\), while \(K(a)\to0\) as \(a\to\infty\), because the maximizing \(u\sim 2a^2\) and \(k_a(u)\) tends to zero. There is therefore exactly one fold width \(a_f>a_c\) at which \(K(a_f)=\gamma\). For \(a_c<a<a_f\), the derivative has two positive simple zeros, and the larger \(t_+(a)\) is the sole positive local maximum; for \(a\ge a_f\), the center globally maximizes. At \(a=a_c\), the outer maximum beats the center; at the fold it is strictly worse than the center, because the multiplier decreases on \((0,t_+(a_f))\).

Along the outer-stationary branch the height difference \(\Delta(a)=M_{a,\gamma}(t_+(a))-M_{a,\gamma}(0)\) obeys, by the envelope theorem,
\[
\Delta'(a)=2\bigl[p_\gamma(a+t_+(a))-p_\gamma(a)\bigr]<0,
\]
because \(p_\gamma\) is strictly decreasing on \([a,\infty)\) whenever \(a>a_c\). Hence \(\Delta\) crosses zero exactly once before the fold. Before \(a_c\) the center is a strict local minimum, leaving the off-center maximum uniquely optimal. At the crossing, the two branches of the sharp norm have unequal derivatives, so the norm has a genuine corner. This proves all cases and all equality conditions.

## Verification
The standalone `checker.py` checks the exact Taylor coefficients and threshold identities symbolically, brackets the unique jump for five genuinely mixed parameters, verifies the negative crossing slope, and checks the two fractional-power laws numerically. Running `python checker.py` outputs `PASS`. The finite tests support but do not replace the global partial-fraction and envelope arguments. For illustration, when \(w=1/5\) (so \(\gamma=1/8\)), the analytic equations give \(a_c=0.935414346693\ldots\), \(a_*=0.952341151642\ldots\) and \(t_*=0.828998681203\ldots\).

## Relationship to prior work
Keller and Luef (2019 preprint) develop Hermite-window anti-Wick and polyanalytic Toeplitz localization theory, supplying the operator-theoretic setting but not the mixed-strip maximizer classification. Nicola and Tilli (2021 preprint; 2022 publication) establish sharp Gaussian-window time-frequency concentration inequalities for finite-measure sets, not the present infinite strip or incoherently mixed windows. The published result “Two-stage symmetry breaking and sixfold spectral fibers in first-Hermite strip localization” describes the \(w=0\) endpoint of the current family, and is explicitly excluded from the novel claim. Existing two-Hermite disk localization and coherent-window spectrogram results use different observables. The new assertion is the complete \(0<w<1\) phase classification, including the exact \(1/3\) tricritical weight and the discontinuous-to-continuous change.

## Limitations
No claim is made for finite frequency cutoffs, coherent superpositions, other Hermite orders, or arbitrary window profiles. The spectral norm is not attained in \(L^2\), since the maximizing multiplier set has measure zero. The older pure-Hermite endpoint was known. Historical priority has been checked against identified relevant work but may be incomplete. Independent audit has not been performed.

## References
- J. Keller and F. Luef, *Polyanalytic Toeplitz Operators: Isomorphisms, Symbolic Calculus and Approximation of Weyl Operators*, arXiv:1905.07741 (first posted 19 May 2019), https://arxiv.org/abs/1905.07741; *Journal of Fourier Analysis and Applications* 27 (2021), article 47, https://doi.org/10.1007/s00041-021-09843-0.
- F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2106.03423 (2021), https://arxiv.org/abs/2106.03423; *Inventiones Mathematicae* 230 (2022), 1–30.
- *Two-stage symmetry breaking and sixfold spectral fibers in first-Hermite strip localization*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-stage-symmetry-breaking-and-sixfold-spectral-fibers-in-first--9ad7b3df9d6d.
- *Exact finite inversion census for two-Hermite disk localization*, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-finite-inversion-census-for-two-hermite-disk-localization--cdf01c361d5b.
