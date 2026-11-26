# Corner-rooted general-position facets and the Blocker-first value on rectangular grids

## Finding

**Theorem.** For integers \(m,n\ge2\), consider the rectangular grid \(G_{m,n}=P_m\square P_n\). In the Builder–Blocker general-position game of Klavžar–Tian–Tuite, Builder maximizes and Blocker minimizes the size of the terminal general-position vertex set. The two optimal-play lengths satisfy

\[
\operatorname{gp}_{\rm g}(G_{m,n})=2,\qquad
\operatorname{gp}'_{\rm g}(G_{m,n})=
\begin{cases}
2,&m=n=2,\\
3,&\text{otherwise}.
\end{cases}
\]

Here the unprimed value refers to Builder moving first; the primed value refers to Blocker moving first. The unprimed equality is previously known for all connected bipartite graphs; the substantive game conclusion is the **exact primed value for every rectangular grid**.

The theorem also gives an exact structural certificate: fixing any corner \(o\) of \(G_{m,n}\), every inclusion-maximal general-position set containing \(o\) has either two or three vertices. Exactly three have size two (the two corner-neighbor pairs and the pair with the opposite corner); exactly

\[
T_{m,n}=\binom{m}{2}\binom{n}{2}-(m-1)(n-1)
\]

have size three. Hence the number of maximal general-position sets through each corner is \(3+T_{m,n}\), and for every non-square-four-cycle grid \(T_{m,n}\ge1\).

## Assumptions and scope

All graphs are finite, simple and undirected. Vertices of \(G_{m,n}\) are lattice pairs \((i,j)\) with \(0\le i<m\) and \(0\le j<n\); edges join pairs at Manhattan distance one. The graph distance is

\[
d((i,j),(k,\ell))=|i-k|+|j-\ell|.
\]

A vertex set is in **general position** if no three distinct selected vertices lie on a common geodesic. A move consists of adding one previously unselected vertex while preserving this condition. The game ends when no legal move exists; Builder maximizes the terminal cardinality and Blocker minimizes it, with perfect play. A general-position set is inclusion-maximal if no further vertex can be added while retaining general position. In particular, a legal triple is *not* presumed maximal without proof.

## Proof

**1. The corner-triple criterion.** By reflection, fix \(o=(0,0)\). For distinct noncorner vertices \(p=(i,j)\) and \(q=(k,\ell)\), the triple \(\{o,p,q\}\) is in general position precisely when \(p,q\) are strictly incomparable under coordinatewise order—one has a smaller first coordinate and a larger second coordinate—and neither \(p\) nor \(q\) occupies a different positive coordinate axis (the excluded pair \(\{(0,b),(a,0)\}\) for \(a,b\ge1\)). Indeed, if the coordinates are comparable, the smaller point lies on an \(o\)-to-larger shortest path. If the points lie on opposite axes, \(o\) lies on a shortest path joining them. Conversely, when they are incomparable and not the excluded axis pair, none of the three points has both coordinates between those of the other two, so no point lies on their geodesic.

Every incomparable unordered pair uniquely comprises the antitone diagonal of a subrectangle: choose two distinct first coordinates and two distinct second coordinates. This gives \(\binom{m}{2}\binom{n}{2}\) choices. Exactly \((m-1)(n-1)\) choices have the forbidden pair on the two positive axes. Therefore exactly \(T_{m,n}\) general-position triples contain \(o\).

**2. No corner-containing four-set.** Suppose \(\{o,p,q,r\}\) were general position. By Step 1 the three noncorner points would be pairwise strictly incomparable. Sort them in increasing order of first coordinate; their second coordinates must strictly decrease. The middle point is therefore coordinatewise between the outer two and lies on a shortest path joining them, a contradiction. Consequently every general-position triple containing \(o\) is inclusion-maximal.

**3. The three maximal corner pairs.** Each neighbor \(u\) of \(o\) forms a maximal general-position pair with \(o\): in a bipartite graph, the distances of any other vertex from adjacent vertices have opposite parity and differ by exactly one, so the third vertex lies on a geodesic containing \(o,u\). The opposite corner \(w=(m-1,n-1)\) also gives a maximal pair, since every grid vertex is on a shortest \(o\)-to-\(w\) path.

Conversely, let \(v=(i,j)\) be distinct from \(o\), its two neighbors, and \(w\). If \(i=0\), then \(j\ge2\) and \(\{o,v,(1,1)\}\) is a general-position triple. If \(j=0\), then \(i\ge2\) and the same witness works. Otherwise \(i,j\ge1\) and at least one of \(i<m-1\) and \(j<n-1\) holds. In the first case, \(\{o,v,(i+1,0)\}\) is general position; in the second case, \(\{o,v,(0,j+1)\}\) is general position. These are direct applications of Step 1. Thus no other pair through \(o\) is maximal, proving the full corner-rooted maximal-set classification.

**4. Builder-first game.** The grid is connected and bipartite. Whatever Builder's first vertex \(u\), Blocker can play a neighbor \(v\) of \(u\). Any third vertex lies on some shortest path containing \(u,v\), as explained in Step 3. Hence the game ends with precisely two vertices. This reproduces the known bipartite corollary in [1].

