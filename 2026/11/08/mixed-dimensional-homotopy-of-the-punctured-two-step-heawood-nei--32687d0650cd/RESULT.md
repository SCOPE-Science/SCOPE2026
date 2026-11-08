# Mixed-dimensional homotopy of the punctured two-step Heawood neighborhood complex

## Finding
Let \(H\) be the point-line incidence graph of the Fano plane, with fourteen vertices. Define the **punctured two-step distance-neighborhood complex** \(K\) by declaring a nonempty subset \(\sigma\subseteq V(H)\) to be a face exactly when some \(v\in V(H)\) satisfies \(d_H(v,u)\in\{1,2\}\) for every \(u\in\sigma\). Then
\[
K\simeq\bigvee^{29}S^4\vee\bigvee^{2}S^5.
\]
Equivalently, this is the ordinary open Lovász neighborhood complex of the **square graph** \(H^2\), whose edges join distinct vertices of \(H\) at distance one or two; \(H^2\) consists of two seven-vertex cliques joined by the original Fano-incidence edges. This is an integral homotopy equivalence, not merely a field-homology calculation. In particular, \(\widetilde H_4(K;\mathbb Z)\cong\mathbb Z^{29}\), \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^2\), and all other reduced integral homology vanishes. The complex is pure eight-dimensional but not shellable.

## Assumptions and scope
The point and line sets are separate copies of \(\{1,2,\ldots,7\}\), encoding nonzero three-bit vectors. A point \(a\) and a line \(b\) are adjacent precisely when the bitwise dot product of \(a\) and \(b\) is zero over \(\mathbb F_2\). Vertex indices \(0,\ldots,6\) encode points \(1,\ldots,7\), while \(7,\ldots,13\) encode lines \(1,\ldots,7\). Distances are shortest-path graph distances. The fourteen generating facets of \(K\) have vertex sets \(\{u:d_H(v,u)\in\{1,2\}\}\), each of size nine. No claim is made for arbitrary cubic graphs or projective planes of other orders.

## Proof
**Step 1: Finite simplicial model.** The explicit incidence prescription gives twenty-one graph edges. Each vertex has one distance-zero vertex, three at distance one, six at distance two and four at distance three. The fourteen nine-element facet sets yield exactly \(4480\) nonempty faces, with face numbers in dimensions zero through eight
\[
(14,91,364,903,1358,1106,504,126,14).
\]
All faces are enumerated as nonzero fourteen-bit masks contained in at least one generating facet.

**Step 2: A reproducible acyclic matching.** On the remaining nonempty face poset, maintain the set of immediate surviving cofaces of each face. Whenever a face has exactly one immediate coface, choose the numerically least such face and match/remove it together with that coface. If no such face exists, remove as critical the maximal-dimensional remaining simplex, breaking ties by numerically least bit mask. Repeat until empty. Every removal is either a free elementary-collapse pair or the removal of a maximal critical face. This produces exactly \(2224\) matched pairs and critical cells consisting of one vertex, twenty-nine four-cells and two five-cells; no other cells remain. As a separate check, orient every Hasse edge toward the lower-dimensional face except along the matched edges, which are reversed. A complete topological sort of all \(4480\) face nodes and \(22974\) covering relations succeeds. Therefore the matching is acyclic, and discrete Morse theory provides a CW model having precisely those critical cells.

**Step 3: Integral attaching map calculation.** Give every simplex its increasing-vertex orientation. For an upper simplex \(\tau\) and codimension-one face \(\rho\), let \([\tau:\rho]\in\{+1,-1\}\) be the ordinary signed incidence. Eliminate each matched lower four-face \(\sigma\) paired with an upper five-face \(\tau\) by substituting
\[
\sigma\longmapsto
-\sum_{\substack{\rho\subset\tau\\|\rho|=5,\ \rho\ne\sigma}}
\frac{[\tau:\rho]}{[\tau:\sigma]}\,\rho.
\]
A noncritical four-cell paired as an upper face with a three-cell contributes zero. Because the matching is acyclic, these substitutions terminate and compute the integral discrete-Morse boundary. The two critical five-cells have bit masks \(\texttt{0x297}\) and \(\texttt{0x1f80}\). Exact signed substitution gives the **zero** coefficient at each of the twenty-nine critical four-cells for both five-cells. Thus the integer Morse boundary \(C_5^{\mathrm M}\to C_4^{\mathrm M}\) is the zero \(29\times2\) matrix. This conclusion is proved by integer arithmetic, not inferred from ranks modulo a prime.

**Step 4: Homotopy, not only homology.** The critical zero-cell and twenty-nine critical four-cells form a CW wedge of twenty-nine four-spheres; there are no one-, two- or three-cells. Each remaining five-cell is attached by a map from \(S^4\) into that wedge. By the Hurewicz isomorphism in degree four, its homotopy class is determined by the vector of integral attaching degrees. Step 3 shows this vector is zero for each cell. Therefore both attaching maps are null-homotopic and the asserted wedge decomposition follows. Since the original complex is pure of dimension eight while reduced homology occurs in dimensions four and five, the standard consequence of pure shellability rules out shellability.

## Verification
Run `python3 verify.py` using Python 3.10 or later. It reconstructs the incidence graph, distances, facet masks, all faces, matching, full oriented Hasse graph and integer Morse boundary directly from this statement. It independently computes mod-two simplicial boundary ranks as a supplementary check. The expected full output is `verification_output.txt`. The final identifier line is `HEAWOOD_PUNCTURED_TWO_STEP_NEIGHBORHOOD_PASS`. This program uses only the Python standard library.

## Relationship to prior work
Lovász's ordinary neighborhood complex of \(H\) uses exactly distance one, while the present complex is \(\mathcal N(H^2)\), the ordinary neighborhood complex of the square graph, equivalently the generalized distance set \(D=\{1,2\}\) on \(H\). Previte's 2014 dissertation introduced generalized \(D\)-neighborhood complexes and computed examples including Petersen and Platonic graphs, but does not determine the homotopy type for this Fano incidence graph at \(D=\{1,2\}\). Shukla's work on graphs of maximum degree at most three concerns the ordinary distance-one neighborhood complex; its theorem does not cover the two-step complex. The previously available projective-plane incidence-graph results for the ordinary neighborhood and the scale-two Vietoris–Rips complexes concern different face relations and do not imply the mixed-dimensional wedge here. The result is limited to this explicitly specified distance set and graph.

## Limitations
There is no classification here of all nonempty distance subsets, the automorphism representation on the two integral homology groups, the inclusions between neighborhood scales, or other projective-plane orders. The certificate verifies a finite graph and a finite acyclic matching and uses the standard discrete-Morse homotopy theorem. Equivalent unindexed literature may exist; publication priority is not certified. No independent mathematical audit has been performed.

## References
1. C. Previte, *The D-neighborhood complex of a graph*, Colorado State University dissertation, Summer 2014; https://hdl.handle.net/10217/83806 .
2. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, submitted December 4, 2005; https://arxiv.org/abs/math/0512077 .
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, submitted February 13, 2018; https://arxiv.org/abs/1802.04526 .
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145; https://doi.org/10.1006/aima.1997.1650 .
