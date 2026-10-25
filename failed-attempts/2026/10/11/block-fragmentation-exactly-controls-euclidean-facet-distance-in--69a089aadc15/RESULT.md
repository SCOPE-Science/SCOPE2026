# Block fragmentation exactly controls Euclidean facet distance in generalized multiplihedra
## Finding
Let
\[
m,n\ge2,
\qquad
N=m+n,
\]
and let
\[
\operatorname{Mul}(m,n)\subset\mathbb R^N
\]
be the \((m,n)\)-multiplihedron in the standard shuffle realization of Chapoton and Pilaud.

Every vertex lies in the affine hyperplane
\[
H=
\left\{
x\in\mathbb R^N:
\sum_{i=1}^N x_i=\binom{N+1}{2}
\right\}.
\tag{1}
\]
Equip \(H\) with its intrinsic Euclidean metric.

A facet is described in Proposition 3.20 of the source by a set
\[
A\subseteq[m]
\]
and by disjoint right-coordinate blocks
\[
B=B_1\sqcup\cdots\sqcup B_k.
\]
Put
\[
a=|A|,
\qquad
b_j=|B_j|,
\qquad
b=\sum_{j=1}^k b_j,
\qquad
s=a+b,
\tag{2}
\]
and define the **fragmentation statistic**
\[
\Gamma(B_1,\ldots,B_k)
=
\sum_{1\le r<t\le k}b_rb_t.
\tag{3}
\]
For \(k\le1\), this sum is \(0\).

Let
\[
c=\frac{N+1}{2}\mathbf1.
\tag{4}
\]
Then the exact intrinsic Euclidean distance from \(c\) to the facet hyperplane is
\[
\boxed{
\delta(A;B_1,\ldots,B_k)
=
\frac12\sqrt{Ns(N-s)}
+
\Gamma(B_1,\ldots,B_k)
\sqrt{\frac{N}{s(N-s)}}.
}
\tag{5}
\]

Consequently the unique incenter is \(c\), and
\[
\boxed{
r_{\mathrm{in}}\bigl(\operatorname{Mul}(m,n)\bigr)
=
\frac12\sqrt{N(N-1)}.
}
\tag{6}
\]

A facet is tangent to the maximal ball if and only if
\[
s\in\{1,N-1\}
\quad\text{and}\quad
k\le1.
\tag{7}
\]
The source proves that \(k\le1\) is exactly the condition for the same facet inequality to be a facet inequality of the ordinary permutahedron
\[
\operatorname{Perm}(N).
\]
Thus the tangent facets are precisely the extreme-cardinality multiplihedron facets inherited from the permutahedron.

Formula (5) gives more than the inradius. At fixed support size \(s\), every split of the right coordinates into multiple separated blocks increases the center-to-facet distance by the exact positive amount
\[
\Gamma
\sqrt{\frac{N}{s(N-s)}}.
\tag{8}
\]
This is a quantitative metric penalty for associahedral block fragmentation inside the shuffle construction.

## Assumptions and scope
The parameters satisfy
\[
m,n\ge2.
\]
This restriction keeps the statement on the genuinely generalized \((m,n)\)-multiplihedra introduced by Chapoton and Pilaud rather than the older classical multiplihedron obtained at \(m=1\).

The realization is exactly the shuffle realization in the cited source,
\[
\operatorname{Mul}(m,n)
=
\operatorname{Perm}(m)\star\operatorname{Asso}(n),
\]
with the source's explicit facet and Minkowski-sum coordinates.

Distances are measured in the affine hyperplane (1) with the metric inherited from \(\mathbb R^N\). The result is not invariant under arbitrary affine changes of realization.

## Proof
The source proves that all vertex coordinate sums are
\[
\binom{m+1}{2}
+
\binom{n+1}{2}
+
mn
=
\binom{N+1}{2},
\]
which gives (1).

For a facet encoded by \(A\) and the right blocks \(B_1,\ldots,B_k\), Proposition 3.20 gives the inequality
\[
x(A\cup B)
\ge
\binom{a+1}{2}
+
\sum_{j=1}^k\binom{b_j+1}{2}
+
ab.
\tag{9}
\]
Since
\[
\binom{s+1}{2}
=
\binom{a+1}{2}
+
\binom{b+1}{2}
+
ab
\]
and
\[
\binom{b+1}{2}
-
\sum_{j=1}^k\binom{b_j+1}{2}
=
\sum_{r<t}b_rb_t
=
\Gamma,
\]
the right side of (9) is
\[
\binom{s+1}{2}-\Gamma.
\tag{10}
\]

At the uniform point (4), the slack in (9) is therefore
\[
\frac{s(N+1)}2
-
\binom{s+1}{2}
+
\Gamma
=
\frac{s(N-s)}2+\Gamma.
\tag{11}
\]

Inside the tangent space
\[
\mathbf1^\perp,
\]
the normal \(\mathbf1_{A\cup B}\) projects to
\[
\mathbf1_{A\cup B}-\frac{s}{N}\mathbf1,
\]
whose squared norm is
\[
s-\frac{s^2}{N}
=
\frac{s(N-s)}N.
\tag{12}
\]
Dividing (11) by the norm in (12) proves (5).

