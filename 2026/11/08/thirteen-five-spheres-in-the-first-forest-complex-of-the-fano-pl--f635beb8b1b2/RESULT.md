# Thirteen five-spheres in the first forest complex of the Fano-plane incidence graph

## Finding

For the Heawood graph \(H\), the incidence graph of the Fano plane, the first positive-level forest-filtration complex has integral homotopy type
\[
\mathcal F_1(H)\simeq\bigvee^{13}S^5.
\]
Thus \(\widetilde H_5(\mathcal F_1(H);\mathbb Z)\cong\mathbb Z^{13}\), and every other reduced integral homology group vanishes. This determines the homotopy type rather than only homology with coefficients in a field.

## Assumptions and scope

Take the points of the Fano plane to be the seven nonzero vectors of \(\mathbb F_2^3\), encoded by integers 1 through 7 in binary. Its seven lines are the distinct unordered triples \(\{a,b,a\oplus b\}\), for distinct nonzero vectors \(a,b\), with \(\oplus\) denoting bitwise XOR. Label the point vertices 0 through 6 and the line vertices 7 through 13, with incidence edges connecting a point to each line containing it. This specifies a simple, undirected, 14-vertex, 21-edge graph \(H\).

A simplex of \(\mathcal F_1(H)\) is a set of graph vertices inducing a graph with maximum degree at most one. Such a graph is automatically a forest, so this is exactly the first forest complex as defined by Carnero Bravo and also the two-independence complex. The empty simplex is included; geometric realizations use the nonempty simplices. The calculation is solely for this fixed graph and this filtration level.

## Proof

The finite proof uses an explicit acyclic discrete-Morse matching, completely reconstructed and checked by the accompanying standalone Python program `verify.py`.

First, generate the seven Fano lines and the 14 adjacency bitmasks. Every selected vertex can have at most one selected neighbor. Equivalently, the selected set contains none of the 42 three-vertex subsets consisting of two distinct neighbors of the same center. Testing every one of the \(2^{14}=16{,}384\) vertex subsets with both predicates gives identical classifications. Exactly 2,257 subsets, including the empty set, are faces. The numbers of faces in dimensions \(-1,0,1,2,3,4,5,6\), respectively, are \(1,14,91,322,651,728,392,58\). There are 70 facets of dimension five and 58 facets of dimension six.

Discard the empty face from the ordinary face poset, and consider vertices of the underlying graph in the order \(0,1,\ldots,13\). At each stage, for each currently unmatched nonempty face \(\sigma\) not containing the next vertex \(v\), pair it with \(\sigma\cup\{v\}\) if that face is also currently unmatched. Remove both faces permanently before proceeding. This defines exactly 1,121 disjoint face pairs; the remaining critical faces are one vertex and thirteen five-simplices. Reverse the vertex order and repeat: the same critical-cell histogram results.

For each matching, orient every codimension-one incidence upwards except matched incidences, which are oriented downwards. There are exactly 10,150 nonempty-face Hasse incidences. A full topological-sort check visits every face of the directed graph, establishing that both matchings are acyclic, not merely locally valid. Discrete Morse theory therefore provides a CW homotopy model having one cell in dimension zero, thirteen cells in dimension five, and no others. Every attaching map of a five-cell has a point as its target and hence is null. The model is precisely a wedge of thirteen five-spheres, proving the integral homotopy equivalence.

## Verification

Run `python3 verify.py` with the Python standard library. The file `verification_output.txt` records one exact execution. The program constructs the graph from the Fano-plane XOR rule; tests all 16,384 possible vertex subsets against independent degree and forbidden-triple predicates; reconstructs both complete discrete-Morse matchings; explicitly verifies all 10,150 oriented Hasse incidences of each; and independently reduces each original simplicial boundary matrix over \(\mathbb F_2\). The reduced mod-two Betti number is 13 in dimension five and zero in all other dimensions. The reduced Euler characteristic is \(-13\), consistent with the sphere-wedge result. The mod-two calculation is corroborative; integral and homotopy conclusions follow from the fully checked acyclic Morse model, not from field calculations.

## Relationship to prior work

Carnero Bravo introduced the forest filtration \(\mathcal F_0(G)\subseteq\mathcal F_1(G)\subseteq\cdots\) and identifies its first positive stage with the two-independence complex. The paper calculates paths, cycles, double stars, cactus graphs and certain graph products; no Heawood/Fano incidence classification appears in the inspected statements and sections. Tsukuda's incidence-graph Alexander-duality theorem concerns the *ordinary* independence complex, and is therefore not a determination of this higher-independence stage. Ordinary matching and two-matching complexes take graph edges, rather than graph vertices, as the simplex vertices, so their homotopy types do not imply the stated result. The exact integral homotopy type is a new finite datum for the canonical incidence graph of the smallest projective plane, subject to the bibliographic limitation below.

## Limitations

The statement is for a single 14-vertex graph. It gives no formula for the incidence graphs of projective planes of higher orders, other levels of the forest filtration, or natural automorphism-group actions on homology. The comparison searched accessible mathematical records and relevant primary sources, but could miss an equivalent calculation in unindexed or inaccessible literature. The proof is finite, executable discrete Morse theory rather than a uniform argument for a graph family. No independent external audit has been performed.

## References

- Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first public preprint 2023-07-25, especially the definition and introductory discussion of the first stage and the families treated in Section 4. https://arxiv.org/abs/2307.13271
- Shuichi Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), https://doi.org/10.55016/ojs/cdm.v12i1.62277 (ordinary independence complexes, not the higher stage).
- Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (standard discrete Morse theory).
