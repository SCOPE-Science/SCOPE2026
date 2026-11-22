# The spin deleted-product four-manifold of a simplex two-skeleton

## Finding
Let \(L=\operatorname{sk}_2\Delta^6\) be the full two-dimensional skeleton on seven vertices. Its ordered two-point discrete configuration space, or deleted product,
\[
M=\operatorname{DConf}(L,2)
=\bigcup_{\substack{\varnothing\ne A,B\subseteq\{0,\ldots,6\}\\ A\cap B=\varnothing,\ |A|,|B|\le3}}\Delta^A\times\Delta^B,
\]
is **topologically homeomorphic** to the connected sum of twenty copies of the product of two two-spheres:
\[
\boxed{M\cong_{\mathrm{TOP}}\mathop{\#}_{20}(S^2\times S^2).}
\]
More precisely, its integral intersection lattice is the even unimodular lattice \(H^{\oplus20}\), where \(H=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). The signature vanishes, and the second Stiefel--Whitney class vanishes. No claim of diffeomorphism or PL-homeomorphism is made.

## Assumptions and scope
All spaces are finite polytopal CW complexes, with their standard geometric realizations. The two coordinates are **ordered**; no quotient by coordinate exchange is taken. Each cell is a product of nonempty pairwise vertex-disjoint faces of \(L\). We use two published inputs: (i) the 2025 homology and connectivity theorem for deleted products of simplex skeleta, implying that \(M\) is simply connected and has torsion-free integral homology \(H_2\cong\mathbb Z^{40}\), \(H_4\cong\mathbb Z\), and no other positive homology; (ii) the 2026 manifold theorem, proving that \(M\) is a closed orientable combinatorial four-manifold. Independently, the finite chain computation below confirms \(\dim_{\mathbb F_2}H^2=40\), and the signed top chain exhibits an integral orientation.

## Proof
**1. Finite cell structure.** Index the seven vertices by \(0,\ldots,6\). The cell associated to the disjoint nonempty subsets \(A,B\), each of cardinality at most three, has dimension \(|A|+|B|-2\). Give each factor its increasing-vertex orientation and the product its ordered orientation. Direct enumeration gives the numbers of cells in dimensions zero to four:
\[
(42,210,490,420,140).
\]
For a cell \((A,B)\), the product boundary is
\[
\partial([A]\times[B])=(\partial[A])\times[B]+(-1)^{|A|-1}[A]\times(\partial[B]).
\]
The finite checker enumerates these cells and all boundaries; its checks are exact integer or binary operations, not floating-point approximations.

**2. An integral orientation and vanishing signature.** Every four-cell has \(|A|=|B|=3\), leaving exactly one vertex \(k\) unused. Define \(\epsilon(A,B,k)\in\{\pm1\}\) as the sign of the seven-letter permutation obtained by concatenating the increasing lists \(A,B,(k)\). The explicit integral four-chain
\[
 z=\sum_{|A|=|B|=3,\ A\cap B=\varnothing}\epsilon(A,B,k)[A]\times[B]
\]
has zero boundary: each codimension-one cell is incident with precisely two four-cells, and their signed incidences cancel. The checker confirms every coefficient of \(\partial z\) is zero. Since all 140 top-cell coefficients are units, this represents the fundamental class. Exchanging the two configuration coordinates sends \([A]\times[B]\) to \((-1)^{2\cdot2}[B]\times[A]=[B]\times[A]\), whereas \(\epsilon(B,A,k)=-\epsilon(A,B,k)\). Thus the coordinate-swap homeomorphism reverses the fundamental class. The intersection form is therefore isometric to its negative, and its signature is zero.

**3. The mod-two cup-square computation.** Work over \(\mathbb F_2\). The cellular boundary ranks in degrees one through four are exactly
\[
(41,169,281,139),
\]
so the space of degree-two cocycles has dimension \(490-281=209\), its degree-two coboundaries have dimension \(169\), and \(H^2(M;\mathbb F_2)\) has dimension forty. An explicit deterministic Gaussian elimination, including checks of \(\partial^2=0\), constructs forty cocycles representing a basis modulo coboundaries.

For two degree-two cellular cochains \(u,v\), the product Alexander--Whitney diagonal on a four-cell \([a_0a_1a_2]\times[b_0b_1b_2]\) gives, modulo two, the sum of three terms:
\[
\begin{aligned}
(u\smile v)(A\times B)={}&u(a_0\times B)\,v(A\times b_2)\\
&+u(a_0a_1\times b_0b_1)\,v(a_1a_2\times b_1b_2)\\
&+u(A\times b_0)\,v(a_2\times B).
\end{aligned}
\]
These product faces all belong to the deleted-product subcomplex, so the diagonal restricts naturally to \(M\). Evaluate the three terms over all 140 four-cells of the mod-two reduction of \(z\). The resulting forty-by-forty pairing matrix is symmetric, has full rank forty over \(\mathbb F_2\), **and has forty zero diagonal entries**. The checker also verifies that a degree-two coboundary cups trivially with each selected cocycle on the fundamental class. Since cup squaring is additive in degree two in characteristic two, vanishing on a basis implies \(\langle x\smile x,[M]\rangle=0\) for **every** \(x\in H^2(M;\mathbb F_2)\).

**4. Integral form and topological classification.** For an oriented closed four-manifold, the Wu formula gives \(\langle x^2,[M]\rangle=\langle w_2(M)x,[M]\rangle\) for each mod-two degree-two class. Perfect Poincaré duality therefore implies \(w_2(M)=0\), equivalently the integral intersection pairing is even. The form is unimodular by integral Poincaré duality, has rank forty by the 2025 theorem, and signature zero by step 2. The classification of indefinite even unimodular integral forms identifies it as twenty hyperbolic planes. Finally, Freedman's classification of closed simply connected topological four-manifolds, with vanishing Kirby--Siebenmann invariant for this PL manifold, gives the claimed topological homeomorphism with \(\mathop{\#}_{20}(S^2\times S^2)\).

## Verification
Run `python3 check_intersection.py` using Python 3.10 or later, without external dependencies, and compare with `check_output.txt`. The program enumerates every cell, every cellular boundary, all cup terms in every four-cell, and the complete mod-two cohomology basis. It verifies boundary compositions, integral orientability, the coordinate-swap orientation sign, a nonsingular forty-dimensional cup pairing, and zero self-cup for every basis class. The full computation uses exact finite operations; the general four-manifold classification is a published mathematical theorem, not an experimental inference.

## Relationship to prior work
González and González (2025, first publicly posted in 2023) proved simple connectivity, torsion-freeness and the Betti numbers for deleted products of simplex skeleta, as well as minimal CW models; this does **not** identify the relevant middle-dimensional cup form. González, González and Pérez-Morales (arXiv:2611.12847v1, first public 9 November 2026) established that the present deleted product is a closed combinatorial manifold and explicitly isolated its four-dimensional middle cup form as a remaining case in their discussion, formulating a connected-sum homotopy conjecture. The present claim determines the parity, signature and resulting **topological homeomorphism type** of that particular middle-dimensional manifold. General results for graph two-particle configuration tori or unrelated simplex doubles do not identify this form.

## Limitations
This is one four-dimensional instance, with seven labelled vertices and two ordered particles. It does not settle the higher-dimensional cases of the connected-sum conjecture, distinguish exotic smooth or PL structures, or classify unordered configuration quotients. The computation is finite and independently reproducible, but the present manuscript is not an external independent audit. Publication-priority searches cannot rule out all unindexed literature.

## References
- E. J. González, J. González and M. C. Pérez-Morales, *Discrete Configuration Spaces of Simplex Skeleta: a Middle-Dimensional Manifold Phenomenon*, arXiv:2611.12847v1 (first posted 9 November 2026), https://arxiv.org/html/2611.12847v1. Theorems 1.1 and 1.3, Remarks 1.2 and 1.5, Conjecture 1.6.
- E. J. González and J. González, *An algorithmic discrete gradient field for non-colliding cell-like objects and the topology of pairs of points on skeleta of simplexes*, arXiv:2307.14454; Selecta Mathematica 31 (2025), Article 60, https://link.springer.com/article/10.1007/s00029-025-01043-8. Theorem 1.2.
- M. H. Freedman, *The topology of four-dimensional manifolds*, Journal of Differential Geometry 17 (1982), 357–453.
- Standard references for cellular Alexander–Whitney products, Wu classes, and even unimodular form classification.
