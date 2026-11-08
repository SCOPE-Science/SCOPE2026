# Two 514-state islands and 108 frozen minimum identifying codes on the Pappus graph

## Finding

Let \(H\) be the 18-vertex Pappus graph (the cubic Levi graph of the Pappus \(9_3\)-configuration). A *closed-neighborhood identifying code* is a vertex set \(C\) for which the 18 traces \(C\cap N[v]\), \(v\in V(H)\), are all nonempty and pairwise different. The minimum cardinality is \(9\). There are exactly \(1028\) distinct minimum codes, with vertices individually distinguished.

The two independent classes of the bipartite graph each contain nine vertices. Let \(a_j\) count minimum codes containing exactly \(j\) vertices in a fixed class. Then
\[
(a_0,a_1,\ldots,a_9)=(1,27,81,243,162,162,243,81,27,1).
\]

Take these 1028 codes as states. In the *token-slide graph* \(\mathcal T\), an edge replaces one code vertex by an adjacent, initially unselected graph vertex, retaining minimum-code validity. In the *token-jump graph* \(\mathcal J\), the new vertex may be any initially unselected graph vertex. The exact reconfiguration classifications are:

* \(\mathcal T\) consists of \(108\) isolated vertices and **two isomorphic connected components on \(460\) states each**. Each nontrivial component has \(702\) edges, radius \(4\), and diameter \(8\); the whole slide graph has \(1404\) edges.
* \(\mathcal J\) consists of **two isomorphic connected components on \(514\) states each**. Each has \(1890\) edges, radius \(4\), and diameter \(8\); the whole jump graph has \(3780\) edges.

Neither move model connects a code whose majority of selected vertices is in one bipartition class to a code whose majority is in the other. Each jump component contains 54 of the configurations that are isolated for sliding. Each of the two large slide components and each jump component has exactly one metric center (eccentricity 4): the state containing an entire bipartition class.

The complete (state-degree: multiplicity) distributions are
\[
\mathcal T:\ (0:108,\ 1:540,\ 3:126,\ 5:108,\ 7:54,\ 9:36,\ 11:54,\ 27:2),
\]
\[
\mathcal J:\ (2:108,\ 4:216,\ 5:216,\ 7:108,\ 11:270,\ 15:108,\ 27:2).
\]
All assertions concern this specified finite graph, not arbitrary incidence graphs.

## Assumptions and scope

The graph is simple and undirected. One explicit labeling is the cyclic vertex set \(\{0,1,\ldots,17\}\) with the edges of the 18-cycle and the chords \(\{i,i+d_i\}\) modulo \(18\), where the LCF offsets \(d_i\) repeat the six-tuple \((5,7,-7,7,-7,-5)\) three times. Duplicate undirected edges are merged, leaving exactly 27 edges. Even and odd labels form the two bipartition classes.

An independent, equivalent model is the incidence graph of nine points \((x,y)\in\mathbb F_3^2\) and nine lines of the three families \(x=c\), \(y=c\), and \(x+y=c\), \(c\in\mathbb F_3\). This is the affine plane with one parallel class removed. The second verifier checks an explicit bijection identifying its 27 edges with the 27 LCF edges; no graph-library model is assumed by either certificate.

All tokens are indistinguishable, states are unordered sets of precisely nine vertices, and reconfiguration edges represent single simultaneous removals and additions, with feasibility checked at both endpoints. Components of size one are called isolated, and radius/diameter are assigned only to nontrivial components.

## Proof

**1. Exact identifying-code condition.** For a vertex \(v\), define its closed ball \(B_v=N[v]\). The definition is equivalent to the finite collection of constraints
\[
C\cap B_v\ne\varnothing\quad(v\in V(H)),\qquad
C\cap(B_u\triangle B_v)\ne\varnothing\quad(u\ne v).
\]
Indeed, a zero trace violates domination, and two equal traces have an empty intersection of \(C\) with the corresponding symmetric difference. Conversely these \(18+\binom{18}{2}=171\) nonempty-intersection conditions give distinct nonzero signatures. Thus an exhaustive traversal of all \(2^{18}=262144\) subsets, checking these exact integer bit masks, is a finite proof rather than sampling.

**2. Exhaustiveness, minimum size and census.** `checker_lcf.py` constructs the 27-edge LCF graph directly from the displayed offsets, forms all 18 closed balls, and tests every integer mask from 0 through 262143. It rejects a mask unless its 18 nonzero signatures are pairwise distinct. No accepted mask has fewer than nine bits. Exactly 1028 accepted masks have nine bits; their even-side occupancy counts give the stated ten-term vector. `checker_affine.py` separately constructs the nine-point/nine-line model and tests the *witness constraints* against each subset of size at most nine, using combinations rather than a full integer-mask sweep. It tests exactly 155382 subsets through the first feasible cardinality and gives the same answer. Both verifiers explicitly establish that the underlying two edge lists are isomorphic. Their standalone source files and executed output records are included as part of this result.

