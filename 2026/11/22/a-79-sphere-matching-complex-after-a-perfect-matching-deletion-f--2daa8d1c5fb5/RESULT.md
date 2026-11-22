# A 79-sphere matching complex after a perfect-matching deletion from \(K_8\)

## Finding
Let \(G\) be the graph on \(\{0,1,2,3,4,5,6,7\}\) obtained from the complete graph by removing the four disjoint edges \(\{0,1\},\{2,3\},\{4,5\},\{6,7\}\). Then its ordinary matching complex, whose vertices are the edges of \(G\) and whose simplices are pairwise disjoint edges, satisfies
\[
\mathcal M(G)\simeq\bigvee^{79}S^2.
\]
In particular, its reduced integral homology is free of rank \(79\) in degree \(2\) and zero in all other degrees. The corresponding matching complex of the intact \(K_8\) is known to be a wedge of \(132\) two-spheres [1].

## Assumptions and scope
The graph is the four-dimensional crosspolytope graph, also called the eight-vertex cocktail-party graph or \(K_{2,2,2,2}\). Edges are ordinary unordered pairs, matchings have no repeated endpoints, and homotopy is for the standard geometric realization of the finite abstract simplicial complex. The statement is specifically for this graph: it asserts no family-wide formula, equivariant decomposition, or persistence result.

## Proof
Enumerate allowed graph edges in lexicographic order as \(e_0,\ldots,e_{23}\), excluding pairs whose endpoint labels have the same integer quotient on division by two. Represent each face (matching) by a 24-bit integer. Enumerate every combination of up to four edges and retain precisely those with twice as many distinct endpoints as edges. The resulting face counts, starting with the empty face, are \((1,24,156,272,60)\), totaling \(513\).

Define a partial matching on the augmented face poset by the following 24 edge-toggle priorities (indices refer to the stated lexicographic edge order):

```text
2,18,23,6,17,0,20,10,11,3,19,7,8,1,15,5,13,22,21,12,9,4,14,16
```

At priority \(j\), scan still-unmatched faces in increasing bitmask order. Pair any still-unmatched face not containing \(e_j\) with the face obtained by adjoining \(e_j\), when that larger face is also still unmatched. Remove both faces before advancing. Each pair differs by exactly one edge, so is a legal Hasse-diagram matching.

Exhaustive enumeration in the accompanying verifier establishes exactly \(217\) disjoint pairs, leaving exactly \(79\) unmatched faces, each consisting of three graph edges (a two-simplex). The empty face belongs to one pair. For an explicit acyclicity certificate, orient every cover relation from higher to lower face except matched relations, which point from lower to higher. The verifier enumerates all \(1392\) oriented cover relations, and Kahn's integer indegree elimination removes all \(513\) vertices. Hence the directed Hasse graph is acyclic, with no closed gradient paths. This is a finite exhaustive certificate, not an inference from sampled paths.

Now discard the one pair involving the empty face. The empty face has no outward matched edge afterward, and cannot lie in a directed cycle; removing this pair cannot introduce any gradient cycle among nonempty faces. The ordinary discrete-Morse matching therefore has one unpaired zero-simplex and exactly \(79\) unpaired two-simplices, with no other critical cells. Forman's discrete Morse theorem gives a CW homotopy model consisting of one zero-cell and \(79\) two-cells, no one-cells. Every two-cell has a constant attaching map to the one-point zero-skeleton, so the CW complex is \(\bigvee^{79}S^2\), as asserted.

## Verification
The accompanying standalone Python file `verify_cocktail.py` is the finite certificate. Run `python3 verify_cocktail.py` using Python's standard library. It rebuilds the graph and every face from the definition; checks the exact face counts, exhaustive pairing, unmatched dimensions, absence of repeated pairs, and all cover orientations; and independently tests DAG acyclicity by a topological sweep. Its captured actual output is in `verification_output.txt`. The Euler characteristic check gives \(24-156+272-60=80=1+79\).

## Relationship to prior work
Mondal, Mukherjee, and Saha [1], especially Example 3.3, give a perfect discrete Morse matching for the complete-graph complex \(\mathcal M(K_8)\simeq\bigvee^{132}S^2\), a related but different complex. The present graph deletes four mutually disjoint graph edges and its matching complex has fewer vertices and a different face poset; the complete-graph result does not imply the count or wedge decomposition above. Bayer, Jelić Milutinović, and Vega [2] prove sphere-wedge existence for outerplanar graphs, but \(G\) has \(24\) edges on eight vertices and is not outerplanar (the outerplanar edge bound is \(13\)). The calculation provides an exact deletion comparison rather than a restatement of either theorem.

## Limitations
The result is one exact finite case. It provides no complete classification of matching complexes of all cocktail-party graphs, no automorphism representation, and no assertion about higher-dimensional matching complexes. Prior work not indexed by the inspected bibliographic searches could conceivably give an equivalent result or a more general theorem from which it follows. The Morse certificate verifies this specific face set and priority list; it is not an infinite-family proof.

## References
[1] A. Mondal, S. Mukherjee, and K. Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, arXiv:2305.02973, publicly posted May 4, 2023, especially Example 3.3, https://arxiv.org/abs/2305.02973 .

[2] M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, publicly posted November 7, 2024, especially Theorem 2, https://arxiv.org/abs/2411.04601 .
