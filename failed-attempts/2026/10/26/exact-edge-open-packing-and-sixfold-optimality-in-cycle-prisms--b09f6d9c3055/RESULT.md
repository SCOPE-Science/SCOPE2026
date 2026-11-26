# Exact edge-open packing and sixfold optimality in cycle prisms

## Finding
Let \(P_n=C_n\square K_2\) denote the simple prism graph, where \(n\ge3\). Two distinct edges conflict when some third edge joins an endpoint of one to an endpoint of the other. An **edge-open packing** is a set of edges having no conflicting pair, and \(\rho_e^{\mathrm o}(G)\) denotes its maximum size. Then
\[
\rho_e^{\mathrm o}(P_n)=\begin{cases}
n,&6\mid n,\\
n-1,&6\nmid n.
\end{cases}
\]
If \(6\mid n\), there are **exactly six** distinct maximum edge-open packings of the labelled prism \(P_n\). Each consists entirely of disjoint induced three-edge stars. Their centers occupy every third rung, with one of three cyclic phases and one of two bipartition orientations.

## Assumptions and scope
The graph has vertices \((i,r)\), where \(i\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\); its edges are the rungs \((i,0)(i,1)\) and the two rim edges \((i,r)(i+1,r)\). Every graph here is finite, simple and undirected. A third edge witnessing conflict must differ from the two chosen edges. Distinct labelled edge subsets count separately; no quotient by automorphisms is taken. Both statements hold for every integer \(n\ge3\), with no asymptotic or generic-position assumptions.

## Proof
**1. Upper bound.** The endpoints of any edge-open packing induce a disjoint union of stars, and all edges of this induced subgraph are the chosen edges: an extra induced edge would be a common edge of two chosen star edges, or the induced graph would contain a triangle or a path with three edges. Choose the leaves of each star, choosing one leaf for an isolated edge. The chosen leaves form an independent set containing precisely one vertex per packed edge. Hence \(\rho_e^{\mathrm o}(G)\le\alpha(G)\), the standard independent-set upper bound.

Every independent set of \(P_n\) meets each rung in at most one vertex, so \(\alpha(P_n)\le n\). If it meets every rung, the vertices chosen on consecutive rungs must alternate between the two rims. This is possible exactly when \(n\) is even, in which case exactly two independent sets have size \(n\). For odd \(n\), omitting a rung and alternating on the remaining path shows \(\alpha(P_n)=n-1\). Thus \(\rho_e^{\mathrm o}(P_n)\le n-1\) for odd \(n\).

Now suppose that \(n\) is even and an edge-open packing \(D\) has \(n\) edges. Its leaves form one of the two size-\(n\) independent sets \(L\), hence exactly one vertex on every rung; the complementary vertex set \(R\) is the other part of the bipartition. Each center of a selected star belongs to \(R\) and has all its three neighbours in \(L\). Since the endpoints of \(D\) induce exactly the selected star forest, **all three** incident edges at every center must be selected. The three-element neighbour sets of the centers therefore partition \(L\). In particular, \(3\mid n\). Consequently \(\rho_e^{\mathrm o}(P_n)\le n-1\) also for even \(n\) not divisible by three.

**2. Explicit lower constructions.** Encode a cyclic choice of edges by a word \(m_0m_1\cdots m_{n-1}\) over \(\{0,1,2,3,4,5\}\). At column \(i\), bit \(1\) selects its rung, bit \(2\) its rim-0 edge to column \(i+1\), and bit \(4\) its rim-1 edge. Only masks \(0,1,2,3,4,5\) are used. The following **cyclic** words are edge-open packings; the last column is adjacent to the first:

| \(n\) | Cyclic mask word | Number of chosen edges |
| ---: | :--- | ---: |
| 3 | `003` | 2 |
| 4 | `0023` | 3 |
| 5 | `02045` | 4 |
| 6 | `023045` | 6 |
| 7 | `0023045` | 6 |
| 8 | `02103045` | 7 |
| 9 | `003045023` | 8 |
| 10 | `0023045023` | 9 |
| 11 | `02045023045` | 10 |

Their validity is checked directly by comparing all pairs of encoded edges with all edges of the prism. This is a finite explicit verification, reproducible with `verify.py`.

