# The complete rational line-incidence spectrum of the Fermat cubic surface

## Finding
Let \(q\) be any prime power with \(\operatorname{char}\mathbb F_q\ne3\), and let
\[
X/\mathbb F_q:\quad x_0^3+x_1^3+x_2^3+x_3^3=0\subset\mathbb P^3.
\]
For \(j\in\{0,1,2,3\}\), let \(N_j(q)\) count those \(P\in X(\mathbb F_q)\) lying on exactly \(j\) of the **27 geometric lines** on \(X_{\overline{\mathbb F}_q}\), whether or not the individual lines are defined over \(\mathbb F_q\). Then the complete spectrum \((N_0,N_1,N_2,N_3)\) is:

| Field condition | \(N_0\) | \(N_1\) | \(N_2\) | \(N_3\) |
| --- | --- | --- | --- | --- |
| \(q\equiv1\pmod3\), odd characteristic | \((q-7)(q-13)\) | \(27(q-7)\) | \(81\) | \(18\) |
| \(q\equiv1\pmod3\), characteristic \(2\) | \((q-4)(q-16)\) | \(27(q-4)\) | \(0\) | \(45\) |
| \(q\equiv2\pmod3\), odd characteristic | \((q-1)^2\) | \(3(q-3)\) | \(3\) | \(6\) |
| \(q\equiv2\pmod3\), characteristic \(2\) | \(q(q-2)\) | \(3(q-2)\) | \(0\) | \(7\) |

In particular, every rational point of \(X\) lies on some geometric line if and only if
\[
\boxed{q\in\{2,4,7,13,16\}.}
\]
The arithmetic set and full four-level incidence spectrum, rather than the classical existence of the 27 lines, are the finding.

## Assumptions and scope
All statements concern finite fields \(\mathbb F_q\) of characteristic other than \(3\), and every possible prime-power \(q\) in that range. A line is a geometric projective line contained in the base change of \(X\); incidence is tested over the algebraic closure, even for an \(\mathbb F_q\)-rational point. No characteristic-three statement is asserted: there the equation is a triple hyperplane rather than a smooth cubic surface.

## Proof
**1. The 27 lines.** The partial derivatives of the defining form are \(3x_i^2\), so \(X\) is smooth under the stated hypothesis. Let \(\mu_3\) be the three cube roots of unity in the algebraic closure. For each of the three pair partitions
\[
(01|23),\qquad(02|13),\qquad(03|12),
\]
and each \((\alpha,\beta)\in\mu_3^2\), impose \(x_i+\alpha x_j=x_k+\beta x_l=0\) for the selected ordered pairs \((ij|kl)\). These are 27 distinct contained lines. They exhaust the geometric lines: a smooth cubic surface has 27 geometric lines (equivalently, one can use the classical line configuration), including in characteristic two.

**2. Fully split case.** If \(q\equiv1\pmod3\), then \(\mu_3\subset\mathbb F_q\) and all 27 lines are rational. For a fixed pair partition, the nine lines have exactly six triple concurrence points: fixing the first ratio and varying the second gives three points on its first coordinate-pair axis, and vice versa. Across the three partitions there are 18 distinct such points. Lines from two different partitions meet if and only if a single equality among their cube-root coefficients holds. For instance, a line with \(x_0+\alpha x_1=x_2+\beta x_3=0\) and a line with \(x_0+\gamma x_2=x_1+\delta x_3=0\) meet exactly when \(\alpha\delta=\beta\gamma\), at
\[
P=(\alpha\delta:-\delta:-\beta:1).
\]
Every one of the nine lines in the first partition meets exactly three in the second, giving 27 meeting pairs for each choice of two partitions and 81 pairs altogether. The displayed point is on a line of the third partition precisely when \(-1\in\mu_3\), which for characteristic different from three means characteristic two. Such cross-partition intersection points have all four coordinates nonzero and are disjoint from the 18 coordinate-pair concurrency points.

In odd characteristic, the cross-partition points are 81 distinct ordinary double intersections; the 18 coordinate-pair points are triple intersections. In characteristic two, each cross-partition meeting is completed by exactly one line of the third partition; every resulting triple point accounts for three meeting pairs, yielding 27 additional triple points and no double intersections. Together with the 18 coordinate-pair points, there are exactly 45 triple points. No point can lie on four lines because all lines through a point are contained in its tangent-plane cubic section.

It remains to count rational points of \(X\). A concrete disjoint six among the 27 lines is obtained by choosing a primitive cube root \(\zeta\) and taking the triples \((M,i,j)\)
\[
(0,0,0),(0,1,1),(0,2,2),(1,0,1),(1,1,2),(1,2,0),
\]
where \(M=0,1\) denotes respectively the first or second pair partition and the coefficients are \((\zeta^i,\zeta^j)\). The same intersection criterion verifies that these six lines are pairwise skew. Contracting them gives a degree-nine del Pezzo surface over \(\mathbb F_q\), necessarily \(\mathbb P^2\), since finite fields have trivial Brauer group. The six contraction centers are distinct rational points. Thus
\[
\#X(\mathbb F_q)=q^2+q+1+6q=q^2+7q+1.
\]
The number \(N_1\) follows from the 27 lines' \(27(q+1)\) total rational-point incidences, after subtracting two incidences per double point and three per triple point. Subtracting \(N_1+N_2+N_3\) from \(\#X(\mathbb F_q)\) yields the first two rows.

