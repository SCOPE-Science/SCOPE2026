# Single-edge faults preserve the \(2\)-torsion of the dodecahedral perfect-matching complex

## Finding

Let \(D=\operatorname{GP}(10,2)\) be the twenty-vertex dodecahedral graph. For a graph \(G\) admitting a perfect matching, let \(\mathcal P(G)\) be the simplicial complex whose vertices are the edges of \(G\) and whose faces are precisely the edge subsets extendible to a perfect matching of \(G\). For **every** graph edge \(e\) of \(D\), there is an integral homotopy equivalence

\[
\boxed{\mathcal P(D-e)\simeq M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^{4}S^3,}
\]

where \(M(\mathbb Z/2\mathbb Z,2)=S^2\cup_{\!2}e^3\) is the Moore space with degree-two three-cell attachment. Moreover, inclusion into the intact complex induces an **isomorphism**

\[
\boxed{\widetilde H_2(\mathcal P(D-e);\mathbb Z)\ \xrightarrow{\ \cong\ }\ \widetilde H_2(\mathcal P(D);\mathbb Z)\cong\mathbb Z/2\mathbb Z.}
\]

The known intact homotopy type is \(M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^{20}S^3\); the new claim shows that every single-edge fault retains its integral two-torsion, although the free third-homology rank decreases from twenty to four. The statement concerns the perfect-matching-extendibility complex, **not** the ordinary matching complex.

## Assumptions and scope

All graphs are simple, finite, and undirected. The dodecahedral graph has vertices \(u_0,\ldots,u_9,v_0,\ldots,v_9\), with subscripts modulo ten. Its edges are \(u_i u_{i+1}\) (outer), \(u_i v_i\) (spoke), and \(v_i v_{i+2}\) (inner), for every \(0\le i<10\). A perfect matching consists of ten pairwise vertex-disjoint graph edges covering all twenty graph vertices. A simplex of \(\mathcal P(G)\) is any subset of such a matching, including the empty simplex.

Cyclic rotation \(u_i\mapsto u_{i+1}\), \(v_i\mapsto v_{i+1}\) is a graph automorphism and acts transitively on each of the three listed edge types. Therefore it suffices to verify an outer edge, one spoke and an inner edge. In lexicographic sorted endpoint-pair edge order (using \(u_i=i\) and \(v_i=10+i\)), these have zero-based indices \(0,2,20\), respectively.

The source framework was publicly available on 2022-09-06, as documented by the first arXiv submission of Bayer–Jelić Milutinović–Vega. The present statement asserts no larger graph-family classification, no multiedge-fault result and no assertion about the maps on third homology.

## Proof

**1. Exhaustive finite face classification.** The independently reproduced least-uncovered-vertex perfect-matching recursion enumerates all thirty-six perfect matchings of \(D\). Each graph edge lies in exactly twelve; deleting any one leaves twenty-four matchings. Taking all subsets of the latter and deduplicating yields exactly \(20,977\) nonempty simplices, with face counts by cardinality

\[
(29,334,1678,4076,5660,4976,2880,1080,240,24).
\]

Each face is included by construction if and only if it extends to one of these twenty-four perfect matchings. The supplied verifier independently recomputes the thirty-six initial matchings by subset dynamic programming as well as the direct recursion, so exhaustiveness is not inferred from a single partial search.

**2. Explicit acyclic Morse matchings.** Encode a face by the thirty-bit mask of its sorted graph-edge coordinates. For each coordinate in increasing order, take every still-unpaired face not containing that coordinate and match it with the face obtained by adding the coordinate, if the latter is still unpaired; remove matched pairs before continuing. In the order of outer, spoke and inner fault representatives, this gives respectively \(10,482\), \(10,481\), and \(10,479\) face–coface pairs. Every representative has exactly \(111,362\) nonempty Hasse cover incidences. Orient matched covers upward and all other covers downward. Exhaustive topological sorting reaches all \(20,977\) faces in each case, proving that the matchings are acyclic (not merely pairwise disjoint). Forman's discrete Morse theorem gives one critical zero-cell, no one-cells, and respectively \((4,8)\), \((5,9)\), and \((7,11)\) critical cells in dimensions two and three.

**3. Integral attaching maps.** Recursively eliminate each matched lower/upper cellular pair using its simplicial incidence coefficient \(\pm1\). The acyclic gradient ensures termination. The resulting exact signed Morse boundaries from critical three-cells to critical two-cells have dimensions \(4\times8\), \(5\times9\), and \(7\times11\). Exact integer Smith reductions give the nonzero diagonals

\[
(1,1,1,2),\qquad(1,1,1,1,2),\qquad(1,1,1,1,1,1,2),
\]

