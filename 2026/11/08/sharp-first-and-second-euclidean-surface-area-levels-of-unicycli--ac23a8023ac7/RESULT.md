# Sharp first and second Euclidean surface-area levels of unicyclic graphical zonotopes

## Finding

The new assertion concerns the **second distinct** surface-area level. Let \(G\) be a connected simple unicyclic graph on \(n\ge5\) vertices, and define
\[
Z_G=\sum_{\{u,v\}\in E(G)}\left[-\frac{e_u-e_v}{2},\frac{e_u-e_v}{2}\right],\qquad
A(G)=\mathcal H^{n-2}(\partial Z_G).
\]
The boundary is intrinsic to the coordinate-sum-zero hyperplane with its inherited Euclidean metric. Exclude the minimizing graph, a triangle with all \(n-3\) extra vertices attached as leaves to one triangle vertex. Among the remaining graphs, the minimum is uniquely attained, up to isomorphism, by the triangle with \(n-4\) leaves on one triangle vertex and one leaf on a second vertex. Its area is
\[
A_2(n)=(6n-16)\sqrt{n-1}+2\sqrt{2(n-2)}+2\sqrt{3(n-3)}.
\]
The gap above the minimum \(A_1(n)=(6n-14)\sqrt{n-1}+2\sqrt{2(n-2)}\) is
\[
A_2(n)-A_1(n)=2\bigl(\sqrt{3(n-3)}-\sqrt{n-1}\bigr)>0.
\]
The first-level benchmark and the general area identity used below are not claimed as new.

## Assumptions and scope

Graphs are finite, connected, simple and have exactly one cycle. The edge generators are the coordinate vectors \(e_u-e_v\) of Euclidean length \(\sqrt2\); no quotient norm, affine distortion or edge weight is used. Area sums each geometric facet once, and graph isomorphism acts by orthogonal coordinate permutation. The second-level theorem is for \(n\ge5\). At \(n=4\) there are just two graphs; the same area identity gives \(10\sqrt3+4\) for a triangle with one leaf and \(8\sqrt3+8\) for the four-cycle, in that order.

## Proof

**Area identity and first-level benchmark.** Write \(F_j=\sqrt{j(n-j)}\). If the cycle has length \(\ell\), the identity in [1, Eq. (4)] in unordered cut notation is
\[
A(G)=2\ell\sum_{e\text{ a bridge}}F_{s_e}
  +2\sum_{\{e,f\}\subset E(C)}F_{s_{ef}},
\]
where \(s_e\) is the order of the component separated from the cycle by deleting the bridge \(e\), and \(s_{ef}\) is either component order after deleting two cycle edges. In [1], the second sum is written over ordered cyclic intervals: their complement symmetry counts each unordered pair twice.

For the geometric normalization, a facet of a connected graphical zonotope occurs when the zero-slope generators for a supporting normal span a codimension-one subspace. The zero-slope edges then form two induced connected shores. For each such bipartition there are two opposite facets, each an orthogonal product of the shores' graphical zonotopes up to translation. A connected shore of order \(k\) has intrinsic zonotope volume \(\sqrt{k}\,\tau\), with \(\tau\) its spanning-tree count: the generator-volume sum runs over its incidence bases, and each tree basis has squared Gram determinant \(k\). This includes the singleton convention. Consequently a shore pair contributes \(2F_j\) times the product of its spanning-tree counts. In a unicyclic graph the minimal cuts are the single bridges and the pairs of distinct cycle edges. In the former case the shore retaining the cycle has \(\ell\) spanning trees and the other has one; in the latter both shores are trees. This gives the factor \(2\ell\) and the factor \(2\) above.

Reference [1, Eq. (1)] proves that for each fixed cycle length \(\ell<n\) the unique minimizer puts all extra vertices as leaves at a single cycle vertex, and gives its area. At \(\ell=3\) this yields \(A_1(n)=6(n-3)F_1+2(F_2+2F_1)\). We compare every longer cycle to the proposed second triangle below, which also confirms the first benchmark as the global minimum.