**3. Nonsplit case.** If \(q\equiv2\pmod3\), the cube map is a bijection on \(\mathbb F_q\), so counting nonzero vectors on \(X\) by solving uniquely for the last coordinate gives
\[
\#X(\mathbb F_q)=(q^3-1)/(q-1)=q^2+q+1.
\]
Frobenius sends a cube root \(\alpha\) to \(\alpha^{-1}\), hence permutes the nine lines of each partition by \((\alpha,\beta)\mapsto(\alpha^{-1},\beta^{-1})\). Exactly the three \((1,1)\)-lines are individually rational. If a rational point lies on any nonrational line \(L\), it lies on both \(L\) and its Frobenius conjugate. Two lines from one partition can meet only when they share one coefficient; for a nonrational conjugate pair this means one coefficient is \(1\). Their intersection is a coordinate-pair point already lying on the \((1,1)\)-line of that partition. Therefore the rational points on the geometric line union are *exactly* the rational points on those three rational lines.

On each of the three rational lines there are two distinct rational coordinate-pair points lying on two further conjugate geometric lines; these are six triple points. The three rational lines have three distinct pairwise intersections in odd characteristic, each of multiplicity two. In characteristic two their three pairwise intersections coincide in one more triple point. Consequently the number of line-covered points is \(3(q+1)-3=3q\) in odd characteristic and \(3(q+1)-2=3q+1\) in characteristic two. Removing the specified triple and double points gives the values of \(N_1,N_2,N_3\); subtracting the line-covered count from \(q^2+q+1\) gives \(N_0\).

**4. Vanishing classification.** In the split, odd case, \((q-7)(q-13)=0\) precisely at \(q=7,13\). In split characteristic two, \((q-4)(q-16)=0\) precisely at \(q=4,16\). In nonsplit odd characteristic, \((q-1)^2>0\). In nonsplit characteristic two, \(q(q-2)=0\) precisely at \(q=2\). These cases exhaust the prime powers of characteristic different from three.

## Verification
`verify_point_spectrum.py` independently enumerates normalized projective points, tests the cubic equation, and calculates the number of containing *geometric* lines from pairwise cube-root equations, including cube roots not in the base field. Its exact results agree with the table over fields of orders \(2,4,5,7,8,11,13,16,19,31\).

`verify_line_geometry.py` separately constructs all 27 lines parametrically in characteristics seven and two, counts all projective line incidences and meeting pairs, checks the double/triple intersection types, and tests the six explicitly given skew lines. It confirms 135 meeting pairs, the \((81,18)\) double/triple distribution in characteristic seven, and 45 triple points in characteristic two. These finite tests illustrate and independently check critical steps; the universal quantifiers rest on the preceding symbolic argument.

Run either file with Python 3 using only its standard library. These two scripts and this manuscript constitute the full proof data; no historical artifacts or external datasets are required for replay.

## Relationship to prior work
The explicit 27-line description is classical and appears in Movasati's 2022 study of cubic-surface lines. McKean's 2021 paper studies the possible numbers of rational lines and their arithmetic, but not the four-level rational *point*-incidence spectrum. Betten, Hirschfeld, and Karaoglu classify 27-line cubic surfaces over \(\mathbb F_{13}\), identifying the equianharmonic surface and its known 18 Eckardt points; the special \(q=13\) value is therefore strongly anticipated by their work. Brosowsky, Page, Ryan, and Smith establish the geometry and 45 star points of the characteristic-two extremal cubic, giving important input for the characteristic-two row. These ingredients are not claimed as new.

The added statement is a single exact all-prime-power classification of the \(0,1,2,3\) geometric-line incidences for rational points, including both Frobenius-nonsplit classes and the precise exceptional fields for total coverage. Published individual-field tables and general line counts are not asserted to have been unknown. The general rationality work of Massarenti (2026) treats rational parametrizations of even-dimensional Fermat cubics rather than this incidence spectrum.

## Limitations
The result applies to this one Fermat cubic surface, not to all smooth cubic surfaces, and excludes characteristic three. It does not classify cubic surfaces up to projectivity or assert that the classification is independent of earlier unindexed computations. The key combinatorics are elementary consequences of the classical 27-line equations; the risk that an equivalent incidence formula has appeared in older finite-geometry literature remains. The reported checks are mathematical self-review only; no independent audit or historical-priority certification has been performed.

## References
1. A. Betten, J. W. P. Hirschfeld, F. Karaoglu, *Classification of cubic surfaces with twenty-seven lines over the finite field of order thirteen*, European Journal of Mathematics, published September 27, 2017, DOI 10.1007/s40879-017-0182-0. https://link.springer.com/article/10.1007/s40879-017-0182-0
2. S. McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217, first public January 20, 2021. https://arxiv.org/abs/2101.08217
3. A. Brosowsky, J. Page, T. Ryan, K. E. Smith, *Geometry of Smooth Extremal Surfaces*, arXiv:2110.15908, first public October 29, 2021. https://arxiv.org/html/2110.15908v1
4. H. Movasati, *Computing the lines of a smooth cubic surface*, arXiv:2210.13947, first public October 25, 2022. https://arxiv.org/abs/2210.13947
5. A. Massarenti, *Rational points on even-dimensional Fermat cubics*, Trans. London Math. Soc., first published March 20, 2026, DOI 10.1112/tlm3.70028. https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/tlm3.70028