respectively. The full signed matrices and critical cell masks are reconstructed in `verify_dodeca_fault.py` and displayed in `MORSE_CERTIFICATE.json`. All matrix entries arise from enumerated signed simplicial incidences, not numerical approximations. Thus every fault complex has \(\widetilde H_2\cong\mathbb Z/2\mathbb Z\), \(\widetilde H_3\cong\mathbb Z^4\), and no other reduced integral homology. More strongly, the Morse CW complexes have only one zero-cell and cells in dimensions two and three. Their two-skeleta are wedges of two-spheres; the degree matrix records the entire three-cell attaching homotopy classes because \(\pi_2(\bigvee S^2)\cong\bigoplus\mathbb Z\). Unimodular changes of basis and cellular handle slides therefore cancel all the unit pairs, leaving one degree-two three-cell and four trivially attached three-cells. This proves the claimed **homotopy** equivalence, rather than only homology.

**4. Persistence of the torsion generator.** For each representative fault, the verifier finds a nonzero degree-two class over \(\mathbb F_2\) in the small Morse chain complex. It lifts that class by the acyclic matching to an explicit sum of **eight** original oriented triangles modulo two, checks its full simplicial boundary vanishes, and checks that its Morse projection is the chosen nonzero class. Regard the same cycle as a two-chain in the intact complex. Independently, row-reducing the **original** intact simplicial three-boundary gives rank \(1,833\) over \(\mathbb F_2\); the lifted cycle does not lie in its image, for each of the three edge representatives. Hence each fault inclusion is nonzero on second homology over \(\mathbb F_2\). By the integral Smith calculations for both the fault complex and the intact complex, their integral second homology groups are both \(\mathbb Z/2\mathbb Z\); the universal coefficient theorem and vanishing of first homology identify their mod-two second homology with their integral torsion classes. Therefore each inclusion induces the asserted isomorphism on integral second homology. The rotational symmetry handles all remaining edges.

## Verification

Run `python3 verify_dodeca_fault.py` with Python 3.9 or later and SymPy available. The script enumerates graph matchings and simplices from scratch; constructs all three discrete Morse matchings; tests acyclicity on the **complete** oriented Hasse diagrams; computes signed integral Morse matrices and their exact Smith factors; reconstructs torsion-generating mod-two cycles; and tests these cycles against the original intact boundary space. The complete expected execution is `VERIFIER_OUTPUT.txt`; `MORSE_CERTIFICATE.json` records the matrices, critical masks and cycle representatives. The final line is `DODECA_SINGLE_EDGE_FAULT_CERTIFICATE_PASS`. The script's source is the certificate, rather than an unexplained recorded log.

For the three graph-edge orbit representatives the certificate verifies all claims separately, rather than relying on numerical similarity or assuming three distinct orbit types have identical reductions. The reduction uses the exact integral coefficient ring; mod-two arithmetic is used only to verify the induced map on the order-two class.

## Relationship to prior work

Bayer, Jelić Milutinović and Vega defined perfect-matching complexes and studied selected honeycomb graphs; their 2022 preprint does not compute this dodecahedral fault. Chandrakar and Singh treated polygonal line tilings and two-row grids; neither is the graph at issue. An earlier exact dodecahedral result identifies \(\mathcal P(D)\simeq M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^{20}S^3\), but that calculation concerns the intact graph and **does not imply** a homotopy type for \(\mathcal P(D-e)\) or the induced torsion map. Known ordinary matching-complex edge-deletion results refer to the larger complex of all matchings rather than perfect-extendible matchings. The new contribution is the *fault-uniform* Moore-space decomposition and nonvanishing integral torsion inclusion.

## Limitations

This is a finite, complete, reproducible combinatorial certificate for one graph and every one of its edges, not a conceptual theorem for arbitrary fullerenes or cubic graphs. The assertion that torsion survives is in integral second homology; the maps on free third homology and any equivariant homotopy properties were not determined. Search and source comparisons do not exclude unindexed equivalent work; the priority statement is limited to sources actually inspected. No independent scientific audit has been performed.

## References

1. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803, first submitted **2022-09-06**, https://arxiv.org/abs/2209.02803.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first submitted **2024-07-08**, https://arxiv.org/abs/2407.05809.
3. *Order-two torsion and a Moore-space decomposition for the dodecahedral perfect-matching complex*, published mathematical record, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-order-two-torsion-and-a-moore-space-decomposition-for-the-dodeca--2c09902bba79.
4. *A Moore-space summand in the dodecahedral perfect-matching complex*, published mathematical record, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-moore-space-summand-in-the-dodecahedral-perfect-matching-compl--efd05431d7b5.
