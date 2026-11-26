# The sharp six-cycle matching-flip threshold and exact metric on the icosahedral graph

## Finding

Let \(I\) be the twelve-vertex icosahedral graph, and let \(\mathcal P(I)\) denote its set of perfect matchings. For \(L\ge 4\), define \(R_L(I)\) to have vertex set \(\mathcal P(I)\), with two distinct matchings adjacent exactly when their symmetric difference is a **single** alternating simple cycle of length at most \(L\). All cycles are in \(I\), and a flip replaces the selected alternating half by the other half.

The following is an exact finite classification:

1. There are \(125\) perfect matchings. The four-cycle exchange graph \(R_4(I)\) has \(300\) edges and precisely six connected components: one of size \(120\) and five isolated configurations. Its nonisolated degrees occur with multiplicities \(20\) of degree \(3\), \(60\) of degree \(5\), and \(40\) of degree \(6\). The five isolated perfect matchings are pairwise edge-disjoint and partition all \(30\) graph edges.
2. There are \(580\) distinct six-cycle exchanges (not four-cycle exchanges). Allowing cycles of length six connects all \(125\) perfect matchings, with exactly \(880\) exchange edges. Thus the **minimum even cycle-length cutoff giving connectivity is six**.
3. The connected graph \(R_6(I)\) is self-centered: \(\operatorname{rad}R_6(I)=\operatorname{diam}R_6(I)=3\). Its degree polynomial is
\[
5t^8+20t^{11}+30t^{14}+60t^{15}+10t^{18}.
\]
The unordered configuration-pair counts at distances one, two and three are respectively \((880,4250,2620)\). In particular every distinct pair of the five four-cycle-frozen matchings lies at distance exactly two in \(R_6(I)\).

The existence of a symmetrical five-factor edge partition of the icosahedron, and the five special cubic perfect matchings underlying that classical structure, are already in the literature. The contribution asserted here is the **bounded-alternating-cycle reconfiguration classification** and its exact transition metric, not discovery of that partition or of perfect-matchings themselves.

## Assumptions and scope

All graphs are finite, undirected and simple. Take vertices \(N,S,U_i,L_i\) for \(i\in\mathbb Z/5\mathbb Z\), and include precisely the edges
\[
NU_i,\quad SL_i,\quad U_iU_{i+1},\quad L_iL_{i+1},\quad U_iL_i,\quad U_iL_{i-1}
\qquad(i\bmod 5).
\]
This has twelve vertices, thirty edges and degree five at each vertex; it is the standard pentagonal-ring realization of the icosahedral graph. A perfect matching is an unordered six-element edge set covering each vertex once. The notation \(R_4\) or \(R_6\) refers only to the **length bound on one alternating-cycle flip**, never to a sequence of arbitrary simultaneous operations. The cycle must be a single connected cycle; replacing edges on several disjoint cycles in one move is not permitted.

## Proof

This is an exact finite proof by a complete, self-contained exhaustive construction. Both deterministic checking programs are part of the accompanying evidence. The logical completeness arguments are as follows.

**Exhaustion of matchings.** For any available vertex subset \(W\), let \(\mathcal M(W)\) be the set of perfect matchings in the induced graph on \(W\). Set \(\mathcal M(\varnothing)=\{\varnothing\}\), and, for \(W\neq\varnothing\) with least vertex \(v\), generate exactly
\[
\mathcal M(W)=\bigcup_{u\in N(v)\cap W}
\bigl\{\{u,v\}\cup Q:Q\in\mathcal M(W\setminus\{u,v\})\bigr\}.
\]
Any perfect matching must cover \(v\) through exactly one such edge, so induction proves both completeness and uniqueness. Applying this recurrence to the stated twelve vertices gives the explicitly replayed count \(125\).

**Exact flip predicate.** For two distinct perfect matchings \(M,Q\), their symmetric difference is a disjoint union of alternating even cycles. It is a legal length-four (respectively length-six) flip precisely if it has that length and is one simple cycle. On a simple graph, every alternating cycle has length at least four; thus, for total difference size four or six, there can be at most one component. The first program enumerates all \(\binom{125}{2}=7750\) unordered pairs and verifies this condition using endpoint incidence counts. The second program independently enumerates all actual simple four- and six-cycles and, for every matching, checks alternating occupancy before toggling. They give the same \(300\) and \(580\) exchange edges. This avoids treating a disconnected symmetric difference as a single cycle.

