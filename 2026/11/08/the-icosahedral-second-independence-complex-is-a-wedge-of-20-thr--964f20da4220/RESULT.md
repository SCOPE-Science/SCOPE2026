# The icosahedral second independence complex is a wedge of \(20\) three-spheres

## Finding
Let \(I\) be the graph of the regular icosahedron and \(\operatorname{Ind}_2(I)\) the simplicial complex of vertex subsets whose induced connected components each contain at most two vertices. Then
\[
\operatorname{Ind}_2(I)\simeq\bigvee^{20}S^3.
\]
This is an integral homotopy equivalence, not merely an isomorphism of rational or finite-field homology groups. In particular its only nonzero reduced integral homology is \(\widetilde H_3\cong\mathbb Z^{20}\).

## Assumptions and scope
Vertices are numbered \(0,1,\ldots,11\). Write \(u_i=1+i\) and \(l_i=6+i\), for \(i\in\mathbb Z/5\mathbb Z\). The edges of \(I\) are precisely
\[
\{0,u_i\},\quad \{11,l_i\},\quad \{u_i,u_{i+1}\},\quad
\{l_i,l_{i+1}\},\quad \{u_i,l_i\},\quad \{u_i,l_{i-1}\}
\]
for the five values of \(i\). This describes the standard two-pentagon icosahedral graph with \(12\) vertices and \(30\) edges. All graphs and simplicial complexes here are finite and unweighted; no geometric distance is involved. The empty vertex subset belongs to the abstract simplicial complex but is not a cell in its nonaugmented face poset.

A nonempty vertex subset \(S\) belongs to \(\operatorname{Ind}_2(I)\) if and only if every vertex of \(S\) has at most one neighbor within \(S\). This equivalence holds because a finite graph of maximum degree at most one is a disjoint union of isolated vertices and edges. Such simplices may alternatively be called dissociation sets, and the resulting complex is the first nontrivial forest-filtration stage.

## Proof
**Enumeration and dimension.** Encode a nonempty subset by its \(12\)-bit integer mask. Let \(N(v)\) be the graph neighborhood of \(v\). Include a mask \(s\) exactly when every bit \(v\) of \(s\) satisfies \(\lvert N(v)\cap s\rvert\le1\). Exhaustively testing the \(4095\) nonzero masks gives \(f_0=12\), \(f_1=66\), \(f_2=140\), \(f_3=105\), and no higher-dimensional simplices: altogether \(323\) nonempty faces. The packaged program separately tests the induced-degree characterization against forbidden triples.

**Acyclic matching.** Sort the nonempty face masks numerically. For each pivot \(v=0,1,\ldots,11\), in that order, traverse the lower masks \(s\) in increasing order; whenever both \(s\) and \(s\cup\{v\}\) are valid and unmatched and \(v\notin s\), pair them. This defines \(147\) pairs. For every covering relation \(s\subset s\cup\{v\}\), orient its edge upward if matched and downward otherwise. The independently replayable finite certificate checks that this directed Hasse graph has \(323\) nodes and \(972\) directed edges and admits a complete topological sort, so the matching is acyclic. Its critical cells comprise one vertex, four \(2\)-cells and twenty-four \(3\)-cells, with no cells of other dimensions. Discrete Morse theory therefore gives a homotopy-equivalent \(3\)-dimensional CW complex \(Y\) having precisely these cells.

**Integral attaching degrees.** Orient each simplex by ascending vertex indices. Use signed alternating gradient paths to compute the cellular boundary \(\partial_3:C_3(Y;\mathbb Z)\to C_2(Y;\mathbb Z)\). The four critical \(2\)-face masks are, in ascending order, \(100,146,164,1042\). The complete \(24\)-by-\(4\) integer matrix (one row per critical \(3\)-cell) and its ordered critical masks are in `morse_certificate.json`. Its rows at zero-based positions \(1,2,3,6\) form an integral matrix of determinant \(+1\). Thus \(\partial_3\) is surjective over \(\mathbb Z\) and has free kernel of rank \(24-4=20\). The only other nontrivial Morse chain group is the single \(0\)-cell, so \(\widetilde H_2(Y;\mathbb Z)=0\) and \(\widetilde H_3(Y;\mathbb Z)\cong\mathbb Z^{20}\), with all other reduced groups zero.

**From homology to homotopy.** The CW model \(Y\) has one \(0\)-cell and no \(1\)-cells, hence is simply connected. By the degree-two Hurewicz theorem, \(\pi_2(Y)\cong H_2(Y)=0\), so it is \(2\)-connected. The degree-three Hurewicz theorem identifies \(\pi_3(Y)\cong H_3(Y)\cong\mathbb Z^{20}\). Choose twenty maps from \(S^3\) representing a basis and wedge them into a map \(\bigvee^{20}S^3\to Y\). This map induces an integral homology isomorphism in every degree (the higher homology vanishes since \(Y\) is \(3\)-dimensional); Whitehead's theorem makes it a homotopy equivalence. Composing with Forman's equivalence proves the claim.

## Verification
Run `python3 verify_icosahedron.py` with `morse_certificate.json` in the same directory. The program uses only the Python standard library. It independently builds and checks the explicit \(12\)-vertex graph, enumerates every candidate face, reconstructs the ordered greedy matching, exhaustively checks acyclicity of all \(972\) covering relations, recomputes the signed Morse matrix from alternating gradient paths, and compares every certificate entry. It also calculates the ranks of the original simplicial boundary matrices over \(\mathbb F_2\), without using the Morse matrix. Those ranks are \((11,55,85)\), giving reduced mod-two Betti numbers \((0,0,0,20)\) in degrees \(0,1,2,3\) respectively. The saved output is `verification_output.txt`. The mod-two calculation alone would not certify the integral homotopy type; the primitive integer minor and the CW argument above are essential.

## Relationship to prior work
Taylan's 2015 theory of devoid complexes and matching trees [1] supplies the historical \(P_3\)-avoidance motivation and treats paths and forests, but its inspected results do not compute this icosahedral complex. Deshpande and Singh [2] determine higher-independence homotopy types for complete multipartite, fully whiskered, path, cycle and perfect rooted-tree families. Carnero Bravo [3] identifies \(\operatorname{Ind}_2(G)\) with the first stage of the forest filtration and proves formulas for other families and graph operations. The icosahedron is none of those classified graph families. Calculations of the icosahedral ordinary independence, matching, three-cut, Lovász neighborhood, or metric-complex constructions concern different simplicial face conditions and do not imply the displayed equivalence.

## Limitations
This is one exact finite canonical graph, not a universal formula for arbitrary triangulated spheres, Platonic graphs, or higher independence parameters. It determines ordinary integral homotopy type, not an equivariant splitting under the icosahedral group or a geometric homeomorphism. Some mathematically equivalent unindexed or unpublished source may exist; literature checks do not establish absolute publication priority. The computational verification is finite and exhaustive for the stated twelve-vertex object, not for a graph family.

## References
[1] D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754 (first public version 2015-01-27), https://arxiv.org/abs/1501.06754.

[2] P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (first public version 2020-01-15), https://arxiv.org/abs/2001.05448.

[3] A. Carnero Bravo, *The forest filtration of a graph*, arXiv:2307.13271 (first public version 2023-07-25), https://arxiv.org/abs/2307.13271.

[4] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145.
