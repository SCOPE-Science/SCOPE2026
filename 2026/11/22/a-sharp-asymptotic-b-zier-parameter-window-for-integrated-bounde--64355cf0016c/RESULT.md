# A sharp asymptotic Bézier parameter window for integrated bounded-variation error

## Finding
For each positive real parameter \(\alpha\), consider the classical Bernstein–Bézier sampling operator \(B_{n,\alpha}\) defined below. Its exact worst integrated approximation error per unit real bounded variation is the maximum of \(2n\) explicit scalar integrals. Moreover, for every fixed \(\alpha>0\),
\[
\lim_{n\to\infty}\sqrt n\,\sup_{|Df|(0,1)>0}\frac{\|B_{n,\alpha}f-f\|_{L^1(0,1)}}{|Df|(0,1)}=\frac12c(\alpha),\quad
c(\alpha)=\int_0^\infty\bigl[\bar\Phi(z)^\alpha+1-\Phi(z)^\alpha\bigr]dz,
\]
where \(\Phi\) is the standard Gaussian distribution function and \(\bar\Phi=1-\Phi\).

The continuous parameter function \(c\) has **exactly one** minimizer \(\alpha_*\) on \((0,\infty)\). It lies strictly between \(1\) and \(2\), and numerically \(\alpha_*\approx1.405429234985\) with \(c(\alpha_*)\approx0.757497464523\). Most importantly,
\[
c(\alpha)\begin{cases}
<c(1),&1<\alpha<2,\\
=c(1),&\alpha=1\text{ or }\alpha=2,\\
>c(1),&0<\alpha<1\text{ or }\alpha>2,
\end{cases}
\qquad c(1)=c(2)=\sqrt{2/\pi}.
\]
Thus each parameter strictly between \(1\) and \(2\) asymptotically **improves** the classical Bernstein sharp integrated BV error, despite performing **worse at degree one**: \(C_1(\alpha)=\alpha/(1+\alpha)>1/2=C_1(1)\). At the optimum, the leading constant is about \(5.06\%\) below the classical one. Every asymptotically norming sequence of single-jump locations converges to \(1/2\).

## Assumptions and scope
Fix an integer \(n\ge1\), \(\alpha>0\), and \(x\in[0,1]\). Write
\[
p_{n,j}(x)=\binom nj x^j(1-x)^{n-j},\quad J_{n,k}(x)=\sum_{j=k}^n p_{n,j}(x),\quad J_{n,0}=1,\ J_{n,n+1}=0.
\]
Set \(Q_{n,k}^{(\alpha)}=J_{n,k}^{\alpha}-J_{n,k+1}^{\alpha}\) and
\[
(B_{n,\alpha}f)(x)=\sum_{k=0}^n Q_{n,k}^{(\alpha)}(x)f(k/n).
\]
The coefficients are nonnegative and sum to one. The domain consists of real functions with finite distributional variation on \((0,1)\), represented canonically by a right-continuous function whose endpoint values are its one-sided traces, so
\(f(x)=c+\mu((0,x])\) for \(0<x<1\), \(f(0)=c\), \(f(1)=c+\mu((0,1))\), with finite signed measure \(\mu=Df\). This convention is necessary because endpoint or nodal point values enter sampling. Let \(C_n(\alpha)\) denote the displayed sharp ratio.

For \(1\le k\le n\) define
\[
F_{n,k,\alpha}(s)=\int_0^s J_{n,k}(x)^\alpha\,dx+\int_s^1\bigl[1-J_{n,k}(x)^\alpha\bigr]dx,
\qquad 0\le s\le1.
\]
Then the **finite-degree formula**, with the specified one-sided supremum interpretation, is
\[
C_n(\alpha)=\max_{1\le k\le n}\max\left\{F_{n,k,\alpha}((k-1)/n),F_{n,k,\alpha}(k/n)\right\}.
\]
Values at left cell endpoints may be limits from the right and need not be attained by a jump exactly at that grid value. No complete finite-degree extremizer classification is claimed.

