# Three collinearity theories of finite affine and projective planes at four variables

## Finding
Let \(\mathcal P\) range over all finite affine and projective planes of order at least two. Interpret \(\mathcal P\) as a *point-only* structure \((P;C)\), with equality and the ternary relation \(C(a,b,c)\) true precisely when some line contains the three points (including any triple with repeated entries). No lines, coordinate operations, constants, counting quantifiers, or sorts are present.

Write \(\ell(\mathcal P)\) for the number of points on each line, so \(\ell=q\) in an affine plane of order \(q\) and \(\ell=q+1\) in a projective plane of order \(q\). For any two such planes \(\mathcal P,\mathcal Q\),

\[
\mathcal P\equiv_{\mathrm{FO}^{4}}\mathcal Q
\quad\Longleftrightarrow\quad
\min\{\ell(\mathcal P),4\}=\min\{\ell(\mathcal Q),4\}.
\]

This equivalence is at **unrestricted quantifier depth**. Thus exactly three four-variable theories occur: (A) affine order two; (B) affine order three together with projective order two; and (C) affine order at least four together with projective order at least three. At variable widths \(1,2,3,4\) the numbers of theories are respectively \(1,1,2,3\).

Moreover any affine plane and projective plane in the *same* four-variable class are first distinguishable by five variables. In particular, the nine-point affine plane of order three and the seven-point Fano projective plane are four-variable equivalent, but not five-variable equivalent. The conclusion holds also for non-Desarguesian finite planes.

## Assumptions and scope
Throughout, an affine plane of order \(q\ge2\) has \(q^2\) points, \(q\) points on every line, a unique line through any two distinct points, and parallel classes of disjoint lines. A projective plane of order \(q\ge2\) has \(q^2+q+1\) points, \(q+1\) points on every line, a unique line through any two distinct points, and every pair of distinct lines intersect. Existence is not asserted at every numerical order. The theorem quantifies only over existing finite planes, without assuming coordinates.

\(\mathrm{FO}^{k}\) means ordinary first-order formulas containing at most \(k\) distinct variable names, which may be rebound arbitrarily many times, without counting quantifiers. \(C(a,a,b)\) and other repetitions always hold, since two points lie on a line. The equivalence concerns sentences in the *single ternary collinearity language*, not first-order logic with lines as objects.

## Proof
Put \(N=|P|\) and \(\ell\) equal to the uniform line size. Every finite plane in the scope has the following elementary property: for three distinct noncollinear points \(a,b,c\), their three pair-lines have union of size \(3\ell-3\), and at least one point lies outside that union. Indeed in an affine plane this outside count is \(q^2-3q+3>0\), while in a projective plane it is \((q-1)^2>0\). Each line also has points off it.

Consider a partial position in the ordinary four-pebble game. After one pebble is lifted, at most three positions remain. Their complete atomic type consists of their equality pattern and the collinearity of any triple of distinct positions. For a prospective new point \(x\), the possible extensions are as follows.

* With zero or one distinct stationary point, \(x\) may equal a stationary point or be different; both options allowed where meaningful.
* With two distinct stationary points \(a,b\), \(x\) may equal one of them, lie on their line but differ from both (possible exactly when \(\ell\ge3\)), or lie off that line (always possible).
* With three distinct stationary points on one line, \(x\) may equal one of them, be a fourth point on that line (possible exactly when \(\ell\ge4\)), or lie off the line (always possible).
* With three distinct noncollinear stationary points \(a,b,c\), \(x\) may equal one of them, be an additional point on precisely one of the three pair-lines (possible exactly when \(\ell\ge3\)), or lie on none of those lines (always possible by the positive outside counts). Distinct pair-lines intersect only at their common stationary vertex, so no additional category exists.

Consequently, if two planes have the same value of \(\min\{\ell,4\}\), then for any correspondence of at most three stationary points preserving their atomic type, every atomic extension type on one side is realized on the other, in both directions. Duplicator chooses the corresponding type after each move. This maintains a partial isomorphism permanently, for arbitrary play length. The standard four-pebble characterization gives \(\mathrm{FO}^{4}\)-equivalence.

