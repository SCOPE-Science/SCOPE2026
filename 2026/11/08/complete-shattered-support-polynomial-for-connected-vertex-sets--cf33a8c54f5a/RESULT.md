# Complete shattered-support polynomial for connected vertex sets of three-path theta graphs

## Finding

Let \(a,b,c\geq1\) be integers. Let \(\Theta(a,b,c)\) be the simple theta graph formed by three internally vertex-disjoint paths between common distinct poles \(u,v\), having respectively \(a,b,c\) internal vertices. Write \(n=a+b+c+2\). Its binary concepts are the vertex sets of all connected induced subgraphs, **together with the empty set**; an instance is a vertex and its label is its membership in the concept.

Let \(\Phi_{a,b,c}(z)=\sum_{k\geq0}s_k(a,b,c)z^k\), where \(s_k\) is the number of \(k\)-vertex supports on which every binary labeling is realized. Then the following identity holds for all positive integers \(a,b,c\):

\[
\boxed{\Phi_{a,b,c}(z)=1+nz+\binom n2 z^2+\binom n3 z^3+Q(a,b,c)z^4,}
\]
where
\[
\begin{aligned}
Q(a,b,c)={}&2abc+\binom a2bc+\binom b2ac+\binom c2ab\\
&+\binom a2\binom b2+\binom a2\binom c2+\binom b2\binom c2.
\end{aligned}
\]
In particular \(\operatorname{VCdim}=4\), independent of the lengths of the three paths.

More precisely, every support of size at most three is shattered, no support of size at least five is shattered, and a four-vertex support is shattered **exactly** in one of these disjoint cases:

1. It contains exactly one pole and one internal vertex of each of the three paths.
2. It contains no pole and its distribution among the three path interiors, in some order, is \((2,1,1)\).
3. It contains no pole and its distribution among the path interiors, in some order, is \((2,2,0)\).

The listed distribution conditions concern counts only; there are no restrictions on the positions selected inside the respective paths.

## Assumptions and scope

All graphs are finite, undirected, simple. Each path from \(u\) to \(v\) has at least two edges; hence every internal branch is nonempty. The three paths have disjoint internal vertex sets and no additional edges. A connected induced vertex subset may be any nonempty subset whose induced subgraph is connected; the empty subset is also admitted as a concept to realize the all-zero labeling. A *shattered support* is an unordered vertex subset on which every labeling in \(\{0,1\}^{S}\) is attained by a concept. The coefficient counts each support once, regardless of how many concepts realize a labeling.

## Proof

**Step 1: the connectivity test.** For any graph and any support \(S\), assuming the empty concept, \(S\) is shattered if and only if, for every two distinct vertices \(x,y\in S\), there is an \(x\)-to-\(y\) path whose internal vertices avoid \(S\setminus\{x,y\}\). Necessity follows by asking that exactly \(x,y\) be positive. Conversely, to realize a nonempty positive set \(P\subseteq S\), fix \(x\in P\) and take the union of paths between \(x\) and each other point of \(P\), each avoiding all vertices of \(S\setminus P\). The induced subgraph on the union is connected and realizes exactly \(P\). The empty concept realizes \(P=\varnothing\). This general pairwise-path test is **previously known**, notably in Kranakis et al. (1994, Corollary 4.4); only its theta-graph specialization and enumeration are claimed below.

**Step 2: deletion geometry of a theta graph.** Deleting no vertex or just one vertex never disconnects \(\Theta(a,b,c)\), because it is 2-vertex-connected. If two deleted vertices lie in the interiors of different paths, the surviving graph remains connected by the third intact \(u\)-to-\(v\) path. If the deleted vertices are both internal to one path, they isolate only the vertices *strictly between them*, when these exist; all other surviving vertices remain mutually connected. Deleting \(u\) and an internal vertex \(x\) isolates only the vertices strictly between \(u\) and \(x\) on its path, while all remaining vertices beyond \(x\) connect to \(v\). There is a symmetric statement for \(v\). Deleting both poles separates the interiors of the three paths. These exhaust the two-vertex deletions.

**Step 3: three or fewer vertices.** With at most three selected vertices, the pairwise-path criterion excludes at most one other selected vertex. Two-vertex-connectivity guarantees all such paths, so all supports of sizes zero through three are shattered. Their counts are the binomial coefficients in the displayed polynomial.

**Step 4: classification of four vertices.** Fix a four-support \(S\); the pairwise-path criterion reduces its shattering to whether any two selected negative vertices disconnect the other two.

If both poles lie in \(S\), and the two remaining vertices lie on different paths, deleting the poles separates them. If they lie on the same path with order \(u,x,y,v\), deleting \(v,x\) separates \(u,y\). Thus no four-support with two poles is shattered.

If exactly \(u\) lies in \(S\), and two internal selected vertices are on the same path, let \(x\) be the one nearer \(u\) and \(y\) the farther one. Deleting \(u,y\) isolates \(x\) from the remaining selected internal vertex. Consequently there must be exactly one selected interior vertex on each path. Conversely, any two deleted selected vertices are either in different path interiors (leaving the graph connected) or are \(u\) and one path interior (leaving both positive interior vertices on the other paths connected through \(v\)). Thus exactly the stated one-pole supports work. Pole \(v\) is symmetric.

