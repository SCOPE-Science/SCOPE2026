# Directed cross-coordinate correlations in the three-dimensional heterochaos baker map

## Finding

Let \(F\) be the three-dimensional heterochaos baker map of Saiki, Takahasi and Yorke, equipped with normalized Lebesgue measure on \([0,1)^3\). Write \((X_n,Y_n,Z_n)=F^n(X_0,Y_0,Z_0)\), with a Lebesgue-distributed initial point. For every integer \(n\ge0\), define the forward directed covariance
\[
C_n=\operatorname{Cov}(Z_0,Y_n).
\]
Put \(R=3/(2\sqrt 2)\) and define the analytic function at the origin
\[
r(t)=\frac{3-\sqrt{9-8t^2}}{2t},\qquad r(0)=0,
\]
with the square root equal to \(3\) at the origin. The exact generating function is
\[
\boxed{\sum_{n\ge0}C_nt^n=\frac{t(2+r(t)^2)}{72(1-t/2)(4-r(t))}.}
\]
In contrast, \(\operatorname{Cov}(Y_0,Z_n)=0\) for every \(n\ge0\). In particular \(C_0=0\), while \(C_1=1/144\), \(C_2=1/216\), and all \(C_n>0\) for \(n\ge1\).

There are **two nonzero asymptotic amplitudes**. Define
\[
d_+=\frac{2\sqrt2}{(4-\sqrt2)^2},\quad
 d_-=\frac{2\sqrt2}{(4+\sqrt2)^2},\quad
 A_+=\frac{R d_+}{18(1-R/2)},\quad
 A_-=\frac{R d_-}{18(1+R/2)}.
\]
Then \(0<A_-<A_+\) and, as \(n\to\infty\) through all integers,
\[
\boxed{C_n=\frac{R^{-n}}{\sqrt\pi\,n^{3/2}}\left(A_+-(-1)^nA_-+O(n^{-1})\right).}
\]
Numerically, \(A_+\approx0.0530726413\) and \(A_-\approx0.0037152913\). Thus the correlation is directionally asymmetric, with an exponential scale \(2\sqrt2/3\), an inverse-three-halves correction and a genuine even/odd amplitude difference.

## Assumptions and scope

The map acts on the unit cube, outside the usual null boundary set, by
\[
F(x,y,z)=
\begin{cases}
(3x\bmod1,\;2y/3,\;z/2), & 0\le x<1/3\quad(A),\\
(3x\bmod1,\;2y/3,\;(1+z)/2), & 1/3\le x<2/3\quad(D),\\
(3x\bmod1,\;2/3+y/6,\;2z), & 2/3\le x<1,\;z<1/2\quad(B),\\
(3x\bmod1,\;5/6+y/6,\;2z-1), & 2/3\le x<1,\;z\ge1/2\quad(C).
\end{cases}
\]
All expectations are with respect to normalized three-dimensional Lebesgue measure. This measure is invariant: each branch has Jacobian determinant of modulus \(1\), and their images partition the cube modulo boundary sets. Hence the statement concerns stationary two-time correlations and ordinary forward iterates, not a random-map replacement or a nonstationary ensemble. The primary subject classification is MSC2020 37A25.

## Proof

**1. Independent driving digits and one-step conditional drift.** Under initial Lebesgue measure, the ternary digits driving the successive \(X\)-branches are independent and uniform on \(\{0,1,2\}\), independently of \((Y_0,Z_0)\). Branch \(0\) pushes binary digit \(0\) onto \(Z\), branch \(1\) pushes digit \(1\), and branch \(2\) deletes the leading binary digit. These choices are independent of the current \((Y,Z)\). For \(b_1(z)=\mathbf1_{[1/2,1)}(z)\), averaging the \(Y\)-update over the next ternary digit gives
\[
\mathbb E[Y_{n+1}-1/2\mid Y_n,Z_n]
=\frac12(Y_n-1/2)+\frac1{18}(b_1(Z_n)-1/2).
\]
Consequently, writing \(D_n=\mathbb E[(Z_0-1/2)(b_1(Z_n)-1/2)]\),
\[
C_0=0,\qquad C_{n+1}=\frac12 C_n+\frac1{18}D_n.
\]
The reverse covariance is identically zero because \(Z_n\) depends only on \(Z_0\) and the first \(n\) ternary digits, independently of \(Y_0\).

