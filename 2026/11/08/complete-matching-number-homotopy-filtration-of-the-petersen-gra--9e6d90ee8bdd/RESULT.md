# Complete matching-number homotopy filtration of the Petersen graph

## Finding

Let \(P\) be the Petersen graph, and for each integer \(k\ge 1\) let \(\operatorname{NM}_k(P)\) be the simplicial complex whose vertices are the edges of \(P\), with an edge subset \(F\) a face exactly when the matching number of \((V(P),F)\) is strictly smaller than \(k\). Then, for geometric realizations,

\[
\operatorname{NM}_k(P)\simeq
\begin{cases}
\bigvee^{6}S^1,&k=2,\\
\bigvee^{9}S^3,&k=3,\\
\bigvee^{4}S^5,&k=4,\\
\bigvee^{5}S^9,&k=5,\\
*,&k\ge 6.
\end{cases}
\]

Here the indicated wedge multiplicities are integral homotopy-type statements, not merely Betti numbers. The natural filtration by matching threshold is nested. For integer thresholds beginning at \(k=2\), its entire positive-degree reduced integral persistence barcode comprises six copies of \([2,3)\) in degree one, nine copies of \([3,4)\) in degree three, four copies of \([4,5)\) in degree five, and five copies of \([5,6)\) in degree nine. At \(k=1\) the complex has only the empty face (and thus no nonempty geometric realization).

## Assumptions and scope

Use the standard generalized Petersen presentation \(P=\operatorname{GP}(5,2)\): vertices \(0,1,\ldots,9\) and fifteen edges consisting of the outer cycle \(\{i,(i+1)\bmod 5\}\), inner pentagram \(\{5+i,5+(i+2)\bmod 5\}\), and spokes \(\{i,5+i\}\), where \(0\le i\le4\). Each undirected edge is stored with its smaller endpoint first and the fifteen resulting pairs are sorted lexicographically. A matching is a set of pairwise vertex-disjoint graph edges, and \(\nu(F)\) is its maximum cardinality. The simplicial complex contains the empty face, which is excluded from the usual unaugmented CW chain complex. The statement concerns precisely this graph and every possible matching threshold, not other graph complexes on the same ground graph.

## Proof

**Enumeration and discrete-Morse model.** For each threshold \(k\in\{2,3,4,5\}\), enumerate every \(k\)-edge matching of \(P\), encode it as a fifteen-bit mask, and retain precisely those edge subsets containing none of these masks. There are respectively \(75,145,90,6\) forbidden matchings, and the numbers of faces including the empty face are \(56,1073,8558,27449\). Their dimension-indexed face vectors (with the empty face in dimension \(-1\)) are:

| \(k\) | Face vector, from dimension \(-1\) upward |
|---|---|
| \(2\) | \((1,15,30,10)\) |
| \(3\) | \((1,15,105,310,405,207,30)\) |
| \(4\) | \((1,15,105,455,1275,2277,2480,1500,420,30)\) |
| \(5\) | \((1,15,105,455,1365,2997,4945,6165,5715,3760,1581,330,15)\) |

Apply the following deterministic elementary matching to nonempty faces. Process the fifteen edge-coordinate indices in increasing order. At each index, pair every remaining face not containing that coordinate with the face obtained by adding it, provided both faces are still unpaired. Direct each matched face-poset cover upward and every unmatched cover downward. Exhaustive topological sorting of this entire directed face graph confirms acyclicity, not just absence of a short cycle. The resulting matching-pair counts are \(24,530,4271,13720\); the directed graph contains respectively \(105,3990,47085,194040\) covering incidences. The critical-cell inventories, excluding the empty face, are:

| \(k\) | Critical cells by dimension |
|---|---|
| \(2\) | one in \(0\), six in \(1\) |
| \(3\) | one in \(0\), ten in \(3\), one in \(4\) |
| \(4\) | one in \(0\), eight in \(5\), five in \(6\), one in \(7\) |
| \(5\) | one in \(0\), six in \(9\), one in \(10\) |

Forman's discrete-Morse theorem therefore supplies finite CW complexes with precisely these critical cells and the same homotopy types as the original simplicial complexes.

**Signed integral Morse boundaries.** Order the critical faces of each dimension by their fifteen-bit mask. Orient every simplicial face by increasing edge index. For an oriented face \(\sigma=[e_0,\ldots,e_d]\), use the signed boundary \(\partial\sigma=\sum_j(-1)^j[\sigma\setminus\{e_j\}]\). To project a codimension-one face \(x\) to critical codimension-one faces, map a critical \(x\) to itself; map a face paired upward with \(y\) to the negative signed boundary of \(y\) with \(x\) eliminated, recursively; and map a face paired downward to zero. Acyclicity makes the recursion terminate. Applying it to each critical higher-dimensional face yields the following integer-column Morse matrices; any unlisted boundary into a noncritical dimension is zero.

