# Exact orthogonal Schäffer constant of the mixed cubic–taxicab plane
## Finding
Let \(X_3=(\mathbb R^2,N)\), with
\[
N(s,t)=\begin{{cases}}
(|s|^3+|t|^3)^{{1/3}},&st\ge0,\\
|s|+|t|,&st<0.
\end{{cases}}
\]
For Birkhoff--James orthogonality \(x\perp_B y\), meaning \(N(x)\le N(x+\lambda y)\) for every real \(\lambda\), define
\[
g_\perp(X_3)=\inf_{{x,y\in S_{{X_3}},\,x\perp_B y}}\max\{{N(x+y),N(x-y)\}}.
\]
Then
\[
g_\perp(X_3)=\left(1+\frac{{3}}{{2^{{4/3}}}}\right)^{{1/3}}
=1.2987267195645926\ldots.
\]
The infimum is attained by
\[
x=(1/2,-1/2),\qquad y=(2^{{-1/3}},2^{{-1/3}}).
\]

## Assumptions and scope
The scalars are real. The assertion concerns exactly the mixed \(\ell_3\)-\(\ell_1\) plane above and the one-sided Birkhoff--James condition \(x\perp_B y\). No assertion is made for other Day--James exponents or for a symmetric orthogonality relation.

Put \(c=2^{{-1/3}}\) and \(K=(1+3c/2)^{{1/3}}\). The goal is to prove \(g_\perp(X_3)=K\).

## Proof
The unit sphere has two smooth types away from the coordinate axes. Its same-sign pieces are cubic arcs, while its opposite-sign pieces are line segments. The norm is invariant under coordinate interchange and simultaneous sign reversal, so these two types and the axes exhaust all unit vectors up to symmetry.

On a same-sign cubic arc, write
\[
x=(a,ta),\qquad 0<t\le1,\qquad a=(1+t^3)^{{-1/3}}.
\]
The unique norming functional has kernel spanned by \( (t^2,-1)\). Hence the unique unit vector, up to sign, with \(x\perp_B y\) is
\[
y=\left(\frac{{t^2}}{{1+t^2}},-\frac1{{1+t^2}}\right).
\]
Set \(u=t^2/(1+t^2)\) and \(v=1/(1+t^2)\). If \(0<t\le1/2\), then \(ta-v<0\), so
\[
N(x+y)=1+a(1-t)\ge1+\frac c2>K,
\]
because \((1+c/2)^3=1+3c/2+3c^2/4+c^3/8>1+3c/2=K^3\).

It remains to treat \(1/2\le t\le1\). Here both coordinates of \(x-y=(a-u,ta+v)\) are positive. Let
\[
F(t)=N(x-y)^3=(a-u)^3+(ta+v)^3.
\]
Direct differentiation, using \(1+t^3=(1+t)(t^2-t+1)\), gives
\[
F'(t)=-\frac{{3G(t)}}{{(t+1)^{{1/3}}(1+t^2)^4(t^2-t+1)^{{1/3}}}},
\]
where, with \(r=(1+t^3)^{{1/3}}\),
\[
G(t)=t^7+2t^5r-2t^5+3t^4-3t^3+2t^2+2tr-1.
\]
Since \(r\ge1\),
\[
G(t)\ge L(t):=t^7+3t^4-3t^3+2t^2+2t-1.
\]
For \(1/2\le t\le3/4\),
\[
L'(t)=7t^6+3t^2(4t-3)+4t+2\ge-\frac{{27}}{{16}}+4=\frac{{37}}{{16}}>0,
\]
and for \(3/4\le t\le1\) every displayed summand of \(L'(t)\) is nonnegative, with \(4t+2>0\). Thus \(L\) is increasing on \([1/2,1]\), and \(L(1/2)=41/128>0\). Therefore \(F'(t)<0\), so
\[
N(x-y)^3=F(t)\ge F(1)=(c-1/2)^3+(c+1/2)^3=1+\frac{3c}{2}=K^3.
\]
Hence every orthogonal pair based at a non-axis cubic point has maximum signed distance at least \(K\).

On an opposite-sign line segment, symmetry lets us write \(x=(a,a-1)\) with \(1/2\le a<1\). Its norming functional is \(f(s,t)=s-t\), so the orthogonal unit direction is \(y=(c,c)\), up to sign. Both coordinates of \(x+y\) are positive and
\[
N(x+y)^3=(a+c)^3+(a+c-1)^3.
\]
This expression is strictly increasing in \(a\), so it is at least its value at \(a=1/2\), namely \(1+3c/2=K^3\).

Finally consider an axis point, say \(x=(1,0)\). Its norming functionals are \(f_s(s_1,s_2)=s_1-s s_2\) with \(0\le s\le1\). Thus, after changing the sign of \(y\) if needed, every unit \(y\) with \(x\perp_B y\) has the form \(y=(p,q)\), where \(0\le p\le q\) and \(p^3+q^3=1\). If \(p\ge1/4\), then
\[
N(x+y)^3=2+3p+3p^2\ge\frac{{47}}{{16}}>K^3,
\]
since \(K^3<5/2\). If \(p\le1/4\), then \(q^3\ge63/64>(3/4)^3\), whence
\[
N(x-y)=1-p+q>\frac32>K.
\]
This covers the nonsmooth axes.

For \(x=(1/2,-1/2)\) and \(y=(c,c)\), both vectors are unit, the norming functional \(f(s,t)=s-t\) at \(x\) annihilates \(y\), and
\[
N(x+y)^3=N(x-y)^3=(c+1/2)^3+(c-1/2)^3=1+\frac{3c}{2}.
\]
Thus the lower bound is attained and the stated exact value follows.

## Verification
The proof exhausts all smooth boundary types and separately treats the nonsmooth coordinate axes. The differentiating identity for \(F'(t)\) was algebraically expanded and checked against the displayed definition of \(F\). The equality pair gives the decimal value \(1.2987267195645926\ldots\), agreeing with the four-decimal value reported in the motivating paper. No finite sampling or numerical optimization is used as a proof of the global infimum.

## Relationship to prior work
Baronti and Papini introduced \(g_\perp\) as the Birkhoff--James-restricted Schäffer constant. Their Example 5.7 is exactly the mixed cubic--taxicab plane above and records only \(g_\perp(X_3)\approx1.2987\), explicitly noting that the calculations are not simple. The exact formula and the global boundary classification above sharpen that numerical entry.

Yang and Li's earlier paper on the same \(\ell_3-\ell_1\) plane computes the classical James constant, not the later orthogonality-restricted Schäffer constant. Searches for the exact decimal, the Example 5.7 wording, the invariant name, and mixed cubic--taxicab aliases did not locate a published exact formula. Related exact computations for other Birkhoff-restricted constants or other spaces do not imply this infimum.

## Limitations
The novelty search cannot prove absence from all literature. The full text of the 2016 Yang--Li paper was not lawfully accessible in the sources inspected; its accessible abstract and the 2022 paper's citation identify its result as the classical James constant. No claim is made about the exact orthogonal James constant of this mixed cubic--taxicab plane or about a general exponent formula.

## References
1. M. Baronti and P. L. Papini, “Parameters in Banach spaces and orthogonality,” Constructive Mathematical Analysis 5 (2022), 37–45, DOI 10.33205/cma.1067323. Published online 9 March 2022.
2. C. S. Yang and H. Y. Li, “The James constant for the \(\ell_3-\ell_1\) space,” Acta Mathematica Sinica, English Series 32 (2016), 1075–1079, DOI 10.1007/s10114-016-5423-5.
