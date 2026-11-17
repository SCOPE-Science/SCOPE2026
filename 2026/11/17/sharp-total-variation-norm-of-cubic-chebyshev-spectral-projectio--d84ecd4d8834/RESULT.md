# Sharp total-variation norm of cubic Chebyshev spectral projection, with displaced extremizers

## Finding
Let \(\mathcal C_3\) be the \(L^2([-1,1],(1-x^2)^{-1/2}\,dx)\)-orthogonal projection onto real polynomials of degree at most three. Its sharp real bounded-variation seminorm is
\[
\|\mathcal C_3\|_{\mathrm{Var}\to\mathrm{Var}}
=\frac{8}{3\pi}\sqrt{1-u_*}\left(1+2u_*+\frac{(16u_*^2-11u_*+2)^{3/2}}{(4u_*-1)^2}\right)
=1.565342822371915\ldots,
\]
where \(u_*\) is the **unique** real root in \((4/9,1)\) of
\[
49152u^8-167936u^7+228352u^6-161536u^5+64448u^4-14464u^3+1676u^2-79u+1=0.
\]
It lies in \((692/1000,693/1000)\). Equality is attained by the single-jump functions \(\mathbf1_{[\sqrt{u_*},1]}\) and \(\mathbf1_{[-\sqrt{u_*},1]}\) (the symmetric jump positions). Neither worst jump is the midpoint. The same norm is the sharp two-input variation Lipschitz constant, by linearity.

## Assumptions and scope
Inputs are real pointwise functions of finite total variation on \([-1,1]\), considered modulo values at sets of Lebesgue measure zero for the projection. The domain seminorm is ordinary total variation on the interval; the polynomial output is measured in the same seminorm. This is **continuous weighted orthogonal projection**, not Chebyshev-node interpolation and not unweighted Legendre projection. No higher-degree assertion is made.

Write \(T_k(\cos\theta)=\cos(k\theta)\). Precisely,
\[
\mathcal C_3 f(x)=\frac1\pi\int_0^\pi f(\cos\theta)\,d\theta
+\frac2\pi\sum_{k=1}^3T_k(x)\int_0^\pi f(\cos\theta)\cos(k\theta)\,d\theta.
\]

## Proof
**1. Reduction to jumps.** Let \(f_t=\mathbf1_{[t,1]}\) for interior \(t\), and let \(\mu\) be the distributional derivative measure of a bounded-variation input. Up to an almost-everywhere constant, \(f(x)=\int f_t(x)\,d\mu(t)\). The projection reproduces constants, so differentiation, Fubini and the triangle inequality give
\[
\operatorname{Var}(\mathcal C_3f)\leq
\left(\sup_{-1<t<1}\operatorname{Var}(\mathcal C_3f_t)\right)|\mu|((-1,1))
\leq\left(\sup_t\operatorname{Var}(\mathcal C_3f_t)\right)\operatorname{Var}(f).
\]
Every \(f_t\) has unit variation, so this upper bound is sharp. This argument includes input jumps and singular-continuous derivatives; endpoint point-value changes can only increase the input seminorm, never the projection.

**2. Quadratic derivative.** Put \(t=\cos\phi\), \(c=\cos\phi\), \(u=c^2\). Since \(\int_0^\phi\cos(k\theta)\,d\theta=\sin(k\phi)/k\), differentiating the three Chebyshev terms gives
\[
(\mathcal C_3 f_t)'(x)=\frac{2\sqrt{1-c^2}}\pi Q_c(x),\qquad
Q_c(x)=(16c^2-4)x^2+4cx+2-4c^2.
\]
Consequently the variation of the jump response is \(2H(c)/\pi\), with
\[
H(c)=\sqrt{1-c^2}\int_{-1}^{1}|Q_c(x)|\,dx.
\]
Symmetry \(Q_{-c}(-x)=Q_c(x)\) makes \(H\) even.

**3. Analytic maximization for \(2/3\le c\le1\).** On this region the two roots of \(Q_c\) lie strictly within \((-1,1)\) whenever \(c<1\). This follows from positivity at both endpoints, a vertex in the interval, and the positive discriminant \(16(16u^2-11u+2)\). The signed integral is \(4(1+2u)/3\). Integrating the negative interval between the roots therefore gives
\[
H(c)=\frac43\sqrt{1-u}\left(1+2u+\frac{(16u^2-11u+2)^{3/2}}{(4u-1)^2}\right).
\]
Its derivative has the sign of
\[
E(u)=(1-2u)(4u-1)^3-\sqrt{16u^2-11u+2}\,(64u^3-80u^2+24u-1).
\]
Squaring the stationary identity \(E(u)=0\) yields exactly the octic in the Finding (with opposite overall sign). A rational Sturm sequence for that octic has sign-variation counts **3 at \(u=4/9\)** and **2 at \(u=1\)**, proving exactly one root in this range. At \(u=1/2\), \(E(u)=1/\sqrt2>0\); at \(u=1\), \(E(u)=-27-7\sqrt7<0\). Thus the unique root is the strict global maximum throughout this upper region. Sturm isolation gives \(692/1000<u_*<693/1000\).

