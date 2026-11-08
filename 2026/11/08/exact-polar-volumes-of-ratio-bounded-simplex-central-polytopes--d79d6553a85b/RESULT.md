# Exact polar volumes of ratio-bounded simplex central polytopes

## Finding

For every integer \(m\ge 2\) and every real \(c>1\), put
\[
H_m=\{x\in\mathbb R^m:\sum_{i=1}^m x_i=1\},\qquad b_m=\frac1m\mathbf1_m,
\]
and define the ratio-bounded central polytope and its centered version by
\[
P_{m,c}=\{x\in H_m:x_i\le c x_j\text{ for all }i\ne j\},
\qquad C_{m,c}=P_{m,c}-b_m\subset H_m^0,
\]
where \(H_m^0=\{z:\sum_i z_i=0\}\) has the Euclidean metric induced from \(\mathbb R^m\). Let \(C_{m,c}^{\circ}\) denote the polar in \(H_m^0\), with threshold \(1\) in the scalar product. Then the complete all-dimensional polar-volume formula is
\[
\boxed{\displaystyle
\operatorname{vol}_{m-1}(C_{m,c}^{\circ})=
\frac{m^{m-2}\sqrt m}{(m-1)(c-1)^{m-1}}
\sum_{k=1}^{m-1}\binom mk
\frac{\bigl(m+(c-1)k\bigr)c^{m-k-1}}{(k-1)!(m-k-1)!}.}
\tag{1}
\]
All volumes are intrinsic Euclidean volumes, not coordinate-projection volumes.

For comparison, the primal volume has the exact expression
\[
\operatorname{vol}_{m-1}(P_{m,c})=
\frac{\sqrt m}{(m-1)!}\frac{m}{c-1}
B\!\left(\frac{m}{c-1},m\right),
\tag{2}
\]
where \(B\) is Euler's beta function. Consequently, multiplying (1) by (2) gives the exact centered polar-volume product for every \(m\) and \(c\). Because the permutation symmetry fixes only \(b_m\) in \(H_m\), that center is also the unique Santaló point; thus the product is the affine-invariant Santaló volume product.

For an arbitrary nondegenerate \((m-1)\)-simplex \(\Delta\), the ratio-bounded central polytope is the affine image of \(P_{m,c}\). Its centroid-polar Euclidean volume is the right side of (1) multiplied by \(\operatorname{vol}_{m-1}(\operatorname{conv}\{e_1,\ldots,e_m\})/\operatorname{vol}_{m-1}(\Delta)\). In particular, the centered volume product is exactly the same for every affine simplex, not merely for regular ones.

The edge-trisection polytope of Kazakov corresponds to \(c=2\) and \(m=n+1\), where \(n\) is the simplex dimension. For example, at \(c=2\), the polar volume is \(117\sqrt3/2\) for \(m=3\) and \(1344\) for \(m=4\). The corresponding volume products are \(351/40\) and \(64/5\). Formula (1) evaluates the polar-volume direction explicitly proposed for investigation in that paper, and extends it to arbitrary real ratios \(c>1\).

## Assumptions and scope

The original simplex is \(\operatorname{conv}\{e_1,\ldots,e_m\}\) in \(H_m\). Its volume is \(\sqrt m/(m-1)!\). The inequalities imply all coordinates of a feasible point are positive, since a zero coordinate would force every coordinate to vanish. Since \(c>1\), the barycenter is strictly feasible, so the centered polar is a bounded full-dimensional polytope. No rationality or integrality of \(c\) is assumed. A zero-dimensional simplex factor has volume \(1\) in the usual product formula below.

## Proof

