# Sharp Gaussian contraction on the odd first–third Hermite plane

## Finding

Let \(\gamma\) be standard Gaussian probability on \(\mathbb R\), let \(H_1(x)=x\), \(H_3(x)=x^3-3x\), and let \(T_\rho H_j=\rho^jH_j\), for \(0<\rho\le1\). On the real plane \(E=\operatorname{span}_{\mathbb R}\{H_1,H_3\}\), put \(r=\rho^2\). Define
\[
\begin{aligned}
N_r(t)={}&3+24rt+252r^2t^2+1296r^3t^3+3348r^4t^4,\\
q_r(t)={}&-324r^3t^4+(558r^4-126r^2)t^3\\
&+(162r^3-18r)t^2+(21r^2-3)t+r.
\end{aligned}
\]
For every \(0<r\le1\), \(q_r\) has exactly two simple real roots: one negative and one positive. Denote the positive root by \(t_r\). Then the exact attained norm is
\[
\boxed{\|T_\rho|_E\|_{L^2(\gamma)\to L^4(\gamma)}^4
=\frac{r^2N_r(t_r)}{(1+6t_r^2)^2}.}
\]
Every nonzero extremizer is a real scalar multiple of \(H_1+t_rH_3\); in particular, neither pure Hermite mode is extremal at any positive \(\rho\).

Let \(B(z)\) be the polynomial
\[
\begin{aligned}
B(z)={}&1984500z^{10}-3061800z^9+1457865z^8-191979z^7\\
&+56574z^6-48015z^5+6108z^4-417z^3\\
&+342z^2-61z+3.
\end{aligned}
\]
There is a unique \(r_*\in(1/3,1/2)\) at which this norm equals one; equivalently, \(r_*\) is the unique \(r\in(1/3,1/2)\) satisfying \(B(r^2)=0\). Numerically,
\[
r_*=0.41396374498806822692\ldots,\qquad
\rho_*=\sqrt{r_*}=0.64340014375819673648\ldots.
\]
On \(E\) the semigroup is \(L^2\)-to-\(L^4\) contractive **exactly when** \(0\le\rho\le\rho_*\); at \(\rho=0\), the zero operator is trivially contractive. In semigroup-time notation \(\rho=e^{-s}\), the sharp time is \(s_*=0.44098844074205304974\ldots\), strictly below the unrestricted Nelson time \(\tfrac12\log 3\).

## Assumptions and scope

All inputs are real; the Gaussian is centered and variance one; the Hermite polynomials are in the probabilists' normalization. The operator is the restriction of the standard Ornstein–Uhlenbeck semigroup to the two-dimensional invariant *mean-zero odd* space \(E\). The input and output norms are taken with respect to the same Gaussian probability measure, with input exponent two and output exponent four. The result does not cover complex input coefficients or the full odd Gaussian space.

## Proof

**Fourth moments and exact reduction.** Gaussian Wick moments give
\[
\mathbb EH_1^2=1,\quad \mathbb EH_3^2=6,\quad
\mathbb E(H_1^{4-k}H_3^k)=(3,6,42,324,3348)_k,\quad0\le k\le4.
\]
For any nonzero \(aH_1+bH_3\) with \(a\ne0\), write \(t=b/a\). Since \(T_\rho(aH_1+bH_3)=a\rho(H_1+rtH_3)\), the exact ratio of output fourth power to input second power squared is
\[
K_r(t)=\frac{r^2N_r(t)}{(1+6t^2)^2}.
\]
For \(t>0\), \(N_r(t)>N_r(-t)\) because
\[
N_r(t)-N_r(-t)=48rt+2592r^3t^3>0.
\]
Thus a maximizer has a positive coefficient ratio, unless it is a pure mode. Direct differentiation yields
\[
K_r'(t)=\frac{24r^2q_r(t)}{(1+6t^2)^3}.
\]
At \(t=0\) the derivative is positive. As \(t\to+\infty\), the derivative is negative, hence the positive maximum is attained at a positive finite zero of \(q_r\), not at either pure mode.

**Exactly one positive stationary ratio.** Put
\[
P_6(z)=961z^6-1212z^5+1359z^4-56z^3+39z^2-12z+1.
\]
The exact quartic discriminant is
\[
\operatorname{Disc}_t(q_r)=-110224800r^6P_6(r^2).
\]
The rational Sturm chain of \(P_6\) has sign vectors \((+,-,-,-,+,-,-)\) at \(z=0\) and \((+,+,-,-,+,+,-)\) at positive infinity. Both have three variations; thus \(P_6\) has no positive real root, and \(P_6(0)=1\) makes it strictly positive on \([0,\infty)\). The discriminant is therefore negative for every \(r>0\). Since \(q_r(0)=r>0\) and \(q_r(t)\to-\infty\) as \(t\to\pm\infty\), \(q_r\) has one negative and one positive real zero, both simple, and no other real zeros. This proves the norm formula and the complete equality classification.

