# Modular mobility of maximum induced matchings in triangular graphs

## Finding

For every integer \(n\ge 3\), let the triangular graph \(T_n=L(K_n)\) have as vertices the unordered pairs of \([n]\), with adjacency for intersecting pairs. Write \(k=\lfloor n/3\rfloor\) and \(r=n-3k\in\{0,1,2\}\). An induced matching is an edge set whose endpoints induce exactly a disjoint union of edges. Its maximum cardinality is

\[
\nu_I(T_n)=k.
\]

Every maximum induced matching is uniquely a collection of \(k\) pairwise disjoint three-element subsets (blocks) of \([n]\), each equipped with a distinguished element (its centre), leaving exactly \(r\) unused labels. The selected edge of \(T_n\) associated with a block \(\{a,b,c\}\) centred at \(a\) joins vertices \(\{a,b\}\) and \(\{a,c\}\). Thus the number of maximum induced matchings is

\[
N_n=\frac{n!}{r!\,2^k k!}.
\]

Define two reconfiguration graphs on these maximum induced matchings. In the edge-jump graph \(J_n\), two states are adjacent if they differ by deletion of one selected *edge of \(T_n\)* and insertion of another edge of \(T_n\), remaining maximum induced matchings. In the edge-slide graph \(S_n\), additionally the deleted and inserted edges of \(T_n\) must share an endpoint in \(T_n\). Equivalently they are adjacent in \(L(T_n)\). These are **edge-token** operations, not operations moving individual endpoint vertices of the induced one-regular subgraph.

Both graphs are regular, with exact degrees

\[
\deg(J_n)=k\bigl(3\binom{r+3}{3}-1\bigr)
=\begin{cases}2k&r=0,\\11k&r=1,\\29k&r=2,\end{cases}
\]

\[
\deg(S_n)=k(4r+2)
=\begin{cases}2k&r=0,\\6k&r=1,\\10k&r=2.\end{cases}
\]

Their connected components agree exactly:

\[
\begin{cases}
\displaystyle \frac{n!}{6^k k!}\text{ components, each isomorphic to }\underbrace{K_3\square\cdots\square K_3}_{k\text{ factors}}, &r=0,\\[4pt]
\text{one connected component},&r=1\text{ or }2.
\end{cases}
\]

In particular, when \(3\mid n\), even unrestricted single-edge jumps cannot change the partition of \([n]\) into triples, while one unused ground label suffices to connect the entire configuration space even under edge sliding.

## Assumptions and scope

All graphs are finite, undirected and simple. The notation \(L(G)\) means the line graph, and \(K_n\) is the complete graph on the labelled set \([n]\). Two distinct vertices of \(T_n\) are adjacent exactly when the corresponding two-element sets intersect. A three-label *support* is the union of the ground labels appearing in the two endpoints of one edge of \(T_n\). The theorem concerns **maximum cardinality** induced matchings, not merely inclusion-maximal ones. Edge jumping and edge sliding act on the edges selected in the matching, never on the individual vertices in its endpoint set.

## Proof

**1. Structural bijection and maximum size.** Each edge of \(T_n\) joins two intersecting, distinct two-subsets, and hence has exactly three ground labels as support. The edge is specified by its three-label support and the unique common ground label of its two endpoint pairs. If two such edges are in an induced matching, no endpoint pair of the first can intersect any endpoint pair of the second. Therefore their three-label supports are disjoint. Conversely, two edges with disjoint three-label supports have neither shared endpoints nor cross-adjacencies in \(T_n\). Thus an induced matching of size \(t\) corresponds exactly to \(t\) disjoint labelled triples with a centre in each, and satisfies \(3t\le n\). Taking \(k=\lfloor n/3\rfloor\) triples realizes this bound. The number of partitions into \(k\) unordered three-element blocks and \(r\) unused labels is \(n!/(r!(3!)^k k!)\); marking one of three possible centres per block multiplies by \(3^k\), giving \(N_n\).

**2. Locality of all moves.** Remove a selected edge whose support is the triple \(B\). Every other selected edge uses three labels disjoint from \(B\) and from the \(r\) unused ground labels. For the replacement to remain an induced matching of cardinality \(k\), its three-label support must lie in the \(3+r\) labels consisting of \(B\) and the unused labels. Conversely, every edge of \(T_n\) with support in these \(3+r\) labels is compatible with every other selected edge. Hence there are exactly \(3\binom{3+r}{3}-1\) alternative edge-jump choices at each of the \(k\) selected edges. Distinct removed edges give distinct resulting states, yielding the formula for \(\deg(J_n)\).

For sliding, the removed edge of \(T_n\) has two endpoints, which are adjacent vertices inside the copy of \(T_{r+3}\) induced on the available \(r+3\) labels. The graph \(T_{r+3}\) has vertex degree \(2(r+1)\). Thus in its line graph, the vertex corresponding to the removed edge has exactly \(2(2(r+1)-1)=4r+2\) neighbors, all and only valid replacement edges under the slide condition. Again the choices at different selected edges give different resulting matchings. This proves the sliding degree formula.

