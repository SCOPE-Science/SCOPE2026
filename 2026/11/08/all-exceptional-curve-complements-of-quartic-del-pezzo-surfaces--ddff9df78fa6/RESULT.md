# A nonsplit full quartic del Pezzo surface over the three-element field

## Finding
Let \(X\) be a smooth degree-four del Pezzo surface over \(\mathbb F_q\), and \(D\) the reduced union of its sixteen geometric exceptional curves. Then \(X(\mathbb F_q)\subset D\), equivalently \((X\setminus D)(\mathbb F_q)=\varnothing\), is possible **if and only if** \(q=3\) or \(q=5\). The \(q=5\) split example is classical (Hirschfeld, as quoted by Knecht–Reyes). The further, nonsplit \(q=3\) example is explicit: blow up \(\mathbb P^2_{\mathbb F_3}\) at one rational point and two degree-two closed points whose five geometric points are listed below. The resulting exceptional-boundary complement has no rational points. **The explicit nonsplit \(\mathbb F_3\) realization and the resulting completed existence dichotomy are the new contribution assessed here.**

The general sixteen-curve-complement zeta identity and the Weyl-group profile table were established independently in the earlier published result *Frobenius zeta formula and fifteen incidence profiles for the sixteen-line complement of a quartic del Pezzo surface* (2026-11-08, `2026/11/8/SCOPE-frobenius-zeta-formula-and-fifteen-incidence-profiles-for-the-si--51ccb894891f`, published Resultary record). That paper treats odd characteristic and gives the corresponding incidence formula for every extension field. Those zeta and first-field formulas, including the odd-characteristic eighteen-class parametrization, are **not claimed as new here**. The argument below verifies the class-based zero restriction also in even characteristic, without claiming an otherwise new general zeta classification.

## Scope and normalization
Exceptional curves mean the sixteen geometric \((-1)\)-curves, including those not individually defined over the base field. A rational point lying at a node with conjugate local branches still belongs to \(D\). The assertion is existence of at least one smooth surface over the specified field, not realizability of every abstract Weyl type in every small field. The ground characteristic may be two.

## Proof
**The universal necessary zero test.** Over an algebraic closure a smooth quartic del Pezzo surface is the blow-up of \(\mathbb P^2\) at five points in general position. Its exceptional curves are \(E_i\) for each point, \(L_{ij}\) for each pair, and the conic transform \(C\). They form a triangle-free incidence graph with sixteen vertices, forty edges and eighty local branches. Frobenius acts through the 1920-element even signed-permutation Weyl group \(W(D_5)\), in all characteristics. Let \(m(g)\) be the number of fixed curves, \(a(g)\) the number of intersections fixed with both component branches individually fixed, \(b(g)\) the number of intersections fixed with the branches transposed, and \(\tau(g)\) the trace of Frobenius on the six-dimensional geometric Picard group. The Weil point count on the ambient smooth rational surface and inclusion–exclusion at the ordinary nodes give
\[
 \#(X\setminus D)(\mathbb F_q)=q^2+\tau(g)q+1-m(g)(q+1)+a(g)-b(g).
\]
This is the previously published incidence formula in odd characteristic, with the same elementary geometric proof valid in characteristic two: the curves and intersections remain smooth and transverse, and the Picard trace formula holds for smooth rational surfaces over every finite field. Its node branch-swap correction is essential.

