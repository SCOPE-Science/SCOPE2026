# Complementary induced-tree bisections and antipodal connected-decycling exchanges of the Heawood graph

## Finding

Let \(H\) be the Heawood graph, the point–line incidence graph of the Fano plane, with fourteen vertices and twenty-one edges. A **connected feedback vertex set** is a vertex subset \(S\) for which \(H[S]\) is connected and the vertex-deleted graph \(H[V(H)\setminus S]\) is acyclic. Its minimum cardinality is \(\operatorname{cfvs}(H)=7\), whereas the previously established unrestricted feedback-vertex number is \(\operatorname{fvs}(H)=4\). Thus its exact single-graph price of connectivity is \(7/4\).

**Complete classification.** Every minimum connected feedback vertex set is a seven-vertex subset \(S\) for which **both** \(H[S]\) and \(H[V(H)\setminus S]\) are induced trees. Conversely every such partition gives a minimum connected feedback vertex set. There are exactly **770** choices of \(S\), or **385** unordered partitions of the fourteen vertices into two induced seven-vertex trees. They form five orbits under the full automorphism group of order 336, of sizes \(42,56,168,168,336\).

**Exact exchange geometry.** Let \(\mathcal R\) have these 770 sets as vertices, with \(S,T\) adjacent if \(|S\setminus T|=|T\setminus S|=1\), so one selected vertex may be relocated while keeping the connected-feedback property and minimum cardinality. Then \(\mathcal R\) is connected and has **6,888** edges. Its degrees are precisely \(16\) (378 configurations), \(18\) (56 configurations), and \(20\) (336 configurations). Every vertex has eccentricity seven, so its radius and diameter are both seven. In fact, for every two distinct optimal sets,
\[
  d_{\mathcal R}(S,T)\in\{7-|S\cap T|,\;8-|S\cap T|\}.
\]
Among its \(\binom{770}{2}=296065\) unordered pairs, **5,460** require the extra exchange. Exactly **385** pairs have distance seven; these are precisely the complementary pairs \(\{S,V(H)\setminus S\}\). Every solution has its own complementary tree as its unique antipode.

The full unordered-pair distance distribution is:

| Exchange distance | Unordered pairs |
|---|---:|
| 1 | 6,888 |
| 2 | 39,312 |
| 3 | 97,524 |
| 4 | 104,412 |
| 5 | 40,656 |
| 6 | 6,888 |
| 7 | 385 |

## Assumptions and scope

Graphs are finite, simple, undirected and vertex-labeled for counting purposes. Let \(\mathbb F_2^3\) have seven nonzero vectors. The point vertices are those seven vectors and the line vertices are their seven nonzero normal vectors. Join a point \(p\) to a normal \(a\) exactly when their mod-two dot product vanishes: \(p\cdot a=0\). This constructs the Fano incidence graph \(H\). The alternative Hamiltonian description is a fourteen-cycle with seven chords in LCF notation \([5,-5]^7\). Both are three-regular and each has twenty-one edges; the verifiers explicitly identify them by a vertex permutation.

A forest can have multiple connected components; a tree is connected and acyclic. **Connected feedback set** means the selected set itself induces a connected graph, not that the remaining forest is connected. The conclusion that the complement is a tree at optimum is a derived property. Exchange uses arbitrary one-vertex replacement (token jumping), not a requirement that the removed and inserted vertices be adjacent in \(H\). The results concern exactly this one fourteen-vertex graph, with no unproved extension to larger cages or arbitrary projective planes.

## Proof

**1. A general lower bound and equality condition.** Suppose \(G\) is a cubic graph on \(2m\) vertices, and \(S\) is a connected feedback vertex set with \(k\) vertices. The bound \(k\ge m\) is immediate if \(k=2m\), so assume \(k<2m\) and the complement is nonempty. Write \(e_G(S)\) for edges internal to \(S\). Connectedness gives \(e_G(S)\ge k-1\). There are \(3m\) edges in all. Deleting \(S\) deletes \(3k-e_G(S)\) edges, so the induced forest on \(2m-k\) vertices has
\[
3m-3k+e_G(S)\ge3m-2k-1
\]
edges. Any forest on the positive number \(2m-k\) of remaining vertices has at most \(2m-k-1\) edges. Thus \(k\ge m\). If \(k=m\), equality must hold in both inequalities: \(e_G(S)=m-1\), so the connected selected graph is a tree, and the complement has \(m-1\) edges on \(m\) vertices, so it too is a tree. Conversely, any bisection into two induced \(m\)-vertex trees is a connected feedback vertex set of size \(m\) and achieves the lower bound.