**1. All vertices of the primal.** Fix a nonempty proper subset \(S\subset[m]\), put \(k=|S|\), \(\ell=m-k\), and \(D=m+(c-1)k\). The point
\[
(x_S)_i=\begin{cases}c/D,&i\in S,\\1/D,&i\notin S\end{cases}
\tag{3}
\]
is feasible. Precisely the \(k\ell\) inequalities with \(i\in S\), \(j\notin S\) are equalities. Their equalities force a common high coordinate and a common low coordinate, in ratio \(c\); the sum-one equation fixes both, so \(x_S\) is a vertex.

Conversely, at any vertex the maximum and minimum coordinate must be in ratio \(c\), since otherwise every inequality is strict. Write \(a\) for the minimum, \(ca\) for the maximum, and let \(I\) comprise any coordinates strictly between them. Every active inequality joins a maximum coordinate to a minimum coordinate. If \(I\) is nonempty, varying one intermediate coordinate while adjusting the common extreme scale to preserve the sum creates a nonconstant feasible interval, since all inequalities involving an intermediate coordinate have slack. Such a point cannot be a vertex. Thus (3), for the \(2^m-2\) nontrivial subsets, lists all vertices.

**2. Polar facets.** Define the zero-sum vectors
\[
a_{ij}=\frac{m}{c-1}\left(e_i-ce_j+\frac{c-1}{m}\mathbf1_m\right),\qquad i\ne j.
\tag{4}
\]
The inequality \(x_i\le c x_j\) is exactly \(\langle a_{ij},x-b_m\rangle\le1\). Polarity therefore gives \(C_{m,c}^{\circ}=\operatorname{conv}\{a_{ij}:i\ne j\}\). Each inequality is a genuine primal facet: take \(x_i=ca\), \(x_j=a\), and every other coordinate strictly between \(a\) and \(ca\), normalized to sum to one; only its named inequality is active.

The polar facet corresponding to \(x_S\) is
\[
F_S=\operatorname{conv}\{a_{ij}:i\in S,\ j\notin S\}.
\tag{5}
\]
Writing the points in (4) as a constant translation plus \(\frac{m}{c-1}e_i-\frac{mc}{c-1}e_j\), we see that \(F_S\) is the orthogonal Cartesian product of an appropriately scaled \((k-1)\)-simplex and an appropriately scaled \((\ell-1)\)-simplex in the complementary coordinate subspaces. It has dimension \(m-2\) and volume
\[
\operatorname{vol}_{m-2}(F_S)
=\left(\frac{m}{c-1}\right)^{m-2}
\frac{\sqrt{k\ell}\,c^{\ell-1}}{(k-1)!(\ell-1)!}.
\tag{6}
\]
For clarity, the regular simplex \(\operatorname{conv}\{e_i:i\in S\}\) has intrinsic volume \(\sqrt k/(k-1)!\), and similarly for the complementary coordinate block. These factors are orthogonal, which proves (6) also when \(k=1\) or \(\ell=1\).

**3. Pyramid heights and summation.** The squared norm of the centered primal vertex is
\[
\|x_S-b_m\|^2
=\frac{(c-1)^2k\ell}{mD^2}.
\tag{7}
\]
Since the supporting hyperplane of \(F_S\) is \(\langle y,x_S-b_m\rangle=1\), its Euclidean distance from the origin equals
\[
h_S=\frac{D\sqrt m}{(c-1)\sqrt{k\ell}}.
\tag{8}
\]
Every facet is one of the \(F_S\) because all primal vertices were determined in step 1. The pyramids \(\operatorname{conv}(0,F_S)\) have pairwise disjoint interiors and exhaust the polar. Summing their volumes \(h_S\operatorname{vol}_{m-2}(F_S)/(m-1)\), with \(\binom mk\) subsets at size \(k\), and substituting (6) and (8), gives exactly (1).

