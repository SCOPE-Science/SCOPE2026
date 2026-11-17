# A primitive codimension-one cap-cycle lattice in ternary affine matroid homology

## Finding
Let \(P=\mathbb F_3^2\), and let \(K\) be the independence complex of the rank-three affine-plane matroid on its nine points. Thus its two-faces are precisely the noncollinear triples of points. For every four-point cap \(Q\subset P\) (no three points collinear), its oriented tetrahedral boundary is a two-cycle \(z_Q\) in \(K\). There are exactly \(54\) caps, a single orbit under affine automorphisms.

Let \(L=\sum_Q\mathbb Z z_Q\subseteq\widetilde H_2(K;\mathbb Z)\). The integral homology is torsion-free and concentrated in degree two, and the exact geometric-lattice statement is
\[
\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^{44},\qquad
\operatorname{rank}L=43,\qquad
\widetilde H_2(K;\mathbb Z)/L\cong\mathbb Z.
\]
Moreover, up to nonzero scalar, the \(54\) cap boundaries are all integral two-cycles with minimum nonempty triangle support, which is four. Every cap boundary is primitive in integral homology.

A canonical affine-orientation functional identifies the quotient. If \([p,q,r]\) is an oriented noncollinear triangle, define \(a(p,q,r)=+1\) when \(\det(q-p,r-p)=1\) in \(\mathbb F_3\), and \(-1\) when it equals \(2\). For integral two-cycles \(z=\sum z_{pqr}[p,q,r]\),
\[
\Phi(z)=\frac{1}{6}\sum_{[p,q,r]}a(p,q,r)z_{pqr}\in\mathbb Z,
\qquad\ker\Phi=L,\qquad\operatorname{im}\Phi=\mathbb Z.
\]
On this one-dimensional integral quotient, \(\operatorname{AGL}_2(\mathbb F_3)\) acts via \(\epsilon(\det g)\), where \(\epsilon(1)=+1\) and \(\epsilon(2)=-1\).

## Assumptions and scope
Vertices are all ordered pairs in \(\{0,1,2\}^2\), numbered lexicographically as in `verify.py`. A line is the three-point set determined by any two distinct points. The matroid-independent faces are exactly the nine vertices, all \(36\) edges, and the \(72\) noncollinear triangles; the \(12\) collinear triples are excluded. Homology is ordinary reduced simplicial homology over \(\mathbb Z\). Orient all faces by increasing vertex index. A cap is a subset of four vertices every triple of which is independent; each cap is an affine parallelogram.

## Proof
**1. The full homology lattice.** The one-skeleton of \(K\) is the complete graph on nine vertices. Its integral cycle lattice \(\ker(\partial_1)\) is free of rank \(\binom{9}{2}-9+1=28\). The boundary map \(\partial_2:\mathbb Z^{72}\to\mathbb Z^{36}\) has rank \(28\) and a unimodular \(28\times28\) minor, using the triangle columns indexed `list(range(25))+[32,36,37]` and the edge rows `[0,1,2,3,4,5,6,8,9,10,11,12,13,15,16,17,18,19,21,22,23,24,26,27,28,30,31,33]` in lexicographic order. The determinant is \(-1\). Therefore the image of \(\partial_2\) is a saturated rank-\(28\) sublattice of the graph cycle lattice, hence all of it. Consequently \(\widetilde H_1(K;\mathbb Z)=0\) and \(\widetilde H_2(K;\mathbb Z)=\ker\partial_2\cong\mathbb Z^{72-28}=\mathbb Z^{44}\). An explicit integral kernel basis is obtained by choosing the other \(44\) triangles as free coordinates and solving for the \(28\) pivot coordinates over integers using the unimodular minor. No two-faces are boundaries of three-chains, since \(K\) is two-dimensional.

**2. Integral primitivity of the cap span.** Exhausting the \(\binom94=126\) four-point sets gives \(54\) caps. Express their tetrahedral boundaries in the preceding kernel basis: one simply retains the \(44\) free coordinates of each boundary, giving an integral \(44\times54\) matrix \(R\). For the rows `[0,...,40,42,43]` and columns `[0,...,26,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44]` (zero-based indices), the determinant of the \(43\times43\) submatrix is \(-1\). Thus \(L\) is a primitive rank-at-least-\(43\) sublattice; the next step proves rank at most \(43\).

