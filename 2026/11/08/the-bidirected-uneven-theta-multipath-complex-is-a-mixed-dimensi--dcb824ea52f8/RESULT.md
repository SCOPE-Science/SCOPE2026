# The bidirected uneven-theta multipath complex is a mixed-dimensional sphere wedge

## Finding
Let \(G=\Theta_{2,2,3}\) have vertices \(0,1,2,3,4,5\) and three internally disjoint paths from \(0\) to \(1\): \(0-2-1\), \(0-3-1\), and \(0-4-5-1\). Replace every undirected edge by both directed arcs, obtaining \(D=\overleftrightarrow{G}\). Let \(X(D)\) be the multipath simplicial complex whose vertices are the fourteen arcs of \(D\) and whose faces are sets of arcs forming disjoint unions of directed simple paths and isolated vertices, with all directed cycles excluded. Then the **integral homotopy type** is
\[
|X(D)|\simeq \left(\bigvee^{5}S^2\right)\vee\left(\bigvee^{6}S^3\right).
\]
In particular, the space is simply connected, with \(\widetilde H_2\cong\mathbb Z^5\), \(\widetilde H_3\cong\mathbb Z^6\), and all other reduced integral homology groups zero.

## Assumptions and scope
All graphs are finite and simple before bidirection. Precisely the seven edges are \(\{0,2\},\{2,1\},\{0,3\},\{3,1\},\{0,4\},\{4,5\},\{5,1\}\). The ordering of the fourteen arcs used in the computation is, in each listed edge's position, its displayed orientation followed by its reversal; thus arc indices run from \(0\) to \(13\). A nonempty arc set is a multipath exactly when every vertex has selected indegree and outdegree at most one and the selected arcs contain no directed cycle. The statement is only about this specific six-vertex, seven-edge graph, not all theta graphs.

## Proof
A face is represented by a nonzero fourteen-bit integer, with bit \(i\) indicating the \(i\)-th directed arc. The stated criterion is necessary for a union of directed simple paths. It is sufficient because every weak component of a finite digraph of indegree and outdegree at most one is a directed path or a directed cycle, and cycles have been excluded. Exhaustively checking all \(2^{14}-1=16383\) nonempty bitmasks against this exact criterion gives \(280\) faces, in dimensions \(0\) through \(4\) with face vector \((14,64,114,76,12)\).

We now give a complete, deterministic acyclic face-poset matching, using the arc-bitmask as the face identifier. Initially mark every nonempty face active. If any active face has exactly one active codimension-one coface, choose the one maximizing the pair *(number of selected arcs, negative bitmask integer)*, match it with its unique coface, and delete both from the active set. Otherwise choose an active maximal face maximizing the same pair, record it as critical, and delete it. Repeat until no active faces remain. All choices, including ties, are completely specified. At each matching step the chosen coface is maximal in the current subcomplex: if it had a further coface, the chosen lower face would have at least two immediate cofaces by downward closure.

The exact full-face-poset certificate (`matching_certificate.json`, independently reproducible by `verify.py`) contains \(134\) face–coface pairs and the following critical counts: one vertex, five \(2\)-simplices, and six \(3\)-simplices, with no other critical faces. For every face–coface incidence in the original poset, direct the Hasse edge downward unless the incidence is matched, in which case reverse it. A complete topological sort visits all \(280\) vertices and all \(834\) incidences. Consequently, the matching is acyclic, so discrete Morse theory supplies a CW model with exactly these critical cells.

The remaining essential check is the **integral** cellular boundary from the six critical \(3\)-cells to the five critical \(2\)-cells. Orient each simplicial face by increasing arc index. Its ordinary signed boundary is the alternating sum of faces obtained by deleting each selected arc in order. The integral Morse projection \(P\) sends a critical cell to itself and an upper matched cell to zero. For a matched lower cell \(a\), with upper partner \(b\) and signed coefficient \(\epsilon=[\partial b:a]\in\{\pm1\}\), recursively set
\[
P(a)=-\epsilon\sum_{c\ne a}[\partial b:c]P(c).
\]
Acyclicity makes this recursion finite. Apply \(P\) to the ordinary boundary of each critical \(3\)-cell. The six resulting columns over \(\mathbb Z\) are **identically zero**, as verified using exact signed integer arithmetic by the included standalone code. This is stronger than a finite-field rank calculation or a homology guess.

The CW model therefore has a point as its \(1\)-skeleton and a wedge of five \(2\)-spheres as its \(2\)-skeleton. A \(3\)-cell attaches by a map from \(S^2\) to this simply connected \(2\)-skeleton. The Hurewicz map from its second homotopy to second integral homology is an isomorphism, so the vanishing attaching-degree column implies the attaching map is nullhomotopic. Each of the six \(3\)-cells consequently supplies an independent \(3\)-sphere, proving the displayed integral homotopy equivalence.

## Verification
Run `python3 verify.py` in the directory containing the embedded files. The standalone script uses only the Python standard library; it rebuilds the directed graph, enumerates all nonempty masks, checks the full face vector, reconstructs all matching pairs, verifies all Hasse orientations are acyclic, computes each signed integral Morse boundary, and independently computes the mod-two Betti numbers from the original full simplicial boundary matrices. It writes the deterministic `matching_certificate.json`. The supplied `verify_output.txt` is the recorded output of an actual successful execution. The full-face calculation is exhaustive **for this finite graph**; no inference to larger graphs is being made.

## Relationship to prior work
Caputi, Collari and Smith (January 9, 2026) computed homology and connectivity for bidirectional polygon multipath complexes and studied bidirectional paths, motivating the examination of the first unequal-arm, branching theta example. Their formulas for paths and single polygons do not classify the present theta complex. Caputi, Collari, Di Trani and Smith (2022) studied oriented paths, polygons, selected small grids and tournaments, not the current bidirected uneven theta. The digraph-without-directed-cycles comparison in Caputi, Collari and Ramos (2024) does not apply to a bidirected graph, which contains opposite-arc directed two-cycles. The exact signed Morse matrix establishes a homotopy classification beyond mere Betti-number enumeration.

## Limitations
This is an explicit finite classification, not an infinite-family theta classification. The proof concerns the full multipath complex of this **bidirected** theta graph, not a matching complex, independence complex, strong discrete-Morse matching complex, or configuration space on the same underlying graph. No equivariant homotopy type, shelling, or claim about subdivisions beyond this graph is established. Originality cannot rule out unindexed equivalent work.

## References
1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (first public version January 9, 2026), https://arxiv.org/abs/2601.05670.
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (August 9, 2022); later published in *Mathematika*, https://arxiv.org/abs/2208.04656.
3. L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1, https://arxiv.org/abs/2401.01248.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
