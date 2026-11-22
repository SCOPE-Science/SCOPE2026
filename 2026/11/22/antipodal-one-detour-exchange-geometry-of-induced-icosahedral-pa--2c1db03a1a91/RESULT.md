# Antipodal one-detour exchange geometry of induced icosahedral path partitions

## Finding
Let \(I\) be the twelve-vertex graph of the regular icosahedron. Let \(\mathcal P\) be the family of **named** two-class partitions \((A,V(I)\setminus A)\) such that both parts induce forests. A configuration is represented by the first class \(A\), so swapping the two class names gives a different configuration.

Every such partition is necessarily equitable: both parts have six vertices and each induces a chordless path \(P_6\). There are sixty configurations. This numerical count is also implied by the previously published induced-forest face vector and is **not** asserted as a novel enumeration.

Define the exchange graph \(\mathcal X\) on \(\mathcal P\) by joining distinct \(A,B\) precisely when \(|A\setminus B|=|B\setminus A|=1\); equivalently, one vertex changes from each color class, and both resulting classes must still induce forests. Then \(\mathcal X\) is a connected, four-regular, bipartite graph on sixty vertices with 120 edges, two bipartition shores of size thirty, girth six, and radius and diameter six. Every legal swap exchanges adjacent vertices of the original icosahedral graph.

For all \(A,B\in\mathcal P\), put \(h(A,B)=|A\setminus B|\), their distance in the ambient Johnson graph \(J(12,6)\). The exact metric satisfies
\[
\boxed{h(A,B)\le d_{\mathcal X}(A,B)\le h(A,B)+1.}
\]
The excess one occurs for exactly 420 of the \(\binom{60}{2}=1770\) unordered distinct pairs. All other 1350 pairs admit a shortest Johnson-geodesic exchange path within \(\mathcal P\). Every configuration \(A\) has the complement \(V(I)\setminus A\) as its **unique** distance-six antipode. In particular, there are exactly thirty unordered diameter pairs. Each vertex has the same distance-shell profile
\[
(1,4,12,17,16,9,1).
\]

The complete unordered-pair metric distribution \((h,d_{\mathcal X}):\text{count}\) is

| Johnson distance | Exchange distance | Unordered pairs |
|---:|---:|---:|
| 1 | 1 | 120 |
| 2 | 2 | 360 |
| 2 | 3 | 150 |
| 3 | 3 | 360 |
| 3 | 4 | 120 |
| 4 | 4 | 360 |
| 4 | 5 | 150 |
| 5 | 5 | 120 |
| 6 | 6 | 30 |

## Assumptions and scope
The standard combinatorial model consists of two poles, indexed \(0\) and \(11\), and two five-cycles \(u_i=1+i\) and \(v_i=6+i\), for \(i\in\mathbb Z/5\mathbb Z\). Its thirty edges are \(0u_i\), \(11v_i\), \(u_iu_{i+1}\), \(v_iv_{i+1}\), \(u_iv_i\), and \(u_iv_{i-1}\), with indices modulo five. This is the regular icosahedral graph. The two verification programs use independently given, explicitly isomorphic, vertex labels. Their relabelling from the pole-and-rims model in `verify_partition.cpp` to the edge-list model in `verify_partition.py`, in order of labels 0 through 11, is \((0,1,5,11,7,8,6,4,10,9,2,3)\). The relabelling preserves all thirty edges.

A forest means a graph without *any* cycle, not merely a graph with some acyclic spanning subgraph. A \(P_6\) is a six-vertex induced chordless path, hence has exactly five edges. Both classes are labelled by colors, so the count of sixty is **not** divided by two. An exchange keeps the class sizes fixed and preserves both induced-forest constraints at every step. The Johnson metric is the minimum number of unrestricted one-out, one-in replacements, whether or not they preserve the constraints.

## Proof
**1. Sharp size and path structure.** Exhaustive enumeration of all \(2^{12}=4096\) induced vertex subsets gives the forest-count vector at cardinalities zero through six as \((1,12,66,200,345,300,60)\), with no forests of size seven or more. A particularly small independently checkable certificate is the induced-edge minima: among all six-vertex sets the minimum number of edges is five; among all seven-vertex sets the minimum is eight. A forest on seven vertices has at most six edges, so no seven-set is a forest; hereditary closure excludes larger forests. Every six-vertex induced forest has at most five edges, and therefore exactly five; it is a tree. Each vertex of \(I\) has neighborhood inducing a five-cycle, in which any three vertices contain an adjacent pair. If an induced forest had a vertex with three neighbors within the forest, that adjacent pair would form a triangle with it. Therefore each induced forest has maximum degree two. A six-vertex induced tree of maximum degree two is necessarily \(P_6\).

Any two complementary forests must both have size at most six, hence exactly six. The complete six-set check confirms that all sixty six-vertex forests have forest complements. Consequently the family of admissible named partitions is precisely the sixty six-vertex induced paths. The pre-existing forest-complex census independently contains the sixty six-vertex faces; the complement and exchange assertions are separate.

**2. Exact exchange graph.** Write each vertex subset as a twelve-bit integer. The programs examine all unordered pairs of the sixty admissible masks. They insert an exchange edge if and only if the XOR has two set bits. This is exactly the stated one-out/one-in rule. All 120 accepted pairs replace vertices joined by an edge of \(I\), and every configuration has four accepted neighbors. The graph is consequently four-regular. A complete two-coloring traversal of the 60-state exchange graph gives two equal independent shores of thirty, establishing bipartiteness. Its shortest cycle is six: deleting each exchange edge in turn and finding a shortest alternative path gives minimum alternate-path length five.

