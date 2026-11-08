# Five-class connectivity census of three-player binary games

## Finding

Let three players each have two actions, and suppose that every unilateral binary comparison is strict. Identify games when their best-response edge directions coincide, rather than identifying complete payoff or preference tables. There are exactly \(2^{12}=4096\) resulting labeled best-response graphs, all orientations of the three-dimensional cube \(Q_3\). Every orientation is realizable by strict utilities.

For each orientation, form the Boolean vector (weakly acyclic, connected, super-connected, acyclic). The **complete joint census** is:

| Weakly acyclic | Connected | Super-connected | Acyclic | Labeled orientations | Orbits under cube automorphisms |
|---|---|---|---|---:|---:|
| No | No | No | No | 962 | 27 |
| Yes | No | No | Yes | 642 | 22 |
| Yes | Yes | No | No | 888 | 20 |
| Yes | Yes | No | Yes | 1220 | 32 |
| Yes | Yes | Yes | No | 384 | 11 |

Thus exactly \(3134\) have a pure Nash equilibrium, \(2492\) are connected, \(384\) are super-connected, and \(1862\) are acyclic. Exactly \(112\) orientation orbits exist under the full \(48\)-element cube automorphism group. In particular, **every cyclic best-response graph that has a pure Nash equilibrium is connected**, whereas **no acyclic orientation is super-connected** in this three-player binary case. Among graphs with equilibria, the exact connected and super-connected proportions are \(1246/1567\) and \(192/1567\), respectively.

## Assumptions and scope

An action profile is a vertex \(v=(v_1,v_2,v_3)\in\{0,1\}^{3}\). Adjacent profiles differ in one player's action. An edge is directed from the profile with the lower payoff for that deviating player toward the profile with the higher payoff. Strictness therefore orients each of the \(12\) cube edges uniquely. For each player, its four paired comparisons involve disjoint pairs of profiles; any choices of the four directions extend to a strict complete preference order for that player. Hence every one of the \(2^{12}\) orientations occurs and occurs equally often under uniform independent strict ordinal preferences.

A **sink** has no outgoing edges and is a pure Nash equilibrium. A **source** has no incoming edges. A game is **weakly acyclic** if every vertex can reach some sink; it is **connected** if a sink exists and every non-sink reaches every sink; it is **super-connected** if a sink exists and every non-sink reaches every non-source. A graph is **acyclic** if it has no directed cycle. Reachability includes paths of length zero. The full automorphism group acts by permuting the three players and independently swapping their two action labels.

The table counts *best-response orientation types*, not distinct cardinal payoff tables or inequivalent full preference rankings. Its probability statements apply to uniform strict ordinal preferences, not arbitrary distributions of correlated cardinal utilities.

## Proof

**Orientation reduction.** There are \(8\) vertices and \(12\) unordered unilateral-deviation edges. Each of the \(12\) strict payoff comparisons is independent as a formal constraint: it connects a unique pair of profiles for a unique player, and no player has a cycle of prescribed comparisons because its four pairs are disjoint. Assigning each pair utilities \(0\) and \(1\), then perturbing distinct payoffs if desired, realizes all edge directions.

**Structural restriction 1 (equilibrium plus cycle implies connectedness).** Given any sink \(s\), all its three neighbors have forced edges toward it. Every vertex reaches *some* sink: otherwise a terminal strongly connected component in the forward-closed set of vertices unable to reach any sink could not be a singleton, hence would contain a directed cycle. Such a component cannot contain \(s\) or any neighbor of \(s\), while the four remaining vertices induce a star without an undirected cycle. Thus every orientation with a sink is weakly acyclic, recovering the known three-player implication. If the sink is unique, all vertices therefore reach it, so the graph is connected.

If exactly two sinks exist, they cannot be adjacent. If their Hamming distance is \(2\), both lie in one bipartition class of \(Q_3\). After deleting them only two vertices of that class remain, so any directed cycle must be a four-cycle using both; that four-cycle is unique. Its two opposite-class vertices have forced outgoing edges, one to each sink, so every vertex on the cycle reaches both sinks. The other two nonsink vertices are directly adjacent to both sinks and reach both. Thus the graph is connected whenever it contains a cycle.

If instead the two sinks are antipodal (distance \(3\)), the other six vertices induce a six-cycle, which is the only possible remaining undirected cycle. Should that cycle be directed, every vertex on it can reach both sinks: each sink has a neighbor on the cycle, and directed cycling reaches both such neighbors. Finally, any independent set of three or four cube vertices belongs entirely to one bipartition class; removing those sinks leaves too few vertices in that class to form a cycle. These cases exhaust all possible numbers of sinks and prove the restriction.

