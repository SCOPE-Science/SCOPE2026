# Octahedral self-volume violates the odd-dimensional hexagon-product minimum

## Finding

Let \(\omega_n(B)\) denote the recursively defined self-volume of a centrally symmetric convex body in an \(n\)-dimensional Euclidean space, with \(\omega_1([-a,a])=2\). For the three-dimensional cross-polytope
\[
O=\{x\in\mathbb R^3: |x_1|+|x_2|+|x_3|\le1\},
\]
its exact self-perimeter and self-volume are
\[
P_{\mathrm{self}}(O)=16,\qquad\omega_3(O)=\frac{16}{3}<6.
\]
For every integer \(k\ge1\), let \(H\) be any centrally symmetric affinely regular hexagon containing the origin in its interior, and put \(B_k=O\times H^{k-1}\). Then
\[
\omega_{2k+1}(B_k)=\frac{16}{3}\,3^{k-1}=\frac{8}{9}\left(2\cdot3^k\right)<2\cdot3^k.
\]
Consequently the odd-dimensional minimum assertion in Conjecture 2 of Wolansky (2026), which proposes \(2\cdot3^k\) for centrally symmetric bodies of dimension \(2k+1\), is false in every odd dimension at least three. This does not determine the true minima.

## Assumptions and scope

All bodies are full-dimensional, compact, convex, centrally symmetric about the origin, and have the usual Euclidean Hausdorff measures. For \(n\ge2\), with \(\nu_F\) the outer Euclidean unit normal to a facet \(F\) of an \(n\)-polytope \(B\), set
\[
\omega_n(B)=\frac1n\sum_{F\text{ facet}}\operatorname{vol}_{n-1}(F)\,
\frac{\omega_{n-1}(B\cap\nu_F^\perp)}{\operatorname{vol}_{n-1}(B\cap\nu_F^\perp)}.
\]
The one-dimensional value is \(\omega_1(I)=2\) for a centrally symmetric segment. This is the polyhedral specialization of the recursive boundary integral in Wolansky's Definition 4.1; here \(\omega_n\) is *not* ordinary Euclidean volume. For planar polygons, \(\omega_2(B)\) equals one half the perimeter in the norm with unit ball \(B\).

## Proof

**Central sections.** The octahedron \(O\) has eight congruent triangular facets, each with area \(\sqrt3/2\) and outward normal \((\epsilon_1,\epsilon_2,\epsilon_3)/\sqrt3\), with each \(\epsilon_i\in\{-1,1\}\). Changing coordinate signs is an isometry of \(O\), so each central normal section is congruent to
\[
H_0=O\cap\{x_1+x_2+x_3=0\}.
\]
Its six vertices are the coordinate permutations of \((1/2,-1/2,0)\). They form a regular hexagon of circumradius \(1/\sqrt2\) and side length \(1/\sqrt2\); the Euclidean area therefore is \(3\sqrt3/4\).

**Planar self-volume.** For a centered regular hexagon, the vector of every oriented edge is another vertex vector. Each edge therefore has norm one in the Minkowski norm having the hexagon as its unit ball. The self-perimeter is the sum of six unit edge lengths, \(6\), and hence \(\omega_2(H_0)=3\). The same holds for every affinely regular centered hexagon by the elementary norm-edge argument (or linear invariance).

**Three-dimensional integral.** Inserting the eight congruent facet contributions gives
\[
\begin{aligned}
P_{\mathrm{self}}(O)&=8\left(\frac{\sqrt3}{2}\right)
\frac{3}{3\sqrt3/4}=16,\\
\omega_3(O)&=\frac13P_{\mathrm{self}}(O)=\frac{16}{3}.
\end{aligned}
\]
The comparison \(16/3<6\) is strict.

**All odd dimensions.** The recursive self-volume is multiplicative for Cartesian products of centered convex bodies:
\[
\omega_{a+b}(A\times B)=\omega_a(A)\omega_b(B).
\]
For completeness, on the boundary part \(\partial A\times B\), the central normal section is \((A\cap\nu^\perp)\times B\). Inducting on \(a+b\), both the recursive self-volume and the Euclidean section volume factor. After integrating over the \(B\) factor, this boundary part contributes \(a\omega_a(A)\omega_b(B)\) to the self-perimeter; the other boundary part contributes \(b\omega_a(A)\omega_b(B)\). Division by \(a+b\) proves multiplicativity; the case of two intervals provides the base. As \(\omega_2(H)=3\), induction yields \(\omega_{2k+1}(B_k)=\omega_3(O)\omega_2(H)^{k-1}\), as asserted. This product identity also appears as Theorem 4.2 of the motivating paper.

## Verification

Run `python3 verify.py` in an environment with Python 3 and SymPy. The verifier independently enumerates octahedral facet normals and face areas, constructs the six vertices of the corresponding central sections, computes their Euclidean areas from the cross-product formula and their self-perimeter from the exact hexagon edge structure, checks the recursive sum, and checks exact rational product comparisons for \(1\le k\le100\). The universal higher-dimensional assertion follows from the preceding induction, not these finite checks.

## Relationship to prior work

Wolansky (2026), Definition 4.1 supplies the recursive invariant, Section 3 the planar self-perimeter, Theorem 4.2 Cartesian-product multiplicativity, and Conjecture 2 proposes \(2\cdot3^k\) as the odd-dimensional centrally symmetric minimum. Those definitions and the product identity are prior work. The assessed contribution is the octahedral evaluation \(\omega_3(O)=16/3\), the strict contradiction at \(k=1\), and its propagation to all odd dimensions through a uniform deficit factor \(8/9\). None of the inspected examples in that paper computes the octahedral self-volume. Relevant mathematical-record searches did not expose an earlier equivalent calculation; absence from an index does not establish priority.

## Limitations

The new fact is a constructive upper bound on any future sharp minimum, not the solution of the minimization problem. It gives no lower bound for all bodies and no claim about the even-dimensional part of Conjecture 2, and it does not establish uniqueness or classify optimizers. An unindexed exact octahedral self-volume computation remains a priority risk. Self-volume is an affine-geometric recursive functional, not Euclidean content or another convention for Minkowski volume.

## References

1. G. Wolansky, *Self perimeter of convex sets*, arXiv:2604.01950 (first posted 2026-04-02), Definition 4.1, Theorem 4.2, Conjecture 2; https://arxiv.org/abs/2604.01950 ; full-text version https://arxiv.org/html/2604.01950v4.
2. S. Gołąb, classical bounds on the self-perimeter of a centrally symmetric planar unit ball, cited in Wolansky's introduction. The present argument directly computes the regular-hexagon case and does not rely on the general extremal theorem.
