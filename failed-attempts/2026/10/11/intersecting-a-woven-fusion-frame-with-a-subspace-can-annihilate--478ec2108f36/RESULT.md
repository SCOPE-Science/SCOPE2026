# Intersecting a woven fusion frame with a subspace can annihilate it

## Finding
Theorem 2.2 of Sadri--Ahmadi--Rahimlou claims that if two continuous fusion-frame families are woven for \(H\), then intersecting every fusion subspace with an arbitrary closed subspace \(W\subset H\) produces a continuous fusion-woven pair for \(W\).

This is false already in dimension two.

Let
\[
H=\mathbb R^2,\qquad X=\{1,2\}
\]
with counting measure, unit weights, and
\[
F(1)=G(1)=\operatorname{span}\{e_1\},
\qquad
F(2)=G(2)=\operatorname{span}\{e_2\}.
\]
Because the two source families are identical, every weaving has energy
\[
\|P_{\operatorname{span}\{e_1\}}h\|^2+
\|P_{\operatorname{span}\{e_2\}}h\|^2
=
\|h\|^2.
\]
Thus the pair is Parseval continuous fusion woven.

Choose
\[
W=\operatorname{span}\{e_1+e_2\}.
\]
Neither coordinate axis has a nonzero vector in common with \(W\). Hence
\[
F(1)\cap W=F(2)\cap W=G(1)\cap W=G(2)\cap W=\{0\}.
\]
The intersected analysis energy is identically zero on \(W\), so no positive lower fusion-frame bound exists.

A sufficient repair is to require the orthogonal projection \(P_W\) to commute almost everywhere with every source projection. Under that condition the theorem becomes valid with the same universal frame bounds.

## Assumptions and scope
The example uses a two-point measure space. Such a finite atomic measure space is a legitimate continuous-fusion-frame setting, with the integrals reducing to finite sums.

Both source families are individually Parseval continuous fusion frames, and because they are identical, every measurable weaving is Parseval.

The result concerns arbitrary intersection with a closed subspace. It does not say that intersections can never preserve a fusion frame. In particular, commutation of the relevant orthogonal projections restores the claimed conclusion.

## Proof
For
\[
h=ae_1+be_2,
\]
the energy of every original weaving is
\[
|a|^2+|b|^2=\|h\|^2.
\]
Thus the universal weaving bounds are exactly \(1,1\).

Let
\[
W=\operatorname{span}\{e_1+e_2\}.
\]
Since neither \(e_1\) nor \(e_2\) is a scalar multiple of \(e_1+e_2\),
\[
\operatorname{span}\{e_1\}\cap W=\{0\},
\qquad
\operatorname{span}\{e_2\}\cap W=\{0\}.
\]
Therefore every intersected fusion subspace in either source family is zero. For any nonzero \(h\in W\),
\[
\sum_{x\in X}
\|P_{F(x)\cap W}h\|^2=0,
\]
and the same is true for every weaving. This contradicts any positive lower fusion-frame bound on \(W\).

The source proof fails at the projection step. It replaces
\[
P_{F(x)}P_Wh
\]
by
\[
P_{F(x)\cap W}h.
\]
For arbitrary closed subspaces those operators are not equal. Indeed, set
\[
u=\frac{e_1+e_2}{\sqrt2}\in W.
\]
Then
\[
P_{\operatorname{span}\{e_1\}}P_Wu
=
\frac1{\sqrt2}e_1,
\]
whereas
\[
P_{\operatorname{span}\{e_1\}\cap W}u=0.
\]

For the repair, assume
\[
P_WP_{F(x)}=P_{F(x)}P_W
\]
and the analogous identity for every other source family, almost everywhere. For commuting orthogonal projections,
\[
P_{F(x)\cap W}=P_{F(x)}P_W.
\]
Hence for every \(h\in W\),
\[
P_{F(x)\cap W}h
=
P_{F(x)}P_Wh
=
P_{F(x)}h.
\]
Consequently the energy of each intersected weaving on \(W\) equals the energy of its original weaving evaluated on the same vector. The original universal lower and upper bounds therefore remain valid on \(W\). Measurability also follows from the measurable original projection field composed with the fixed operator \(P_W\).

## Verification
The arXiv preprint and the later journal full text were inspected at the continuous fusion-frame definition, the weaving definition, Theorem 2.2, and its complete proof. The theorem is unchanged in the journal version.

The proof explicitly passes from
\[
P_{F(x)}P_Wh
\]
to the projection onto \(F(x)\cap W\) without a commutation hypothesis. The displayed two-dimensional computation shows that this operator identity fails in the counterexample.

Earlier intersection theory for fusion and \(K\)-fusion frames explicitly assumes commuting orthogonal projections before identifying the product of projections with the projection onto an intersection. This supplies an independent structural check on the repaired hypothesis.

All calculations are exact. No numerical experiment or finite search is used.

## Relationship to prior work
Bhandari--Mukherjee's *Atomic Subspaces for Operators* studies intersection of fusion-type systems. Before its intersection results it states the standard fact that if orthogonal projections \(P_U\) and \(P_V\) commute, then
\[
P_UP_V=P_{U\cap V}.
\]
Its intersection theorem correspondingly assumes commutation of \(P_V\) with every fusion-subspace projection.

That earlier result does not imply failure whenever commutation is absent, so it does not subsume the counterexample here. Rather, it identifies exactly the structural hypothesis missing from the proof of Sadri--Ahmadi--Rahimlou's unrestricted theorem.

Targeted searches by exact title, arXiv identifier, DOI, theorem number, intersection language, projection-commutation language, and counterexample terminology did not locate an indexed erratum or a checked source containing this theorem-specific counterexample.

## Limitations
Commutation is a clean sufficient repair, not asserted to be the weakest possible condition. Some noncommuting configurations may still yield intersected woven fusion frames for geometric reasons.

The result does not reassess the paper's other construction, deletion, characterization, or perturbation theorems.

The counterexample is finite and atomic; its purpose is to refute the universal statement, not to exhibit a specifically nonatomic pathology.

## References
1. V. Sadri, R. Ahmadi and G. Rahimlou, *On continuous weaving fusion frames in Hilbert spaces*, arXiv:1901.03799v1, 12 January 2019; published as *Continuous weaving fusion frames in Hilbert spaces*, International Journal of Wavelets, Multiresolution and Information Processing 18(5) (2020), 2050035, DOI 10.1142/S0219691320500356.
2. A. Bhandari and S. Mukherjee, *Atomic Subspaces for Operators*, arXiv:1705.06042; Indian Journal of Pure and Applied Mathematics 51 (2020), 1039--1052, DOI 10.1007/s13226-020-0448-y.
