# Four-variable collapse across finite projective dimensions and the skew-line boundary

## Finding
For a prime power \(q\ge 2\) and an integer \(d\ge 0\), define \(\mathcal P(d,q)\) to be the point-only structure on the projective points of \(\operatorname{PG}(d,q)\), in the pure language with equality and the ternary collinearity relation \(C(a,b,c)\). Collinearity is true for a triple containing repeated points. There are **exactly five** counting-free \(\mathrm{FO}^{4}\)-theories among all \(\mathcal P(d,q)\), at unrestricted quantifier depth:

1. \(d=0\), for every \(q\).
2. \(d=1\) and \(q=2\).
3. \(d=1\) and \(q\ge 3\).
4. \(d\ge 2\) and \(q=2\).
5. \(d\ge 2\) and \(q\ge 3\).

In particular, for \(d,e\ge 2\),
\[
\mathcal P(d,q)\equiv_{\mathrm{FO}^{4}}\mathcal P(e,r)
\quad\Longleftrightarrow\quad (q=2\ \Longleftrightarrow\ r=2).
\]
This dimension-independent statement remains true if either or both dimension-two geometries are replaced by *arbitrary finite abstract projective planes*, including non-Desarguesian examples, with order in the same binary class (two versus at least three).

For any projective plane \(\Pi\) of order at least two and any \(\operatorname{PG}(d,q)\) with \(d\ge3\), five variables distinguish the two structures: the sentence saying that two projective lines are disjoint holds in the latter and fails in the former. Hence, whenever their four-variable theories agree, width **five is exactly the first width** at which projective dimension two can be separated from dimension at least three.

## Assumptions and scope
All spaces and planes are finite; field orders are prime powers at least two in \(\operatorname{PG}(d,q)\). Abstract finite projective planes need not be coordinatizable. The only nonlogical relation is ternary point collinearity; there are no line variables, scalar symbols, coordinate labels, constants, counting quantifiers, or built-in order. The definition of \(C\) includes coincident points: for distinct points it means they lie on one projective line. \(\mathrm{FO}^{k}\) uses at most \(k\) reusable variable names, without bounding quantifier depth.

The five-theory enumeration includes point spaces of dimension zero and projective lines of dimension one. In a line the collinearity predicate is universal, so a four-variable formula can see at most whether the universe contains one, two, three, or at least four points. Within the projective-line family this leaves two cases, of sizes three and at least four.

## Proof
**Extension-profile lemma.** Consider any finite projective space of dimension at least two, or any finite projective plane, with \(q+1\) points on each line, \(q\ge2\). For any ordered tuple of at most three stationary points, the set of possible atomic equality/collinearity patterns of a fourth point depends only on the stationary tuple's equality pattern, whether its three distinct entries are collinear, and whether \(q=2\).

To verify the lemma, discard duplicate stationary entries (which are retained in their named equality positions). With zero distinct anchors there is one generic pattern. With one anchor, there are two: equal and unequal. With two distinct anchors \(a,b\), there are four: equal to \(a\), equal to \(b\), on the line \(ab\) but distinct from both, or outside that line. The latter two exist because \(q-1\ge1\) and the dimension is at least two.

For three *distinct collinear* anchors \(a,b,c\), the patterns are equality with each of the three, a further point on their common line, or a point off that line. The fourth-on-line pattern occurs precisely when \(q+1\ge4\), i.e., \(q\ge3\). The off-line pattern always occurs.

For three *distinct noncollinear* anchors \(a,b,c\), the patterns are equality with any of the three; one additional point on each of the three pair-lines \(ab\), \(ac\), \(bc\); and a point on none of those lines. Each pair-line has \(q-1\ge1\) points besides the two anchors. The three pair-lines lie in a projective plane, and their union has \(3(q+1)-3=3q\) points. That plane has \(q^2+q+1\) points, leaving \((q-1)^2\ge1\) points off the union. Any higher-dimensional projective space contains this plane. Thus all seven patterns occur, for every \(q\ge2\). Atomic instances of \(C\) with repeated arguments are automatically true and introduce no extra patterns. This proves the lemma, including for abstract projective planes.

**Four-variable equivalence.** Given two geometries of dimension at least two on the same side of the split \(q=2\) versus \(q\ge3\), Duplicator maintains an equality-preserving correspondence of the at most four pebbled points that preserves every ternary collinearity atom. Upon a pebble move, remove its pair, leaving at most three stationary pairs. Their equality and collinearity types match. The extension-profile lemma supplies a matching choice for the moved pebble, regardless of which structure Spoiler plays in. The invariant therefore holds after arbitrarily many moves. The unrestricted four-pebble game characterizes counting-free \(\mathrm{FO}^{4}\)-equivalence; hence all geometries in each of the two dimension-at-least-two classes agree on every such sentence.

