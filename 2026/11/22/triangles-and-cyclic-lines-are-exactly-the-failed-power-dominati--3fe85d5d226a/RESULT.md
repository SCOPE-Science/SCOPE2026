# Triangles and cyclic lines are exactly the failed power-dominating placements in the Shrikhande graph

## Finding

Let \(A=\mathbb Z_4\times\mathbb Z_4\), and let \(G\) be the Shrikhande graph with vertex set \(A\), in which distinct \(x,y\) are adjacent exactly when \(y-x\) lies in
\[\Gamma=\{\pm(1,0),\pm(0,1),\pm(1,1)\}.\]
Write \(K=2A=\{(0,0),(0,2),(2,0),(2,2)\}\). A vertex subset \(S\subseteq A\) **fails power domination** if and only if it is contained in either (i) a triangle of \(G\), or (ii) a four-vertex cyclic line \(a+\langle d\rangle\), where \(a\in A\) and \(d\in\{(1,0),(0,1),(1,1)\}\). There are exactly \(32\) triangles and \(12\) such lines. In particular, the inclusion-maximal failed placements are exactly these \(44\) sets.

The complete failed-set cardinality polynomial is
\[F_G(z)=1+16z+72z^2+80z^3+12z^4.\]
Consequently, the power-domination polynomial counting successful placements by cardinality is
\[P_G(z)=(1+z)^{16}-F_G(z).\]
All placements of at least five sensors succeed. The minimum power-domination number is \(\gamma_P(G)=2\), and there are exactly \(48\) minimum placements. They are the pairs \(\{a,b\}\) whose difference lies in
\[D=\{(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)\}.\]
The **entire set of inclusion-minimal successful placements**, not just the smallest ones, consists of these \(48\) pairs together with the \(16\) triples formed by deleting one vertex from any of the four cosets of \(K\). No inclusion-minimal successful placement has more than three vertices. Every minimum pair and every inclusion-minimal successful triple observes all vertices after a single simultaneous propagation wave following initial closed-neighborhood observation.

## Assumptions and scope

The graph is the explicitly labelled finite simple undirected Cayley graph above; all sets are ordinary sets of distinct vertices. Starting from \(S\), the observed set is initially \(M_0=N[S]\), the union of closed neighborhoods of selected vertices. At each subsequent round, any currently observed vertex with exactly one unobserved neighbor observes that neighbor; all eligible observations may occur simultaneously. The monotone process terminates when no new observation is possible. The set \(S\) is power dominating if the final observed set is all of \(A\). This is the standard graph-theoretic power-domination convention, with initial domination before propagation. All quantifiers include the empty set and all \(2^{16}\) labelled vertex subsets.

## Proof

**1. Types of two-sensor placements.** Translation by an element of \(A\) preserves adjacency and power domination. The linear maps \((x,y)\mapsto(y,x)\) and \((x,y)\mapsto(x-y,-y)\), with coordinates modulo four, preserve \(\Gamma\). Their actions are transitive on each of the three difference classes: the six elements of \(\Gamma\), the three nonzero elements of \(K\), and the six elements of \(D=A\setminus(\{0\}\cup\Gamma\cup K)\). Direct inspection of neighborhoods gives, respectively, an observed-set size of \(10\) with no legal force, \(12\) with no legal force, and \(12\) followed by a wave observing the four remaining vertices. Hence a two-set succeeds precisely when its difference belongs to \(D\). There are \(16\cdot6/2=48\) such pairs. A singleton sees only seven vertices and admits no legal force.

**2. A small independent-set calculation.** Suppose a placement contains no successful pair. Translate one of its vertices to \(0\). Every other selected vertex must belong to the nine-element set
\[B=\Gamma\cup(K\setminus\{0\}).\]
For the other selected vertices to be mutually compatible with the absence of a successful pair, every pairwise difference must also lie in \(B\). In the resulting nine-vertex compatibility graph on \(B\), direct subtraction modulo four shows that every vertex has four neighbors (eighteen edges in total), and that its **only** triangles are the following four:
\[\begin{gathered}
\{(0,1),(0,2),(0,3)\},\quad \{(1,0),(2,0),(3,0)\},\\
\{(1,1),(2,2),(3,3)\},\quad \{(0,2),(2,0),(2,2)\}.
\end{gathered}\]
There is no four-clique. The claims follow by comparing differences among the nine displayed elements of \(B\); the accompanying independent code checks this nine-vertex table explicitly by its equivalent full-set test.

It follows that any placement without a successful pair has at most four vertices. There are \(16\cdot18/3=96\) three-element placements with no successful pair. They are precisely \(32\) triangles (each of the 48 edges belongs to two triangles), \(48\) three-vertex subsets of cyclic lines (four subsets from each of twelve lines), and \(16\) three-subsets of the four cosets of \(K\). These three types are disjoint, and their counts exhaust \(96\). For four-sets lacking a successful pair, the four compatibility triangles above imply exactly \(16\cdot4/4=16\) possibilities: the twelve cyclic lines and the four cosets of \(K\). No five-set can lack a successful pair.

