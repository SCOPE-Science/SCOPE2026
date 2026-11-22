# Exchange geometry of optimal identifying codes on odd square rook graphs

## Finding

Let \(R_n=K_n\square K_n\), with vertices the cells \((i,j)\) of an \(n\times n\) board, adjacent exactly when they share a row or column. An *identifying code* is a subset \(C\) such that the traces \(N[v]\cap C\) are nonempty and pairwise distinct. Let \(\mathcal X_n\) have as its vertices **all minimum-cardinality identifying codes** of \(R_n\); join two codes precisely when their symmetric difference has two elements (one codeword is replaced by one unoccupied cell).

For every odd \(n=2m+1\ge5\), the exchange graph \(\mathcal X_n\) is vertex-transitive and **\(7m\)-regular**, with
\[
|V(\mathcal X_n)|=\frac{n^2((n-1)!)^2}{m!},\qquad
|E(\mathcal X_n)|=\frac{7m\,n^2((n-1)!)^2}{2m!}.
\]
Every exchange is one of exactly two geometric types: a local change to a selected three-edge path inside a fixed \(2\times2\) block (three choices per path), or a transfer involving that path and the unique isolated selected edge (four choices per path).

At the first order covered by this theorem, \(n=5\), the graph \(\mathcal X_5\) has \(7200\) vertices, \(50400\) edges, one connected component, and radius and diameter both \(9\). Every vertex has the same distance-shell vector
\[
(1,14,81,208,504,1024,1696,2184,1352,136).
\]
The minimum code size \(3m+1\) and the unique optimum orbit under independent row and column permutations are **previously known** [1]. The asserted new contribution is the precise exchange geometry, including the all-order degree and the first nontrivial full distance census; the orbit count is included for normalization, not claimed independently new.

## Assumptions and scope

All graphs are finite, simple, labelled and undirected. The parameter \(n\) is an odd integer at least \(5\), and \(m=(n-1)/2\). The exchange move replaces exactly **one** chosen cell by exactly **one** previously unchosen cell, preserving identifying-code feasibility and minimum cardinality at every intermediate state. No adjacency restriction is imposed on the replacement sites (token jumping, not token sliding). The finite distance census concerns \(n=5\) alone; no diameter or connectedness assertion is made for all larger odd orders.

Identify an \(n\times n\) board with edges of \(K_{n,n}\): rows and columns become its two shore classes, and each selected cell is a selected edge. Two cells share a row or column precisely when the corresponding edges of \(K_{n,n}\) intersect. Thus an identifying code on \(R_n=L(K_{n,n})\) is an edge-identifying code of \(K_{n,n}\).

## Proof

**1. Classification of optimum supports (static fact [1], reconstructed for use here).** The 2008 classification [1] gives \(\gamma^{\rm ID}(R_n)=3m+1\) and uniqueness of the optimum orbit for odd \(n\ge5\). We also give a direct structural argument, which is required for the exchange analysis. Let \(H\) be the spanning bipartite graph of the \(2n=4m+2\) row and column vertices with the selected code cells as edges. A component on three vertices is impossible: its two selected edges have identical identifying traces. There cannot be two isolated vertices (same-shore rows or columns would generate duplicate traces, whereas opposite-shore isolates would give an undominated cell), two isolated selected edges (the crossed cells between them would have equal traces), or an isolated vertex together with an isolated selected edge (one original and one cross cell would have equal traces). Hence all but at most one component have at least four vertices.

Write \(c\) for the number of components of \(H\), including isolates. Since each component has at least \(v-1\) edges, the known minimum size implies \(3m+1\ge (4m+2)-c\), hence \(c\ge m+1\). On the other hand, the small-component restriction and total vertex count give \(c\le m+1\). Therefore \(c=m+1\), and equality in the forest edge bound forces every component to be a tree. Having no small component would require at least \(4(m+1)\) vertices, so exactly one component has size one or two. A singleton would force one five-vertex tree and \(m-1\ge1\) four-vertex trees. Every four-vertex tree allowed as an identifying code must be a path of three edges: a three-leaf star would give two selected edges with the same trace. In each selected four-vertex path there is a leaf on each shore. A singleton row/column together with a selected leaf on that same shore creates two distinct cells with equal traces in the neighboring opposite-shore row/column. Therefore the small component cannot be a singleton. It is a single selected edge; all other components have four vertices and three selected edges, hence are four-vertex paths \(P_4\).

Conversely, one disjoint selected edge and \(m\) disjoint alternating selected \(P_4\)'s cover all row and column vertices and always identify the board: every row/column has at least one selected incident edge; within each \(P_4\) no two adjacent selected edges are pendant twins; two selected isolated edges never occur; and a direct comparison of signatures \(S(i,j)=\operatorname{star}_H(i)\cup\operatorname{star}_H(j)\) separates all distinct cells. Equivalently this is precisely the constructive sufficiency argument of the girth-four edge-code criterion in [2]. This confirms the form already implied by [1].

**2. Count and vertex transitivity.** Choose the isolated selected edge in \(n^2\) ways. Partition the remaining \(2m\) row vertices and \(2m\) column vertices independently into unordered pairs, then match the \(m\) row-pairs with the \(m\) column-pairs. Each resulting \(2\times2\) rectangle has exactly four possible selected \(P_4\)'s, according to which corner is absent. This gives
\[
n^2\left(\frac{(2m)!}{2^m m!}\right)^2 m!4^m
=\frac{n^2((2m)!)^2}{m!}.
\]
The unique decomposition and the uniquely missing cell make this count free of multiplicity. Independent permutations of row labels and column labels take any such decomposition to any other; hence their action is transitive on the exchange-graph vertices.

