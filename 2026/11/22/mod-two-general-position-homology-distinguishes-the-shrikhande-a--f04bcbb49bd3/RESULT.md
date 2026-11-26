# Mod-two general-position homology of the Shrikhande graph

## Finding
Let \(\operatorname{GP}(G)\) consist of the subsets of vertices of \(G\) containing no three vertices on a common shortest path of the full graph. For the Shrikhande graph \(\mathrm{Sh}\), the complete reduced homology with coefficients in \(\mathbb F_2\) is
\[
\widetilde H_i(\operatorname{GP}(\mathrm{Sh});\mathbb F_2)\cong
\begin{cases}\mathbb F_2^{57},&i=3,\\0,&i\ne3.\end{cases}
\]
The face counts by size, beginning with the empty face, are \((1,16,120,416,672,432,144,16)\).

This distinguishes Shrikhande from its strongly regular counterpart \(R=K_4\square K_4\). The separately established homotopy equivalence \(|\operatorname{GP}(R)|\simeq (\bigvee^{98}S^3)\vee S^4\) [1] implies mod-two reduced ranks 98 and 1 in degrees 3 and 4, respectively. Those ranks and the previously enumerated rook face counts [2] are comparison data, not new claims here.

## Graph and chain model
Use vertex set \((\mathbb Z/4\mathbb Z)^2\), indexed lexicographically, with edges at differences \(\pm(1,0),\pm(0,1),\pm(1,1)\) in Shrikhande and edges between distinct vertices sharing a coordinate in the rook graph. For Shrikhande the six difference vectors give degree six, and enumerating the differences between the six vectors gives exactly two common neighbors for every pair of distinct vertices. Hence the graph has diameter two and any forbidden geodesic triple is an induced three-vertex path. Conversely any induced three-vertex path has nonadjacent endpoints, so it lies on a shortest path. There are 144 forbidden triples: 72 unordered nonedges, each with two choices for the middle vertex.

## Exact computation
Generate every mask from \(0\) to \(2^{16}-1\), keeping it if none of the forbidden triple masks is contained in it. Equivalently, test that every component of the induced subgraph is complete, since a shortest path between nonadjacent vertices within a component of a \(P_3\)-free graph is impossible. For each size \(k\), make one column for each retained mask of size \(k\) and one row for each retained mask of size \(k-1\). Set a row entry to one exactly when its mask is obtained by removing one vertex of the column face. This is the augmented simplicial boundary; composition vanishes because each removal of an unordered pair is counted twice. Eliminate modulo two using XOR, counting independent pivots. The exact Shrikhande counts are:

| Face size \(k\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Faces \(c_k\) | 1 | 16 | 120 | 416 | 672 | 432 | 144 | 16 |
| Boundary rank \(r_k\) | 0 | 1 | 15 | 105 | 311 | 304 | 128 | 16 |

Writing \(r_8=0\), the reduced Betti number in degree \(k-1\) is \(c_k-r_k-r_{k+1}\). It is 57 at \(k=4\), by \(672-311-304=57\), and zero otherwise. The zero in degree \(-1\) is included since the augmentation is onto. In particular the absence of degree-four mod-two homology contrasts with the known rook case even though both graphs have parameters \((16,6,2,2)\).

## Verification and scope
Run `python3 verify.py` from the package directory. The program checks the two equivalent face predicates on all \(2^{16}\) masks, computes each rank by row and column elimination, and checks the boundary composition and Euler identities. Its rook calculation replays the comparison data. Only reduced mod-two homology is asserted for Shrikhande; no integral, rational, torsion, equivariant, or homotopy classification is claimed.

## Relationship to prior work
The general-position characterization of Anand et al. [3] encompasses the face predicate on these diameter-two graphs. The general-position polynomial of Iršič et al. [4] encodes face counts. Neither characterization nor face counts determine the boundary ranks used here. Higher-independence complexes and four-vertex-path avoidance complexes impose different constraints. Equivalent unlocated computations may exist.

## References
1. *Ninety-eight three-spheres and one four-sphere in the four-by-four rook general-position complex*, [result](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-ninety-eight-three-spheres-and-one-four-sphere-in-the-four-by-fo--7d66b9444862/RESULT.md).
2. *General-position polynomials of rectangular rook graphs via bipartite star forests*, [result](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-general-position-polynomials-of-rectangular-rook-graphs-via-bipa--fc2af413d7b2/RESULT.md).
3. B. S. Anand et al., *Characterization of general position sets and its applications to cographs and bipartite graphs*, [arXiv:1812.08460](https://arxiv.org/abs/1812.08460).
4. V. Iršič et al., *General position polynomials*, [arXiv:2401.05696](https://arxiv.org/abs/2401.05696).