**3. Propagation on the remaining representatives.** Translations and the stated linear automorphisms carry every member of each of the three triple types and two four-set types to the indicated representative. The following table is obtained directly from the six-neighbor rule; \(e_1=(1,0)\) and \(e_2=(0,1)\). The middle column is the initial observed count \(|N[S]|\), and the last column is the final observed count.

| Representative \(S\) | \(|N[S]|\) | Final |
|---|---:|---:|
| \(\{0\}\) | 7 | 7 |
| \(\{0,e_1\}\) | 10 | 10 |
| \(\{0,2e_1\}\) | 12 | 12 |
| \(\{0,e_1+2e_2\}\) | 12 | 16 |
| \(\{0,e_1,e_1+e_2\}\) (triangle) | 12 | 12 |
| \(\{0,e_1,2e_1\}\) (three on line) | 12 | 12 |
| \(\{0,2e_1,2e_2\}\) (three on \(K\)) | 15 | 16 |
| \(\{0,e_1,2e_1,3e_1\}\) (line) | 12 | 12 |
| \(K\) | 16 | 16 |

Thus the failed triples are exactly the triangles and cyclic-line triples, while the triples drawn from a coset of \(K\) succeed. Of the four-element sets without successful pairs, the cyclic lines fail while the four cosets of \(K\) succeed. All larger sets succeed because they contain a successful pair. Monotonicity holds because adding initially observed vertices cannot prevent any observation achievable previously. This proves the failure characterization.

**4. Enumeration and minimality.** Distinct cyclic lines intersect in at most two vertices; their three-element subsets are pairwise distinct and disjoint from triangles. Each edge of \(G\) lies in a triangle; each involution-separated pair is contained in at least one cyclic line. Consequently, the failed sets have counts \(1\) (empty), \(16\) (singletons), \(48+24=72\) (pairs), \(32+48=80\) (triples), and \(12\) (four-sets), proving \(F_G\). Every successful pair is inclusion-minimal because singletons fail. Every successful \(K\)-coset triple is inclusion-minimal because its three pairs have nonzero order-two differences and therefore fail. Every other successful set contains one of these pairs or triples, proving completeness of the inclusion-minimal family and its count \(48+16=64\).

## Verification

The package includes two standalone, independently written verifiers: `verify_python.py` (Python 3, all subsets, simultaneous mask propagation) and `verify_cpp.cpp` (C++17, all subsets, sequential adjacency-list propagation). Run `python3 verify_python.py` and `c++ -std=c++17 -O2 verify_cpp.cpp -o verifier && ./verifier`. Both were executed from their actual package source paths and independently checked all \(65,536\) subsets, the 44 predicted maximal failures, the cardinality distribution, and the 48/16 minimal-placement classification. The Python verifier additionally checks the explicit two-/three-element geometric types. Results are recorded in `VERIFICATION.md`. The analytical proof does not rely on treating a partial search as an infinite statement; the entire graph and all its subsets are finite and explicitly covered.

## Relationship to prior work

Haynes, Hedetniemi, Hedetniemi and Henning (2002) introduced power domination for electric network monitoring; their paper treats complexity and trees, not this exact Shrikhande classification. Bjorkman et al. (2026) study general power-domination reconfiguration, with examples on small graphs and graph families distinct from the Shrikhande graph. Published complete power-domination enumerations of rectangular rook graphs do not imply this theorem: the \(4\times4\) rook graph shares the strongly regular parameters \((16,6,2,2)\) with the Shrikhande graph, but it is nonisomorphic and its previously determined minimum power-domination number is three, rather than two. Searches of indexed findings and primary literature were performed for a statement subsuming this exact structural criterion; none was identified. The claim is not an assertion of certified historical priority.

## Limitations

This is an exact finite theorem about the explicitly labelled Shrikhande graph, not a universal theorem for all strongly regular graphs. The equivalence between the original edge-monitoring and graph-theoretic closed-neighborhood/propagation definitions is taken from later standard literature and stated explicitly above. All subset counts are for labelled vertices of this fixed graph. Completeness of literature indexing cannot be guaranteed; independent external validation and historical priority confirmation have not been performed.

## References

1. T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi and M. A. Henning, *Domination in Graphs Applied to Electric Power Networks*, SIAM Journal on Discrete Mathematics 15(4) (2002), 519–529, https://doi.org/10.1137/S0895480100375831 (published electronically 10 September 2002).
2. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob and C. Reinhart, *Power Domination Reconfiguration*, La Matematica 5, article 8 (2026), https://doi.org/10.1007/s44007-025-00187-5.
3. Published indexed result, *Complete power-domination-set classification and polynomial of rectangular rook graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-complete-power-domination-set-classification-and-polynomial-of-r--48ce98e1f82f (used only for mathematical comparison, not as proof of the Shrikhande theorem).