**3. Transition graphs.** For each accepted nine-bit mask \(m\), every ordered choice of a selected position \(u\) and an unselected position \(v\) gives the unique potential replacement mask \(m\oplus2^u\oplus2^v\). This is a legal jump exactly if it is another accepted mask; it is also a legal slide exactly if \(\{u,v\}\) is among the original 27 graph edges. Both verifiers explicitly visit every one of the nine times nine choices at each state. They construct the complete symmetric adjacency relation, take connected components by graph traversal and compute all component eccentricities by breadth-first search from every state. Consequently neither component counts nor diameter estimates depend on partial exploration or randomized experiments.

The resulting counts are 108 singleton slide components plus two slide components with 460 states and 702 edges each, and two jump components with 514 states and 1890 edges each; the respective nontrivial eccentricity histograms, identical in each paired component, are
\[
\begin{aligned}
\mathcal T &: (4:1,\ 5:27,\ 6:81,\ 7:243,\ 8:108),\\
\mathcal J &: (4:1,\ 5:27,\ 6:81,\ 7:243,\ 8:162).
\end{aligned}
\]
The complete degree distributions and component sizes above follow from the same exhaustive adjacency lists. The no-cross-majority assertion is separately checked on **every** jump edge, hence also on every slide edge. The singleton slide states split 54/54 according to their bipartition majority.

**4. Why paired large components are isomorphic.** The explicit LCF-coordinate permutation
\[
\sigma=(1,0,5,6,7,8,9,16,17,12,11,10,3,4,15,14,13,2)
\]
(its \(i\)th entry is \(\sigma(i)\)) is a bijection preserving all 27 graph edges and exchanging the even and odd classes. This is independently checked against the graph edge set. It preserves identifying-code validity, replacement adjacency, and graph distances, and therefore interchanges the corresponding 460- and 514-state components.

## Verification

Run `python3 checker_lcf.py` and `python3 checker_affine.py` with Python 3.9 or later and no third-party packages. Each program aborts on a failed invariant and prints a deterministic JSON summary. The exact outputs from the executed programs are included as `output_lcf.json` and `output_affine.json`. Each program independently constructs its graph and all admissible states, checks every legal replacement, and performs a full shortest-path traversal on each nontrivial component. The affine verifier checks the explicit graph isomorphism rather than relying on matching totals from unrelated graphs. Exhaustive execution completed and the printed counts matched across both models.

## Relationship to prior work

The definition and use of identifying codes originate with Karpovsky, Chakrabarty and Levitin (1998), who give universal size bounds and treat meshes, cubes, and trees. In the Pappus graph, their elementary degree bound \(\gamma^{ID}\ge 2|V|/(\Delta+2)\) gives only \(\gamma^{ID}\ge8\), not the exact value nine, much less the configuration graphs. Foucaud, Klasing, Kosowski and Raspaud (arXiv:1010.5975, first posted October 28, 2010) give bounds and constructions for triangle-free graphs; their inspected definitions and constructive main arguments are not an enumeration of this 18-vertex graph or its reconfiguration graphs.

Foucaud et al. (arXiv:1107.0207, first posted July 1, 2011) study identifying codes in **line graphs**, which are identifying codes on edges of the input graph, not identifying codes of the Pappus Levi graph itself. The published Pappus graph descriptions give its LCF and incidence representations, without these optimal-code or token-mobility enumerations. Related results for other cubic graphs or for edge-colour swaps are not implications about closed-neighborhood identifying codes here.

The contribution claimed here is exactly the 1028-state minimum-code census, balance vector, and both reconfiguration classifications, not the defining concept, the Pappus graph construction, or existing general extremal bounds. Accessible search evidence has not established that this exact finite census was previously published; that is a best-knowledge, not an absolute priority, assessment.

## Limitations

This is a finite graph-specific theorem. It does not imply a similar formula for other Levi graphs, larger cubic symmetric graphs, open-neighborhood identifying codes, locating-dominating sets, or identifying codes with nonminimum cardinality. Exhaustive enumeration is a complete finite proof only because the search visits all relevant subsets and replacements; the supplied two independent implementations and outputs are essential to the computational certificate. Existing unindexed code tables, unsearched print publications, and unpublished calculations could contain the same census. The older foundational paper was examined in relevant portions, not certified exhaustively against every possible implicit specialization; no originality assertion is based solely on absence of a word in a snippet. No independent scholarly audit has been performed.

## References

1. M. G. Karpovsky, K. Chakrabarty, L. B. Levitin, *On a New Class of Codes for Identifying Vertices in Graphs*, IEEE Transactions on Information Theory 44 (1998), 599–611, DOI: 10.1109/18.661507. Author-hosted full text: https://sites.bu.edu/mark/files/2018/02/132.pdf .
2. F. Foucaud, R. Klasing, A. Kosowski, A. Raspaud, *On the size of identifying codes in triangle-free graphs*, first publicly posted October 28, 2010, https://arxiv.org/abs/1010.5975 .
3. F. Foucaud, S. Gravier, R. Naserasr, A. Parreau, P. Valicov, *Identifying codes in line graphs*, first publicly posted July 1, 2011, https://arxiv.org/abs/1107.0207 .
4. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html , including Frucht's 1976 LCF representation and the Pappus-configuration incidence model.