For \(n\ge5\), conflicts are **local** in columns: two selected edges can have a common third edge only if their column indices are within cyclic distance two. Thus admissibility is equivalent to admissibility of every cyclic triple of consecutive column masks. Each of the six words of lengths \(6,7,8,9,10,11\) contains the consecutive mask pair `02`. View a cyclic word as a closed walk of overlapping pairs of masks, advancing \((a,b)\mapsto(b,c)\). Concatenating two such closed walks at their shared state \((0,2)\) preserves every allowed triple, hence preserves edge-open packing; their lengths and edge counts add.

For \(n=6q+r\), where \(q\ge1\) and \(0\le r<6\), concatenate one walk of length \(6+r\) (use the length-six walk for \(r=0\)) with \(q-1\) copies of the length-six walk. The resulting cyclic edge set has \(n\) edges when \(r=0\), and \(n-1\) edges otherwise. The three smaller orders were checked individually above. This attains every upper bound and proves the numerical formula.

**3. Rigidity and count at equality.** Suppose \(6\mid n\) and \(|D|=n\). By step 1 its leaves are one of two alternating maximum independent sets \(L\). For each rung \(i\), write \(x_i=1\) if its vertex in the opposite bipartition \(R\) is selected as a star center and \(x_i=0\) otherwise. Every vertex of \(L\) has precisely three neighbours in \(R\), at rungs \(i-1,i,i+1\). Partition into three-leaf stars is therefore equivalent to
\[
x_{i-1}+x_i+x_{i+1}=1\quad(i\in\mathbb Z/n\mathbb Z).
\]
Subtract successive equations to obtain \(x_{i+3}=x_i\); exactly one of the three consecutive values is one. Thus for each of the two choices of \(L\), precisely three phases of star centers are possible. Every such phase gives a valid induced-star packing and different edge set, yielding exactly six maximizers.

## Verification
The standalone program `verify.py` builds graph edges and the full edge-conflict relation directly from vertex endpoints. It independently solves maximum edge-open packing by a boundary-conditioned exact transfer dynamic program for every \(3\le n\le40\); all 38 values match the theorem. It checks the explicit cyclic constructions for every \(3\le n\le200\), and independently enumerates all six-edge feasible subsets of the six-rung prism, finding exactly six maximizers. Its recorded successful output is `verification_output.txt`. The unlimited-\(n\) conclusion is supplied by the proof, not inferred from finite experiments.

## Relationship to prior work
Chelladurai, Kalimuthu and Soundararajan (2022) introduced this edge-packing parameter and determined it for individual paths, cycles, complete multipartite graphs, wheels and the Petersen graph, but not for prisms. Brešar, Dravec, Hedžet and Samadi (2024/2025) established general Cartesian-product bounds and the independent-set upper bound, as well as exact values for certain hypercubes; their stated product inequalities do not produce this prism formula or the classification of six maximizers. Das and Santra (2026) supply general polynomial-time algorithms on other classes of graphs and the oriented-star-conflict approach, but no exact cycle-prism extremal formula. The present claim is the exact cyclic-prism determination and equality rigidity, not the existence of an algorithm or the general bound \(\rho_e^{\mathrm o}\le\alpha\).

## Limitations
The result applies to the ordinary Cartesian prism with two rim cycles and one matching of rungs. It does not determine the invariant on Möbius ladders, wider cylindrical grids or arbitrary Cartesian products. The upper-bound method relies on the particular three-regular bipartite structure, and the small witness-table checks are finite although the concatenation argument is general. Independent mathematical review and definitive bibliographic-priority assessment have not been performed.

## References
1. G. Chelladurai, K. Kalimuthu, and S. Soundararajan, *Edge Open Packing Sets in Graphs*, RAIRO Operations Research 56 (2022), 3765–3776; DOI: 10.1051/ro/2022171.
2. B. Brešar, T. Dravec, J. Hedžet, and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (first posted 2024-06-06), Discrete Mathematics 348 (2025), 114458.
3. G. K. Das and K. Santra, *Maximum Edge Open Packing on AT-Free, Chordal, and Convex Bipartite Graphs*, arXiv:2610.02275v1 (posted 2026-10-01).
4. G. K. Das and K. Santra, *Maximum Edge Open Packing in Permutation, Interval, and Well-Partitioned Chordal Graphs*, arXiv:2608.05310v1 (posted 2026-08-05).
