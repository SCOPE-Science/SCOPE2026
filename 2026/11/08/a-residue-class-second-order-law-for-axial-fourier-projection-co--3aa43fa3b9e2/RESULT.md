# A residue-class second-order law for axial Fourier projection constants

## Finding

For \(q=3,4\), let \(G_{q,d}=(\mathbb Z/q\mathbb Z)^d\), with normalized counting measure, and let \(G_{\infty,d}=\mathbb T^d\), with normalized Haar measure. Here \(d\ge1\), and \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). Let \(E_{q,d}\) be the real span of the \(2d\) functions \(\cos(2\pi x_j/q)\) and \(\sin(2\pi x_j/q)\) for finite \(q\), or \(\cos x_j\), \(\sin x_j\) on the torus. These are the *axial first-frequency* functions, not the full first Hamming level when \(q=4\).

Let \(\Lambda_q(d)\) be the minimum norm of any bounded real-linear projection \(C(G_{q,d};\mathbb R)\to E_{q,d}\), with the uniform norm. The normalized-Haar orthogonal projection is minimum-norm and, for every \(d\ge1\),
\[
\Lambda_3(d)=\frac{4d}{3}\binom{d-1}{\lfloor d/3\rfloor}
 \left(\frac13\right)^{\lfloor d/3\rfloor}
 \left(\frac23\right)^{d-1-\lfloor d/3\rfloor},
\qquad
\Lambda_4(d)=\frac{2d}{4^d}\binom{2d}{d},
\]
while
\[
\Lambda_\infty(d)=\frac2\pi\int_0^\infty
\frac{1-J_0(2t)^d}{t^2}\,dt.
\]
Here \(J_0\) is the order-zero Bessel function of the first kind; the integral is absolutely convergent.

The **second-order law** is
\[
\begin{aligned}
\Lambda_3(d)&=2\sqrt{\frac d\pi}\left[1+\frac{c_{d\bmod3}}d+O(d^{-2})\right],\\
\Lambda_4(d)&=2\sqrt{\frac d\pi}\left[1-\frac1{8d}+O(d^{-2})\right],\\
\Lambda_\infty(d)&=2\sqrt{\frac d\pi}\left[1+\frac1{16d}+O(d^{-2})\right],
\end{aligned}
\qquad c_0=-\frac7{24},\quad c_1=c_2=\frac5{24}.
\]
The constants implicit in the three error terms are absolute for these fixed models. Consequently,
\[
\lim_{m\to\infty}\sqrt{\pi(3m+r)}\,
 [\Lambda_3(3m+r)-\Lambda_\infty(3m+r)]
 =\begin{cases}-17/24,&r=0,\\7/24,&r=1,2,\end{cases}
\]
and
\[
\lim_{d\to\infty}\sqrt{\pi d}\,[\Lambda_4(d)-\Lambda_\infty(d)]=-3/8.
\]
Thus a ternary grid *alternately underestimates and overestimates* the continuous first-frequency projection norm according to dimension modulo three; the quaternary grid underestimates it for all sufficiently large dimensions. All models share the leading term \(2\sqrt{d/\pi}\). The finding is the precise comparison and residue-dependent correction, not the classical translation-averaging principle, binomial identities, or the leading Gaussian limit in isolation.

## Assumptions and scope

The domain is the compact abelian product group above, with normalized Haar measure and real continuous functions. The subspace contains only the \(2d\) axial frequency modes; it does not contain constants, products of frequencies, or higher harmonics. For \(q=3,4\), sine and cosine form two independent real modes in every coordinate. For the torus, continuous functions are used, although the convolution norm may be approached rather than attained by a continuous sign function. The comparison uses a common number \(d\) of coordinates, not a common total number of group elements.

## Proof

**1. Minimum projection and kernel.** Write \(\chi_j(x)=e^{2\pi i x_j/q}\) for finite \(q\) and \(\chi_j(x)=e^{ix_j}\) on the torus. Character orthogonality shows that the orthogonal projector onto \(E_{q,d}\) is convolution with
\[
K_{q,d}(x)=\sum_{j=1}^d(\chi_j(x)+\overline{\chi_j(x)})
=2\sum_{j=1}^d\cos(2\pi x_j/q),
\]
with the evident torus interpretation. Consequently its operator norm is \(\int|K_{q,d}|\): for finite groups, take the sign of the kernel, and for the torus approximate the measurable sign in \(L^1(|K|\,d\mu)\) by continuous functions bounded by one. Translation-averaging any competing bounded projection onto \(E_{q,d}\) does not increase its norm. The average commutes with all translations. Such an invariant projection is uniquely determined by its character multipliers: it acts as identity on the selected characters and annihilates all other characters. Hence the convolution projector is minimum-norm, not merely the normalized-Haar orthogonal projector.

