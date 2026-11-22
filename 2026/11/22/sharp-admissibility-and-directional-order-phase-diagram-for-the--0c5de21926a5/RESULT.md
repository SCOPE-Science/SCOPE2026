# Sharp admissibility and directional-order phase diagram for the power-mean FGM-N1 copula

## Finding

For the power-mean FGM-N1 family introduced by Chesneau (2024), the complete copula-validity interval is generally larger than the previously supplied sufficient interval \([-1,1]\). Moreover, a sharp shape threshold determines whether conditional stochastic monotonicity survives or reverses in each direction; the same thresholds characterize density total positivity of order two (TP2) and reverse regularity (RR2).

Write, for \(0<a<1\) and \(b\in\mathbb R\setminus\{0\}\),
\[
P_{a,b}(t)=\{a+(1-a)t^b\}^{1/b},\qquad
h_{a,b}(t)=t\{1-P_{a,b}(t)\},\quad 0<t\le1,
\]
with \(h_{a,b}(0)=0\). Define the positive numbers
\[
M(a,b)=\begin{cases}1-a^{1/b},&b>0,\\1,&b<0,\end{cases}
\qquad
L(a,b)=\begin{cases}
1-a,&b\ge 1-2/a,\\
-1-\dfrac{2b}{1-b}\left\{\dfrac{a(1-b)}{2}\right\}^{1/b},&b<1-2/a.
\end{cases}
\]
For \(a_i\in(0,1)\), \(b_i\in\mathbb R\setminus\{0\}\) and \(\alpha\in\mathbb R\), set \(M_i=M(a_i,b_i)\), \(L_i=L(a_i,b_i)\) and
\[
C_\alpha(u,v)=uv+\alpha h_{a_1,b_1}(u)h_{a_2,b_2}(v).
\]
Then \(C_\alpha\) is a bivariate copula **if and only if**
\[
\boxed{-\frac{1}{\max\{M_1M_2,L_1L_2\}}
\le\alpha\le\frac{1}{\max\{M_1L_2,L_1M_2\}}.}
\]
Both endpoints are attainable. For any nonzero admissible \(\alpha\), the conditional response \(V\mid U=u\) is globally stochastically monotone in \(u\) if and only if \(b_1\ge1-2/a_1\). For \(\alpha>0\) it is stochastically increasing, and for \(\alpha<0\) decreasing. If \(b_1<1-2/a_1\), its direction switches exactly once at
\[
u_* =\left\{-\frac{a_1(b_1+1)}{2(1-a_1)}\right\}^{1/b_1}\in(0,1).
\]
Interchanging the indices gives the analogous statement for \(U\mid V=v\). The copula density is TP2 precisely when \(\alpha=0\), or when \(\alpha>0\) and **both** \(b_i\ge1-2/a_i\); it is RR2 precisely when \(\alpha=0\), or when \(\alpha<0\) and both thresholds hold. In all other nonzero cases its \(2\times2\) density minors have both signs.

## Assumptions and scope

The assertion concerns the continuously extended original power-mean formula, with each \(a_i\) strictly between zero and one, each \(b_i\) nonzero and finite, and \(\alpha\) any finite real number. Its boundary margins are uniform: \(C(u,0)=C(0,v)=0\), \(C(u,1)=u\), and \(C(1,v)=v\). The order assertions refer to conditional distributions at interior conditioning values; TP2 and RR2 refer to all ordered pairs of interior density arguments. Independence \(\alpha=0\) is both TP2 and RR2, and has conditional equality rather than a strict direction. The signs are strict on open intervals away from the unique switching point in the reversing regime.

## Proof