A finite complete census uses the sixteen even-parity signed vectors in \(\{\pm1\}^5\) and declares two curves adjacent when their vectors differ in four coordinates. The 120 coordinate permutations and sixteen even sign changes act on those curves and their forty incidence pairs. The exhaustive arithmetic source `dp4_verify.py` enumerates all 1920 elements and gives the fourteen distinct first-field expressions
\[
\begin{gathered}
 q^2-2q+1,\ q^2+1,\ q^2+q+1,\ q^2-2q-7,\ q^2+q-1,\\
 q^2+2q+1,\ (q-5)^2,\ q^2-4q+5,\ q^2-q+1,\ q^2-3,\\
 q^2-2q-3,\ q^2-1,\ q^2-q-1,\ q^2.
\end{gathered}
\]
The list contains all eighteen signed conjugacy types, some sharing the same first-field expression. For each polynomial \(q^2+Aq+B\), its value at \(q=6\) and derivative \(2q+A\) on \([6,\infty)\) are positive. Direct substitution at \(q=2,3,4,5\) yields zeros only for \(q=3\) with \(q^2-2q-3\) and for \(q=5\) with \((q-5)^2\). A formally negative value for a very small field means that the abstract Frobenius type cannot occur there; it does not affect this necessary condition.

**An explicit nonsplit surface at \(q=3\).** Work in \(\mathbb F_9=\mathbb F_3[\alpha]\) where \(\alpha^2=-1\). In \(\mathbb P^2(\mathbb F_9)\) put
\[
 P_0=[0:0:1],\quad A=[1:\alpha:0],\quad A^3=[1:-\alpha:0],\quad
 B=[1:1+\alpha:\alpha],\quad B^3=[1:1-\alpha:-\alpha].
\]
The superscript \(3\) means geometric Frobenius applied coordinatewise. The set consists of one rational point and two Frobenius-conjugate pairs. Every determinant of three distinct listed projective vectors is nonzero in \(\mathbb F_9\); all ten determinants are checked exactly by the self-contained script `dp4_verify.py`, using arithmetic modulo \(\alpha^2+1\) and modulo 3. Hence the points are in general position and their blow-up \(X/\mathbb F_3\) is a smooth degree-four del Pezzo surface. Frobenius has signed Weyl type \((1,2,2)\) with positive cycles. The displayed incidence formula yields
\[
 \#(X\setminus D)(\mathbb F_3)=3^2-2(3)-3=0.
\]
The same count can be checked geometrically: \(X(\mathbb F_3)\) has 16 points; four individually rational exceptional curves contribute fourteen boundary points after correcting their two mutual intersections, and two further rational nodes have conjugate branches. Thus all sixteen rational points lie on \(D\).

**The classical split realization at \(q=5\).** Pick five of the six rational points on a smooth \(\mathbb F_5\)-conic and blow up. No three lie on a line. Frobenius acts trivially on the exceptional configuration and the complement has \((5-5)^2=0\) rational points. This case was previously known and serves only to close the necessary-and-sufficient statement.

## Verification and limits
`dp4_verify.py` is an unchanged, dependency-free exact verifier. It enumerates the complete finite Weyl group, validates the sixteen-curve/forty-node/eighty-branch model, and certifies the ten projective determinants for the explicit \(\mathbb F_9\) arc. The finite Weyl census is exhaustive because the group has exactly 1920 elements; by contrast, finite experiments over isolated fields would not prove the all-field assertion. The proof does not assert realization of every abstract class over every field, and it makes no independent originality claim for the general zeta formula or for the split five-element-field case. Historical priority of the explicit nonsplit configuration remains qualified by possible older finite-geometry classification tables.

## References
- *Frobenius zeta formula and fifteen incidence profiles for the sixteen-line complement of a quartic del Pezzo surface*, published research record `2026/11/8/SCOPE-frobenius-zeta-formula-and-fifteen-incidence-profiles-for-the-si--51ccb894891f`, especially the complete Weyl profile table and all-extension incidence formula.
- A. Knecht and K. Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields*, arXiv:1510.04621 (2015), introduction reporting Hirschfeld's classical split quartic formula.
- B. Banwait, F. Fité and D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, arXiv:1606.00300 (2016), Picard-trace results.
- S. Rybakov, *Zeta Functions of Conic Bundles and Del Pezzo Surfaces of Degree 4 over Finite Fields*, Moscow Mathematical Journal 5 (2005), complete-surface zeta functions.
