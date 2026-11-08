# The token-slide graph of minimum identifying codes of the Heawood graph is a star forest

## Finding

**Theorem (exact slide mobility of optimal Fano incidence codes).** Let \(H\) be the 14-vertex Heawood graph, the point-line incidence graph of the Fano plane. A radius-one closed-neighborhood identifying code is a set \(C\subseteq V(H)\) for which the fourteen sets \(N_H[v]\cap C\) are all nonempty and pairwise distinct. Among its minimum-cardinality identifying codes, join two codes when one selected vertex is replaced by an unselected **adjacent** vertex and the resulting set remains a minimum identifying code (a legal token slide). The resulting reconfiguration graph is exactly
\[
\boxed{\mathcal S(H)\cong 56K_{1,3}\;\sqcup\;2K_{1,21}.}
\]
Its \(268\) states therefore form **58** connected components, with **210** legal transitions. There are \(210\) degree-one states, \(56\) degree-three states, and two degree-21 states. There are no isolated states, but every connected component is a star: no shortest slide sequence requires more than two moves between reachable codes, and every longer attempted excursion through a leaf must immediately retrace an edge. Exactly \(798\) unordered pairs of distinct minimum codes are mutually reachable: \(210\) at distance one and \(588\) at distance two. The two 22-state stars are centered respectively at the code of all seven point vertices and the code of all seven line vertices; the 56 four-state claws cover every other minimum code.

This theorem concerns the **token-slide** move condition. It does not claim a new count of minimum identifying codes, a new token-**jump** reconfiguration classification, or any result for nonminimum codes.

## Assumptions and scope

Vertices of \(H\) are labeled \(0,\ldots,13\), with point vertices \(0,\ldots,6\) and line vertices \(7,\ldots,13\). Point \(i\) is joined to line \(7+j\) exactly when \(i-j\pmod 7\in\{0,1,3\}\). Thus each line has points \(j,j+1,j+3\) modulo seven; this is the usual Fano-plane incidence geometry. Tokens are indistinguishable, and graph vertices retain their labels. A slide removes one vertex \(u\) from a code and adds one vertex \(v\) that is not in the code, with \(uv\in E(H)\); the resulting code must meet the same identification condition and cardinality. We do **not** quotient by graph automorphisms.

The minimum identifying-code cardinality for this fixed graph is seven, with exactly 268 seven-element codes, as is also verified by the complete certificate. Those cardinality facts are inputs to the reconfiguration question and are not claimed as novel here.

## Proof

**Exhaustive, logically complete state classification.** For each vertex \(v\), let \(b_v\) be the 14-bit integer mask of its closed neighborhood. For a candidate code with mask \(c\), the identifying signature of \(v\) is exactly the integer \(b_v\mathbin{\&}c\). Consequently the code is identifying if and only if all fourteen signatures are nonzero and pairwise unequal. This condition is necessary **and** sufficient by definition, not merely a heuristic test. The certificate programs exhaust every one of the \(2^{14}=16384\) masks, including all cardinalities below seven; they find no identifying code of size at most six and exactly 268 at size seven, and reconstruct the sorted list `states.txt` without omission. Each code in this list is thus minimum.

**Every slide, including all absent ones.** For two distinct seven-vertex codes \(C,D\) with masks \(c,d\), exactly one selected vertex changes if and only if \(c\oplus d\) contains exactly two set bits. When these positions are \(u\) and \(v\), the move is a slide if and only if \(uv\in E(H)\). Thus the two necessary-and-sufficient conditions test **every** unordered pair of the 268 states. The resulting complete list of 210 unordered edges is `slides.txt`. Both provided checkers reconstruct it independently, comparing every edge rather than only the edge count.

**Star forest and sharp distances.** A breadth-first component traversal of the certified complete slide adjacency list produces exactly 56 components of order four, each with one degree-three vertex and three degree-one vertices, and two components of order 22, each with one degree-21 vertex and 21 degree-one vertices. These degree conditions and component orders force the claimed star isomorphisms, rather than merely suggesting them. The center of each large component is identified in the certificates as either the all-points or the all-lines code. The 21 possible slides from the all-points code replace an incident point with a line, one for each of the 21 Fano incidences; the dual statement holds for the all-lines code. No extra adjacent state exists because the complete pair test finds exactly those 21.

