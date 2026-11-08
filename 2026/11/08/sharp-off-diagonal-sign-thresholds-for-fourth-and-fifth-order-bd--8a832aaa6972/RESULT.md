# Sharp off-diagonal sign thresholds for fourth- and fifth-order BDF convolution kernels

## Finding

For an integer \(k\in\{4,5,6\}\), let
\[
\delta_k(z)=\sum_{j=1}^{k}\frac{(1-z)^j}{j},\qquad
\delta_k(z)^\alpha=\sum_{n=0}^{\infty}\omega_n^{(k)}(\alpha)z^n,
\]
with the Taylor branch positive at \(z=0\) and real \(0<\alpha<1\). The following are exact all-index statements:

1. For \(k=4\), all noninitial convolution coefficients are nonpositive, \(\omega_n^{(4)}(\alpha)\leq0\) for every integer \(n\geq1\), **if and only if** \(0<\alpha\leq7/32\). They are all strictly negative when \(0<\alpha<7/32\). At \(\alpha=7/32\), exactly the coefficient with index \(n=2\) is zero; every other noninitial coefficient is strictly negative.
2. For \(k=5\), the corresponding sharp nonpositivity range is \(0<\alpha\leq13/150\), with strict negativity for \(0<\alpha<13/150\). At the endpoint, exactly \(\omega_2^{(5)}\) vanishes.
3. For \(k=6\), \(\omega_2^{(6)}(\alpha)>0\) for **every** \(0<\alpha<1\); hence there is no admissible positive fractional order with all noninitial coefficients nonpositive.

These are statements about the **uncorrected convolution coefficients**. They neither assert that a fully discretized fractional evolution equation is positivity-preserving nor cover any starting-weight corrections.

## Assumptions and scope

The BDF symbols are normalized at zero by \(p_k(z)=\delta_k(z)/\delta_k(0)\), with \(p_k(0)=1\). Multiplication by the positive factor \(\delta_k(0)^\alpha\) does not change coefficient signs. For the first two orders in the theorem the exact polynomials are
\[
\begin{aligned}
p_4(z)&=1-\frac{48}{25}z+\frac{36}{25}z^2-\frac{16}{25}z^3+\frac3{25}z^4,\\
p_5(z)&=1-\frac{300}{137}z+\frac{300}{137}z^2-\frac{200}{137}z^3+\frac{75}{137}z^4-\frac{12}{137}z^5.
\end{aligned}
\]
They factor as \(p_k(z)=(1-z)q_k(z)\), where
\[
\begin{aligned}
q_4(z)&=1-\frac{23}{25}z+\frac{13}{25}z^2-\frac3{25}z^3,\qquad q_4(1)=\frac{12}{25},\\
q_5(z)&=1-\frac{163}{137}z+z^2-\frac{63}{137}z^3+\frac{12}{137}z^4,\qquad q_5(1)=\frac{60}{137}.
\end{aligned}
\]
All timestep scalings \(h^{-\alpha}\) with \(h>0\) preserve signs and can be included without changing the assertions.

## Proof

**1. Necessary sharp bounds.** If \(p(z)=1+p_1z+p_2z^2+\cdots\), then
\[
[z^2]p(z)^\alpha=\alpha p_2+\frac{\alpha(\alpha-1)}2p_1^2.
\]
For the two indicated BDF symbols this is, respectively,
\[
[z^2]p_4(z)^\alpha=\frac{\alpha(1152\alpha-252)}{625},\qquad
[z^2]p_5(z)^\alpha=\frac{300\alpha(150\alpha-13)}{18769}.
\]
Thus \(\alpha\leq7/32\), respectively \(\alpha\leq13/150\), is necessary. For BDF6, the normalized first two nonconstant coefficients are \(-120/49\) and \(150/49\), giving
\[
[z^2]p_6(z)^\alpha=\frac{\alpha(150+7200\alpha)}{2401}>0
\]
for every \(\alpha>0\).

