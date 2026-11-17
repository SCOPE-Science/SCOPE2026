# A signed integral sphere lattice at the four-cycle boundary of toroidal three-cut complexes

## Finding
For every integer \(n\ge5\), let \(G=C_4\square C_n\) and let \(\Delta=\Delta_3(G)\) be its ordinary three-cut complex, with facets the complements of **disconnected induced triples**. Put \(K=\Delta^\vee\), the Alexander dual on the complete \(4n\)-vertex ground set. Then
\[
|K|\simeq\bigvee^{8n(n-3)+1}S^1\vee\bigvee^nS^2.
\]
Consequently, the full reduced integral homology of the original cut complex is
\[
\widetilde H_j(\Delta;\mathbb Z)\cong
\begin{cases}
\mathbb Z^n,&j=4n-5,\\
\mathbb Z^{8n(n-3)+1},&j=4n-4,\\
0,&\text{otherwise}.
\end{cases}
\]
The new equivariant assertion identifies a **primitive integral basis** \(z_b\) of \(H_2(K;\mathbb Z)\), indexed by \(b\in\mathbb Z/n\mathbb Z\), in which the full coordinate-dihedral action is
\[
 r_4z_b=z_b,\quad s_4z_b=-z_b,\qquad
 r_nz_b=z_{b+1},\quad s_nz_b=-z_{-b-1}.
\]
Here the generators act on coordinates by \(r_4(a,b)=(a+1,b)\), \(s_4(a,b)=(-a,b)\), \(r_n(a,b)=(a,b+1)\), and \(s_n(a,b)=(a,-b)\), with residues taken in the indicated factors. The full-group fixed integral and rational second homology vanish. The ordinary cut complex is pure and nonshellable.

The non-equivariant homotopy type is an explicit specialization of the earlier general square-filling theorem [3]; **the new assertion is the geometric integral dihedral lattice, including its primitive basis and all reflection signs**, in the short-period family excluded from earlier ordinary toroidal-grid classifications [4,5].

## Assumptions and scope
The graph is finite, simple, undirected, with vertices \((a,b)\in\mathbb Z/4\mathbb Z\times\mathbb Z/n\mathbb Z\). Adjacent vertices differ by one in precisely one coordinate. We assume \(n\ge5\), so each opposite vertex pair has at most two common neighbors. Each group generator above is a graph automorphism. We use the ordinary cut complex, not the total cut complex, and integral simplicial homology. The square filling \(S(G)\) is the two-dimensional CW complex attaching one square disk along each (unoriented) embedded graph four-cycle. Its cellular homology maps canonically to the homology of the Alexander dual through the square-cycle reduction, as explained below. All indices in the formulas are modulo their cycle length.

## Proof
**1. Complete Alexander-dual faces and collapse.** A face of \(K\) is exactly a set whose every induced triple is connected. Because \(G\) is triangle-free, admissible triples induce two-edge paths. Its admissible four-sets induce precisely embedded four-cycles, and there are no admissible five-sets: ten connected triples would contribute twenty edge incidences, whereas each edge of a five-set contributes three incidences. There are \(4n\) ordinary coordinate squares and \(n\) additional four-cycles traveling completely around the \(C_4\) factor, so there are \(5n\) tetrahedral faces of \(K\). Every opposite pair has exactly two common neighbors, while a remaining distance-two pair has exactly one. For each four-cycle, collapse its tetrahedron through one free triangular face and then collapse the now-free diagonal edge through a second triangle. For every remaining distance-two pair with a unique common neighbor, collapse its sole triangle through that pair. The latter class has exactly \(4n\) pairs. Each step is an elementary simplicial collapse, since distinct four-cycles share no opposite-vertex pair. There are \(14n\) elementary pairs in total. The surviving complex triangulates the square filling \(S(G)\), with one additional edge for every vertex pair at graph distance at least three. All such edges attach at existing vertices and are in no triangles.

