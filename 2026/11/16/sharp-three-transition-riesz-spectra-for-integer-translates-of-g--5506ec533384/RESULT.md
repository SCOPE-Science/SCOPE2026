# Sharp three-transition Riesz spectra for integer translates of Gaussian–first-Hermite mixtures

## Finding

For \(c\ge0\) define \(g_c(t)=(t+c)e^{-\pi t^2}\). The full family of integer translates is a Riesz sequence, and its optimal squared Riesz bounds have three exact transitions. For \(a=c^2\), put
\[
P_a(x)=\sum_{k\in\mathbb Z}\bigl((x+k)^2+a\bigr)e^{-2\pi(x+k)^2},\quad x\in\mathbb R.
\]
Write \(S_j(x)=\sum_{k\in\mathbb Z}(x+k)^j e^{-2\pi(x+k)^2}\), \(j=0,2\), and define
\[
R(x)=-\frac{S_2'(x)}{S_0'(x)},\quad 0<x<\tfrac12,
\quad a_-=\lim_{x\uparrow1/2}R(x),\quad a_+=\lim_{x\downarrow0}R(x),
\]
\[
a_* =\frac{S_2(1/2)-S_2(0)}{S_0(0)-S_0(1/2)}.
\]
These exact constants satisfy
\[
a_-\approx0.142534182823081,\quad a_*\approx0.170429503114442,\quad a_+\approx0.196497405926695.
\]
The function \(R\) is **strictly decreasing**, so \(a_-<a_*<a_+\). The exact optimal lower Riesz bound is
\[
A(c)=\begin{cases}P_a(0),&0\le a\le a_*;\\P_a(1/2),&a_*\le a<\infty.\end{cases}
\]
At \(a=a_*\), both frequencies are minimizing. The exact optimal upper Riesz bound is
\[
B(c)=\begin{cases}P_a(1/2),&0\le a\le a_-;\\P_a(x_a),&a_-<a<a_+;\\P_a(0),&a_+\le a<\infty,\end{cases}
\]
where the unique \(x_a\in(0,1/2)\) solves \(R(x_a)=a\). The only maximizing frequencies modulo one are \(1/2\), respectively \(x_a,1-x_a\), respectively \(0\). The minimizing frequencies are exactly \(0\) if \(a<a_*\), \(1/2\) if \(a>a_*\), and both at \(a=a_*\).

## Assumptions and scope

Use \(\widehat f(\xi)=\int_\mathbb R f(t)e^{-2\pi it\xi}\,dt\) and Lebesgue \(L^2\)-norms. The index set consists of all integers, \(c\) is real nonnegative, and Riesz constants are for finite coefficient sequences with optimal constants. Negative real \(c\) yields the same bounds by parity and translation reflection. The symbol is strictly positive at every real argument, including \(a=0\), because not all summands can vanish at once.

## Proof

**1. Gram diagonalization.** Direct Fourier transformation gives \(\widehat g_c(\xi)=(c-i\xi)e^{-\pi\xi^2}\), whence \(|\widehat g_c(\xi)|^2=(c^2+\xi^2)e^{-2\pi\xi^2}\). For any finitely supported complex sequence \((v_j)\), Plancherel and periodization give
\[
\left\|\sum_jv_jg_c(\cdot-j)\right\|_2^2
=\int_0^1P_a(x)\left|\sum_jv_je^{-2\pi ijx}\right|^2dx.
\]
Normalized Dirichlet/Fejér approximate identities demonstrate optimality of both essential spectral extrema; continuity makes them minima/maxima. Positivity and compactness yield positive Riesz bounds.

