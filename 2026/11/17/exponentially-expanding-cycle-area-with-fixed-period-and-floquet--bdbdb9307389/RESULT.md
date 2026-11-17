# Exponentially expanding cycle area with fixed period and Floquet multiplier in a cubic star-node flow

## Finding

For any fixed \(\lambda,a,\omega>0\) and **every** real anisotropy \(\varepsilon\), the explicit cubic polynomial flow below has a unique periodic orbit in the punctured plane, attracting every nonzero trajectory. Its original-time period and transverse Floquet multiplier are independent of \(\varepsilon\), but the Euclidean area \(\mathcal A(\varepsilon)\) enclosed by its orbit is a strictly increasing function of \(|\varepsilon|\), with sharp exponential growth. In particular, arbitrarily large cycle areas coexist with one unchanged physical period and one unchanged transverse multiplier within a fixed-degree polynomial family.

Put \(A=a/\omega\), \(B=|\varepsilon|/\omega\), and let \(I_0\) be the modified Bessel function. The exact law, convergent power series, and asymptotic are

\[
\begin{aligned}
T_\varepsilon&=\frac{2\pi a}{\lambda\omega},\qquad
\mu_\varepsilon=e^{-4\pi a/\omega},\\
\mathcal A(\varepsilon)
&=\frac{\pi\lambda}{\omega}\int_0^\infty e^{-At}I_0\!\left(2B\sin\frac t2\right)\,dt\\
&=\frac{\pi\lambda}{a}\sum_{n=0}^\infty
\frac{\binom{2n}{n}}{4^n\prod_{k=1}^{n}(A^2+k^2)}B^{2n},\\
\mathcal A(\varepsilon)&\sim
\frac{\pi\lambda}{2|\varepsilon|\sinh(\pi a/\omega)}
\exp\left(\frac{2|\varepsilon|}{\omega}\right)
\quad (|\varepsilon|\to\infty).
\end{aligned}
\]

The empty product is one. In particular, \(\mathcal A(0)=\pi\lambda/a\), with strict inequality \(\mathcal A(\varepsilon)>\mathcal A(0)\) for \(\varepsilon\ne0\). The cycles remain well defined when \(|\varepsilon|\ge a\), where the cubic homogeneous term is no longer everywhere radially contracting.

## Assumptions and scope

Let \(\lambda,a,\omega\) be arbitrary fixed positive real numbers and \(\varepsilon\) any real number. The original-time polynomial differential equation is

\[
\begin{aligned}
\dot x &= \lambda x-[a(x^2+y^2)+\varepsilon(x^2-y^2)]x-\omega(x^2+y^2)y,\\
\dot y &= \lambda y-[a(x^2+y^2)+\varepsilon(x^2-y^2)]y+\omega(x^2+y^2)x.
\end{aligned}
\]

An attracting limit cycle means a simple, isolated periodic orbit and attraction of the orbit as a set; it does not assert synchronization of absolute phases. Euclidean enclosed area is the ordinary Lebesgue measure of the bounded Jordan component. No parameter-dependent change of the original time variable occurs in the claims for period or multiplier. The primary MSC2020 classification is 34C05.

## Proof

**Exact linear radial-power equation.** Put \(x=r\cos\theta\), \(y=r\sin\theta\) for \(r>0\). Then

\[
\dot r=\lambda r-(a+\varepsilon\cos2\theta)r^3,
\qquad \dot\theta=\omega r^2>0.
\]

With \(u=2\theta\) and \(v=r^2\), differentiation in the direction of positive angular motion gives

\[
\frac{dv}{du}=\frac{\lambda}{\omega}
-\frac{a+\varepsilon\cos u}{\omega}v.
\tag{1}
\]

The coefficient has positive mean \(A=a/\omega\), although it may be negative at individual angles. The unique periodic solution of (1) is

\[
V_\varepsilon(u)=\frac{\lambda}{\omega}
\int_0^\infty\exp\!\left[-At-
\frac{\varepsilon}{\omega}\bigl(\sin u-\sin(u-t)\bigr)\right]dt.
\tag{2}
\]

