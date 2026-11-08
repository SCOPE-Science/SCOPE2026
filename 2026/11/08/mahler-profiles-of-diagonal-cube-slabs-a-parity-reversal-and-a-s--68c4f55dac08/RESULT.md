# Mahler profiles of diagonal cube slabs: a parity reversal and a sharp three-dimensional phase

## Finding
For every integer \(d\ge2\) and real \(0<t\le d\), set
\[
K_d(t)=[-1,1]^d\cap\left\{x:\left|\sum_{i=1}^d x_i\right|\le t\right\},\qquad
\mathcal P_d(t)=\operatorname{Vol}_d(K_d(t))\operatorname{Vol}_d(K_d(t)^\circ).
\]
The polar is with respect to the origin. Write \(z_+=\max(z,0)\). Both volumes, and therefore the complete Mahler-product profile, are given by the finite expressions
\[
\begin{aligned}
V_d(t)&=\frac1{d!}\sum_{j=0}^{d}(-1)^j\binom dj
\left[(d+t-2j)_+^d-(d-t-2j)_+^d\right],\\
W_d(t)&=\frac1{d!}\left[2^d+2\sum_{j=0}^d\binom dj
\left(\frac{d-2j}{t}-1\right)_+\right],\qquad \mathcal P_d(t)=V_d(t)W_d(t).
\end{aligned}
\]
There is a strict parity reversal in the degeneration toward the central hyperplane. In every odd dimension \(d\ge3\), \(\mathcal P_d(t)\) is strictly decreasing on \(0<t\le1\). In every even dimension \(d\ge2\), it is strictly increasing for all sufficiently small positive \(t\). More explicitly, for even \(d\ge4\), its positive right derivative at \(t=0\) (of the continuously extended product) equals
\[
\mathcal P_d'(0+)=\frac{\binom{d}{d/2}}{d!}\,H_d>0,\quad
H_d=\frac2{(d-1)!}\sum_{j=0}^{\lfloor(d-1)/2\rfloor}
(-1)^j\binom dj(d-2j)^{d-1}>0.
\]
For \(d=2\), the exact profile is \(\mathcal P_2(t)=8+2t-t^2\) on \(0<t\le2\), hence \(\mathcal P_2'(0+)=2\).

In dimension three the complete sharp profile is
\[
\mathcal P_3(t)=
\begin{cases}
12-\dfrac43t^2,&0<t\le1,\\[2mm]
\left(8-\dfrac{(3-t)^3}{3}\right)\left(1+\dfrac1t\right),&1\le t\le3.
\end{cases}
\]
It has global minimum \(32/3\) **exactly** at \(t=1\) and \(t=3\), a unique strict local maximum on \((1,3)\) at the root \(t_*\in(1,3)\) of
\[
3t_*^4-16t_*^3+18t_*^2+3=0,
\qquad t_*=1.775633451807\ldots,
\]
with \(\mathcal P_3(t_*)=11.549073272632\ldots\). Its sharp supremum on the positive-width family is \(12\), approached only as \(t\downarrow0\) and not attained. In particular the three-dimensional profile has an interior minimum separating a thin-slab decreasing phase from a finite-width increasing phase.

## Assumptions and scope
All volumes are ordinary ambient-dimensional Euclidean Lebesgue volumes. The body is full dimensional precisely for \(t>0\); no volume product is assigned to \(t=0\), and the value \(12\) there is a one-sided limit, not the Mahler product of a lower-dimensional section. The origin is the Santaló point because the body is centrally symmetric. The polar is \(K^\circ=\{y:\langle x,y\rangle\le1\text{ for every }x\in K\}\). For \(t=d\), the body is the cube. No all-dimensional global extremizer beyond the stated near-zero parity characterization is asserted.

## Proof
**1. Cube-slab volume.** If independent \(U_i\) are uniform on \([0,1]\), then \(\sum_i(2U_i-1)\) is the sum of independent uniform \([-1,1]\) variables. Inclusion-exclusion for the Irwin--Hall distribution gives
\[
\operatorname{Pr}\left\{\sum_i U_i\le u\right\}
=\frac1{d!}\sum_{j=0}^d(-1)^j\binom dj(u-j)_+^d.
\]
Take the difference of this CDF at \((d+t)/2\) and \((d-t)/2\), multiply by cube volume \(2^d\), and simplify to obtain the displayed \(V_d(t)\).

**2. Polar volume.** Put \(C=B_1^d=\operatorname{conv}\{\pm e_i:1\le i\le d\}\) and \(v=t^{-1}(1,\ldots,1)\). Polarity of intersections yields
\[
K_d(t)^\circ=\operatorname{conv}(C\cup\{v,-v\}).
\]
Since \(0\in C\), \(\operatorname{conv}(C,v)\cup\operatorname{conv}(C,-v)=\operatorname{conv}(C,v,-v)\). Moreover their intersection is exactly \(C\): if a point is written both as \(\alpha v+(1-\alpha)p\) and \(-\beta v+(1-\beta)q\), with \(p,q\in C\) and \(\alpha,\beta>0\), then it equals the convex combination
\[
\frac{\beta(1-\alpha)}{\alpha+\beta}p+
\frac{\alpha(1-\beta)}{\alpha+\beta}q+
\frac{2\alpha\beta}{\alpha+\beta}\,0\in C.
\]
Each facet of \(C\) is the simplex \(F_\varepsilon=\operatorname{conv}\{\varepsilon_i e_i\}_{i=1}^d\), with normal \(\varepsilon\in\{-1,1\}^d\) and inequality \(\langle\varepsilon,y\rangle\le1\). If \(\langle\varepsilon,v\rangle>1\), the exterior pyramid over this facet in \(\operatorname{conv}(C,v)\) has volume \((\langle\varepsilon,v\rangle-1)/d!\); otherwise the facet contributes zero. The analogous statement holds for \(-v\). Distinct visible-facet pyramids have disjoint interiors, giving
\[
W_d(t)=\frac1{d!}\left[2^d+2\sum_{\varepsilon\in\{-1,1\}^d}
(\langle\varepsilon,v\rangle-1)_+\right].
\]
Grouping normal signs by number of negative entries yields the claimed formula. This calculation does not rely on an unproved equality between ambient and section volume.

**3. Thin-slab parity.** Define
\[
B_d=\sum_{j=0}^{d}\binom dj|d-2j|
=2d\binom{d-1}{\lfloor(d-1)/2\rfloor},\quad
C_d=\begin{cases}\binom d{d/2},&d\text{ even},\\0,&d\text{ odd}.\end{cases}
\]
The binomial identity follows by writing \((d-2j)\binom dj=d[\binom{d-1}{j}-\binom{d-1}{j-1}]\) and telescoping the positive half of the sum. For \(0<t\le1\), counting positive, negative and zero facet-normal sums in the polar formula gives
\[
W_d(t)=\frac1{d!}\left(\frac{B_d}{t}+C_d\right).
\]
Let \(f_d\) be the probability density of a sum of \(d\) independent uniform \([-1,1]\) variables. The density \(f_2(s)=(2-|s|)/4\) is strictly decreasing for \(0<s<2\). The convolution recurrence
\[
f_{d+1}'(s)=\tfrac12\bigl(f_d(s+1)-f_d(s-1)\bigr)
\]
shows inductively that \(f_d\) is even and strictly decreasing on \((0,d)\) for every \(d\ge2\). Indeed \(|s+1|>|s-1|\), and \(f_d(s-1)>0\) when \(0<s<d+1\). Hence
\[
\frac{V_d(t)}t=\frac{2^{d+1}}t\int_0^t f_d(s)\,ds
\]
is strictly decreasing. For odd \(d\), \(C_d=0\), which proves strict decrease of \(\mathcal P_d(t)\) on \((0,1]\). For even \(d\ge4\), the density is differentiable and even at zero, so \(V_d(t)=H_dt+o(t^2)\) with \(H_d=V_d'(0)>0\), and the product expansion gives \(\mathcal P_d'(0+)=H_dC_d/d!>0\). For \(d=2\), direct substitution yields the stated quadratic with right derivative \(2\).

**4. Complete three-dimensional profile.** Directly evaluating the two volume formulas gives
\[
\begin{array}{c|cc}
&0<t\le1&1\le t\le3\\ \hline
V_3(t)&6t-2t^3/3&8-(3-t)^3/3\\
W_3(t)&2/t&1+1/t
\end{array}
\]
and thus the displayed piecewise product. The first branch is strictly decreasing. On the second branch,
\[
3t^2\mathcal P_3'(t)=Q(t)=3t^4-16t^3+18t^2+3,
\qquad Q'(t)=12t(t-1)(t-3).
\]
On \((1,3)\), \(Q'\) is strictly negative; moreover \(Q(1)=8\) and \(Q(3)=-24\). Exactly one interior critical point exists, with a sign change from positive to negative. The exact factorization
\[
\mathcal P_3(t)-\frac{32}{3}
=\frac{(t-3)(t-1)(t^2-4t-1)}{3t}>0\qquad(1<t<3)
\]
together with the first branch proves both global equality cases. To certify the sharp upper bound without relying on numerical root approximation, set \(u=(t-1)/2\). On \(1\le t\le3\),
\[
3t(12-\mathcal P_3(t))=
4(1-u)^4+8u(1-u)^3+24u^3(1-u)+12u^4>0.
\]
On \(0<t\le1\), \(\mathcal P_3(t)=12-4t^2/3<12\), and its limit at zero is \(12\). This proves all assertions.

## Verification
The accompanying `checker.py` computes the finite inclusion-exclusion and facet-pyramid formulas with exact fractions and independently reconstructs the clipped-cube and polar convex hulls from their vertices using SciPy's convex-hull routines. It passed 15 pairs of Euclidean-volume comparisons in dimensions two through five. SymPy identities check the three-dimensional product, its derivative and factorization; exact binomial identities and the small-slab polar formula are also checked for dimensions two through ten. Command: `python checker.py`. Runtime requirements: Python 3.10 or later, NumPy, SciPy and SymPy. The analytic all-dimensional proof above, not finite checker coverage, establishes the infinite-dimensional parameter statement.

## Relationship to prior work
Iriyeh--Shibata prove the dimension-three symmetric Mahler lower bound and characterize its equality bodies (arXiv:1706.01749, first public version June 6, 2017). The lower bound \(32/3\) is therefore known; the present contribution is not that inequality, but this one-parameter family's explicit all-dimensional product, odd/even thin-slab reversal and exact three-dimensional extrema and upper endpoint. Fradelizi--Hubard--Meyer--Roldán-Pensado--Zvavitch give an alternative proof and a general stability statement (arXiv:1904.10765), not this parametrized profile. Karasev proves the Mahler lower bound for hyperplane sections of \(\ell_p\) balls and Hanner polytopes (arXiv:1902.08971); a positive-width slab is an ambient-dimensional intersection, not such a hyperplane section. The known Irwin--Hall distribution supplies one volume ingredient and is not claimed as new. Related published cube--cross-polytope intersection families use \(\sum_i|x_i|\le c\) rather than the single diagonal slab \(|\sum_i x_i|\le t\); they have different intermediate face structures and do not directly yield this phase diagram.

## Limitations
Historical priority remains provisional, especially for implicit formulas obtained from classical polar-volume identities under different terminology. The result does not prove the Mahler conjecture in dimensions four and higher, a global multidimensional extremum of this slab family, or any independent validation. The supremum \(12\) refers only to the full-dimensional positive-width three-dimensional family; it is not the volume product of the singular limiting section.

## References
1. H. Iriyeh and M. Shibata, *Symmetric Mahler's conjecture for the volume product in the three dimensional case*, arXiv:1706.01749 (first public version 2017-06-06).
2. M. Fradelizi, A. Hubard, M. Meyer, E. Roldán-Pensado and A. Zvavitch, *Equipartitions and Mahler volumes of symmetric convex bodies*, arXiv:1904.10765 (first public version 2019-04-24).
3. R. Karasev, *Mahler's conjecture for some hyperplane sections*, arXiv:1902.08971 (first public version 2019-02-24).
4. H. Iriyeh and M. Shibata, *Minimal volume product of convex bodies with certain discrete symmetries and its applications*, arXiv:2203.13990 (first public version 2022-03-26).
