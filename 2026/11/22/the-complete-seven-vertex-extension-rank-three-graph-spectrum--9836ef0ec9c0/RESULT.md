# The complete seven-vertex extension-rank-three graph spectrum

## Finding

Let \(\mathcal G\) be the class of finite simple undirected graphs, with the induced-subgraph notion of embedding. Among graphs on **exactly seven vertices**, precisely **372 isomorphism types**, or **1,163,358 graphs on the labelled vertex set \(\{0,1,\ldots,6\}\)**, have one-point-extension rank three. The numbers by edge count are the coefficients of the following complete unlabelled and labelled rank-three polynomials:

\[
\begin{aligned}
U(z)={}&z^6+10z^7+31z^8+61z^9+83z^{10}+83z^{11}\\
&+61z^{12}+31z^{13}+10z^{14}+z^{15},\\
L(z)={}&5040z^6+31500z^7+99540z^8+191520z^9\\
&+254079z^{10}+254079z^{11}+191520z^{12}\\
&+99540z^{13}+31500z^{14}+5040z^{15}.
\end{aligned}
\]

A structural test recognizes **every** such graph without enumerating its isomorphisms. A seven-vertex graph \(G\) has rank three exactly when there is a vertex \(v\) of degree three such that, writing \(A=N_G(v)\) and \(B=V(G)\setminus(A\cup\{v\})\), both of the following hold:

1. Some \(a\in A\) has one neighbor in \(A\setminus\{a\}\) and either one or two neighbors in \(B\).
2. Some \(b\in B\) has one neighbor in \(B\setminus\{b\}\) and either one or two neighbors in \(A\).

Both \(A\) and \(B\) necessarily have three vertices. Complementation exchanges the two sides of the test and sends the edge count \(e\) to \(21-e\), explaining the palindromic polynomials. The known seven-vertex onset and unique six-edge extremizer are **not** new claims here; the contribution is the entire threshold-layer classification and its two exact edge distributions.

## Assumptions and scope

All graphs here are simple, undirected, finite and loopless; there are no colours or additional predicates, and an embedding preserves both edges and nonedges. If \(F\subseteq V(G)\), set \(\operatorname{rk}_G(F)\geq0\), and recursively set \(\operatorname{rk}_G(F)\geq r+1\) exactly when **every** abstract way to add one new vertex with specified adjacencies to the named points of \(F\) can be realized by some \(x\in V(G)\setminus F\) for which \(\operatorname{rk}_G(F\cup\{x\})\geq r\). Write \(\operatorname{rk}(G)=\operatorname{rk}_G(\varnothing)\). Thus types are evaluated relative to their named bases and individual realizations may depend on the type.

Define \(P_G(v,w)=\{(\mathbf1_{vx\in E(G)},\mathbf1_{wx\in E(G)}):x\in V(G)\setminus\{v,w\}\}\) for distinct vertices \(v,w\). Call a pair *full* when \(P_G(v,w)=\{0,1\}^2\). The polynomials count unlabelled isomorphism classes and labelled graphs, respectively, **on exactly seven vertices**, grouped by their exact number of edges. The theorem makes no claim about their number at larger orders or the separate universal forcing invariant.

## Proof

**Step 1 (unrolling the extension game).** A pair has rank at least one exactly when it is full, since the four abstract extensions of a named pair are its four possible adjacency masks. A singleton has rank at least two exactly when it admits both an adjacent and a nonadjacent full pair, with possibly different partners. Therefore, for any graph \(G\),

\[
\operatorname{rk}(G)\ge3\quad\Longleftrightarrow\quad
\exists v\,\exists a\,\exists b\quad
[va\in E(G),\ vb\notin E(G),\ P_G(v,a)=P_G(v,b)=\{0,1\}^2],
\]

where \(v,a,b\) are distinct. This also appears in the previously published rank-three graph extremum [2], and is used here rather than presented as a new general lemma.

**Step 2 (structural test at the first feasible order).** Suppose \(v,a,b\) satisfy Step 1. Fullness of \((v,a)\) forces at least two other neighbors of \(v\), and fullness of \((v,b)\) forces at least two other nonneighbors of \(v\). As \(a\) is a neighbor and \(b\) a nonneighbor, \(v\) has at least three vertices of each kind. On seven vertices its degree is therefore exactly three, with \(|A|=|B|=3\). To make \((v,a)\) full, the other two points of \(A\) must give one adjacency and one nonadjacency to \(a\); the three points of \(B\) must do likewise. These are precisely the first numbered condition. Similarly, the two points of \(B\setminus\{b\}\) must give one adjacency and one nonadjacency to \(b\), and the three points of \(A\) must do likewise, which is the second condition. Conversely these two conditions supply all four patterns for each of the two pairs, so Step 1 proves the structural test is sufficient as well as necessary.

No graph on fewer than seven vertices has rank at least three by the same neighbor/nonneighbor bound. Every seven-vertex graph in the theorem has rank **exactly** three: rank at least four would entail a three-element named base of rank at least one, requiring all eight adjacency patterns on eight *distinct* vertices outside that base, hence at least eleven vertices in total.