## Proof
**1. Exact jump reduction and finite formula.** For an interior jump \(h_s(x)=\mathbf1_{[s,1]}(x)\), choose the unique \(k\) with \((k-1)/n<s\le k/n\). The definition telescopes to \((B_{n,\alpha}h_s)(x)=J_{n,k}(x)^\alpha\). Its integrated error equals \(F_{n,k,\alpha}(s)\). In the canonical BV representation \(f=c+\int h_s\,d\mu(s)\), the operator fixes constants; Fubini and the triangle inequality give \(\|B_{n,\alpha}f-f\|_1\le\int F_{n,k(s),\alpha}(s)d|\mu|(s)\), and jumps (or sequences of jumps approaching cell endpoints) establish the reverse sharpness. Because \(J_{n,k}\) is strictly increasing on \((0,1)\),
\[
F'_{n,k,\alpha}(s)=2J_{n,k}(s)^\alpha-1,\qquad F''_{n,k,\alpha}(s)=2\alpha J_{n,k}(s)^{\alpha-1}J'_{n,k}(s)>0.
\]
A strictly convex function maximizes on a closed cell at an endpoint; continuity supplies the one-sided limits. This proves the exact formula. For \(n=1\), \(J_{1,1}(x)=x\), so \(C_1(\alpha)=\max\{\alpha,1\}/(1+\alpha)\).

**2. Pointwise scaled jump-error limit.** Let \(s_n\to s\in(0,1)\), and \(k_n=\lceil ns_n\rceil\). In the window \(x=s_n+z\sqrt{s(1-s)/n}\), the binomial central limit theorem and \(0\le k_n/n-s_n<1/n\) give
\[
J_{n,k_n}(x)\longrightarrow\Phi(z)
\]
for every fixed \(z\). The step-error integrand becomes \(\Phi(z)^\alpha\) for \(z<0\), and \(1-\Phi(z)^\alpha\) for \(z>0\). For dominated convergence, binomial Bernstein tail bounds yield, with positive constants depending only on \(\alpha\),
\[
|h_{s_n}(x)-(B_{n,\alpha}h_{s_n})(x)|\le C_\alpha\exp\left[-c_\alpha\frac{n|x-s_n|^2}{s_n(1-s_n)+\frac43|x-s_n|}\right].
\]
Indeed on the left use \(J^\alpha\) and a binomial upper-tail bound, and on the right use \(1-J^\alpha\le\max\{1,\alpha\}(1-J)\) and a lower-tail bound. The variance function \(x(1-x)\) is one-Lipschitz, allowing the denominator replacement. The same tail inequality is uniformly integrable in the scaled coordinate on compact interior neighborhoods. Consequently
\[
\sqrt n\,\|B_{n,\alpha}h_{s_n}-h_{s_n}\|_1\longrightarrow\sqrt{s(1-s)}\,c(\alpha).
\]

**3. Boundary control and global sharpness.** Integrating the preceding exponential tail bound, separately over \(u\le s_n(1-s_n)\) and \(u\ge s_n(1-s_n)\), gives
\[
\|B_{n,\alpha}h_{s_n}-h_{s_n}\|_1\le C_\alpha\left[\sqrt{\frac{s_n(1-s_n)}n}+\frac1n\right].
\]
Thus any sequence \(s_n\to0\) or \(s_n\to1\) has scaled error tending to zero. Choose nearly maximizing jumps, pass to a subsequence of their locations, and apply either the interior limit or boundary bound. The unique maximizer of \(\sqrt{s(1-s)}\) is \(s=1/2\); taking jumps with \(s_n\to1/2\) gives the matching lower bound. The global limit and localization assertion follow.

