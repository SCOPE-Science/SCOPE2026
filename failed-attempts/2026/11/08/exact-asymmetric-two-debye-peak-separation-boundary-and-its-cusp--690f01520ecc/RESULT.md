# Exact asymmetric two-Debye peak-separation boundary and its cusp law

## Finding
For two ideal additive Debye processes with unequal positive relaxation strengths, there is one and only one relaxation-time ratio at which the loss profile changes from one spectral peak to two. The boundary has an algebraic parametrization and a nonanalytic \(2/3\)-power cusp near balanced strengths.

Let \(\alpha=a/b>0\) be the ratio of relaxation strengths and \(r=\tau_2/\tau_1>1\) the ratio of times. Define, for \(0<y<1/3\),
\[
 A(y)=\frac18\left(\frac{1+y}{1-y}\right)^3\sqrt{\frac{(3-y)(1-3y)}{y}},\qquad
 R(y)=\sqrt{\frac{3-y}{y(1-3y)}}.
\]
There is a unique \(y_\alpha\in(0,1/3)\) with \(A(y_\alpha)=\alpha\). The exact peak-splitting threshold is \(r_*(\alpha)=R(y_\alpha)\). For \(1<r\le r_*(\alpha)\), there is exactly **one strict local maximum** of the loss on positive frequencies; for \(r>r_*(\alpha)\), there are exactly **two strict local maxima** separated by one strict local minimum. Precisely at threshold, for \(\alpha\ne1\) there is an additional stationary shoulder that is not a local extremum; for \(\alpha=1\), the sole maximum is quartically flat.

The threshold is symmetric under exchanging the components: \(r_*(\alpha)=r_*(1/\alpha)\), satisfies \(r_*(1)=3+2\sqrt2\), and has the sharp unequal-strength law
\[
 r_*(\alpha)\sim8\max\{\alpha,\alpha^{-1}\}
 \quad\text{as }\max\{\alpha,\alpha^{-1}\}\to\infty.
\]
Near equal strengths its cusp is
\[
 r_*(\alpha)=3+2\sqrt2+K|\log\alpha|^{2/3}+o(|\log\alpha|^{2/3}),\qquad
 K=\frac{6^{2/3}}4\left(210+\frac{297\sqrt2}2\right)^{1/3}
 \approx6.18198051534.
\]

## Assumptions and scope
The complex susceptibility is
\[
 \chi^*(\omega)=\frac{a}{1+i\omega\tau_1}+\frac{b}{1+i\omega\tau_2},
 \qquad a,b>0,\quad 0<\tau_1<\tau_2,\quad \omega>0.
\]
Loss means \(L(\omega)=-\operatorname{Im}\chi^*(\omega)\); the overall additive frequency-independent real permittivity is immaterial. These are two *ideal*, uncoupled, purely Debye linear responses with finite positive strengths. The claim classifies exact mathematical stationary points and extrema, not instrument-resolvable experimental peaks.

