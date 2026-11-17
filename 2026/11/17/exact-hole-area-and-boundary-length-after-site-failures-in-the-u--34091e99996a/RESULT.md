# Exact hole area and boundary length after site failures in the unit triangular-lattice disk covering

## Finding
Let \(e_1=(1,0)\), \(e_2=(1/2,\sqrt3/2)\), and \(\Lambda=\mathbb Ze_1+\mathbb Ze_2\). Put a **closed disk of radius one** at each retained site. For a finite set \(S\subset\Lambda\) of deleted sites define the uncovered open set
\[
U_S=\mathbb R^2\setminus\bigcup_{p\in\Lambda\setminus S}\overline B(p,1).
\]
An elementary face means a unit equilateral triangular face of the standard lattice triangulation. Let \(F(S)\) count faces whose three vertices have been deleted and \(B(S)\) count the elementary sides incident to exactly one such face. Then the following **exact global laws** hold:
\[
\boxed{\ |U_S|=\frac{\sqrt3}{4}F(S)-\left(\frac\pi6-\frac{\sqrt3}{4}\right)B(S),\qquad
\mathcal H^1(\partial U_S)=\frac\pi3 B(S).\ }
\]
The boundary measure is the ordinary one-dimensional Hausdorff measure and both quantities vanish if the uncovered set is empty. In particular, \(U_S\ne\varnothing\) **if and only if** \(F(S)>0\). No one- or two-site erasure produces a hole; a three-site erasure does so precisely if the sites form an elementary face, and its uncovered area is then \(\sqrt3-\pi/2\) and its boundary length is \(\pi\).

Equivalently, if \(I(S)\) counts unordered edge-adjacent pairs of fully deleted faces, then \(B=3F-2I\), and the damage law is
\[
|U_S|=\left(\sqrt3-\frac\pi2\right)F(S)+\left(\frac\pi3-\frac{\sqrt3}2\right)I(S).
\]
Thus neighboring fully failed faces have a strictly positive additional area effect, beyond their isolated-face costs.

For independently deleted lattice sites with probability \(q\in[0,1]\), put unit disks at the retained sites. Almost surely, as \(R\to\infty\), the uncovered area fraction in \(B(0,R)\) tends to
\[
\boxed{\ \phi(q)=q^3\left[4-\frac{2\pi}{\sqrt3}+\left(\frac{2\pi}{\sqrt3}-3\right)q\right].\ }
\]
The almost-sure boundary-length density of the uncovered set tends to
\[
\boxed{\ \ell(q)=\frac{4\pi}{\sqrt3}q^3(1-q).\ }
\]
These formulas also cover the deterministic extreme cases \(q=0\) and \(q=1\), with boundary density zero at both endpoints.

## Assumptions and scope
The radius **equals the nearest-neighbor lattice spacing**, rather than the smaller radius of a minimally redundant triangular-lattice covering. The deleted set is arbitrary but finite for the exact global area and perimeter identities. The Bernoulli model has independent identically distributed deletion statuses on the entire infinite lattice. All statements are planar Euclidean, at their stated exact radius; no generalization to nonunit radius or irregular sites is claimed. Areas and boundary lengths for finite deletions are finite.

## Proof
**1. Locality lemma.** Tile the plane by unit equilateral faces. If any one of a face's vertices remains, its closed unit disk contains the entire face: the distance to that vertex is convex over the triangle and has maximum one at either other vertex. Therefore any uncovered point is in a face whose three vertices are deleted (except irrelevant tiling-edge conventions).

Fix the face \(T=\operatorname{conv}\{0,e_1,e_2\}\). Among sites outside its three vertices, precisely the three sites opposite its edges can lie at distance strictly less than one from a point in the interior of \(T\). They are \(e_1-e_2\), \(e_1+e_2\), and \(e_2-e_1\). Here is a direct exhaustive geometric argument: for a lattice point outside the triangle, its nearest point on \(T\) is on an edge or at a vertex. If at a vertex, the nearest distance is at least the lattice minimum one. If at the interior of the edge from \(0\) to \(e_1\), the point must lie in the outer half-plane, with second lattice coordinate \(j\le-1\). Its perpendicular distance is \(\sqrt3|j|/2\), so distance less than one forces \(j=-1\); its projected abscissa is \(i-1/2\) and lies strictly between zero and one only if \(i=1\). That is \(e_1-e_2\). Rotating this calculation through \(120^\circ\) yields the other two sites. Every other lattice site has distance at least one from all of \(T\), hence cannot cover any positive-area part of its interior.

**2. Circular caps.** Each of the three opposite sites is at perpendicular distance \(\sqrt3/2\) from its corresponding side of \(T\). Its unit disk intersects \(T\) in a circular cap of area
\[
c=\arccos(\sqrt3/2)-(\sqrt3/2)\sqrt{1-3/4}=\frac\pi6-\frac{\sqrt3}{4},
\]
bounded on the interior by a unit-radius circular arc of central angle \(\pi/3\), hence arc length \(\pi/3\). The cap extends no farther than its associated two side endpoints; this follows from the fact that the opposite disk meets each other side of \(T\) only at the shared endpoint. The three opposite sites have pairwise distance exactly two, so their closed disks are pairwise tangent at those endpoints and their cap interiors are disjoint.