**Sharp contraction threshold.** The maximum \(M(r)=\max_{t\in\mathbb R\cup\{\infty\}}K_r(t)\) is continuous on \([0,1]\). It is strictly increasing for \(r>0\): if \(r_2>r_1>0\), at the positive maximizing \(t_{r_1}\), all coefficients of \(r^2N_r(t_{r_1})\) are nonnegative and its constant coefficient is positive, so \(K_{r_2}(t_{r_1})>K_{r_1}(t_{r_1})\). At \(r=1/3\), the norm is strictly less than one because
\[
(1+6t^2)^2-\tfrac19N_{1/3}(t)
=\frac2{27}\bigl[t^2(424t^2-72t+4)+(116t^2-12t+9)\bigr]>0
\]
for every real \(t\); both displayed quadratics are positive because their discriminants are negative. At \(r=1/2\), the same difference evaluated at \(t=1/3\) equals \(-413/144<0\). Hence there is one crossing \(r_*\in(1/3,1/2)\).

At a crossing the two polynomials
\[
D_r(t)=(1+6t^2)^2-r^2N_r(t),\qquad q_r(t)
\]
vanish at the same positive \(t\). Direct elimination gives
\[
\operatorname{Res}_t(D_r,q_r)=419904A(r^2)B(r^2),\quad
A(z)=2883z^4-12z^3+198z^2-52z+3.
\]
On \(z\in(1/9,1/4)\), exact Sturm variation counts for \(A\) at the left and right endpoints are \(2,2\), and for \(B\) they are \(6,5\). Thus \(A\) has no root and \(B\) exactly one root there. This is precisely \(r_*^2\), and exact rational evaluation further gives
\[
0.413963<r_*<0.413964.
\]
The positive optimizer at the threshold has \(t_{r_*}=0.46107618244813027968\ldots\). Since the norm is strictly increasing in \(r\), contractivity is equivalent to \(r\le r_*\). Finally \(r_*>1/3\) proves the strict improvement over the classical all-input radius \(1/\sqrt3\).

## Verification

The included standalone `check_odd_hermite.py` recomputes Gaussian moments, the stationary equation, the quartic discriminant, the rational Sturm-chain variation counts, the elimination resultant, strict Nelson-radius inequality, and rational isolating brackets. It requires Python 3 with SymPy. Run `python check_odd_hermite.py`. Its exact-arithmetic completion message is `ALL_ODD_HERMITE_CONTRACTIVITY_CHECKS_PASSED`. Rational sample root isolations supplement, but do not replace, the universal Sturm arguments.

## Relationship to prior work

Classical Nelson–Gross Gaussian hypercontractivity gives \(L^2\)-to-\(L^4\) contraction on the *whole* Gaussian space for \(\rho\le1/\sqrt3\), but does not determine the optimal larger radius after restricting to the odd first–third eigenspace. Bakry, Bolley, and Gentil analyze dimensional refinements and Gaussian kernel inequalities, not the exact two-eigenmode optimization here. Van Neerven and Portal study Gaussian Weyl calculus and general \(L^p\)-to-\(L^q\) boundedness, likewise not this two-mode sharp constant. The older Weissler work concerns semigroup mapping conditions, but its full text was unavailable during this comparison; a hidden equivalent calculation cannot be excluded. Exact sixth moments for the same Hermite pair and exact bounds for the first–second Hermite plane concern different exponents/operators or different spectral subspaces and do not imply the present result.

## Limitations

The result is confined to real coefficients and the two fixed odd eigenlevels one and three, under the fourth-moment target norm. It gives no classification for higher odd Hermite levels, arbitrary finite spectral masks, other exponent pairs, or complex-time semigroups. The algebraic norm formula is implicit through a uniquely isolated real root rather than a radical formula. The originality assessment remains subject to older unindexed calculations and the unavailable full text of Weissler's paper.

## References

1. D. Bakry, F. Bolley and I. Gentil, *Dimension dependent hypercontractivity for Gaussian kernels*, arXiv:1003.5072, initially public March 26, 2010; subsequently *Probability Theory and Related Fields* 154 (2012), 845–874.
2. J. van Neerven and P. Portal, *Weyl calculus with respect to the Gaussian measure and restricted \(L^p\)-\(L^q\) boundedness of the Ornstein–Uhlenbeck semigroup in complex time*, arXiv:1702.03602, initially public February 13, 2017; *Bulletin de la Société Mathématique de France* 146 (2018), 691–712.
3. F. B. Weissler, *Two-point inequalities, the Hermite semigroup, and the Gauss–Weierstrass semigroup*, *Journal of Functional Analysis* 32 (1979), 102–121, DOI:10.1016/0022-1236(79)90080-6.
4. L. Gross, *Logarithmic Sobolev inequalities*, *American Journal of Mathematics* 97 (1975), 1061–1083.
