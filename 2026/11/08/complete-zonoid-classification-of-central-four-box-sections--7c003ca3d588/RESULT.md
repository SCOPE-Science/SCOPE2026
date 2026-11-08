# Complete zonoid classification of central four-box sections

## Finding
Let \(Q=\prod_{i=1}^{4}[-s_i,s_i]\subset\mathbb R^4\), where all \(s_i>0\), and let \(u=(u_1,u_2,u_3,u_4)\ne0\). Put \(H=u^\perp\), \(K=Q\cap H\), and \(a_i=s_i|u_i|\). Then the following statements are equivalent:

1. \(K\), regarded as a three-dimensional convex body in \(H\), is a zonoid.
2. \(K\) is a zonotope.
3. Every two-dimensional facet of \(K\) is centrally symmetric.
4. Either at least one \(a_i\) is zero, or \(\max_i a_i\ge\sum_{j\ne i_*}a_j\) for an index \(i_*\) attaining that maximum.

If no coefficient vanishes and condition 4 holds, \(K\) is a three-dimensional parallelotope (an affine cube). If at least one coefficient vanishes, it is a Cartesian product of a centrally symmetric planar polygon and an interval, up to a coordinate permutation and linear equivalence. All boundary equalities are included. In particular, for a four-cube with four nonzero normal coordinates, **the single largest absolute normal coordinate must be at least the sum of the other three**: a pairwise-dominance condition is not enough.

## Assumptions and scope
The section is *central*, namely its hyperplane passes through the center of the box. A zonoid is a Hausdorff limit of Minkowski sums of segments; a zonotope is an actual finite such sum. A parallelotope is an affine image of a three-cube. The statement includes normals with zero coordinates and exact ties; the normal \(u\) need not have unit length. No probability assumption is imposed. Diagonal rescaling and sign changes transform the problem to \(C=[-1,1]^4\) and a nonnegative normal \(a\), preserving both zonoids and zonotopes.

## Proof
**1. Planar noncentral cube-section lemma.** Let \(\alpha_1,\alpha_2,\alpha_3>0\), \(0<|t|<\alpha_1+\alpha_2+\alpha_3\), and let
\[
F=\{x\in[-1,1]^3:\alpha_1x_1+\alpha_2x_2+\alpha_3x_3=t\}.
\]
Then \(F\) is a two-dimensional polygon. If \(F\) is centrally symmetric, **some** coefficient satisfies
\[
\alpha_k\ge |t|+\sum_{j\ne k}\alpha_j.
\]
Conversely, under this inequality, \(F\) is a parallelogram.

To prove necessity, call coordinate \(i\) active if one of \(x_i=1\) or \(x_i=-1\) supports a nondegenerate edge of \(F\). Every edge is supported by one of these six planes. As all three coefficients are nonzero, the edge lines from *different* coordinates have distinct directions within \(\alpha\cdot x=t\): an intersection of \(x_i=\mathrm{constant}\) and \(x_j=\mathrm{constant}\) with the plane is a point. Thus, in a centrally symmetric \(F\), every edge in the coordinate-\(i\) direction must be paired with an edge on the opposite face \(x_i=\mp1\). Its symmetry center \(z\) consequently has \(z_i=0\) for each active \(i\). At least two distinct coordinates are active, because the polygon is bounded. All three cannot be active, since that would force \(z=0\), contradicting \(\alpha\cdot z=t\ne0\). Therefore exactly two coordinates, say \(i,j\), are active. The other pair of coordinate slabs cannot cut the resulting parallelogram into a smaller polygon without supplying an additional edge; hence every \((x_i,x_j)\in[-1,1]^2\) is feasible with \(x_k=(t-\alpha_i x_i-\alpha_j x_j)/\alpha_k\). Applying \(|x_k|\le1\) at all four corners gives \(\alpha_k\ge |t|+\alpha_i+\alpha_j\). The same graph formula proves sufficiency, including equality.

**2. Dominant coefficient.** If all \(a_i>0\) and, after permuting coordinates, \(a_1\ge a_2+a_3+a_4\), then every triple \((x_2,x_3,x_4)\in[-1,1]^3\) uniquely determines
\[
x_1=-\frac{a_2x_2+a_3x_3+a_4x_4}{a_1}\in[-1,1].
\]
Therefore the section is an affine image of \([-1,1]^3\), hence a zonotope and zonoid. This includes the equality case.

