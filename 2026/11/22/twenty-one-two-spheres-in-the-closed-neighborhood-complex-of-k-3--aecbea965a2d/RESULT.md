# Twenty-one two-spheres in the closed-neighborhood complex of \(K_3\square C_4\)

## Finding
Let \(G=K_3\square C_4\) be the Cartesian product of the triangle and the unfilled four-cycle. For a graph vertex \(v\), let \(N[v]\) be its closed graph neighborhood, and define \(\mathcal N[G]\) to contain every subset of some \(N[v]\). Then
\[
\boxed{|\mathcal N[K_3\square C_4]|\simeq\bigvee^{21}S^2.}
\]
This is an integral homotopy equivalence. In particular \(\pi_1\) is trivial, \(\widetilde H_2(-;\mathbb Z)\cong\mathbb Z^{21}\), and all other reduced integral homology groups vanish. The complex is four-dimensional and has face vector \((12,54,112,60,12)\). It admits an acyclic simplicial discrete-Morse matching with exactly one critical vertex, twenty-one critical triangles and no other critical cells.

## Assumptions and scope
Vertices are \(v_{i,a}\), where \(i\in\{0,1,2,3\}\) is reduced modulo four and \(a\in\{0,1,2\}\). Distinct vertices are adjacent if their cycle indices agree and their triangle labels differ, or their triangle labels agree and their cycle indices differ by one modulo four. Thus each closed neighborhood is the five-element set
\[
F_{i,a}=\{v_{i,0},v_{i,1},v_{i,2},v_{i-1,a},v_{i+1,a}\}.
\]
There are exactly twelve such maximal simplices. The definition uses *closed* neighborhoods and differs from the Lovász *open* neighborhood complex and from a Vietoris–Rips complex. The result is the short-cycle boundary case of the vertex-centered graph Čech construction at scale two. The graph and its parameters are fixed; no assertion for other clique widths or cycle lengths is included in the new theorem.

## Proof
**1. Exhaustive facet-to-face reconstruction.** Label \(v_{i,a}\) by \(3i+a\). A nonempty simplex is a bit mask \(s\) contained in at least one of the twelve explicitly listed five-vertex masks \(F_{i,a}\). The supplied standalone `verify.py` constructs every nonempty subset of each mask with no reliance on stored face lists. Deduplication produces exactly \(250\) nonempty simplices and the face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(12,54,112,60,12).
\]
The bit-mask representation and full generator code specify a finite, independently executable certificate without omitted cases.

**2. A complete discrete-Morse matching.** Order the twelve vertices by labels \(0,1,\ldots,11\). Starting from the full face set, for each vertex \(j\) match *simultaneously* every still-unmatched nonempty face \(s\) not containing \(j\) to its one-vertex extension \(s\cup\{j\}\), provided both are still unmatched. Remove all faces in that stage's pairs before advancing to \(j+1\). At each stage pairs are disjoint, because toggling a fixed vertex is an involution. Repeating for all twelve vertices gives exactly \(114\) pairs and critical vector
\[
(c_0,c_1,c_2,c_3,c_4)=(1,0,21,0,0).
\]
To establish global acyclicity, orient every codimension-one incidence from the larger face to the smaller, except reverse each matched incidence. On the complete set of \(250\) simplices there are exactly \(744\) such incidence arrows. The verifier constructs *all* these arrows, applies Kahn's exact integer topological sorting algorithm, and confirms it deletes all \(250\) vertices of this directed graph. Therefore the oriented Hasse graph has no cycle, which is the discrete-Morse acyclicity condition. The assertion is a finite exhaustive proof: the generating neighborhoods, matching selection, cover incidences and full cycle test are all explicitly derived rather than inferred from a sample or a log.

For an additional, genuinely independent choice of certificate, the verifier repeats the complete construction with the reverse vertex order and with the color-major order. Each also produces \(114\) pairs, the same critical vector, and a directed acyclic incidence graph. No numerical approximation enters these checks.

