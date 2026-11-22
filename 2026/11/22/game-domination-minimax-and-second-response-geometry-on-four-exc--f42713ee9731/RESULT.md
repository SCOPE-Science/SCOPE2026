# Game-domination minimax and second-response geometry on four exceptional cubic graphs of girth six

## Finding

In the ordinary domination game, Dominator (D) minimizes and Staller (S) maximizes the final number of chosen vertices, with each move required to dominate at least one vertex not previously dominated. Let \(\gamma_g(G)\) be the number of moves under optimal D-first play and \(\gamma'_g(G)\) the number under optimal S-first play. For the four exceptional cubic symmetric girth-six graphs listed below, both exact values are as follows.

| Graph | Vertices | \(\gamma_g\) | \(\gamma'_g\) |
|---|---:|---:|---:|
| Heawood | 14 | 7 | 6 |
| Möbius–Kantor | 16 | 7 | 6 |
| Pappus | 18 | 8 | 7 |
| Desargues | 20 | 9 | 9 |

Thus the S-first game is strictly shorter for the first three graphs, but not for Desargues. More sharply, the *entire optimal second-response geometry* is classified below. Fix any initial vertex \(r\), and suppose that the second player selects \(w\). Each table entry \(d:c\mapsto t\) means \(c\) legal replies at graph distance \(d=d_G(r,w)\) result in exactly \(t\) total moves when the remaining game is optimal. No first-vertex choice changes these tables.

When D plays first, the second move is by S:

| Graph | Exact second-reply outcomes by distance | Optimal S replies |
|---|---|---:|
| Heawood | \(d=1:3\to7;\ d=2:6\to5;\ d=3:4\to5\) | 3 |
| Möbius–Kantor | \(d=1:3\to7;\ d=2:6\to7;\ d=3:3\to7,2\to5;\ d=4:1\to5\) | 12 |
| Pappus | \(d=1:3\to8;\ d=2:6\to7;\ d=3:6\to7;\ d=4:2\to7\) | 3 |
| Desargues | \(d=1:3\to9;\ d=2:6\to8;\ d=3:6\to8;\ d=4:3\to8;\ d=5:1\to9\) | 4 |

When S plays first, the second move is by D:

| Graph | Exact second-reply outcomes by distance | Optimal D replies |
|---|---|---:|
| Heawood | \(d=1:3\to6;\ d=2:6\to6;\ d=3:4\to6\) | 13 |
| Möbius–Kantor | \(d=1:3\to7;\ d=2:6\to7;\ d=3:3\to7,2\to6;\ d=4:1\to6\) | 3 |
| Pappus | \(d=1:3\to8;\ d=2:6\to8;\ d=3:6\to8;\ d=4:2\to7\) | 2 |
| Desargues | \(d=1:3\to9;\ d=2:6\to9;\ d=3:6\to9;\ d=4:3\to9;\ d=5:1\to9\) | 19 |

In particular, on Pappus, D can achieve the S-first optimum only by choosing one of the two vertices at distance four from S's opening. On Heawood and Desargues every legal second reply to an S opening is optimal. The Möbius–Kantor graph has exactly three optimal D replies, in two distance classes.

## Assumptions and scope

All graphs are finite, simple, undirected, and connected. The graph models are explicitly fixed as follows; all indices and coordinate arithmetic are reduced modulo the indicated modulus.

* **Heawood**: points \(p_i\), lines \(\ell_j\), with \(i,j\in\mathbb Z/7\mathbb Z\); incidence \(p_i\ell_j\) precisely when \(j-i\in\{0,1,3\}\pmod{7}\).
* **Möbius–Kantor**: \(GP(8,3)\), on \(u_i,v_i\) for \(i\in\mathbb Z/8\mathbb Z\); edges \(u_i u_{i+1}\), \(u_i v_i\) and \(v_i v_{i+3}\).
* **Pappus**: point vertices \((x,y)\in\mathbb F_3^2\), and nine line vertices \(x=c\), \(y=c\), \(x+y=c\) for \(c\in\mathbb F_3\); point-line incidence gives the edges.
* **Desargues**: the ten two-subsets and ten three-subsets of a five-element ground set; an edge is present exactly when the two-subset is contained in the three-subset.

The move \(v\) is legal after dominated set \(U\) iff \(N[v]\setminus U\neq\emptyset\). Previously selected vertices cannot make legal repeat moves. The second-reply tables account for **all** legal replies, not only those on one geodesic or from selected orbit representatives.

## Proof

For any dominated set \(U\subseteq V(G)\), define \(F_D(U)\) (respectively \(F_S(U)\)) as the optimal number of *additional* legal moves when D (respectively S) is to move. Set \(F_D(V)=F_S(V)=0\), and otherwise use the complete finite minimax recurrences

\[
F_D(U)=1+\min_{v:\,N[v]\not\subseteq U}F_S(U\cup N[v]),\qquad
F_S(U)=1+\max_{v:\,N[v]\not\subseteq U}F_D(U\cup N[v]).
\]

These identities follow by conditioning on the immediate legal choice, because the dominated set and side to move completely determine all future legal choices and their payoffs. Every transition strictly increases \(|U|\), so descending-cardinality induction determines both functions uniquely for every one of the \(2^{|V|}\) subsets. There is always a legal move from a nonterminal state, since any undominated vertex dominates itself when selected. This is a finite exhaustive proof, not a sampling argument.

The starting values are \(F_D(\varnothing)\) and \(F_S(\varnothing)\). For an opening at \(r\) and legal second reply \(w\), the total move counts (including those two moves) are respectively

\[
2+F_D(N[r]\cup N[w])\quad\text{for D-first play},\qquad
2+F_S(N[r]\cup N[w])\quad\text{for S-first play}.
\]

The attached C++17 checker evaluates all \(2^{14}\), \(2^{16}\), \(2^{18}\) and \(2^{20}\) masks in descending numerical order. Every successor mask is strictly larger than its predecessor, making that order a valid topological evaluation order. The independent Python implementation uses memoized recursion from the starting states, with different graph-generation and state-evaluation code. Both independently generate the stated graphs and calculate the same starting values and every conditional second-response multiplicity. All starting vertices are checked in Python; both programs explicitly check that their D-first and S-first initial values agree at each vertex. As every legal second reply appears once in each distance tally, these finite computations establish each table entry and its optimality assertion.

## Verification

Run `python3 verify_minimax.py` and `g++ -std=c++17 -O2 verify_minimax.cpp -o verify_minimax && ./verify_minimax` from a directory containing the supplied files. The exact machine-readable expected table is in `NUMERICAL_CERTIFICATE.json`. The Python program reports the memoized reachable-state counts 2216, 4948, 11836 and 29812 in graph order. The C++ program checks the recurrence for every dominated-set mask (including unreachable ones) and produces the same values. Each program prints its own success marker after internal assertions pass. Both programs were executed against the embedded sources before delivery.

## Relationship to prior work

Brešar, Klavžar and Rall established the ordinary domination-game definition and the general comparison between D-first and S-first games, including examples where S-first is shorter; those general conclusions do not determine the four explicit graph values or their optimal second replies. Later general bounds by Kinnersley–West–Zamani and Henning–Kinnersley constrain game length but are not exact for these four graphs. The original classification of cubic symmetric graphs of girth six singles out precisely Heawood, Möbius–Kantor, Pappus and Desargues as the four exceptions to a normal-Cayley description, motivating their joint comparison. Closest available indexed mathematical records on graph domination, matching and other games were compared by game rule and implication rather than graph name alone. No inspected source provides this exact four-graph minimax/reply classification. This is an access-limited priority assessment, not a guarantee that an unindexed table does not exist.

## Limitations

The result is a finite four-graph classification backed by complete exact dynamic programming, not a symbolic formula for all cubic symmetric graphs of girth six. The numerical certificate does not establish any statement for graph families outside these four. Public search coverage and access to later full-text tables are imperfect; independent scholarly validation has not been performed. The earliest cited game paper is used as a **foundational source**, not claimed as a new source for these computations.

## References

1. B. Brešar, S. Klavžar and D. F. Rall, *Domination Game and an Imagination Strategy*, SIAM Journal on Discrete Mathematics 24 (2010), 979–991, online 2010-08-17, https://doi.org/10.1137/100786800.
2. W. B. Kinnersley, D. B. West and R. Zamani, *Extremal Problems for Game Domination Number*, SIAM Journal on Discrete Mathematics 27 (2013), 2090–2107, https://doi.org/10.1137/120884742.
3. M. A. Henning and W. B. Kinnersley, *Domination Game: A Proof of the 3/5-Conjecture for Graphs with Minimum Degree at Least Two*, SIAM Journal on Discrete Mathematics 30 (2016), 20–35, https://doi.org/10.1137/140976935.
4. *A Complete Classification of Cubic Symmetric Graphs of Girth 6*, Journal of Combinatorial Theory, Series B (2008), https://doi.org/10.1016/j.jctb.2008.06.001.