The integral is absolutely convergent, strictly positive, smooth, and \(2\pi\)-periodic. Direct differentiation under the integral proves (1), and its boundedness and positivity on the compact angular circle are immediate. Differences of arbitrary solutions of (1) obey

\[
 v(u)-V_\varepsilon(u)=[v(u_0)-V_\varepsilon(u_0)]
 \exp\!\left[-A(u-u_0)-\frac{\varepsilon}{\omega}(\sin u-\sin u_0)\right].
\tag{3}
\]

Every initially positive solution stays positive for every forward angle because variation of constants has a positive forcing integral. On \(u\ge u_0\), its value stays bounded above, and, after a finite angular interval, it has a positive lower bound. Since \(dt/du=1/(2\omega v(u))\), angular motion corresponds to forward-complete original physical time. No other nonzero equilibria exist because \(\dot\theta>0\). Formula (3) shows convergence of every positive-radius orbit to the periodic graph and ensures uniqueness of any periodic graph. The plane orbit has least angular period \(2\pi\) in \(\theta\), hence it is a simple, isolated attracting limit cycle. The origin is an unstable node.

**Floquet and physical-time rigidity.** One complete spatial turn corresponds to \(u\) increasing by \(4\pi\). The exact radial-power Poincaré derivative obtained from (3) is \(\exp(-4\pi A)\), which equals the sole nontrivial Floquet multiplier, unaffected by using \(v=r^2\) as a smooth local transverse coordinate at the cycle. To compute the true physical period, integrate \(d\log r/d\theta\) over the limit cycle:

\[
0=\lambda\int_0^{2\pi}\frac{d\theta}{\omega r^2}
-\frac1\omega\int_0^{2\pi}(a+\varepsilon\cos2\theta)d\theta
=\lambda T_\varepsilon-\frac{2\pi a}{\omega}.
\]

This gives the displayed period without any rescaling of physical time.

**Exact area formula.** By the polar area formula and the fact that \(V_\varepsilon\) is \(2\pi\)-periodic in \(u\),

\[
\mathcal A(\varepsilon)
=\frac12\int_0^{2\pi}V_\varepsilon(2\theta)d\theta
=\frac12\int_0^{2\pi}V_\varepsilon(u)du.
\]

Inserting (2), the trigonometric identity
\(\sin u-\sin(u-t)=2\sin(t/2)\cos(u-t/2)\), and the definition
\(I_0(s)=(2\pi)^{-1}\int_0^{2\pi}e^{s\cos u}du\), proves the exact positive Bessel integral in the Finding. Since \(I_0\) is even, the area depends only on \(|\varepsilon|\).

Expand \(I_0(2B\sin(t/2))=\sum_{n\ge0}B^{2n}\sin^{2n}(t/2)/(n!)^2\). Nonnegativity permits termwise integration by monotone convergence. Elementary Fourier expansion or a beta-function recurrence gives

\[
\int_0^\infty e^{-At}\sin^{2n}(t/2)dt
=\frac{(2n)!}{4^n A\prod_{k=1}^{n}(A^2+k^2)}.
\]

This proves the series. Every coefficient after the constant term is strictly positive, implying strict monotonicity in \(|\varepsilon|>0\). The ratio test shows the series is entire in \(\varepsilon\), and its first correction is

\[
\mathcal A(\varepsilon)=\frac{\pi\lambda}{a}
\left(1+\frac{\varepsilon^2}{2(a^2+\omega^2)}+O(\varepsilon^4)\right).
\]

**Sharp high-anisotropy area.** The even periodicity of \(I_0\) allows one to write

\[
\int_0^\infty e^{-At}I_0(2B\sin(t/2))dt
=\frac{\int_0^{2\pi}e^{-At}I_0(2B\sin(t/2))dt}{1-e^{-2\pi A}}.
\]

For \(B\to\infty\), the integrand in the finite interval has one dominant interior peak at \(t=\pi\). The standard integral-definition asymptotic \(I_0(z)\sim e^z/\sqrt{2\pi z}\) and the Taylor expansion \(\sin((\pi+s)/2)=1-s^2/8+O(s^4)\) show by Laplace's method that the numerator is

