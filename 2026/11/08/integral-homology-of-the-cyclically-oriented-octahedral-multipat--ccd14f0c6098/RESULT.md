# Integral homology of the cyclically oriented octahedral multipath complex

## Finding

Let \(D\) be the cyclic orientation of the complete tripartite graph with three parts of size two and all edges between consecutive parts in the directed cycle. Then the directed-linear-forest (multipath) complex \(X\) is simply connected, and
\[
H_j(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0,2,\\
\mathbb Z^4,&j=3,4,\\
0,&\text{otherwise}.
\end{cases}
\]
Its integral cellular model arising from an explicit acyclic Morse matching has one 0-cell, one 2-cell, four 3-cells, and four 4-cells, with all integral differentials zero. In particular the homology has no torsion. The result does **not** identify the full homotopy type as a wedge or determine attaching maps beyond their cellular degrees.

## Assumptions and scope

The six labeled vertices are \(\{0,1,2,3,4,5\}\), partitioned into \(A=\{0,1\}\), \(B=\{2,3\}\), and \(C=\{4,5\}\). The arc set consists of \(A\times B\), \(B\times C\), and \(C\times A\), exactly twelve directed edges. A subset of arcs is admissible if every vertex has at most one selected incoming and at most one selected outgoing arc, and the selected directed subgraph has no directed cycle. Isolated vertices are permitted. The abstract simplicial complex \(X\) has these admissible edge-subsets as faces. All homology groups are ordinary integral homology of its geometric realization. The claim is for this particular first nontrivial complete cyclic tripartite blow-up, not for arbitrary part sizes or cycle lengths.

## Proof

**1. Exhaustive face criterion.** Label the twelve arcs by indices \(0\) through \(11\) in lexicographic order by part-transition, starting vertex, and ending vertex: first the four arcs from \(A\) to \(B\), then four from \(B\) to \(C\), then four from \(C\) to \(A\). Represent each possible face by its twelve-bit mask. A mask is a face exactly when its selected sources and targets are respectively pairwise distinct and its partial vertex-successor function has no cycle. The standalone verifier tests this iff-condition for every one of the \(2^{12}\) masks, including the empty mask. Exactly \(279\) masks qualify, with face vector \((12,54,104,84,24)\) in dimensions \(0\) through \(4\); together with the empty mask, the count is \(279\).

**2. Acyclic matching.** On nonempty faces, process the arc-index pivots in the following order: \(1,9,8,5,10,2,3,7,4,0,11,6\). At a given pivot, pair every as-yet-unpaired face lacking that arc with the face obtained by inserting the arc, whenever both are still unpaired. These are cover relations in the face poset. There are exactly \(134\) pairs. The ten unpaired faces have dimensions \(0,2,3,3,3,3,4,4,4,4\). To verify acyclicity independently of the pivot-rule reasoning, orient each unmatched face incidence downward and each matched incidence upward. The verifier constructs all \(876\) nonempty-face Hasse incidences and processes the resulting directed graph by topological sort; all \(278\) nonempty faces are reached. Hence the matching is acyclic.

**3. Exact integral Morse boundary.** For each oriented simplex in increasing arc-index order, the ordinary signed boundary is the alternating sum over the deletion of one arc. Perform algebraic Morse cancellation on each matched incidence using its coefficient \(\pm1\). At each stage choose a matched pair whose current pivot remains an integral unit; update every other boundary column by subtracting the corresponding multiple of the canceled column. The verifier constructs and simplifies actual integer dictionaries for all boundary coefficients, not just their reductions modulo primes. All \(134\) pairs cancel by integral units and every surviving boundary column is exactly zero. Thus the Morse chain complex consists of \(\mathbb Z\) in degrees \(0\) and \(2\), \(\mathbb Z^4\) in degrees \(3\) and \(4\), and zero otherwise, with zero differentials. Because each cancellation is an integral chain equivalence, this computes the full integral homology, including the absence of torsion.

**4. Fundamental group.** Discrete Morse theory also gives a homotopy-equivalent CW complex with the critical-cell numbers just listed. It has one vertex and no one-cells, so its fundamental group is trivial. This proves the simply-connected statement; it does not force the unspecified higher attaching maps to be null-homotopic.

## Verification

Run `python3 verify.py` in a Python 3 environment. No third-party dependencies are needed. The verifier regenerates all \(279\) masks, validates the \(134\)-pair matching against the entire \(876\)-incidence face-poset graph, performs complete topological sorting, carries out signed integral algebraic Morse elimination, and checks the zero final differential. Its recorded output is in `verification.txt`; the decisive line is `ALL_VERIFY_OK`. The finite exhaustive computation **is** a complete proof for the specified finite digraph; no extrapolation to larger graphs is used.

## Relationship to prior work

Deshpande and Sawant (arXiv:2602.14936v1, 16 February 2026) define directed linear forest complexes and their conflict hypergraphs. Their Section 6, Problem 6.3 asks for homology or homotopy descriptions for broader directed graph classes, especially in the presence of directed cycles. Their paper does not give the present cyclic complete-tripartite integral calculation. Caputi, Collari, Di Trani, and Smith (arXiv:2208.04656v1, 9 August 2022) study the same complex under the name of multipath complex, evaluating linear graphs, polygons, certain grids, and transitive tournaments, and Euler characteristics of other orientations. The present strongly connected, cyclically oriented octahedral graph is outside those treated graph families. For contrast, if directed-cycle exclusions were discarded while retaining the in/out-degree constraints, the complex would be the join of three copies of the matching complex of \(K_{2,2}\), which is homotopy equivalent to \(S^2\). The actual feedback orientation produces additional nonzero integral homology in two higher consecutive dimensions.

## Limitations

This is a finite, exactly specified graph result. It does not classify other cyclic blow-up widths, all octahedral orientations, integral equivariant actions, cup products, higher homotopy groups, or the full attaching maps of the Morse CW structure. A vanishing Morse cellular differential does not by itself certify that the space is a wedge of spheres. The result is supported by a complete computational certificate rather than a shorter conceptual collapse formula. Independent mathematical review is not claimed.

## References

1. P. Deshpande and R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936v1 (16 February 2026), especially Sections 2, 5, and Problem 6.3; https://arxiv.org/html/2602.14936v1.
2. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (9 August 2022); https://arxiv.org/pdf/2208.04656.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (standard acyclic-matching theorem).