**Exact components, frozen states and metric.** The first program builds the adjacency sets from the checked matching pairs. A complete graph traversal yields component sizes \((120,1,1,1,1,1)\) for length four and \((125)\) for lengths at most six. Exactly five four-cycle-isolated matchings occur; their six-edge sets have pairwise zero intersection and every one of the thirty graph edges occurs in exactly one of them. Degree counting gives the stated degree polynomial, and breadth-first search from **each** of the \(125\) configurations gives eccentricity three throughout. Counting unordered pairs of the calculated distances yields \((880,4250,2620)\), whose sum is \(7750\). The second, independent dual-graph/cycle-toggle checker reproduces every one of these tests and the pairwise distance-two property of the frozen configurations.

Since every cycle flip has even length at least four, the disconnectedness at four and connectivity at six prove the minimum cycle-length cutoff. All computations use exact integer sets and exhaustive finite loops, not samples, estimates or numerical tolerances.

## Verification

Execute both included files with Python 3 and no external packages:

```sh
python code/check_primal.py
python code/check_dual.py
```

The first program constructs the two-pentagon graph above and tests perfect-matching symmetric differences. It prints `ICOSAHEDRAL_PRIMAL_PAIR_DIFFERENCES_PASS` only after its assertions succeed. The second builds the dodecahedral graph \(GP(10,2)\), constructs the twelve faces of length five and their planar-dual adjacency, generates its perfect matchings, directly toggles all alternating four- and six-cycles, and prints `ICOSAHEDRAL_DODECAHEDRAL_DUAL_CYCLE_TOGGLES_PASS` only after its independent tests succeed. The pentagonal-face dual is an icosahedral graph. Both programs were executed from the actual packaged source contents and returned success.

The dual checker also finds exactly thirty simple four-cycles and \(240\) simple six-cycles in the icosahedron, with cycles identified up to starting point and reversal; not every cycle is alternating for every matching. These are distinct from the \(300\) and \(580\) edges of the matching reconfiguration graph.

## Relationship to prior work

Pisanski and Servatius discuss the five special cubic perfect matchings of the icosahedron and their edge partition (chapter 3). Wedd presents a highly symmetric five-edge-colouring. These precedents cover the **existence of the classical partition**, but not the number of four- or six-cycle switches, components, threshold or full shortest-path metric established here. Van Cleemput and Zamfirescu determine icosahedral **whole 1-factorization** Kempe-equivalence classes; their state space has 1-factorizations as vertices, not individual perfect matchings. The latter distinction is essential: their two Kempe classes do not imply either six isolated components under individual four-flips or connectivity under individual six-flips.

Bonamy et al. study four-cycle perfect-matching reconfiguration in general graph classes. Ito et al. consider arbitrary-length alternating cycles; the unrestricted matching-polytope adjacency model does not imply the sharp **six-cycle** cutoff or these exact finite metrics. The known cardinality of perfect matchings is not claimed as new.

## Limitations

The result is an exhaustive theorem for one fixed natural graph, not a statement about larger icosahedral-like graph families. It gives no efficient algorithmic bounds for general inputs. The account in *Configurations from a Graphical Viewpoint* is directly pertinent and its indexed geometric claims were compared, but complete publisher full-text access was not obtained, leaving residual risk of a previously unstated equivalent reconfiguration calculation. Similarly, a specialized historical table of switch-distance statistics could exist under alternate terminology. No independent scholarly verification has been performed.

## References

- Pisanski and Servatius (2012), *Configurations from a Graphical Viewpoint, chapter 3, published 22 September 2012, DOI 10.1007/978-0-8176-8364-1; includes the five cubic matchings and their edge partition.* https://link.springer.com/book/10.1007/978-0-8176-8364-1
- Van Cleemput and Zamfirescu (2020), *Hamiltonian cycles and 1-factors in 5-regular graphs, Proposition 3 and appendix; exact icosahedral 1-factorizations and their Kempe-equivalence classes.* https://arxiv.org/pdf/2008.03173
- Bonamy et al. (2019), *The Perfect Matching Reconfiguration Problem; general four-cycle-flip model and complexity theorems.* https://arxiv.org/pdf/1904.06184
- Ito et al. (2019), *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles; unrestricted single-alternating-cycle changes.* https://arxiv.org/pdf/1907.01700
- Wedd (undated), *Edge-5-colourings of the Icosahedron; documents the known highly symmetric five-class edge colouring.* https://weddslist.com/miscmaths/icos/
