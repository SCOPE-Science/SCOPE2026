# A Moore space and twelve spheres in the Singer quotient of the ternary projective matroid

## Finding

Let \(P=\operatorname{PG}(2,\mathbb F_3)\), and let \(K\) be the rank-three matroid independence complex on its thirteen projective points: its vertices are points, all pairs are edges, and precisely the **noncollinear** triples are its two-simplices. The projective Singer cycle \(C_{13}\) acts regularly on the thirteen point labels. Its ordinary geometric orbit space \(Y=|K|/C_{13}\) has the complete integral homotopy type

\[
\boxed{Y\simeq M(\mathbb Z/13\mathbb Z,1)\vee\bigvee^{12}S^2,}
\]

where \(M(\mathbb Z/13\mathbb Z,1)=S^1\cup_{13}e^2\) is the two-dimensional Moore space with a degree-thirteen attaching map. In particular,

\[
\pi_1(Y)\cong C_{13},\qquad H_1(Y;\mathbb Z)\cong\mathbb Z/13\mathbb Z,\qquad H_2(Y;\mathbb Z)\cong\mathbb Z^{12},
\]

and all higher integral homology groups vanish. There is a further **integral deck-group consequence**, not merely a character decomposition: writing \(R=\mathbb Z[C_{13}]\) and \(I=\ker(\varepsilon:R\to\mathbb Z)\),

\[
\widetilde H_2(K;\mathbb Z)\cong_R I\oplus R^{12}.
\]

The equivariance here concerns the natural homology action of the Singer deck group; an equivariant wedge decomposition of \(K\) itself is not asserted.

## Assumptions and scope

All spaces are finite ordinary geometric realizations, not Borel constructions or simplicial complexes obtained by indiscriminately identifying all orbit vertices. We identify the point set with \(\mathbb Z/13\mathbb Z\) using a Singer difference set \(D=\{0,1,3,9\}\). The thirteen lines are the translates \(D+t\), and \(r(i)=i+1\) generates the Singer group. The asserted matroid complex comprises faces of size at most three; it is **not** the three-dimensional arc/cap complex, whose faces include certain four-point caps, nor the incidence complex whose facets are lines.

The polynomial \(T^3-T+1\in\mathbb F_3[T]\) is irreducible. In the field \(\mathbb F_{27}=\mathbb F_3[\alpha]\), where \(\alpha^3=\alpha-1\), we have \(\alpha^{13}=-1\). The projective classes of \(1,\alpha,\ldots,\alpha^{12}\) exhaust the points of \(P\), and the line spanned by \(1\) and \(\alpha\) contains precisely the indexed points \(0,1,3,9\). This identifies the difference-set model with the standard ternary Desarguesian plane and identifies translation with the projective Singer action.

The theorem concerns this order-three plane and its complete order-thirteen Singer subgroup. It makes no assertion for larger projective planes or their other collineation subgroups.

## Proof

**1. The cyclic projective-plane model and free action.** The twelve ordered nonzero differences of \(D=\{0,1,3,9\}\) cover the twelve nonzero elements of \(\mathbb Z/13\mathbb Z\) exactly once. Hence every pair of distinct labels lies on exactly one translate of \(D\), and this is a projective plane of order three, explicitly coordinatized above. A triple is independent if and only if it is not contained in one of the thirteen four-point lines. There are \(13\binom43=52\) dependent triples, all distinct, so the face vector of \(K\) is

\[
(f_0,f_1,f_2)=(13,78,\binom{13}{3}-52)=(13,78,234).
\]

Every nonidentity element of \(C_{13}\) is a thirteen-cycle on vertices. No nonempty face of size at most three is setwise stable, so the action on \(|K|\) is free. The quotient inherits a valid two-dimensional \(\Delta\)-complex/CW structure with one vertex, six oriented edge orbits, and eighteen triangle orbits.

