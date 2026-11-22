# Paired acute–obtuse dihedral spectra and a Dirichlet ridge-angle law for Loday associahedra

## Finding
For each integer \(n\ge3\), the canonical Euclidean Loday associahedron \(P_n\) of intrinsic dimension \(n-1\) has a complete two-branch multiset of interior dihedral angles. For each \(1\le a<b\le n-1\), the **obtuse** angle
\[
\theta^{\mathrm{obt}}_{a,b}=\pi-\arccos\sqrt{\frac{a(n-b)}{b(n-a)}}
\]
occurs \((n-b+1)(b-a+1)\) times. For each \(a,c\ge1\) with \(a+c\le n-1\), the **acute** angle
\[
\theta^{\mathrm{acu}}_{a,c}=\arccos\sqrt{\frac{ac}{(n-a)(n-c)}}
\]
occurs \((n-a-c)(n-a-c+1)/2\) times. Identical numerical angles coming from distinct parameter pairs have additive multiplicities. Every deviation from \(\pi/2\) represented in one branch has its reflected counterpart in the other, though the multiplicities need not agree. There are no right-angle ridges.

The numbers of acute, obtuse, and all ridges are respectively
\[
A_n=\binom{n+1}{4},\qquad
O_n=\frac{(n-2)(n-1)(n^2+9n+12)}{24},\qquad
R_n=\frac{(n-2)(n-1)(n+2)(n+3)}{12}.
\]
In particular, the exact acute fraction is
\[
\frac{A_n}{R_n}=\frac{n(n+1)}{2(n+2)(n+3)}=\frac12-\frac{2n+3}{(n+2)(n+3)}.
\]
It tends to one-half, with the first-order deficit \(2/n\).

A uniformly selected ridge has a nondegenerate limiting angle distribution. Let \(G=(G_0,G_1,G_2,G_3,G_4)\) have the uniform \(\operatorname{Dirichlet}(1,1,1,1,1)\) distribution on the five-dimensional simplex, and define
\[
U=\sqrt{\frac{G_1G_3}{(1-G_1)(1-G_3)}},\qquad
V=\sqrt{\frac{G_2(G_0+G_4)}{(G_1+G_2+G_3)(G_0+G_1+G_3+G_4)}}.
\]
Then, for the interior angle \(\Theta_n\) of a uniformly chosen ridge of \(P_n\),
\[
\Theta_n\ \Longrightarrow\ \tfrac12\,\mathcal L(\arccos U)
+\tfrac12\,\mathcal L(\pi-\arccos V),
\]
where the plus sign denotes a probability mixture of the displayed laws, not addition of independent angles. Its two components are respectively supported in \((0,\pi/2)\) and \((\pi/2,\pi)\).

## Assumptions and scope
Use ordinary Euclidean length and angle in the affine hyperplane
\[
H_n=\left\{x\in\mathbb R^n:\sum_{i=1}^n x_i=\binom{n+1}{2}\right\}.
\]
The **unit-weight Loday associahedron**, not an arbitrary affinely equivalent associahedron, is
\[
P_n=\left\{x\in H_n:\sum_{i=p}^q x_i\ge\binom{q-p+2}{2}
\text{ for every nonempty proper interval }[p,q]\subsetneq[n]\right\}.
\]
The interval inequalities define distinct facets; its face lattice is the nested complex of the path on \([n]\). An interior dihedral angle is the angle between the two inward halfspaces along a codimension-two intersection of distinct facets; it equals \(\pi\) minus the angle between their outward Euclidean unit normals. All exact multiplicities count geometrically distinct ridges once.

## Proof
**1. Ridge incidence.** The path-tubing description of the face lattice implies that distinct proper intervals \(I,J\) intersect in a ridge exactly when one is strictly contained in the other, or when they are disjoint and nonadjacent, meaning at least one index separates them. Neither overlapping nonnested nor adjacent disjoint intervals gives a ridge. Since the associahedron is simple, a two-element tubing indeed specifies one codimension-two face.

**2. Intrinsic normals.** Put \(\mathbf 1=(1,\ldots,1)\) and let \(\mathbf1_I\) be the interval indicator. The outward unit normal of the facet \(I\) *within* \(H_n\) is
\[
\nu_I=-\frac{\mathbf1_I-(|I|/n)\mathbf1}{\sqrt{|I|(n-|I|)/n}}.
\]
Thus for \(a=|I|\), \(b=|J|\), and \(h=|I\cap J|\),
\[
\nu_I\cdot\nu_J=
\frac{nh-ab}{\sqrt{a(n-a)b(n-b)}}.
\]
If \(I\subsetneq J\), then \(h=a\), and the normal dot product is positive with value \(\sqrt{a(n-b)/(b(n-a))}\). This gives the stated obtuse interior angle. If disjoint, \(h=0\), and the normal dot product is \(-\sqrt{ac/((n-a)(n-c))}\), giving the acute angle. Neither dot product is zero, proving the absence of right angles. Substitution \(c=n-b\) gives \(\theta^{\mathrm{obt}}_{a,b}=\pi-\theta^{\mathrm{acu}}_{a,n-b}\); the parameter restrictions correspond bijectively.