**Longer cycles are above the proposed second level.** Each split has \(F_j\ge F_1\), so for \(4\le\ell\le n\), including the bare cycle, the area identity gives
\[
A(G)\ge\bigl(2\ell(n-\ell)+\ell(\ell-1)\bigr)F_1
\ge 4(2n-5)F_1.
\]
The quadratic \(\ell(2n-\ell-1)\) is concave, and the value at \(\ell=n\) minus its value at \(4\) is \((n-4)(n-5)\ge0\). The difference between this lower bound and \(A_2(n)\) is \((2n-4)F_1-2(F_2+F_3)>0\): use \(F_1\ge2\), \(F_2,F_3\le n/2\), and \(4n-8>2n\) for \(n\ge5\).

**Non-leaf attachments on a triangle are also above the proposed second level.** Let the three rooted trees (each including its cycle vertex) have orders \(w_1,w_2,w_3\ge1\) with sum \(n\). Removing two cycle edges isolates one such tree, so the cycle-area term is \(2\sum_i F_{w_i}\). The strictly concave function \(t\mapsto\sqrt{t(n-t)}\) gives \(\sum_i F_{w_i}\ge F_2+2F_1\) by majorization by \((n-2,1,1)\). There are \(n-3\) bridges. If any noncycle vertex is not a leaf, some bridge separates a component of size between \(2\) and \(n-3\), with \(F_{s_e}\ge F_2\). Hence the area is at least \(A_1(n)+6(F_2-F_1)\), strictly above \(A_1(n)+2(F_3-F_1)=A_2(n)\), since \(F_2>F_1\) and strict concavity gives \(F_3-F_1<2(F_2-F_1)\).

**Second level among all-leaf triangles.** Their bridge term is the constant \(6(n-3)F_1\). After excluding \((n-2,1,1)\), the largest entry of any permissible sorted integer triple \((w_1,w_2,w_3)\) is at most \(n-3\) and the two largest sum to at most \(n-1\). Thus \((n-3,2,1)\) majorizes every remaining triple. Strict concavity gives equality in the minimal cycle-area term only for permutations of this triple, i.e. one graph up to isomorphism. Substitution gives \(6(n-3)F_1+2(F_3+F_2+F_1)=A_2(n)\); the gap is strict since \(3(n-3)>n-1\). This also covers \(n=5\), where the split leaf allocation is \((2,2,1)\) in rooted-tree orders.

## Verification

The bundled checker `check_unicyclic_surface.py` uses enumeration of nonisomorphic unicyclic graphs and compares area via connected bipartitions and via the bridge/cycle-pair formula; these are finite floating-point consistency checks. It also compares to convex-hull areas in selected cases through order six. The comparisons of all excluded classes and the strict-concavity equality argument above, not this enumeration, prove the second level for every \(n\ge5\). The checker requires Python 3, NetworkX, NumPy and SciPy.

## Relationship to prior work and limitations

The earlier unicyclic result [1] gives both the exact area formula and the unique minimizer **within every fixed cycle length** with off-cycle vertices. In particular the triangle benchmark is already an exact specialization; only a comparison across cycle lengths is needed for the global first level. Its balanced maximum and stability bound within the direct-leaf family address another end of the area range, not the least area after removing the minimizer. The additional result here is the sharp second level over *all* connected simple unicyclic graphs, with the unique extremizer and exact gap. The separation from the longer cycles and from non-leaf attachments is needed before a discrete second-level optimization over leaf allocations can establish this global statement.

Padrol–Pilaud–Poullot [2] give the face and normal framework for graphical zonotopes. Joós–Lángi [3] give the general Euclidean intrinsic-volume decomposition; their abstract zonotope isoperimetry does not itself order these incidence-vector realizations. The second-level result does not describe the rest of the spectrum, the maximum among all unicyclic graphs, or weighted, multicyclic or affinely distorted realizations. Priority beyond the sources compared is provisional.

## References

1. *Sharp minimum and stability of surface area for unicyclic graphical zonotopes*, Resultary record `fa812a991423`, 2026-10-25, Eqs. (1) and (4). https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-sharp-minimum-and-stability-of-surface-area-for-unicyclic-graphi--fa812a991423
2. A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422. https://arxiv.org/abs/2111.12422
3. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204. https://arxiv.org/abs/2206.03204
