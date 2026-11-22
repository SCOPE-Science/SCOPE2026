# Mutual-visibility facets and frozen optimal relocations in the Desargues graph

## Finding

For the Desargues graph \(D=H(5,2)\), the complete polynomial of ordinary mutual-visibility vertex sets is
\[
\mathcal P_D(z)=1+20z+190z^2+1080z^3+3925z^4+8944z^5+11300z^6+5840z^7+150z^8.
\]
Thus exactly \(31,450\) subsets are feasible and \(\mu(D)=8\), with exactly \(150\) optimum sets. The polynomial enumerating **inclusion-maximal** mutually visible sets is
\[
\mathcal F_D(z)=60z^6+4700z^7+150z^8.
\]
The \(150\) optimal sets form precisely two orbits under \(\mathfrak S_5\times C_2\), of sizes \(30\) and \(120\). The first orbit comprises pure single-bipartition-shore eight-sets; the second comprises sets inducing three independent edges and two isolated vertices. Replacing exactly one chosen vertex by one unchosen vertex while preserving cardinality eight gives the reconfiguration graph
\[
\mathcal R_{\rm jump}(D)\cong 2L(P)\sqcup120K_1,
\]
where \(P=KG(5,2)\) is the Petersen graph; hence there are \(60\) exchanges, two fifteen-state connected components (both of diameter three), and \(120\) isolated states. If a replacement additionally requires its removed and inserted vertices to be adjacent in \(D\), the slide graph is \(150K_1\): every optimum is frozen.

## Assumptions and scope

The vertices of \(D\) are all \(2\)-subsets and \(3\)-subsets of \([5]=\{0,1,2,3,4\}\); a two-subset and a three-subset are adjacent exactly when the former is contained in the latter. This is the standard twenty-vertex cubic Desargues graph, isomorphic to \(GP(10,3)\) and to the bipartite double cover of the Petersen graph.

A set \(S\subseteq V(D)\) is **mutually visible** when for every distinct \(u,v\in S\), at least one shortest \(u,v\)-path has no internal vertex in \(S\). Define \(\mathcal P_D(z)=\sum_{S\text{ feasible}}z^{|S|}\) and \(\mathcal F_D(z)=\sum_{S\text{ inclusion-maximal feasible}}z^{|S|}\). These definitions count labelled vertex subsets, not isomorphism classes. A token jump is \(S\mapsto(S\setminus\{u\})\cup\{v\}\) for \(u\in S\), \(v\notin S\), if the new set remains optimal; a token slide additionally imposes \(uv\in E(D)\).

## Proof

**1. Exhaustive finite face certificate.** Order the twenty vertices lexicographically, first the ten two-subsets and then the ten three-subsets. Construct all thirty edges from inclusion and independently calculate graph distances \(d(u,v)\). For each unordered pair \(u,v\), construct the finite collection \(I_{uv}\) of bitmasks of internal vertices of **all** shortest paths. An increasing-distance depth-first traversal is exhaustive, because precisely the steps satisfying \(d(u,w)=d(u,x)+1\) and \(d(u,w)+d(w,v)=d(u,v)\) lie on geodesics. The recorded numbers of distinct shortest paths are: ninety pairs have one, sixty have two, thirty have four, and ten have twelve (the total is \(190\) vertex pairs).

The following is an exact necessary-and-sufficient feasibility test for every selected-vertex mask \(s\):
\[
\forall\{u,v\}\subseteq S,\quad \exists i\in I_{uv}\text{ with }(i\mathbin{\&}s)=0.
\]
Because mutual visibility is hereditary under taking subsets, it suffices to build all feasible sets by appending increasing vertex indices to smaller feasible sets, testing each extension. Every feasible nonempty subset has exactly one increasing sequence of vertices, so the algorithm is exhaustive and duplicate-free. The layer sizes at cardinalities zero through nine are respectively
\[
(1,20,190,1080,3925,8944,11300,5840,150,0).
\]
No larger subset exists, as every larger feasible subset would contain a feasible nine-set. A feasible subset is inclusion-maximal if and only if every one-vertex extension is infeasible, again by heredity. Testing all \(31,450\) feasible masks gives exactly sixty maximal six-sets, 4,700 maximal seven-sets, and 150 maximal eight-sets. The attached `verify_visibility.py` executes every step and asserts the counts.