**4. Certified exclusion of \(0\le c\le2/3\).** We verify the strict rational bound \(H(c)<49/20\) across this entire lower region, using an explicit exact-integer certificate (the accompanying `CHECK.py`). For \(c\) in this range, \(|16c^2-4|\le4\), \(|4c|\le8/3\), and \(|2-4c^2|\le2\), so \(\int|Q_c|\le52/3\). The derivative satisfies \(|\partial_cQ_c|\le92/3\) on \([-1,1]\), and \(|(\sqrt{1-c^2})'|<1\); hence \(|H'(c)|<80\). For any quadratic \(Q\), the composite midpoint approximation to \(\int_{-1}^1|Q|\) with \(M\) equal cells of length \(h=2/M\) has absolute error at most \(h^2(|A|/6+L/2)\), where \(A\) is the quadratic coefficient and \(L=2|A|+|B|\) is a Lipschitz bound; at most two cells contain roots. Here this error is at most \(24/M^2\).

Take \(M=128\), and take exactly the \(8001\) rational values \(c=k/12000\) for \(k=0,\dots,8000\). Midpoint values of \(Q_c\) are rational; all are summed in integers. The factor \(\sqrt{1-c^2}\) is rounded *upward* by an integer-square-root bound with denominator \(10^8\). Add \(24/128^2\) to the integral and \(40/12000\) for the distance to the nearest sampled \(c\). The exact rational maximum of all resulting upper enclosures is less than \(2.442589<49/20\); the maximal upper enclosure occurs at \(c=0\). There is no floating-point reliance in this exclusion.

Finally, the exact value at \(c=5/6\) is
\[
H(5/6)=\frac{\sqrt{11}\,[673\sqrt{673}+44032]}{82944}>\frac{49}{20}.
\]
The last inequality follows already from \(\sqrt{11}>3316/1000\) and \(\sqrt{673}>2594/100\), verified by squaring. Thus the lower region cannot contain a global maximizer, and the unique upper-region maximizer proves the claimed coefficient and its attaining jump locations.

## Verification
Run `python CHECK.py` (Python standard library only). It independently reconstructs the octic from the unsquared stationary equation, computes the exact rational Sturm sign variations and root bracket, checks every integer midpoint/upper-square-root enclosure, and establishes the rational gap witness. Its diagnostic decimal value is *not* part of the proof. The certificate prints `ALL_CERTIFICATES_PASS`. Each certificate is finite and exhaustive for the explicitly defined rational grid; the continuum extension is proved by the preceding analytic Lipschitz and root-count arguments.

## Relationship to prior work
Benoit, Joldes and Mezzarobba (2014), §2.1, define this weighted Chebyshev projection and analyze recurrence-based, validated uniform polynomial approximation for analytic D-finite functions. Their analysis does not imply a sharp total-variation norm or a discontinuous worst input. Wang (2021/2023) analyzes pointwise convergence/error localization for Chebyshev spectral projections and singular test functions, not the fixed-degree BV-to-BV operator norm. Akansha and Subramaniam (2024 preprint; 2025 article) prove coefficient-decay and \(L^1\) error estimates for quadrature-based Chebyshev approximations of BV functions, not this norm. The separately studied cubic **Legendre** projector uses a different weight and has a midpoint extremizer; that norm does not determine the Chebyshev value.

## Limitations
This is a fixed-degree, real-data, unweighted-output-variation result; it does not classify higher Chebyshev degrees, weighted variation seminorms, nor complex-valued total variation. The originality assessment is bounded by the inspected literature and indexed searches, not a proof that no historical source exists. An independent mathematical audit has not been performed.

## References
1. A. Benoit, M. Joldes and M. Mezzarobba, *Rigorous uniform approximation of D-finite functions using Chebyshev expansions*, arXiv:1407.2802, first posted 2014-07-10. https://arxiv.org/abs/1407.2802
2. H. Wang, *Analysis of error localization of Chebyshev spectral approximations*, arXiv:2106.03456, first posted 2021-06-07. https://arxiv.org/abs/2106.03456
3. S. Akansha and A. Subramaniam, *Exploring Chebyshev polynomial approximations: Error estimates for functions of bounded variation*, AIMS Mathematics 10 (2025), 8688–8706; earlier arXiv:2404.18723 (2024-04-29). https://www.aimspress.com/aimspress-data/math/2025/4/PDF/math-10-04-398.pdf
4. AMS, Mathematics Subject Classification 2020, 41A10 (approximation by polynomials). https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=41Axx