**5. Blocker-first game, upper bound.** Blocker starts at any corner \(o\). Steps 2–3 imply every general-position set containing \(o\) has at most three vertices. Therefore the terminal set has size at most three. If \(m=n=2\), then \(G_{2,2}\) is a four-cycle and every three vertices contain a geodesically collinear triple, so its game length is two.

**6. Blocker-first game, matching lower bound.** Suppose \((m,n)\ne(2,2)\). Every grid vertex \(u\) belongs to a contiguous isometric \(2\times3\) (or \(3\times2\)) subgrid. In a \(2\times3\) subgrid with coordinates \((a,b)\in\{0,1\}\times\{0,1,2\}\), the two disjoint triples

\[
X=\{(0,0),(0,2),(1,1)\},\qquad
Y=\{(1,0),(1,2),(0,1)\}
\]

are each in general position, and together cover all six vertices. Since the subgrid is isometric, these triples are also general position in the whole grid. After any opening choice \(u\) of Blocker, Builder chooses another vertex \(v\) of the triple containing \(u\); the remaining vertex of that triple would be a legal third move. Thus \(\{u,v\}\) cannot be terminal, irrespective of Blocker's third move. At least three vertices are selected. Together with the upper bound, this proves the primed formula. \(\square\)

## Verification

The standalone checker `artifacts/verify_grid_game.py` constructs each test graph's actual edges and derives its distance matrix by breadth-first search. It builds all forbidden collinear triples from the distance equality; recursively solves the two perfect-information games by exact minimax over legal configurations without imposing a cardinality cutoff; and for each of the four corners independently counts all general-position triples, lists maximal pairs, and checks that no corner-containing triple can extend. The checker verifies 18 grids with dimensions \(2\le m\le5\), \(m\le n\le6\), together with four longer grids. It evaluates 20,504 minimax states and 72 corner classifications. Output is embedded at `artifacts/verify_grid_game_output.txt` and ends with `VERIFICATION_OK graph_cases=18 total_minimax_states=20504 corner_classifications=72`. Reproduce with `python3 artifacts/verify_grid_game.py` using Python 3 and no external dependencies. Finite exhaustive checks do not establish the theorem for arbitrary grid dimensions; Steps 1–6 supply its all-parameter proof.

## Relationship to prior work

[1] Klavžar, Tian and Tuite introduced exactly this alternating optimization game and proved in Corollary 2.4 that Builder-first play on every connected bipartite graph has value two; their Lemma 3.1 and Theorem 3.2 characterize when Blocker-first play has value two. They pose classifying graphs with Blocker-first value three as an explicit problem (Problem 5.7). The present result supplies an entire natural product family and a sharp four-cycle exception. The Builder-first equality is known, not new.

[2] Iršič, Klavžar, Rus and Tuite determined the *unrooted* general-position polynomial of every rectangular grid in their Section 3 (Corollary 3.4 and Theorem 3.5). Those coefficient formulas and known extremal general-position numbers are excluded from the novelty claim: neither their aggregate counts nor the maximum set size determines adversarial optimal terminal lengths or specifies exactly which maximal sets contain a particular corner. The rooted maximal-set structure is established here from geodesic intervals.

[3] The survey distinguishes the last-player-wins achievement/avoidance games studied on grids from the Builder–Blocker optimization game. Results about the former do not determine the latter's terminal cardinality.

[4] The later mutual-visibility Builder–Blocker game is a different feasibility rule; the game models coincide on geodetic graphs, but nontrivial rectangular grids are not geodetic because opposite vertices of a unit square admit multiple shortest paths. Its statements concerning Cartesian grids do not imply this theorem.

## Limitations

The result covers only two-dimensional Cartesian products of two nontrivial paths. No claims are made for higher-dimensional grids, grids with identified boundaries, cylinders, or the mutual-visibility game. No claim of priority or independent verification is made; unindexed equivalent work may exist. The complete rooted facet count applies to a fixed corner, not to arbitrary root vertices. The computational experiments cover finitely many graphs, whereas the proof is uniform.

## References

[1] S. Klavžar, J. Tian, J. Tuite, *Builder-Blocker General Position Games*, arXiv:2310.19949 (first submitted 2023-10-30), https://arxiv.org/abs/2310.19949.

[2] V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, Results in Mathematics 79 (2024), article 110, arXiv:2401.05696, https://doi.org/10.1007/s00025-024-02133-3.

[3] U. S. V. Chandran, S. Klavžar, J. Tuite, *The General Position Problem: A Survey*, arXiv:2501.19385, https://arxiv.org/abs/2501.19385.

[4] V. I. Chenoweth, S. Klavžar, G. Rus, E. Tan, J. Tian and collaborators, *Builder-Blocker Mutual-Visibility Game*, Bulletin of the Malaysian Mathematical Sciences Society 49 (2026), article 89, https://doi.org/10.1007/s40840-026-02083-9.
