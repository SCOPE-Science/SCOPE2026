# Strict dimensional convexity of logarithmic Brownian-hull absorption time

## Finding

Let \(B^{(d)}\) be standard Brownian motion in \(\mathbb R^d\) starting at the origin, and let \(\tau_d\) be the first time its path's closed convex hull contains \(e_1\). For every integer \(d\ge1\), the finite logarithmic mean \(M_d=\mathbb E\log\tau_d\) obeys the exact identity

\[
M_d=2d-1-\log 2-\psi(d/2)-\sum_{n=1}^{\infty}\frac{1}{n(n+1)(2n+1)^{d-1}},
\]

where \(\psi\) is the digamma function. In particular, writing \(\Delta_d=M_{d+1}-M_d\),

\[
0<\Delta_d<\Delta_{d+1}<2\quad(d\ge1),\qquad \lim_{d\to\infty}\Delta_d=2.
\]

Thus the mean logarithmic absorption time is strictly increasing and **strictly convex in the ambient dimension**, with strictly increasing dimensional increments. More precisely,

\[
M_d=2d-\log d-1+\frac1d+O(d^{-2}),\qquad
\sum_{n\ge1}\frac{1}{n(n+1)(2n+1)^{d-1}}=\frac{1}{2\,3^{d-1}}+O(5^{1-d}).
\]

The asymptotic estimates are as \(d\to\infty\) through integers. The exact finite-dimensional assertions do not require any limiting dimension.

## Assumptions and scope

The Brownian coordinates are independent standard variance-\(t\) processes; \(e_1=(1,0,\ldots,0)\). The hitting time is

\[
\tau_d=\inf\{t\ge0:e_1\in\operatorname{conv}\{B^{(d)}(s):0\le s\le t\}\}.
\]

This normalization matters: a global time-rescaling shifts every \(M_d\) by the same constant without changing the dimensional differences. Existence of positive and negative Mellin moments in a neighborhood of the origin is supplied by the previously proved Mellin formula cited below; this guarantees \(\mathbb E|\log\tau_d|<\infty\). All statements concern first **point absorption**, not the volume or diameter of the random hull.

## Proof

**1. Extract an exact logarithmic moment.** Kabluchko's dimension-generating Mellin identity (Theorem 1.8, equation (49) of [1]) states, for \(0<\Re s<1/2\) initially and by analytic continuation near \(s=0\) coefficientwise,

\[
\sum_{d\ge1}\frac{2^s\Gamma(d/2+s)}{\Gamma(d/2)}\mathbb E[\tau_d^s]w^{d-1}
=\frac{1+w\,\frac{\Gamma(1+s)}{\Gamma(1-s)}\frac{\Gamma((1-2s-w)/2)}{\Gamma((1+2s-w)/2)}}{(1-w^2)\cos(\pi s)}.
\]

Differentiate at \(s=0\). The logarithmic derivative on the left is \(M_d+\log2+\psi(d/2)\), while on the right it is

\[
F(w)=\frac{w[-2\gamma-2\psi((1-w)/2)]}{1-w^2}.
\]

The digamma partial-fraction expansion \(\psi(z)=-\gamma+\sum_{j\ge0}[(j+1)^{-1}-(j+z)^{-1}]\), followed by cancelling the removable singularity at \(w=-1\), gives, for \(|w|<1\),

\[
F(w)=\frac{2}{(1-w)^2}-\frac1{1-w}-\sum_{n=1}^{\infty}\frac{1}{n(n+1)(1-w/(2n+1))}.
\]

The series is locally uniformly absolutely convergent on \(|w|<1\). Its coefficient of \(w^{d-1}\) is \(2d-1-S_d\), where

\[
S_d=\sum_{n\ge1}\frac{(2n+1)^{1-d}}{n(n+1)}.
\]

Comparison of Taylor coefficients proves the exact formula. In particular \(0<S_d\le1\).

**2. Curvature in dimension.** Put \(C_d=M_{d+2}-2M_{d+1}+M_d\). The elementary integral for the difference of digammas yields

\[
C_d=2\int_0^1u^{d-1}\frac{1-u}{1+u}\,du
-\sum_{n\ge1}\frac{(2n+1)^{1-d}}{n(n+1)}\left(1-\frac1{2n+1}\right)^2.
\]

For every \(d\ge3\), the first term is at least

\[
2\int_0^1u^{d-1}(1-u)^2\,du=\frac{4}{d(d+1)(d+2)},
\]

using \((1+u)^{-1}\ge1-u\) on \([0,1]\). Separating \(n=1\) and bounding the remainder of the second term using \(\sum_{n\ge2}1/[n(n+1)]=1/2\), its magnitude is at most

