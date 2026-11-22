# Antineighborhood involution and sharp two-token mobility of minimum rainbow placements on the Clebsch graph

## Finding
Let \(G\) be the Clebsch graph on \(\mathbb F_2^4\), where two distinct vertices are adjacent when their xor belongs to \(\{1,2,4,8,15\}\), with the integers interpreted as four-bit vectors. A two-rainbow dominating function assigns to every vertex a subset of \(\{1,2\}\), requiring every unlabelled vertex to have neighbors carrying each of the two colors; its weight is the total number of color copies.

**Theorem.** The minimum weight is exactly \(6\). There are exactly \(320\) named-color minimum functions. Every minimum function consists of disjoint three-sets \(A\) (color 1) and \(B\) (color 2), with no doubly colored vertices, and is uniquely obtained from a three-set \(A\) by putting
\[
B=F(A):=V(G)\setminus N[A].
\]
The allowed \(A\) are precisely the \(160\) independent triples and the \(160\) triples inducing a three-vertex path. The map \(F\) is an involution on these \(320\) triples and interchanges the two types.

Among optimum functions, moving one copy of one color to another vertex never preserves validity. Moving exactly two color copies simultaneously, while keeping their colors, defines a connected reconfiguration graph on the \(320\) optima, with \(1440\) edges. It is \(9\)-regular, triangle-free, and self-centered of radius and diameter \(5\). The distance-shell cardinalities about **every** optimum are
\[
(1,9,54,159,90,7).
\]
Thus the minimum number of simultaneous color-copy relocations necessary for global mobility is precisely \(2\).

## Assumptions and scope
Vertices and colors are individually named; interchanging the colors gives a different function unless the assignments already agree (which is impossible at the optimum). A copy of color \(i\) at vertex \(v\) is represented by membership of \(v\) in the set \(A_i\). Multiple colors may be hosted on one vertex in the unrestricted definition. Every graph edge has the form \(x\sim x\oplus d\), with \(d\in\{1,2,4,8,15\}\). This is a simple, degree-five, triangle-free strongly regular graph of parameters \((16,5,0,2)\).

For two optima \((A,B)\) and \((C,D)\), define the number of relocated color copies by
\[
\delta((A,B),(C,D))=\tfrac{1}{2}\bigl(|A\mathbin\triangle C|+|B\mathbin\triangle D|\bigr).
\]
A simultaneous \(r\)-token move is legal if \(\delta=r\), both endpoints are optimum functions, and the intervening changes are simultaneous: intermediate partially altered assignments need **not** be feasible. The reconfiguration graph asserted above uses **exactly** \(r=2\), not a threshold of at most two. These are color-preserving token relocations, not arbitrary vertex-label changes.

## Proof
**1. A lower bound.** Write \(A\) and \(B\) for the sets of vertices bearing color 1 and color 2, respectively. If the weight is at most five, one of these sets has at most two elements, so its open neighborhoods cover at most ten vertices. Yet at least eleven vertices are unlabelled, contradicting the rainbow-domination condition. At weight six, neither color can occupy at most two vertices: if it occupies two nonadjacent vertices, their open neighborhoods cover only eight vertices because nonadjacent vertices of \(G\) share two neighbors. If it occupies two adjacent vertices, their open neighborhoods cover ten vertices but include the two occupied vertices, so at most eight unlabelled vertices are covered. There are at least ten unlabelled vertices. Therefore at weight six \(|A|=|B|=3\).

**2. Three-set geometry.** For any three-set \(A=\{u,v,w\}\), the closed neighborhoods have size six and every two closed neighborhoods meet in exactly two vertices. Inclusion-exclusion gives
\[
|N[A]|=12+|N[u]\cap N[v]\cap N[w]|.
\]
If \(A\) induces one edge, the triple intersection is empty, and \(|F(A)|=4\). If it induces a path, its central vertex is the unique element of the triple intersection, and \(|F(A)|=3\). If \(A\) is independent, the triple intersection again has one vertex and \(|F(A)|=3\): to check this last assertion, represent \(G\) equivalently by even-cardinality subsets of a five-set, adjacent when their symmetric difference has size four. Translations by even sets and permutations of the five coordinates act transitively on independent triples. After translating one member to the empty set, the other two are intersecting two-sets, which have exactly one common four-set neighbor. The same model shows transitivity on induced paths (the vertex of degree two can be translated to the empty set and its two neighbors are distinct four-sets).

For the two representative triples in the four-bit model, direct neighborhood calculation gives
\[
F(\{0,1,2\})=\{7,11,12\},\quad F(\{7,11,12\})=\{0,1,2\},
\]
\[
F(\{0,3,5\})=\{6,9,14\},\quad F(\{6,9,14\})=\{0,3,5\}.
\]
The first triple induces a path and the second is independent. The transitivity above proves that \(F\) is an involution interchanging the two types for *every* independent or induced-path triple.

