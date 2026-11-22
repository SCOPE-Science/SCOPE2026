# Sharp locality costs for optimal feedback-set relocation on the Desargues graph

## Finding

Let \(D\) be the Desargues graph, with its twenty vertices represented by the ten two-subsets and ten three-subsets of a fixed five-element ground set. A two-subset is adjacent to a three-subset when contained in it. A feedback vertex set (decycling set) is a vertex set whose deletion leaves a forest. Its minimum size is six; there are exactly 2,860 minimum sets, a count already established in earlier work.

Form two graphs on these same 2,860 states: \(J\) joins two minimum feedback sets when they differ by replacing one selected vertex with an arbitrary unselected vertex; \(S\) permits the replacement only if the departing and arriving vertices are adjacent in \(D\). The **new result is their exact reconfiguration metric**, not the known optimum size or count.

**Theorem (complete locality metric).** Both \(J\) and \(S\) are connected. The jump graph \(J\) has 27,780 undirected edges, and every one of its 2,860 vertices has eccentricity six; hence its radius and diameter are both six. The slide graph \(S\) has 8,280 undirected edges and has radius nine and diameter ten: exactly 520 vertices have eccentricity nine and the other 2,340 have eccentricity ten. For every pair \(U,V\) of distinct minimum feedback sets,

\[
0\le d_S(U,V)-d_J(U,V)\le 6.
\]

The upper bound is attained by exactly 210 unordered pairs. Every such extremal pair satisfies \(|U\cap V|=4\), \(d_J(U,V)=2\), and \(d_S(U,V)=8\). Of the 4,088,370 unordered distinct-state pairs, the exact numbers with surcharge \(d_S-d_J=0,1,2,3,4,5,6\) are, respectively,

\[
430950,\ 1275090,\ 1482330,\ 741480,\ 148080,\ 10230,\ 210.
\]

The standard Johnson lower bound \(b(U,V)=6-|U\cap V|\) can underestimate a slide distance by as much as six moves, attained on exactly 240 unordered pairs. For unrestricted jumps it underestimates by at most two, attained on exactly 840 unordered pairs.

The all-pairs exact shortest-distance distributions are:

| Distance | Jump pairs | Slide pairs |
| ---: | ---: | ---: |
| 1 | 27,780 | 8,280 |
| 2 | 204,240 | 36,960 |
| 3 | 743,050 | 137,800 |
| 4 | 1,413,660 | 413,910 |
| 5 | 1,276,290 | 846,960 |
| 6 | 423,350 | 1,164,710 |
| 7 | 0 | 958,800 |
| 8 | 0 | 429,960 |
| 9 | 0 | 84,960 |
| 10 | 0 | 6,030 |

## Assumptions and scope

All graphs are finite, simple, undirected, and unweighted. The five underlying symbols are \(0,1,2,3,4\). Number the two-subsets by lexicographic order from vertices \(0\) through \(9\), and the three-subsets likewise from \(10\) through \(19\). A state mask is a twenty-bit nonnegative integer with bit \(i\) equal to one exactly for a *deleted* vertex \(i\). Every reconfiguration step changes exactly one deleted vertex and keeps the deletion set of minimum cardinality six. Slide adjacency is along one original Desargues edge, not along a path and not along an edge of the state-exchange graph. The metric assertion is for this fixed graph; no variable-order extension is asserted.

An equivalent labeled presentation is the generalized Petersen graph \(GP(10,3)\): outer vertices \(u_i\), inner vertices \(v_i\), and edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+3}\), indices modulo ten. An explicit isomorphism from the lexicographically indexed inclusion graph to the order \(u_0,\ldots,u_9,v_0,\ldots,v_9\) is

`[0,2,13,19,11,17,8,4,15,6,1,10,9,3,12,16,14,18,7,5]`.

## Proof

**1. The feasible-state universe is finite and complete.** The Desargues graph has twenty vertices, thirty edges, and degree three. If deleting a set \(X\) of \(k\) vertices leaves a forest with \(c\) components, and if \(e(X)\) is the number of edges induced within \(X\), then edge counting gives

\[
30-3k+e(X)=20-k-c,\qquad 2k=10+e(X)+c.
\]

When the surviving graph is nonempty, \(e(X)\ge0\) and \(c\ge1\); hence \(k\ge6\). Direct inspection of a listed valid size-six state establishes attainment, and complete enumeration of all \(\binom{20}{6}=38,760\) candidates yields 2,860 feasible states. This cardinality is also credited to the earlier published classification. Both bundled verifiers independently regenerate the entire state universe; one additionally tests all size-five candidates.

**2. Every possible legal move is considered.** In each verifier, for each feasible size-six mask \(X\), each selected vertex \(a\in X\), and each unselected vertex \(b\notin X\), form \(Y=(X\setminus\{a\})\cup\{b\}\). Include the undirected jump edge when \(Y\) is again a feasible size-six mask. Keep it as a slide edge exactly when \(ab\in E(D)\). Both programs test the symmetry of the resulting adjacency lists. Therefore the adjacency lists represent the full legal state graphs, not samples or optimally chosen subgraphs.

