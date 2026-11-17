# Exact facial-distance spectrum and extremal-face rigidity of orthogonal cubical joins

## Finding
For integers \(2\le p\le q\), consider the orthogonal free sum of two unit cubes
\[
K_{p,q}=\operatorname{conv}\bigl(([-1,1]^p\times\{0\}^q)\cup(\{0\}^p\times[-1,1]^q)\bigr)\subset\mathbb R^{p+q}.
\]
For a nonempty proper face \(F\) define \(K[F]=\operatorname{conv}(\operatorname{vert}K_{p,q}\setminus F)\) and \(d(F)=\operatorname{dist}_2(F,K[F])\). Every face distance depends only on its type and fixed-coordinate counts:

* An exclusive face on the first cube, with exactly \(k\in\{1,\ldots,p\}\) fixed signed coordinates, has \(d(F)=1\) for \(k=1\), and \(d(F)=2/\sqrt{k}\) for \(k\ge2\). The analogous second-cube face with \(l\) fixed coordinates has \(d(F)=1\) for \(l=1\) and \(d(F)=2/\sqrt l\) for \(l\ge2\).
* A mixed face joining a first-cube face with \(k\in\{1,\ldots,p\}\) fixed signed coordinates and a second-cube face with \(l\in\{1,\ldots,q\}\) fixed signed coordinates has
\[
\boxed{d(F)=\frac{2}{\max(k,l)\sqrt{1/k+1/l}}
=2\sqrt{\frac{\min(k,l)}{\max(k,l)(k+l)}}.}
\]

In particular the exact Euclidean facial distance, equivalent to pyramidal width, and the diameter are
\[
\boxed{\Phi_2(K_{p,q})=\frac{2}{\sqrt{q(q+1)}}},\qquad
\boxed{\operatorname{diam}_2(K_{p,q})=2\sqrt q}.
\]
All minimizing faces are characterized: when \(p<q\), exactly the joins of a facet of the first cube and a vertex of the second, numbering \(2p\,2^q\). When \(p=q\), the additional, swapped family also minimizes, giving \(4p\,2^p\) minimizing faces. The normalized condition ratio is
\[
\boxed{\frac{\Phi_2(K_{p,q})}{\operatorname{diam}_2(K_{p,q})}=\frac{1}{q\sqrt{q+1}}}.
\]
For comparison, the \(q\)-dimensional cube has \(\Phi_2([-1,1]^q)=2/\sqrt q\). Thus free-summing even a fixed small second cube reduces the facial distance by the exact multiplicative factor \(1/\sqrt{q+1}\), with its minimizing faces combining a low-codimension face of the smaller block and a vertex of the larger.

## Assumptions and scope
Coordinates are endowed with the ordinary Euclidean norm and the two cubes occupy orthogonal coordinate subspaces with unit semiaxes. Integer parameters obey \(2\le p\le q\). Only nonempty proper exposed faces enter the minimum (every face of a polytope is exposed). The complement is the convex hull of vertices not in the face, not the set-theoretic complement of the face in the body. The result is for these orthogonal free sums, not arbitrary affine images, Cartesian products, or all Hanner polytopes.

## Proof
**1. Exhaustion of face types.** Split a supporting normal as \((u,v)\in\mathbb R^p\times\mathbb R^q\). The support value of the first cube is \(\|u\|_1\), and the second is \(\|v\|_1\). A strictly larger first (respectively second) value exposes an exclusive face of the corresponding cube. Equal positive support values expose the convex hull of two proper cube faces. For a cube, a nonzero support vector fixes each coordinate where its component is nonzero to the corresponding sign. Accordingly every nonempty proper face is either an exclusive cube face or a mixed join of two proper cube faces with respective positive fixed-coordinate counts \(k,l\). Coordinate sign reversals and within-block permutations preserve Euclidean distances, so all fixed signs can be taken positive and the fixed coordinates can be taken first in their block.

**2. Exclusive faces.** Suppose the first \(k\) coordinates of the first cube are fixed to \(+1\). Let \(u\) equal \(1/k\) on those \(k\) coordinates and zero elsewhere. Then \(\langle u,x\rangle=1\) on the exclusive face. Outside it, the largest possible value is \(\max\{1-2/k,0\}\): a first-cube vertex loses at least two in one fixed coordinate, while any second-cube vertex has value zero. For any \(x\) in the face and \(y\) in the complementary vertex hull, Cauchy--Schwarz gives
\[
\|x-y\|_2\ge\frac{1-\max\{1-2/k,0\}}{\|u\|_2}
=\begin{cases}1,&k=1,\\ 2/\sqrt k,&k\ge2.\end{cases}
\]
For \(k=1\), the barycenter of the face and the origin (contained in the other cube) attain the lower bound. For \(k\ge2\), take the barycenter of the face and the average of first-cube vertices formed by reversing exactly one of the \(k\) fixed coordinates; the difference is \(2/k\) in each of those \(k\) coordinates and zero elsewhere, attaining \(2/\sqrt k\). Interchange blocks for the second-cube formula.

