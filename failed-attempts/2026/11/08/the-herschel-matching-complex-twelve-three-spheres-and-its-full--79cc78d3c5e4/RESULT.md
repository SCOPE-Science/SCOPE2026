# The Herschel matching complex: twelve three-spheres and its full symmetry character

## Finding

For the eleven-vertex Herschel graph \(H\), let \(\mathcal M(H)\) be the ordinary simplicial matching complex: its vertices are the graph edges, and its faces are sets of pairwise vertex-disjoint edges. Then

\[\mathcal M(H)\simeq\bigvee^{12}S^3.\]

There is an explicit natural splitting \(\operatorname{Aut}(H)\cong S_3\times C_2\). Let \(\rho\) be the rational standard two-dimensional representation of \(S_3\), let \(\operatorname{sgn}\) denote its sign representation, and let \(\varepsilon\) be the nontrivial one-dimensional representation of \(C_2\). The entire rational homology representation is

\[\widetilde H_3(\mathcal M(H);\mathbb Q)\cong (\mathbf1\oplus2\rho)\boxtimes\mathbf1\ \oplus\ (\operatorname{sgn}\oplus3\rho)\boxtimes\varepsilon.\]

In particular, \(\widetilde H_3(\mathcal M(H);\mathbb Z)\cong\mathbb Z^{12}\); all other reduced integral homology groups vanish. The full group-invariant rational homology has dimension one, while the central involution has eigenspaces of dimensions five and seven.

## Assumptions and scope

The graph is defined without reliance on a drawing. Take the vertices \(0,1,2\) (degree four), \(3,4\) (two degree-three poles), and six vertices \(w_{ij,t}\), indexed by \(0\leq i<j\leq2\) and \(t\in\{0,1\}\). For each \(w_{ij,t}\), include precisely the three edges joining it to \(i\), \(j\), and \(3+t\). There are exactly 18 edges and no other edges. This is the standard bipartite Herschel graph: three degree-four vertices, two degree-three poles, and six degree-three common neighbors, with three four-cycles formed by pairs of degree-four vertices. It is a three-connected planar graph and the classical smallest-order non-Hamiltonian polyhedral graph.

The graph's 18 edges are sorted lexicographically as unordered pairs of the specified numerical vertex labels, with \(w_{01,0},w_{01,1},w_{02,0},w_{02,1},w_{12,0},w_{12,1}\) represented by the labels \(5,6,7,8,9,10\). Every face is encoded by its 18-bit edge-incidence mask, and the empty face is distinguished from the geometric vertices of the simplicial complex.

## Proof

**Integral homotopy.** Two distinct exhaustive enumerators agree on all face masks. The numbers of nonempty simplices in dimensions \(0\) through \(4\) are, respectively, \((18,111,280,270,72)\), totaling 751. In particular the ordinary Euler characteristic is \(-11\).

Construct a matching on the nonempty face poset as follows. Initially all nonempty faces are unpaired. Process the 18 edge coordinates in the order `6,17,8,0,9,16,10,11,14,12,1,4,15,5,13,7,3,2`. At the stage with pivot coordinate \(e\), pair every still-unpaired face \(\sigma\) not containing \(e\) with \(\sigma\cup\{e\}\) whenever both are currently unpaired faces. This gives 369 disjoint cover pairs and leaves exactly one critical vertex and twelve critical dimension-three simplices.

This is an *acyclic* matching, not merely a collection of disjoint pairs. Orient each of the 2,502 covering relations in the nonempty face poset from the higher-dimensional simplex to its facet, except reverse each matched relation. The resulting directed graph on 751 nodes admits a complete topological ordering of all 751 nodes; therefore it has no directed cycles. The accompanying standalone verifier constructs these orientations directly and checks the ordering exhaustively.

By the acyclic-matching theorem of discrete Morse theory, \(\mathcal M(H)\) has the homotopy type of a CW complex with exactly the critical cells just described: one zero-cell and twelve three-cells, with no cells in dimensions one or two. Every attaching map of a three-cell to the single zero-cell is constant. Thus this CW complex is precisely a wedge of twelve three-spheres up to homotopy. This is an integral homotopy argument, not a deduction from field-valued Betti numbers.