**Structural restriction 2 (acyclic excludes super-connected).** In any super-connected graph every pair of vertices that are simultaneously non-sources and non-sinks can reach each other. In an acyclic graph there can therefore be at most one such *mixed* vertex. If exactly one vertex \(w\) were mixed, all vertices of the connected graph \(Q_3-w\) would be pure sources or pure sinks. Every edge between them must run from a source to a sink, forcing their source/sink assignment to agree with the two cube parity classes. All three neighbors of \(w\) would consequently be of the same type, making \(w\) itself either a source or a sink, a contradiction. Thus an acyclic super-connected candidate would have no mixed vertices. It would then be a complete bipartition orientation with four sources and four sinks, but every source is adjacent to only three of those four sinks and cannot reach the fourth. This again contradicts super-connectedness.

**Exact finite census.** Fix the lexicographically ordered list of cube edges \((u,v)\), where \(u<v\). Every integer \(b\) from \(0\) to \(4095\) selects the direction on edge \(j\) by bit \(j\) of \(b\). The accompanying `verify.py` checks, for every integer, the sink/source sets, directed reachability and all four predicates; it accumulates the five rows shown above. A separately implemented reverse-target reachability algorithm checks both connectedness predicates for every orientation, and Kahn's topological sorting algorithm independently checks every acyclicity verdict. There are no samples or unvisited orientation types.

For the orbit counts, each of the \(2^3\cdot3!=48\) cube automorphisms induces an edge-direction permutation. The program selects each orbit's least integer representative and verifies constant class labels across its members. It independently computes the Burnside fixed-point sum \(5376\), giving \(5376/48=112\) orbits and the class-specific counts in the table.

There is also an independent combinatorial check on the Nash-equilibrium count. The cube's independence polynomial is \(1+8z+16z^2+8z^3+2z^4\). An independent \(j\)-vertex set can simultaneously be a sink set in exactly \(2^{12-3j}\) orientations, because its \(3j\) incident edges have prescribed directions. Hence the sums of \(\binom{Z}{j}\), over all orientations and with \(Z\) the number of sinks, are \(4096,1024,64,2\) for \(j=1,2,3,4\). Inverting these equations yields the exact sink-frequency distribution \((962,2232,844,56,2)\) for \(Z=0,1,2,3,4\), independently confirming \(3134\) orientations with a Nash equilibrium.

## Verification

Run `python3 verify.py` from a directory containing the standalone program. It exhaustively visits exactly \(4096\) orientations, checks reachability twice by distinct algorithms, checks directed cycles by both depth-first recursion and topological sorting, computes automorphism orbits and their independent Burnside sum, and checks the combinatorial sink moment equations. All assertions passed when the embedded program was extracted and executed. The source code itself is the complete finite certificate and uses only the Python standard library.

## Relationship to prior work

Johnston, Savery, Scott and Tarbush introduce the connected and super-connected classes, establish asymptotic results for generic games, and report random-sample percentages for small player counts (their Appendix H). Their available primary text does not state this exact five-class \(Q_3\) table or the joint symmetry-orbit census. Fabrikant, Jaggard and Schapira prove the *already known* fact that every strict \(2\times2\times2\) game with a pure Nash equilibrium is weakly acyclic (Lemma 5). That fact is credited rather than presented as new. General acyclic-orientation and unique-sink-orientation enumeration are distinct graph-theoretic lines of work; neither a marginal acyclic count nor a count of unique-sink orientations alone establishes this joint table.

## Limitations

The census is finite and limited to strict three-player two-action best-response orientations. It does not infer the same logical exclusions or class probabilities for four or more players, non-generic games, or games with three or more actions. The explicit exact counts are reproducible and the two structural exclusions are proved for \(Q_3\), but the literature comparison cannot guarantee publication priority against unindexed equivalent orientation tables. No independent external audit has been performed.

## References

- Tom Johnston, Michael Savery, Alex Scott and Bassel Tarbush, *Game Connectivity and Adaptive Dynamics*, arXiv:2309.10609, first posted September 19, 2023; especially Sections 2–4 and Appendix H. https://arxiv.org/abs/2309.10609 and https://arxiv.org/html/2309.10609v6.
- Alex Fabrikant, Aaron D. Jaggard and Michael Schapira, *On the Structure of Weakly Acyclic Games*, 2013, Lemma 5. https://www.cs.yale.edu/homes/schapira/weakly-acyclic-full.pdf.
- David D. Gebhard and Bruce E. Sagan, *Sinks in Acyclic Orientations of Graphs*, 1999, for general context on orientation sink enumeration. https://arxiv.org/abs/math/9907078.