**3. Mixed faces.** Let \(k,l\ge1\) be the numbers of prescribed positive coordinates. Set \(u\) equal to \(1/k\) in the prescribed first-block coordinates, \(1/l\) in the prescribed second-block coordinates, and zero elsewhere. Every vertex of the mixed face has \(\langle u,x\rangle=1\). Among vertices outside the face, the maximum is exactly \(\max\{1-2/k,1-2/l\}=1-2/\max(k,l)\), because one specified sign must be reversed in at least one block. Therefore
\[
 d(F)\ge \frac{2}{\max(k,l)\sqrt{1/k+1/l}}.
\]
To attain equality, suppose \(k\le l\), let \(a\) be the barycenter of the specified first-cube face and \(b\) the barycenter of the specified second-cube face, and set
\[
 x=\frac{2}{k+l}a+\left(1-\frac{2}{k+l}\right)b\in F.
\]
Since \(k+l\ge2\), this is a convex combination. In the second block, take \(y\) to be the average of all second-cube corners with exactly one of the \(l\) specified signs reversed, averaging the remaining free signs symmetrically. Thus \(y\in K[F]\); its specified second-block coordinates equal \(1-2/l\), and all other coordinates vanish. The difference \(x-y\) has first-block entries \(2/(k+l)\), and second-block entries \(2k/[l(k+l)]\); it is exactly \(2k/(k+l)\) times the selected normal \(u\). Hence the lower bound is attained. When \(k\ge l\), interchange the roles of the two blocks. This proves the complete face-distance spectrum.

**4. Global minimizers.** For \(k\le l\), the squared distance is \(4k/[l(k+l)]\), strictly increasing in \(k\) for fixed \(l\) and strictly decreasing in \(l\) for fixed \(k\). Its unique minimum within that sector occurs at \((k,l)=(1,q)\), giving \(2/\sqrt{q(q+1)}\). The opposite sector has its unique minimum at \((k,l)=(p,1)\), of value \(2/\sqrt{p(p+1)}\), which is equal only for \(p=q\). Every exclusive face has distance at least \(\min\{1,2/\sqrt q\}\), strictly larger than \(2/\sqrt{q(q+1)}\) when \(q\ge2\). Thus the claimed global minimum and complete equality classification follow. There are \(2p\) first-cube facets, \(2^q\) second-cube vertices, and, if \(p=q\), another \(2q\,2^p\) minimizing faces in the swapped family.

**5. Diameter and comparison.** Within the first and second cubes the diameters are \(2\sqrt p\) and \(2\sqrt q\); between their corners the greatest separation is \(\sqrt{p+q}\). Since \(p\le q\), the maximum is \(2\sqrt q\). The normalized expression follows. The standard cube facial distance \(2/\sqrt q\) is the established cube result, also recovered from the exclusive-face computation in the cube alone.

## Verification
A standalone checker, `verify_facial_distance.py`, constructs full sets of cube corners, forms representative faces and complementary vertex hulls independently from fixed-coordinate incidence, and solves the distance minimization between two convex hulls as an equality-constrained quadratic program. It checks all exclusive and mixed face types for \((p,q)=(1,2),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\): **96** optimizations, plus analytical-formula global minima and equality-family type comparisons. The \(p=1\) case is diagnostic only, outside the claimed theorem. The finite optimizations corroborate the infinite-parameter algebraic proof; they do not replace it. Run `python verify_facial_distance.py` with NumPy and SciPy.

## Relationship to prior work
Peña and Wirth's *Calculus of the Facial Distance* (first public 2026-08-29, arXiv:2608.28971) formalizes facial distance and computes it for cubes and cross-polytopes; its Section 3 proves a **Cartesian-product** rule. The full text also develops facet-normal and linear-image bounds, but provides no all-rank distance spectrum for orthogonal **free sums of two cubes**. Deza, Martínez-Rubio, Peña, and Wirth's *Facial distance and diameter* (first public 2026-09-26, arXiv:2609.32440) proves a universal sharp dimension-only upper bound and computes the Birkhoff-polytope invariant; neither result specializes to the exact free-sum spectrum. Iommazzo and collaborators (arXiv:2505.11259) discuss products, a different operation. The cross-polytope special case \(p=q=2\) has previously been treated through the general cross-polytope formula: its single numerical instance is not presented as novel. The complete unbounded two-cube family, equality-face classification, and sharp asymptotic loss are the specific present contribution. The result is conditional on the literature and recorded-result coverage described below; absence of a retrieved equivalent does not prove absolute historical novelty.

## Limitations
Only orthogonal unit-coordinate cubes with \(p,q\ge2\) are classified. Arbitrary nonsymmetric weights, nonorthogonal embeddings, and more than two free-summed blocks are not covered. No algorithmic iteration-bound improvement beyond evaluating an existing geometric condition measure is proved. Research-record and literature searches cannot rule out results stated in unindexed documents or under an unknown equivalent formulation. Independent scientific validation has not been performed.

## References
1. J. Peña and E. Wirth, *Calculus of the Facial Distance*, arXiv:2608.28971, first publicly available 2026-08-29. https://arxiv.org/abs/2608.28971 ; available full text: https://optimization-online.org/wp-content/uploads/2026/08/calculusoptonline.pdf .
2. A. Deza, D. Martínez-Rubio, J. Peña and E. Wirth, *Facial distance and diameter*, arXiv:2609.32440, first publicly available 2026-09-26. https://arxiv.org/abs/2609.32440 .
3. R. Iommazzo et al., *Linear Convergence of the Frank--Wolfe Algorithm over Product Polytopes*, arXiv:2505.11259, 2025. https://arxiv.org/abs/2505.11259 .
