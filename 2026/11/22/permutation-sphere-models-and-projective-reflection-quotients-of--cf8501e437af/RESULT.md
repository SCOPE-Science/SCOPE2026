# Equivariant permutation spheres for independence complexes of higher-arm spiders

## Finding

Let \(k\ge3\) and \(\ell\ge2\). Form a tree \(T_{k,\ell}\) by attaching \(k\) paths of \(\ell\) edges at a common hub, and let \(X_{k,\ell}=|\operatorname{Ind}(T_{k,\ell})|\). The full symmetric group \(S_k\) acts by permuting the arms. There are genuine \(S_k\)-homotopy equivalences
\[
X_{k,3m}\simeq_{S_k}*,\qquad
X_{k,3m+1}\simeq_{S_k}S\!\left(\mathbb R\oplus(\mathbb R^m\otimes\mathbb R^k)\right),\qquad
X_{k,3m+2}\simeq_{S_k}S\!\left(\mathbb R^{m+1}\otimes\mathbb R^k\right),
\]
with \(m\ge1\) in the first two cases and \(m\ge0\) in the third. Here \(S(V)\) is the real unit sphere, \(S_k\) permutes the basis of \(\mathbb R^k\), and the other factors have trivial action.

For any subgroup \(H\le S_k\) with \(o\) arm orbits, the geometric fixed space is canonically PL homeomorphic to \(|\operatorname{Ind}(T_{o,\ell})|\), allowing \(o=1\) or \(2\) in this fixed-space formula. Its homotopy type is a point, \(S^{mo}\), or \(S^{(m+1)o-1}\) in the three cases above. The ambient top reduced integral homology has orientation character \(\operatorname{sgn}^m\) or \(\operatorname{sgn}^{m+1}\) in the respective sphere cases.

## Assumptions and scope

The ordinary vertex independence complex has all vertex subsets containing no edge as faces. The vertices are a hub \(c\) and arm vertices \((a,j)\) for \(1\le a\le k\), \(1\le j\le\ell\); adjacency is between successive depths in the same arm and between \(c\) and the first vertex of each arm. The action is the literal geometric realization of this simplicial action. Fixed spaces include points in setwise invariant simplices, not just faces on individually fixed vertices. The representation-sphere equivalences are not asserted to be PL homeomorphisms. The claim is restricted to uniform arms and concerns a single model for all subgroups of the full arm permutation group.

## Proof

For \(\ell\ge3\) remove every vertex \((a,\ell-2)\). There is an equivariant simplicial retraction onto the deletion: send each removed vertex to \((a,\ell)\), leaving the others unchanged. The only neighbor of \((a,\ell)\) is \((a,\ell-1)\), which is also a neighbor of the removed vertex. The replacement vertices on distinct arms are mutually nonadjacent. Consequently, for every independent face its union with its image is still independent. This is equivariant contiguity: affine interpolation inside each such union gives an equivariant homotopy relative to the deletion. This argument works even when \(\ell-2=1\), where the removed vertices also neighbor the hub.

The deletion is the disjoint union of the shorter spider with arm length \(\ell-3\) and \(k\) isolated edges, each edge being attached to no other vertex. The group acts diagonally by permuting the shorter arms and permuting the edges, without flipping either endpoint within a factor. Independence complexes turn disjoint unions into joins, so the step joins \(X_{k,\ell-3}\) with the permuted join of \(k\) copies of \(S^0\). Model that join as \(S(\mathbb R^k)\) by using the two points of the \(a\)-th factor as the two opposite directions of coordinate \(a\).

The three starting models are as follows. For zero arm length the graph is the single hub, giving a point. For one edge the independence complex is the simplex on the arm vertices disjoint from the hub, with equivariant contraction of that simplex to its barycenter, giving \(S^0\) with trivial action. For two edges, deleting the hub gives the join of \(k\) two-point complexes. The only extra part is a cone from the hub on the simplex of the \(k\) leaf vertices, and it retracts onto that simplex by sending the hub to its invariant barycenter and fixing the simplex, with straight-line homotopy in the cone. The two-edge model is therefore \(S(\mathbb R^k)\). A join of spheres of orthogonal representations is the sphere of the direct sum, equivariantly by the square-root weighting of join coordinates. A join with a fixed-point model that equivariantly contracts to a point is an equivariant cone up to homotopy. Iterating the deletion proves all three claims, including \(\ell=2,3,4\).

For the fixed space, a realization point is fixed by \(H\) exactly if its barycentric weights are constant on the vertex orbits. Each orbit is independent, and the compatibility of whole orbits is exactly the independence test on the smaller spider: adjacent positive depths give an edge precisely within a single arm orbit, and the hub forbids all first depths. Affine extension of the map from these orbit vertices to their barycenters gives the asserted PL homeomorphism. Taking fixed subspaces in the sphere models replaces \(\mathbb R^k\) by a space of dimension \(o\), giving the dimensions. Finally the degree of the sphere action is the determinant of the corresponding linear action. There are respectively \(m\) or \(m+1\) permutation blocks, so this is the stated sign power.

## Relationship to prior work

Ehrenborg–Hetyei [1, Corollaries 6.1, 6.3] establish the underlying nonequivariant forest and path sphere-or-contractible results. Kawamura [2] studies nonequivariant homotopy types of forest independence complexes. The earlier *Reflection quotients of path independence complexes as projective suspensions* [3, Finding] gives the reversal representation and ordinary geometric orbit space for paths. In particular it already includes both odd-path projective join series, the contractible residue class and the integral torsion example at \(P_{17}\). None of these two-arm conclusions is an added finding here. The earlier subdivided-star record [4, Finding] gives the ordinary homotopy type and integral sign when \(\ell=2\) in the ordinary case. It does not assert a simultaneous equivariant model for the full arm action. The contribution concerns the full \(S_k\) action for higher-arm ordinary spiders: a path reversal calculation or separate orientation and fixed-space results do not specify this ambient equivariant homotopy type.

## Verification and limitations

The proof uses an explicit equivariant retraction on every three-edge step, not an inference from ordinary homology. `python3 checks/verify_spider.py` independently tests contiguity of the fold on all faces in four higher-arm examples and compares orbit-face sets for selected subgroups, including the full \(S_3\). These are bounded tests of the combinatorial steps, not proofs of the infinite classification. Other arm lengths, other graph complexes and arbitrary automorphism groups are not covered. The available prior comparisons are not an exhaustive priority search; equivalent constructions in unindexed sources remain possible.

## References

1. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923, https://www.ms.uky.edu/~jrge/Papers/Independence.pdf .
2. K. Kawamura, *Homotopy types of independence complexes of forests*, Contributions to Discrete Mathematics 5 (2010), https://cdm.ucalgary.ca/article/view/62064 .
3. *Reflection quotients of path independence complexes as projective suspensions*, Resultary, 2026-11-17, https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-reflection-quotients-of-path-independence-complexes-as-projectiv--0bdf05d1d268/RESULT.md .
4. *Higher independence complexes of subdivided stars*, Resultary, 2026-11-08, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-higher-independence-complexes-of-subdivided-stars-homotopy-types--e0ebcee83467/RESULT.md .