For \(H\), set \(m=7\). An explicit qualifying bisection is verified in the Fano labeling, for example \(S=\{0,1,3,4,5,7,8\}\), where point vertices are labeled zero through six and normal vertices seven through thirteen, corresponding respectively to nonzero binary vectors numbered one through seven. Consequently \(\operatorname{cfvs}(H)=7\), and the claimed complementary-tree condition is necessary and sufficient.

**2. Exact finite count, with no sampling.** The first standalone verifier constructs the Fano incidence adjacency relation from the seven nonzero binary vectors. It examines every one of the \(\binom{14}{7}=3432\) seven-subsets. For each \(S\), it checks connectivity of the selected induced subgraph by full transitive closure, then computes connected components and internal edge counts of the complement. An induced subgraph is a forest precisely if its edge count equals its vertex count minus its component count. The test finds exactly 770 qualifying seven-subsets, and directly verifies that each complement is also a tree. The exact algorithm and full finite domain are provided in `verify_fano.py`.

An independently constructed verifier, `verify_hamilton.cpp`, builds \(H\) as a cycle with the seven LCF chords and performs a separately implemented exhaustive check of all \(2^{14}=16384\) vertex masks and all connected feedback sets of cardinality at most seven. Its same conclusion is not inferred from the first program's data or tables. The first verifier also tests the explicit permutation
\[
(0,4,6,2,10,12,8,3,1,7,5,9,13,11)
\]
from its incidence vertex numbering to the fourteen-cycle numbering, confirming every adjacency. The two different graph constructions therefore compute the same labeled graph invariant. The ordinary four-vertex feedback count of 70 is a consistency check against an existing exact classification, not asserted as new.

**3. Symmetry orbits.** For each invertible linear transformation of \(\mathbb F_2^3\), the induced point permutation and inverse-transpose normal permutation form an automorphism of the Fano incidence graph. There are \(168\) such transformations. Combining them with the polarity interchanging each point vector and its corresponding line normal gives \(336\) distinct graph automorphisms. Explicit adjacency tests certify every permutation. Computing the image of all 770 solutions under all these automorphisms partitions them into disjoint orbits with cardinalities \(42,56,168,168,336\), which sum to 770. The standard full automorphism group of \(H\) is known to have order 336, so these are its full orbits.

**4. Exchange distance and complementary antipodes.** For each optimum \(S\), exhaustively enumerate its 49 potential exchanges of one selected and one unselected vertex; retain an edge exactly when the resulting mask belongs to the complete set of 770 optima. This finds an undirected graph with 6,888 edges and degree multiplicities as stated. Breadth-first search from **each** of the 770 vertices reaches all 770, certifying connectedness and every exact shortest-path distance. The independently coded C++17 verifier constructs the same exchange relation and performs its own all-start-vertex breadth-first searches. Both compute the table above, eccentricity seven at every vertex and the precise detour count.

Every exchange can replace at most one member of \(S\setminus T\), so the Johnson distance \(7-|S\cap T|\) is a lower bound. For each of the \(\binom{770}{2}\) unordered pairs the two exhaustive programs check whether the distance equals this bound or exceeds it by one. Exactly 5,460 pairs have excess one and none have larger excess. Every complementary pair has disjoint selected sets and hence lower bound seven; since the diameter is seven, each is at distance seven. There are 385 complementary pairs, and the complete distance table has exactly 385 distance-seven pairs. Hence each complement is the unique antipode of the other.

**5. Unrestricted comparison.** For a cubic fourteen-vertex graph, deletion of an arbitrary four-set leaves \(9+e_G(S)\) edges on ten vertices. Acyclicity therefore forces independence and one component at cardinality four; the full enumeration yields exactly 70 such sets. This agrees with the existing published result for \(H\). The connectivity requirement raises the minimum from four to seven, as demonstrated independently in step 1. The general cubic edge-count lower bound is elementary and not itself presented as a new discovery.

## Verification

Two self-contained source files use only standard Python 3 and a C++17 compiler. Run `python3 verify_fano.py`, then `c++ -std=c++17 -O2 verify_hamilton.cpp -o verify_hamilton && ./verify_hamilton`. The programs print `PASS` and reproduce 70 ordinary four-sets, 770 connected seven-sets, 385 complement pairs, 6,888 exchange edges, the degree and distance distributions, and the 5,460 one-step excess pairs. The Python verifier additionally confirms all 336 automorphisms, five orbit sizes and an explicit isomorphism to the Hamiltonian construction.

