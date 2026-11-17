# Every edge of the asymmetric Frucht graph both creates and destroys majority-consensus initial states

## Finding

Let \(G\) be the twelve-vertex Frucht graph specified below, and let \(F_e\) denote synchronous binary open-neighbor majority with incumbent retention on a tie, on the graph obtained by deleting edge \(e\). Write \(F_\varnothing\) for the original graph. For every one of the eighteen edges \(e\), define the unanimous attraction basin

\[
\mathcal B_e=\{x\in\{0,1\}^{12}:F_e^t(x)\in\{\mathbf0,\mathbf1\}\text{ for some }t\ge0\}.
\]

**Complete finite classification.** The original basin has \(|\mathcal B_\varnothing|=1240\). **Every** edge deletion both adds and removes initial configurations from this basin: \(|\mathcal B_e\setminus\mathcal B_\varnothing|>0\) and \(|\mathcal B_\varnothing\setminus\mathcal B_e|>0\) for all eighteen edges. Eleven deletions increase its cardinality and seven decrease it, with no net-zero case. The range is from \(866\) to \(1478\), attained by deleting \(\{0,6\}\) and \(\{3,9\}\), respectively. Thus there is neither set inclusion nor even a fixed sign for the influence of deleting one edge.

For all nineteen maps, \(F_e^{10}=F_e^8\) on the entire state space. This common cutoff is sharp among the nineteen systems: five deleted-edge systems have configurations of first periodic entry time eight, whereas the unmodified graph has sharp time seven. All periodic orbits have period one or two. Table entries count labelled binary initial configurations, not orbits.

| Deleted edge | Newly unanimous | Lost unanimity | Total unanimous basin | Largest first periodic entry |
|:--|--:|--:|--:|--:|
| none | 0 | 0 | 1240 | 7 |
| \(0,1\) | 90 | 84 | 1246 | 7 |
| \(0,6\) | 60 | 434 | 866 | 8 |
| \(0,7\) | 80 | 94 | 1226 | 6 |
| \(1,2\) | 100 | 248 | 1092 | 7 |
| \(1,7\) | 82 | 62 | 1260 | 7 |
| \(2,3\) | 312 | 258 | 1294 | 8 |
| \(2,8\) | 360 | 132 | 1468 | 5 |
| \(3,4\) | 98 | 80 | 1258 | 8 |
| \(3,9\) | 300 | 62 | 1478 | 6 |
| \(4,5\) | 84 | 382 | 942 | 8 |
| \(4,9\) | 128 | 106 | 1262 | 6 |
| \(5,6\) | 80 | 86 | 1234 | 8 |
| \(5,10\) | 96 | 84 | 1252 | 6 |
| \(6,10\) | 104 | 92 | 1252 | 6 |
| \(7,11\) | 104 | 248 | 1096 | 6 |
| \(8,9\) | 308 | 254 | 1294 | 6 |
| \(8,11\) | 190 | 134 | 1296 | 7 |
| \(10,11\) | 146 | 294 | 1092 | 6 |

There are \(12\) fixed configurations and \(268\) states on primitive temporal two-cycles (\(134\) such cycles) for the original graph. For each deletion, the complete fixed-state count, two-cycle-state count, and first-entry histogram appear in the accompanying machine-readable output.

## Assumptions and scope

The labelled Frucht graph has vertex set \(\{0,1,\ldots,11\}\) and exactly the following eighteen undirected edges:

```
(0,1) (0,6) (0,7) (1,2) (1,7) (2,3) (2,8) (3,4) (3,9)
(4,5) (4,9) (5,6) (5,10) (6,10) (7,11) (8,9) (8,11) (10,11)
```

Every vertex initially has degree three. For a binary configuration \(x\), the simultaneous update at vertex \(v\) is the majority bit among the current neighbors when that majority is strict, and is \(x_v\) when the two neighbor counts tie. The update uses the graph after deletion, so the two exposed endpoints have degree two and use incumbent tie retention. All other vertices remain cubic. Initial states, graph labels, and simultaneous updates are fixed as specified; there is no random sampling assumption. Uniformly random initial configurations only provide an optional probabilistic interpretation through division by \(4096\).

## Proof

**Reduction of the local defect.** On a cubic graph the next bit at \(v\) is \(\operatorname{maj}(x_a,x_b,x_c)\), where \(a,b,c\) are the three neighbors and \(\operatorname{maj}(p,q,r)=(p\wedge q)\vee(p\wedge r)\vee(q\wedge r)\). After deleting edge \(\{u,v\}\), the two remaining neighbors of \(u\) create a tie exactly when their bits disagree; in that case the rule retains \(x_u\). Thus its new bit equals \(\operatorname{maj}(x_u,x_a,x_b)\). The same replacement occurs at \(v\). All other local expressions are unchanged. This equivalence between tie retention and self-substitution is used by the second independent classifier.

