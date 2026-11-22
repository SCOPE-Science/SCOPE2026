# Mixed circle–sphere homotopy and square symmetries of the first planar grid general-position complex

## Finding

Let \(G=P_3\square P_3\), with vertices \((i,j)\) for \(i,j\in\{0,1,2\}\) and graph distance \(d((i,j),(k,l))=|i-k|+|j-l|\). A vertex set is in general position when none of its triples lies on a common graph geodesic; its simplicial complex is \(X=\operatorname{GP}(G)\). The exact integral homotopy type is
\[
|X|\simeq\bigvee^{14}S^1\vee S^2.
\]

The square's eight graph symmetries act on the one-dimensional integral group \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z\) by the determinant of their planar coordinate action. On \(\widetilde H_1(X;\mathbb Q)\), their traces are:

| Square symmetry | Trace on \(H_1\) | Trace on \(H_2\) |
|---|---:|---:|
| Identity | 14 | 1 |
| Quarter or three-quarter turn | 0 | 1 |
| Half turn | -2 | 1 |
| Horizontal or vertical reflection | 2 | -1 |
| Either diagonal reflection | 0 | -1 |

Averaging the character over \(D_4\) gives
\[
\widetilde H_k(|X|/D_4;\mathbb Q)\cong
\begin{cases}\mathbb Q^2,&k=1,\\0,&k\ne1.\end{cases}
\]
The quotient statement is about rational homology, not its integral homotopy type.

## Assumptions and scope

The graph uses the four-neighbor Cartesian product, not the nine-vertex rook graph. A triple \(\{u,v,w\}\) is forbidden exactly when, after permuting the vertices, \(d(u,v)=d(u,w)+d(w,v)\). Vertices are indexed by \(3i+j\), from \(0\) to \(8\). Every two-vertex subset is a simplex. All homotopy statements concern the geometric realization of this finite abstract simplicial complex. The action of \(D_4\) is induced by the usual rotations and reflections of the square.

## Proof

**Face classification.** Enumerating the nine metric points and rejecting subsets with a forbidden triple gives precisely nine vertices, thirty-six edges, sixteen triangles and one tetrahedron; the latter has vertex indices \((1,3,5,7)\). No graph-distance-one edge lies in a permitted triangle: a third grid point lies beyond one endpoint in at least one of the two edge directions, making that endpoint geodesically intermediate. Therefore the twelve original grid edges attach only to vertices of the complex formed from the remaining twenty-four edges and all higher faces.

**Integral homotopy.** The triangle \((1,3,5)\) occurs in the unique tetrahedron and no other three-dimensional face. Their deletion is an elementary simplicial collapse. In the remaining two-dimensional complex, omit the twelve grid edges temporarily, leaving a connected nine-vertex CW complex \(Y\) with twenty-four edges and fifteen triangles. The explicit checker constructs a spanning tree of eight edges. Contracting this tree leaves sixteen oriented edge generators and fifteen triangular attaching words. Fourteen successive eliminations each select an attaching word containing one generator exactly once with exponent \(\pm1\), solve for that generator and substitute into the remaining words. Each step is a standard elementary two-cell/one-cell CW homotopy cancellation (equivalently, a Nielsen change followed by a free-cell cancellation). Exactly two edge generators and one freely trivial two-cell attaching word remain. Hence \(Y\simeq S^1\vee S^1\vee S^2\). Reattaching the twelve grid edges between vertices of connected \(Y\) contributes twelve independent one-cells with both endpoints identified up to homotopy. This proves \(X\simeq\bigvee^{14}S^1\vee S^2\), integrally and at the level of homotopy, not merely from Betti numbers.

**Symmetry action.** The verifier supplies an explicit oriented fourteen-triangle integral cycle \(z\) with vanishing boundary. The above integral cellular reduction shows the top homology is infinite cyclic; since \(z\) has a coefficient \(\pm1\) on a triangle outside the tetrahedron's boundary, it is primitive. For each of the eight square symmetries, applying the signed simplicial permutation gives \(g(z)-\det(g)z\) as an integral multiple of the unique tetrahedral boundary. Thus \(g_*\) acts by \(\det(g)\) on \(H_2\). The signed simplicial fixed-face trace gives each Lefschetz number \(L(g)\). Since the only homology degrees are zero, one and two, \(\operatorname{tr}(g_*|H_1)=1+\det(g)-L(g)\), yielding the table. For finite simplicial group actions, rational homology of the geometric orbit space equals the invariant rational homology (after an equivariant subdivision). Character averaging gives two first-dimensional invariant classes and no second-dimensional invariant class.

## Verification

Run `python3 verify_gp3x3.py` from a directory containing that standalone file, using Python 3. The script reconstructs all faces directly from the Manhattan metric, the free tetrahedral collapse, the connected non-grid one-skeleton, the fourteen deterministic generator/relator eliminations, a primitive signed two-cycle, and the complete dihedral character calculation. It checks exact integer identities without relying on a precomputed homology table. The full script exits normally only if every asserted identity passes.

## Relationship to prior work

Manuel and Klavžar (first public preprint 2017) establish general-position bounds for grid networks, including the four-point bound. Iršič, Klavžar, Rus and Tuite (first public preprint 2024) give the entire general-position polynomial for rectangular Cartesian grids, implying the face vector used here, but not the attaching maps, fundamental group, integral sphere splitting or dihedral homology character. The present result uses their combinatorial setting, not a claim to rederive their polynomial as new. Results for rook-graph general-position complexes, ordinary grid matching complexes, and higher robust clique complexes concern different permitted simplices and do not imply this statement.

## Limitations

Only the nine-vertex square grid is classified; this does not prove the analogous homotopy type for any larger rectangle. The quotient assertion is rational, so no claim about torsion or its integral homotopy type is made. An unindexed earlier equivalent topological calculation remains a bibliographic possibility. No independent review is claimed.

## References

1. P. Manuel and S. Klavžar, *The graph theory general position problem on some interconnection networks*, first public preprint 2017-09-30, https://arxiv.org/abs/1710.00244.
2. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General position polynomials*, first public preprint 2024-01-11, https://arxiv.org/abs/2401.05696; published *Results in Mathematics* 79 (2024), article 110, https://doi.org/10.1007/s00025-024-02133-3.