**2. Full optimum classification.** Apply all \(5!\) permutations of the underlying labels and the simultaneous complement operation exchanging two- and three-subsets. All \(240\) maps preserve incidence, and the verifier explicitly checks this for every edge. On the 150 feasible eight-sets, direct orbit generation yields two orbits of sizes 30 and 120, with no unclassified optimum. For the first orbit, each optimum consists entirely of eight vertices from one shore: it omits exactly two shore vertices. On the two-subset shore, these omissions are disjoint two-subsets of \([5]\), hence exactly the fifteen edges of \(P=KG(5,2)\). Complement duality gives fifteen more on the three-subset shore. The other orbit has the representative
\[
\big\{\{0,1\},\{0,3\},\{1,2\},\{3,4\},\{0,1,4\},\{0,2,4\},\{1,2,3\},\{2,3,4\}\big\},
\]
whose induced subgraph is \(3K_2\sqcup2K_1\). Orbit enumeration and selected-degree checks show all 120 have this induced type; none is wholly within a shore. A second implementation reconstructs the graph as \(GP(10,3)\) and exhaustively checks all \(2^{20}=1,048,576\) subsets by graph search rather than by geodesic-mask enumeration; it reproduces the complete face polynomial.

**3. Exchanges and slides.** Exhaustive pairwise comparison of the 150 optimum masks gives exactly sixty unordered pairs with symmetric difference two. All sixty are between pure eight-sets on the **same** shore. Omitting two two-subsets identifies each pure optimum with an edge of the Petersen graph. Two pure configurations on the same shore differ by one selected vertex precisely when the omitted Petersen edges share an endpoint, the definition of adjacency in \(L(P)\). There are no jump edges incident to the other 120 optimum sets; the verifier confirms the equivalence on all \(\binom{150}{2}\) pairs. Each \(L(P)\) has fifteen vertices, thirty edges and diameter three. Since every edge of the original graph joins different shores, a jump between two pure sets on the same shore cannot be a slide, and the 120 remaining states have no jumps at all. Consequently the slide graph is edgeless.

## Verification

`verify_visibility.py` uses the standard library, inclusion-model geodesic interiors, exact hereditary face generation, explicit symmetry actions, a facet test, and all optimum exchange pairs. Run `python verify_visibility.py`; expected final line is `VERIFY_OK`. `verify_bfs.py` independently uses the generalized Petersen \(GP(10,3)\) adjacency model, traverses every subset mask, and checks geodesic preservation by shortest-path breadth-first search with blocked selected interior vertices; run `python verify_bfs.py` and expect `VERIFY_BFS_OK`. The second model has the same labelled graph isomorphism type and the complete polynomial agrees coefficient by coefficient. An independently checked graph isomorphism between the two graph constructions is also available using a graph-isomorphism algorithm, but that auxiliary library is not required by either supplied verifier.

The verification is a reproducible, terminating exhaustive proof of a finite proposition. Neither verifier assumes an infinite-family theorem or equates numerical experiments with a proof about graphs of arbitrary order.

## Relationship to prior work

Di Stefano's foundational work (2021) defines ordinary mutual visibility and studies several graph classes. Cicerone–Di Stefano–Klavžar (2021/2022) treats Cartesian products, independent mutual visibility, and the triangle-free graphs of mutual-visibility number three; its last characterization cannot cover \(D\), whose mutual-visibility number is eight. Later work defines visibility polynomials and considers hypercube-like graphs, distinct constructions. None of the materially inspected primary works states the exact Desargues polynomial, its two symmetry orbits, or its extremal exchange geometry. A finite graph library might calculate the polynomial mechanically; an automated number is not assumed to establish these structural orbit/exchange claims. Related published Desargues locating-dominating and zero-forcing records concern different predicates and do not imply visibility of chosen pairs. Publication priority remains subject to independent literature review.

## Limitations

The claim is specific to the twenty-vertex Desargues graph, and is conditional on the **ordinary**, existential-geodesic notion of mutual visibility. It does not determine total/outer/dual visibility or invariants of all generalized Petersen graphs. Facet counts and the mixed-orbit rigidity are computationally established via fully specified exhaustive enumerations rather than a closed-form infinite-family classification. The computational checks and manuscript assessment have not received independent mathematical audit; absence of an identical indexed statement is not proof of worldwide novelty.

## References

- G. Di Stefano, *Mutual Visibility in Graphs*, arXiv:2105.02722, first publicly posted 2021-05-06, https://arxiv.org/abs/2105.02722.
- S. Cicerone, G. Di Stefano, S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024, first posted 2021-12-24, https://arxiv.org/abs/2112.13024.
- *Mutual visibility in hypercube-like graphs*, arXiv:2308.14443, first posted 2023-08-28, https://arxiv.org/abs/2308.14443.
- B. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066, first posted 2024-12-04, https://arxiv.org/abs/2412.03066.
- *Mobile mutual-visibility sets in graphs*, accessible author-hosted PDF https://rodin.uca.es/bitstream/handle/10498/39355/amc_3410.pdf (later work on related movement concepts).