## Proof
Put \(u=\omega\tau_1>0\), \(r=\tau_2/\tau_1\), and \(\alpha=a/b\). Scaling by \(b>0\) leaves modality unchanged:
\[
 \frac{L}{b}=\frac{\alpha u}{1+u^2}+\frac{ru}{1+r^2u^2}.
\]
The derivative has the same signs and positive zeros as the cubic polynomial in \(Y=u^2\)
\[
 P(Y)=\alpha(1-Y)(1+r^2Y)^2+r(1-r^2Y)(1+Y)^2.
\]
Its leading coefficient is negative and \(P(0)=\alpha+r>0\). Thus exactly one or three distinct positive critical roots can occur, barring degeneracies. The derivative of each component is positive below its individual peak and negative above it. Consequently, every stationary point is in \(1/r<u<1\). A multiple positive stationary point must satisfy both \(L'(u)=0\) and \(L''(u)=0\).

At such a point let \(y=u^2\in(0,1)\), \(z=r^2u^2>1\). Eliminating the strength ratio between the two equations yields
\[
 y(3-y)(1-z^2)=z(3-z)(1-y^2),
\]
which factors as \((y-z)(3yz-y-z+3)=0\). Since \(z>y\), one has \(z=(3-y)/(1-3y)\), forcing \(0<y<1/3\). Substitution into \(L'(u)=0\) gives
\[
 r=R(y),\qquad \alpha=A(y).
\]
These are necessary and sufficient equations for an interior multiple stationary root, because both original derivative conditions are recovered by substitution.

Differentiating yields the exact strict-monotonicity identity
\[
 \frac{d}{dy}\log A(y)
 =-\frac{3(y^2-6y+1)^2}{2y(3-y)(1-y)(1+y)(1-3y)}\le0.
\]
The equality occurs at only the isolated point \(y_0=3-2\sqrt2\), so \(A\) is strictly decreasing, with endpoint limits \(+\infty\) and \(0\). Hence each \(\alpha>0\) has a **unique** possible critical \(r=R(y_\alpha)\). At \(r=1\) the loss is a single Debye peak. At arbitrarily large \(r\) the derivative has alternating signs on four successive frequencies (for example at \(u=1/(2r)\), \(u=2/r\), \(u=1/2\), and \(u=2\), for sufficiently large \(r\)), producing three positive stationary points and therefore two maxima. Positive-root multiplicities cannot change except at the unique multiple-root curve, since \(P(0)>0\), its cubic leading coefficient never vanishes, and roots stay in the bounded interval \(1/r^2<Y<1\). This proves the complete modality classification. If \(\alpha\ne1\), the multiple root is double, giving a stationary shoulder, because the sole triple-root degeneracy occurs at \(y_0\), where \(A(y_0)=1\). At balance symmetry about the geometric-mean log frequency yields a quartically flat central maximum.

Exchanging the two Debye terms and rescaling frequency by the geometric mean proves \(r_*(\alpha)=r_*(1/\alpha)\). Direct substitution of \(y_0\) gives \(R(y_0)=3+2\sqrt2\). As \(y\downarrow0\), \(A(y)\sim\sqrt3/(8\sqrt y)\) and \(R(y)\sim\sqrt3/\sqrt y\), giving \(r_*(\alpha)\sim8\alpha\) as \(\alpha\to\infty\); symmetry gives the other tail.

For the cusp put \(\ell(y)=\log A(y)\) and \(C=210+297\sqrt2/2\). At \(y_0\), exact differentiation gives
\[
 \ell(y_0)=\ell'(y_0)=\ell''(y_0)=0,\quad \ell'''(y_0)=-C,
 \qquad R'(y_0)=0,\quad R''(y_0)=C/2.
\]
Thus \(\log\alpha=-C(y-y_0)^3/6+o((y-y_0)^3)\) while \(R(y)-R(y_0)=C(y-y_0)^2/4+o((y-y_0)^2)\). Eliminating \(y-y_0\) establishes the claimed coefficient and exponent \(2/3\).

## Verification
Run `python verify.py` with Python, NumPy, SciPy and SymPy. It reproduces symbolic Wronskian factorization, strength-curve elimination, monotonicity identity, critical equal-strength constants and cusp derivatives. It additionally compares the threshold with direct positive roots of the cubic for seven strength ratios, independent sampled log-frequency loss curves for five ratios and two large-strength asymptotic checks. The verifier returned `PASS 31 checks; cusp coefficient 6.181980515339464`. Numerical tests corroborate but are not used to establish infinite-parameter quantifiers.

Representative critical time ratios are \(r_*(0.1)\approx79.8872\), \(r_*(1)=5.82842712\), and \(r_*(10)\approx79.8872\).

## Relationship to prior work
The additive-response treatment of physically distinct dielectric processes is established, including Jakobsen *et al.* (2008), who separate a dominant Debye-like response from a secondary non-Debye process in mono-alcohols. Their experiments neither satisfy the two-exact-Debye hypotheses in general nor provide a universal exact two-peak boundary. Došlá (2009) develops general implicit modality criteria for two unimodal mixtures and explicit criteria for Cauchy and logistic mixtures, among other specified distributions. A Debye loss expressed against log frequency is proportional to a *hyperbolic-secant* component, whereas the logistic density has a squared hyperbolic-secant profile; the logistic-specific threshold is not the present result. The generic implicit criterion applies in principle, but the exact unique algebraic physical threshold, extreme-contrast coefficient and \(2/3\) cusp require the explicit elimination above and are not reported in the inspected source. Earlier equal-strength two-Cole–Cole or four-Debye mode counts do not entail the unequal-strength threshold or its cusp.

## Limitations
The idealized additive two-Debye response excludes non-Debye broadening, dispersive strengths, interacting relaxation channels, conductor backgrounds, finite frequency ranges, peak detection noise and instrument resolution. A strict mathematical local maximum is not necessarily distinguishable experimentally. The proof does not assert a universal criterion for mixtures of arbitrary unimodal spectra or a priority guarantee over unindexed literature.

## References
- B. Jakobsen, C. Maggi, T. Christensen and J. C. Dyre, *Investigation of the shear-mechanical and dielectric relaxation processes in two mono-alcohols close to the glass transition*, first public arXiv posting 2008-05-29, https://arxiv.org/abs/0805.4519.
- Š. Došlá, *Conditions for bimodality and multimodality of a mixture of two unimodal densities*, Kybernetika **45** (2009), 279–292, https://www.dml.cz/handle/10338.dmlcz/140075.
