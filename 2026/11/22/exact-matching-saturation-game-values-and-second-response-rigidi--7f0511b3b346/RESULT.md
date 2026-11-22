# Exact matching-saturation game values and second-response rigidity on the five Platonic graphs

## Finding
Let two players, Max and Min, alternately select an edge disjoint from all previously selected edges of a fixed graph, until no move remains. Max wants to maximize the size of the terminal maximal matching, and Min wants to minimize it. Write \(g_+(G)\) for the optimal score when Max moves first and \(g_-(G)\) when Min moves first.

**Theorem.** For the one-skeleta of the five regular convex Platonic solids, the game values, ordered as (Max first, Min first), are
\[
\begin{array}{c|cc}
G & g_+(G) & g_-(G)\\\hline
\text{tetrahedron} &2&2\\
\text{cube}&4&4\\
\text{octahedron}&2&3\\
\text{dodecahedron}&8&9\\
\text{icosahedron}&5&6
\end{array}
\]
The octahedral case already follows from the complete-graph-minus-matching construction of Cranston, Kinnersley, O and West, and is included as background to the complete family classification. The distinctive evaluations here are the two dodecahedral–icosahedral dual graphs: in both, Max moving first obtains **one fewer edge** than when Min moves first. On the icosahedron, Min-first play forces a perfect matching of six edges, whereas Max-first optimal play stops at five. On the dodecahedron both values are strictly between the smallest maximal matching size (six) and the ordinary maximum matching size (ten).

**Sharp second-response statement.** Every edge is an equivalent opening. Fix any opening edge. On the icosahedron, there are exactly \(21\) legal second edges. If Max opened, exactly nine second moves (by Min) lead to a five-edge optimal outcome, and twelve lead to six; if Min opened, exactly **one** second move (by Max) yields six, and twenty yield five. On the dodecahedron, there are exactly \(25\) legal second edges. If Max opened, five Min replies yield eight and twenty yield nine; if Min opened, eight Max replies yield nine and seventeen yield eight. Here "yield" means the eventual score when both players play optimally from the remaining position.

## Assumptions and scope
All five graphs are the ordinary simple undirected vertex-edge graphs of the regular convex solids. Vertex labels are arbitrary. Selected edges remain part of a matching, so an edge \(uv\) removes both \(u\) and \(v\) from future play. A position is completely determined by the set \(S\) of unmatched (available) vertices and the identity of the player to move. No passing is allowed, and all moves are made with perfect information. The terminal score is the number of selected edges; the state recurrences below count additional edges, which are added to those already selected. No claim is made for other polyhedra or for the different 2018 vertex-choice matcher game.

A self-contained constructive representation for the five graphs is implemented in `verify_recursive.py`: the tetrahedral graph is \(K_4\); the cubical graph is the binary three-cube; the octahedral graph is \(K_6\) minus the matching \(\{03,14,25\}\); the dodecahedral graph is the generalized Petersen graph \(G(10,2)\), with an outer ten-cycle, ten spokes and step-two inner edges; and the icosahedral graph has two poles, two five-cycles and the two staggered cross-ring neighbors per upper-cycle vertex. `verify_bottomup.cpp` uses separately specified labelled edge lists. Both descriptions give exactly the indicated simple Platonic graphs.

## Proof
For any subset \(S\) of available vertices, define \(U(S)\) and \(L(S)\) to be the optimal numbers of *additional* edges if Max and Min, respectively, move next. Set both values to zero when the induced graph \(G[S]\) has no edges. Otherwise backward induction on \(|S|\) gives the exhaustive recurrences
\[
U(S)=1+\max_{uv\in E(G[S])}L(S\setminus\{u,v\}),
\qquad
L(S)=1+\min_{uv\in E(G[S])}U(S\setminus\{u,v\}).
\]
These recurrences are exact: every legal next move deletes the two incident vertices, and the subsequent player is the opponent. Since the remaining set strictly decreases, induction reaches a terminal position, covering every possible strategy pair without sampling. Thus \(U(V(G))=g_+(G)\) and \(L(V(G))=g_-(G)\).