**2. Binary-digit resolvent.** For \(j\ge1\), let \(R_j(z)=2b_j(z)-1\), where \(b_j\) is binary digit \(j\). The annealed one-step Koopman operator \(P\), acting on functions of the \(Z\)-coordinate, satisfies the pointwise (outside dyadic boundaries) identities
\[
P R_1=\frac13R_2,\qquad
P R_j=\frac23R_{j-1}+\frac13R_{j+1}\quad(j\ge2).
\]
Since the digits of \(Z_0\) are independent fair bits,
\[
w_j=\mathbb E[(Z_0-1/2)R_j(Z_0)]=2^{-j-1}.
\]
Set \(h_j(t)=\sum_{n\ge0}t^n\mathbb E[(Z_0-1/2)R_j(Z_n)]\). For \(|t|<1\), the series are bounded uniformly in \(j\), and satisfy
\[
h_1=w_1+\frac t3h_2,\qquad
h_j=w_j+t\left(\frac23h_{j-1}+\frac13h_{j+1}\right)\ (j\ge2).
\]
The root of the homogeneous characteristic equation bounded at the origin is \(r(t)\), defined above, and the other root is unbounded as \(t\to0\). Solving the unique bounded sequence with boundary condition \(h_0=0\) yields
\[
h_j(t)=\frac{2^{-j-1}-r(t)^j/2}{1-3t/2}.
\]
The apparent singularity at \(t=2/3\) cancels. As \(D_n=\frac12\mathbb E[(Z_0-1/2)R_1(Z_n)]\), its generating function is
\[
\sum_{n\ge0}D_nt^n=\frac{h_1(t)}2
=\frac{1-2r(t)}{8(1-3t/2)}
=\frac{2+r(t)^2}{4(4-r(t))}.
\]
The last equality uses \(3r=t(r^2+2)\). Substitution into the one-step recurrence for \(C_n\) proves the exact generating function. Positivity follows without analytic continuation: \(P\) has nonnegative coefficients in the digit basis, \(w_j>0\), so \(D_n>0\) and then \(C_n>0\) for \(n\ge1\).

**3. Singularities and sharp asymptotics.** The analytic branch \(r(t)\) has radius \(R=3/(2\sqrt2)\) with its only singularities on that circle at \(t=\pm R\). Since the Taylor coefficients of \(r\) are nonnegative, \(|r(t)|\le r(R)=\sqrt2<4\) on \(|t|\le R\), and \(1-t/2\) has no zero there. Hence no other singularity competes with these two branch points. For \(u\downarrow0\),
\[
r(R(1-u))=\sqrt2-2\sqrt u+O(u),\qquad
r(-R(1-u))=-\sqrt2+2\sqrt u+O(u).
\]
Differentiating \(D(r)=(r^2+2)/(4(4-r))\) gives \(D'(\sqrt2)=d_+\) and \(D'(-\sqrt2)=-d_-\). Therefore the square-root terms in the two local expansions of the covariance generating function have coefficients \(-2A_+\) at \(+R\) and \(+2A_-\) at \(-R\). The standard coefficient estimate \([t^n](1-t/R)^{1/2}\sim-R^{-n}/(2\sqrt\pi n^{3/2})\), together with the next Puiseux term, yields the displayed all-integer asymptotic with its parity correction and relative \(O(n^{-1})\) remainder. Both amplitudes are strictly positive and distinct.

## Verification

Run `python verify.py` using only the Python standard library. The program independently integrates \(C_n\) over ternary-branch paths and dyadic cells using exact rational arithmetic for \(0\le n\le5\); compares operator recurrences and formal generating-function coefficients through degree \(16\); and checks the stated asymptotic for six larger sample lags. Its exact short-lag results begin \(0,1/144,1/216,7/1728,5/1944,131/62208\). The analytical steps above, not these finite experiments, prove the infinite claims.

## Relationship to prior work

Saiki, Takahasi and Yorke define the three-dimensional heterochaos baker map, establish its ergodicity and analyze heterogeneous periodic-point instability. Takahasi subsequently proves qualitative and exponential mixing for related heterochaos baker maps away from center neutrality. The present result is the exact *directed cross-coordinate* covariance for the original three-dimensional model, including its algebraic resolvent, backward-direction vanishing, leading constant and parity modulation. Generic mixing bounds, invariant-measure statements and periodic-fiber counts do not imply this observable-specific equality. The earlier exact center-coordinate autocovariance for a generalized two-dimensional model concerns different observables and does not specify a central-to-stable cross-correlation.

## Limitations

The formulas concern the original parameter-free three-dimensional map, Lebesgue-stationary initial data, and the two specified coordinate observables. They make no claim about arbitrary Hölder observables, arbitrary initial distributions, or sharp uniform mixing rates. Exact priority beyond the inspected primary papers and discoverable research results is not independently established; an unindexed equivalent computation remains possible. No independent mathematical audit has been performed.

## References

1. Y. Saiki, H. Takahasi and J. A. Yorke, *Piecewise linear maps with heterogeneous chaos*, arXiv:1811.01009 (first public version 2018-11-02); especially definition (1.2), the branch partition, and Theorem 1.2. https://arxiv.org/abs/1811.01009
2. H. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119 (first public version 2023-07-16); especially Theorems A–B and the treatment of correlation bounds. https://arxiv.org/abs/2307.08119
3. H. Takahasi and K. Yamamoto, *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for the breakdown of entropy approachability*, arXiv:2209.04905 (first public version 2022-09-11). https://arxiv.org/abs/2209.04905