Conversely, the sentence asserting three pairwise distinct collinear points, using \(3\) variables, holds exactly when \(\ell\ge3\). The sentence asserting four pairwise distinct collinear points, using \(4\) variables, holds exactly when \(\ell\ge4\). (The latter can be written by taking four distinct points \(a,b,c,d\) with \(C(a,b,c)\land C(a,b,d)\).) These sentences separate the three classes. With at most two variables every collinearity atom is automatically true and all these planes have at least four points, giving one theory. With three variables the same extension analysis truncated to two stationary pebbles gives precisely two theories, separated by the three-collinear sentence. One variable likewise gives one theory.

Finally, using only five variable names \(a,b,c,d,z\), write the sentence saying that four pairwise distinct points \(a,b,c,d\) exist with
\[
\forall z\;\neg\big(C(a,b,z)\land C(c,d,z)\big).
\]
This holds in every affine plane (choose two parallel, hence disjoint, lines and two points on each) and fails in every projective plane (the two lines always meet). Therefore, for any affine/projective pair in the same four-variable class, the minimum distinguishing width is exactly five. This proves all claims.

## Verification
Run `python3 verify.py` using only the Python standard library, and compare its output with `VERIFY.out`. It constructs prime-field examples \(\operatorname{AG}(2,p)\) and \(\operatorname{PG}(2,p)\) for \(p=2,3,5\), computes every equality/collinearity atomic extension type for each ordered stationary triple (including repeated positions), and checks equality of the complete extension catalogues within the predicted classes. The six examples have \(4,7,9,13,25,31\) points and exhibit catalogues with \(15,25,25,26,26,26\) extension types respectively. All comparisons pass.

These are finite demonstrations only; the above geometric case analysis proves the theorem for arbitrary finite affine and projective planes, including non-coordinatizable examples.

## Relationship to prior work
Grohe and Otto's *Pebble Games and Linear Equations* (first arXiv version 2012) supplies the ordinary pebble-game characterization and studies algebraic formulations of finite-variable equivalence, but does not claim the present plane-specific cross-type classification. Venema's *Points, Lines and Diamonds* studies a two-sorted modal incidence language for projective planes, explicitly contrasts this with ternary point-collinearity frames, and addresses axiomatization, decidability and complexity; its comparison does not establish four-variable equivalence between affine and projective planes. Stebletsova's earlier report concerns modal logics of projective collinearity structures; its full report was not obtained for direct comparison. The conclusion is specific to point-only \(\mathrm{FO}^{4}\) without counting, and does not follow from equivalence results in the different two-sorted incidence language without a variable-width argument.

## Limitations
Historical priority is not conclusively established: a more general existing theorem on finite-variable logic of rank-three linear spaces could imply this result, and Stebletsova's full 1998 report was unavailable. The argument does not classify five-variable theories within affine planes or within projective planes; it only supplies the sharp affine-versus-projective separator for pairs already four-variable equivalent. Adding named lines, other predicates, or counting quantifiers changes the expressive resources. The experiment covers only six prime-field models and supplies no proof of the unrestricted result beyond the separate geometric argument.

## References
1. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990 (first posted 2012-04-09), especially Section 2 and Theorem 2.1. https://arxiv.org/abs/1204.1990
2. Y. Venema, *Points, Lines and Diamonds: A Two-Sorted Modal Logic for Projective Planes*, *Journal of Logic and Computation* 9 (1999), 601–621, especially Introduction and Section 2. https://staff.science.uva.nl/y.venema/papers/vene-poin99.pdf
3. V. Stebletsova, *Modal Logic of Projective Geometries of Finite Dimension*, Technical Report 184, Utrecht (1998); contextual comparison based on its available abstract and the account in Venema, not its uninspected complete text.