The independent bottom-up program evaluates both recurrences for **all** \(2^{|V(G)|}\) subsets of each graph, in increasing integer-mask order. Every child mask has fewer set bits and is numerically smaller. For the largest case, the dodecahedron, this is exactly \(2^{20}=1{,}048{,}576\) masks, with no omitted state. It also evaluates the least and greatest possible terminal maximal-matching sizes by replacing both alternating objectives with the same minimization or maximization; the resulting ranges are \((2,2),(3,4),(2,3),(6,10),(5,6)\) in the order displayed in the theorem. The second program independently constructs graph edges using formulas, and evaluates the same minimax values by recursive memoization over reachable masks. Both return the exact theorem table and the response counts.

For the response counts, after a fixed first edge \(ab\) and a second legal edge \(cd\), let \(S=V(G)\setminus\{a,b,c,d\}\). The eventual total is \(2+U(S)\) if Max opened, and \(2+L(S)\) if Min opened. Each program exhausts every second edge after **every** first edge and verifies that the stated histograms are independent of the first edge. This proves the response classifications as well as the main game values. In particular, the unique successful Max reply after a Min opening on the icosahedron is an exact exhaustive result, not a probabilistic claim.

## Verification
The standalone files `verify_recursive.py` and `verify_bottomup.cpp` use only Python's standard library and standard C++17, respectively. Reproduce with:

```sh
python3 verify_recursive.py > recursive.json
g++ -std=c++17 -O2 verify_bottomup.cpp -o verify_bottomup
./verify_bottomup > bottomup.json
python3 -c 'import json; assert json.load(open("recursive.json")) == json.load(open("bottomup.json")); print("PASS")'
```

The precomputed exact summary is in `checks.json`; both independently implemented solvers generated identical parsed JSON for all five graphs, including ordinary matching extremes and second-response histograms. The canonical constructed graphs were additionally checked for isomorphism against established graph generators for the dodecahedron and icosahedron. The C++ exhaustive check and the Python recursive check are finite proofs for the specified five graphs; they do not claim a symbolic theorem about arbitrary graph families.

## Relationship to prior work
Cranston, Kinnersley, O and West introduced these Max-start and Min-start game-matching numbers, proved their difference is at most one, and gave the complete-graph-minus-perfect-matching construction: for six vertices this **already covers the octahedron**. They established broader lower bounds and graph classes, but those general statements do not imply the specific values \((8,9)\) for the dodecahedron and \((5,6)\) for the icosahedron, nor the quantified second-response profiles. Their paper was inspected through the text of Sections 1–5 and checked for the names and defining features of these solids. The cube and tetrahedron entries are elementary and are not claimed as individual discoveries. The novel substantive object in this complete canonical five-graph classification is the pair of simultaneous reverse starting-player inequalities and response rigidity on dual icosahedral graphs.

Subsequent "matcher game" literature uses a different protocol in which Max chooses a vertex and Min then selects a neighbor; it cannot be identified with the alternating-edge-choice game. General saturation-game results likewise need not describe the same fixed host-graph edge process. Searches of relevant mathematical-result records and the indexed literature did not reveal a prior determination of the dodecahedral and icosahedral game values or response profiles, but negative searches alone cannot establish absolute priority.

## Limitations
The statement is restricted to the five finite graphs. The proof is an exact exhaustive dynamic-programming certificate, not a short noncomputational positional strategy classification. The octahedral values are known from the foundational article and included to complete the natural collection. An unindexed or differently named prior calculation of the two dual graph values remains possible. Independent external validation is not claimed.

## References
- D. W. Cranston, W. B. Kinnersley, Suil O, and D. B. West, *Game matching number of graphs*, arXiv:1208.0085, first public version August 1, 2012; Discrete Applied Mathematics 161 (2013), 1828–1836. https://arxiv.org/abs/1208.0085 ; https://doi.org/10.1016/j.dam.2013.03.010
- W. Goddard and M. A. Henning, *The matcher game played in graphs*, Discrete Applied Mathematics 237 (2018), 82–88. https://doi.org/10.1016/j.dam.2017.11.038 (different move protocol)
- *On saturation games*, European Journal of Combinatorics 51 (2016), 315–335. https://doi.org/10.1016/j.ejc.2015.05.017 (different host-game formulation)
