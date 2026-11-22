# Exact periodic census and geometric memory in a four-term Rényi–remainder map

## Finding

For the explicitly published three-remainder Rényi map at integer seed gain one, a hidden expanding-circle factor determines **all** invariant probabilities and periodic points. On the state interval \(X=[0,4)\), put
\[
H(x)=\{x\}+\{10x\}+\{100x\}+\{1000x\},\qquad \{t\}=t-\lfloor t\rfloor.
\]
Then \(H:X\to X\) has exactly \(1111^n-1\) points fixed by its \(n\)-th iterate for every \(n\ge1\), and its Artin–Mazur zeta function is
\[
\zeta_H(z)=\frac{1-z}{1-1111z}.
\]
The unique absolutely continuous invariant probability \(\mu\) is exact (hence mixing), has metric entropy \(\log1111\), and is physical for Lebesgue-almost every initial point. It has mean \(2\), variance \(2321/6000\), and the complete stationary coordinate autocovariance law
\[
\operatorname{Cov}_{\mu}(X_0,X_h)=\frac{2321}{6000}\,1111^{-h}\qquad(h=0,1,2,\ldots).
\]
Consequently, its normalized coordinate autocorrelation is exactly \(1111^{-h}\), despite its nonuniform stationary density. Its centered spectral density, in the normalization \(S(\theta)=\sum_{h\in\mathbb Z}\operatorname{Cov}(X_0,X_h)e^{-ih\theta}\), is
\[
S(\theta)=\frac{2321}{6000}\frac{1-1111^{-2}}{1-2\cdot1111^{-1}\cos\theta+1111^{-2}}.
\]
More strongly, reduction modulo one gives an affine bijection between *all* invariant Borel probability measures of \(H\) and those of multiplication by \(1111\) modulo one, preserving ergodicity and measure-theoretic entropy.

## Assumptions and scope

The braces above mean fractional part in \([0,1)\), including at discontinuities. The underlying map is Equation (29) of Moysis, Lawnik, Antoniades, Kafetzis, Baptista and Volos (2023) with their three remainder gains \(10,100,1000\), remainder moduli all equal to one, and Rényi seed gain \(k=1\). On nonnegative arguments the signed remainder used there agrees with fractional part. This is an exact real-arithmetic dynamical result; floating-point implementations may differ at discontinuities. The original article analyzes other gains numerically. No security claim is made.

Write \(Y=[0,1)\), \(\pi:X\to Y\), \(\pi(x)=\{x\}\), and \(G:Y\to Y\), \(G(t)=\{1111t\}\). We use invariant Borel probabilities on these half-open standard Borel spaces, with entropy in the measure-theoretic sense, not a topological-entropy assertion for a discontinuous map.

## Proof

**1. The exact factor and finite-time identity.** Because all four coefficients of \(H\) are integers, \(H(x+1)=H(x)\). Furthermore, summing integer multiples before taking fractional part gives
\[
H=H\circ\pi,\qquad \pi\circ H=G,\qquad H\circ G=H^2\ \text{on }Y,
\]
and in particular
\[
H^{\circ n}(x)=H\!\left(G^{\circ(n-1)}(\pi x)\right)\qquad(n\ge1).
\]
These identities include all rational discontinuity points under the stated half-open convention.

**2. Invariant measures and entropy.** For any \(G\)-invariant probability \(\nu\), the pushforward \(\mu_\nu=H_*\nu\) is \(H\)-invariant because \(H\circ G=H\circ H\) on \(Y\). Moreover \(\pi_*\mu_\nu=G_*\nu=\nu\). Conversely any \(H\)-invariant probability \(\mu\) satisfies \(\mu=H_*\pi_*\mu\), with \(\pi_*\mu\) invariant under \(G\). Therefore \(\nu\mapsto H_*\nu\) and \(\mu\mapsto\pi_*\mu\) are mutually inverse on invariant measures. The two maps are mutual *measure-theoretic factors* via \(H\) and \(\pi\), hence have equal Kolmogorov–Sinai entropy on corresponding measures and corresponding ergodicity. In particular \(\mu=H_*m\), with \(m\) uniform on \(Y\), is invariant with entropy \(\log1111\). The integer Bernoulli map \(G\) has unique absolutely continuous invariant probability \(m\) and is exact. Since every absolutely continuous invariant \(H\)-measure projects to an absolutely continuous \(G\)-measure, \(\mu\) is the unique absolutely continuous invariant measure; since it is a factor of \(G\), it too is exact. For Lebesgue-almost every \(x\in X\), \(\pi x\) is \(G\)-generic, and the finite-time formula, followed by the bounded piecewise-affine observation \(H\), gives physicality.

**3. Periodic orbit bijection.** For every \(n\ge1\), \(\pi\) sends \(\operatorname{Fix}(H^{\circ n})\) bijectively to \(\operatorname{Fix}(G^{\circ n})\); its inverse sends a \(G\)-periodic point \(t\) to \(H(G^{\circ(n-1)}t)\). The second identity in Step 1 proves both assertions and the absence of extra lifts. Since the fixed points of \(G^n\) on \([0,1)\) are exactly \(j/(1111^n-1)\), with integers \(0\le j<1111^n-1\), there are \(1111^n-1\). Exponentiating the resulting series \(\sum_{n\ge1}(1111^n-1)z^n/n\) gives the stated zeta function. No finite enumeration is used as proof of the all-period count.