**2. Ternary exact expression.** At a uniformly chosen point of \(G_{3,d}\), the \(d\) summands \(2\cos(2\pi x_j/3)\) independently equal \(2\) with probability \(1/3\) and \(-1\) with probability \(2/3\). With \(B\sim\operatorname{Bin}(d,1/3)\), their sum is \(3B-d\). Put \(k=\lfloor d/3\rfloor\). The identities \(\mathbb E(3B-d)=0\) and \(\mathbb E[B\mathbf1_{B\ge k+1}]=(d/3)\Pr(\operatorname{Bin}(d-1,1/3)\ge k)\) yield
\[
\begin{split}
\mathbb E|3B-d|
&=2d\{\Pr(\operatorname{Bin}(d-1,1/3)\ge k)
 -\Pr(B\ge k+1)\}\\
&=\frac{4d}{3}\Pr(\operatorname{Bin}(d-1,1/3)=k).
\end{split}
\]
This proves the first exact expression for all positive integers \(d\), including the cases where \(3\mid d\) and the kernel can vanish.

**3. Quaternary exact expression.** The single-coordinate kernel \(2\cos(\pi x/2)\) on \(\mathbb Z/4\mathbb Z\) has law \(2,0,-2,0\) at the four sites. It is exactly the law of the sum of two independent fair signs. The whole kernel therefore has the law of the sum of \(2d\) fair signs. Its expected absolute value, calculated by the same adjacent-binomial-mass identity, is \(2d\binom{2d}{d}/4^d\). The probability identity is an equality in distribution, not an approximation or a central-limit argument.

**4. Shifted Stirling expansion.** Let \(r\in\{0,1,2\}\) be the residue of \(d\) modulo three, and put \(k=(d-r)/3\). The binomial mass in step 2 can be written exactly as
\[
p_d=\frac{\Gamma(d)}{\Gamma(d/3+1-r/3)\Gamma(2d/3+r/3)}
 3^{-(d-r)/3}(2/3)^{(2d+r-3)/3}.
\]
For fixed \(a>0\) and fixed \(b\), the standard uniform shifted Stirling expansion is
\[
\log\Gamma(ad+b)
=ad(\log(ad)-1)+(b-\tfrac12)\log(ad)
 +\tfrac12\log(2\pi)
 +\frac{b(b-1)/2+1/12}{ad}+O(d^{-2}).
\]
Substituting the three pairs \((a,b)=(1,0),(1/3,1-r/3),(2/3,r/3)\), and collecting terms, gives
\[
\log p_d=-\frac12\log d+\log\frac3{2\sqrt\pi}
 +\frac{c_r}{d}+O(d^{-2}),
\qquad (c_0,c_1,c_2)=(-7/24,5/24,5/24).
\]
Exponentiating and multiplying by \(4d/3\) proves the ternary second-order law. The standard central binomial expansion
\[\binom{2d}{d}=\frac{4^d}{\sqrt{\pi d}}
(1-1/(8d)+O(d^{-2}))\]
proves its quaternary counterpart.

**5. Continuous second order with a controlled remainder.** Let \(U\) be uniform on \([0,2\pi)\). The characteristic function of \(2\cos U\) is \(J_0(2t)\). For a symmetric integrable random variable \(Y\), the elementary cosine representation of absolute value gives
\[
\mathbb E|Y|=\frac2\pi\int_0^\infty
\frac{1-\mathbb E\cos(tY)}{t^2}\,dt.
\]
Apply this to \(d\) independent copies of \(2\cos U\). To expand, set \(t=s/\sqrt{2d}\). For \(s\) in a slowly growing interval and \(d\to\infty\), the Taylor series of \(J_0\) gives
\[
d\log J_0(\sqrt{2/d}\,s)=-s^2/2-s^4/(16d)+O(s^6/d^2),
\]
whence
\[
J_0(\sqrt{2/d}\,s)^d=e^{-s^2/2}
\left(1-\frac{s^4}{16d}
 +O((s^6+s^8)/d^2)\right).
\]
For justification under the improper integral, split at \(s=d^{1/10}\) and at \(t=\delta\) for fixed sufficiently small \(\delta>0\). The interval below \(d^{1/10}\) has a uniform Gaussian-polynomial majorant. Between \(d^{1/10}\) and \(\delta\sqrt{2d}\), the bound \(|J_0(2t)|\le e^{-c t^2}\) for \(|t|\le\delta\) makes the contribution exponentially small in \(d^{1/5}\). For \(t\ge\delta\), continuity, strict \(|J_0(2t)|<1\) away from zero, and the standard decay \(J_0(t)=O(t^{-1/2})\) make the integral of \(|J_0(2t)|^d/t^2\) exponentially small. Thus the remainder after integration is \(O(d^{-2})\) relative to the leading \(\sqrt d\) term. Finally,
\[
\int_0^\infty\frac{1-e^{-s^2/2}}{s^2}\,ds
=\int_0^\infty s^2e^{-s^2/2}\,ds=\sqrt{\pi/2}.
\]
The continuous expansion follows with relative coefficient \(1/16\).