**3. A geometric functional and exact cokernel.** Let \(a\) be the orientation sign defined in the finding. For every cap \(Q\), the signed sum of the values of \(a\) on the four triangle faces of its tetrahedral boundary vanishes; this is checked for all \(54\) caps in `verify.py`. On the constructed \(44\) element integral kernel basis, the raw sum \(z\mapsto\sum a z\) takes value \(0\) on \(32\) basis elements, \(+6\) on \(6\), and \(-6\) on \(6\). Hence \(\Phi=\frac16\sum a z\) is integral on *every* two-cycle and is surjective. It annihilates \(L\), forcing \(\operatorname{rank}L\le43\). Combining with the unimodular minor, \(L\) is a primitive rank-\(43\) sublattice contained in the primitive rank-\(43\) subgroup \(\ker\Phi\). Two such sublattices coincide, giving \(L=\ker\Phi\) and the asserted infinite cyclic cokernel. An explicit cycle with \(\Phi=1\) is
\[
-[0,1,3]+[0,1,6]+[0,2,3]-[0,2,6]-[1,2,3]+[1,2,6].
\]
Here the brackets refer to the above vertex indices; its boundary vanishes term by term after summation.

**4. Symmetry and minimum support.** An affine map \(g(p)=Ap+b\), \(A\in\operatorname{GL}_2(\mathbb F_3)\), multiplies the area sign by \(\epsilon(\det A)\) after accounting for orientation permutation; hence the action on \(\Phi\) and on the cokernel is the determinant-sign character. The \(48\) invertible linear maps and nine translations yield \(432\) affine maps, and the orbit of any cap has size \(54\). Finally, in a two-dimensional subcomplex of a simplex, a nonzero integral two-cycle needs at least four triangular faces: with fewer faces some edge occurs in only one face. With exactly four, cancellation at every edge forces the four faces of a single tetrahedron, with coefficients determined up to scalar by its orientation. All four faces are in \(K\) exactly when their four vertices form a cap. A cap boundary has coefficients \(\pm1\), so is primitive.

## Verification
Run `python3 verify.py` with the Python standard library; it rebuilds all points, lines, independent triangles, caps, boundary matrices and the integral kernel basis from definitions. Bareiss exact determinants certify the two displayed unimodular minors; rational Gauss–Jordan elimination constructs an exact integral boundary section; all \(432\) affine maps and the orientation-sign rule are checked. The output is reproduced in `verification_output.txt` and ends with `AG23_GEOMETRIC_CYCLES_PRIMITIVE_CODIM_ONE_PASS`. The finite enumeration is exhaustive for this nine-point matroid, not an extrapolation to larger affine planes.

## Relationship to prior work
Ardila–Castillo–Samper (2014) give general shellings of matroid independence complexes and their topological consequences; their theorem does not identify which particular four-point cap spheres generate a saturated subgroup, or an affine-orientation quotient. Moci–Pezzoli (2020) develop symmetry representations of matroid homology using duality and the lattice of flats; their generic framework does not supply this explicit integral geometric sublattice computation. Other known studies address projective-plane matroids, point-line incidence Vietoris–Rips complexes, or Fourier minors on the affine plane: these concern different spaces or invariants. The present result is a new object-specific identification of the primitive cap span and its one-dimensional affine orientation obstruction, not a claim that matroid independence homology or its basic rank is new.

## Limitations
This result concerns the nine-point rank-three ternary affine matroid only. It does not classify analogous lattices for other affine planes, the full \(44\)-dimensional integral automorphism module, or an equivariant homotopy type. Computation with exact integers is part of the proof; independent mathematical assessment is not yet performed. Unindexed equivalent literature cannot be excluded categorically.

## References
1. F. Ardila, F. Castillo, J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870, first public 2014-10-14. In particular the independence-complex shelling theorem.
2. L. Moci and G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760, first public 2020-01-11.
3. SageMath matroid catalog, ternary affine geometry `AG23`, for a standard description of the underlying matroid. The claim and computation are fully specified here without requiring that software.
