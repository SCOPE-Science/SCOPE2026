# Exact Gram completion for star-shaped polygonal cycles

## Finding
Let \(n\ge3\), and let \(v_0,\ldots,v_{n-1}\in\mathbb R^2\setminus\{0\}\) be the cyclically ordered, distinct vertices of a simple polygon whose **strict kernel contains the origin**: every oriented boundary edge leaves the origin strictly on its left, with counterclockwise indexing. Give each cycle vertex the scalar \(s_i=\langle v_i,v_i\rangle\) and each cycle edge the scalar \(t_i=\langle v_i,v_{i+1}\rangle\), with indices modulo \(n\). Set
\[
\alpha_i=\arccos\!\left(\frac{t_i}{\sqrt{s_i s_{i+1}}}\right)\in(0,\pi).
\]
Then \(\sum_i\alpha_i=2\pi\) and **every previously unrecorded pairwise inner product is determined explicitly**:
\[
\boxed{\langle v_i,v_j\rangle=\sqrt{s_i s_j}\,\cos\!\left(\sum_{k=i}^{j-1}\alpha_k\right)}\qquad(0\le i<j<n).
\]
Consequently, any two such polygonal cycles with the same labeled local data are related by a single orthogonal transformation. More generally, every dihedral automorphism of the cycle preserving the vertex and edge scalars extends to a unique orthogonal symmetry of the polygon; thus the metric coloring captures its full orthogonal symmetry group. The theorem applies to nonconvex polygons, not merely to convex polytopes.

## Assumptions and scope
A simple polygon is a non-self-intersecting closed polygonal curve with distinct noncollinear consecutive vertices; its kernel is the intersection of the inward closed halfplanes supported by its oriented boundary edges. The **strict kernel** is the intersection of the corresponding open halfplanes. Reversing the initial orientation if necessary, the polygon is assumed counterclockwise and \(0\) belongs to its strict kernel. Such a polygon is star-shaped with \(0\) as a visibility center. Equivalently for the present argument, the rays to successive vertices wind once around \(0\), with strictly positive angular increments smaller than \(\pi\). There is no lower bound on consecutive edge lengths or requirement of convexity. All inner products and norms are Euclidean and the origin is fixed. Comparisons concern two realizations satisfying the same stated geometric condition, not arbitrary unconstrained graph frameworks or realizations in higher dimensions.

## Proof
For a counterclockwise simple polygon with origin in its strict kernel, every oriented edge obeys \(\det(v_i,v_{i+1})>0\), since the origin lies strictly to its left. Each ray is nonzero. Hence the counterclockwise angular increment from \(v_i\) to \(v_{i+1}\) is uniquely in \((0,\pi)\). Because the polygon surrounds the origin and its boundary has winding number one, the sum of these increments is exactly \(2\pi\).

The local vertex and edge scalars give \(\|v_i\|=\sqrt{s_i}\) and \(\cos\alpha_i=t_i/\sqrt{s_i s_{i+1}}\). The strict determinant inequality selects the positive branch \(\alpha_i\in(0,\pi)\) uniquely; no choice of supplementary angle or orientation remains. Choosing the first vertex ray as polar angle zero, every later ray therefore has angle \(\sum_{k=0}^{j-1}\alpha_k\). Subtracting the angular positions of rays \(i\) and \(j\) gives the boxed formula. This reconstructs the *whole Gram matrix*, not only edge lengths.

If two realizations have identical local labeled data, their Gram matrices coincide by the formula. Since their position matrices have rank two (the origin is strictly interior), an orthogonal map of \(\mathbb R^2\) sends each vertex of the first to its corresponding vertex of the second. Any automorphism of a cycle is a rotation or reversal of its cyclic indexing. Relabeling by an automorphism preserving the local colors retains the strict-kernel property after choosing the correct orientation; hence the same Gram completion proves that the relabeling is realized by an orthogonal map. Conversely every orthogonal polygon symmetry preserves vertex norms and adjacent inner products, so the two groups agree. Uniqueness of the orthogonal map follows from the spanning property.

The class genuinely includes nonconvex polygons: for \(n=6\), take alternating radii \(2,1/2,2,1/2,2,1/2\) at successive angles \(0,\pi/3,\ldots,5\pi/3\). Every edge has positive determinant \(\sqrt3/2\) with its predecessor ray, while consecutive signed turns have alternating signs, so the hexagon is simple, strictly star-shaped about the origin, and nonconvex.

## Verification
Run `python verify_polygon.py` with Python 3 and NumPy. The standalone checker tests 792 polygonal configurations: 414 affine images of convex regular polygons and 378 nonconvex-capable radial cycles. It reconstructs every Gram-matrix entry from only the vertex norms and consecutive inner products, checks positive angular branches and one full winding, and compares all 22,932 dihedral candidate symmetries against the reconstructed full Gram matrix. The observed success message is `RADIAL_CYCLE_GRAM_COMPLETION_PASS`. These finite tests are diagnostics, not proof for all \(n\); the argument above supplies the infinite proof.

## Relationship to prior work
Martin Winter's *Capturing Polytopal Symmetries by Coloring the Edge-Graph* (first publicly posted August 30, 2021; journal 2023) defines exactly these vertex- and edge-inner-product colors and asks whether they capture orthogonal symmetries for general polytopes (Question 6.6). The present theorem gives an explicit reconstruction formula on radially ordered planar cycles including **nonconvex** star-shaped polygons.

The stronger 2023 paper by Winter, *Rigidity, Tensegrity, and Reconstruction of Polytopes Under Metric Constraints*, proves global metric reconstruction for **combinatorially equivalent convex polytopes** (Theorem 4.7 and Corollary 4.10); in particular its theorem already subsumes the convex-polygon corollary here. **That convex result is not claimed as new.** The contribution here is extending an exact, explicit local-to-global Gram reconstruction to nonconvex star-shaped polygonal cycles, which do not satisfy that polytope hypothesis. Classical generic global rigidity of wheel graphs does not by itself imply rigidity at all nongeneric radially ordered realizations; the theorem makes no claim about all arbitrary wheel realizations. The positive angular branch and winding are the geometric ingredients of this extension.

## Limitations
The result needs a common marked origin strictly in the kernel of both realizations, positive planar winding once, and the given cyclic boundary correspondence. It does not assert global rigidity against arbitrary graphs or non-star-shaped competitor embeddings, and it does not settle the general higher-dimensional metric-coloring question. It also does not claim newness for convex polygons, covered by Winter's 2023 convex-polytope theorem. A previously unindexed star-shaped wheel global-rigidity statement is a residual historical-priority risk.

## References
1. M. Winter, *Capturing Polytopal Symmetries by Coloring the Edge-Graph*, arXiv:2108.13483, first posted 2021-08-30; Discrete Comput. Geom. 71 (2024), 1003–1020, https://doi.org/10.1007/s00454-023-00560-7, especially Definition 1.2 and Questions 6.4 and 6.6.
2. M. Winter, *Rigidity, Tensegrity, and Reconstruction of Polytopes Under Metric Constraints*, arXiv:2302.14194, first posted 2023-02-27; IMRN 2024, 7721–7747, https://doi.org/10.1093/imrn/rnad298, especially Theorem 4.7 and Corollary 4.10.