\[
 e^{-\pi A}\frac{e^{2B}}{B}(1+o(1)).
\]

For completeness, on the scale \(t=\pi+w/\sqrt B\), the Bessel factor is \(e^{2B-w^2/4}/\sqrt{4\pi B}\) to leading order, and the Gaussian integral \(\int_{\mathbb R}e^{-w^2/4}dw=2\sqrt\pi\) gives the exact coefficient \(1/B\). Outside any fixed neighborhood of \(\pi\), the exponential rate is strictly below \(2B\), providing domination for the usual Laplace truncation. Since \(e^{-\pi A}/(1-e^{-2\pi A})=[2\sinh(\pi A)]^{-1}\), substitution of \(B=|\varepsilon|/\omega\) yields the stated sharp asymptotic.

## Verification

Run the standalone Python file `check.py` with `python3 check.py`. It independently evolves (1) using fourth-order Runge–Kutta at several values including \(|\varepsilon|>a\), computes original-time period and enclosed area from that graph, and compares with the exact series; the expected success message is `CUBIC_ALL_ANISOTROPY_AREA_IDENTITIES_OK`. These finite numerical tests do not establish the theorem. The analytical proof above establishes all parameter quantifiers and the asymptotic; the numerical check tests representative points only.

## Relationship to prior work

Bendjeddou, Llibre and Salhi (2013), Theorems 1–2, prove general star-node integrability and limit-cycle existence/uniqueness criteria without requiring pointwise radial contraction. Their proof also introduces the linear radial-power angular equation; thus the general angular reduction, the existence of a cycle in the noncontracting parameter region, and its uniqueness are **not claimed as original discoveries here**. Alarcón, Castro and Labouriau (arXiv:2307.16020, first public 2023-07-29; journal 2024) classify the strictly contracting homogeneous class and provide the motivating geometry.

A published published-finding corpus finding, *Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles* (2026-10-11, identifier ending `7c00337eaa41`), already proves the affine radial-power return, the physical-time period and Floquet multiplier, and specifically exhibits the same noncircular cubic subfamily for \(|\varepsilon|<a\). Those identities are explicitly prior work. The additional statement here is the full exact **enclosed Euclidean area law**, its positive-coefficient rigidity, and its sharp exponentially expanding high-anisotropy limit, which lives outside the strict contraction assumptions. The 2013 general quadratures make this computation accessible in principle; none of these sources' inspected full texts gives the Bessel area law or its sharp exponential coefficient.

## Limitations

The theorem concerns this explicit cubic family, with \(\lambda,a,\omega>0\), not arbitrary homogeneous nonlinearities. It does not assert a universal area law for other star-node systems, a general optimal area bound, or an independent priority certification. A future discovery of an equivalent computation in other literature could affect originality. Period and Floquet rigidity themselves are old; the novel mathematical content is the global area law, its monotonicity and its noncontracting asymptotic. All statements refer to exact continuous dynamics, not a numerical integrator.

## References

1. B. Alarcón, S. B. S. D. Castro and I. S. Labouriau, *Global planar dynamics with a star node and contracting nonlinearity*, arXiv:2307.16020v1 (first public 29 July 2023), *Research in the Mathematical Sciences* 11, 21 (2024), DOI:10.1007/s40687-024-00427-0. Full HTML: https://link.springer.com/article/10.1007/s40687-024-00427-0.
2. A. Bendjeddou, J. Llibre and T. Salhi, *Dynamics of the polynomial differential systems with homogeneous nonlinearities and a star node*, *Journal of Differential Equations* 254 (2013), 3530–3537, DOI:10.1016/j.jde.2013.01.032. Author preprint: https://ddd.uab.cat/pub/artpub/2013/gsduab_3507/BenLliSal2013_Preprint.pdf.
3. B. Alarcón, S. B. S. D. Castro and I. S. Labouriau, *Global planar dynamics with star nodes: beyond Hilbert's 16th problem*, arXiv:2106.07516v1 (14 June 2021); full-text qualitative classification.
4. *Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles*, published-finding corpus (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-angular-return-and-physical-time-floquet-rigidity-for-cont--7c00337eaa41.