\[
\frac29\,3^{1-d}+\frac12\,5^{1-d}.
\]

At \(d=3\), this is \(2/81+1/50<1/15\), below the lower bound \(4/(3\cdot4\cdot5)\). At each subsequent integer \(d\), the upper bound shrinks by a factor at most \(1/3\), whereas the lower bound shrinks by \(d/(d+3)\ge1/2\). Thus \(C_d>0\) for all \(d\ge3\).

The two remaining curvatures are exact:

\[
C_1=\frac{\pi^2}{2}-2-4\log2>0,\qquad
C_2=4\log2+\frac72\zeta(3)+3-\pi^2>0.
\]

The first is positive from \(\pi>3.14\), \(\log2<0.7\); the second from \(\pi<22/7\), \(\log2>0.69\), and \(\zeta(3)>6/5\) (the last follows from the first sixteen positive terms). Therefore \(C_d>0\) for **all** \(d\ge1\).

**3. Increment bounds.** Direct evaluation gives \(M_1=\gamma+\log2\) and \(M_2=\gamma+3\log2\), so \(\Delta_1=2\log2>0\). Strict positivity of all \(C_d\) implies every later increment is positive and strictly increasing. On the other hand,

\[
\Delta_d=2-[\psi((d+1)/2)-\psi(d/2)]+(S_d-S_{d+1}).
\]

The integral representation \(\psi(x+1/2)-\psi(x)=\int_0^\infty e^{-xt}/(1+e^{-t/2})\,dt\) gives \(\psi((d+1)/2)-\psi(d/2)>1/d\). For \(d\ge2\), \(0<S_d-S_{d+1}<S_d\le 3^{1-d}\le1/d\); hence \(\Delta_d<2\). The same bound for \(d=1\) follows from \(2\log2<2\). Finally the digamma difference and the series difference both tend to zero, showing \(\Delta_d\to2\).

**4. Asymptotic refinement.** The standard expansion \(\psi(d/2)=\log(d/2)-1/d+O(d^{-2})\) proves the displayed polynomial expansion. The first summand of \(S_d\) equals \(3^{1-d}/2\); bounding all later summands by \(5^{1-d}\sum_{n\ge2}1/[n(n+1)]=5^{1-d}/2\) gives the exponential remainder.

## Verification

The companion standalone `verify.py` computes Taylor coefficients of the independently evaluated digamma generating function at 70-digit precision, evaluates \(S_d\) by convergent numerical sums, checks the low-dimensional closed forms and exact rational majorants, and tests finite-dimensional curvature, increments, and bounds for \(1\le d\le30\). Its reproducible execution reports **221 passed checks**. These are diagnostic checks only; the inequalities and all-dimensional statements are proved above without numerical extrapolation. Run with `python verify.py`, requiring the `mpmath` Python package.

## Relationship to prior work

[1] proves the exact dimension-generating Mellin transform and a Gaussian high-dimensional limit for logarithmic absorption time. That transform is explicitly used above, not claimed as new. The new contribution is the extracted summable log-mean representation together with **strict convexity of the log mean for every integer dimension**, global bounds and the exact monotone approach of its increments to \(2\), via a nontrivial sign comparison between a digamma integral and a geometric series.

[2] concerns inverse intrinsic-volume, circumradius and diameter processes of high-dimensional Brownian convex hulls, rather than first absorption of an exterior point. Although both works involve Brownian hulls, [2] does not supply the point-absorption Mellin identity or the convexity assertion. The present proof draws no implication from its inverse-functional bounds.

## Limitations

The expectation of \(\tau_d\) itself is infinite, so this theorem is specifically about the **logarithmic** mean. It concerns standard Brownian motion, a fixed point of Euclidean norm one, and consecutive integer dimensions; no pathwise coupling order, stochastic order between full hitting-time distributions, or arbitrary drift claim is proved. The central moment identity is from [1]; the theorem is not an independent rederivation of that identity. Historical priority of the strict convexity inequality has not been independently certified, and similar inequalities could be implicit in less visible literature. Finite numerical checks are not substitutes for the analytical proof. Independent mathematical review has not been performed.

## References

[1] Z. Kabluchko, *Absorption Probabilities for Brownian Convex Hulls in Arbitrary Dimension*, arXiv:2611.00381 (first posted 2026-10-30), Theorem 1.8, equation (49), and its proof: https://arxiv.org/abs/2611.00381 .

[2] H. Panzo and E. Socher, *Bounds on some geometric functionals of high dimensional Brownian convex hulls and their inverse processes*, arXiv:2407.08712: https://arxiv.org/abs/2407.08712 .
