# Complementary chainlink sections can have different face lattices first in section dimension three

## Finding

Among interior complementary sections of admissible chainlink polytopes, dimension three is the smallest section dimension in which the face lattices can differ. For \(\mathbf a=(4,5,6,7)\), \(\ell=2\), the sections at heights \(9\) and \(13\) have face vectors \((16,25,11)\) and \((15,24,11)\), respectively, in vertex–edge–facet order. They have seven coordinate facets and four link facets each, and the sums of the respective Euclidean facet areas are \(43\sqrt3\) and \(49\sqrt2\) on both sides. The two sections have the same Ehrhart quasipolynomial by the known chainlink theorem. Thus even equality of these geometric and counting invariants does not force equality of the vertex counts.

## Definitions and scope

Use cyclic indices and
\[
C=\{x\in\mathbb R^s:0\le x_i\le a_i,\quad x_i-x_{i+1}\le a_i-\ell\},\qquad
P_t=C\cap\{x:\textstyle\sum_i x_i=t\},\qquad N=\sum_i a_i.
\]
Here \(s\ge2\), \(a_i>0\), \(0\le2\ell\le\min_i a_i\), and \(0<t<N\). An interior section has dimension \(s-1\): the proportional point \(x_i=ta_i/N\) strictly satisfies the box inequalities and the link inequalities. Euclidean areas are measured in the induced metric. The minimal-dimension assertion concerns face-lattice isomorphism, not affine or metric congruence.

## Proof

### Smaller dimensions

For \(s=2\) the sections are nondegenerate intervals. For \(\ell=0\), the reflection \(x\mapsto\mathbf a-x\) sends a section to its complement. It remains to show that for \(s=3\) and \(\ell>0\) the two sections have equally many sides. The following facet-count argument works for every \(s\ge3\).

The lower coordinate facet \(x_i=0\) has height range \([0,N-a_i-\ell]\): its maximum is attained at all other upper bounds except \(x_{i-1}=a_{i-1}-\ell\). The upper coordinate facet \(x_i=a_i\) has range \([a_i+\ell,N]\): its minimum is attained at \(x_{i+1}=\ell\) with the remaining coordinates zero. The link facet \(x_i-x_{i+1}=a_i-\ell\) has range \([a_i-\ell,N-a_{i+1}+\ell]\): on it \(x_i=a_i-\ell+u\) and \(x_{i+1}=u\) for \(0\le u\le\ell\), and at the two ends the remaining coordinates are all zero or all at their upper bounds, respectively. The threshold \(2\ell\le\min_i a_i\) makes all the specified extremizers feasible; each endpoint is attained by a unique point from the coordinate bounds just described.

Each defining face is a facet. For a lower coordinate face take the other coordinates positive and sufficiently small, and for an upper face take them just below their respective upper bounds. For a link face take \(0<u<\ell\) and all other coordinates at \(a_j/2\); all other inequalities are strict. Thus an original facet gives a section facet exactly when the height is strictly inside its range: its relative interior meets each such height, while an endpoint yields one point, of dimension less than \(s-2\). The projected normal directions of different coordinates and differences do not coincide for \(s\ge3\); the two opposite planes for a fixed coordinate have distinct offsets. This counts all section facets without duplication.

The intervals for the lower and upper coordinate facets pair under \(t\mapsto N-t\) for each \(i\). For links set \(b_i=a_i-\ell\). Since \(b_i<N-b_{i+1}\), the number of open intervals \((b_i,N-b_{i+1})\) containing \(t\) is
\[
\#\{i:b_i<t\}+\#\{i:b_i<N-t\}-s.
\]
This is also symmetric, including at interval endpoints. For \(s=3\) this proves that the two polygons have equal side counts, so their face lattices are isomorphic.

### A three-dimensional witness

For \(\mathbf a=(4,5,6,7)\), \(\ell=2\), the interval formulas yield seven coordinate facets and four link facets at each of the two heights. The exact enumeration in `check_witness.py` finds every vertex by intersecting three independent active planes with the height equation and testing every constraint. It finds 16 and 15 vertices, respectively; Euler's formula with 11 facets gives 25 and 24 edges. For each facet polygon the same enumeration projects to two free coordinates and computes the convex-hull area by shoelace arithmetic. The Jacobian of that projection converts the coordinate area to Euclidean area by factors \(\sqrt3\) for each coordinate facet and \(\sqrt8/2\) for each link facet. The totals are \(43\sqrt3\) and \((49/2)\sqrt8\) at both heights. This computes only the stated witness; the lower-dimensional exclusion above is analytic.

## Relation to earlier results

Kantarcı Oğuz, Özel and Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, [arXiv:2211.08382v1](https://arxiv.org/abs/2211.08382v1), Theorem 4.8, supplies the complementary Ehrhart and volume identities. Its introduction, Figure 2, describes complementary planar sections at heights 4 and 11 for \((6,4,5;2)\) as “non-isomorphic”; by the interval count above both have five sides, so they have isomorphic face lattices. The earlier record *Complementary three-chainlink sections preserve Euclidean perimeter and separate facet-length totals* gives the planar perimeter and edge-length analogue and examples of noncongruent hexagons, not a face-lattice separation.

The separate equality of the two Euclidean facet-area totals is a consequence of the earlier volume theorem, not a novelty claim here. After rational scaling and continuity, that theorem applies to real admissible data. Varying \(\ell\) gives the link total by the usual facet first variation. To isolate the coordinate total at strict admissibility, move each lower coordinate support outward by \(h\) and each upper support outward by \(h\), keeping the link supports fixed. Translating by \(h\mathbf 1\) identifies the perturbed sections with chainlink data \((a_i+2h,\ell+2h)\) at complementary heights \(t+sh,N-t+sh\). Their equal volumes give equality of the coordinate totals by first variation. Fixed normals and continuity extend these consequences to the admissibility boundary. The distinct claim here is a face-lattice difference at the first possible section dimension despite these equalities and the equality of facet counts.