If neither pole belongs to \(S\), and some path contains three selected vertices while another path contains at least one, deleting the first and third of those three isolates the middle selected vertex from the selected vertex on the other path. If all four are on one path, write their order as \(x_1,x_2,x_3,x_4\); deleting \(x_2,x_4\) isolates \(x_3\) from \(x_1\). Thus every path contains at most two selected vertices. Conversely, with at most two selected vertices per path, deleting two on different paths leaves the graph connected; deleting two on the same path leaves no selected vertex strictly between them, and all surviving selected vertices are connected externally via the poles and other paths. The possible distributions of four interiors among three nonempty branches are precisely \((2,2,0)\) and \((2,1,1)\).

**Step 5: five or more vertices.** Shattering is hereditary under taking subsets, so it suffices to exclude five-supports. Any five-support containing two poles contains a nonshattered four-support with both poles. Any five-support containing exactly one pole contains a nonshattered four-support with that pole, two selected internal vertices on one arm and a third selected internal vertex (by pigeonhole). For a five-support with no pole, if any arm contains at least three selected interiors then it has a nonshattered four-subset of the kind in Step 4 (either three on one arm and one elsewhere, or four on a single arm). The only distribution not already excluded is \((2,2,1)\). Name the two selected vertices on the first arm \(x_1,x_2\) in order from \(u\) to \(v\), the two on the second arm \(y_1,y_2\), and the selected vertex on the third arm \(w\). Delete the three negative vertices \(x_2,y_1,w\). These three deletions destroy every pole-to-pole route; the two remaining positive vertices \(x_1\) and \(y_2\) lie in different components. This labeling cannot be realized. Therefore no five-support, hence no larger support, is shattered.

**Step 6: counting.** The one-pole supports contribute \(2abc\). Four interior selections with distribution \((2,1,1)\) contribute \(\binom a2bc+\binom b2ac+\binom c2ab\). Distribution \((2,2,0)\) contributes \(\binom a2\binom b2+\binom a2\binom c2+\binom b2\binom c2\). Together with Steps 3 and 5 this proves the polynomial and \(\operatorname{VCdim}=4\), since \(abc>0\).

## Verification

The accompanying standalone Python program `theta_verify.py` uses two independent finite tests. Directly enumerating all connected induced vertex sets (plus the empty set) validates every support up to size five for the tested theta graphs with at most ten vertices, yielding `DIRECT_CONNECTED_SUBSETS_PASS 6680`. A separate graph-deletion/BFS implementation validates the support characterization for all triples of arm interior lengths from one through four, every support of size at most five, and the coefficient formula, yielding `ALL_THETA_ARMS_1_TO_4_PASS 45740`. It concludes with `THETA_CONNECTED_SHATTERING_PASS`. The unrestricted proof is above; this finite verification is corroboration only.

Reproduce with `python theta_verify.py` using Python 3 standard library.

## Relationship to prior work

Kranakis, Krizanc, Ruf, Urrutia and Woeginger (1994), *VC-Dimensions for Graphs*, established the general connected-set VC framework, the pairwise connectivity test, a maximum-leaf spanning tree comparison, and the NP-completeness of computing the invariant. Those general results are acknowledged here and are not claimed as new; their inspected discussion does not supply the present theta-specific four-support classification or polynomial. Dossou-Olory (arXiv:1910.04552v1, first public 2019-10-08) studies enumeration of connected induced subgraphs and structural extremes by cut and pendant vertices. This counts **concepts**, not shattered query supports, and its inspected text does not establish the polynomial above. The two-distance coloring of theta graphs and topological theta-space findings returned by semantic searches concern different invariants. A historical result using alternate nomenclature for connected-subgraph trace complexes could still cover the enumeration; this remains a residual priority risk.

## Limitations

The result addresses the three-path theta graphs with three nonempty internally disjoint arms, and the full family of connected induced vertex sets (plus empty). It does not establish an analogous classification for four or more arms, graphs containing additional edges, restricted connected set sizes, connected *edge*-set queries, or path-only concepts. No independent expert mathematical audit has been performed. The general connectivity test is established prior work. Priority of the explicit theta polynomial beyond searched sources is not guaranteed.

## References

1. E. Kranakis, D. Krizanc, B. Ruf, J. Urrutia, and G. J. Woeginger, *VC-Dimensions for Graphs*, Carleton University Technical Report TR-255, November 1994. https://carleton.ca/scs/wp-content/uploads/sites/260/TR255.pdf (especially Section 4 and Corollary 4.4).
2. A. A. V. Dossou-Olory, *Cut and pendant vertices and the number of connected induced subgraphs of a graph*, arXiv:1910.04552v1 (submitted 2019-10-08). https://arxiv.org/html/1910.04552v1.
3. M. Radovanović, N. Trotignon, and K. Vušković, *The (theta, wheel)-free graphs Part IV: Induced paths and cycles*, Journal of Combinatorial Theory, Series B 146 (2021), 495–531. https://eprints.whiterose.ac.uk/id/eprint/161693/ (graph-family context only).
