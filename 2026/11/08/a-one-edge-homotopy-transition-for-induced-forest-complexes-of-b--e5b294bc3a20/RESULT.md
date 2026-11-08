# A one-edge homotopy transition for induced-forest complexes of bipartite graphs

## Finding
Let \(G\) be any finite simple bipartite graph with a specified bipartition \(A\sqcup B\), where \(a=|A|\ge2\) and \(b=|B|\ge2\). Let \(\mathcal F(G)\) consist of all vertex subsets inducing an acyclic graph. Then
\[
\mathcal F(K_{a,b})\simeq\bigvee^{(a-1)(b-1)}S^2.
\]
If \(G\) omits at least one edge between \(A\) and \(B\), then \(\mathcal F(G)\) is \(2\)-connected: \(\pi_1(\mathcal F(G))=\pi_2(\mathcal F(G))=0\), and \(\widetilde H_i(\mathcal F(G);\mathbb Z)=0\) for \(0\le i\le2\). If exactly one cross-edge is missing, the complex is in fact contractible. The connectivity threshold is sharp: deleting two independent edges from \(K_{3,3}\) produces an induced-forest complex homotopy equivalent to \(S^3\).

Equivalently, among bipartite graphs with fixed bipartition sizes at least two, nonzero integral second homology of the induced-forest complex occurs **exactly for the complete bipartite graph**, with free rank \((a-1)(b-1)\). One missing edge destroys all these classes, irrespective of \(a\) and \(b\).

## Assumptions and scope
Graphs are finite, simple, undirected, and have a specified bipartition \(A\sqcup B\). No connectivity assumption on \(G\) is needed. All homotopy and homology assertions concern geometric realizations of abstract simplicial complexes, with integral coefficients unless a field is specified. A vertex subset is a face of \(\mathcal F(G)\) precisely when its induced subgraph contains no cycle. The theorem concerns the unrestricted induced-forest complex (not a bounded-maximum-degree stage of the forest filtration). The one-edge deletion is of a cross-edge of \(K_{a,b}\). The sharpness example deletes two disjoint edges, not two adjacent edges.

## Proof
**1. Complete-bipartite model.** Put \(Q=\mathcal F(K_{a,b})\). Because any induced subgraph containing at least two vertices on each side contains a four-cycle, a face of \(Q\) meets at most one of the sides in more than one vertex. Write
\[
X=\Delta_A * B_{\mathrm{disc}},\qquad Y=\Delta_B * A_{\mathrm{disc}}.
\]
Here \(\Delta_A\) and \(\Delta_B\) are full simplices, and \(A_{\mathrm{disc}}\), \(B_{\mathrm{disc}}\) are discrete vertex complexes. Then \(Q=X\cup Y\). Both \(X\) and \(Y\) are contractible cones; \(X\cap Y\) is the one-dimensional complete bipartite graph \(K_{a,b}\), realized as a simplicial complex with cross-edges. The intersection is connected. The homotopy pushout for this cofibration cover therefore gives
\[
Q\simeq \Sigma K_{a,b}\simeq\bigvee^{(a-1)(b-1)}S^2.
\]
More precisely, Mayer–Vietoris supplies an **integral isomorphism**
\[
\partial_{\mathrm{MV}}:\ H_2(Q;\mathbb Z)\longrightarrow H_1(K_{a,b};\mathbb Z).
\]
The van Kampen theorem gives \(\pi_1(Q)=0\). All three-vertex subsets of \(A\sqcup B\) induce forests in any bipartite graph; hence \(Q\) and \(\mathcal F(G)\) have the same two-skeleton for any spanning bipartite subgraph \(G\subseteq K_{a,b}\). Consequently \(\pi_1(\mathcal F(G))=0\) in all cases.

**2. A missing cross-edge supplies an integral basis of killing cells.** Choose an absent edge \(xy\) with \(x\in A\), \(y\in B\). For each \(u\in A\setminus\{x\}\) and \(v\in B\setminus\{y\}\), the four vertices \(\{x,u,y,v\}\) induce at most three edges in \(G\), because \(xy\) is absent. A four-vertex bipartite graph with at most three edges is a forest. Thus each tetrahedron
\[
\tau_{uv}=\Delta_{\{x,u,y,v\}}
\]
is present in \(\mathcal F(G)\); its entire two-dimensional boundary already lies in \(Q\).

Under \(\partial_{\mathrm{MV}}\), the oriented boundary cycle \(\partial\tau_{uv}\) maps, up to sign, to the fundamental four-cycle \(x-v-u-y-x\) in the *simplicial intersection graph* \(X\cap Y=K_{a,b}\). It is important that the edge \(xy\) is a one-simplex of the complex even though it is absent from the graph \(G\). The spanning tree of this intersection graph consisting of all \(xv\) for \(v\in B\), together with all \(uy\) for \(u\in A\setminus\{x\}\), has \(a+b-1\) edges. Its non-tree edges are exactly the \((a-1)(b-1)\) edges \(uv\) indexed above, and their fundamental four-cycles are a **\(\mathbb Z\)-basis** of \(H_1(K_{a,b};\mathbb Z)\). Hence the boundaries of these tetrahedra map onto all of \(H_2(Q;\mathbb Z)\).

Because the two-skeleton is common, \(\ker(\partial_2)\) is unchanged; every class in \(\ker(\partial_2)/\operatorname{im}(\partial_3(Q))\) is represented by a combination of the displayed tetrahedral boundaries. Therefore \(H_2(\mathcal F(G);\mathbb Z)=0\). Since \(\mathcal F(G)\) is simply connected, the degree-two Hurewicz isomorphism yields \(\pi_2(\mathcal F(G))=0\). This proves the universal \(2\)-connectivity assertion for every proper bipartite spanning subgraph, including disconnected graphs.