**Exhaustion is complete.** There are exactly \(2^{12}=4096\) labelled input configurations for each graph and nineteen graphs, the original and its eighteen distinct labelled single-edge removals. `enumerate_forward.py` explicitly constructs the complete one-step image table and, for *each* initial bit-mask, iterates until the first \(t\ge0\) satisfying \(F_e^{t+2}(x)=F_e^t(x)\). Once this equality occurs, determinism makes it hold at every later time, so \(t\) is exactly the first periodic-entry time. This program checks that the first such \(t\) does not exceed 100, then tabulates its exact value and the eventual unanimous destination. Its returned histograms have zero entries beyond eight, with maximum eight attained on five deletions; hence the identity \(F_e^{10}=F_e^8\) follows for *every* starting configuration. Direct inspection of the time-eight count proves sharpness, not merely an upper bound.

**Independent complete certificate.** `enumerate_functional_graph.py` constructs the same graph from its Hamiltonian LCF encoding, rather than the edge list; a fixed bijective relabelling maps LCF positions to the displayed labels. It then computes the one-step update by the three-input Boolean majority identity above, builds the entire \(4096\)-vertex directed functional graph, removes noncyclic vertices by indegree peeling, checks that every remaining cycle has length one or two, and propagates cycle periods, destinations and exact distances backward along every incoming edge. This algorithm uses neither the forward-trajectory stopping rule nor its majority-count implementation. The resulting nineteen census rows agree **entry-for-entry** with the forward classifier.

**Basin set differences.** For every initial configuration and every deletion, each program tests whether the eventually reached cycle is the all-zero or all-one fixed point. It counts the newly unanimous states \(\mathcal B_e\setminus\mathcal B_\varnothing\), those losing unanimity \(\mathcal B_\varnothing\setminus\mathcal B_e\), and the resulting total. The tabulated integers are the exact results of these finite loops. The smallest new and lost counts over the eighteen edges are respectively \(60\) and \(62\), which proves strict two-sided membership changes for every deletion. The signed cardinality changes are the differences of these exact counts. The original graph's fixed and two-cycle census is obtained independently as part of the same exhaustion.

## Verification

Both self-contained Python 3 programs use only the standard library. Execute `python3 enumerate_forward.py > forward.json` and `python3 enumerate_functional_graph.py > functional.json`; compare the `runs` arrays after decoding JSON. They agree on every entry, including the counts of gained and lost consensus states, exact largest first-periodic-entry times, fixed and two-cycle populations, and full entry histograms. The deposited `forward.json` and `functional.json` are the resulting exact outputs. The forward program uses a defensive 100-step bound; it completed without triggering that bound. No partial enumeration, statistical extrapolation, or external solver is used.

## Relationship to prior work

Benjamini, Chan, O'Donnell, Tamuz and Tan's 2014 preprint defines synchronous binary majority dynamics and investigates consensus on unimodular and random graphs. Kaaser, Mallmann-Trenn and Natale's 2015 preprint defines the same tie-retaining update and studies voting-time bounds and computational hardness. The earlier Goles–Olivos period-two theorem (cited in those papers) guarantees eventual periods at most two, but neither that theorem nor the general voting-time bounds determine the present Frucht graph's exact basins or their signed changes under all eighteen edge deletions. The Frucht graph itself is a classical asymmetric cubic example; its graph-theoretic identity is not new. The full available one-edge majority-defect result for complete bipartite graphs relies on shore-wise count reductions and does not apply to the nonbipartite Frucht graph. The full Frucht matching-complex edge-deletion classification concerns homotopy types of complexes of edge matchings rather than dynamics on binary vertex states; neither result implies the table here.

## Limitations

This is a finite exact classification on one specified twelve-vertex graph and its one-edge deletions; it is not a universal theorem about deleting an edge on arbitrary graphs. The nineteen exact censuses do not imply a general formula for larger asymmetric cubic graphs, and no statistical approximation is involved. The novelty comparison is based on identified relevant preprints, an indexed mathematical-record search and accessible historical descriptions; it cannot certify exhaustive historical priority. Verification is reproducible finite enumeration, not independent mathematical review.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, arXiv:1405.2486, first posted 2014-05-11. https://arxiv.org/abs/1405.2486.
2. D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, first posted 2015-08-14. https://arxiv.org/abs/1508.03519.
3. E. W. Weisstein, *Frucht Graph*, MathWorld, https://mathworld.wolfram.com/FruchtGraph.html (graph description and LCF representation).
4. E. Goles and J. Olivos, classical eventual-period-two theorem for symmetric threshold automata, as cited and stated in Reference 1.
