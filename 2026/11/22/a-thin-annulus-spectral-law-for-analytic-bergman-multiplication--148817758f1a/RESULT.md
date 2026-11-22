# A thin-annulus spectral law for analytic Bergman multiplication commutators

## Finding
Let \(0<r<1\), let \(A_r=\{z\in\mathbb C:r<|z|<1\}\), and let \(A^2(A_r)\) be its analytic Bergman space with planar area norm. For any fixed integer \(m\ge1\), set \(C_{r,m}=M_{z^m}^{*}M_{z^m}-M_{z^m}M_{z^m}^{*}\) and \(\varepsilon=-\log r\). Then \(C_{r,m}\) is positive, compact, injective, and belongs to \(\mathcal S_p\) **exactly for** \(p>1/2\). Its positive eigenvalues, counted with multiplicities and arranged nonincreasingly, satisfy
\[
\lim_{j\to\infty}j^2s_j(C_{r,m})=m^2(1+r^m)^2,
\qquad \operatorname{Tr}C_{r,m}=m(1-r^{2m}).
\]
Set
\[
\Theta(y)=\begin{cases}y^{-2}-\sinh^{-2}y,&y\ne0,\\1/3,&y=0.\end{cases}
\]
The function \(\Theta\) is positive, even, strictly decreasing on \((0,\infty)\), and tends to zero. For every fixed \(p>1/2\), the thin-annulus limit has the exact scaling law
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{1-2p}\operatorname{Tr}(C_{e^{-\varepsilon},m}^{p})
=m^{2p}\int_{\mathbb R}\Theta(y)^p\,dy.}
\]
In particular, the limiting Hilbert–Schmidt constant has the closed form
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-3}\|C_{e^{-\varepsilon},m}\|_{\mathcal S_2}^2
=\frac{8m^4}{\pi^2}\bigl(\zeta(2)-\zeta(3)\bigr).}
\]
The operator norm and all positive-threshold eigenvalue counts obey
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-2}\|C_{e^{-\varepsilon},m}\|=m^2/3,}
\]
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon\,\#\{j:s_j(C_{e^{-\varepsilon},m})>m^2\varepsilon^2t\}
=2\Theta_{(0,\infty)}^{-1}(t)\quad(0<t<1/3).}
\]
At \(t\ge1/3\), the limit of the rescaled count is zero; at \(t=0\) each positive count is infinite. Thus the profile describes a locally finite distribution away from zero, not a finite probability measure.

## Assumptions and scope
The area normalization is immaterial since a common positive scaling of the Hilbert norm does not alter an adjoint. On the orthonormal Laurent monomial basis \(e_n(z)=z^n/\|z^n\|\), \(n\in\mathbb Z\), put
\[
I_n=\int_r^1t^{2n+1}\,dt=
\begin{cases}\dfrac{1-r^{2n+2}}{2(n+1)},&n\ne-1,\\-\log r,&n=-1.\end{cases}
\]
Then \(\|z^n\|^2=2\pi I_n\). The integer \(m\) is held fixed when \(r\uparrow1\). All trace powers use the positive functional calculus; \(p\) is fixed and strictly greater than \(1/2\) in the thin-annulus trace limit. There is no assertion of summability for \(p\le1/2\).

