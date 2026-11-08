# Arithmetic descent of sextactic conics and trisecants of the Fermat cubic

## Finding
Let \(q\) be a prime power of characteristic \(p\ge5\). Over \(\mathbb F_q\), let \(E\subset\mathbb P^2\) be the smooth Fermat cubic
\[
E:\quad x^3+y^3+z^3=0,
\]
with group-law origin \(O=[1:-1:0]\). Let \(S\) denote the reduced geometric set of sextactic points: points admitting an irreducible conic with intersection multiplicity six at that point. Let \(L\) denote the reduced geometric set of projective lines each containing three distinct members of \(S\). Then \(\#S=27\) and \(\#L=81\) over the algebraic closure, in every indicated characteristic.

The Frobenius cycle decomposition, rational-point count, and rational-incidence count are given by the complete table below. Here \(1^a2^b3^c\) denotes \(a\) fixed points, \(b\) two-cycles and \(c\) three-cycles in the corresponding finite geometric set; \(I_q\) is the number of incident pairs \((P,\ell)\in S(\mathbb F_q)\times L(\mathbb F_q)\) with \(P\in\ell\).

| Arithmetic condition | Frobenius on \(S\) | Frobenius on \(L\) | \(\#S(\mathbb F_q)\) | \(\#L(\mathbb F_q)\) | \(I_q\) |
|---|---|---|---:|---:|---:|
| \(q\equiv1\pmod3\) and \(2^{(q-1)/3}=1\) | \(1^{27}\) | \(1^{81}\) | 27 | 81 | 243 |
| \(q\equiv1\pmod3\) and \(2^{(q-1)/3}\ne1\) | \(3^9\) | \(1^9 3^{24}\) | 0 | 9 | 0 |
| \(q\equiv2\pmod3\) | \(1^3 2^{12}\) | \(1^9 2^{36}\) | 3 | 9 | 9 |

In the second row, each of the nine rational trisecants meets \(E\) in a Frobenius orbit of three nonrational sextactic points. In the third row, each of the nine rational trisecants contains exactly one rational sextactic point, and each of the three rational sextactic points lies on three rational trisecants. In the first row, every line has three rational sextactic points. The number of \(\mathbb F_q\)-rational irreducible hyperosculating conics equals \(\#S(\mathbb F_q)\) in the table.


**The six-point conics.** Let \(\mathcal C\) denote the reduced collection of all plane conics passing through exactly six *distinct* geometric sextactic points (equivalently, through at least six). It has \(8244\) members, of which \(2268\) are reducible (unions of two distinct geometric trisecants) and \(5976\) are geometrically smooth. The complete arithmetic descent is:

| Arithmetic condition (same order as above) | Frobenius on all \(8244\) conics | On reducible \(2268\) conics | On smooth \(5976\) conics | Rational reducible | Rational smooth |
|---|---|---|---|---:|---:|
| \(q\equiv1\), \(2\) a cube | \(1^{8244}\) | \(1^{2268}\) | \(1^{5976}\) | 2268 | 5976 |
| \(q\equiv1\), \(2\) a noncube | \(1^{36}3^{2736}\) | \(1^{36}3^{744}\) | \(3^{1992}\) | 36 | **0** |
| \(q\equiv2\) | \(1^{76}2^{4084}\) | \(1^{54}2^{1107}\) | \(1^{22}2^{2977}\) | 54 | **22** |

All congruences in this table are modulo three. In particular, when \(q\equiv1\pmod3\) but \(2\) is not a cube, **every rational conic through six distinct sextactic points is reducible**; when \(q\equiv2\pmod3\), precisely 22 of these conics are geometrically smooth and rational. In each case the associated finite étale conic-parameter schemes have zeta functions obtained directly from the displayed cycles: for instance, in the noncube case the smooth-conic scheme has \(Z(\mathcal C_{\mathrm{sm}},T)=(1-T^3)^{-1992}\), and in the involution case it has \(Z(\mathcal C_{\mathrm{sm}},T)=(1-T)^{-22}(1-T^2)^{-2977}\). The displayed cycle table similarly determines the zeta functions of the full and reducible conic configurations over all extensions.

Equivalently, the zeta functions of the two reduced finite étale schemes, defined by \(Z(A,T)=\exp(\sum_{n\ge1}\#A(\mathbb F_{q^n})T^n/n)\), are:
\[
\begin{array}{c|c|c}
\text{condition}&Z(S,T)&Z(L,T)\\\hline
q\equiv1,\ 2\text{ a cube}&(1-T)^{-27}&(1-T)^{-81}\\
q\equiv1,\ 2\text{ a noncube}&(1-T^3)^{-9}&(1-T)^{-9}(1-T^3)^{-24}\\
q\equiv2&(1-T)^{-3}(1-T^2)^{-12}&(1-T)^{-9}(1-T^2)^{-36}
\end{array}
\]
with congruences modulo three. These formulas give exact counts in every extension \(\mathbb F_{q^n}\).

## Assumptions and scope
The ambient field is a finite field of characteristic at least five. All geometric points and lines are taken after extension to an algebraic closure, but rationality is always relative to the specified \(\mathbb F_q\). A line counts as rational when its projective coefficient triple is Frobenius-stable, even if its three geometric intersection points are not individually rational. An irreducible hyperosculating conic is one whose scheme-theoretic intersection divisor with \(E\) is six times a point. A six-point conic is a different object: it contains six *distinct* sextactic points, and may be smooth or geometrically reducible. No claim is made for characteristics two and three.

## Proof
**(1) Sextactic points and torsion.** The plane embedding satisfies \(\mathcal O_E(1)\simeq\mathcal O_E(3O)\), since \(O\) is a rational flex. Therefore \(\mathcal O_E(2)\simeq\mathcal O_E(6O)\). Restriction of plane quadrics induces an isomorphism between the six-dimensional space of homogeneous quadratic forms and \(H^0(E,\mathcal O_E(6O))\): injectivity holds since no conic contains the irreducible cubic \(E\), and both spaces have dimension six by Riemann--Roch. A conic intersects \(E\) in \(6P\) exactly when \(6P=O\) in the elliptic group law. If \(3P=O\), such a conic is the doubled flex tangent and is reducible. Conversely, if \(6P=O\) but \(3P\ne O\), any reducible conic with divisor \(6P\) would consist of two lines each meeting \(E\) in \(3P\), forcing \(3P=O\), a contradiction. Thus \(S=E[6]\setminus E[3]\). Because \(p\nmid6\), the canonical product decomposition is \(E[6]\simeq E[2]\oplus E[3]\) and \(S\simeq(E[2]\setminus\{O\})\times E[3]\). Hence \(\#S=3\cdot9=27\). The unique conic attached to each point descends exactly when that point does, proving the claim about rational hyperosculating conics.

**(2) The 81 lines.** On a plane cubic with origin at a flex, distinct points \(P_1,P_2,P_3\) are collinear exactly when \(P_1+P_2+P_3=O\). The three nonzero elements of \(E[2]\) sum to zero, and no three nonzero elements of \(E[2]\) with repetition sum to zero. Thus a line through three members of \(S\) contains precisely one point in each of the three \(E[2]\)-cosets. Label the nonzero \(2\)-torsion points \(T_1,T_2,T_3\). Every such line is uniquely represented by
\[
\{T_1+B_1,\ T_2+B_2,\ T_3+B_3\},\qquad B_i\in E[3],\quad B_1+B_2+B_3=O.
\]
There are exactly \(9^2=81\) solutions. These define distinct lines: a line cannot contain four distinct points of a smooth plane cubic by Bézout. This argument also establishes the configuration without requiring the characteristic-zero coordinates of its previously known form.

**(3) Rational torsion and Frobenius.** The projective linear change of coordinates on \(E\), given on \(x+y\ne0\) by
\[
X=-12z/(x+y),\qquad Y=36(x-y)/(x+y),
\]
gives \(Y^2=X^3-432\), with \(O\) at infinity. The three nonidentity \(2\)-torsion points correspond to the roots of \(X^3=432=2^4\cdot3^3\). If \(q\equiv1\pmod3\), Frobenius is the identity on \(E[2]\) exactly when \(2\) is a cube, and otherwise is a three-cycle on its nonzero points. If \(q\equiv2\pmod3\), Frobenius fixes one nonzero \(2\)-torsion point and exchanges the other two.

The nine \(3\)-torsion points are precisely the nine flexes of \(E\), lying on its coordinate axes with coordinate ratios given by cube roots of unity. For \(q\equiv1\pmod3\), Frobenius fixes all nine. For \(q\equiv2\pmod3\), it is an involution with exactly three fixed points (and three transposed pairs). These statements use only the separability of torsion and are valid for every prime power of the allowed characteristic.

**(4) Frobenius cycles of sextactic points.** On \(S\simeq(E[2]\setminus\{O\})\times E[3]\), Frobenius acts diagonally. If both torsion groups split, all 27 points are fixed. With a three-cycle on the nonzero \(2\)-torsion and trivial action on \(E[3]\), the 27 points form nine three-cycles. With a transposition on nonzero \(2\)-torsion and the indicated involution on \(E[3]\), precisely \(1\cdot3=3\) points are fixed, and the other 24 points form twelve two-cycles.

**(5) Frobenius cycles of trisecants.** Use the representation in (2). In the fully split case all 81 lines are fixed. In the noncube case with \(q\equiv1\), the nonzero \(T_i\) are cycled while every \(B_i\) is fixed. A line is invariant exactly when \(B_1=B_2=B_3\), which gives nine fixed lines; all other 72 lines lie in 24 three-cycles.

When \(q\equiv2\), index so Frobenius fixes \(T_1\) and swaps \(T_2,T_3\). Let \(F\) denote its involution on \(E[3]\). A line is invariant precisely when \(B_3=F(B_2)\) and \(B_1=-B_2-F(B_2)\). Every one of the nine choices of \(B_2\) gives such a line, with \(B_1\) automatically fixed by \(F\). The remaining 72 lines lie in 36 two-cycles because the second iterate fixes all geometric torsion. Exactly one point on each fixed line lies in the Frobenius-fixed \(T_1\)-coset. Moreover \(B_2\mapsto-B_2-F(B_2)\) maps onto the fixed order-three subgroup of \(E[3]\), with fibers of size three: \(F\) has \(+1\) and \(-1\) eigenspaces of dimension one over \(\mathbb F_3\). Hence each of the three rational sextactic points lies on precisely three rational lines. This proves the incidence assertions.


**(6) Six-point conics and exact fixed-point counts.** A six-element subset \(D\subset S\) is cut out by a unique plane conic precisely when its sum in \(E[6]\) is \(O\): indeed, \(D\sim6O\) is the exact criterion for a section of \(\mathcal O_E(6O)\), and restriction of plane conics is an isomorphism by (1). Every resulting conic contains exactly those six distinct points, by Bézout, so different eligible subsets define different conics. It is reducible precisely when its subset admits a partition into two collinear triples, equivalently into two three-subsets with group sum \(O\). This is a complete, characteristic-independent finite combinatorial criterion. An exhaustive enumeration of all \(\binom{27}{6}=296010\) subsets gives \(8244\) with total sum zero and exactly \(2268\) with a zero-sum triple. The self-contained script `verify_conics.py` implements the four modular group-coordinate sums and examines every combination and triple; these are exhaustive finite combinatorial computations, not statistical samples or extrapolation. The geometric totals agree with Szemberg--Szpond.

When Frobenius is trivial on \(S\), all the conics are rational. When Frobenius cycles the three nonzero \(2\)-torsion cosets, its 27 sextactic points form nine three-cycles. Each three-cycle is itself a collinear triple: its group sum is \(T_1+T_2+T_3+3B=O\). Any stable six-subset must be a union of exactly two of the nine cycles, giving \(\binom92=36\) invariant conics; all are reducible unions of two rational trisecants. Thus none of the \(5976\) smooth six-point conics is rational in this case.

In the remaining case Frobenius is an involution with exactly three fixed sextactic points and twelve two-cycles. Identify the fixed part of \(E[3]\) with \(\mathbb F_3\), and choose eigencoordinates \((u,v)\in\mathbb F_3^2\) so that Frobenius sends \((u,v)\mapsto(u,-v)\). The two-cycles consist of three pairs of type A, each inside the fixed nonzero \(2\)-torsion coset and indexed by \(u\in\mathbb F_3\), and nine pairs of type B, between the other two cosets and indexed by \((u,v)\in\mathbb F_3^2\). Their group sums are respectively \((O,2u)\) and \((T_1,2u)\). A stable six-subset contains either three two-cycles or two fixed points plus two two-cycles. For three cycles, its total \(2\)-primary part vanishes exactly when it contains zero or two B pairs. Selecting all three A pairs contributes one; selecting one A and two B with total three-primary sum zero contributes \(3\cdot12=36\). This yields 37. With two fixed points, selecting two A pairs contributes three, and selecting two B pairs contributes \(3\cdot12=36\), giving 39. The number \(12\) is the number of unordered distinct pairs of the nine B labels whose two \(u\)-coordinates have any prescribed sum: three same-\(u\) pairs and nine cross-\(u\) pairs. Hence exactly \(37+39=76\) conics are rational.

To count reducible rational conics without presupposing geometric smoothness, use the 81 trisecants from (2). A reducible six-point conic is an unordered pair of trisecants with disjoint sextactic triples. In the involution case, nine individual lines are rational and 36 pairs of lines are Frobenius-exchanged. Each rational line contains exactly one rational sextactic point; the nine rational lines fall into three groups of three through those three points. Two distinct rational lines cannot share a nonrational sextactic point, since then their common point and its conjugate would give two distinct common points. Thus \(\binom92-3\binom32=27\) unordered pairs of rational lines have disjoint sextactic triples. Among the 36 nonrational line-pairs exchanged by Frobenius, precisely nine pairs share a sextactic point: the shared point must be rational, and each of the three rational sextactic points lies on six nonrational lines grouped into three exchanged pairs. The other 27 pairs are disjoint. Consequently exactly \(27+27=54\) reducible conics are rational, and \(76-54=22\) rational conics are smooth.

Because Frobenius has order at most three on the complete torsion configuration, the remaining conics have orbit lengths three in the cyclic case, or two in the involution case. Subtracting the fixed counts from the known geometric totals gives every cycle multiplicity in the conic table.

**(7) Zeta functions.** For a finite reduced scheme, one Frobenius orbit of length \(d\) contributes \((1-T^d)^{-1}\) to its zeta function. Applying this to the cycle decompositions in (4)--(5) gives the displayed expressions, with no limit on the extension degree.

## Verification
The standalone program `verify.py` uses exact arithmetic in three finite fields and independently constructs the torsion points, trisecant lines, Frobenius permutations, and rational incidence; it does not input the predicted line coordinates or the 81-line list. The three cases are \(p=5\) (quadratic splitting field), \(p=7\) (cubic splitting field), and \(p=31\) (already split). It checks the three distinct Frobenius types and prints `VERIFY_SEXTACTIC_LINES_OK` if and only if all checks succeed. These finite-field computations cross-check the group-theoretic argument; they are not the proof of its universal quantifiers. The second program `verify_conics.py` exhaustively enumerates all 296010 six-subsets of the *fixed* 27-element abstract torsion configuration and its three universal Frobenius types, certifying the universal finite group-combinatorics used in (6). It verifies 8244 six-point conics, 2268 reducible conics, and every Frobenius cycle decomposition in the new table. This is exhaustive finite reasoning within the universal group model, not an extrapolation from sampled finite fields.

Run with `python verify.py` and `python verify_conics.py` using Python 3 and the standard library. The proof itself depends only on the geometric group law, separable torsion, and the displayed explicit Weierstrass transformation.

## Relationship to prior work
Szemberg--Szpond (first preprint November 1, 2022, arXiv:2211.00494, especially Remark 4.1 and Lemma 4.8) identified the 27 sextactic points with non-3-primary six-torsion and determined the 81-line configuration over \(\mathbb C\). Those numbers and their geometric incidence are not claimed as new. Merta--Zięba (arXiv:2406.13802) analyze related tangent-line and conic configurations, including the Weierstrass model. Moe--Toft (arXiv:2412.16993) give further explicit line-grid descriptions, also over \(\mathbb C\). The contribution here is the uniform finite-field Frobenius classification of the complete sextactic point, trisecant and six-point-conic configurations, including the new rational smooth-versus-reducible conic counts, the rational incidence profiles, and the finite-étale zeta functions. No inspected cited source states those arithmetic classifications. Earlier equivalent arithmetic descriptions remain a possible priority risk.

## Limitations
The statement concerns the Fermat plane cubic with the specified rational flex, not arbitrary twists or other plane cubics. The finite étale zeta functions count the marked geometric points and lines, not the points of the complement of their union or the zeta function of the ambient curve. Small characteristics two and three are excluded because the separable six-torsion description and given Weierstrass model no longer apply. The proof does not classify the intersection singularities of the 81-line arrangement away from the sextactic points, nor the geometry of intersections among those six-point conics away from the Fermat cubic.

## References
1. T. Szemberg and J. Szpond, *Sextactic points on the Fermat cubic curve and arrangements of conics*, arXiv:2211.00494 (first posted 2022-11-01), Sections 2--4, in particular Remark 4.1 and Lemma 4.8. https://arxiv.org/abs/2211.00494
2. Ł. Merta and M. Zięba, *Sextactic and type-9 points on the Fermat cubic and associated objects*, arXiv:2406.13802 (first posted 2024-06-19), Sections 2--4. https://arxiv.org/abs/2406.13802
3. T. K. Moe and N. P. A. Toft, *The Fermat curves, arrangements of lines, and intersections of osculating curves*, arXiv:2412.16993 (first posted 2024-12-22), Section 3 and Remark 3.7. https://arxiv.org/abs/2412.16993
