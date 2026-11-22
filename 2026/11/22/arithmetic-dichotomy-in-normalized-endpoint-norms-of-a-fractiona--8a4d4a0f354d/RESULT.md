# Arithmetic dichotomy in normalized endpoint norms of a fractional unilateral-shift semigroup

## Finding

Let \(1<\alpha<2\), let \(S_p\) be the unilateral right shift on complex \(\ell^p(\mathbb N_0)\), and let \(T_{\alpha,p}(t)=\exp[-t(I-S_p)^\alpha]\) for \(t\geq0\), with the binomial fractional power. An exact exponential growth rate is common to the endpoint norm and Hilbert norm, but their ratio has a sharp arithmetic dichotomy.

Put
\[
\phi=\frac{\pi}{\alpha+1},\quad
\theta=\frac{\pi(\alpha-1)}{\alpha+1},\quad
\delta=2\cos\phi,\quad
c=\delta^\alpha\cos\phi,\quad
b=\delta^\alpha\sin\phi,\quad
v=\alpha\delta^{\alpha-1},
\]
\[
K=\frac v2\left((\alpha+1)-i(\alpha-1)\tan\phi\right),\qquad
u=\operatorname{Re}(K^{-1}),\quad \omega=\operatorname{Im}(K^{-1}).
\]
All of \(b,c,v,\nu,\omega,\operatorname{Re}K\) are positive. For every \(t\geq0\),
\[
\|T_{\alpha,2}(t)\|=e^{ct}.
\]
Define \(R_\alpha(t)=e^{-ct}\|T_{\alpha,1}(t)\|\) and
\[
C_\alpha=\frac4\pi\sqrt{\frac{|K|}{\operatorname{Re}K}}
=\frac4\pi\left(1+\frac{(\alpha-1)^2\tan^2\phi}{(\alpha+1)^2}\right)^{1/4}.
\]
If \(\alpha\) is irrational, \(\lim_{t\to\infty}R_\alpha(t)=C_\alpha\).

If \(\alpha\) is rational, uniquely write \(\theta/\pi=a/q\) with coprime positive integers \(a,q\) (necessarily \(q\geq4\)), and define
\[
F_{\alpha,q}(s)=\frac{2}{q\sqrt{2\pi|K|}}\sum_{r=0}^{q-1}
\int_{\mathbb R}e^{-\nu y^2/2}
\left|\cos\left(s-r\theta-\frac{\arg K}{2}-\frac{\omega y^2}{2}\right)\right|\,dy.
\]
Then
\[
R_\alpha(t)=F_{\alpha,q}(bt)+o(1)\qquad(t\to\infty).
\]
The positive, continuous function \(F_{\alpha,q}\) is nonconstant, has fundamental period \(\pi/q\), and has mean \(C_\alpha\) over that period. In particular, the normalized endpoint norm has no limit for rational orders, and its exact liminf and limsup are respectively the minimum and maximum of the displayed one-variable function.

## Assumptions and scope

The shift is \(S_p(x_0,x_1,\ldots)=(0,x_0,x_1,\ldots)\). The power \((I-S_p)^\alpha=\sum_{k\geq0}(-1)^k\binom\alpha k S_p^k\) converges absolutely in operator norm since its coefficients are \(O(k^{-\alpha-1})\). The complex power is the principal branch, continued from the open right half-plane to the closed right half-plane. Values at the circle point \(1\) are defined by continuity. All limits concern real \(t\to+\infty\). The theorem deliberately excludes orders \(\alpha\leq1\) and \(\alpha\geq2\), and does not assert the same result for other sequence norms.

## Proof

**1. Norm identities and the two maxima.** Write \(f_t(z)=\exp[-t(1-z)^\alpha]=\sum_{n\geq0}a_n(t)z^n\). Absolute summability follows by the holomorphic functional calculus in the Wiener algebra: the binomial series for \((1-z)^\alpha\) is absolutely summable and the Wiener algebra is closed under exponentials. Convolution by \((a_n(t))\) has \(\ell^1\) norm \(\sum_{n\geq0}|a_n(t)|\), with equality on the first unit vector. The unitary identification \(\ell^2(\mathbb N_0)\cong H^2\) makes the same operator multiplication by \(f_t\), so its norm is \(\max_{|z|=1}|f_t(z)|\).