**4. Explicit stationary density.** In each interval \(J_j=[j/1000,(j+1)/1000)\), \(0\le j<1000\), the map \(H\) is affine with slope \(1111\):
\[
H(t)=1111t-c_j,\qquad c_j=j+\lfloor j/10\rfloor+\lfloor j/100\rfloor.
\]
Thus the density of \(\mu=H_*m\), at almost every \(y\), is the explicit rational step function
\[
h(y)=\frac1{1111}\sum_{j=0}^{999}\mathbf1_{[1111j/1000-c_j,\;1111(j+1)/1000-c_j)}(y).
\]
It is normalized automatically by change of variables. This is not a uniform distribution on \([0,4)\). Uniform grids of all \(G^n\)-fixed points push forward under \(H\) to uniform grids of all \(H^n\)-fixed points, because multiplication by \(1111^{n-1}\) permutes the nonnegative residues modulo \(1111^n-1\). Since the total variation of \(H\) on \([0,1)\), with the left-limit convention at one, is \(1111+9+99+999=2218\), one-dimensional bounded-variation quadrature gives, for each \(n\ge1\),
\[
W_1(\operatorname{unifFix}(H^{\circ n}),\mu)\le\frac{2218}{1111^n-1}.
\]

**5. Exact all-lag statistics.** The fractional part \(\{aU\}\) has mean \(1/2\) for any positive integer \(a\) and uniform \(U\) on \([0,1)\). For positive integers \(a,b\), direct Fourier expansion of the centered sawtooth, or integration over the common rational partition, gives
\[
\int_0^1(\{at\}-\tfrac12)(\{bt\}-\tfrac12)\,dt
=\frac{\gcd(a,b)^2}{12ab}.
\]
For clarity, the only common nonzero Fourier frequencies are integer multiples of \(\operatorname{lcm}(a,b)\); the remaining sum is \(\sum_{\ell\ge1}\ell^{-2}=\pi^2/6\). With \(a_i=10^i\), \(0\le i\le3\), this yields
\[
\operatorname{Var}_m(H(U))=\frac1{12}\sum_{i,j=0}^3 10^{-|i-j|}=\frac{2321}{6000}.
\]
The stationary process \((X_h)\) is a factor of \(U,GU,G^2U,\ldots\) via \(X_h=H(G^h U)\). Since \(\gcd(1111,10)=1\),
\[
\gcd(10^i,1111^h10^j)=10^{\min(i,j)}\qquad(i,j\in\{0,1,2,3\},\ h\ge0).
\]
Applying the sawtooth identity term by term proves the all-lag covariance formula. The absolutely summable geometric covariance series gives the displayed spectral density.

## Verification

Run \(\texttt{python3 check.py}\) with Python 3 and no third-party dependencies. It verifies the moment integrals independently by exactly integrating all \(1000\) affine cells using rational arithmetic; checks six independently integrated fractional-part covariance pairs; verifies seven lags of the arithmetic all-lag formula; and checks \(2095\) exact rational periodic lifts, including complete periods one to three for smaller gain vectors. The script prints the exact mean, variance and lag-one covariance. The infinite-period, all-lag, entropy and exactness statements follow from Steps 1–5, not from these finite checks.

## Relationship to prior work

The originating 2023 paper introduces the multi-remainder construction, states the concrete three-remainder Rényi formula, and investigates Lyapunov exponents and numerical phase diagrams. The 2022 single-remainder precursor derives derivative-based instability conditions, without the present all-period census or the physical all-lag covariance law. The classical integer circle map and the standard Fourier sawtooth identity are explicitly used as tools; they are not claimed as new. The contribution is the arithmetic identification of the published four-term system and the resulting complete dynamical-statistical package, including its nonuniform physical marginal, measure correspondence and exact spectral memory.

## Limitations

The conclusions require exact real arithmetic, the literal positive-integer gains \(1,10,100,1000\) and the naturally invariant half-open domain \([0,4)\). They do not assert the same formulas for noninteger gain, negative arguments where signed remainder may differ, finite-precision hardware or arbitrary nonlinear seed maps. The proof uses known properties of expanding integer circle maps and Fourier sawtooth series. Priority relative to unindexed arithmetic-dynamical literature requires independent assessment. The result is not a cryptographic-security guarantee.

## References

1. L. Moysis, M. Lawnik, I. P. Antoniades, I. Kafetzis, M. S. Baptista, and C. Volos, *Chaotification of 1D Maps by Multiple Remainder Operator Additions—Application to B-Spline Curve Encryption*, Symmetry **15** (2023), 726, DOI: 10.3390/sym15030726, first published 2023-03-14. Equations (27)–(29) and Section 3.4.
2. L. Moysis, I. Kafetzis, M. S. Baptista, and C. Volos, *Chaotification of One-Dimensional Maps Based on Remainder Operator Addition*, Mathematics **10** (2022), 2801, DOI: 10.3390/math10152801, first published 2022-08-07. Sections 2, 3 and 4.5.
3. Standard identities for the multiplication map on the circle and Fourier expansion of the centered sawtooth are proved or explicitly reduced above; no unexamined external theorem concerning the specific map is assumed.