**Group and character.** Any graph automorphism permutes the three unique degree-four vertices and separately permutes the two remaining degree-three vertices that have *no* degree-four neighbors. Every other vertex is uniquely identified by the unordered pair of its degree-four neighbors and by its adjacent pole. Conversely, every choice of a permutation of the three high-degree vertices and an independent interchange of the poles extends uniquely to a graph automorphism. Hence the full group has order twelve and is \(S_3\times C_2\).

For a simplicial automorphism \(g\), count the signed fixed oriented simplices in the augmented simplicial chain complex. Because the only nonzero reduced homology is in dimension three, its rational character is the *negative* of the reduced simplicial Lefschetz number. The exact class traces are:

| \(S_3\) conjugacy class | identity on \(C_2\) | nontrivial element of \(C_2\) |
|---|---:|---:|
| identity | 12 | -2 |
| transposition | 0 | 2 |
| three-cycle | -3 | 1 |

Taking inner products with the six rational irreducible characters of \(S_3\times C_2\) gives multiplicities \(1,0,0,1,2,3\) for, respectively, the trivial, pole-sign, permutation-sign, product-sign, standard-even, and standard-odd representations. This is the decomposition stated above.

## Verification

Run `python3 herschel_matching_verify.py` using Python 3.8 or later. The code is standalone and uses only the standard library. It constructs the graph and complex from the stated definitions, independently enumerates all 262,144 possible edge masks, verifies all 2,502 face-cover orientations, and checks the exact discrete-Morse critical-cell count. It separately computes signed simplicial boundary ranks over the fields of orders \(2,3,5,101\) (ranks \(17,94,186,72\) for dimensions one through four). Those finite-field calculations corroborate, but are not substituted for, the integral homotopy proof.

All twelve group-element Lefschetz characters are evaluated directly using signed fixed simplices. A second computation counts automorphism-stable unions of compatible edge-orbits with alternating signs and agrees on every character. Exact inner products with \(S_3\times C_2\) characters verify the multiplicities. The expected program output is included as `herschel_matching_verify_output.txt`.

## Relationship to prior work

Marietti and Testa (first public preprint May 10, 2007), Section 4.4 and Theorem 4.11, prove a sphere-wedge result for matching complexes of **forests**. The Herschel graph has four-cycles and is not a forest. Bayer, Jelić Milutinović and Vega (first preprint November 7, 2024), Theorem 2, prove a wedge-or-contractible result for **outerplanar** graphs; the Herschel graph is not outerplanar, since all its vertices have degree at least three. Neither theorem gives the above rank or automorphism character. Their proofs and conclusion were inspected for possible stronger coverage.

The published Goldner–Harary matching-complex computation concerns a different non-Hamiltonian polyhedral graph on eleven vertices; its sphere multiplicities do not imply the present Herschel computation. The ordinary independence complex of the Herschel graph and its graph-metric Vietoris–Rips complexes concern distinct face predicates. The precise identity \(\mathcal M(H)=\operatorname{Ind}(L(H))\), where \(L(H)\) is the graph's line graph, was included in the novelty comparison. Targeted searches found no examined statement already giving this integral homotopy classification or the full rational group character. These searches do not establish absolute publication priority.

## Limitations

The theorem concerns one specified graph, not an entire class of polyhedral graphs. A rational homology representation does not determine an integral representation lattice or an equivariant wedge splitting. No independent mathematical audit has been performed, and inaccessible or unindexed prior work could affect the originality assessment.

## References

1. M. Marietti and D. Testa, *A Simple Uniform Approach to Complexes Arising from Forests*, arXiv:0705.1461v1, first public May 10, 2007. https://arxiv.org/abs/0705.1461
2. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, first public November 7, 2024. https://arxiv.org/abs/2411.04601
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145. DOI: 10.1006/aima.1997.1650.
4. E. W. Weisstein, *Herschel Graph*, MathWorld. https://mathworld.wolfram.com/HerschelGraph.html