**Step 3 (exact Burnside enumeration).** Label seven vertices by \(0,\ldots,6\) and identify a graph with one of the \(2^{21}\) subsets of the twenty-one unordered pairs. A permutation of the vertices acts on these twenty-one edge positions. If a permutation has cycle partition \(\lambda\vdash7\), a graph is fixed by it exactly when its edge set is a union of cycles of this induced edge permutation. Choose one permutation for each of the fifteen partitions \(\lambda\), determine its edge cycles, and enumerate every subset of those cycles. For each resulting fixed graph, apply the necessary-and-sufficient root-degree test from Step 2, retaining its edge count. This is an exhaustive finite proof: all fixed graphs occur exactly once in the edge-cycle subset enumeration.

Let \(f_{\lambda,e}\) be the number of retained fixed graphs with \(e\) edges, and put \(z_\lambda=\prod_{j\ge1}j^{m_j}m_j!\) when \(\lambda\) has \(m_j\) cycles of length \(j\). The conjugacy class has size \(7!/z_\lambda\), so Burnside's lemma gives the integer counts

\[
[z^e]U(z)=\frac1{7!}\sum_{\lambda\vdash7}\frac{7!}{z_\lambda}f_{\lambda,e},
\qquad [z^e]L(z)=f_{1^7,e}.
\]

The fifteen fixed-graph totals, in descending cycle-partition order, are \(0,2,0,8,0,2,18,18,0,0,0,1238,2262,15630,1163358\). Weighted by the fifteen class sizes, their sum is \(1,874,880=7!\cdot372\). Evaluating the same formulas edge by edge yields exactly the two polynomials displayed above; `CENSUS_OUTPUT.txt` records all fixed totals and coefficients. Crucially, `rank3_burnside.cpp` is a complete standalone C++17 implementation of the edge-orbit derivation, not a precomputed graph-isomorphism table. Its `good` test implements Step 2, and its explicit loops over all integer partitions, edge orbits and orbit subsets establish complete coverage.

**Step 4 (a logically independent recurrence check).** `rank3_recursive.py` evaluates the original rank recursion, considering every abstract one-point adjacency mask at every marked base, rather than the Step 2 root test. Its input `atlas_le7.g6` contains the 1,253 graph6 representatives of all unlabelled simple graphs on at most seven points in the Read–Wilson graph atlas [3]. It finds no rank-three examples below seven points, and exactly the 372 seven-point types and edge coefficients of \(U(z)\). This separately checks the root reduction and the finite count. The primary Burnside enumeration does **not** rely on the atlas's completeness.

## Verification

The exact source files in this package are `rank3_burnside.cpp`, `rank3_recursive.py`, `atlas_le7.g6` and `CENSUS_OUTPUT.txt`. With a C++17 compiler, run `g++ -O3 -std=c++17 rank3_burnside.cpp -o rank3_burnside` and `./rank3_burnside`. It enumerates every graph fixed by representatives of every permutation cycle type, checks both entire edge histograms and prints `BURNSIDE_ALL_CHECKS_OK`. Run `python3 rank3_recursive.py` (Python 3 standard library only). It evaluates the rank recursion across the 1,253 graph6 cases and prints `DIRECT_RECURSION_OK`. Both were executed successfully from the constructed package sources and are to be replayed after extraction of the embedded delivery row. No finite experiment is being extrapolated to larger orders.

## Relationship to prior work

López-Callejas and Navarro-Castillo [1] give the underlying rank definition for hereditary classes of relational structures and explicitly raise graph quantitative questions. The previously published result [2] proves the seven-vertex onset, the six-edge minimum and the unique six-edge graph, together with the general full-pair criterion; its stated limitations do **not** classify all seven-vertex rank-three graphs. The present contribution counts *every* graph at that natural first-order boundary, at every edge count, in both named and isomorphism-quotiented forms; it proves an explicit seven-vertex root criterion and the complete spectrum. The Read–Wilson atlas [3] enumerates all small graphs without the extension-rank filter. No identity of titles or parameter numbers is treated as evidence of originality: the implication comparison distinguishes the previously proved sparse extremum from the unrestricted first-layer rank spectrum.

## Limitations

The theorem is an exact finite classification on exactly seven vertices, not an asymptotic law or a classification at arbitrary order. Its Burnside enumeration is a finite, inspectable combinatorial certificate, not a general closed-form family of rank polynomials. The graph-atlas test is corroboration, not a substitute for the complete orbit enumeration. Historical priority is provisional and an independent mathematical audit has not been performed. The separate universal forcing cutoff \(N(3)\) is not determined here.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, first public posting 2026-04-15, arXiv:2604.14461v1, https://arxiv.org/html/2604.14461v1.
2. *Sharp rank-three onset and six-edge extremum for finite graphs*, published research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-rank-three-onset-and-six-edge-extremum-for-finite-graphs--a3c35b6162f1.
3. R. C. Read and R. J. Wilson, *An Atlas of Graphs*, Oxford University Press, 1998. Graph-index documentation: https://r.igraph.org/reference/graph_from_atlas.html.
