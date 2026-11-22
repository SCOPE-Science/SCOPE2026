# A finite-disk criterion for planar Steiner symmetrization

## Finding
Let \(K=\bigcap_{i=1}^{m}\overline B((a_i,b_i),1)\subset\mathbb R^2\) have nonempty interior and let \(S(K)\) be its Steiner symmetral along horizontal fibers (hence symmetric about the vertical axis). For each height \(y\) in the interior of the projection of \(K\) to the vertical axis, set
\[
 L(y)=\max_i\bigl(a_i-\sqrt{1-(y-b_i)^2}\bigr),\quad
 R(y)=\min_j\bigl(a_j+\sqrt{1-(y-b_j)^2}\bigr).
\]
The displayed functions are understood only where all disks meet the horizontal line; there \(L<R\). Partition the positive-length fiber heights into finitely many open intervals on which active left and right indices \(i,j\) are constant, apart from isolated switching heights (duplicate disks may be removed). **Finite-disc criterion:** \(S(K)\) is an intersection of finitely many unit disks if and only if \(b_i=b_j\) on *every* such open interval.

In particular let \(L_a=\overline B(ae_1,1)\cap\overline B(-ae_1,1)\), \(0<a<1\). A Steiner symmetrization of \(L_a\) has a finite unit-disk representation precisely when the fibers are parallel or perpendicular to the line of centers. For every strictly oblique fiber direction the symmetral still is a unit ball-body, but has no finite unit-disk representation. It admits a countable representation, by compactness and density of supporting unit-disk centers.

## Assumptions and scope
Disks are closed, Euclidean, of a common *fixed unit radius*; the input is any finite nonempty-interior intersection (redundant or duplicate disks allowed). Finiteness of the output means existence of *some* finite family of unit disks, not necessarily disks from the original input. The criterion concerns a single classical Steiner symmetrization. It is invariant under rigid rotations of the fiber coordinates and under common translation of all centers. We rely on the established planar theorem that Steiner symmetrization preserves the class of intersections of unit disks (Artstein-Avidan and Florentin, Theorem 4.1).

## Proof
**1. Finite active partition.** For fiber heights inside the common vertical projection of the disks put \(r_i(y)=\sqrt{1-(y-b_i)^2}\). The interval from disk \(i\) is \([a_i-r_i(y),a_i+r_i(y)]\). Thus the intersection fiber is \([L(y),R(y)]\), and the symmetral fiber is \([-h(y),h(y)]\), \(h=(R-L)/2\). Two distinct unit circles intersect in at most two points; consequently each pair of left-endpoint functions, and likewise each pair of right-endpoint functions, can switch order at only finitely many heights unless they are identical, in which case duplicate centers may be removed. The positive-fiber interval therefore has a finite partition into intervals with fixed active pair \(i,j\).