**3. Homotopy, not merely homology.** The finite acyclic matching satisfies Forman's discrete-Morse theorem: the geometric realization is homotopy equivalent to a CW complex having one cell for each critical simplex in the corresponding dimension. Here there is one zero-cell, no one-cells, twenty-one two-cells, and no higher cells. Every two-cell therefore attaches by the unique map of its boundary circle into a point. Consequently the Morse CW complex is precisely a wedge of twenty-one two-spheres. This proves the displayed integral homotopy equivalence, including simple connectivity and absence of torsion.

**4. A separate chain calculation.** Without using the Morse matching, the verifier constructs mod-two simplicial boundaries in dimensions one through four. Their exact ranks are respectively \(11,43,48,12\), giving simplicial Betti vector \((1,0,21,0,0)\). This corroborates, but is not substituted for, the stronger integral homotopy argument of Step 3.

## Verification
The complete self-contained Python 3 standard-library checker `verify.py`, accompanied by `verify_output.txt`, reconstructs all twelve maximal neighborhoods, all \(250\) faces, each of the three complete Morse pairings, the exact directed face-incidence graphs (all \(744\) arrows each), and an independent mod-two boundary reduction. It uses explicit assertions and deterministic integer operations. Executing `python3 verify.py` must end in `VERIFY_OK` and reproduce the accompanying output exactly. The calculation is exhaustive for this twelve-vertex graph, not a finite test extrapolated to an infinite family. All input definitions and expected invariants are printed or reconstructible from the code above.

## Relationship to prior work
T. Matsushita [1] introduces closed-neighborhood complexes and relates their fundamental groups to graph fundamental groups; its Cartesian-product example treats products of two complete graphs, not \(K_3\square C_4\). The closely relevant clique-fiber Čech theorem [2] proves, for graphs \(H\) *without* triangles or four-cycles, that \(\mathcal N[H\square K_m]\simeq H\vee\bigvee^{|E(H)|(m-1)^2}S^2\). For \(H=C_n\) and \(m=3\), it gives \(S^1\vee\bigvee^{4n}S^2\) for every \(n\ge5\). The four-cycle has two common neighbors at opposite vertices, invalidating the theorem's key uniqueness hypothesis. In contrast, the exceptional four-cycle case here has *trivial* fundamental group and twenty-one second-homology generators, not the extrapolated circle and sixteen spheres. This is the first excluded cycle length beyond the already separately understood complete-graph case \(n=3\).

The square-completion theorem [3] assumes the *whole graph* is triangle-free, which fails here. The published triangular-cylinder result [4] calculates the *open* neighborhood complex of the same graph family; it does not determine the present closed complex. The full primary mathematical statements of [1]–[4] were compared, rather than relying only on matching or differing titles. The computation is offered as the exact natural missing girth-four boundary case, not as a replacement for or extension of the known theorem at \(n\ge5\).

## Limitations
Only \(K_3\square C_4\) is classified. The equivalence is nonequivariant and does not determine automorphism representations or persistence maps at other scales. The proof depends on the independently regenerable exact finite matching; it does not give an all-parameter geometric collapse for arbitrary clique widths or cycles. Searches and full-text comparisons cannot rule out an unindexed earlier equivalent computation. Independent mathematical validation has not been performed.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, first posted 2025-11-16, arXiv:2511.12608. https://arxiv.org/abs/2511.12608
2. *Clique-fiber Čech nerves over graphs of girth at least five*, publicly accessible mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-clique-fiber-ech-nerves-over-graphs-of-girth-at-least-five--bcf5b8b96c75
3. *Square-completion splitting of closed-neighborhood complexes with codegree at most two*, publicly accessible mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-square-completion-splitting-of-closed-neighborhood-complexes-wit--006bbbe8a937
4. *The triangular-cylinder neighborhood complex: a torus except at length four*, publicly accessible mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-triangular-cylinder-neighborhood-complex-a-torus-except-at-l--3f9179cdd224