**3. Classification and counting.** In any weight-six function, each vertex of \(F(A)\) must bear color 2, since it lies outside \(A\) and has no color-1 neighbor. Hence \(F(A)\subseteq B\). Since \(|B|=3\) and \(|F(A)|\ge3\), necessarily \(B=F(A)\) and \(A\) induces zero or two edges. In particular \(A\cap B=\varnothing\). Conversely, for either allowed type, the involution identity \(F(B)=A\) implies that all unlabelled vertices have a neighbor in both color classes; hence \((A,F(A))\) is valid.

There are \(16\binom{5}{2}=160\) induced three-vertex paths (unique center and a choice of two of its five neighbors). There are \(40\cdot6=240\) three-sets inducing exactly one edge (choose the edge and one of the six vertices nonadjacent to both endpoints). Because there are \(\binom{16}{3}=560\) triples and no triangles, the number of independent triples is \(560-160-240=160\). Each allowed \(A\) yields one distinct named function: exactly \(320\) in all.

**4. Reconfiguration.** Since \(B=F(A)\) and \(A=F(B)\) uniquely, a move relocating only one color copy while leaving the other entire color class unchanged is impossible. For the exact two-token graph, the accompanying exhaustive checker independently enumerates all \(320\) ordered color-class pairs and all \(\binom{320}{2}\) pair differences. It finds exactly \(1440\) pairs with \(\delta=2\) (each changes one token of each color), with degree nine at every vertex. A complete breadth-first search from each of the \(320\) vertices gives the identical shell tuple \((1,9,54,159,90,7)\). All \(320\) BFS runs reach all vertices, proving connectedness, radius and diameter five. An adjacency test finds no triangle. A separate implementation uses the distinct five-bit even-subset graph representation and independently reproduces every asserted count and distance.

## Verification
Run `g++ -std=c++17 -O2 check_a.cpp -o check_a && ./check_a` and `python3 check_b.py` from the extracted directory. Both are standalone programs, require no network or nonstandard libraries, and assert all intermediate and final values. The first constructs the four-bit Cayley graph, enumerates **all** weight-zero through weight-six assignments by independent color subsets and checks every blank vertex. The second constructs the even-subset graph from scratch, independently repeats the exhaustive weight-bounded check, then constructs all exact two-token edges and runs complete BFS from all \(320\) optima. `CHECKS.txt` gives their verified standard outputs. No higher-weight enumeration is needed to prove minimality or classify optima. Counts of paths are exact finite exhaustive results, not sampled or inferred from a timeout.

## Relationship to prior work
Walikar, Acharya and Shirkol (first public online December 22, 2009) analyze maximum independent sets and ordinary domination in the Clebsch graph, including its standard even-subset representation. Their optimal objects have different constraints from the two-color function and do not determine the present two-rainbow optimizer set or token graph. Kraner Šumenjak, Rall and Tepeh (arXiv:1210.0514, first posted October 1, 2012) give the standard \(k\)-rainbow definition and identify its domination interpretation on Cartesian products, but not this Clebsch classification. Alvarado, Dantas and Rautenbach (arXiv:1507.04901, first posted July 17, 2015) derive general relations between rainbow and weak Roman domination, again without this configuration classification. A separate work on minimum 2-rainbow functions of the Petersen graph has an analogous antineighborhood principle for pairs, but its statement and proof apply to a different graph and do not imply the three-set involution or the \(320\)-state metric here.

## Limitations
The numerical topology of the exact two-token graph (degrees, connectivity, distances, triangle-freeness) is established by two complete finite computations, rather than a symbolic closed-form characterization of all graph distances. The combinatorial optimum classification and impossibility of one-token moves have direct proofs above. No result is asserted for nonminimum weights, other numbers of colors, other graphs, or asynchronous single-token moves through invalid intermediate states. Indexed searches and inspected relevant sources did not identify an earlier equivalent classification; this is not a proof of absolute historical priority.

## References
- H. B. Walikar, B. D. Acharya, S. S. Shirkol, *Designs associated with maximum independent sets of a graph*, Designs, Codes and Cryptography 57 (2010), 91–105, DOI: 10.1007/s10623-009-9351-6; first online December 22, 2009. Full relevant Clebsch section: https://www.researchgate.net/publication/225156199_Designs_associated_with_maximum_independent_sets_of_a_graph
- T. Kraner Šumenjak, D. F. Rall, A. Tepeh, *Rainbow domination in the lexicographic product of graphs*, arXiv:1210.0514, first public posting October 1, 2012. https://arxiv.org/abs/1210.0514
- J. D. Alvarado, S. Dantas, D. Rautenbach, *Relating 2-rainbow domination to weak Roman domination*, arXiv:1507.04901, first public posting July 17, 2015. https://arxiv.org/abs/1507.04901
