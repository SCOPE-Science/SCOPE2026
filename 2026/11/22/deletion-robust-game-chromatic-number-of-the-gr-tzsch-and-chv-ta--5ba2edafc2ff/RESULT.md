# Deletion-robust game chromatic number of the Grötzsch and Chvátal graphs

## Finding

Let \(G\) be the eleven-vertex Grötzsch graph (the Mycielskian of a pentagon), and let \(H\) be the twelve-vertex Chvátal graph, with the explicit edge constructions below. In the ordinary alternating proper vertex-colouring game, Alice plays first and wins precisely if every vertex is coloured; Bob wins if an incomplete position becomes impossible to extend. Write \(\chi\) for ordinary chromatic number and \(\chi_g\) for game chromatic number.

**For every vertex \(v\in V(G)\) and every vertex \(w\in V(H)\),**
\[
\chi(G-v)=\chi(H-w)=3,\qquad
\chi_g(G-v)=\chi_g(H-w)=4.
\]
Thus all **23** vertex deletions reduce ordinary chromatic number from four to three, yet **none reduces the game chromatic number**. Both original graphs also satisfy \(\chi=\chi_g=4\). The original full-graph value for the Grötzsch graph is a previously published fact, not a new contribution. The contribution is the complete vertex-deletion persistence classification for both classical critical graphs.

| Graph | Vertices | Edges | Original \(\chi\) | Original \(\chi_g\) | Number of one-vertex deletions with \((\chi,\chi_g)=(3,4)\) |
|---|---:|---:|---:|---:|---:|
| Grötzsch | 11 | 20 | 4 | 4 | 11 of 11 |
| Chvátal | 12 | 24 | 4 | 4 | 12 of 12 |

## Assumptions and scope

All graphs are labelled, finite, undirected, and simple. The Grötzsch graph has base vertices \(v_i\) and shadow vertices \(u_i\), for \(i\) modulo five, and an apex \(a\). Its edges are \(v_iv_{i+1}\), \(u_iv_{i-1}\), \(u_iv_{i+1}\), and \(au_i\) for each \(i\). In the checker, label \(v_i\) by \(i\), \(u_i\) by \(i+5\), and the apex by \(10\).

The Chvátal graph has vertex set \(\{0,1,\ldots,11\}\) and the following 24 unordered edges, with each edge listed once:

`(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)`.

For a fixed palette \(\{1,\ldots,k\}\), a move assigns a currently uncoloured vertex an available colour (one absent from its already-coloured neighbours); Alice and Bob alternate such moves, Alice starting. Alice wins if all vertices become coloured, and Bob wins if a vertex remains uncoloured without any legal colour. Both players may choose either a vertex or an allowed colour. No recolouring of already coloured vertices is allowed. These game rules must not be confused with reconfiguration of completed colourings.

## Proof

**Ordinary chromatic assertions.** The two included programs separately construct each graph from the above definitions. Each runs exhaustive recursive proper-colouring search with 2, 3, and 4 colours, varying the graph by removing each possible labelled vertex. For both original graphs, three-colour search fails and four-colour search succeeds. For each of the 23 deletions, two-colour search fails and three-colour search succeeds. Hence the ordinary chromatic assertions, including *equality* to three rather than just three-colourability, follow.

**Exact game recurrence.** For any one of the above finite graphs and palette size \(k\), a partial state is a vector \(s\) with entries \(0,1,\ldots,k\), with zero meaning uncoloured. Only proper partial states are generated. Define \(A_k(s)\) to mean that Alice has a forced win from state \(s\) with the next player determined by the parity of the number of coloured vertices. If every vertex is coloured, \(A_k(s)=\mathrm{true}\). If any uncoloured vertex has all \(k\) colours on its neighbours, \(A_k(s)=\mathrm{false}\), since subsequent legal moves can never restore its missing colours. Otherwise all legal moves \((v,c)\) are explicitly enumerated. At an Alice turn, \(A_k(s)\) is the disjunction over successor values; at a Bob turn it is their conjunction. Each successor colours exactly one new vertex, so induction on the remaining uncoloured count makes this recurrence an exact, terminating minimax proof, with no strategy guess, depth cutoff, or sampling.