Put \(D(t)=a+(1-a)t^b\), \(P(t)=D(t)^{1/b}\) and \(k(t)=h'(t)\). Direct differentiation gives the exact identities
\[
k(t)=1-P(t)-(1-a)t^bD(t)^{1/b-1},
\]
\[
\boxed{k'(t)=-(1-a)t^{b-1}D(t)^{1/b-2}
\{a(b+1)+2(1-a)t^b\}.}
\]
All factors except the last bracket have a fixed positive sign after the minus sign. At the right endpoint \(k(1)=-(1-a)\). At the left endpoint \(\lim_{t\downarrow0}k(t)=1-a^{1/b}\) for \(b>0\), and equals \(1\) for \(b<0\). For \(b\ge1-2/a\), the bracket is positive in \((0,1)\) (even at equality it is positive before the right endpoint), so \(k\) decreases strictly. If \(b<1-2/a\), necessarily \(b<-1\), and the bracket changes sign precisely once, from positive to negative, at the stated \(u_*\). Thus \(k\) decreases to a unique minimum and then increases; its maximum remains at the left endpoint. At the minimum the base \(D(u_*)=a(1-b)/2\) and \((1-a)u_*^b/D(u_*)=-(b+1)/(1-b)\), hence
\[
k(u_*)=1+\frac{2b}{1-b}\{a(1-b)/2\}^{1/b}=-L(a,b).
\]
Consequently the full closure of the derivative range is \([-L(a,b),M(a,b)]\), with \(0<M,L\le1\). The endpoint limits also prove that the formula and the first derivatives are integrable up to the boundary.

The mixed density of the proposed function is
\[
c(u,v)=1+\alpha k_1(u)k_2(v).
\]
By the independent attainability (or approachability) of each derivative endpoint, its possible correction factor has sharp maximum \(\max\{M_1M_2,L_1L_2\}\) and sharp negative minimum \(-\max\{M_1L_2,L_1M_2\}\). Thus \(c\ge0\) everywhere exactly on the asserted interval. On this interval the margin identities and integration of the nonnegative density over every rectangle prove two-increasingness. Outside it, a strictly negative mixed density occurs at some interior point near an endpoint extremizer, contradicting two-increasingness. This proves both necessity and sufficiency, including parameter boundaries.

For \(v\in(0,1)\), positivity of \(h_2(v)\) follows from \(P_{a_2,b_2}(v)<1\). The regular conditional distribution function is
\[
F_{V\mid U=u}(v)=\partial_u C(u,v)=v+\alpha k_1(u)h_2(v).
\]
Stochastic ordering therefore follows exactly the direction of \(-\alpha k_1(u)\). The proven derivative sign diagram gives the claimed monotonicity and its unique reversal at \(u_*\). The transposed conditional is identical with indices exchanged.

Finally, for \(u_1<u_2\) and \(v_1<v_2\), the density minor has the exact rank-one identity
\[
c(u_1,v_1)c(u_2,v_2)-c(u_1,v_2)c(u_2,v_1)
=\alpha\{k_1(u_1)-k_1(u_2)\}\{k_2(v_1)-k_2(v_2)\}.
\]
If both derivative functions decrease, this has the sign of \(\alpha\). If either derivative reverses, the difference in that direction has both signs, while the other direction always has a strictly positive or negative difference, so both determinant signs occur. That proves the sharp TP2/RR2 claims.

## Verification

The included standalone `checker.py` reproduces exact elementary benchmark cases, evaluates the derivative identities numerically and checks sharp interval endpoints and the unique directional reversal on deterministic test grids. In particular, \(a_1=a_2=1/2\), \(b_1=-5\), \(b_2=1\) gives the exact enlarged admissible interval \([-2,2]\) and a reversal in only the first conditioning direction; \(\alpha=3/2\) is valid but lies outside the original sufficient box. The checker is a reproducibility aid, not a substitute for the general analytic proof above.

## Relationship to prior work

Chesneau (2024), Table 2 and Section 4.2, introduces precisely this FGM-N1 expression with \(\alpha\in[-1,1]\), provides a density expansion and plots, but does not derive the full \(\alpha\)-validity interval, the one-switch shape threshold or the TP2/RR2 classification. Fuchs and Tschimpke (2023), Example 4, gives the general derivative-positivity criterion for generalized FGM copulas and general positive dependence context. That abstract criterion underlies the present calculation but does not give these shape-specific exact extrema or conditional phase diagram. Durante (2009) supplies the more general copula-construction scheme. The result does not claim novelty for generic rank-one factorization or for classical stochastic ordering and total-positivity definitions.

## Limitations

Only the specified FGM-N1 family is classified. The singular formal value \(b=0\), boundary shapes \(a=0\) or \(a=1\), and other copulas from the same construction are excluded. The complete novelty comparison is limited to accessible text and research-index matches; a related older general FGM paper was available only as an abstract, so publication priority is not independently certified. The work has not received independent mathematical validation.

## References

1. C. Chesneau, *Diverse copulas through Durante's method: Exploring parametric functions*, Operations Research and Decisions 34(3) (2024), 61–86. DOI: 10.37190/ord240304. First published online 17 October 2024. https://ord.pwr.edu.pl/assets/papers_archive/ord2024vol34no3_4.pdf .
2. S. Fuchs and M. Tschimpke, *A novel positive dependence property and its impact on a popular class of concordance measures*, arXiv:2306.09676 (first posted 16 June 2023), Example 4. https://arxiv.org/pdf/2306.09676 .
3. F. Durante, *Construction of non-exchangeable bivariate distribution functions*, Statistical Papers 50 (2009), 383–391. DOI: 10.1007/s00362-007-0064-5.
4. C. Amblard and S. Girard, *A new extension of bivariate FGM copulas*, Metrika 70 (2009), 1–17. DOI: 10.1007/s00184-008-0174-7. Full text not inspected.