**3. A zero coefficient.** If \(a_4=0\), then the section factors as \(F_0\times[-1,1]\), where \(F_0\) is a central plane section of \([-1,1]^3\). Such a planar section is a centrally symmetric polygon and therefore a planar zonotope. Its product with a segment is a three-dimensional zonotope. The argument also covers two or three zero entries.

**4. Failure of dominance with full support.** Suppose every \(a_i>0\) and \(a_1=\max_i a_i<a_2+a_3+a_4\). The intersection of the section with the supporting cube face \(x_1=1\) is a genuine two-dimensional facet: it is affinely identical to
\[
F=\{(x_2,x_3,x_4)\in[-1,1]^3:a_2x_2+a_3x_3+a_4x_4=-a_1\}.
\]
The lemma says that if this facet were centrally symmetric, some coefficient among \(a_2,a_3,a_4\) would be at least \(a_1\) plus the *other two positive coefficients*, impossible because \(a_1\) is the largest. Hence \(K\) has a non-centrally-symmetric facet and cannot be a zonoid, since every exposed face of a zonoid is a translate of a zonoid and in particular centrally symmetric. This closes the necessity proof.

**5. Equivalent characterizations.** Every zonotope is a zonoid and has centrally symmetric two-faces. Conversely, for a three-dimensional polytope, the classical zonotope criterion says all its two-faces are centrally symmetric if and only if it is a zonotope. Alternatively, the preceding cases directly show that a centrally symmetric-facet section must meet condition 4, which explicitly constructs its zonotope representation. Thus all four statements are equivalent.

## Verification
The bundled `verify.py` requires only the Python standard library. It enumerates all \(6^4-1=1295\) nonzero integer normal coefficient vectors with entries in \(\{0,1,2,3,4,5\}\). It exactly constructs rational vertices by intersecting cube edges with the section, enumerates genuine supporting facets, and tests facet central symmetry by exact reflection. Each case agrees with the theorem: 730 meet the condition, 565 do not. Examples with \((2,1,1,1)\), \((3,1,1,1)\), \((1,1,1,0)\), and \((4,4,4,1)\) test both sides and degeneracies. The analytical proof above handles all real normals; the finite checker alone is not an exhaustive real-parameter proof. Run `python3 verify.py` and require `FOUR_CUBE_ZONOID_CLASSIFICATION_RATIONAL_CHECKS_PASSED`.

## Relationship to prior work
Anantharaman's article *Example of cube slices that are not zonoids* supplies explicit four-cube non-zonoid examples, some parallelotope examples, and the facet obstruction, but explicitly leaves a complete characterization open. Its final family also leaves a case of six-sided faces undecided. The present result resolves that gap with one necessary-and-sufficient inequality and treats all degenerate normals. A separate published investigation obtains the two generic face vectors and their frequency for random four-cube sections, distinguishing coordinate-dominance regimes. Face-vector information does not by itself decide zonoid status: a hexagonal prism is a zonotope with eight facets, and a four-cube section with a zero normal coordinate can realize that type. Here the *facets' central symmetry*, not their number, supplies the missing test.

## Limitations
No claim is made for arbitrary affine (noncentral) sections, other ambient dimensions, or arbitrary non-box convex bodies. This classification concerns *zonoid status*, not section volume or combinatorial type. The criterion for three-dimensional polytopes used in the proof is classical; the contribution is its full exact application to four-box central sections. Historical priority may be affected by earlier unindexed formulations of the same facet-symmetry argument; no independent audit has been performed.

## References
1. R. Anantharaman, *Example of cube slices that are not zonoids*, Scientiae Mathematicae Japonicae **81** (2019), 315–326; public J-STAGE release May 10, 2019, DOI: https://doi.org/10.32219/isms.81.3_315. Full accessible version: https://arxiv.org/abs/2305.18351.
2. E. D. Bolker, *A class of convex bodies*, Transactions of the American Mathematical Society **145** (1969), 323–345, DOI: https://doi.org/10.1090/S0002-9947-1969-0256265-X (classical zonotope/zonoid context).
3. G. Ambrus, *Critical central sections of the cube*, arXiv:2107.14778 (2021), https://arxiv.org/abs/2107.14778 (related but distinct metric section questions).