**2. Poisson reduction.** With \(q=e^{-\pi/2}\) and \(\theta=2\pi x\), Poisson summation yields
\[
S_0(x)=\frac1{\sqrt2}\left(1+2\sum_{n\ge1}q^{n^2}\cos(n\theta)\right),\qquad
S_2(x)=\frac1{4\pi}S_0(x)+\frac1{16\pi^2}S_0''(x).
\]
For \(z=\cos\theta\), define the uniformly and analytically convergent series
\[
H(z)=\sum_{n\ge1}nq^{n^2}U_{n-1}(z),
\]
where \(U_m\) is the Chebyshev polynomial of the second kind, with \(U_m(\cos\theta)=\sin((m+1)\theta)/\sin\theta\). Then
\[
S_0'(x)=-\frac{4\pi}{\sqrt2}\sin\theta\,H(z),\quad
R(x)=\frac14-\frac1{4\pi}+\frac14\frac{3zH'(z)-(1-z^2)H''(z)}{H(z)}.
\]

**3. Uniform strict monotonicity, not just numerical sampling.** For \(j=0,1,2,3\), the standard Chebyshev supremum estimate followed by Markov's polynomial inequality gives
\[
\left|\frac{d^j}{dz^j}U_{n-1}(z)\right|\le n(n-1)^{2j},\quad -1\le z\le1.
\]
Set \(T_j=\sum_{n\ge3}n^2(n-1)^{2j}q^{n^2}\). The elementary enclosure \(0.2078<q<0.208\), followed by bounding the \(n\ge4\) ratios by \((5/4)^2(4/3)^6(0.208)^9<10^{-5}\), yields
\[
T_0<0.000007,\quad T_1<0.000027,\quad T_2<0.00011,\quad T_3<0.00043.
\]
Indeed, an explicit upper bound for each \(T_j\) is \(9\,2^{2j}(0.208)^9 +16\,3^{2j}(0.208)^{16}/(1-10^{-5})\). Since \(H(z)=q+4q^4z+\text{tail}\), the bounds imply uniformly
\[
0.200<H(z)<0.216,\quad 0.0074<H'(z)<0.0076,\quad
|H''(z)|<0.00011,\quad |H'''(z)|<0.00043.
\]
For \(N(z)=3zH'(z)-(1-z^2)H''(z)\), the derivative of \(N/H\) has numerator
\[
\bigl(3H'+5zH''-(1-z^2)H'''\bigr)H
-\bigl(3zH'-(1-z^2)H''\bigr)H'.
\]
Its lower bound is strictly greater than
\[
(3(0.0074)-5(0.00011)-0.00043)(0.200)
-(3(0.0076)+0.00011)(0.0076)>0.004.
\]
Hence \(dR/dz>0\). Because \(z=\cos(2\pi x)\) strictly decreases on \((0,1/2)\), \(R\) strictly decreases with \(x\). Also \(H>0\) implies \(S_0'(x)<0\) on that interval.

**4. Precise frequency extrema and ordering.** Since
\[
P_a'(x)=S_0'(x)\bigl(a-R(x)\bigr),
\]
the symbol increases throughout \((0,1/2)\) when \(a\le a_-\), decreases throughout when \(a\ge a_+\), and for \(a_-<a<a_+\) has a unique strict interior maximum. Therefore its minimum is always an endpoint. Poisson summation gives the explicit exact value
\[
a_*=-\frac1{4\pi}+\frac14\frac{\sum_{n\ge1,\,n\text{ odd}}n^2q^{n^2}}{\sum_{n\ge1,\,n\text{ odd}}q^{n^2}}.
\]
The relation \(P_a(1/2)-P_a(0)=(S_0(0)-S_0(1/2))(a_*-a)\), with \(S_0(0)>S_0(1/2)\), specifies the lower-bound switch. Strict decrease of \(R\) makes \(a_*\) its strictly weighted average against \(-S_0'(x)\) on \((0,1/2)\), and therefore \(a_-<a_*<a_+\). Reflection and periodicity give all equality frequencies.

## Verification

The optional standalone file `CHECK.py` evaluates the two expressions for \(P_a\), numerically checks the three ordered thresholds and tests extremizing frequencies over representative parameters. Those finite numerical tests supplement the analytic proof above and do not establish monotonicity on their own. The exact tail-ratio inequality and differentiated theta identities are the critical infinite certificates. The bounds are optimal by Dirichlet/Fejér localization.

## Relationship to prior work

Lemvig's November 2026 paper *On the Gabor frame set of polynomial-Gaussian windows* studies full time–frequency Gabor frames for polynomial-Gaussian windows via Gramian and Wronskian techniques; it does not report these sharp integer-translation Riesz bounds or the three parameter thresholds in the inspected full text. Kiselev, Minin, Novikov, and Sitnik's work *On Evaluation of Riesz Constants for Systems of Shifted Gaussians* gives quantitative Riesz constants for pure Gaussian and Cauchy-type translates; it does not cover the first-Hermite mixture or its moving upper-bound spectral maximum. Existing indexed findings on half-density Hermite Gabor frame regularization and high-density Gabor frame conditioning concern distinct two-dimensional time-frequency sampling operators, not this one-dimensional shift Gram spectral extremization.

## Limitations

The theorem concerns unit-spaced translates of a fixed-width degree-one Gaussian polynomial with real parameter. It does not classify arbitrary translation spacings, higher polynomial degrees, nonreal parameters, or full Gabor frames. Possible equivalent earlier theta-function extremum theorems in older shift-invariant space literature remain an originality risk. All review herein is same-model; no independent mathematical audit has been performed.

## References

1. J. Lemvig, *On the Gabor frame set of polynomial-Gaussian windows*, first public arXiv version November 3, 2026, https://arxiv.org/abs/2611.05337.
2. Kiselev, Minin, Novikov, and Sitnik, *On Evaluation of Riesz Constants for Systems of Shifted Gaussians*, original arXiv manuscript 2013, https://arxiv.org/abs/1308.2649.
