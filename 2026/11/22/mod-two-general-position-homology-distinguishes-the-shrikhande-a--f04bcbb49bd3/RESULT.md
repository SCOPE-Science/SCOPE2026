# Mod-two general-position homology distinguishes the Shrikhande and four-by-four rook graphs

## Finding

Let \(\operatorname{GP}(G)\) be the abstract simplicial complex of all subsets of vertices of a graph \(G\) containing no three vertices on a common shortest graph path. For the Shrikhande graph \(\mathrm{Sh}\) and the four-by-four rook graph \(R=K_4\square K_4\), the complete reduced homology over \(\mathbb F_2\) is

\[
\widetilde H_i(\operatorname{GP}(\mathrm{Sh});\mathbb F_2)\cong
\begin{cases}\mathbb F_2^{57},&i=3,\\0,&i\ne3,\end{cases}
\qquad
\widetilde H_i(\operatorname{GP}(R);\mathbb F_2)\cong
\begin{cases}\mathbb F_2^{98},&i=3,\\\mathbb F_2,&i=4,\\0,&\text{otherwise}.\end{cases}
\]

Both graphs are strongly regular with parameters \((16,6,2,2)\), but their general-position complexes have different mod-two homology, including a fourth-dimensional class only on the rook side. In size order, including the empty simplex, their face-count vectors are respectively \((1,16,120,416,672,432,144,16)\) and \((1,16,120,416,632,240,16)\).

## Assumptions and scope

The vertex set of each graph is \((\mathbb Z/4\mathbb Z)^2\), indexed lexicographically by \((a,b)\) with \(a,b\in\{0,1,2,3\}\). In \(\mathrm{Sh}\), two distinct vertices are adjacent precisely when their difference is one of \(\pm(1,0)\), \(\pm(0,1)\), \(\pm(1,1)\) modulo four. In \(R\), distinct \((a,b)\) and \((c,d)\) are adjacent precisely when \(a=c\) or \(b=d\). Every graph distance and every geodesic is taken in the *original full graph*, not in a subgraph induced by a proposed face. Homology is reduced simplicial homology with coefficients in \(\mathbb F_2\). No claim is made for arbitrary graphs with these parameters.

## Proof

Each graph has sixteen vertices, six neighbors at each vertex, and precisely two common neighbors for every pair of distinct vertices, independently of adjacency. These assertions follow by enumerating coordinate differences; the verifier exhaustively checks them. In particular, every nonadjacent pair has distance two. Consequently a triple lies on a geodesic if and only if its induced graph is a three-vertex path: a geodesic containing three distinct vertices has length two, while every induced two-edge path joins a nonadjacent pair and is therefore shortest.

Thus a subset is a face if and only if none of its three-subsets induces exactly two edges. Each graph has precisely 144 forbidden triples: the 72 nonedges have exactly two common neighbors, and each forbidden triple has one uniquely determined nonadjacent endpoint pair. Equivalently a face induces a disjoint union of cliques. These two equivalent predicates are independently checked on **all** \(2^{16}=65536\) vertex subsets.

Let \(c_k\) denote the number of faces of cardinality \(k\), with \(c_0=1\). Let \(r_k\) be the exact rank over \(\mathbb F_2\) of the augmented simplicial boundary sending a face of cardinality \(k\) to the sum of its \(k\) immediate subfaces. Then \(r_1=1\), and the mod-two reduced Betti number in degree \(k-1\) equals \(c_k-r_k-r_{k+1}\), where the final missing rank is zero. The exact computation yields:

| Graph | \((c_0,c_1,\ldots)\) | \((r_1,r_2,\ldots)\) |
|---|---|---|
| Shrikhande | \((1,16,120,416,672,432,144,16)\) | \((1,15,105,311,304,128,16)\) |
| Four-by-four rook | \((1,16,120,416,632,240,16)\) | \((1,15,105,311,223,16)\) |

Every column is assembled by deleting each vertex from the corresponding face. Field-two Gaussian elimination is carried out exactly, with integer bitsets and XOR, never floating-point numerical rank. A second, independent row-bitset implementation computes every same rank on the transposed boundary matrix. The program verifies that consecutive boundary maps compose to zero, that each generated face has every codimension-one subface, and that the alternating face count agrees with the resulting Euler characteristic. The claimed homology follows immediately from the displayed rank identity.

## Verification

Run `python3 verify.py` using Python 3 and no external packages. The script checks the strongly regular parameters, forbidden triples, all 65,536 masks by two different face-membership predicates, the complete face vectors, every mod-two boundary rank by two elimination orientations, consecutive boundary compositions, and reduced Euler identities. The run completed with `ALL CHECKS PASSED`. These are exhaustive finite calculations, not statistical experiments.

## Relationship to prior work

Manuel and Klavžar (2017) introduced the graph-geodesic general-position problem. Anand, Chandran, Changat, Klavžar, and Thomas (2018 preprint) characterize general-position vertex sets; their graph-theoretic characterization supplies context for the induced-path formulation. Iršič, Klavžar, Rus, and Tuite (2024 preprint) study general-position counting polynomials rather than the mod-two homology of this strongly regular pair. Published work on three-row rook-graph general-position complexes concerns graphs with exactly three rows, not the four-by-four rook graph; published computations for Shrikhande/rook higher-independence and four-vertex-path-free complexes concern different face predicates. Numerical coincidence between an unrelated homology rank and the value 57 does not imply that the complexes have the same homology. No covering statement was identified in the inspected texts and indexed mathematical records; an unindexed equivalent computation remains possible.

## Limitations

Only reduced homology over \(\mathbb F_2\) is determined. Neither integral torsion, rational homology, wedge decompositions, fundamental groups nor group actions are claimed. The finite computation concerns exactly the two specified sixteen-vertex graphs; it does not imply any infinite-family formula or a result for all strongly regular graphs. The literature check does not prove absolute novelty.

## References

- P. Manuel and S. Klavžar, *Graph theory general position problem*, public preprint 2017-08-30, https://arxiv.org/abs/1708.09130 .
- B. S. Anand, U. Chandran S. V., M. Changat, S. Klavžar, E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, public preprint 2018-12-20, https://arxiv.org/abs/1812.08460 .
- V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General position polynomials*, public preprint 2024-01-11, https://arxiv.org/abs/2401.05696 .