**2. Exact two-cell attaching words.** Denote by \(a,b,c,d,e,f\) the oriented quotient loops represented by steps \(1,2,3,4,5,6\), respectively. A step congruent to \(-j\pmod {13}\) represents the inverse of the positive step-\(j\) loop. For each representative triangle \((u,v,w)\), its attaching word follows the directed circuit \(u\to v\to w\to u\). Enumerating all eighteen translation-orbits gives the following words; labels refer to exact orbit representatives rather than unordered quotient vertices:

| Triangle | Attaching word | Triangle | Attaching word |
| --- | --- | --- | --- |
| \((0,1,2)\) | \(a^2b^{-1}\) | \((0,2,4)\) | \(b^2d^{-1}\) |
| \((0,1,4)\) | \(acd^{-1}\) | \((0,2,5)\) | \(bce^{-1}\) |
| \((0,1,5)\) | \(ade^{-1}\) | \((0,2,6)\) | \(bdf^{-1}\) |
| \((0,1,6)\) | \(aef^{-1}\) | \((0,2,7)\) | \(bef\) |
| \((0,1,7)\) | \(af^2\) | \((0,2,9)\) | \(bf^{-1}d\) |
| \((0,1,8)\) | \(af^{-1}e\) | \((0,2,10)\) | \(be^{-1}c\) |
| \((0,1,10)\) | \(ad^{-1}c\) | \((0,3,6)\) | \(c^2f^{-1}\) |
| \((0,1,11)\) | \(ac^{-1}b\) | \((0,3,7)\) | \(cdf\) |
|  |  | \((0,3,8)\) | \(ce^2\) |
|  |  | \((0,4,8)\) | \(d^2e\) |

All words are in the fundamental group of the one-skeleton, the free group on six loops. A word here also records the **actual cellular attaching map**, not only its abelianization.

**3. Five homotopy-preserving cancellations.** A two-cell whose attaching word contains a particular one-cell exactly once, with exponent \(\pm1\), permits a one-cell/two-cell cancellation; its relation substitutes that generator by a word in the others. Apply the five cells represented, in order, by

\[
(0,1,2),\quad(0,1,11),\quad(0,1,4),\quad(0,1,5),\quad(0,1,6).
\]

The corresponding equations are successively

\[
b=a^2,\qquad c=ba=a^3,\qquad d=ac=a^4,\qquad e=ad=a^5,\qquad f=ae=a^6.
\]

Every step eliminates a generator occurring exactly once in its selected two-cell, so these are homotopy-preserving CW cancellations, not deductions from a merely abelian presentation. There remains one loop \(a\) and thirteen two-cells.

Under these substitutions, eight of the thirteen remaining attaching words freely reduce to the empty word: the triangles

\[
(0,1,8),(0,1,10),(0,2,4),(0,2,5),(0,2,6),(0,2,9),(0,2,10),(0,3,6).
\]

The other five attaching maps are all the **same** degree-thirteen loop \(a^{13}\), arising from

\[
(0,1,7),(0,2,7),(0,3,7),(0,3,8),(0,4,8).
\]

Attach one of these five cells first: the one-skeleton and this cell form exactly \(S^1\cup_{13}e^2\). Each remaining degree-thirteen map is now nullhomotopic by that two-cell, and the eight empty-word maps were already nullhomotopic. Adding a two-cell along a nullhomotopic map contributes an \(S^2\) wedge summand, up to homotopy. Thus the remaining twelve two-cells give precisely \(\bigvee^{12}S^2\), proving the displayed homotopy equivalence.

**4. The integral Singer homology lattice.** The Moore summand has fundamental group \(C_{13}\), generated by the loop \(a\) corresponding to the point translation \(r\). The action of \(C_{13}\) on \(|K|\) is free and the quotient map has degree thirteen. Since the quotient has fundamental group exactly \(C_{13}\), this cover is its universal cover. Let \(N=1+r+\cdots+r^{12}\in R\). The lifted cellular complex for the Moore summand is

\[
0\to R\xrightarrow{N}R\xrightarrow{r-1}R\to0.
\]