**3. Multiplicities and totals.** An outer interval of length \(b\) has \(n-b+1\) possible positions and contains \(b-a+1\) subintervals of length \(a\); this proves its multiplicity. Two disjoint ordered left-to-right intervals of lengths \(a,c\) have \(n-a-c\) unused sites distributed among the before, between, and after gaps; the middle gap must be positive. The number of distributions is \(\binom{n-a-c+1}{2}\), giving the acute multiplicity. Each pair is counted once. Summation yields
\[
\sum_{1\le a<b\le n-1}(n-b+1)(b-a+1)
=\frac{(n-2)(n-1)(n^2+9n+12)}{24},
\]
while the left-to-right disjoint intervals are in bijection with four distinct boundary positions from \(\{0,1,\ldots,n\}\), hence their number is \(\binom{n+1}{4}\). Adding gives \(R_n\) and the acute fraction.

**4. Weak limit.** Choose boundary positions \(0\le s<t<u<v\le n\). Each such quadruple corresponds to exactly one disjoint nonadjacent pair, \([s+1,t]\) and \([u+1,v]\). Conditioned on an acute ridge, all quadruples are equiprobable. Their normalized five gaps \((s,t-s,u-t,v-u,n-v)/n\) converge jointly to uniform Dirichlet five-spacings (the gaps of four ordered independent uniform points), and the angle formula becomes \(\arccos U\). For nested facets, quadruples with four distinct boundaries give the outer interval \([s+1,v]\) and inner interval \([t+1,u]\), with the outer full interval excluded. The number excluded in this generic construction is \(\binom{n-1}{2}\); nested pairs sharing a boundary endpoint number only \(O(n^3)\). Both exceptional populations are negligible beside \(O_n\sim n^4/24\), so a uniform nested pair has the same limiting five-spacings. Its ratio of inner length to outer length is \(G_2/(G_1+G_2+G_3)\), and the complementary-length ratio is \((G_0+G_4)/(G_0+G_1+G_3+G_4)\). The angle becomes \(\pi-\arccos V\). Continuous mapping applies since each limiting gap is strictly positive almost surely. The branch probabilities converge to one-half by the exact counts, yielding the mixture.

## Verification
Run `python verify_loday_angles.py` with Python 3 and NumPy. The program independently constructs all Loday vertices from planar binary-tree leaf-product coordinates, finds facet tight-vertex sets, tests codimension-two affine ranks, and compares exact rational squared normal cosines, the acute–obtuse level pairing, and total-count formulas for all integers \(3\le n\le8\). It prints `LODAY_RIDGE_ANGLE_PASS` on success. This finite check corroborates the all-parameter geometric proof; it is not a proof of an unbounded family or of weak convergence.

## Relationship to prior work
Loday's original vertex and facet realization and the later survey by Pilaud, Santos, and Ziegler supply the definition and the known path-nested-complex incidence theorem; neither fact is new here. Prior associahedron-realization and low-dimensional projection studies address affine/combinatorial structure and specific small-dimensional angles. The proposed contribution is the resulting **full intrinsic Euclidean ridge-angle multiset**, its paired angular support, exact acute/obtuse counts, and a five-spacing limiting law. The polytope's Euclidean embedding is essential: a general affine change would not preserve the displayed angles.

## Limitations
Novelty is provisional pending independent historical-priority review. The derivation uses the established complete facet description and path-tubing theorem, which must be retained as assumptions if a different coordinate realization is used. The displayed weak limit is for uniformly sampled **ridges**, not surface-area-weighted ridge sampling, and is not a law for arbitrary associahedron realizations. The exact expression is a Dirichlet-mixture representation, not a claimed closed elementary density. Computational validation reaches finite dimensions only; no independent audit has been performed.

## References
1. Jean-Louis Loday, *Realization of the Stasheff polytope*, arXiv:math/0212126 (first public version 9 December 2002), https://arxiv.org/abs/math/0212126.
2. Vincent Pilaud, Francisco Santos and Günter M. Ziegler, *Celebrating Loday's associahedron*, arXiv:2305.08471 (first public version 15 May 2023), https://arxiv.org/abs/2305.08471; open-access version https://doi.org/10.1007/s00013-023-01895-6.
3. César Ceballos, Francisco Santos and Günter M. Ziegler, *Many non-equivalent realizations of the associahedron*, arXiv:1109.5544, https://arxiv.org/abs/1109.5544.
4. Markus Rost, *The Loday realization of the associahedron (projections)*, https://www.math.uni-bielefeld.de/~rost/associahedron-loday-projections/ (low-dimensional geometry).