**2. Exact local curvature.** On any such open interval,
\[
 h(y)=\frac{a_j-a_i}{2}+\frac{f_i(y)+f_j(y)}2,
 \qquad f_k(y)=\sqrt{1-(y-b_k)^2}.
\]
For a circular cap, \(f_k''=-(1+f_k'^2)^{3/2}\). The (unsigned) curvature of the smooth right boundary graph is
\[
 \kappa(y)=\frac{(1+f_i'(y)^2)^{3/2}+(1+f_j'(y)^2)^{3/2}}
 {2\left(1+\left((f_i'(y)+f_j'(y))/2\right)^2\right)^{3/2}}.
\]
Strict convexity of \(t\mapsto(1+t^2)^{3/2}\) gives \(\kappa(y)\ge1\), with equality if and only if \(f_i'(y)=f_j'(y)\). Since \(t\mapsto-t/\sqrt{1-t^2}\) is strictly decreasing, this happens if and only if \(b_i=b_j\). If heights differ, an entire positive-length analytic arc has curvature strictly greater than one.

**3. Necessity.** The boundary of a finite intersection of unit disks, away from finitely many circle intersections, consists of open arcs of unit circles, all with curvature exactly one. Therefore a smooth open arc of curvature strictly greater than one is impossible. The strict case of Step 2 rules out every active interval with unequal heights.

**4. Sufficiency.** If all active pairs have equal heights, on each interval \(h(y)=(a_j-a_i)/2+\sqrt{1-(y-b_i)^2}\). Both right and left boundary graphs there are arcs of unit circles; finitely many intervals give finitely many such arcs, whose closures cover the entire boundary, including switching heights and vertical extremes. The planar ball-body preservation theorem implies \(S(K)\) is an intersection of unit disks. At a smooth interior point of one of its circular arcs, at least one of these containing disks has boundary contact (choose a compact generating center set); the smooth outward normal forces its center to be the center of that arc's unit circle. Thus the disk defined by each arc contains \(S(K)\). Select one disk per arc and intersect them to form \(P\). Since every boundary point of \(S(K)\) lies on a selected circle, \(P=S(K)\): otherwise the segment from a point strictly inside \(S(K)\) to a point in \(P\setminus S(K)\) would meet the boundary of a selected disk while still strictly inside that disk, contradicting convexity. This proves sufficiency.

**5. Complete two-disk lens classification.** After rotating fiber coordinates, write the opposite original disk centers as \((p,q)\) and \((-p,-q)\), where \(p^2+q^2=a^2<1\). If either \(p=0\) or \(q=0\), reflection in the target symmetrization axis preserves the lens, hence the symmetral is the original two-disk lens. If \(pq\ne0\), reflect signs to take \(p,q>0\). At \(y=0\), the active left and right disks are different and their center heights \(q\) and \(-q\) differ. Their overlap width is positive because \(\sqrt{1-q^2}>p\). The active pair is stable on an open interval about zero. There the symmetral has
\[
 h(y)=-p+\tfrac12\bigl(\sqrt{1-(y-q)^2}+\sqrt{1-(y+q)^2}\bigr),
\qquad \kappa(0)=(1-q^2)^{-3/2}>1.
\]
Necessity proves non-finite representability. A countable unit-disk representation follows from the known existence of a closed representation and a countable dense set of centers in a compact subset of their possible centers: intersecting along a countable dense center set does not change the intersection.

## Verification
The proof reduces the decision to finitely many circle-circle switching heights and one explicit strictly convex scalar function. For the two-disk example with \(p=3/10\), \(q=2/5\), the local exact curvature is \((25/21)^{3/2}>1\), and the positive central fiber criterion holds because \(p^2+q^2=1/4<1\). The strict-convexity step is analytic, not a finite sampling extrapolation. If the input disks share all heights, every active pair passes and the output arcs have unit curvature as predicted.

## Relationship to prior work
Artstein-Avidan and Florentin prove in their Theorem 4.1 that the planar symmetral of any unit ball-body remains a unit ball-body; this important existence theorem is used in Step 4 and is **not** claimed as new. Their proof also uses curvature convexity. The present question is instead when a finite input admits a finite output representation, with an all-input active-pair criterion and sharp two-disk directional classification. Existing work on ball-lens curvature in dimensions at least three and Fodor–Vígh's best disc-polygon approximations treats other questions and does not supply this finite-representation criterion.

## Limitations
No optimal number of disks is claimed when finite. The criterion presupposes a full-dimensional planar intersection and a fixed common radius; it does not address unequal radii, non-Euclidean balls, higher-dimensional symmetrizations, or the complexity of approximate representations. This is a self-review, not an independent audit. Priority remains provisional in the face of potentially unindexed equivalent formulations.

## References
1. Shiri Artstein-Avidan and Dan I. Florentin, *Symmetrizations of Ball-Bodies*, arXiv:2602.14090v1 (first posted 15 February 2026), §4.1 and Theorem 4.1. https://arxiv.org/html/2602.14090
2. Ferenc Fodor and Viktor Vígh, *Disc-polygonal approximations of planar spindle convex sets*, Acta Scientiarum Mathematicarum 78 (2012), 331–350; full statement reprinted as Theorem 8.1.1 of Fodor's 2019 dissertation. https://real-d.mtak.hu/1259/8/dc_1638_19_doktori_mu.pdf