These are exact finite proofs for the single graph: the membership and distance loops cover the full stated finite domains and use integer operations only. A successful source execution is corroborating evidence; the logic of the enumeration, the explicit graph constructions and completeness of the loops are part of the certificate. Nothing is extrapolated from a sample or from a timeout.

## Relationship to prior work

Belmonte, van 't Hof, Kamiński and Paulusma study the **price of connectivity** for feedback vertex sets, giving the standard terminology and structural questions on graph classes. Their inspected 2015 preprint focuses on forbidden-induced-subgraph characterizations and does not supply the exact Heawood census or its exchange metric. Esperet, Lemoine and Maffray study equitable partitions into induced forests. Their 2014 preprint provides broad partition principles, not a count or connectedness classification for complementary induced seven-vertex **trees** in \(H\).

The published *All seventy minimum feedback-vertex sets of the Heawood graph* (2026) establishes the unconstrained cardinality four, all 70 optimum sets, and their two automorphism orbits. That result is credited rather than reproduced as original. It does not imply the new constrained optimum seven, 770 connected optima, complementary tree bisections, five symmetry orbits, or the exact exchange distances. The published *A wedge of eight 8-spheres and Steinberg symmetry of the Heawood induced-forest complex* (2026) computes the homotopy and representation of the full induced-forest complex; it does not classify **simultaneously connected** complementary tree halves or their exchanges. The ordinary forest face numbers in that result cannot directly determine the connected bisection count.

General cubic decycling identities, including those of Ren, Yang and Zhao, explain edge-accounting lower bounds but do not give this exact census. A 1993 paper by Goddard, Henning, Oellermann and Swart about trees *framed* by the Heawood graph has a different definition of “frame”: an embedding property of larger trees, not two-tree vertex partitions. Only its abstract was available. Nedela and Škoviera's 2022 cyclic-connectivity work gives a related existence perspective for cubic graphs, but its abstract does not state this Heawood enumeration; full-text priority comparison remains incomplete. These access limits are acknowledged as residual risks, not treated as proof of novelty.

## Limitations

This is an exact finite claim for one graph, not a general theorem enumerating connected feedback vertex sets of all regular graphs. The upper bound, census and reconfiguration properties rely on complete finite enumeration and full-distance searches provided in the stand-alone verifiers. The published primary sources and mathematical-result records that were accessible revealed no equivalent coverage; this cannot exclude prior unpublished enumerations or statements in inaccessible full texts. No independent external audit has been performed.

## References

- L. Esperet, L. Lemoine and F. Maffray, *Equitable partition of graphs into induced forests*, arXiv:1410.0861v1, first posted 3 October 2014, https://arxiv.org/abs/1410.0861.
- R. Belmonte, P. van 't Hof, M. Kamiński and D. Paulusma, *The Price of Connectivity for Feedback Vertex Set*, arXiv:1510.02639v1, first posted 9 October 2015, https://arxiv.org/abs/1510.02639.
- *All seventy minimum feedback-vertex sets of the Heawood graph*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-all-seventy-minimum-feedback-vertex-sets-of-the-heawood-graph--83a003d33b54.
- *A wedge of eight 8-spheres and Steinberg symmetry of the Heawood induced-forest complex*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-wedge-of-eight-8-spheres-and-steinberg-symmetry-of-the-heawood--07bd367089bb.
- A. E. Brouwer, *Heawood graph*, https://aeb.win.tue.nl/graphs/Heawood.html.
- H. Ren, C. Yang and T.-X. Zhao, *A new formula for the decycling number of regular graphs*, Discrete Math. **340** (2017), 3020–3031, https://doi.org/10.1016/j.disc.2017.07.011.
- W. Goddard, M. A. Henning, O. R. Oellermann and H. C. Swart, *Which trees are uniquely framed by the Heawood graph?*, Quaest. Math. **16** (1993), 237–251, https://doi.org/10.1080/16073606.1993.9631736 (abstract inspected; full text not inspected).
- R. Nedela and M. Škoviera, *Cyclic connectivity, edge-elimination, and the twisted Isaacs graphs*, J. Combin. Theory Ser. B (2022), https://doi.org/10.1016/j.jctb.2022.01.007 (abstract inspected; full text not inspected).