If \(T\) has three deleted vertices, its uncovered portion is exactly \(T\) minus the caps belonging to those opposite sites that survive. An opposite site survives exactly when the face on the opposite side of that edge is *not* fully deleted (because the other two endpoints of the edge are already deleted). Thus if a deleted face has \(b_T\) boundary sides, its uncovered area contribution is \(\sqrt3/4-cb_T\). Summing over deleted faces and noting \(\sum_Tb_T=B(S)\) proves the area identity. On each boundary side, the circular cap interior arc separates the uncovered portion from a retained disk, while on each edge shared by two deleted faces the uncovered portions join across an open edge interval. There are no other positive-length boundary portions: lattice edges and vertices not in these two classes are covered by retained disks, and any exceptional vertex contributes zero one-dimensional measure. Each boundary side therefore contributes exactly one arc of length \(\pi/3\), establishing the perimeter identity.

**3. Sharp robustness criterion.** The local uncovered portion of each fully deleted face has area at least \(\sqrt3/4-3c=\sqrt3-\pi/2>0\). When no face is fully deleted every point is covered by an undeleted vertex of one of its incident faces. Consequently \(U_S\ne\varnothing\) precisely when \(F(S)>0\). The criterion for at most three failed sites and the single-face value follow immediately.

**4. Random independent failures.** The area of one lattice face is \(a=\sqrt3/4\), giving \(1/a=4/\sqrt3\) faces per unit area. For any fixed face, it is fully deleted with probability \(q^3\). The probability that any specified boundary side belongs to a fully deleted face but has a surviving opposite vertex is \(q^3(1-q)\), involving four distinct sites. The mean local uncovered area is
\[
aq^3-3cq^3(1-q).
\]
Dividing by \(a\) and substituting \(c=\pi/6-\sqrt3/4\) gives \(\phi(q)\). The mean boundary-arc length per face is \((\pi/3)3q^3(1-q)\); division by \(a\) gives \(\ell(q)\). Because both face contributions are bounded local functions of finitely many independent deletion indicators, the lattice ergodic theorem implies almost-sure convergence of their spatial averages. A disk of radius \(R\) intersects only \(O(R)\) faces across its boundary, contributing at most \(O(R)\) errors to area and boundary length, whereas disk area is order \(R^2\). This transfers the limits from unions of complete faces to circular windows. The endpoint cases are immediate.

## Verification
The accompanying standard-library script `check.py` generates finite deletion sets, counts fully deleted elementary faces and their shared edges, and checks the formula against an independent midpoint integration of distance to retained lattice sites. It also enumerates all \(2^6\) local survival/deletion patterns and checks the polynomial formula for several probabilities. The discrete midpoint integrals are finite numerical checks only; the unrestricted and almost-sure claims follow from the proof above.

An isolated deleted elementary face gives exactly \(F=1\), \(B=3\), area \(\sqrt3-\pi/2\approx0.1612544808\), perimeter \(\pi\). Two adjacent deleted faces give \(F=2\), \(B=4\), area \(2(\sqrt3-\pi/2)+(\pi/3-\sqrt3/2)\approx0.5036811090\), perimeter \(4\pi/3\).

## Relationship to prior work
Johnson and coauthors' *More is More: The Benefits of Denser Sensor Deployment* (INFOCOM 2009, DOI 10.1109/INFCOM.2009.5061942), particularly Section V, studies coverage resilience of denser hexagonal/triangular sensor lattices after independent sensor failures and bounds or simulates local coverage multiplicity. The present theorem fixes the edge-to-disk-radius ratio to one and gives instead exact total **uncovered area, its boundary length, and all-failure-probability spatial density** from face-adjacency counts. The cited local multiplicity lower bound is not an expression for these observables. Sykes and Essam (1964, DOI 10.1063/1.1704215) studied triangular-lattice site-percolation thresholds, not disk-union loss areas. Standard circle-segment area calculus is used and is not claimed as new.

## Limitations
No statement is made about arbitrary nonunit radii, finite observation domains with external boundaries, general point patterns, or the topology of infinite failed clusters. The result describes deterministic finite deletions and spatial densities of i.i.d. infinite failures, not probabilities of full coverage of a finite sensor field. The independent-failure formula depends on lattice geometry and should not be applied to a minimally redundant triangular deployment. Historical priority beyond the inspected directly relevant research remains open to independent review.

## References
1. M. P. Johnson et al., *More is More: The Benefits of Denser Sensor Deployment*, INFOCOM 2009, DOI: 10.1109/INFCOM.2009.5061942. Conference listing dated April 19, 2009; a separately maintained institutional publication page is dated October 12, 2009.
2. M. F. Sykes and J. W. Essam, *Exact Critical Percolation Probabilities for Site and Bond Problems in Two Dimensions*, J. Math. Phys. 5 (1964), 1117–1127, DOI: 10.1063/1.1704215.