**4. Unique parameter optimum and exact improvement window.** Put \(q(z)=\bar\Phi(z)\), so \(0<q(z)<1/2\) for \(z>0\), and write
\[
c(\alpha)=\int_0^\infty\{q^\alpha+1-(1-q)^\alpha\}\,dz,
\quad c'(\alpha)=A_\alpha-B_\alpha,
\]
where
\[
A_\alpha=\int_0^\infty(1-q)^\alpha[-\log(1-q)]dz,\qquad
B_\alpha=\int_0^\infty q^\alpha[-\log q]dz.
\]
Both are finite and strictly positive. In the logarithmic derivative of \(A_\alpha/B_\alpha\), the first integral weights values \(-\log(1-q)\in(0,\log2)\) and the second weights \(-\log q\in(\log2,\infty)\). Therefore
\[
\frac d{d\alpha}\log(A_\alpha/B_\alpha)=
\mathbb E_{B,\alpha}[-\log q]-\mathbb E_{A,\alpha}[-\log(1-q)]>0.
\]
Hence \(c'\) changes sign at most once, from negative to positive. At \(\alpha=1\), the integrand of \(B_1-A_1\) is
\(g(q)=-q\log q+(1-q)\log(1-q)>0\): its continuous extension vanishes at both \(q=0\) and \(q=1/2\), and \(g''(q)=-1/q+1/(1-q)<0\) between them. Thus \(c'(1)<0\). Pointwise algebra gives \(q^2+1-(1-q)^2=2q=q+1-(1-q)\), so \(c(2)=c(1)=2\int_0^\infty\bar\Phi(z)dz=\sqrt{2/\pi}\). Since \(c'(1)<0\), \(c(2)=c(1)\), and \(A_\alpha/B_\alpha\) is strictly increasing, a unique \(\alpha_*\in(1,2)\) satisfies \(c'(\alpha_*)=0\); \(c\) strictly decreases before it and increases afterward. This proves the complete parameter window. Numerical quadrature/root solving gives the stated approximations but is not needed for uniqueness or inequalities.

## Verification
The accompanying standalone `check.py` uses SciPy quadrature, binomial survival functions and Gaussian integrals. It directly compares 126 step responses with a separate numerical integral, checks the degree-one formula, confirms the exact Gaussian order-one/order-two identity, locates the parameter minimum, and compares scaled finite-degree coefficients for four degrees and three parameters. These finite checks corroborate, but do not prove, the universal asymptotic or parameter-ordering statements.

## Relationship to prior work
The original generalized Bernstein–Bézier polynomial uses cumulative binomial tails raised to a positive power; Chang (1983), Zeng–Piriou (1998), and Zeng (2000) study related approximation questions. Lian (2013) studies one-point BV convergence bounds for the Bernstein–Bézier/Chlodowsky family, rather than maximizing the **integral of approximation error divided by global variation** or optimizing its sharp leading coefficient over \(\alpha\). Ren–Zeng (2015) review the classical family while proving modulus-of-continuity estimates for a *different*, beta-modified Bézier operator. The present claim is the exact BV-to-integrated-error norm formula plus its global Gaussian-limit parameter classification, not the classical pointwise jump-limit already described in prior work. A close historical-priority risk remains because the original 1998 and 2000 journal texts could not be reviewed in full.

## Limitations
The theorem uses one-dimensional equispaced **point sampling**, canonical right-continuous BV representatives with endpoint trace constraints, real scalar inputs, fixed positive \(\alpha\), and Lebesgue \(L^1(0,1)\) error. It says nothing about parameters varying with degree, continuous-data minimax error, other norms, higher dimensions, or the exact first finite degree at which a particular \(1<\alpha<2\) outperforms \(\alpha=1\). Numerical decimals are approximations; the exact parameter is characterized by the unique zero of \(A_\alpha-B_\alpha\). Historical novelty is subject to independent priority checking.

## References
- G.-Z. Chang, *Generalized Bernstein–Bézier polynomial*, Journal of Computational Mathematics 1(4) (1983), 322–327 (historical definition referenced by Ren–Zeng).
- X. M. Zeng and A. Piriou, *On the rate of convergence of two Bernstein–Bézier type operators for bounded variation functions*, Journal of Approximation Theory 95 (1998), 369–387. DOI: 10.1006/jath.1997.3227.
- X. M. Zeng, *On the rate of convergence of two Bernstein–Bézier type operators for bounded variation functions II*, Journal of Approximation Theory 104 (2000), 330–344. DOI: 10.1006/jath.2000.3451.
- H. Karsli, *On Convergence of Chlodovsky and Chlodovsky–Kantorovich Polynomials in the Variation Seminorm*, Mediterranean Journal of Mathematics 10 (2013), 41–56; first public online April 12, 2012. DOI: 10.1007/s00009-012-0186-4.
- B.-Y. Lian, *Rate of approximation of bounded variation functions by the Bézier variant of Chlodowsky operators*, Journal of Mathematical Inequalities 7 (2013), 647–657. DOI: 10.7153/jmi-07-59. https://files.ele-math.com/articles/jmi-07-59.pdf.
- M.-Y. Ren and X.-M. Zeng, *Approximation of a kind of new type Bézier operators*, Journal of Inequalities and Applications 2015:412; first public December 23, 2015. DOI: 10.1186/s13660-015-0940-9.