**2. A single endpoint suffices.** Write \(a_4=7/32\) and \(a_5=13/150\). Suppose at \(\alpha=a_k\) the normalized series has the shape
\[
p_k(z)^{a_k}=1-G_k(z),\quad G_k(z)=\sum_{n\geq1}c_nz^n,
\]
where \(c_1>0\), \(c_2=0\), and \(c_n>0\) for all \(n\geq3\). For any \(0<\alpha<a_k\), set \(\gamma=\alpha/a_k\in(0,1)\). The binomial expansion
\[
1-(1-G_k(z))^\gamma=\sum_{j\geq1}(-1)^{j+1}\binom\gamma j G_k(z)^j
\]
has nonnegative coefficients, because each displayed scalar is positive. In particular its coefficients at indices one and three or higher are positive by the \(j=1\) term, and its index-two coefficient is positive by the \(j=2\) term involving \(c_1^2\). Therefore all noninitial coefficients of \(p_k(z)^\alpha\) are strictly negative. It remains to prove the endpoint assertion for each \(k\in\{4,5\}\).

**3. Exact finite endpoint checks.** Set \(W_n=[z^n]p_k(z)^{a_k}\), \(p_k(z)=\sum_{j=0}^k p_jz^j\), and \(W_0=1\). Differentiating \(p_k(z)^{a_k}\) yields the exact rational recurrence
\[
nW_n=\sum_{j=1}^{\min(k,n)}\big((1+a_k)j-n\big)p_jW_{n-j}.
\]
The standalone Python checker `verify.py` uses `fractions.Fraction`, not floating-point comparisons, to establish \(W_1<0\), \(W_2=0\), and \(W_n<0\) for **every** integer \(3\leq n\leq999\), for both orders. It additionally verifies \(W_3=-133/5000\) for order four and \(W_3=-676/56307\) for order five. A finite computation alone is not used as the infinite proof.

**4. Root separation for the infinite tail.** For \(k=4\) choose \(R=7/5\); for \(k=5\) choose \(R=4/3\). In each case every zero of \(q_k\) has modulus strictly greater than \(R\). This is verified exactly using the Schur reduction on the reciprocal polynomial \(f(w)=w^{k-1}q_k(R/w)\). For a real monic polynomial \(f(w)=w^m+\cdots+c\) with \(|c|<1\), define \(f^*(w)=w^mf(1/w)\) and \(f_{\rm new}(w)=(f(w)-cf^*(w))/(w(1-c^2))\). If the reduced polynomial is Schur-stable, so is \(f\): a unit-circle zero of \(f\) would also be a zero of the reduced polynomial, and otherwise Rouché's theorem applies since \(|cf^*|<|f|\) on the circle. The successive constant coefficients from this procedure are, for order four,
\[
-\frac{1029}{3125},\quad \frac{726425}{1088348},\quad -\frac{1162595}{1814773},
\]
and, for order five,
\[
\frac{1024}{3699},\quad-\frac{8905536}{12634025},\quad
\frac{3865313017488}{4724118603137},\quad
-\frac{1438423308}{3211002475}.
\]
Every one has absolute value strictly less than one. The checker derives and compares these fractions, thereby proving the claimed root separation by the reduction argument.

**5. Explicit analytic tail certificate.** Fix either endpoint order and write \(a=a_k\), \(q=q_k\). The function \(\psi(z)=q(z)^a\), with \(\psi(0)=1\), is analytic in a neighborhood of \(|z|\leq R\). On that circle, the triangle inequality gives \(|q_4(z)|<4\) or \(|q_5(z)|<6\). Since \(a_4<1/4\) and \(a_5<1/10\), \(|\psi(z)|<2\) in both cases. Let
\[
\eta(z)=\frac{\psi(z)-\psi(1)}{1-z}=\sum_{j\geq0}\eta_jz^j.
\]
The denominator satisfies \(|1-z|\geq R-1\) on the circle and \(\psi(1)<1\). Consequently Cauchy's estimate gives \(|\eta_j|\leq MR^{-j}\), with the rational choices \((R,M)=(7/5,8)\) or \((4/3,9)\).

Put \(b_n=[z^n](1-z)^a\) and \(s_n=-b_n>0\) for \(n\geq1\). For \(n\geq2\),
\[
s_n=\frac a n\prod_{j=1}^{n-1}\left(1-\frac a j\right)
\geq\frac{a(1-a)}{n(n-1)}.
\]
Because \(0<a<1/2\), for \(1\leq m\leq n\) we also have \(s_m/s_n\leq(n/m)^2\): multiply the individual inequalities \((j+1)/(j-a)\leq((j+1)/j)^2\). Moreover
\[
[z^r](1-z)^{a+1}=\frac{1+a}{r}s_{r-1}\quad(r\geq2),
\]
and every coefficient of \((1-z)^{a+1}\) has modulus at most \(1+a\).

