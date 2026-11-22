# Same one-step NOR statistics, different attraction basins on the Shrikhande and rook graphs

## Finding

Let \(R=K_4\square K_4\) be the 16-vertex rook graph and let \(H\) be the Shrikhande graph, both on \(V=\mathbb Z_4^2\), with coordinates ordered by \(i=4x+y\). For a state \(S\subseteq V\), let synchronous *open-neighborhood* NOR act by
\[
 F_G(S)=\{v\in V:N_G(v)\cap S=\varnothing\}.
\]
Thus the vertex's own state is **not** an input unless there is a self-loop; both graphs are simple and loopless. All states are labelled; temporal orbits are counted modulo time shift but not graph automorphisms.

**Exact assertion.** Both systems have precisely \(654\) periodic states among their \(2^{16}=65536\) states. Every orbit enters recurrence in at most one update, and the two systems have **identical distributions of the pair** \((|S|,|F_G(S)|)\), **identical one-step output support and fiber multiplicities**, and identical \(53732\)-state basins for the empty/full primitive two-cycle. Nevertheless the two systems have distinct complete attractor-basin spectra:

| Eventual orbit and its basin size | \(R\): number of temporal orbits | \(H\): number of temporal orbits |
|---|---:|---:|
| Fixed, basin \(1\) | 0 | 32 |
| Fixed, basin \(5\) | 24 | 16 |
| Primitive two-cycle, basin \(2\) | 160 | 144 |
| Primitive two-cycle, basin \(10\) | 18 | 22 |
| Primitive two-cycle, basin \(20\) | 120 | 120 |
| Primitive two-cycle, basin \(549\) | 16 | 16 |
| Primitive two-cycle, basin \(53732\) | 1 | 1 |
| **Total fixed / two-cycle orbits** | **24 / 315** | **48 / 303** |

The fixed-point attraction populations are \(120\) for \(R\) and \(112\) for \(H\). Consequently their fixed-point counts differ by a factor of two, although all one-step input/output *cardinality* statistics and the numbers of recurrent configurations agree. This is an exact example of how a shared bipartite double does not determine temporal recurrence after the input and output copies are identified.

In both graphs the nonzero one-step fiber multiplicities are
\[
 \#\{Y:|F_G^{-1}(Y)|=j\}=\begin{cases}
 457,&j=1,\\ 60,&j=5,\\120,&j=19,\\16,&j=548,\\1,&j=53731,\\0,&\text{otherwise}.
 \end{cases}
\]
The \(654\) output states split into the following eight support/fiber types:

| Output size \(|Y|\) | Number of outputs | Each preimage fiber |
|---:|---:|---:|
| 0 | 1 | 53731 |
| 1 | 16 | 548 |
| 2 | 120 | 19 |
| 3 | 320 | 1 |
| 4 | 60 | 5 |
| 6 | 120 | 1 |
| 10 | 16 | 1 |
| 16 | 1 | 1 |

## Assumptions and scope

The rook adjacency is \((x,y)\sim_R(u,v)\) precisely when the vertices differ and \(x=u\) or \(y=v\). Shrikhande adjacency is \((x,y)\sim_H(u,v)\) when \((u-x,v-y)\pmod 4\in\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}\). Both have degree six. The theorem is about these two **specified finite networks**, not all strongly regular graphs with parameters \((16,6,2,2)\), not a random-graph limit, and not closed-neighborhood NOR. The basin of an orbit consists of *all* initial configurations whose forward iterates eventually visit that orbit, including points on the orbit.

## Proof

**1. First-update entry.** For every undirected graph, \(F_G\) is inclusion-reversing, while \(S\subseteq F_G^2(S)\): every neighbor of a vertex in \(S\) is absent from \(F_G(S)\). Order reversal yields \(F_G^3(S)\subseteq F_G(S)\), and applying the inclusion to \(F_G(S)\) yields the reverse. Thus
\[
 F_G^3=F_G.
\]
Every state in \(\operatorname{im} F_G\) is periodic with least period one or two. Conversely every periodic state is in this image, and every initial state enters it at its first update. For each recurrent orbit \(C\), its exact attraction basin is the disjoint union of the immediate fibers of the points in \(C\), so
\[
 |\mathcal B(C)|=\sum_{Y\in C}|F_G^{-1}(Y)|.
\]

