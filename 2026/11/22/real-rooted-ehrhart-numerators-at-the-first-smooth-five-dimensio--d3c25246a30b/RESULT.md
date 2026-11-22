# Real-rooted Ehrhart numerators at the first smooth five-dimensional sign obstruction

## Finding
For every integer \(c\ge0\), consider the five-dimensional lattice polytope
\[
Q_c=\{(x_1,x_2,x_3,x_4,z):0\le z\le1,\ x_i\ge0,\ \sum_{i=1}^4x_i\le1+cz\}.
\]
It has exactly seven facets, ten vertices, and is smooth. Let \(L_c(t)=\#(tQ_c\cap\mathbb Z^5)\) for integer \(t\ge0\), and define the Ehrhart numerator \(H_c(u)\) by
\[
\sum_{t\ge0}L_c(t)u^t=\frac{H_c(u)}{(1-u)^6}.
\]
**Theorem.** For every integer \(c\ge0\), *every root of \(H_c\) is real, strictly negative, and simple*. The degree is one at \(c=0\), three at \(c=1,2\), and four at every integer \(c\ge3\). Moreover, its ordinary Ehrhart polynomial has a negative linear coefficient **if and only if** \(c\ge16\), the sharp integer threshold. In particular the numerator stays real-rooted throughout, and beyond, the onset of ordinary Ehrhart nonpositivity within this smooth, facet-minimal five-dimensional family.

The exact numerator is
\[
\begin{aligned}
H_c(u)={}&1+h_1(c)u+h_2(c)u^2+h_3(c)u^3+h_4(c)u^4,\\
h_1(c)={}&\frac{(c+1)(c+6)(c^2+7c+16)}{24},\\
h_2(c)={}&\frac{c(c+1)(c+3)(11c+34)}{24},\\
h_3(c)={}&\frac{c(c+1)(11c^2+19c-18)}{24},\\
h_4(c)={}&\frac{c(c-1)(c-2)(c+1)}{24}.
\end{aligned}
\]
In the ordinary power basis,
\[
[t]L_c(t)=\frac{-c^4+175c^2+750c+2220}{720}.
\]
In particular this coefficient equals \(37/12\) at \(c=15\) and \(-181/20\) at \(c=16\).

## Assumptions and scope
All parameters \(c\) are nonnegative integers; the ambient lattice is \(\mathbb Z^5\). The polytope is the height-one Cayley frustum joining \(\Delta_4\) and \((c+1)\Delta_4\), where \(\Delta_4=\operatorname{conv}(0,e_1,e_2,e_3,e_4)\). The smoothness, seven-facet property, and integer-height lattice-count formula for this family are established in Liu–Tang–Tao–Zhang (2026), Proposition 5.1; these underlying facts are credited and not asserted as new. The theorem classifies *numerator* roots and one sharp ordinary-coefficient threshold for precisely this family, not all smooth five-polytopes.

## Proof
**Lattice count and coefficient extraction.** At integer height \(j\in\{0,\ldots,t\}\), the slice of \(tQ_c\) is \((t+cj)\Delta_4\). Weak compositions therefore give the exact formula
\[
L_c(t)=\sum_{j=0}^{t}\binom{t+cj+4}{4}.
\tag{1}
\]
For \(k\in\{0,1,2,3,4,5\}\), the coefficient of \(u^k\) in the Ehrhart numerator is
\[
h_k(c)=\sum_{j=0}^{k}(-1)^{k-j}\binom{6}{k-j}L_c(j).
\tag{2}
\]
Expanding (1) in (2) yields the four displayed factorizations, with \(h_0=1\) and \(h_5=0\). The last equality is also forced because there can be no interior lattice point at a height strictly between zero and one. Hence the degree bounds are exact; for \(c\ge3\), all five displayed nonzero coefficients are positive.

**Boundary parameters.** Direct substitution gives \(H_0(u)=1+4u\), \(H_1(u)=1+14u+15u^2+u^3\), and \(H_2(u)=1+34u+70u^2+16u^3\). The two cubic discriminants are respectively \(23377\) and \(2455472\), both strictly positive. All cubic coefficients are positive, so all their three distinct real roots are negative. The linear case is immediate.

**All twists \(c\ge3\).** Put \(\Delta(c)=\operatorname{Disc}_{u}(H_c)\). Direct exact polynomial expansion gives
\[
995328\,\Delta(c)=c^2(c+1)^3P(c-2),
\tag{3}
\]
where \(P(v)=\sum_{j=0}^{19}p_jv^j\). The complete sequence of twenty **strictly positive integer coefficients** \((p_0,\ldots,p_{19})\) is given in `certificate.json` and explicitly checked against the resultant/discriminant formula by `verify.py`. Thus \(\Delta(c)>0\) for every integer \(c\ge3\). Further, exact substitution gives
\[
H_c\left(-\frac1{c+1}\right)
=-\frac{c^6+5c^5+22c^4+68c^3+136c^2+152c+72}{24(c+1)^3}<0.
\tag{4}
\]
But \(H_c(0)=1>0\), and the leading quartic coefficient is positive, so \(H_c(u)\to+\infty\) as \(u\to-\infty\). By continuity, equation (4) gives at least two distinct negative real roots. A real quartic with nonzero positive discriminant has either zero or four real roots (a conjugate-pair case would have negative discriminant). Therefore all four roots are **distinct and real**. Since \(H_c(u)>0\) for \(u\ge0\) by positivity of every coefficient, all roots are strictly negative. This is an infinite-parameter proof by polynomial identity and sign analysis, not numerical sampling.

**Sharp ordinary sign threshold.** Taking the coefficient of \(t\) in the polynomial interpolation of (1) yields the linear coefficient displayed in the finding. Write \(f(c)=c^4-175c^2-750c-2220\). Its coefficient sequence has exactly one sign change, so Descartes' rule gives exactly one positive real root (existence follows since \(f(0)<0\) and \(f(c)\to+\infty\)). Exact evaluation gives \(f(15)<0<f(16)\). Therefore \([t]L_c(t)>0\) for integers \(0\le c\le15\) and \([t]L_c(t)<0\) for integers \(c\ge16\). The remaining positive ordinary coefficients follow directly from their power-basis formulas: 
\[
\begin{aligned}
[t^2]L_c&=\frac{5(c^3+9c^2+24c+34)}{48},\\
[t^3]L_c&=\frac{c^4+18c^3+83c^2+150c+135}{72},\\
[t^4]L_c&=\frac{c^4+9c^3+26c^2+34c+22}{48},\\
[t^5]L_c&=\frac{c^4+5c^3+10c^2+10c+5}{120}.
\end{aligned}
\]
Thus the linear coefficient is the only one ever negative in this five-dimensional family. This completes the theorem.

## Verification
Run `python3 verify.py` beside `certificate.json`; Python 3 with SymPy is required. The program reconstructs equation (3) as a full symbolic polynomial identity, checks that every one of the twenty shifted coefficients is positive, verifies equation (4) symbolically and the two exceptional cubic discriminants, and recomputes the polynomial numerator from integer slice counts at nine separate twists and seven dilations. It also reconstructs the ordinary linear coefficient and checks its two threshold values exactly. All checks passed in the packaged source. The finite checks only cross-check transcription; the symbolic identities and the stated analytic sign arguments prove the claims for all permitted integers.

## Relationship to prior work
Liu, Tang, Tao, and Zhang, *Ehrhart positivity of smooth polytopes with few facets* (2026), introduce exactly \(Q_{r,c}\), prove smoothness/facet counts, and the lattice-count identity (1). Their Section 5 proves eventual ordinary Ehrhart negativity in dimensions at least five and exhibits \(Q_{4,16}\). Their inspected treatment does not derive the complete numerator polynomial, an all-twist root classification, or the sharp threshold \(c=16\) as an iff statement.

Two related published research results concern different, **four-dimensional** smooth Cayley families: the complete two-parameter height-one tetrahedral frusta \(P_{a,b}\), and the product-fiber family \(R_{2,c}\). Their cubic numerator real-rootedness theorems do not imply this five-dimensional **quartic** case: changing the fiber from a tetrahedron to a four-simplex changes both the polynomial degree and discriminant. Another published result on \(Q_{r,c}\) determines its *eventual ordinary Ehrhart coefficient signs*, but not numerator-root geometry or the exact smallest five-dimensional sign threshold. In particular, a result about ordinary Ehrhart coefficients does not logically imply real-rootedness of its series numerator.

Ferroni, *Unimodality shenanigans in Ehrhart theory* (2026), studies smooth Cayley sums of **rectangular-prism fibers** and gives counterexamples to general unimodality, which shows that smooth Cayley structure alone does not yield a universal real-rootedness theorem. Width-asymptotic and Cartesian-product results also do not automatically cover the present nonproduct width-one family.

## Limitations
The theorem applies only to the one-parameter, unit-height, homothetic four-simplex frusta \(Q_c\). It does not claim the analogous assertion for arbitrary positive pairs of four-simplex layer sizes, for all smooth five-dimensional seven-facet polytopes, or in dimensions six and above. The numerical lattice-count checks are supplementary and not proofs of an infinite statement. The exact discriminant identity is reproducible using SymPy. Prior-art comparisons included the relevant manuscript, published overlapping records, and targeted database searches, but cannot exclude unindexed equivalent formulations. No independent mathematical audit has been performed.

## References
1. F. Liu, J. Tang, S. Tao, Z. Zhang, *Ehrhart positivity of smooth polytopes with few facets*, arXiv:2610.27819, first public 2026-10-20, especially Proposition 5.1 and Theorem 5.2. https://arxiv.org/abs/2610.27819
2. L. Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513, first public 2026-09-09, Sections 1–3. https://arxiv.org/abs/2609.10513
3. *Real-rooted Ehrhart numerators of height-one tetrahedral Cayley frusta*, published mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-real-rooted-ehrhart-numerators-of-height-one-tetrahedral-cayley--09f6ec741063
4. *Sharp Ehrhart root and coefficient transitions in smooth four-dimensional Cayley polytopes*, published mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-ehrhart-root-and-coefficient-transitions-in-smooth-four-di--7f5f9bc91987
5. *The complete eventual Ehrhart sign spectrum at the minimal smooth facet threshold*, published mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-complete-eventual-ehrhart-sign-spectrum-at-the-minimal-smoot--c97e66b91125
