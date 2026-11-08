# Antipodal-pair classification and sharp relocation metrics for paired domination on the icosahedron

## Finding
Let \(I\) be the ordinary 12-vertex icosahedral graph. A set \(S\) is *paired-dominating* if every vertex belongs to or has a neighbor in \(S\), and the induced graph \(I[S]\) admits a perfect matching. Then the paired-domination number is \(\gamma_{\mathrm{pr}}(I)=4\), and the 135 minimum paired-dominating sets are exactly
\[
\bigl\{\{u,\bar u,v,w\}:u\in V(I),\ v\in N(u),\ w\in N(\bar u)\bigr\},
\]
where \(\bar u\) is the unique vertex at distance three from \(u\); duplicate sets are removed. Precisely 15 minima contain two antipodal pairs. The other 120 contain one, with 60 inducing two edges and 60 inducing three edges.

Form a token-slide graph \(\mathcal{T}\) and token-jump graph \(\mathcal{J}\) whose vertices are these 135 four-sets; two states are adjacent if one selected vertex is replaced by one unselected vertex, maintaining paired domination. In \(\mathcal{T}\) the replacement vertices must be adjacent in \(I\), whereas in \(\mathcal{J}\) they may be arbitrary. Both reconfiguration graphs are connected and self-centered:
\[
|E(\mathcal{T})|=360,\quad \operatorname{rad}(\mathcal{T})=\operatorname{diam}(\mathcal{T})=6,
\]
\[
|E(\mathcal{J})|=720,\quad \operatorname{rad}(\mathcal{J})=\operatorname{diam}(\mathcal{J})=4.
\]
In the three state classes (one antipodal pair/two induced edges; one pair/three edges; two pairs), the token-slide degrees are respectively 6, 4, 8 and the token-jump degrees 10, 10, 16.

## Assumptions and scope
The graph is the ordinary skeleton of a regular icosahedron, *not* a subdivided or icosahedral-hexagonal network. The vertex set is \(\{0,1,\dots,11\}\), with two poles \(0,11\), upper pentagon \(u_i=1+i\), and lower pentagon \(\ell_i=6+i\), where \(i\) is read modulo five. Its 30 edges are exactly
\[
0u_i,\quad 11\ell_i,\quad u_i u_{i+1},\quad \ell_i\ell_{i+1},\quad u_i\ell_i,\quad u_i\ell_{i-1}
\quad (i\in\mathbb Z/5\mathbb Z).
\]
Each \(S\) is an *unordered* vertex subset; each reconfiguration transition is undirected and counted once. Distances, radii and diameters are in the reconfiguration graphs, not in the host graph. No assertion is made for other icosahedral subdivisions or graph families.

## Proof
**Minimum size.** A paired-dominating set has positive even cardinality. Every host edge \(xy\) has closed-neighborhood union of size eight, because \(x,y\) have exactly two common neighbors and both lie in each other's closed neighborhoods. Hence no two-vertex paired-dominating set exists. The construction below provides four-vertex examples.

**Antipodal geometry and construction.** The host diameter is three, with exactly six antipodal pairs \(\{u,\bar u\}\). For each such pair the two closed neighborhoods \(N[u]\) and \(N[\bar u]\) are disjoint six-sets whose union is the entire host. Consequently each set \(\{u,\bar u,v,w\}\) with \(v\in N(u)\) and \(w\in N(\bar u)\) dominates, and its induced subgraph has the matching \(uv,\bar u w\).

**Exhaustiveness.** Conversely, any four-vertex paired-dominating set consists of the endpoints of two disjoint edges. The following complete 30-edge test rules out the absence of an antipodal pair. For each of the 30 edges \(ab\), inspect all 21 edges \(cd\) disjoint from it. Test domination of the four-vertex union using the twelve explicitly defined closed neighborhoods. Exactly nine disjoint edges \(cd\) pass, and every successful union contains an antipodal pair. This finite lemma is independently checkable by the bounded loops in `check_ring.py`; it is not a probabilistic statement or inference from samples. For illustration, for \(ab=01\), the four vertices not dominated by \(\{0,1\}\) are \(\{7,8,9,11\}\); the successful disjoint second edges are
\[
(3,8),(4,8),(6,11),(7,8),(7,11),(8,9),(8,11),(9,11),(10,11).
\]
Each contains either \(8=\bar1\) or \(11=\bar0\). The same finite predicate is exhaustively checked for each of the other 29 edges, without requiring an unverified symmetry assumption. A matching on a successful four-set must match the antipodal endpoints to the other two vertices, one on either side; hence every minimum set belongs to the displayed family.