**2. A concrete two-sided bipartite-double isomorphism.** With indices \(0,\ldots,15\), define the permutations \(p\) and \(q\) by their successive values

```
p = [0,1,9,8,2,3,11,10,12,7,15,4,14,5,13,6]
q = [13,4,12,5,15,6,14,7,3,0,8,11,1,2,10,9]
```

Direct substitution into the two displayed adjacency definitions verifies, for *each* \(i,j\in\{0,\ldots,15\}\),
\[
 (i\sim_R j)\quad\Longleftrightarrow\quad(p(i)\sim_H q(j)).
\]
This is a side-preserving isomorphism between the graphs' 32-vertex bipartite doubles; it is not an isomorphism of \(R\) and \(H\), since the two side permutations differ. For any input \(S\), it follows exactly that
\[
 F_H(q(S))=p(F_R(S)).
\]
Hence the complete bivariate size enumerator \(\sum_{S\subseteq V}u^{|S|}v^{|F_G(S)|}\), the output-size histogram, and the multiset of immediate preimage-fiber sizes are the same for the two graphs. This equality is a consequence of the bipartite-double isomorphism, *not* asserted as a newly discovered graph isomorphism.

**3. Exact rook enumerator and its independent cross-check.** Identify a subset \(S\) with four four-bit row masks \(r_0,r_1,r_2,r_3\). Write \(r_i^{\#}\) for the row occupancy, \(c_j^{\#}\) for the number of active cells in column \(j\), and \(s_{ij}\in\{0,1\}\) for the cell state. For each position, the rook-NOR output is one **if and only if**
\[
 r_i^{\#}+c_j^{\#}-2s_{ij}=0.
\]
Therefore enumerating exactly the \(16^4=65536\) quadruples of masks (not sampling) gives the eight support/fiber types displayed above. The complete bivariate input/output population has \(29\) nonzero coefficients, and both explicitly generated graphs agree coefficient by coefficient. The pure Python `verify_structural.py` constructs this rook transformation from row/column occupancies and verifies the two-sided permutation on all inputs. `verify_direct.py` independently constructs local vertex neighborhoods and scans all \(65536\) states in *each* network. Their recorded output contains the complete support/fiber census. All loops are finite and bounded by constants stated in the source; thus this direct enumeration certifies the finite assertions rather than extrapolating from a small sample.

**4. The support pairs and fixed points.** On the \(654\)-state image of *each* graph, the permitted pairs \((|Y|,|F_G(Y)|)\), with their multiplicities, are exactly
\[
 (0,16):1,\ (16,0):1,\ (1,10):16,\ (10,1):16,\ (2,6):120,\ (6,2):120,\ (3,3):320,\ (4,4):60.
\]
The programs check this identity separately from the bivariate state enumeration. A fixed point of NOR is precisely a maximal independent set: every active vertex must have no active neighbor, and every inactive vertex must have an active neighbor. Enumerating the labelled independent dominating sets in the specified adjacency matrices gives \(24\) rook fixed points, all of size four, and \(48\) Shrikhande fixed points, of which \(32\) have size three and \(16\) size four. The same count is checked by a separate combinations-only enumeration in `verify_structural.py` using independence and domination, without calling the NOR orbit evaluator. For the rook graph, its 24 fixed configurations are exactly the \(4!\) permutation-matrix rook placements.

**5. Derive the full orbit and basin table.** The support pairs \(0\leftrightarrow16\), \(1\leftrightarrow10\), and \(2\leftrightarrow6\) necessarily consist of primitive two-cycles. Using the preimage fiber sizes from Step 3, these produce respectively one basin of \(53731+1=53732\), sixteen of \(548+1=549\), and 120 of \(19+1=20\). The \(320\) outputs of size three each have fiber one and pair within size three, except for the 32 Shrikhande fixed points; thus the remaining orbits are \(160\) two-cycles on the rook graph and \(144\) on the Shrikhande graph, each of basin size two. The \(60\) outputs of size four each have fiber five and pair within size four except for \(24\) rook or \(16\) Shrikhande fixed points. They yield respectively \((60-24)/2=18\) and \((60-16)/2=22\) two-cycles, each of basin size ten. The fixed basins have sizes one or five according to their supports. This proves the entire table. Summing basin populations gives exactly \(65536\) separately on each graph, so no attractor or initial state is omitted.

## Verification

Reproduce with `python3 verify_direct.py` and `python3 verify_structural.py` from the same directory. No packages outside the Python standard library are needed. The first script independently checks all \(131072\) labelled input/network pairs, confirms \(F_G^3=F_G\) and enumerates complete basins. The second uses a rook-row occupancy formula, verifies the explicit bipartite-double side permutations on every edge and all inputs, independently identifies maximal independent sets, and checks the output support-pair map. Recorded full output: `direct_output.txt`, `structural_output.txt`. These are exhaustive proofs for the **two finite 16-vertex systems**; they do not imply an unproved all-graph generalization.

## Relationship to prior work

The general NOR period restriction and the fixed-point/maximal-independent-set correspondence are established results and not claimed as new. Aledo, Martinez and Valverde (2015) survey parallel Boolean graph systems and their period restrictions. Aracena, Richard and Salinas (2015 preprint; later journal publication) discuss the all-negative conjunctive fixed-point interpretation. Brouwer's description of the Shrikhande graph records the already-known isomorphism of its bipartite double with that of the \(4\times4\) rook graph. A published *NOR dynamics on rook graphs: rectangles, matchings, and a square-board gap* gives the all-size rook recurrence classification, covering the rook-only periodic-state counts. The present finite comparison adds the specified Shrikhande basin spectrum, the explicit two-sided NOR input/output conjugacy, and the equality of complete one-step statistics despite different recurrent orbit and basin partition counts. Related published Shrikhande/rook comparisons for majority and excitation concern different local maps and do not give the displayed NOR census.

## Limitations

This is a fully finite, graph-pair-specific result: the computation is an exhaustive enumeration and the combinatorial reduction gives an explanation, but no theorem is asserted for arbitrary cospectral pairs or arbitrary graphs with isomorphic bipartite doubles. The bipartite-double isomorphism and abstract NOR periodicity were already known. The accessible literature and published-result comparisons did not expose this exact Shrikhande/rook NOR basin table; unindexed equivalents remain possible. A relevant published rook-graph classification was inspected in full, but its available source metadata does not prove exhaustive historical priority. No independent external mathematical audit has been performed.

## References

1. J. A. Aledo, S. Martinez, and J. C. Valverde, "Parallel Dynamical Systems over Graphs and Related Topics: A Survey," *Journal of Applied Mathematics* (2015), article 594294, first published 2015-03-24. https://doi.org/10.1155/2015/594294
2. J. Aracena, A. Richard, and L. Salinas, "Fixed points in conjunctive networks and maximal independent sets in graph contractions," arXiv:1507.06141, first public 2015-07-22. https://arxiv.org/abs/1507.06141
3. A. E. Brouwer, "Shrikhande," *Distance-Regular Graphs* reference database, https://aeb.win.tue.nl/drg/graphs/Shrikhande.html (describes the preexisting bipartite-double equivalence).
4. "NOR dynamics on rook graphs: rectangles, matchings, and a square-board gap," published research record, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-nor-dynamics-on-rook-graphs-rectangles-matchings-and-a-square-bo--c79fc7919f54
5. "Spectral twins separate under majority dynamics: exact Shrikhande–rook attraction censuses," published research record, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-spectral-twins-separate-under-majority-dynamics-exact-shrikhande--a7ee2eb89698