**3. Exactly one missing edge.** Now suppose \(G=K_{a,b}-xy\). Any face outside \(Q\) must contain at least two vertices of each side. If it contained at least three vertices of \(A\) and two of \(B\), two selected vertices of \(A\setminus\{x\}\) would have both selected \(B\)-vertices as neighbors, producing a four-cycle. Symmetrically, no face outside \(Q\) can have at least three vertices from \(B\). Hence the only new faces are precisely the \((a-1)(b-1)\) tetrahedra \(\tau_{uv}\) and their already-present subfaces. In the relative cellular chain complex of \((\mathcal F(G),Q)\), these are independent three-cells, so \(H_3(\mathcal F(G),Q;\mathbb Z)\cong\mathbb Z^{(a-1)(b-1)}\), with no other relative homology. The long exact sequence of the pair identifies the connecting map with the basis isomorphism just proved. Thus all reduced integral homology groups of \(\mathcal F(G)\) vanish. Since the complex is simply connected and a finite CW complex, the homological Whitehead theorem implies that it is contractible.

**4. Sharpness at two deleted edges.** Take \(G_*=K_{3,3}-\{a_1b_1,a_2b_2\}\). Direct classification by shore sizes yields exactly \(6\) vertices, \(15\) edges of the simplicial complex, \(20\) triangles, \(13\) tetrahedra, and \(2\) four-simplices; there are no higher simplices. Specifically the tetrahedra comprise the six original \((3,1)\) and \((1,3)\) faces plus seven \((2,2)\) faces containing at least one of the two missing cross-edges. The only four-simplices are \(\{a_1,a_2,a_3,b_1,b_2\}\) and \(\{a_1,a_2,b_1,b_2,b_3\}\). Their oriented boundaries are independent because each has a tetrahedral face not contained in the other; the resulting image in the free tetrahedral chain group is primitive (it contains a unit \(2\times2\) minor). Hence \(H_4(\mathcal F(G_*);\mathbb Z)=0\), and \(H_3\) has no torsion. The reduced Euler characteristic is
\[
-1+6-15+20-13+2=-1.
\]
The second step already proves that the complex is \(2\)-connected, so its only nonzero reduced integral homology is \(H_3\cong\mathbb Z\). By degree-three Hurewicz, a map \(S^3\to\mathcal F(G_*)\) represents its integral generator. It is a homology equivalence between simply connected CW complexes, and hence a homotopy equivalence by Whitehead's theorem. Therefore \(\mathcal F(G_*)\simeq S^3\).

## Verification
The accompanying standalone `verify.py` constructs bipartite graphs directly from their edges; for each vertex subset it determines acyclicity using independent union–find cycle detection. It constructs all simplicial boundary matrices and eliminates them over \(\mathbb F_2\) to check the reduced Betti numbers; mod-two checks corroborate but do not prove the integral theorem. It exhaustively checks every bipartite edge subset on bipartitions of sizes \((2,2)\), \((2,3)\), \((2,4)\), and \((3,3)\), tests additional sampled larger graphs, checks all single-edge deletions in the listed larger shapes, and validates the \((3,3)\) sharpness face vector and top-dimensional boundaries. The proof above establishes the integer lattice basis and primitive boundary facts, which are not inferred from mod-two computations.

Reproduction: run `python3 verify.py` with a standard Python 3 installation in the same directory. No external packages, data, network access, or randomness beyond a deterministic seeded sample are needed.

## Relationship to prior work
Carnero Bravo's 2023 forest-filtration paper establishes the induced-forest complex framework, the complete-bipartite base homotopy type, and a general girth connectivity bound \(\operatorname{conn}\mathcal F(G)\ge g(G)-3\). Its bound for graphs of girth four provides only simple connectivity, not the degree-two conclusion here. The complete-bipartite case of the displayed dichotomy is therefore previous knowledge. The new statement is the **uniform jump to two-connectivity after any missing cross-edge**, with contractibility after precisely one deletion and a sharp two-deletion example.

Carnero Bravo's 2023 work on polyhedral joins studies forest complexes for lexicographic products and does not state this missing-edge bipartite dichotomy. The proof here does not use results about lexicographic products. Related work on induced-forest extremal sizes concerns maximal cardinality, not these integral homotopy groups.

## Limitations
The theorem does not classify higher homotopy groups or homology in dimensions at least three for every proper bipartite graph. It treats the unrestricted induced-forest complex, not all bounded-degree filtration stages. Some high-girth bipartite instances already enjoy stronger connectivity from the published girth bound; the genuinely new uniform regime includes the many proper bipartite graphs with four-cycles. As with any literature comparison, an equivalent unindexed statement or a stronger theorem elsewhere remains a publication-priority risk. Finite verification is corroborative, and independent mathematical review has not been performed.

## References
1. A. Carnero Bravo, *The Forest Filtration of a Graph*, first public arXiv version July 25, 2023, arXiv:2307.13271. https://arxiv.org/abs/2307.13271
2. A. Carnero Bravo, *Polyhedral joins and graph complexes*, first public arXiv version July 26, 2023, arXiv:2307.14321. https://arxiv.org/abs/2307.14321
3. K. Gunderson, K. Meagher, J. Morris, V. R. T. Pantangi, *Induced forests in some distance-regular graphs*, January 12, 2023, arXiv:2301.05207. https://arxiv.org/abs/2301.05207