All 56 small components are claws and their 224 states split into 56 centers plus 168 leaves; the large components provide two centers plus 42 leaves. Hence the degree distribution is \(210,56,2\) at degrees \(1,3,21\), respectively, and edge count is \(56\cdot3+2\cdot21=210\). An order-\(r+1\) star has \(r\) distance-one unordered pairs and \(\binom r2\) distance-two pairs. Therefore here the reachable-pair counts are \(56\cdot3+2\cdot21=210\) and \(56\binom32+2\binom{21}2=588\). These sum to \(798\). Pairs from different components are unreachable. This exhausts every optimal-code pair and proves the theorem.

## Verification

`states.txt` contains every qualifying seven-vertex mask; `slides.txt` contains every token-slide edge as a pair of increasing masks. For cross-checking the different move definitions, `jumps.txt` contains all possible one-vertex replacement edges without the adjacency restriction, but its larger reconfiguration graph is **not** asserted as a new result. The Python checker constructs Fano incidence using sets and chooses candidate subsets by cardinality; the C++17 checker independently uses 14-bit neighborhood masks and iterates all integers 0 through 16383. Both regenerate and compare every certificate line and check all slide components and distances. Run instructions appear in `VERIFICATION.md`. All files needed to replay the proof are included.

This is a rigorous finite exhaustion of all 14-vertex configurations, not extrapolation from a sample or a statement about other projective planes.

## Relationship to prior work

Balbuena, Foucaud and Hansberg (arXiv:1407.7263v1, 2014) examine identifying codes and locating domination in girth-at-least-five graphs. Their Heawood result in Proposition 24 is for **locating domination**, which identifies only vertices outside the selected set, rather than the complete token-slide reconfiguration of minimum closed-neighborhood identifying codes.

Mynhardt and Teshima (arXiv:1707.02039v1, 2017) define identifying-code slide reconfiguration and show that arbitrary finite target graphs can be realized using suitable **constructed input graphs**. Their theorem does not supply the slide graph for the specific canonical Heawood incidence graph. Teshima's dissertation (2022), Chapter 2, develops the general framework. In the present result the input graph is fixed, and the dramatic fragmentation into stars is an explicit answer to that natural prescribed-graph problem.

The minimum-code count and the **one-vertex token-jump** graph of this same Heawood graph have been previously enumerated, with three jump-connected components, including one of 224 states. The jump classification does not assert the **different**, adjacency-restricted token-slide star forest. The value of the present theorem is precisely that the stricter move destroys all large slide-connectivity while leaving no code completely immobile. Neither the known code count nor the abstract unmarked jump-component isomorphism determines which exchanges occur along incidence edges. The present slide graph is not represented as a novel discovery about unrestricted exchanges.

## Limitations

The graph is fixed at fourteen vertices; no higher-order projective-plane theorem follows. Two complete finite checkers and explicit state/transition certificates are integral to the proof; the star-forest conclusion relies on verified complete enumeration rather than a supplied uniform structural argument. A known list of 268 codes alone is not the same as this slide-edge classification, but an unpublished or unindexed calculation could already contain it. The paper and dissertation inspections concerned their directly relevant sections, not a claim that every external source is exhaustively ruled out. No independent scholarly audit has been performed.

## References

1. C. Balbuena, F. Foucaud, A. Hansberg, *Locating-dominating sets and identifying codes in graphs of girth at least 5*, arXiv:1407.7263v1 (2014-07-27), *Electronic Journal of Combinatorics* 22 (2015), #P2.15. https://arxiv.org/abs/1407.7263 ; https://perso.limos.fr/ffoucaud/Publications/Papers/J13_ID-LD-girth5_ElJC_2015.pdf
2. C. M. Mynhardt, L. E. Teshima, *A note on some variations of the gamma-graph*, arXiv:1707.02039v1 (2017-07-07), *Journal of Combinatorial Mathematics and Combinatorial Computing* 104 (2018), 217–230. https://arxiv.org/abs/1707.02039
3. L. E. Teshima, *The i-Graph and Other Variations on the gamma-Graph*, University of Victoria doctoral dissertation (2022; repository entry 2023-01-03), Chapter 2. https://dspace.library.uvic.ca/items/740e5c10-d1aa-4992-970b-3711b397f7f5