**Separation of the five classes.** A two-variable inequality sentence distinguishes dimension zero from every positive dimension. A three-variable sentence asserting three distinct noncollinear points distinguishes dimensions zero/one from dimensions at least two. On a projective line, the four-variable sentence asserting four distinct points separates \(q=2\) from \(q\ge3\). In every dimension at least two, the four-variable sentence asserting four distinct collinear points separates \(q=2\) from \(q\ge3\). These sentences jointly separate all five classes, so the preceding equivalence classification is complete.

**Sharp five-variable dimension boundary.** Let \(\operatorname{Distinct}_4(a,b,c,d)\) abbreviate the conjunction of the six pairwise inequalities. The five-variable formula
\[
\exists a\,\exists b\,\exists c\,\exists d\;
\bigl(\operatorname{Distinct}_4(a,b,c,d)\ \wedge\
\forall z\,\neg(C(a,b,z)\wedge C(c,d,z))\bigr)
\]
uses precisely the five names \(a,b,c,d,z\). Since \(C(a,b,z)\) identifies the line through distinct \(a,b\), the formula asserts two disjoint lines. Every projective plane has intersecting lines, so it is false there. For dimension at least three, take the two lines associated with independent vector pairs \(e_1,e_2\) and \(e_3,e_4\): their associated two-dimensional vector subspaces meet only at zero, hence their projectivizations are disjoint. The formula is true in every such higher-dimensional projective space. Four-variable equivalence established above proves minimality of width five whenever the field-order categories match.

## Verification
A standalone, standard-library-only Python program, `projective_profile_check.py`, independently constructs finite prime-field projective spaces for the parameter pairs \((q,d)=(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(5,2),(5,3)\). It verifies vertex counts, all five representative stationary-pattern profiles, and the crossing/noncrossing line property. The output gives respective extension-profile sizes \((1,2,4,4,7)\) for \(q=2\) and \((1,2,4,5,7)\) for \(q\ge3\), with every checked dimension consistent. Projective linear changes of coordinates reduce distinct stationary configurations to the representative triple cases. Execute `python projective_profile_check.py`. The script does not enumerate arbitrary non-Desarguesian planes, nonprime field orders, or all dimensions; those cases are covered by the geometric argument, not by experiment.

## Relationship to prior work
Classical projective-plane incidence and collinearity axioms supply the geometry used in the proof. The earlier projective-plane literature treats finite and non-Desarguesian planes as standalone geometries, while the theorem here compares their point-only four-variable theories directly with spaces of *every higher dimension*. Venema's 1999 study addresses two-sorted **modal** logic of projective planes, not counting-free first-order four-variable equivalence across dimensions. Stebletsova's 1998 report uses collinearity-based projective geometries in a modal/Lyndon-algebra setting. Grohe and Otto's 2012 paper supplies the broad finite-variable pebble-game framework, not the special uniform extension profiles or the dimension threshold. Previous special-case descriptions of plane structures do not by themselves establish equivalence with higher-dimensional projective spaces.

## Limitations
The theorem is restricted to pure point collinearity and counting-free finite-variable logic. It gives a complete classification at width four and one sharp dimension separation at width five; it does **not** classify all five-variable theories, distinguish all finite fields, or address richer incidence languages, counting logic, or infinite projective spaces. Historical-priority verification is provisional, particularly for early modal/cylindric treatments of collinearity that were not fully accessible in equivalent full text. The finite computations are corroboration, not proof of the infinite parameter range.

## References
1. Martin Grohe and Martin Otto, *Pebble Games and Linear Equations*, first public arXiv version 9 April 2012, arXiv:1204.1990; CSL 2012, DOI 10.4230/LIPIcs.CSL.2012.289. https://arxiv.org/abs/1204.1990
2. Yde Venema, *Points, lines and diamonds: a two-sorted modal logic for projective planes*, Journal of Logic and Computation 9 (1999), 601–621, DOI 10.1093/logcom/9.5.601. https://staff.science.uva.nl/y.venema/papers/vene-poin99.pdf
3. Vera Stebletsova, *Modal Logic of Projective Geometries of Finite Dimension*, Technical Report 184, Utrecht University (1998). https://www.researchgate.net/publication/2665403_Modal_Logic_of_Projective_Geometries_of_Finite_Dimension
4. R. C. Lyndon, *Relation algebras and projective geometries*, Michigan Mathematical Journal 8 (1961), 21–28.