**3. Exhaustive shortest-path computation proves the metric.** For every one of the 2,860 roots in each state graph, breadth-first search records the minimal path length to every reachable state; BFS correctness follows from expanding vertices in nondecreasing path length in an unweighted graph. Both programs verify that all 2,860 states are reached from every root. The computed row maxima yield the eccentricities; counting adjacency-list degrees yields 27,780 and 8,280 edges after dividing the degree sum by two. For each pair with indices \(i<j\), the programs compare its jump and slide distance, and count the seven surcharge classes displayed above. Each pair is counted once, so the seven values sum to \(\binom{2860}{2}=4,088,370\). The distance-distribution columns each sum to the same total.

**4. The sharpness is witnessed explicitly.** In the inclusion-graph vertex indexing, take feedback-set masks `262175` and `262547`. An unrestricted two-move path has successive masks

`262175, 262423, 262547`.

An eight-slide path has successive masks

`262175, 327695, 65615, 81991, 65863, 327943, 336131, 328067, 262547`.

Each adjacent pair of these masks is checked by the executable move predicates. The complete breadth-first-search distance arrays prove that no shorter route exists. Exhausting every unordered state pair proves the upper bound six and counts precisely 210 pairs where it is sharp. The separate Johnson-lower-bound comparison gives exactly 240 pairs with six moves of slide excess.

**5. Independent representations agree.** `verify_incidence.py` constructs the subset-inclusion graph and checks an explicit edge-preserving isomorphism to \(GP(10,3)\), with a depth-first cycle test on complements. `verify_petersen.py` independently constructs \(GP(10,3)\), tests complement acyclicity with disjoint-set union, generates moves with bitmask manipulation, and independently performs all-source BFS. The expected complete histograms are reproduced by both scripts. The finite certificates require no probabilistic tests or extrapolation to larger graphs.

## Verification

From the directory containing the standalone artifacts, execute `python3 verify_incidence.py` and `python3 verify_petersen.py` using Python 3 (standard library only). They each return a JSON summary of the complete state, transition and shortest-distance census. For comparison, `metrics_incidence.json` and `metrics_petersen.json` contain the respective expected outputs; the second verifier also asserts every reported value against hard-coded independent expected numbers. The explicit mask isomorphism is validated against all thirty edges. These programs check all 2,860 roots and all 4,088,370 unordered pairs, not a sample. Verification duration depends on the host and is not part of the theorem.

## Relationship to prior work

The general study by Bousquet, Hommelsheim, Kobayashi, Mühlenthaler, and Suzuki analyzes feedback-vertex-set reconfiguration under unrestricted one-vertex replacements and proves general connectivity under specific minor restrictions, with counterexamples among cubic graphs. The Desargues graph is nonplanar, three-regular and bipartite, and those general results do not provide its exact jump graph, slide graph, shortest-distance distributions, or locality surcharge. The earlier *2,860 optimal decycling sets of the Desargues graph* gives the exact number and classification of optimum sets, credited here; a set count and orbit classification are not an all-pairs metric. Prior studies on optimal decycling sets of the dodecahedron and of \(GP(7,2)\) concern different base graphs; their diameter values cannot be transferred by either of the two Desargues representations. Prior Desargues zero-forcing-set reconfiguration concerns a different six-versus-eight-sized family with a different feasibility predicate. The earliest dated guiding source for the token-sliding framework is the arXiv posting of *Galactic Token Sliding* on 2022-04-12; the feedback-set paper appeared in 2023.

## Limitations

This is a complete finite, computer-assisted classification for one twenty-vertex graph. BFS certificates yield exact finite facts but do not establish an all-size theorem for generalized Petersen or incidence graphs. The prior public set census is not claimed as new. A potentially relevant full 2023 feedback-set reconfiguration article could not be inspected in full; the available scientific preview, abstracts, section descriptions, theorem statements and relevant comparisons were examined. An older equivalent all-pairs calculation in an unindexed source remains a priority risk. Neither the executable checks nor this description amount to an independent mathematical audit.

## References

1. V. Bartier, N. Bousquet, A. E. Mouawad, *Galactic Token Sliding*, arXiv:2204.05549, first publicly posted 2022-04-12. https://arxiv.org/abs/2204.05549
2. N. Bousquet, F. Hommelsheim, Y. Kobayashi, M. Mühlenthaler, A. Suzuki, *Feedback vertex set reconfiguration in planar graphs*, *Theoretical Computer Science* 979 (2023), article 114188. https://doi.org/10.1016/j.tcs.2023.114188
3. *The 2,860 optimal decycling sets of the Desargues graph*, publicly available exact classification (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-the-2-860-optimal-decycling-sets-of-the-desargues-graph--3f38acb4cf34
4. E. Wei and Y. Li, *Decycling Number and Upper-Embeddibility of Generalized Petersen Graphs*, *Acta Mathematica Sinica, Chinese Series* 56 (2013), 211–216. https://doi.org/10.12386/A2013sxxb0022
5. L. Gao, X. Xu, J. Wang, D. Zhu, Y. Yang, *The decycling number of generalized Petersen graphs*, *Discrete Applied Mathematics* 181 (2015), 297–300. https://doi.org/10.1016/j.dam.2014.09.005