**Counting and internal structure.** For each of six antipodal pairs there are \(5\cdot5=25\) ordered choices of neighbors at opposite ends. Exactly five choices also yield another antipodal pair; each such four-set is double-counted, once for each of its two opposite pairs. Thus the number of distinct configurations is \(6\cdot25-\binom62=135\). The 15 double-pair states induce two independent edges. Fixing an antipodal pair, the 25 neighbor choices split into ten adjacent cross-neighbor pairs, ten nonadjacent cross-neighbor pairs, and five opposite cross-neighbor pairs; the first ten give three induced edges and the other ten one-pair configurations with two. Each of these classes occurs six times, proving the counts \(60,60,15\).

**Reconfiguration and sharp distances.** Each of the 135 masks is tested against every one-vertex replacement, of which there are \(4(12-4)=32\) possible directed proposals per state, retaining precisely the proposals that yield another one of the 135 states. The token-slide subset also checks the replaced and inserted vertices are adjacent in the host. This exhaustive finite calculation yields degree distributions \(\{4:60,6:60,8:15\}\) and \(\{10:120,16:15\}\), respectively, so the undirected edge counts are \((60\cdot4+60\cdot6+15\cdot8)/2=360\) and \((120\cdot10+15\cdot16)/2=720\). Breadth-first search from **all 135** states in each graph reaches all states and finds maximum distance exactly six (slide) or four (jump) from **every** starting state. This establishes connectivity and sharp equalities of radius and diameter. The two explicit, independent implementations described below reconstruct the claims from the host graph rather than relying on imported state lists.

## Verification
`check_ring.py` uses a modular-pentagon adjacency construction, enumerates all \(\binom{12}{2}=66\) potential two-sets and all \(\binom{12}{4}=495\) potential four-sets, checks opposite-neighborhood partitions, verifies all 30 edge-completion cases, classifies all minima, and performs all-pairs breadth-first searches on both relocation graphs. Run `python3 check_ring.py` with a standard-library Python 3 interpreter.

`check_coordinates.cpp` independently constructs the regular icosahedron using the twelve Euclidean coordinates \((0,\pm1,\pm\varphi)\), \((\pm1,\pm\varphi,0)\), \((\pm\varphi,0,\pm1)\), where \(\varphi=(1+\sqrt5)/2\), joining pairs at squared distance four. It enumerates all 4096 vertex masks, tests three possible perfect matchings of each four-set, builds both transition graphs and runs breadth-first search from each state. Compile with `g++ -std=c++17 -O2 check_coordinates.cpp -o check_coordinates` and execute `./check_coordinates`. The textual outputs `check_ring.out` and `check_coordinates.out` record the executions. Neither program requires a third-party mathematical library. The geometric and cyclic constructions agree on the properties reported above.

## Relationship to prior work
Haynes and Slater introduced paired domination, including the induced-perfect-matching condition [1]; the new claim is not this definition or a general domination-number bound. Teshima's accessible dissertation, Chapter 2, studies the token-slide graph of minimum paired-dominating sets and proves that every finite graph is realizable as such a relocation graph for a specially constructed host [2]. It does not classify the unmodified icosahedral host, its antipodal-pair minimum configurations, or its jump and slide distances. Carević studies subdivided icosahedral-hexagonal networks with ordinary domination [3], rather than paired domination of the twelve-vertex skeleton. Prior metric-basis relocation results on the same icosahedral host likewise involve a different admissibility condition and different state space. None of these cited results implies the exact classification and relocation metrics above.

## Limitations
This theorem is specific to the twelve-vertex graph, and the reconfiguration distance claims are finite exhaustive facts, not closed formulas for an infinite family. The complete structural census has a short geometric count, but the all-pairs relocation-distance equalities use reproducible exhaustive verification. Search of indexed literature and mathematical research records cannot exclude unindexed earlier calculations; no claim of exhaustive historical priority or independent formal certification is made. The publisher page for [1] exposed its bibliographic record and abstract, not full text; its direct contribution here is only the foundational definition. No external independent audit has been conducted.

## References
[1] T. W. Haynes and P. J. Slater, "Paired-domination in graphs," *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F. First published 1998-12-07.

[2] L. E. Teshima, *The i-Graph and Other Variations on the \(\gamma\)-Graph*, PhD thesis, University of Victoria, 2022, Chapter 2, especially Theorem 2.2. Full text: https://dspace.library.uvic.ca/server/api/core/bitstreams/629149d6-8ad6-4692-aa43-8fa12718ee55/content.

[3] M. Mihajlov Carević, "Dominating Number on Icosahedral-Hexagonal Network," *Mathematical Problems in Engineering* (2021), article 6663389. DOI: 10.1155/2021/6663389.