For \(n\geq1000\), split the convolution of \(\eta\) with \((1-z)^{a+1}\) at \(j=n/2\). In the first half, \(s_{n-j-1}\leq5s_n\), and summing the geometric majorant gives
\[
\left|\sum_{j\leq n/2}\eta_j[z^{n-j}](1-z)^{a+1}\right|
\leq \frac{C_1}{n}s_n,\quad C_1=\frac{10M(1+a)R}{R-1}.
\]
For the remaining indices, the lower bound for \(s_n\) gives
\[
\left|\sum_{j>n/2}\eta_j[z^{n-j}](1-z)^{a+1}\right|
\leq C_2 n(n-1)R^{-n/2}s_n,\quad
C_2=\frac{M(1+a)R}{(R-1)a(1-a)}.
\]
Exact rational inequalities in `verify.py` show \(C_2n(n-1)R^{-n/2}<1/100\) for **all** \(n\geq1000\): its left-hand side decreases with integer \(n\), and the value at \(n=1000\) is less than \(1/100\). They also give
\[
\begin{array}{c|cc}
k&C_1/1000&q_k(1)\\\hline
4&0.34125&12/25\\
5&0.3912&60/137
\end{array}
\]
so in each case \(C_1/1000+1/100<q_k(1)\leq q_k(1)^a=\psi(1)\). Finally,
\[
W_n=\psi(1)b_n+[z^n](1-z)^{a+1}\eta(z)<0\qquad(n\geq1000).
\]
Together with the finite exact recurrence checks, this proves the endpoint signs for every positive index, completing the theorem.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. The checker independently forms the normalized symbols and their factors, computes the Schur reflection constants in exact rational arithmetic, replays all recurrence coefficients through index \(999\), and checks the rational tail inequalities whose derivation is written above. Its expected final output is `ALL EXACT CHECKS PASSED`. The analytic estimates and the composition step, rather than mere enumeration, justify the infinite quantifier.

## Relationship to prior work

Lubich's 1986 fractional BDF construction introduced the generating symbols and treated convergence, not the sharp all-index off-diagonal sign thresholds. Schädle, López-Fernández and Lubich's 2005 preprint develops fast computation of convolution quadratures, including high-order BDF context, without this classification. López-Fernández and Płociniczak explicitly motivate a negative-history-weight admissibility condition, establish a BDF2 formula and discuss numerical signs, but do not derive the BDF4 and BDF5 endpoint classifications or the BDF6 impossibility. Jin, Li and Zhou analyze high-order BDF corrections and convergence, not the asserted coefficient sign thresholds. Previously analyzed lower BDF orders do not imply the higher-order claims; the proof here requires separate exact zero separation and analytic tail bounds.

## Limitations

This theorem concerns the uncorrected scalar convolution weights on a uniform step grid, not variable steps, starting corrections, inverse integral weights, or positivity of a complete numerical solver. A negative-history-weight condition is relevant to certain comparison and discrete energy arguments, but it is not by itself a universal convergence or maximum-principle theorem. The verification is a reproducible exact computer-assisted proof with an analytic infinite-tail argument, not an independently audited theorem. While the listed primary sources were inspected for the relevant formulas and comparison statements, further specialist literature might affect priority.

## References

- Ch. Lubich, *Discretized Fractional Calculus*, SIAM Journal on Mathematical Analysis 17 (1986), 704–719, https://doi.org/10.1137/0517050 ; lawful full text: https://people.math.ethz.ch/~hiptmair/Seminars/CONVQUAD/Articles/LUB86.pdf .
- A. Schädle, M. López-Fernández and C. Lubich, *Fast and oblivious convolution quadrature*, arXiv:math/0504461v1, first publicly submitted 2005-04-22, https://arxiv.org/abs/math/0504461 .
- M. López-Fernández and Ł. Płociniczak, *Convolution Quadrature for the quasilinear subdiffusion equation*, arXiv:2311.00081v1 (2023), https://arxiv.org/abs/2311.00081 .
- B. Jin, B. Li and Z. Zhou, *Correction of High-Order BDF Convolution Quadrature for Fractional Evolution Equations*, SIAM Journal on Scientific Computing 39 (2017), A3129–A3152, https://doi.org/10.1137/17M1118816 .
