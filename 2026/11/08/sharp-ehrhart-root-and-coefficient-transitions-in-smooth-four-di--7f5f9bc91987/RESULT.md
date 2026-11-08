# Sharp Ehrhart root and coefficient transitions in smooth four-dimensional Cayley polytopes

## Finding
For every integer \(c\ge 0\), set
\[
R_c=\left\{(x_1,x_2,y,z)\in\mathbb R^4:
0\le z\le1,\quad x_1,x_2\ge0,\quad x_1+x_2\le1+cz,
\quad 0\le y\le c+1-cz\right\}.
\]
This is the smooth, seven-facet, twelve-vertex family \(R_{2,c}\) of Liu--Tang--Tao--Zhang. For \(t\in\mathbb Z_{\ge0}\), let \(L_c(t)=\#(tR_c\cap\mathbb Z^4)\), and let \(h_c^*(u)\) denote the Ehrhart-series numerator, normalized by
\[
\sum_{t\ge0}L_c(t)u^t=\frac{h_c^*(u)}{(1-u)^5}.
\]
The following identities and exhaustive parameter classification hold:
\[
L_c(t)=\frac{(t+1)((c+2)t+4)}{24}
\Bigl((c^2+6c+6)t^2+(-c^2+6c+12)t+6\Bigr),
\]
\[
h_c^*(u)=1+(c+1)(c+7)u
+\frac{(c+1)(c^2+11c+8)}2u^2
+\frac{c(c+1)^2}2u^3.
\]
The \(h^*\)-polynomial has two distinct strictly negative real roots when \(c=0\), and three distinct strictly negative real roots for every integer \(c\ge1\). In contrast, the Ehrhart polynomial undergoes three sharp transitions:

1. Its linear coefficient is negative exactly when \(c\ge10\).
2. Its quadratic coefficient is negative exactly when \(c\ge12\).
3. It has two distinct positive real roots, both in \((0,1)\), exactly when \(c\ge13\). For \(1\le c\le12\), its remaining quadratic factor has nonreal conjugate roots; at \(c=0\), all Ehrhart roots are negative.

In particular this provides an infinite smooth lattice-polytope family in which the entire \(h^*\)-root spectrum remains strictly negative and real, even after two Ehrhart coefficients become negative and two positive Ehrhart roots appear.

## Assumptions and scope
The parameter \(c\) ranges over all nonnegative **integers**, and the lattice is the standard lattice \(\mathbb Z^4\). The family has dimension four; it is smooth and has exactly seven facets and twelve vertices as established by Proposition 4.1 of [1] (with \(r=2\)). These structural properties are premises rather than new claims. Real-rootedness of \(h_c^*\) is claimed for the displayed family, not all smooth four-polytopes. The distinction between Ehrhart roots and roots of its series numerator is essential. At \(c=0\), \(h_c^*\) has degree two rather than three.

## Proof
Fix nonnegative integers \(c,t\). A lattice point of \(tR_c\) at integer height \(z=j\), \(0\le j\le t\), has \(\binom{t+cj+2}{2}\) possible pairs \((x_1,x_2)\) and \((c+1)t-cj+1\) possible \(y\)-coordinates. Hence
\[
L_c(t)=\sum_{j=0}^{t}\binom{t+cj+2}{2}((c+1)t-cj+1).\tag{1}
\]
Expanding this summand in powers of \(j\), and using
\[
\sum_{j=0}^{t}1=t+1,\quad\sum_{j=0}^{t}j=\frac{t(t+1)}2,
\quad\sum_{j=0}^{t}j^2=\frac{t(t+1)(2t+1)}6,
\quad\sum_{j=0}^{t}j^3=\frac{t^2(t+1)^2}4,
\]
produces the stated factored formula for \(L_c(t)\). In particular its coefficients, from constant through fourth degree, are
\[
\begin{aligned}
[t^0]L_c&=1,\\
[t^1]L_c&=-\frac{2c^2-15c-42}{12},\\
[t^2]L_c&=-\frac{(c+6)(c^2-10c-18)}{24},\\
[t^3]L_c&=\frac{8c^2+33c+30}{12},\\
[t^4]L_c&=\frac{(c+2)(c^2+6c+6)}{24}.
\end{aligned}
\]
The last two are strictly positive for \(c\ge0\). The first possibly negative coefficient crosses zero at the positive real parameter \((15+\sqrt{561})/4\), strictly between \(9\) and \(10\); the second crosses at \(5+\sqrt{43}\), strictly between \(11\) and \(12\). This gives the two integer thresholds.

For any four-dimensional lattice polytope, the numerator coefficients satisfy
\[
[u^j]h_c^*(u)=\sum_{k=0}^j(-1)^{j-k}\binom{5}{j-k}L_c(k)
\quad(0\le j\le4).
\tag{2}
\]
Substituting the factored \(L_c\) into (2) yields the displayed cubic \(h_c^*\) (and zero coefficient at \(u^4\)). At \(c=0\), the polynomial is \(1+7u+4u^2\), whose discriminant is \(33>0\) and whose two roots are negative. For \(c\ge1\), the cubic discriminant is exactly
\[
\operatorname{Disc}_u(h_c^*)=\frac{(c+1)^3}{4}
(c^7+27c^6+298c^5+1714c^4+5258c^3+8416c^2+6696c+2112).
\tag{3}
\]
Every coefficient of the parenthesized polynomial is strictly positive. Therefore the discriminant is positive for \(c\ge1\), giving three distinct real roots. Every nonzero coefficient of \(h_c^*\) is positive, so there are no nonnegative roots; all three are strictly negative.

Finally, the remaining quadratic factor of \(L_c(t)\) has discriminant
\[
(-c^2+6c+12)^2-24(c^2+6c+6)=c^2(c^2-12c-12).
\tag{4}
\]
For integral \(1\le c\le12\), (4) is negative; for every integer \(c\ge13\), it is positive. In the latter range, the sum of the two quadratic roots equals
\[
\frac{c^2-6c-12}{c^2+6c+6}\in(0,1),
\]
while their product is \(6/(c^2+6c+6)>0\). Thus both roots belong to \((0,1)\). The other two Ehrhart roots come from the linear factors and are strictly negative. At \(c=0\), \(L_0(t)=(t+1)^3(t+2)/2\), completing all boundary cases.

## Verification
The supplied \(verify.py\) uses only standard-library exact integers and rational arithmetic. For the lattice-slice formula (1), both sides are polynomials in \((c,t)\) of respective degrees at most \((3,4)\). The complete grid of four distinct \(c\)-values and five distinct \(t\)-values therefore certifies the polynomial identity. The same degree argument verifies (2) using four \(c\)-values, while (3), an identity of degree at most ten in \(c\), is checked at eleven distinct values. These are exact finite polynomial-identity certificates, not a finite experiment extrapolated without a degree bound. Coefficient-sign and root-sign conclusions are proved analytically above. Execute `python3 verify.py` to reproduce the checks; the script also checks boundary parameters.

## Relationship to prior work
Liu, Tang, Tao, and Zhang [1] introduce this smooth four-polytope family in their general construction \(R_{r,c}\), prove its facet and smoothness properties, and give a slicing formula and the explicit example \(R_{2,12}\) with two negative Ehrhart coefficients. Their examined Section 4 does not give the complete two-threshold classification, the positive-real-root transition, or the real-rooted \(h^*\) formula for every parameter. The present result takes their polynomial-count formula as the starting point and adds those exact parameter and root conclusions.

Castillo, Liu, Nill, and Paffenholz [2] establish earlier smooth negative-coefficient examples using vertex chiseling, not the present seven-facet Cayley family. Beck, De Loera, Develin, Pfeifle, and Stanley [3] give general restrictions on Ehrhart roots in low dimension, but not the exact transition in this family. Ferroni [4] derives Ehrhart formulas for Cayley sums of boxes and constructs nonunimodal \(h^*\) examples; the current fibers are products of triangles and segments rather than boxes, and the examined results do not imply (3).

For \(c>0\), the four triangular faces at the ends of this four-polytope occur in two different scales; they are not all translates, so the polytope is not an affine Cartesian product of a triangle and quadrilateral. Thus general Cartesian-product real-rootedness results do not establish the present assertion. The conclusion does not rest solely on a title search; these geometric differences prevent the closest product result from implying it.

## Limitations
This is a sharp parameter classification for one natural infinite family, not a theorem for all seven-facet smooth four-polytopes, all smooth Cayley sums, or all dimensions. The exact analytic identities prove the claims; the supplementary program requires only Python 3. A self-review was performed; independent mathematical audit has not been performed. No priority claim is based on the absence of a search hit: historical equivalence in unindexed literature remains a residual risk.

## References
[1] Feihu Liu, Jinlong Tang, Sihao Tao, Zihao Zhang, *Ehrhart positivity of smooth polytopes with few facets*, arXiv:2610.27819v1, first submitted 2026-10-20, §4, Proposition 4.1 and equation (4.4). https://arxiv.org/abs/2610.27819

[2] Federico Castillo, Fu Liu, Benjamin Nill, Andreas Paffenholz, *Smooth polytopes with negative Ehrhart coefficients*, arXiv:1704.05532, especially §§1–2. https://arxiv.org/abs/1704.05532

[3] Matthias Beck, Jesús A. De Loera, Mike Develin, Julian Pfeifle, Richard P. Stanley, *Coefficients and Roots of Ehrhart Polynomials*, arXiv:math/0402148, especially §4. https://arxiv.org/abs/math/0402148

[4] Luis Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513v2, especially §§2–3. https://arxiv.org/abs/2609.10513