Because a facet uses a nonempty proper coordinate set,
\[
1\le s\le N-1.
\]
Hence
\[
s(N-s)\ge N-1,
\tag{13}
\]
with equality exactly when
\[
s=1
\quad\text{or}\quad
s=N-1.
\]
Also
\[
\Gamma\ge0,
\]
with equality exactly when the right part has at most one nonempty block. Formula (5) therefore yields
\[
\delta
\ge
\frac12\sqrt{N(N-1)},
\tag{14}
\]
and equality is exactly the condition in (7).

This proves that the radius
\[
r_0=\frac12\sqrt{N(N-1)}
\]
ball centered at \(c\) satisfies every facet inequality.

It remains to prove that no larger ball, and no other radius-\(r_0\) center, is possible. Proposition 3.21 realizes the multiplihedron as a Minkowski sum of coordinate simplices and includes every singleton simplex
\[
\Delta_{\{i\}}.
\]
Therefore every point of the polytope satisfies the valid support inequality
\[
x_i\ge1
\qquad
(1\le i\le N).
\tag{15}
\]
Within \(H\), the boundary hyperplane \(x_i=1\) has projected normal norm
\[
\sqrt{\frac{N-1}{N}}.
\tag{16}
\]

If a radius-\(r\) ball centered at \(q\in H\) is contained in the multiplihedron, (15) implies
\[
q_i-1
\ge
r\sqrt{\frac{N-1}{N}}
\qquad
(1\le i\le N).
\tag{17}
\]
Summing and using
\[
\sum_i q_i=\binom{N+1}{2}
\]
gives
\[
\frac{N(N-1)}2
\ge
r\sqrt{N(N-1)}.
\]
Thus
\[
r\le r_0.
\tag{18}
\]
If equality holds, then equality must hold in every inequality in (17), forcing
\[
q_i=\frac{N+1}{2}
\]
for every \(i\). Hence \(q=c\).

This proves the exact inradius and uniqueness of the incenter. The equality conditions in (13)--(14), together with the source's criterion that \(k\le1\) is precisely the permutahedral-facet case, prove the tangent-facet classification.

## Verification
The proof is symbolic and applies to every
\[
m,n\ge2.
\]

The source-dependent premises were checked directly in the full text and page image: Proposition 3.20 gives the facet constant in (9), Proposition 3.21 gives the Minkowski-sum realization, and Proposition 3.19 gives the common coordinate sum.

The accompanying `verify.py` independently reconstructs the Minkowski summands from Proposition 3.21 for every
\[
2\le m,n\le7.
\]
For every nonempty proper coordinate subset it counts the contained simplex summands directly, compares that count with (10), computes the exact rational squared distance from the uniform center, and verifies the global lower bound and all equality conditions. These finite checks are corroborative only.

## Relationship to prior work
Chapoton and Pilaud introduce the shuffle of deformed permutahedra and the generalized \((m,n)\)-multiplihedra. Their paper gives explicit vertex, facet, Minkowski-sum, lattice, and enumerative descriptions. Proposition 3.20 notes exactly when a multiplihedron facet inequality is also a permutahedron facet inequality, but does not compare normalized Euclidean facet distances.

The same paper explicitly states that the classical multiplihedra occur when \(m=1\), while general \(m\) extends that older family. The present theorem is restricted to \(m,n\ge2\), so it concerns the genuinely generalized family introduced there.

Later work on Hochschild polytopes starts from the same \((m,n)\)-multiplihedra and deletes selected inequalities to obtain new quotient-like realizations. That literature develops faces and rotation lattices rather than the Euclidean Chebyshev geometry computed here.

The ordinary permutahedron and Loday associahedron are known neighboring shuffle factors with the same numerical inradius in these coordinates. That coincidence alone does not imply the present theorem: formula (5) identifies the exact distance of every generalized-multiplihedron facet and isolates the additional block-fragmentation term.

Targeted literature searches under “multiplihedron”, “\((m,n)\)-multiplihedron”, “painted tree”, “inradius”, “Chebyshev center”, “Euclidean facet distance”, and “block fragmentation” did not locate a theorem implying (5)--(7).

## Limitations
The theorem concerns only the Chapoton--Pilaud shuffle realization, not Forcey's older realization of the classical \(m=1\) multiplihedron or arbitrary affine realizations.

The restriction
\[
m,n\ge2
\]
is part of the claim. No assertion is made here about whether every boundary specialization should be assigned the same earliest source date.

The result determines the inball and all facet distances from its center, but it does not determine the circumradius, John ellipsoid, or pairwise vertex metric.

Because the proof becomes short after Proposition 3.20 is rewritten using the fragmentation statistic, an equivalent folklore observation could exist under generalized-permutahedron terminology. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Frédéric Chapoton and Vincent Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, first public version 2022-01-18; Annales Henri Lebesgue 7 (2024), 1535--1601, DOI 10.5802/ahl.225.
2. Vincent Pilaud and Daria Poliakova, *Hochschild polytopes*, Séminaire Lotharingien de Combinatoire 91B (2024), article 1; later expanded in Mathematische Annalen.
