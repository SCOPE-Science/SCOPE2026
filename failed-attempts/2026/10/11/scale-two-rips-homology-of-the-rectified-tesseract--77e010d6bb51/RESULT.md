# Scale-two Rips homology of the rectified tesseract
## Finding
Let \(R=L(Q_4)\) be the line graph of the four-dimensional hypercube graph, equipped with its shortest-path metric, and let \(K=\mathrm{VR}_{\le 2}(R)\). Then \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^8\), and all other reduced integral homology groups vanish. In particular, the scale-two Rips complex of the rectified tesseract has genuinely mixed-dimensional homology and cannot be homotopy equivalent to a wedge of spheres all in one dimension.

The graph \(R\) has \(32\) vertices and is the one-skeleton of the rectified tesseract: its vertices are the edges of the four-cube, and two are adjacent exactly when the corresponding cube edges share an endpoint. For the inclusive scale-two Rips complex \(K\), exhaustive face enumeration gives
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)=(32,336,1568,3672,4512,2848,832,96).
\]

## Assumptions and scope
The four-cube graph has vertex set \(\{0,1\}^4\), with edges joining binary strings at Hamming distance one. The line graph \(R=L(Q_4)\) has one vertex for each of the \(32\) cube edges. Its metric is the unweighted shortest-path metric. The notation \(\mathrm{VR}_{\le 2}(R)\) means the abstract simplicial complex whose nonempty faces are the finite subsets of \(V(R)\) having pairwise graph distance at most \(2\).

The claim concerns integral homology. It does not assert a complete homotopy decomposition.

## Proof
The verifier in `artifacts/verify.py` constructs the \(32\) cube edges canonically, builds their line graph, computes all-pairs shortest-path distances, and then enumerates every clique in the distance-at-most-two graph. This produces exactly \(13{,}896\) nonempty faces and the face vector displayed above.

A repeated-vertex matching is then applied to the face poset. The verifier checks every one of the \(66{,}304\) Hasse covers and reverses exactly the matched covers. A topological sort visits all \(13{,}896\) faces, so the reversed Hasse diagram is acyclic. The matching contains \(6{,}943\) pairs and leaves exactly one critical \(0\)-cell, one critical \(3\)-cell, and eight critical \(5\)-cells.

By discrete Morse theory, \(K\) is homotopy equivalent to a CW complex with precisely those critical cells. Its cellular chain groups are therefore nonzero only in dimensions \(0\), \(3\), and \(5\). Every cellular differential is zero because there are no critical cells in adjacent dimensions. Hence
\[
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z,\qquad
\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^8,
\]
and all other reduced integral homology groups vanish.

## Verification
Run `python3 artifacts/verify.py`. The packaged output in `artifacts/verify_output.txt` records `VERIFY_OK`. In addition to the Morse certificate, the verifier independently forms the full simplicial boundary matrices over \(\mathbb F_2\). Their ranks in dimensions \(1\) through \(7\) are
\[
(31,305,1263,2408,2104,736,96),
\]
which gives reduced mod-two Betti ranks \(1\) in degree \(3\), \(8\) in degree \(5\), and zero elsewhere. The reduced Euler characteristic from the face vector is \(-9\), agreeing with the integral homology calculation.

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine graph-metric Vietoris--Rips homotopy types for the five Platonic solids and explicitly point toward extensions beyond that class. Their paper, first public as arXiv:2302.14388v1 on 2023-02-28, has primary MSC 55N31 and provides the middle-window literature anchor for this calculation. It does not treat the four-dimensional rectified tesseract.

Adamaszek and Adams prove that \(\mathrm{VR}_{\le 2}(Q_n)\) is a wedge of \(3\)-spheres for every hypercube graph \(Q_n\). For \(Q_4\) itself their formula gives a single-dimensional degree-\(3\) homology pattern, whereas passing to the line graph changes the vertex set from cube vertices to cube edges and changes the graph metric. Thus their theorem does not imply the mixed degree-\(3\) and degree-\(5\) homology above. Exact searches also used the aliases “rectified 8-cell,” “rectified tesseract,” “runcic tesseract,” and “line graph of the four-cube,” as well as the equivalent clique-complex formulation for the square of the line graph; no statement implying this exact integral homology was located.

## Limitations
The Morse CW model has cells in dimensions \(0\), \(3\), and \(5\), but the calculation does not determine the attaching maps of the \(5\)-cells into the \(3\)-skeleton. Consequently no claim is made that \(K\) is homotopy equivalent to \(S^3\vee\bigvee^8 S^5\). A residual originality risk is an unindexed computation under a less common polytope or graph-power alias.

## References
1. Nada Saleh, Thomas Titz Mite, and Stefan Witzel, *Vietoris--Rips complexes of Platonic solids*, arXiv:2302.14388v1, 2023.
2. Michał Adamaszek and Henry Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040, 2021.