## Proof
**Exact spectrum and fixed-annulus tails.** Multiplication by \(z^m\) is an \(m\)-step bilateral weighted shift:
\[
M_{z^m}e_n=\sqrt{I_{n+m}/I_n}\,e_{n+m}.
\]
Consequently \(C_{r,m}e_n=a_ne_n\), where
\[
a_n=\frac{I_{n+m}}{I_n}-\frac{I_n}{I_{n-m}}.
\]
The strict Cauchy–Schwarz inequality for the nondegenerate interval measure \(t^{2n+1}dt\) gives \(I_n^2<I_{n-m}I_{n+m}\), hence every \(a_n>0\). The exact moment formulas give, as \(n\to+\infty\) and \(n\to-\infty\) respectively,
\[
a_n\sim m^2n^{-2},\qquad a_n\sim m^2r^{2m}n^{-2}.
\]
Thus the operator is positive, compact and injective and is in \(\mathcal S_p\) exactly for \(p>1/2\). The two tails yield the counting law \(\#\{n:a_n>t\}\sim m(1+r^m)t^{-1/2}\) as \(t\downarrow0\), hence the announced ordered-eigenvalue coefficient. Telescoping \(a_n=b_n-b_{n-m}\), with \(b_n=I_{n+m}/I_n\), and the limits \(b_{+\infty}=1\), \(b_{-\infty}=r^{2m}\), yields \(\sum_n a_n=m(1-r^{2m})\).

**Logarithmic moment curvature and a uniform bound.** For \(\varepsilon=-\log r\), let \(y_n=\varepsilon(n+1)\), \(h=m\varepsilon\), and
\[
F(y)=\int_0^1e^{-2yt}\,dt=e^{-y}\frac{\sinh y}{y},\qquad L(y)=\log F(y).
\]
The continuous values at zero are understood. Since \(I_n=\varepsilon F(y_n)\), the exact eigenvalue expression becomes
\[
a_n=\exp(L(y_n+h)-L(y_n))-\exp(L(y_n)-L(y_n-h)).
\]
Direct differentiation gives \(L''(y)=\Theta(y)\), while \(-2<L'(y)<0\) follows from the integral expression for \(F\) (its logarithmic derivative is \(-2\) times a tilted mean of \(t\in(0,1)\)). Thus both exponential arguments are nonpositive and the exponential map is one-Lipschitz on their range. Therefore
\[
0<a_n\le L(y_n+h)-2L(y_n)+L(y_n-h)
=\int_{-h}^{h}(h-|u|)\Theta(y_n+u)\,du.
\]
The function \(\Theta\) is positive by strict log-convexity of the Laplace transform \(F\). It is even, satisfies \(\Theta(0)=1/3\), and has \(\Theta(y)=y^{-2}+O(e^{-2|y|})\) at infinity. Its derivative for \(y>0\) is \(2(\cosh y/\sinh^3y-1/y^3)<0\): indeed \(\sinh^3 y>y^3\cosh y\), as follows coefficientwise from \(\sinh^3y=(\sinh3y-3\sinh y)/4\); the \(y^3\) and \(y^5\) coefficients agree and every coefficient from \(y^7\) onward is strictly larger. Consequently \(0<\Theta(y)\le1/3\), and for \(0<h\le1\) there is an absolute \(B\) with
\[
0<a_n\le h^2/3,\qquad a_n/h^2\le B/(1+y_n^2).
\]
On every compact interval of \(y_n\), Taylor's formula in the exact exponential representation gives \(a_n/h^2=\Theta(y_n)+O(h)\) uniformly (in fact the error can be improved). These bounds establish both the pointwise limiting spectral profile and its integrable tails.

**All Schatten limits, norm and counting.** For fixed \(p>1/2\), \((1+y^2)^{-p}\) is integrable. Apply dominated Riemann-sum convergence to \(h^{-2p}a_n^p\) on the \(\varepsilon\)-mesh \(y_n\), using the uniform tail bound just proved:
\[
\varepsilon\sum_{n\in\mathbb Z}(a_n/h^2)^p\longrightarrow\int_{\mathbb R}\Theta(y)^p\,dy.
\]
Substitute \(h=m\varepsilon\). The global upper bound \(a_n\le h^2/3\), plus indices with \(y_n\to0\), proves the sharp norm limit. Since \(\Theta\) decreases strictly from \(1/3\) to zero on the positive half-line, compact-window Riemann counting and the uniform tail estimate give the positive-level counting limit; the threshold boundary has Lebesgue measure zero. At or above \(1/3\) the rescaled count tends to zero by the same compactness and upper-bound argument.

**Exact quadratic moment.** Euler's convergent product \(\sinh y/y=\prod_{k\ge1}(1+y^2/(\pi^2k^2))\) yields
\[
\Theta(y)=\frac{d^2}{dy^2}\sum_{k\ge1}\log(1+y^2/(\pi^2k^2)).
\]
Taking Fourier transforms with convention \(\widehat f(\xi)=\int_{\mathbb R}e^{-i\xi y}f(y)dy\), the elementary Cauchy-kernel transform (applied after differentiation) gives
\[
\widehat\Theta(\xi)=2\pi|\xi|\sum_{k\ge1}e^{-\pi k|\xi|}=
\frac{2\pi|\xi|}{e^{\pi|\xi|}-1},
\]
with continuous value \(2\) at \(\xi=0\). Plancherel and the positive series \((e^t-1)^{-2}=\sum_{j\ge2}(j-1)e^{-jt}\) give
\[
\int_{\mathbb R}\Theta(y)^2dy
=\frac4{\pi^2}\int_0^\infty\frac{t^2}{(e^t-1)^2}\,dt
=\frac8{\pi^2}\sum_{j=2}^\infty\frac{j-1}{j^3}
=\frac8{\pi^2}(\zeta(2)-\zeta(3)).
\]
This establishes the stated Hilbert–Schmidt constant without extrapolating any finite computation.

## Verification
Run `python check_annulus.py` using Python 3's standard library. It checks the strict moment inequalities and exact finite-rational eigenvalue identities over selected integer parameters, compares finite partial traces with the telescoping trace, checks the nonasymptotic norm bound and pointwise continuum samples, and independently integrates the quadratic profile against its zeta expression. The output is `ANNULAR_BERGMAN_COMMUTATOR_DIAGNOSTIC_OK 779`. The finite checks only support algebra and normalization; all infinite claims, fixed-radius tails and limiting constants are proved analytically above.

## Relationship to prior work
Adhikari and Das (2026) characterize Toeplitz operators on annular **Hardy** space and discuss algebraic zero products, not this analytic Bergman annulus commutator's singular spectrum. Das and Narayanan (2025) analyze zero products on Hardy and Bergman annuli, not these pinching singular-value limits. Douglas and Kim (2009) analyze reducing subspaces of annular multiplication shifts, providing weighted-shift context but not the thin-annulus curvature profile. Previously published Hardy-annulus self-commutator results have a \(\operatorname{sech}^2\) spectral profile and all finite Schatten powers; the analytic **Bergman** area norm instead produces the new \(y^{-2}-\operatorname{csch}^2y\) profile, two \(j^{-2}\) tails, and the sharp cutoff \(p>1/2\). Standard weighted Bergman disk self-commutator results concern the simply connected disk, not the two-boundary pinching limit here. The novelty claim is the **combined complete thin-annulus profile and exact limiting constants**, not the elementary fact that multiplication by a monomial is a weighted shift.

## Limitations
The domain is a concentric circular annulus with **unweighted planar area**, and the multiplier is a fixed monomial of positive integer degree. Neither higher-order symbols nor simultaneous growth of degree and reciprocal thickness is treated. The spectral counting measure has infinite mass near zero, so only thresholds strictly above zero are asserted. An equivalent spectral asymptotic could be implicit in general weighted-shift or semiclassical results not identified in the inspected primary literature. No independent mathematical audit has been performed.

## References
1. S. Adhikari and S. Das, *Algebraic properties of Toeplitz operators on annulus and multiply connected domains*, arXiv:2611.01717v1 (first public 2026-11-01), https://arxiv.org/abs/2611.01717.
2. S. Das and E. K. Narayanan, *Zero Products of Toeplitz operators on the Hardy and Bergman spaces over an annulus*, arXiv:2504.04270, https://arxiv.org/abs/2504.04270.
3. R. G. Douglas and Y.-S. Kim, *Reducing Subspaces on the Annulus*, arXiv:0902.1794, https://arxiv.org/abs/0902.1794.
4. *Half-Schatten perimeter law and spectral Weyl profile for pinching annular Hardy multipliers*, published mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-schatten-perimeter-law-and-spectral-weyl-profile-for-pinchi--afd674958865.
5. *A universal spectral determinant for the Hardy-annulus coordinate commutator*, published mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-universal-spectral-determinant-for-the-hardy-annulus-coordinat--a4f1018e59c1.