Global permutation of colour names preserves legal moves and the winner. In each program, used colours are renamed \(1,2,\ldots\) by first appearance along the fixed vertex order before memoization. This is a genuine permutation symmetry, not a heuristic state merging: two states assigned the same canonical key differ only by a global colour permutation. The C++ implementation encodes its canonical state into three bits per vertex; the Python implementation stores a canonical integer tuple. Both independently generate all legal vertex-colour moves and evaluate the recurrence with short-circuit Boolean rules.

**Complete cases.** For both original graphs, the four-colour recurrence gives an Alice win (and ordinary \(\chi=4\) already excludes any smaller game palette). For each vertex deleted from either graph, the three-colour recurrence returns Bob as the winner and the four-colour recurrence returns Alice as the winner. Since the deleted graphs are exactly three-chromatic, three colours are necessary and four sufficient: \(\chi_g=4\) on all 23 deletions. The exhaustive programs produce a separate result for every vertex index from zero to ten and zero to eleven respectively; no vertex-transitivity assumption is used. This proves the claim.

## Verification

The standalone files `game_color_check.cpp` and `game_color_check.py` reproduce all cases without external data, graph packages, stochastic algorithms, or network calls. Use:

```sh
g++ -std=c++17 -O2 game_color_check.cpp -o game_color_check
./game_color_check
python3 game_color_check.py
```

Each prints 23 deletion lines with `game3=0` and `game4=1` (the Python version spells these as `game3=` and `game4=` as well), checks the original chromatic value, validates every 2-versus-3 ordinary deleted colouring test, and finishes with `ALL CHECKS PASS`. The source code, not terminal logs alone, defines the fully exhaustive search. The implementations construct the graphs independently using respectively an explicit edge-list construction and literal adjacency tuples. Their representations, DFS orders, and memoization storage differ.

The theorem is finite and covers precisely the 11-plus-12 labelled deletions. The exhaustive state recurrence proves their game outcomes, not a conjectured infinite family.

## Relationship to prior work

Krawczyk and Walczak (2015) give the standard colouring-game setup and investigate game chromatic gaps in incomparability graphs; their theorems do not analyse the two graphs or their deletions. Alagammai and Vijayalakshmi (2019), Theorem 2.2, explicitly establish \(\chi_g(\mu(C_n))=4\) for \(n\ge5\), including the **whole Grötzsch graph**. That published statement is credited as known. It does not imply the value after deleting a vertex: game chromatic numbers are governed by adversarial partial colourings, not merely by the finished chromatic number or a full-graph Alice strategy.

A prior exact game result concerns the distinct two-layer graph \(M_2(C_5)\), not \(\mu(C_5)-v\). Published complete-colouring reconfiguration results for the Grötzsch and Chvátal graphs address connectivity of *completed proper colourings* under recolouring, a different operation and quantifier structure from Alice/Bob alternating proper placements. Their counts and components do not determine the minimax winner on any deleted graph. The original Chvátal graph and both graphs' chromatic criticality are also prior background, not claimed as newly discovered.

## Limitations

This is an exact computer-assisted finite result, based on complete minimax enumeration rather than a short symbolic strategy for Bob's 23 three-colour games. It does not prove that all four-chromatic vertex-critical graphs have the property. The independent code checks reduce implementation risk but do not constitute independent scholarly review. Unindexed earlier game-colouring tables or alternative descriptions of vertex-deleted Mycielski/Chvátal graphs may exist; mathematical priority is assessed on accessible sources, not asserted absolutely.

## References

1. T. Krawczyk and B. Walczak, *Asymmetric coloring games on incomparability graphs*, arXiv:1503.04748v1, first submitted 2015-03-16, https://arxiv.org/abs/1503.04748.
2. R. Alagammai and V. Vijayalakshmi, *Game Chromatic Number and Game Chromatic Index of the Mycielski Graphs of Some Families of Graphs*, Applied Mathematics & Information Sciences 13(S1) (2019), 261–265, Theorem 2.2, https://www.naturalspublishing.com/files/published/4d0us4el8te290.pdf.
3. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, Journal of Combinatorial Theory 9 (1970), 93–94, DOI: 10.1016/S0021-9800(70)80057-6.
4. Y. Mou, Q. Sun and C. Zhang, *The game chromatic number of generalized Mycielski graphs of paths and cycles*, arXiv:2609.02283 (2026), a distinct graph family, https://arxiv.org/abs/2609.02283.
