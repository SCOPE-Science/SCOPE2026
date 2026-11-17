# Sharp FCC Kuhn-packet radius and all 24 minimizing frames

## Finding
Let \(D_3=\{z\in\mathbb Z^3:z_1+z_2+z_3\equiv0\pmod2\}\) be the standard face-centered-cubic lattice, with Euclidean norm. For each linearly independent lattice triple \(B=(b_1,b_2,b_3)\), not necessarily a lattice basis, form the six permutation tetrahedra
\[
\Delta_\sigma(B)=\operatorname{conv}\{0,b_{\sigma(1)},b_{\sigma(1)}+b_{\sigma(2)},b_1+b_2+b_3\},\qquad\sigma\in S_3.
\]
Write \(r(S)=\inf_c\max_{x\in S}\|x-c\|_2\), and define the original common-frame Kuhn-packet radius \(\kappa(B_2^3,D_3)=\inf_B\max_\sigma r(\Delta_\sigma(B))\). Then
\[
\boxed{\kappa(B_2^3,D_3)=\mu(B_2^3,D_3)=1.}
\]
There are exactly **24 unordered minimizing frames** (and 144 ordered frames). They are precisely the triples of roots \(b_i\in D_3\) of squared length \(2\) whose off-diagonal pairwise inner-product multiset is \(\{-1,-1,0\}\). Every such frame is a full lattice basis. This classification is over **all independent triples**, including proper-sublattice frames as candidates.

## Assumptions and scope
The fitting ball is allowed to have a different center for each permutation tetrahedron, but the three independent lattice vectors are held common to all six. The lattice normalization is the integral even-coordinate-sum root lattice \(D_3\). This statement addresses the FCC lattice alone: it does not claim a new result about the dual BCC lattice, whose complete optimal-frame classification and sharp second level were established separately before the present analysis. The classical covering radius \(\mu\) is the supremum of Euclidean distance to the nearest lattice point.

## Proof
**1. Diameter obstruction valid for every independent lattice triple.** If a triple has packet radius at most \(R\), every nonempty subset sum of its three vectors has Euclidean length at most \(2R\). Indeed, an ordering beginning with that subset has both the origin and the partial sum among the vertices of one permutation tetrahedron. Thus any candidate with packet radius at most \(1\) must have every nonempty subset sum of squared norm at most \(4\).

**2. Exhaustive short-vector reduction.** The nonzero \(D_3\) vectors of squared norm at most four consist of the twelve roots \((\pm1,\pm1,0)\) and coordinate permutations (squared norm \(2\)), together with six axis vectors \(\pm2e_i\) (squared norm \(4\)). Suppose a frame contains the axis vector \(a=2e_1\) after signed coordinate permutation. The other two independent vectors must be roots with first coordinate \(-1\), because each pair sum with \(a\) has squared norm at most \(4\). Their pair sum must have squared norm at most \(4\) and first coordinate \(-2\), forcing the sum to equal \(-a\). This contradicts independence. Hence every candidate frame consists entirely of roots.

Each root has squared norm two. The pair subset-sum bounds and root inner products restrict each off-diagonal Gram entry to \(-1\) or \(0\): equal or opposite roots are linearly dependent, and positive inner product gives a pair sum longer than two. The total three-vector sum must have squared length at most \(4\), so there is at least one \(-1\). If there is exactly one \(-1\), the Gram determinant is \(6\), impossible because the frame matrix has integer determinant and its Gram determinant is its square. Three \(-1\) entries give Gram determinant zero. Therefore precisely two entries are \(-1\) and one is zero. The Gram determinant is four, giving frame determinant of absolute value two, which equals the covolume of \(D_3\). Thus every surviving frame is a full lattice basis.

There are twelve unordered orthogonal root pairs: each of the twelve roots has exactly two orthogonal root partners. Each such pair extends in precisely two ways to a third root having inner product \(-1\) with both partners. The orthogonal pair is unique in each triple, so the count is exactly \(12\cdot2=24\) unordered frames.

**3. Every surviving packet attains radius one.** Label an eligible triple \((u,v,w)\), where \(u\cdot v=0\), \(u\cdot w=v\cdot w=-1\), and all three norms are \(\sqrt2\). When \(u\) and \(v\) occur consecutively in the permutation, the tetrahedron includes a pair of vertices differing by \(u+v\), of norm two. The midpoint of this diameter lies at squared distance at most one from all four vertices, so those four permutation tetrahedra have minimum enclosing radius one. For the two remaining orders, all six tetrahedral edge lengths are \(\sqrt2\); these are regular tetrahedra with squared circumradius \(3/4\), which is also their minimum enclosing-ball squared radius. Hence the packet radius of each of the 24 frames is exactly one. The preceding necessary enumeration excludes every other independent frame of packet radius at most one, proving the sharp global infimum and all equality cases.

**4. Classical covering radius.** The general packet-to-covering inequality \(\mu(B_2^3,D_3)\le\kappa(B_2^3,D_3)\) is Xue's Proposition 2.4. Conversely the point \((1,0,0)\) has nearest \(D_3\)-lattice distance exactly one: every even-sum integer point is at least distance one, and both \((0,0,0)\) and \((1,1,0)\) attain it. Combining this deep-hole lower bound with the constructed packet gives \(\mu=\kappa=1\).

## Verification and limits
The original package's `verify_packet.py` exhaustively enumerates the finite root/axis candidates forced by the subset-sum obstruction, tests Gram patterns and determinants with integer arithmetic, and verifies each of the six packet tetrahedra with rational ball-center calculations. Its FCC checks report exactly 24 unordered optimal frames and 96 packet tetrahedra of squared radius 1 and 48 of squared radius 3/4. Other BCC computations still present in that unchanged program are independent supplemental comparisons, not part of this narrowed theorem. Finite computation alone does not establish the unrestricted result: the universal subset-sum argument does. The claim is confined to this Euclidean normalization of the three-dimensional FCC lattice and does not assert arbitrary-lattice equality or historical completeness of lattice-frame terminology.

## Relationship to earlier results
Fei Xue, *On κ-covering minima*, arXiv:2610.39034 (October 28, 2026), introduced the invariant, proved \(\mu\le\kappa\), and distinguished the original common-frame invariant from a more flexible extended triangulation variant. Those general inequalities and the known FCC covering radius do not imply the above common-frame optimizer classification. The separately published *Rigid optimal Kuhn packets and the sharp second level for the body-centered cubic lattice* establishes the full analogous BCC theorem, so no BCC novelty is claimed here. Koca et al., *Explicit Construction of the Voronoi and Delaunay Cells of W(A_n) and W(D_n) Lattices and Their Facets*, arXiv:1804.05836 (2018), describe classical lattice cell geometry; their complete text was not materially verified, leaving a residual historical-priority risk for an equivalent FCC frame enumeration.

## References
- Fei Xue, *On κ-covering minima*, arXiv:2610.39034v1, https://arxiv.org/abs/2610.39034.
- *Rigid optimal Kuhn packets and the sharp second level for the body-centered cubic lattice*, published mathematical finding, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-rigid-optimal-kuhn-packets-and-the-sharp-second-level-for-the-bo--8e6d7843a500.
- M. Koca, N. O. Koca, A. Al-Siyabi and R. Koc, *Explicit Construction of the Voronoi and Delaunay Cells of W(A_n) and W(D_n) Lattices and Their Facets*, arXiv:1804.05836, https://arxiv.org/abs/1804.05836.
