# Four-variable collapse of the finite projective-plane incidence theories

## Finding
Let \(\Pi=(P,L,I)\) and \(\Pi'=(P',L',I')\) be arbitrary finite, nondegenerate projective planes of orders \(q,r\ge 2\). Regard them as relational structures on the disjoint union of points and lines, with unary predicates distinguishing the two sorts and binary incidence \(I(p,\ell)\) directed from points to lines. Let \(\mathrm{FO}^{k}\) mean counting-free first-order logic using at most \(k\) reusable variable names **in total**, without restricting quantifier depth.

Then
\[
 \Pi\equiv_{\mathrm{FO}^{k}}\Pi'\quad\text{for every }1\le k\le3,
\]
and, sharply,
\[
 \boxed{\Pi\equiv_{\mathrm{FO}^{4}}\Pi'\quad\Longleftrightarrow\quad(q=2\iff r=2).}
\]
Thus there is exactly **one** \(\mathrm{FO}^{k}\)-theory on finite projective planes for each \(k=1,2,3\), and exactly **two** for \(k=4\). In particular, **every** two finite projective planes of orders at least three satisfy the same four-variable sentences, even when their orders differ or one of them is non-Desarguesian. The Fano plane and every plane of larger order are distinguished by one explicit four-variable sentence. These are relative equivalence statements *within the projective-plane family*, not claims about defining that family among arbitrary structures.

## Assumptions and scope
A finite projective plane of order \(q\ge2\) has \(q^2+q+1\) points and as many lines; each line has \(q+1\) points, each point lies on \(q+1\) lines, two distinct points determine exactly one line, and two distinct lines meet at exactly one point. No Desarguesian or coordinatization hypothesis is used. Points and lines are different sorts, and incidence is the sole binary relation; no counting quantifiers, order, constants, or additional geometric predicates are present. If two-sorted syntax is preferred, the result holds with the same total budget of variable names: the one-sorted game strategy is stronger, and the separating sentence is well-sorted.

## Proof
**1. An augmented triple invariant.** For a tuple of at most four pebbled positions retain all equality, sort, and point-line incidence data. Also retain whether every triple of **pairwise distinct** pebbled points is collinear, and whether every triple of **pairwise distinct** pebbled lines is concurrent. The latter two properties are auxiliary strategy information, not atomic symbols in the signature. Call this the enhanced type. Equality and sorts make repeated positions harmless.

**2. Uniform extension lemma for orders at least three.** For any \(q,r\ge3\), any two enhanced-equivalent tuples of at most three elements in arbitrary projective planes of orders \(q\) and \(r\) admit **exactly the same possible enhanced types** when one arbitrary fourth element is added. It suffices by point-line duality to consider three distinct points, or two distinct points and a line. Configurations with repeated positions reduce to fewer distinct elements, and the at-most-two-element extension cases have all geometrically consistent incidences.

For three distinct points \(A,B,C\), if they are collinear, a fresh fourth point can lie on their line (\(q-2\ge1\) choices) or off it. A fresh line can meet all three (the unique common line), exactly one (\(q\) choices for each selected point), or none (\(q(q-2)\ge3\) choices), but cannot meet exactly two. If they are noncollinear, a fresh point can lie on any one of the three pair-lines (\(q-1\ge2\) choices per side), or on none (\((q-1)^2\ge4\) choices); it cannot lie on two different pair-lines without equalling a previously pebbled point. A fresh line can meet exactly two old points (one line for each pair), exactly one (\(q-1\ge2\) choices), or none (\((q-1)^2\ge4\) choices), but cannot meet all three. The dual statements treat three distinct lines. All these availability and nonavailability conditions depend only on the triple's enhanced type, not on the plane's order once the order is at least three.

For two distinct points \(A,B\) and a line \(L\), write \(J=AB\) for their unique joining line. A new **point** distinct from \(A,B\) is classified by its membership in \(J\) (the new collinearity bit) and in \(L\) (the incidence bit). When \(L=J\), a fresh point of \(J\) exists in \(q-1\ge2\) ways and a point outside \(J\) exists. When \(L\) contains exactly one of \(A,B\), \(J\cap L\) is that old point; fresh choices in \(J\setminus L\), \(L\setminus J\), and outside both exist, while a fresh point on both does not. When \(L\) contains neither, the unique intersection \(J\cap L\) is a fresh point, there are \(q-2\ge1\) further fresh points on \(J\setminus L\), \(q\ge3\) on \(L\setminus J\), and \(q(q-1)>0\) off both. These cases exhaust the possibilities.

A new **line** is determined, for the enhanced-type purpose, by equality with \(L\) and whether it contains each of \(A,B\): the only line through both is \(J\); apart from that, there are \(q\) lines through each one but not the other, and \(q(q-1)\) through neither. Excluding \(L\) removes at most one candidate from any category, leaving a candidate whenever the category is geometrically consistent, because \(q\ge3\). The mixed case with two distinct lines and one point follows by duality. This proves the lemma without assuming any coordinatization or transitivity of automorphism groups.

**3. Four-pebble equivalence.** Duplicator initially matches the empty tuple. Maintain equal enhanced types among the at most four occupied positions. Whenever a pebble moves, remove its old positions: at most three matched positions remain. The extension lemma supplies a matching new position of exactly the required enhanced type, regardless of which plane Spoiler plays in. The enhanced invariant in particular preserves all atomic formulas. Thus Duplicator wins arbitrarily many rounds, establishing \(\mathrm{FO}^{4}\)-equivalence of any two planes of orders at least three.

**4. Three-pebble equivalence including order two.** With at most two surviving positions, equality, sorts and incidences form a back-and-forth extension invariant in **every** plane of order at least two. For two distinct old points there is a line through both, a line through exactly either one, and a line through neither (the last count is \(q(q-1)>0\)); the dual holds for two lines. For one point and one line, fresh points or lines both incident and nonincident with the opposite-sort old object are available. New objects equal to an existing same-sort object are matched by equality. Hence Duplicator wins the unlimited three-pebble game in any pair of such planes.

**5. Explicit four-variable separator.** Use three line variables \(\ell,m,n\) and one point variable \(p\), reusing \(p\) in the innermost quantifier:
\[
\begin{aligned}
\varphi:=\exists\ell\,\exists m\,\exists p\;[&L(\ell)\wedge L(m)\wedge P(p)\wedge\ell\ne m\\
&\wedge\neg I(p,\ell)\wedge\neg I(p,m)\\
&\wedge\exists n\;[L(n)\wedge n\ne\ell\wedge n\ne m\wedge\neg I(p,n)\\
&\qquad\wedge\exists p\;(P(p)\wedge I(p,\ell)\wedge I(p,m)\wedge I(p,n))]].
\end{aligned}
\]
The displayed unary sort guards enforce the required point/line sorts also in the one-sorted presentation (and are redundant in strictly two-sorted syntax). The inner \(\exists p\) intentionally shadows the previously bound point name; the total variable budget is four. The sentence says that there exist distinct lines \(\ell,m\), a point \(p\) off both, and a *third* line \(n\) through their intersection but not through \(p\). The two old lines and the line joining their intersection to \(p\) are three distinct lines through the intersection. Thus \(\varphi\) is false when \(q=2\), because only three lines pass through each point, and true when \(q\ge3\), because there are at least four. This proves the sharp dichotomy.

## Verification
The standalone `verify.py` constructs the Desarguesian planes of orders \(2,3,4,5\) by exact field arithmetic, with \(\mathrm{GF}(4)\) constructed explicitly. It enumerates all 48 possible enhanced triple types in each example and their sets of possible enhanced quadruple types. It exhaustively tests all triples for orders two and three and reproducibly samples many triples for orders four and five, checking that extension sets are independent of the chosen representative of an enhanced triple type. The order-at-least-three models all yielded the same 410 quadruple types and the same 48-row extension catalogue; the Fano plane yielded 400 quadruple types, differing in eight triple-extension rows. The program independently evaluates the explicit four-variable separator and finds zero witnesses at order two, and positive numbers at orders three, four, and five. The verification log is in `verify.out`.

These finite tests corroborate the proof; they are **not** a proof of the universal statement for arbitrary finite planes (especially non-Desarguesian ones). The uniform extension lemma proved above supplies that step.

## Relationship to prior work
Grohe's 1998 survey *Finite Variable Logics in Descriptive Complexity Theory*, Proposition 2.1 and Example 6.8, proves counting **three-variable** equivalence for planes of the *same order* and discusses the corresponding complete counting theories; that result does not imply counting-free four-variable equivalence across different orders. Venema's *Points, Lines and Diamonds* studies two-sorted **modal** logic and proves completeness, decidability and complexity results, not the present fixed-variable first-order separation. Grohe and Otto's *Pebble Games and Linear Equations* studies general counting and counting-free pebble/linear-equation correspondences without a projective-plane-specific four-variable classification. Related work on definability of incidence graphs in the pure uncolored graph language concerns a different vocabulary and implication. The present theorem identifies the exact four-variable collapse across projective-plane orders, rather than establishing a general pebble-game correspondence.

## Limitations
Only ordinary counting-free first-order logic, total variable width at most four, and the point/line-sorted incidence vocabulary are treated. Counting quantifiers immediately see different plane cardinalities. At higher widths, further distinctions can arise; no classification is asserted there. The result is relative to the class of finite projective planes, not a first-order definition of that class. The local computations do not settle historical priority, and no independent mathematical validation has been performed. An unidentified earlier theorem on finite-variable equivalence of symmetric designs could imply the classification.

## References
1. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, initially submitted 2012-04-09; CSL 2012, DOI: 10.4230/LIPIcs.CSL.2012.289. https://arxiv.org/abs/1204.1990 and https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2012.289
2. Y. Venema, *Points, Lines and Diamonds: a Two-Sorted Modal Logic for Projective Planes*, Journal of Logic and Computation 9 (1999), 601–621, DOI: 10.1093/logcom/9.5.601. Open author copy: https://staff.science.uva.nl/y.venema/papers/vene-poin99.pdf
3. M. Grohe, *Finite Variable Logics in Descriptive Complexity Theory*, Bulletin of Symbolic Logic 4 (1998); survey dated October 1998, §2.1 and Example 6.8. Accessible scan: https://citeseerx.ist.psu.edu/document?doi=516ed34d23a6639367393f67be21c9b312b2db07&repid=rep1&type=pdf