**6. The signed comparisons.** Subtracting the expansions gives the stated limits. Their nonzero values imply the corresponding strict signs for all sufficiently large admissible dimensions. No claim is made that these signs already hold in every small dimension.

## Verification

Run the embedded `checker.py` with Python 3, SciPy, and mpmath. It independently enumerates all full finite-group convolution kernel rows for \(q=3,4\) and \(1\le d\le6\), checks exact rational agreement with the two binomial formulas, compares high-precision masses against the three claimed residue coefficients and the quaternary coefficient for six large dimensions per model, and verifies the continuous second-order expansion by an independent characteristic-function quadrature for four dimensions. Its finite checks do not establish the expansions. In dimension one the continuous value is exactly \(4/\pi\), and in dimension two it is exactly \(16/\pi^2\); these values provide additional independent normalization checks.

## Relationship to prior work

The translation-averaging/minimal-invariant-projection argument is classical; the Krawtchouk-transform and Bernoulli-walk formulas of Feinsilver and Schott provide nearby discrete harmonic-analysis machinery. Fourier analysis on finite products and the first-level viewpoint are likewise standard. More recent work of Defant, Galicer, Mansilla, Mastyło and Muro studies projection constants on Boolean and nonbinary Hamming schemes and establishes leading Gaussian limits. In the nonbinary *full first Hamming level*, the ternary case agrees with the present two-character-per-coordinate subspace, while the quaternary case has an additional order-two character and is not the same subspace. The new statement assessed here is the joint residue-sensitive **second-order** comparison for the two axial finite alphabets against the continuous torus. General leading-order projection theorems cannot determine the sign of this correction. The exact binomial identities and their individual Stirling consequences are elementary and are not separately advanced as new mathematical claims.

The primary manuscript on general nonbinary Hamming projection constants (arXiv:2607.05594) could not be inspected in full; its accessible abstract and third-party synopsis describe leading projection limits but do not settle the presence or absence of the specific second-order comparisons here. This is an explicit unresolved bibliographic priority risk, not evidence of uniqueness.

## Limitations

Only the axial \(2d\)-dimensional Fourier subspace and the three specified ambient groups are covered. The result does not assert analogous corrections for \(q=5,6\) or general mixed alphabets. The second-order error bounds are asymptotic in dimension and do not provide an effective universal threshold for the sign comparisons. The exact identities do not imply existence of a norming continuous input on the torus; finite-group sign inputs do attain the projector norm. Independent mathematical audit has not been performed.

## References

- Ronald de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Library 1 (published 2008-09-25), DOI: 10.4086/toc.gs.2008.001.
- Philip Feinsilver and René Schott, *Krawtchouk transforms and Convolutions*, first posted 2014-09-16, arXiv:1409.4715. In particular, Sections 2–4 on Bernoulli walks, transforms and convolution.
- Andreas Defant, Daniel Galicer, Martín Mansilla, Mieczysław Mastyło and Santiago Muro, *Projection constants for spaces of Dirichlet polynomials*, first posted 2023-02-01, arXiv:2302.00231.
- Andreas Defant, Daniel Galicer, Martín Mansilla, Mieczysław Mastyło and Santiago Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, first posted 2023-02-01, arXiv:2302.00233.
- Andreas Defant, Daniel Galicer, Martín Mansilla, Mieczysław Mastyło and Santiago Muro, *Support-Sensitive Bohnenblust–Hille Inequalities and Local Invariants on Hamming Schemes*, first posted 2026-07-06, arXiv:2607.05594 (full text unavailable for this comparison).