There are \(8n\) original graph edges, \(10n\) pairs that are diagonals of the \(5n\) squares, and \(4n\) other distance-two pairs. The \(\binom{4n}{2}\) pairs therefore include exactly
\[
L=\binom{4n}{2}-8n-10n-4n=8n(n-3)
\]
pairs at distance at least three. Hence \(K\simeq S(G)\vee\bigvee^L S^1\). This general reduction is known in the broader no-\(K_{2,3}\) triangle-free setting [3] and is reproduced here to specify the exact equivariant chain model.

**2. Homotopy and two sphere degrees.** The \(4n\) coordinate-square disks form the standard square cellulation of the torus \(S^1\times S^1\). The other \(n\) disks cap the \(n\) pairwise parallel meridian loops \(\{b\}\times C_4\). Attaching the first disk kills that meridian generator of the torus fundamental group; its commutator two-cell then attaches trivially, producing \(S^1\vee S^2\). Every remaining meridian is freely homotopic to the now-null first meridian and each additional cap contributes one independent two-sphere. Therefore
\[
S(G)\simeq S^1\vee\bigvee^n S^2,
\]
and the homotopy formula for \(K\) follows. The two-sphere wedge also implies that all products of positive-degree degree-one cohomology classes of \(K\) vanish; this contrasts with the persistent torus cup product in the previously studied two-long-cycle products [4,5].

**3. Primitive integral lattice.** Orient the coordinate four-cycle \(c_b\) in the increasing first coordinate direction. Let \(D_b\) be its oriented cap disk, with \(\partial D_b=c_b\). Let \(Q_{a,b}\) be the oriented elementary square from \((a,b)\) through \((a+1,b)\), \((a+1,b+1)\), \((a,b+1)\). Set \(A_b=\sum_{a\in\mathbb Z/4}Q_{a,b}\), so \(\partial A_b=c_b-c_{b+1}\). Define the cellular two-cycle
\[
 z_b=A_b-D_b+D_{b+1}.
\]
The support is precisely the sphere made from a four-square annulus capped at both ends. To verify **integral** primitivity without relying on rational ranks, take an arbitrary integral two-cycle \(Z\) in \(S(G)\). The coefficient of a vertical first-coordinate edge in its cellular boundary is the difference between the coefficients of two neighboring elementary squares. Hence all four square coefficients in each strip are equal to an integer \(\lambda_b\). The remaining horizontal-edge equations uniquely force the cap coefficient at column \(b\) to be \(\lambda_{b-1}-\lambda_b\). Thus \(Z=\sum_b\lambda_b z_b\). There are no three-cells in \(S(G)\), so these \(n\) cycles form a primitive, free integral basis of \(H_2(S(G);\mathbb Z)\cong\mathbb Z^n\).

To transfer this basis to \(K\), triangulate each square disk using its diagonal. Each two-triangle sum is a chain in \(K\) whose oriented boundary is the original four-cycle. Changing the diagonal changes this chain by the signed boundary of the corresponding tetrahedron, hence not its homology class. Every remaining non-square two-path triangle has a private distance-two edge and disappears in the elementary chain cancellation. Consequently this correspondence identifies \(H_2(S(G);\mathbb Z)\) with \(H_2(K;\mathbb Z)\) **naturally under graph automorphisms**, even though the particular collapse choices are not themselves equivariant. The classes \(z_b\) therefore give a canonical up-to-orientation integral homology lattice in the original dual.

**4. Exact dihedral action.** Each \(C_4\) rotation preserves the orientations of \(A_b,D_b\), while its reflections reverse both, yielding \(r_4z_b=z_b\) and \(s_4z_b=-z_b\). A \(C_n\) rotation sends \((A_b,D_b)\) to \((A_{b+1},D_{b+1})\), so \(r_nz_b=z_{b+1}\). A \(C_n\) reflection sends \(A_b\mapsto-A_{-b-1}\) and \(D_b\mapsto D_{-b}\), whence \(s_nz_b=-z_{-b-1}\). These equations determine the full **integral**, not merely rational, \(D_4\times D_n\) representation. In particular the first-factor reflection is negative identity and forces the full-group fixed sublattice to vanish. The sum \(\sum_bz_b\), the fundamental torus two-cycle, generates the sublattice fixed by cyclic translations in the second factor. No assertion is made that the corresponding homotopy wedge splits equivariantly.