**4. Primal volume and the Santaló center.** Let \(Y_1,\ldots,Y_m\) be independent mean-one exponential variables. The normalized vector \(Y/\sum_iY_i\) is uniform on the simplex. The event that its largest coordinate is at most \(c\) times the smallest has probability
\[
 m\int_0^\infty e^{-my}\left(1-e^{-(c-1)y}\right)^{m-1}\,dy
=\frac{m}{c-1}B\!\left(\frac{m}{c-1},m\right).
\]
Multiplying by the simplex volume proves (2). Under an invertible affine transformation with linear part \(T\) on the affine span, primal volume scales by \(|\det T|\) and polar volume by \(|\det T|^{-1}\). This proves the asserted affine-simplex polar-volume scaling. The Santaló point is unique for every full-dimensional convex body and commutes with affine symmetries. Every coordinate permutation preserves \(P_{m,c}\), and the only point fixed by all these permutations in \(H_m\) is \(b_m\). This gives the stated Santaló interpretation.

## Verification

The accompanying standalone `verify_polar_volume.py` executes exact rational checks of the vertex-to-polar support pairing in dimensions \(m=2,\ldots,8\), for several rational ratio parameters, including every predicted active inequality. It also checks the exact low-dimensional specializations of (1), and the beta-product specialization at \(c=2\). In total **177,492 exact-rational assertions** pass. Separately, the verifier constructs the complete list of polar vertices from (4), projects them to an orthonormal basis of \(H_m^0\), and independently computes convex-hull volumes with SciPy/Qhull for \(m=2,\ldots,7\) and \(c\in\{3/2,2,3\}\): **all 18 numerical volume comparisons** pass at relative tolerance \(10^{-8}\). The latter are finite corroboration, not a substitute for the universal proof.

Run `python verify_polar_volume.py` with Python 3.10+, NumPy, and SciPy. The exact checks use only the Python standard library. For reproducible BLAS behavior, `OPENBLAS_NUM_THREADS=1 python verify_polar_volume.py` is sufficient.

## Relationship to prior work

Kazakov's 2026 paper derives the primal volume fraction \(1/\binom{2m-1}{m-1}\) for \(c=2\), and gives the vertices and facets of this central polytope; its conclusion explicitly identifies the dual polytope and its volume as a direction for future investigation. The novelty asserted here is the evaluated polar volume (1) for all dimensions and ratios, together with the resulting Santaló product—not the previously known primal volume or basic vertex list.

Rietsch and Williams study root polytopes generated by unweighted vectors \(e_i-e_j\) and \(\pm e_i\), with connections to quivers and toric geometry. The configuration (4) has the unequal coordinate weights \(1,-c\) and a zero-sum centering; their stated root-polytope family does not supply (1). General polar-volume methods, such as Filliman's, are broader computational tools but no explicit instance of the present all-parameter evaluation was found in the material available for comparison.

## Limitations

The polar is taken at the barycenter in the induced metric on the sum-zero hyperplane. Its individual Euclidean volume is not invariant under arbitrary affine changes of the original simplex; the volume product is affine invariant. The proof does not classify Ehrhart coefficients, combinatorial automorphism groups, or arbitrary nonuniform pairwise ratio bounds. Independent historical-priority review has not been performed, and inaccessible older polar-volume literature could contain an equivalent specialization.

## References

- Yu. V. Kazakov, *Generalization of Marion's Theorem: Volumes of Central Polytopes Obtained by Trisecting the Edges of Simplices*, arXiv:2606.02087v1, first posted 2026-06-01. https://arxiv.org/abs/2606.02087
- K. Rietsch and L. Williams, *Root, flow and order polytopes with connections to toric geometry*, Forum of Mathematics, Sigma **13** (2025), e194, DOI:10.1017/fms.2025.10056. https://doi.org/10.1017/fms.2025.10056
- P. Filliman, *The volume of duals and sections of polytopes*, Mathematika **39** (1992), 67–80, DOI:10.1112/S0025579300006860. https://doi.org/10.1112/S0025579300006860
- K. Mészáros, *Root polytopes, triangulations, and the subdivision algebra, I*, arXiv:0904.2194, 2009. https://arxiv.org/abs/0904.2194
