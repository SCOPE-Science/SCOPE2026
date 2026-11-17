# A simultaneous consensus-and-oscillation gain under every Robertson-cage edge deletion

## Finding

Let \(R\) be the canonical nineteen-vertex Robertson \((4,5)\)-cage, with the labelled adjacency array specified in `check_all_edges.cpp` and independently in `independent_numpy.py`. The following table gives the exact complete response of synchronous binary majority voting to **every** one-edge deletion. A one-based representative denotes an orbit of edges under graph automorphisms. \(H\) is the number of fixed labelled configurations; \(C\) is the number of *primitive period-two orbits* (not configurations); \(U\) is the combined attraction basin of the all-zero and all-one fixed configurations; \(T\) is the maximum number of updates before first periodic entry.

| Deleted edge | Orbit multiplicity | \(H\) | \(C\) | \(U\) | \(T\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| None | — | 6508 | 2166 | 295138 | 11 |
| \((1,2)\) | 2 | 3772 | 2670 | 309046 | 11 |
| \((1,3)\) | 12 | 3584 | 2478 | 310832 | 12 |
| \((3,9)\) | 12 | 3620 | 2490 | 312052 | 12 |
| \((3,10)\) | 12 | 3622 | 2518 | 311104 | 12 |

In particular, removing any of the 38 edges **simultaneously decreases** \(H\), **increases** \(C\), and **increases** \(U\). The combination is not a universal monotonicity assertion for other graphs. Of note, both oscillatory orbit count and unanimous attraction rise, notwithstanding their distinct meanings. In 36 deletions the sharp first-periodic-entry time rises from eleven to twelve updates.

## Assumptions and scope

For every vertex \(v\), let \(N_G(v)\) be its *open* neighbor set. A configuration is a function \(x:V(G)\to\{0,1\}\), and all vertices update simultaneously by

\[
F_G(x)_v=\begin{cases}1,&2\sum_{w\in N_G(v)}x_w>\deg_G(v),\\0,&2\sum_{w\in N_G(v)}x_w<\deg_G(v),\\x_v,&2\sum_{w\in N_G(v)}x_w=\deg_G(v).\end{cases}
\]

The vertex set is labelled \(\{1,\ldots,19\}\) according to the adjacency arrays in the independent source files. The original graph has four neighbors at each vertex; deleting one edge makes precisely two vertices degree three. No self-loops or parallel edges are introduced. There are exactly \(2^{19}=524288\) labelled binary configurations for every graph. The first periodic entry time of \(x\) is the smallest \(t\ge0\) such that \(F_G^t(x)\) is periodic. In the present finite family, all eventual periods are one or two.

## Proof

The claim is a finite exhaustive theorem, proved by exact integer computation with fully included independent implementations. The exhaustion is complete, not a finite sample from an infinite family.

1. The hard-coded symmetric 19-by-4 neighbor table defines 38 undirected edges. `independent_numpy.py` independently checks the graph is four-regular, has 19 vertices and girth five, determines all 24 graph automorphisms, and computes their four disjoint edge orbits, whose cardinalities are \(2,12,12,12\). Thus it is enough to classify four representatives, while `check_all_edges.cpp` computes all 38 deletions without relying on this symmetry reduction.
2. Each algorithm constructs the exact map on the integer-coded set \(\{0,\ldots,2^{19}-1\}\). For each vertex it sums the applicable neighbor bits and applies the three-case threshold rule above. Bit operations are integer exact. The two implementations use different languages, different graph storage conventions and different algorithms (vectorized array evolution and explicit individual trajectory traversal).
3. For each graph, all 524288 states are visited. An immediate fixed state satisfies \(F(x)=x\); an immediate primitive period-two state satisfies \(F^2(x)=x\) and \(F(x)\ne x\), so the latter state population is divided by two to count orbits. Repeatedly applying the exact map to all starts until each lies in one of those two sets counts first-entry times. The maximum nonempty time bin gives \(T\); the corresponding nonempty bin is also a witness that the bound is sharp.
4. To determine \(U\), count exactly those states whose eventually periodic representative is either integer \(0\) or integer \(2^{19}-1\). These are the two unanimous configurations and both are fixed. The C++ program independently traces trajectories to this target from every initial state, rather than inferring the result from recurrence counts. The Python program computes the same count from its terminal iterates.
5. The complete 39-case C++ table in `check_all_edges_output.txt` consists of the original graph and each individual edge deletion, matching the four-edge-class representative table computed independently in `independent_numpy_output.txt`. The four orbit multiplicities total \(38\), and the strict inequalities in the displayed table prove the three asserted simultaneous changes for every edge.

For example, the all-state first-entry histogram on \(R\), indexed from \(t=0\) through \(t=11\), is

\[
(10840,59422,179676,155502,75768,23424,9408,4752,2856,1824,768,48).
\]

It sums to \(524288\), its last entry is positive, and all more distant bins are zero, proving the sharp eleven-update cutoff. Every deleted-edge class also has its displayed positive final bin, ending at eleven or twelve.

## Verification

Run `g++ -O3 -std=c++17 check_all_edges.cpp -o check_all_edges` and then `./check_all_edges > check_all_edges_output.txt`. Independently install Python with NumPy and NetworkX and run `python independent_numpy.py > independent_numpy_output.txt`. The two **included** output files are the actual outputs observed for the included source programs. Their baseline and edge-class results coincide in every reported statistic. The C++ output has one data row per each of the 38 deleted edges, not just representatives. The Python code checks the graph's automorphism group and derives the four orbits without using the C++ output. The critical counting operations, not just diagnostic logs, are in the code.

## Relationship to prior work

Robertson's original description of the smallest quartic girth-five cage (1964, pages 824–825) explicitly identifies its 24 automorphisms and four classes of edges of sizes \(2,12,12,12\), but does not study majority-vote dynamical basins or period-two populations. The classical Goles–Olivos result gives eventual periods at most two for symmetric threshold maps; it gives no quantitative census or edge-deletion inequality for this cage. Agur–Fraenkel–Klein count fixed states of a cyclic three-site binary majority rule, a different network and neighborhood rule.

The closest identified exact one-edge majority classification concerns the 12-vertex Chvátal graph: all single-edge removals *increase* its unanimity basin but *decrease* the number of two-cycle orbits. The present Robertson result has the opposite response for that orbit count. General edge-defected complete-bipartite majority systems have different hypotheses and do not imply a result on a girth-five quartic cage. These statement-level distinctions support originality, while not constituting an exhaustive guarantee of historical priority.

## Limitations

This theorem is specifically about one-edge deletions of the labelled Robertson graph, with simultaneous deterministic open-neighbor majority and incumbent-tie retention. It gives no statement about arbitrary quartic graphs, additions of edges, stochastic tie-breaking, or asynchronous updates. The proof is computational and finite, with source code and exact outputs provided for reproducibility; no short hand derivation of each numerical count is claimed. No independent external validation or comprehensive historical-priority certificate has been performed. Some classical general-threshold papers were available only through abstracts in this assessment.

## References

- N. Robertson, *The smallest graph of girth 5 and valency 4*, Bulletin of the American Mathematical Society 70 (1964), 824–825, DOI 10.1090/S0002-9904-1964-11250-7. Full two-page text inspected at https://artefacts-discovery.researcher.life/full_text/DA-2/bb/bb3144f818ed314f9cebb308a0a5efd6/full_text/9b254f347a4a56021538dea19270036d.pdf.
- G. Exoo and R. Jajcay, *Dynamic Cage Survey*, Electronic Journal of Combinatorics, first published 2008-09-29, DOI 10.37236/37, https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS16.
- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI 10.1016/0012-365X(80)90121-1.
- Z. Agur, A. S. Fraenkel, S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302, DOI 10.1016/0012-365X(88)90005-2; full paper at https://u.cs.biu.ac.il/~tomi/Postscripts/majority.pdf.
- OEIS A184945, Robertson-graph labelled adjacency presentation, https://oeis.org/A184945. The full array used is reproduced directly in the included code.
- Related published exact Chvátal-graph majority edge-deletion result, compared at the level of orbit and basin implications in the review below.