**3. Complete enumeration of legal one-cell replacements.** Fix one optimum. Removing the unique isolated selected edge creates two singleton vertices in \(H\), and no *different* added edge can restore the required component decomposition. In any one \(P_4\) there are two leaf edges and one central edge. Removing a leaf edge leaves a \(P_3\) and one isolated shore vertex: the sole alternative restoration producing a \(P_4\) in the same block is to attach that vertex to the opposite endpoint of the \(P_3\), yielding exactly one new code per removed leaf edge. Removing the central edge leaves two disjoint selected \(K_2\)'s, alongside the original isolated selected \(K_2\). One replacement edge can connect the two newly separated \(K_2\)'s in just one new way (the missing fourth corner), or it can connect the original \(K_2\) to either newly separated \(K_2\) in two bipartite ways, yielding four more new codes. A replacement touching a different intact \(P_4\) necessarily leaves a forbidden three-vertex component, an isolated vertex, or a component of size at least six; thus there are no other possibilities. Each original \(P_4\) contributes exactly \(2+1+4=7\) distinct neighbors, and a move can affect only one of the \(m\) original paths. Therefore every optimum has degree \(7m\). Handshaking gives the edge count above.

**4. The first odd graph's complete metric.** For \(n=5\), enumerate all \(\binom{25}{7}=480700\) seven-cell subsets and select precisely those whose 25 row-or-column closed-neighborhood signatures are nonempty and pairwise distinct. There are \(7200\). Build adjacency by deleting one of the seven selected cells and adding one of the eighteen unselected cells, retaining an edge only when the resulting 25-bit mask also indexes an optimum. Both standalone verification programs obtain 14 neighbors at every optimum and 50400 exchange edges. Breadth-first search from the canonically first enumerated optimum visits all \(7200\) and gives the distance-shell vector reported above; in particular its eccentricity is \(9\). Since independent row and column permutations act transitively, this one breadth-first search certifies the diameter and radius of the entire graph, not merely a representative's eccentricity.

## Verification

The attached `verify_py.py` independently enumerates the \(480700\) candidates using combination iteration, obtains traces as sets of labelled selected squares, constructs the entire exchange adjacency and performs breadth-first search. The attached `verify_cpp.cpp` enumerates exactly the same candidate universe by a separate bit-combination iteration and an independent signature-sorting implementation, builds the exchange graph using a mask-index dictionary, and performs its own breadth-first search. Both tests have been executed and agree on
\[
|\mathcal C_5|=7200,\quad \deg_{\mathcal X_5}=14,\quad |E(\mathcal X_5)|=50400,
\quad \operatorname{diam}(\mathcal X_5)=9
\]
and the full ten-term shell vector. These exhaustive finite computations establish the \(n=5\) assertions. They do **not** prove the all-order assertion; its proof is the structural exchange argument in Step 3.

To reproduce, run `python3 verify_py.py` and `c++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp` in a directory containing the two files. No third-party Python libraries or graph packages are required.

## Relationship to prior work

[1] Gravier, Moncel and Semri proved the exact minimum code size and **uniqueness up to independent row and column permutations** for odd square rook graphs. Their Theorem 1 covers the underlying static optimizer family, and the component form and count here are presented as background/normalization, not new discoveries. The extra questions solved here concern *the graph of replacements between optima*: full local move classification, exact all-order degree, and the first odd board's diameter and distance distribution. These do not follow from the published static numerical statement without analyzing replacement feasibility.

[2] Foucaud, Gravier, Naserasr, Parreau and Valicov give an equivalent edge-code formulation for line graphs, a general edge-identification criterion, and the minimum size of an edge-identifying code of the balanced biclique, consistent with [1]. The paper does not report replacement-graph edges or distances.

[3] Goddard and Wash extend minimum-size results to rectangular Cartesian products of cliques; their work concerns optimizing cardinality, not the exchange metric on the odd balanced equality cases.

## Limitations

The all-order conclusion establishes regularity, transitivity and edge counts, **not** connectedness, diameter or a distance-shell formula at arbitrary odd orders. The ten-shell census and diameter are proved only at \(n=5\) by exhaustive finite enumeration, using vertex transitivity to reduce the global metric check to one source. The static optimizer classification is established prior work and is not an originality claim. Publication-priority completeness cannot be guaranteed; obscure or unindexed earlier work could potentially contain the same reconfiguration result. No independent scholarly audit has been conducted.

## References

[1] S. Gravier, J. Moncel and A. Semri, *Identifying codes of Cartesian product of two cliques of the same size*, Electronic Journal of Combinatorics **15** (2008), N4; published February 11, 2008. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1n4/pdf/

[2] F. Foucaud, S. Gravier, R. Naserasr, A. Parreau and P. Valicov, *Identifying codes in line graphs*, Journal of Graph Theory **73** (2013), 425–448, online July 17, 2012; arXiv:1107.0207. https://arxiv.org/abs/1107.0207 ; https://doi.org/10.1002/jgt.21686

[3] W. Goddard and K. Wash, *ID codes in Cartesian products of cliques*, Journal of Combinatorial Mathematics and Combinatorial Computing **85** (2013), 97–106. https://combinatorialpress.com/article/jcmcc/Volume%20085/vol-085-paper%206.pdf
