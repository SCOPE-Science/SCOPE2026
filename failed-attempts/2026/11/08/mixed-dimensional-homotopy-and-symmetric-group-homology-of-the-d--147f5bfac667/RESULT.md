# Mixed-dimensional homotopy and symmetric-group homology of the Desargues nonincidence neighborhood complex

## Finding
Let \(B\) be the point–line **nonincidence** graph of the Desargues \(10_3\) configuration. Then its ordinary open-neighborhood complex is the disjoint union of two copies of
\[
X\simeq S^3\vee\bigvee^{5}S^4.
\]
On each copy, the canonical action of \(S_5\) on rational reduced homology is
\[
\widetilde H_3(X;\mathbb Q)\cong\operatorname{sgn},\qquad
\widetilde H_4(X;\mathbb Q)\cong\mathbb Q^5,
\]
where \(\mathbb Q^5\) is the natural permutation module on five letters. In particular, the integral homology is torsion-free with one generator in degree three and five in degree four per component.

## Assumptions and scope
Set \([5]=\{0,1,2,3,4\}\). Write \(P=\binom{[5]}2\) for the ten configuration points and \(L=\binom{[5]}3\) for the ten lines. Declare \(p\in P\) incident with \(\ell\in L\) if \(p\subseteq\ell\). The graph \(B\) has vertex classes \(P,L\), with \(p\sim\ell\) if and only if \(p\not\subseteq\ell\). This is a 70-edge, seven-regular, bipartite graph; it is the **bipartite complement of**, not the same graph as, the familiar 30-edge cubic Desargues incidence graph.

For any simple graph \(G\), its ordinary open-neighborhood complex \(\mathcal N(G)\) consists of the nonempty vertex subsets with a common neighboring vertex, together with the empty face. Because \(B\) is bipartite, no nonempty face mixes points and lines. Its two components are isomorphic via the point–line complementation \(\ell\mapsto[5]\setminus\ell\). Let \(X\) denote the point component. It has ten vertices and ten facets
\[
F_{\ell}=\{p\in P:p\not\subseteq\ell\}\qquad(\ell\in L),
\]
each of size seven. Equivalently, \(X\) is the noncover complex of the ten triples of edges forming the triangles of the complete graph on five labeled vertices; it is the Alexander dual of the complex of triangle-free graphs on these vertices. These equivalent descriptions are for deduplication and do not equate this complex to an independence or Čech complex of the cubic Desargues graph.

## Proof
Enumerate the ten points in lexicographic order and encode each nonempty point subset by a ten-bit mask. The ten forbidden triangle-edge masks \(T_{\ell}\) consist of the three two-subsets contained in each \(\ell\). A nonempty mask \(s\) belongs to \(X\) precisely when \(s\cap T_{\ell}=\varnothing\) for at least one \(\ell\). Direct enumeration gives 635 nonempty faces, with face vector by dimensions zero through six
\[
(10,45,120,200,180,70,10).
\]
This enumeration is independently reproduced by forming all subfaces of the ten masks \(F_{\ell}\).

Use a lexicographic vertex-toggle matching: for each point vertex \(v\), in order, pair every still-unmatched face \(a\) omitting \(v\) with \(a\cup\{v\}\) whenever both are still unmatched. This produces 314 matched pairs and exactly seven critical faces: one vertex, one three-simplex and five four-simplices. Form the directed Hasse graph by reversing its matched covering arrows. A complete topological sort of its 635 nodes and 2,640 incidences succeeds, proving acyclicity. The same conclusions follow for the reverse point order, independently establishing the critical dimensions.

The cellular Morse differential from the five critical four-cells to the critical three-cell is calculated integrally by eliminating each matched pair via its signed simplicial incidence \(\pm1\). All five coefficients are exactly zero. The Morse model is therefore a CW complex with one vertex, one three-cell and five four-cells attached by degree-zero maps to its three-sphere. Since \(\pi_3(S^3)\cong\mathbb Z\) and degree completely classifies these attaching maps, each attachment is null-homotopic; the asserted integral homotopy wedge follows. The computation does not infer homotopy equivalence merely from Betti numbers.

For the action, an element \(\sigma\in S_5\) sends \(\{a,b\}\) to \(\{\sigma(a),\sigma(b)\}\), and hence acts simplicially on \(X\). A primitive integral three-cycle is constructed from the single critical three-cell by canceling all paired two-dimensional boundary incidences. It has eight oriented facets, vanishing boundary, and evaluates to one under the integral Morse-projection cocycle. Exact transport of this cycle under all 120 permutations yields multiplication by \(\operatorname{sgn}(\sigma)\) on integral third homology.

The signed fixed-face Lefschetz trace is computed for every permutation on every simplex. Subtracting the degree-zero trace gives \(\widetilde L(\sigma)=-\chi_3(\sigma)+\chi_4(\sigma)\). Substituting the established sign character, the resulting values \(\chi_4(\sigma)\) equal exactly the number of fixed letters of \(\sigma\). Over the rationals, characters determine finite-group representations, giving the five-letter permutation representation. On cycle types \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), the characters \((\chi_3,\chi_4)\) are respectively \((1,5),(-1,3),(1,1),(1,2),(-1,0),(-1,1),(1,0)\).

## Verification
Run the included standard-library program `desargues_verify.py` with Python 3. It checks two independent membership criteria over all 1,023 nonempty vertex subsets, two complete Morse matchings, exhaustive directed acyclicity, integral Morse differential, an integral eight-facet primitive generator and cocycle, all 120 symmetry actions, and independently formed mod-two boundary matrices. Boundary ranks from dimensions one through six are \((9,36,84,115,60,10)\). The program exits only after every assertion succeeds; its recorded output is included in `desargues_verification_output.txt`.

## Relationship to prior work
Tsukuda establishes general Alexander-dual and incidence-graph relationships; Kim and Kim introduce and analyze noncover complexes and related bounds. Their inspected results do not supply the explicit Desargues nonincidence neighborhood homotopy or its \(S_5\)-homology characters. The exact published-finding corpus record for the nonincidence graph of the projective plane of order three studies a different 13-point, 13-line incidence geometry. Results for the cubic Desargues graph's independence or matching complexes and its scale-three Čech nerve also concern different simplicial complexes. Linusson–Shareshian's published abstract addresses the complex of graphs of chromatic number at most \(t\), which is not the same as the complex of five-vertex triangle-free graphs.

## Limitations
This is a finite exact-computation proof for the specified graph, not a theorem for all symmetric \(10_3\) configurations or general nonincidence geometries. The representation statement is rational; no canonical equivariant sphere-wedge equivalence or complete integral equivariant lattice is claimed. Bibliographic novelty is supported by named searches and inspected primary sources, not by exhaustive coverage of every unindexed or inaccessible monograph; some relevant older graph-complex articles were accessible only through abstracts.

## References
1. Shuichi Tsukuda, “Independence complexes and incidence graphs,” *Contributions to Discrete Mathematics* 12 (2017), doi:10.55016/ojs/cdm.v12i1.62277, first public evidence September 27, 2017.
2. J. Kim and S. Kim, “Domination numbers and noncover complexes of hypergraphs,” arXiv:2101.01850 (first publicly posted January 6, 2021); subsequently *Journal of Combinatorial Theory A*, doi:10.1016/j.jcta.2021.105408.
3. S. Linusson and J. Shareshian, “Complexes of t-Colorable Graphs,” *SIAM Journal on Discrete Mathematics* 16 (2003), doi:10.1137/S0895480100366968. Different monotone graph property; abstract inspected, full text not established to be available.