For \(k=3\), the boundary from dimension four to three is the single ten-entry column
\[
(0,-1,1,-1,-1,-1,0,1,-1,1)^{\mathsf T}.
\]
For \(k=4\), the five columns of the boundary from dimension six to five are
\[
\begin{aligned}
&(0,0,-1,1,0,0,0,0)^{\mathsf T},\\
&(0,0,0,0,1,-1,0,0)^{\mathsf T},\\
&(0,1,-1,0,0,0,0,1)^{\mathsf T},\\
&(1,0,0,0,-1,0,1,1)^{\mathsf T},\\
&(1,-1,1,0,0,-1,1,0)^{\mathsf T}.
\end{aligned}
\]
The boundary from dimension seven to six is the column \((0,1,-1,1,-1)^{\mathsf T}\). Direct multiplication gives \(\partial_6\partial_7=0\). The dimension-six-to-five matrix has rank exactly four: the minor with zero-based row indices \((0,1,2,4)\) and column indices \((0,1,2,3)\) has determinant \(+1\), while its nonzero dimension-seven boundary lies in the kernel, so the rank is at most four. Consequently its image is a primitive sublattice, and its rank-one kernel is generated by the primitive dimension-seven boundary column. For \(k=5\), the boundary from dimension ten to nine is \((1,-1,-1,-1,1,0)^{\mathsf T}\). Both this column and the \(k=3\) boundary column contain unit entries, hence have primitive image. For \(k=2\), the six critical one-cells have zero boundary to the sole critical vertex.

**Integral homology and homotopy.** These matrices give precisely the following nonzero reduced integral homology: \(\widetilde H_1\cong\mathbb Z^6\) at \(k=2\), \(\widetilde H_3\cong\mathbb Z^9\) at \(k=3\), \(\widetilde H_5\cong\mathbb Z^4\) at \(k=4\), and \(\widetilde H_9\cong\mathbb Z^5\) at \(k=5\). All other reduced integral groups vanish, including all torsion. For \(k=2\), the CW model has one vertex and six loop edges, so it is a wedge of six circles. For each \(k\ge3\) under consideration, the Morse CW model has one vertex and no positive-dimensional cells below the one nonzero homology dimension. It is therefore simply connected and has the required connectivity. The Hurewicz isomorphism represents a basis of its sole nontrivial reduced homology by maps from spheres of that dimension. The induced map from their wedge is an integral homology equivalence between simply connected CW complexes, hence a homotopy equivalence by the homological Whitehead theorem. For \(k\ge6\), a matching of size \(k\) is impossible on ten vertices, so every subset of the fifteen edges is allowed: the complex is a simplex and is contractible.

**Filtration.** The complexes increase with \(k\). Since all nontrivial reduced homology in the four noncontractible stages occurs in different degrees, the induced maps to the next stage vanish in positive degrees. This yields exactly the persistence intervals stated above, with no unverified extension or infinite-range claim.

## Verification

Run `python3 verify_nonmatching.py` for the complete face enumeration, full directed-Hasse acyclicity check, signed Morse matrices, nonzero primitive boundaries and the exact unit minor. Run `python3 verify_kneser.py` for an independent construction of the Petersen graph as the Kneser graph on two-element subsets of a five-element set, an explicit vertex-isomorphism check, and exhaustive simplicial boundary ranks over \(\mathbb F_2\) in every dimension. The included `verify_nonmatching_output.txt` and `verify_kneser_output.txt` are the recorded outputs of these two programs. The integral result rests on the signed Morse calculation, not on the mod-two cross-check alone.

## Relationship to prior work

Linusson, Shareshian and Welker (first arXiv version October 15, 2004) introduced and analyzed these bounded-matching simplicial complexes for complete and complete bipartite graphs, proving exact uniform-dimensional sphere-wedge formulas. The Petersen graph is neither complete nor complete bipartite; the published formula for a complete graph does not determine the homotopy of an arbitrary induced subcomplex on selected graph edges. Holmsen and Lee (first arXiv version March 25, 2020) proved general field-homological Leray bounds and link vanishing for arbitrary underlying graphs, but the inspected statements do not specify the ranks or homotopy types here. Nearby indexed computations of Petersen matching, two-matching, higher-independence, cut and Morse complexes use distinct face rules: ordinary matching requires selected edges pairwise disjoint, a degree-two matching complex bounds vertex degrees, and the higher-independence complex selects graph vertices rather than graph edges. No comparable complete matching-threshold homotopy classification was identified in the examined sources, though priority is not certain.

## Limitations

The classification is for one fifteen-edge graph and integer thresholds only. It neither determines an equivariant homotopy splitting nor extends to general cubic graphs. Exact integral homology and homotopy are established by exhaustive finite constructions and standard topology, with two reproducible programs; neither a machine computation by itself nor a literature search proves historical novelty. A graph-specific stronger theorem or unindexed table not found in the searched records may cover part of the statement. Independent validation has not been performed.

## References

- S. Linusson, J. Shareshian, V. Welker, *Complexes of graphs with bounded matching size*, initial public arXiv submission `math/0410345v1`, October 15, 2004; Journal of Algebraic Combinatorics 27 (2008), 331–349. https://arxiv.org/abs/math/0410345
- A. F. Holmsen, S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, initial public arXiv submission `2003.11270v1`, March 25, 2020; Journal of Combinatorial Theory, Series A (2022). https://arxiv.org/abs/2003.11270
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
- J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer (2008), chapter 24 (complexes avoiding matchings).