**3. Components when no ground labels are unused.** If \(r=0\), step 2 shows that a replacement cannot change any support triple. On each fixed triple there are exactly three choices of centre, and any two of the corresponding three edges of \(T_n\) share one endpoint in \(T_n\). Therefore they form a \(K_3\) under both moves. Changes in distinct triple blocks are independent, so every component is the Cartesian product of \(k\) copies of \(K_3\). The components are indexed by the partitions into unordered triples, counted by \(n!/(6^k k!)\).

**4. Connectivity with at least one unused ground label.** Let \(r\ge1\). Within a fixed support triple \(\{a,b,c\}\), we can change its centre from \(a\) to \(b\) in a single slide, since edges \(\{\{a,b\},\{a,c\}\}\) and \(\{\{a,b\},\{b,c\}\}\) of \(T_n\) share the vertex \(\{a,b\}\). Next choose any unused ground label \(x\), and any occupied ground label \(c\) in the block \(\{a,b,c\}\). First, if necessary, choose the centre \(a\). Replacing the block edge joining \(\{a,b\},\{a,c\}\) by the edge joining \(\{a,b\},\{a,x\}\) is a legal edge slide: the two edges of \(T_n\) share endpoint \(\{a,b\}\), and the new block's support \(\{a,b,x\}\) stays disjoint from all other supports. It interchanges the occupied label \(c\) with the unused label \(x\).

Consequently, sliding moves can exchange any occupied label with any unused label, while changes of centre are independently possible. With a chosen free label serving as a temporary vacancy, three such exchanges interchange the labels in any two occupied positions: exchange the first label with the vacancy, the second with the now-free first, and the original free label with the now-free second. Together with one-exchange transfers to the unused positions, these operations generate every assignment of the \(n\) distinct ground labels to the \(3k\) occupied positions and the \(r\) free positions; in particular, they connect every collection of disjoint support triples to every other. Each target centre can then be selected by a within-triple slide. Hence \(S_n\) is connected for \(r=1,2\). Since \(S_n\) is a spanning subgraph of \(J_n\), the jump graph is connected as well. This completes the proof.

## Verification

The standalone programs `direct.py` and `abstract.py` use separate representations. The former builds \(T_n\) directly from pairs and tests every \(k\)-edge candidate for induced matching, then constructs both reconfiguration graphs. The latter enumerates independently all supported marked-triple packings and generates both move sets. The two programs check vertex counts, exact regular degrees and complete component-size distributions.

Run with Python 3 using `python direct.py` and `python abstract.py`. Saved deterministic outputs are `direct_output.txt` and `abstract_output.txt`. The direct program completes all \(3\le n\le8\); the independent marked-triple program completes all \(3\le n\le9\). Both return PASS on their stated ranges. These finite checks corroborate, but do not replace, the proof for all \(n\ge3\).

## Relationship to prior work

Induced matchings and their enumeration are classical, and strong matchings and \(2\)-edge packings are synonymous terminology. Basavaraju et al. study bounds and enumeration of *inclusion-maximal* induced matchings in triangle-free graphs; a triangular graph \(T_n\) contains triangles and the present exact maximum-configuration reconfiguration theorem is not a consequence of their triangle-free result. Bonsma, Kamiński and Wrochna study independent-set jumping and sliding in claw-free graphs, giving general reachability algorithms rather than this matching-edge configuration enumeration. The model of Eto et al. replaces a *vertex* of a one-regular induced subgraph; it is distinct from the present replacement of one whole matched edge. Brešar et al. study induced matching numbers in graph products, not the exact marked-triple configuration spaces and edge-move components of \(T_n\).

The packing reduction resembles matching reconfiguration in complete three-uniform hypergraphs, but the marked centre and distinction between edge jumping and edge sliding change the degree formulas and must be retained. Available public searches revealed no publication directly identifying the full classification above; this is not proof of absolute priority.

## Limitations

The theorem assumes the complete-graph line graph \(T_n\) and single-edge exchanges preserving maximum cardinality. It does not address arbitrary triangular line graphs, nonmaximum induced matchings, or the vertex-token operations in regular-induced-subgraph reconfiguration. The formulas determine regularity and connected components but not diameters when \(r>0\). Priority remains subject to unindexed or otherwise inaccessible relevant studies of complete-hypergraph packing reconfiguration and induced matchings.

## References

1. M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei, and Y. Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180v1, publicly posted 2013-12-18, https://arxiv.org/abs/1312.5180.
2. P. Bonsma, M. Kamiński, and M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1, publicly posted 2014-03-03, https://arxiv.org/abs/1403.0359.
3. H. Eto, T. Ito, Y. Kobayashi, Y. Otachi, and K. Wasa, *Reconfiguration of Regular Induced Subgraphs*, arXiv:2111.13476, first posted 2021-11-26, https://arxiv.org/abs/2111.13476.
4. B. Brešar, T. Dravec, J. Hedžet, and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020, first posted 2024-06-06, https://arxiv.org/abs/2406.04020.