**3. Exact metric.** The one-exchange excess occurs concretely between
\(A=\{0,1,3,7,9,10\}\) and \(B=\{0,1,3,6,8,9\}\) in the pole-and-rims labelling: \(h(A,B)=2\) but \(d_{\mathcal X}(A,B)=3\). One shortest valid sequence replaces the first set successively by
\(\{0,1,3,7,9,11\}\), \(\{0,1,3,6,9,11\}\), and finally \(B\). These three steps give an explicit sharpness witness; nonexistence of a two-step route is certified by the full adjacency check.

From each of the sixty exchange states run breadth-first search over all 120 edges. Every search reaches all sixty configurations, with the same exact distance-shell profile \((1,4,12,17,16,9,1)\), proving connectivity, radius six, diameter six, and the unique farthest state. Checking that the unique vertex at distance six is the complement gives the antipode characterization. For every unordered pair compute \(h=|A\setminus B|\) and compare with its BFS distance. The full count is the nine-row table above, and in particular 420 pairs have \(d=h+1\), with no larger excess. The elementary lower bound \(d\ge h\) follows because each exchange can improve agreement with the target by at most one selected vertex. Thus the finite exhaustive certificate proves the claimed sharp bounds for **all** configurations of this fixed graph, not merely sampled pairs.

## Verification
`verify_partition.py` supplies an explicit thirty-edge list and checks acyclicity by union-find on induced edges. It tests all 4096 masks, all 1770 unordered state pairs, and sixty complete breadth-first searches. It also checks every allowed move against the original icosahedral edges, both color shores, every shortest-cycle candidate, and the entire joint Johnson/exchange-distance table.

`verify_partition.cpp` independently constructs the icosahedron using pentagonal rims and poles. Its forest predicate uses connected-component BFS together with the identity \(|E(F)|=|V(F)|-c(F)\). It independently enumerates all 4096 vertex masks, forms all sixty configurations and their exchanges, and repeats all sixty breadth-first metric checks and the bipartite and excess-distance counts. Both programs finish with the literal `CERTIFICATE_PASS`. The text outputs `verify_python.out` and `verify_cpp.out` record the executions. These are exact finite checks; their internal assertions and fully provided source make the enumerations repeatable.

## Relationship to prior work
Esperet, Lemoine and Maffray [1] established general theorems on equitable partitions into induced forests; their 2014-10-03 arXiv submission motivates asking for the sharp, smallest-color partition dynamics of a highly symmetric planar graph. Its inspected complete four-page text does not contain an exact icosahedral configuration-exchange graph.

The published icosahedral induced-forest complex computations [2,3] are the closest direct prior work. They explicitly enumerate sixty maximal six-vertex forest faces and compute integral homotopy and the icosahedral symmetry character. **The count of sixty, and the existence of such six-vertex forests, are consequently prior results.** The new claim concerns the additional complement pairing, the precise ridge/exchange adjacency of those faces, local-swap rigidity, connectedness, girth, the distance metric relative to the Johnson graph, and unique complementary antipodes. None of those statements is stated or implied merely by the face vector, the homotopy type, or the rational character. A fully explicit *list of all facets* could in principle be postprocessed to reconstruct the exchange graph, so such data remains a source of derivability and priority risk; no false independent novelty is claimed for the input census.

Akbari, Horsley and Wanless [4] develop general induced-path-factor theory. Their inspected preprint is mainly about cubic graphs and asymptotic bounds for regular graphs; its searchable full text has no occurrence of the icosahedron or the relevant exchange terminology. Published icosahedral zero-forcing exchange work [5] uses 200 different six-vertex sets selected by eight or nine induced edges, rather than the present sixty sets with exactly five edges. Its metric is therefore not a stronger statement about these configurations. A published dodecahedral odd-cycle-transversal one-detour result [6] has a similar type of distance bound but uses a different graph and feasible-set family, with no evident reduction yielding the table here.

## Limitations
All assertions concern the single finite graph \(I\); no unbounded-family or universal reconfiguration theorem is claimed. The geometric explanation of why all legal swaps are local and why exactly 420 pairs incur a detour is presently algorithmic rather than a compact intrinsic classification. Earlier accessible complete forest-facet data substantially reduces the novelty of the classification input. Exact publication priority cannot be guaranteed against unindexed tables or unpublished exchange-graph computations. This scientific record has undergone only self-review, not independent scholarly validation.

## References
1. L. Esperet, L. Lemoine and F. Maffray, *Equitable partition of graphs into induced forests*, arXiv:1410.0861v1, first public 2014-10-03, https://arxiv.org/abs/1410.0861.
2. *Induced-forest topology and full icosahedral symmetry*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-induced-forest-topology-and-full-icosahedral-symmetry--c48e67f704dd .
3. *Forty four-spheres and the full symmetry character of the icosahedral induced-forest complex*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-forty-four-spheres-and-the-full-symmetry-character-of-the-icosah--cbbdda7e1993 .
4. S. Akbari, D. Horsley and I. M. Wanless, *Induced path factors of regular graphs*, arXiv:1809.04394v1, first public 2018-09-12, https://arxiv.org/abs/1809.04394.
5. *Icosahedral six-set edge criterion and zero-forcing exchange geometry*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-icosahedral-six-set-edge-criterion-and-zero-forcing-exchange-geo--3e6559fd96e0 .
6. *One-detour exchange metric of optimal vertex bipartizations of the dodecahedral graph*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-one-detour-exchange-metric-of-optimal-vertex-bipartizations-of-t--6689e33109ba .