Set \(\psi(x)=-(1-e^{ix})^\alpha\). On \(0<x<\pi\), write \(1-e^{ix}=2\cos\varphi\,e^{-i\varphi}\), \(\varphi=(\pi-x)/2\). Direct differentiation gives
\[
\frac{d}{d\varphi}\left[-(2\cos\varphi)^\alpha\cos(\alpha\varphi)\right]
=\alpha 2^\alpha(\cos\varphi)^{\alpha-1}\sin((\alpha+1)\varphi).
\]
Thus \(\operatorname{Re}\psi\) has precisely two global maximizers on the circle, at \(x=\pm\theta\), with common maximum \(c\). Direct differentiation at the positive maximizer gives
\[
\psi(\theta)=c+ib,\qquad \psi'(\theta)=iv,\qquad -\psi''(\theta)=K.
\]
Conjugation shows \(\psi(-\theta)=c-ib\), \(\psi'(-\theta)=iv\), and \(-\psi''(-\theta)=\overline K\). It follows that \(\|T_{\alpha,2}(t)\|=e^{ct}\) for all \(t\geq0\).

**2. Uniform two-saddle coefficient asymptotic.** Fourier inversion yields \(a_n(t)=(2\pi)^{-1}\int_{-\pi}^{\pi}e^{t\psi(x)-inx}\,dx\). Fix \(L>0\) and write \(n=vt+y\sqrt t\), \(|y|\leq L\). Near \(\theta\), substitute \(x=\theta+z/\sqrt t\), use the Taylor expansion with curvature \(K\), and integrate the limiting complex Gaussian. Near \(-\theta\) one obtains the complex conjugate term. On the rest of the circle the real part of \(\psi\) is at most \(c-\eta\) for some \(\eta>0\). Standard dominated Laplace estimates, uniform for bounded \(y\), therefore give
\[
a_n(t)=\frac{2e^{ct}}{\sqrt{2\pi t|K|}}
 e^{-\nu y^2/2}
 \cos\left(bt-n\theta-\frac{\arg K}{2}-\frac{\omega y^2}{2}\right)
 +o_L(e^{ct}t^{-1/2}).\tag{1}
\]
Indeed, the positive-frequency saddle is \(e^{t(c+ib)-in\theta}(2\pi t K)^{-1/2}\exp[-y^2/(2K)]\), and the negative-frequency saddle is its conjugate. The principal square root of \(K\), which has positive real part, fixes the displayed phase and normalization.

**3. Control of all coefficients outside the Gaussian window.** Parseval for \(f_t(e^{ix})=e^{t\psi(x)}\) gives
\[
\sum_{n\geq0}|a_n(t)|^2=O(e^{2ct}t^{-1/2}).\tag{2}
\]
Since \(\psi'\) exists and is bounded on the whole circle for \(\alpha>1\), Parseval for \((-i\partial_x-vt)e^{t\psi(x)}=t(-i\psi'(x)-v)e^{t\psi(x)}\) gives
\[
\sum_{n\geq0}(n-vt)^2|a_n(t)|^2=O(e^{2ct}t^{1/2}).\tag{3}
\]
To justify (3), the factor \(-i\psi'(x)-v\) vanishes linearly at **both** maximizers; the Gaussian localization contributes \(t^{-3/2}\) before multiplication by \(t^2\); the complement contributes exponentially less. By weighted Cauchy–Schwarz and (3), for \(L\geq1\),
\[
e^{-ct}\sum_{|n-vt|>L\sqrt t}|a_n(t)|
\leq C L^{-1/2}.\tag{4}
\]
Consequently, (1) gives the complete endpoint norm after first letting \(t\to\infty\) with a fixed window, then letting \(L\to\infty\). This rules out hidden mass in the coefficient tails.

**4. Irrational orders.** Since \(\theta/\pi=(\alpha-1)/(\alpha+1)\), the angle is irrational exactly when the order is irrational. The absolutely uniformly convergent Fourier series
\[
|\cos x|=\frac2\pi+\frac4\pi\sum_{k\geq1}\frac{(-1)^k}{1-4k^2}\cos(2kx)
\]
shows that only its constant term survives in a Gaussian-weighted sum over \(n\) when \(\theta/\pi\) is irrational. For each nonzero Fourier harmonic, the partial sums of \(e^{2ikn\theta}\) are bounded; Abel summation against the slowly varying profile over a window of size \(\sqrt t\) makes the normalized sum tend to zero, uniformly in the time-dependent phase. Uniform convergence of the Fourier series allows interchange of the limits. Thus (1)–(4) give
\[
\lim_{t\to\infty}R_\alpha(t)
=\frac{2}{\sqrt{2\pi|K|}}\frac2\pi
\int_{\mathbb R}e^{-\nu y^2/2}\,dy
=\frac4\pi\sqrt{\frac{|K|}{\operatorname{Re}K}}.
\]

**5. Rational orders and strict oscillation.** If \(\theta/\pi=a/q\) in lowest terms, grouping coefficient indices by \(n\bmod q\) makes each congruence class a Riemann sum with mesh \(q/\sqrt t\). Equations (1)–(4) then give \(R_\alpha(t)=F_{\alpha,q}(bt)+o(1)\). Shifting \(s\) by \(\pi/q\) permutes the \(q\) residue-class phases modulo \(\pi\), because \(a\) and \(q\) are coprime. The Fourier series for \(|\cos|\) shows that precisely the harmonics indexed by multiples of \(q\) survive. Its first surviving nonconstant harmonic has a nonzero coefficient: the coefficient at frequency \(2q\) is a nonzero multiple of
\[
\int_{\mathbb R}e^{-\nu y^2/2}e^{-iq\omega y^2}\,dy
=\sqrt{\frac{2\pi}{\nu+2iq\omega}}\ne0.
\]
Hence \(F_{\alpha,q}\) is nonconstant, and its first harmonic enforces fundamental period \(\pi/q\). Averaging over a period removes the nonconstant harmonics and gives exactly \(C_\alpha\). Continuity, positivity, and compactness of a period interval give the asserted limiting extrema. Since \(b>0\), the argument \(bt\) traverses infinitely many complete periods as real \(t\to\infty\), so no limit exists. This completes the proof.

## Verification

All derivative and saddle identities are elementary algebraic identities given explicitly above. The finite reproducibility program `CHECK.py` evaluates those identities, samples the full boundary maximum, tests predicted rational periodicity and nonconstancy, and compares finite Fourier-coefficient approximations to both asymptotic profiles for two rational and one irrational order. Its successful result is `FRACTIONAL_WIENER_ARITHMETIC_DIAGNOSTIC_OK 49`. These finite checks are supplementary; infinite uniformity and tail control are provided by the proof, not by a numerical extrapolation.

## Relationship to prior work

Barberán and Miana [1] give the fractional-shift polynomial coefficients, absolute summability, and applications to entire groups and the Wiener algebra, thereby providing the natural starting object. Their results do not state the large-time sharp ratio between \(\ell^1\) and \(\ell^2\) operator norms, nor its dependence on arithmetic of the fractional order. Girard [2] treats norms of high powers of absolutely convergent Fourier series. His Section 4 obtains additive contributions when different spectral maxima have **different drift slopes** and warns that same-slope interference may prevent convergence; here the two maximizers have the **same drift slope**, and we compute the complete surviving interference and its arithmetic law. The complex-sequence local limit results [3,4] provide relevant general Gaussian techniques for convolution powers. They do not explicitly determine this continuous fractional-shift semigroup's rational oscillation profile, the sharp irrational constant, or the exact normalization against its Hilbert-space norm. The proof above is self-contained and does not require a claimed general local-limit theorem beyond its published hypotheses.

## Limitations

The result covers real nonnegative times, fractional orders strictly between one and two, and the unilateral shift on complex \(\ell^1\) and \(\ell^2\). It does not classify the operator norm on other \(\ell^p\) spaces, or behavior at the integer endpoints. The \(o(1)\) remainder has no stated uniform rate as the order approaches a rational number or an endpoint. As with any originality assessment based on available literature, equivalent earlier statements under other terminology may exist. No independent mathematical audit has been performed.

## References

[1] R. Barberán and P. J. Miana, *Entire groups generated by fractional powers of operators*, arXiv:2606.16895, first publicly posted 2026-06-15. https://arxiv.org/abs/2606.16895

[2] D. M. Girard, *The asymptotic behavior of norms of powers of absolutely convergent Fourier series*, Pacific Journal of Mathematics 37 (1971), 357–381, especially §4, pp. 379–380. https://msp.org/pjm/1971/37-2/pjm-v37-n2-p09-p.pdf

[3] L. Coeuret, *Local limit theorem for complex valued sequences*, arXiv:2201.01514 (2022); Asymptotic Analysis 142 (2025), 379–431. https://arxiv.org/abs/2201.01514

[4] J.-F. Coulombel and G. Faye, *The local limit theorem for complex valued sequences: the parabolic case*, arXiv:2408.12876 (2024). https://arxiv.org/abs/2408.12876