Its second homology is \(\ker N=I\), because \(Nw=\varepsilon(w)N\). Each of the twelve sphere wedge summands lifts to thirteen spheres permuted freely by the deck group, contributing one regular \(R\)-module. Therefore \(\widetilde H_2(K;\mathbb Z)\cong_R I\oplus R^{12}\). This is an integral isomorphism and has rank \(12+12\cdot13=168\), consistent with the directly computed reduced Euler characteristic \(13-78+234-1=168\).

## Verification

Run `python3 verify_singer13.py` from the package root. This standard-library program independently constructs the cyclic difference-set plane and the projective field model \(\mathbb F_{27}\), checks all pair-on-line incidences, enumerates the matroid faces and translation-orbit representatives, regenerates the eighteen attaching words, tests that the five indicated eliminations are legal, and computes each remaining attaching degree. It reports exactly eight null attaching words and five words of degree thirteen, then `VERIFY_OK`.

An additional exact Smith normal form calculation on the \(6\times18\) cellular two-boundary matrix, independently assembled from these words, gave nonzero invariant factors \((1,1,1,1,1,13)\). This corroborates the quotient homology, but the **homotopy** conclusion uses the actual generator/relator cancellations and nullhomotopies, not the Smith form alone. The recorded expected output is in `verification_output.txt`.

## Relationship to prior work

Classical Singer finite geometry gives the regular cyclic action, and Björner's matroid shellability theorem (as revisited by Ardila, Castillo and Samper) establishes that the **unquotiented** rank-three matroid complex is a wedge of two-spheres. Those results do not specify the orbit-space attaching maps. Cook, Migliore, Nagel and Zanello (2015) study the *incidence complex whose maximal faces are collinear point sets*, along with Stanley–Reisner and inverse-system invariants; this differs from the independence complex studied here.

A separate general computation of Singer quotients of projective rank-three matroid complexes gives the fundamental group and integral homology for all prime powers; at \(q=3\) it yields \(\pi_1=C_{13}\) and \(H_2=\mathbb Z^{12}\). **Neither datum specifies the two-dimensional homotopy type or the integral deck-group homology module.** The present explicit cancellation identifies both. Previously recorded Fano-plane Singer calculations have a different field order and cyclic group, while known ternary projective-plane cap-complex results concern the three-dimensional no-three-collinear-set complex rather than the two-dimensional rank-three independence complex or its cyclic quotient. Moci and Pezzoli's 2020 equivariant theory treats complex-valued representations, not these complete integral orbit-space attaching maps. No equivalent or stronger homotopy classification was identified in the checked sources, but absence from a search is not proof of priority.

## Limitations

The theorem concerns only the Singer quotient of the rank-three matroid complex of \(\operatorname{PG}(2,3)\). It does not classify other subgroup quotients, finite projective planes of other orders, higher homotopy groups of the resulting wedge in explicit coordinates, or a Singer-equivariant wedge decomposition of the original complex. The associated integral deck-module is determined only up to the natural choice of generator of \(C_{13}\). The finite checker is a reproducibility aid, while the proof of the homotopy equivalence is the explicit CW attaching-map argument. An inaccessible or unindexed earlier equivalent classification cannot be excluded; no independent external validation has been performed.

## References

1. F. Ardila, F. Castillo and J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870, first submitted 2014-10-14; see introduction and Theorem 1.3 for matroid independence complexes. https://arxiv.org/abs/1410.3870
2. D. Cook II, J. Migliore, U. Nagel and F. Zanello, *An algebraic approach to finite projective planes*, arXiv:1503.04335, first submitted 2015-03-14; see Section 2, Definition 2.1 and Proposition 2.2. https://arxiv.org/html/1503.04335v2
3. J. Singer, *A theorem in finite projective geometry and some applications to number theory*, Trans. Amer. Math. Soc. 43 (1938), 377–385, DOI: 10.1090/S0002-9947-1938-1501951-4. Classical difference-set background; original full text not inspected.
4. L. Moci and G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760, first submitted 2020-01-11; see introduction and Sections 2–4. https://arxiv.org/abs/2001.03760
