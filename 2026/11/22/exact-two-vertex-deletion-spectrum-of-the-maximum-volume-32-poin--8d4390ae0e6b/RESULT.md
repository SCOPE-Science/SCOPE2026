# Exact two-vertex deletion spectrum of the maximum-volume 32-point spherical polytope

## Finding

Let \(\varphi=(1+\sqrt5)/2\) and \(u=\sqrt{(2+\varphi)/3}\). Start with the twelve vertices \(I\) of the regular edge-\(2\) icosahedron and the twenty points \(D\) of norm \(\sqrt3\) normal to its faces, as specified by the standalone exact-coordinate checker. Let \(K=\operatorname{conv}(I\cup uD)\), a rescaling of the unique maximum-volume 32-point spherical polytope. Delete any two distinct vertices and take the convex hull \(K'\) of the other thirty. The volume loss \(\operatorname{vol}(K)-\operatorname{vol}(K')\) has exactly five values, with complete multiplicities: (i) \(2d_I\) on all 66 pairs of icosahedral vertices; (ii) \(2d_D-\eta\) on exactly 30 pairs of face-normal vertices corresponding to adjacent icosahedral facets; (iii) \(2d_D\) on the other 160 face-normal pairs; (iv) \(d_I+d_D-\delta\) on the 60 incidence pairs consisting of a vertex and a facet containing it; and (v) \(d_I+d_D\) on the other 180 mixed pairs. Here \(\eta=(4+2\varphi-6u)/9\), \(d_I=\tfrac{10+5\varphi-5(1+\varphi)u}{9}\), \(d_D=1+\varphi/3-u\), and \(\delta=\frac{2+2\varphi-(8-2\varphi)u}{9}\). Equivalently, the two interaction deductions are \(\eta\) for adjacent face normals and the stated \(\delta\) for incidence pairs. These are positive at the specified parameter. In particular, among all 496 two-vertex erasures, the maximum volume loss is \(2d_D\), attained by exactly the 160 nonadjacent face-normal pairs; the minimum is \(2d_D-\eta\), attained precisely by 30 adjacent face-normal pairs.

The five levels, ordered by increasing loss, have approximate values and multiplicities \(0.8104344776\) (30), \(0.8254967763\) (66), \(0.8534201304\) (60), \(0.8539075797\) (180), and \(0.8823183830\) (160). These numbers are illustrative only; all equalities are exact in the formulas above.

## Assumptions and scope

The regular icosahedron is represented by all cyclic coordinate permutations of \((0,\pm1,\pm\varphi)\), with full edge length \(2\). Its twenty triangular faces are precisely the 20 triples with all pairwise squared distances \(4\). For each face \(f=\{i,j,k\}\), define \(D_f=(2-\varphi)(I_i+I_j+I_k)\). Then \(\lVert I_i\rVert^2=\varphi+2\), \(\lVert D_f\rVert^2=3\), and \(u=\sqrt{(2+\varphi)/3}\) makes both orbits lie on one sphere. Scaling by the common circumradius converts this to the unit-sphere volume maximizer without changing the classification (volumes scale by the cube of the radius).

A two-vertex erasure consists of an **unordered** pair of different members of the 32-point union. ``Adjacent face normals'' means that their underlying icosahedral faces share an edge; a mixed incidence pair means the icosahedral vertex belongs to the underlying face. Other pairs in each category are as stated.

## Proof

The coordinate-construction code verifies all 20 regular faces, their 30 edges and exact support inequalities. The unpunctured hull at the displayed parameter has 60 triangular facets with the exact positive orientation and volume \(20u^2\), proved by its exact 60-facet determinant computation.

For a finite erasure, select the triangular boundary mesh from a convex-hull candidate calculation, then independently verify in the algebraic field \(\mathbb Q(\varphi,u)\) that: each triangle lies in a supporting plane for every surviving vertex; each mesh edge appears in exactly two triangles; every remaining vertex is used; the mesh comprises \(2v-4\) triangles, for \(v=31\) or \(v=30\); and the oriented determinant sum divided by six equals the claimed volume. These conditions give a closed supporting triangulated boundary without missing facets, by the planar boundary topology of a three-dimensional convex polytope. The exact positivity check uses \(u^2=(2+\varphi)/3\) and the sign of \(a^2-b^2u^2\) when \(a+bu\) has opposing-sign terms. It therefore involves no floating-point uncertainty after candidate generation.

The icosahedral full symmetry group is explicitly constructed by mapping three linearly independent generating vertices to all triples with identical Gram matrix. Exactly 120 transformations result. They act transitively on each of twelve distance-and-type pair classes: three for icosahedron–icosahedron pairs, five for face-normal–face-normal, and four for mixed pairs. Those classes have sizes \(6,10,30,30,30,30,60,60,60,60,60,60\), summing to \(496\). The checker selects one exact representative of every class, plus one representative of each singleton orbit, and verifies 14 erasure meshes. Equal exact determinant sums coalesce the twelve pair orbits into five levels, with the exact multiplicities above. The inequality \(0<\delta<\eta\) and the distinct-level ordering follow by elementary comparisons in the same field. Consequently the worst two-point deletion and all equality cases are complete.

## Verification

Run `python deletion_certificate.py` from the same directory as `checker.py`, with Python 3, NumPy and SciPy installed. SciPy supplies only candidate triangulations. The 120 orbit maps, all supporting-plane signs, determinant volumes, and pair-class counts are checked in exact rational arithmetic in \(\mathbb Q(\sqrt5,u)\), using the minimal relations stated in the proof. The checker prints `PASS: 120 exact isometries, 12 complete pair orbits, 14 exact deletion hulls, five volumes, 496 pairs.`

## Relationship to prior work

Hoehner's November 2026 study determines the sharp maximum-volume 32-point sphere polytope and its icosahedral/face-normal geometric realization. The exact volume profile of the two-orbit radial interpolation, including its combinatorial thresholds, is also previously known and is **not** new here. The present claim instead gives the full two-site erasure robustness spectrum at the optimizing spherical realization: the five distinct exact losses, their complete multiplicities, and sharp worst/best deletion configurations. Related vertex deletion theorems for symmetric-edge polytopes concern different vertex configurations and do not imply these five values.

## Limitations

This theorem concerns one uniquely volume-maximizing 32-vertex spherical polytope. It makes no statement about arbitrary 32-point sphere sets, optimal reconfiguration of surviving points, deletion of three or more vertices, or a new proof of the known maximum-volume theorem. Historical priority is not independently certified. Candidate hull triangulations use floating-point computation for discovery, but the final finite certificate checks the necessary geometry and determinant identities exactly. Independent mathematical audit has not been performed.

## References

- Steven Hoehner, *On maximum volume polytopes inscribed in the sphere*, arXiv:2611.10777, first posted 2026-11-07, especially Theorem 1.4 and the 32-vertex construction.
- Related published geometric deletion results on complete-bipartite symmetric-edge polytopes and complete type-A root polytopes (for contrast; not asserted equivalent).