**5. Alexander duality.** With \(N=4n\), combinatorial Alexander duality gives \(\widetilde H_j(\Delta;\mathbb Z)\cong\widetilde H^{N-j-3}(K;\mathbb Z)\). The free cohomology of the proved sphere wedge yields precisely the two integral groups displayed above. Every facet of \(\Delta\) has \(N-3\) vertices, so \(\Delta\) is pure of dimension \(N-4\). The nonzero group in dimension \(N-5\) obstructs pure shellability.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter; no external packages are needed. The checker reconstructs the dual directly from connected-triple constraints for \(n=5,6,7,8\), exhaustively enumerates all tetrahedra and possible five-faces, checks the actual free faces of all \(14n\) prescribed collapse pairs, and checks the complete residual graph and square triangulation. It independently reduces the original simplicial boundary matrices over \(\mathbb F_2\), giving first and second Betti vectors \((81,5),(145,6),(225,7),(321,8)\) in those four cases. A second checker uses **signed integral cellular boundaries**, constructs every \(z_b\) with its exact oriented coefficients, checks \(\partial z_b=0\), verifies a primitive coordinate identity minor, and checks the signed actions of all four dihedral generators for each \(n\). Successful replay prints `THIN_TORUS_THREE_CUT_PASS` and `INTEGRAL_SYMMETRY_PASS`. The infinite theorem follows from the chain and topological arguments, not from the finite checks.

## Relationship to prior work
Bayer and collaborators [1] classify cut complexes of rectangular path grids, with different boundary conditions. Carnero Bravo [2] studies newer total-cut and bounded-independence constructions for cycle powers and certain Cartesian products, providing the timely motivation for investigating omitted periodic boundaries. The previously published general square-filling theorem [3] **already implies the non-equivariant homotopy and homology parts here**, once this family's square-filling topology is computed. They are therefore *not* claimed as independent general novelty. Two previously published periodic-grid results [4,5] cover products of cycles whose lengths are both at least five, but explicitly exclude a four-cycle factor and determine no integral action there. The independently meaningful contribution is the **complete primitive signed integral dihedral module** for this boundary family. An earlier result about a signed edge-permutation lattice for a scale-two Vietoris–Rips complex of a different cycle product [6] has similar representation structure but refers to a different complex and does not imply the present cut-complex statement. No inspected statement gives the present integral basis or its dihedral action.

## Limitations
The hypothesis \(n\ge5\) excludes the four-by-four product, whose square list has further identifications. The topological decomposition concerns the **Alexander dual** \(K\), not a homotopy wedge decomposition of \(\Delta\); the latter's full integral homology is determined. The homology lattice is equivariant, but the collapse and homotopy wedge decomposition are not asserted equivariant. The two non-equivariant formulas are corollaries of the published general square-filling theorem [3]. The originality of an abstract presentation of the integral symmetry lattice beyond the inspected literature cannot be guaranteed; a differently described equivalent action could exist. Self-review is not independent mathematical validation.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public 2024-07-11), particularly Section 5.

[2] A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first public 2026-02-24), especially the introduction and Section 5.4.

[3] *Square-filling theorem for ordinary three-cut complexes of triangle-free graphs*, public mathematical record 8942f5d1eacf (2026-11-01); its statement and proof were examined in full.

[4] *Toroidal three-cut complexes retain an integral fundamental-surface class*, public mathematical record 4a74053b5bd8 (2026-10-25); full statement and proof compared.

[5] *Toroidal-grid three-cut complexes retain two adjacent integral homology degrees*, public mathematical record b2790592d78c (2026-11-01); full statement and proof compared.

[6] *Integral dihedral homology characters of five-by-long toroidal Rips complexes*, public mathematical record 8c315c4b44d0 (2026-10-25); relevant published summary compared, not a full-text inspection.
