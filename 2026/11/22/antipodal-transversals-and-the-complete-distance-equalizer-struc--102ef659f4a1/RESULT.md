# Antipodal transversals and the complete distance-equalizer structure of the dodecahedral graph

## Finding

Let \(D=GP(10,2)\) denote the 20-vertex dodecahedral graph. A **distance-equalizer set** \(S\subseteq V(D)\) has the property that each distinct \(u,v\notin S\) admit a witness \(w\in S\) with \(d(u,w)=d(v,w)\). The exact classification is

\[
S\text{ is a distance-equalizer set}\quad\Longleftrightarrow\quad
|S\cap\{x,\bar x\}|\ge 1\text{ for every antipodal pair }\{x,\bar x\}.
\]

Here \(\bar x\) is the unique vertex at graph distance five from \(x\), and the ten antipodal pairs partition the vertex set. Thus the complete cardinality polynomial is

\[
E_D(z)=\sum_{S\text{ distance-equalizing}}z^{|S|}=(2z+z^2)^{10},
\]

and the equidistant dimension equals \(\xi(D)=10\). All 1024 minimum equalizer sets choose exactly one endpoint of each antipodal pair; no larger equalizer is inclusion-minimal.

The full 120-element automorphism group acts on these 1024 sets in exactly **20** orbits: two orbits of size 12, four of size 20, two of size 40, ten of size 60, and two of size 120. The one-vertex replacement (token-jump) reconfiguration graph on minimum equalizers is \(Q_{10}\), with diameter ten; if replacements must move along graph edges, all 1024 configurations are isolated.

## Assumptions and scope

Define the graph on vertices \(o_i,p_i\), with \(i\in\mathbb Z/10\mathbb Z\). Its edges are the unordered pairs \(o_io_{i+1}\), \(o_ip_i\), and \(p_ip_{i+2}\), for each index \(i\). The antipodal involution is \(\bar o_i=o_{i+5}\), \(\bar p_i=p_{i+5}\). Every distance is an ordinary unweighted shortest-path distance. The result concerns this graph, not every generalized Petersen graph.

A token jump exchanges exactly one selected vertex with one unselected vertex and preserves the number of selected vertices and the distance-equalizer property. A token slide additionally requires these two vertices to be adjacent in \(D\). Configurations are vertex subsets, not ordered sequences; vertices of the graph remain labeled.

## Proof

**1. Antipodal distances.** The graph's adjacency rule determines all pair distances by breadth-first search. The resulting finite distance certificate, reproduced by `verify_direct.cpp`, establishes that the diameter is five and, for every vertex \(x\), the only vertex at distance five is \(\bar x\), with

\[
d(w,x)+d(w,\bar x)=5\qquad\text{for all }w\in V(D).
\]

Hence no vertex is equidistant from an antipodal pair, since equal integer distances would sum to the odd number five. If a distance-equalizer set omitted both endpoints of such a pair, the defining condition would fail. This proves the necessary ten pair-hitting conditions.

**2. The finite non-antipodal witness lemma.** For every pair of distinct vertices \(u,v\) with \(d(u,v)<5\), its equalizer set

\[
W(u,v)=\{w:d(w,u)=d(w,v)\}
\]

consists of exactly **two complete antipodal pairs** (four vertices). This finite assertion can be reconstructed without a graph library by breadth-first search and checking all \(\binom{20}{2}=190\) unordered vertex pairs; the certificate `verify_direct.cpp` makes exactly these checks. For an additional hand-checkable reduction, the graph has a 120-element automorphism group transitive on each distance sphere around \(o_0\). One representative at distance \(r\in\{1,2,3,4,5\}\) is \(o_r\), with the corresponding equalizer lists (using the indexing \(o_i=i\), \(p_i=10+i\)):

| \(r\) | \(W(o_0,o_r)\) |
|---:|---|
| 1 | \(\{p_2,p_4,p_7,p_9\}\) |
| 2 | \(\{o_1,o_6,p_1,p_6\}\) |
| 3 | \(\{p_1,p_2,p_6,p_7\}\) |
| 4 | \(\{o_2,o_7,p_2,p_7\}\) |
| 5 | \(\varnothing\) |

The sphere-transitivity and all 120 automorphisms are checked independently in `verify_symmetry.py`: every automorphism is determined by the image of a fixed oriented two-edge path, because the 20 triples of distances to its three ordered vertices are distinct. The program constructs the 120 candidate mappings from the 120 oriented two-edge paths and verifies adjacency preservation, proving that none are missing and that each distance sphere is one orbit of the root stabilizer. Alternatively, the first certificate directly verifies the lemma without invoking transitivity.

**3. Sufficiency and counting.** Suppose \(S\) intersects every antipodal pair. Then any two vertices \(u,v\notin S\) cannot be antipodal. By step 2, the equalizer set \(W(u,v)\) contains two whole antipodal pairs, each intersecting \(S\), so a witness belongs to \(W(u,v)\cap S\). Thus \(S\) is a distance-equalizer set. For each of the ten disjoint pairs one may choose its first endpoint, its second endpoint, or both, giving independent weights \(z,z,z^2\), proving \(E_D(z)=(2z+z^2)^{10}\). Minimum sets take exactly one endpoint of each pair, so there are \(2^{10}=1024\).

**4. Symmetry and mobility.** Every minimum set corresponds bijectively to a binary word of length ten, indicating which endpoint is selected in each antipodal pair. Changing one selected vertex while preserving minimality necessarily flips exactly one such bit; hence the token-jump graph is \(Q_{10}\). Since antipodal vertices lie at graph distance five, no such flip is a graph-edge slide, and the token-slide graph has zero edges. To obtain the full automorphism orbit census, act on all 1024 binary-word subsets using the 120 adjacency-preserving permutations from step 2. Their disjoint orbit sizes are \(12,12;20\) repeated four times; \(40\) repeated twice; \(60\) repeated ten times; and \(120\) repeated twice. These sum to 1024 and constitute exactly 20 orbits. This is a complete finite enumeration, not an inference from only a sample.

## Verification

Two standalone source programs are included. `verify_direct.cpp` builds the adjacency lists, calculates all 20 breadth-first distance vectors, verifies all 190 witness sets and the antipodal identity, and **directly tests the distance-equalizer definition on all \(2^{20}=1,048,576\) vertex subsets**, confirming equivalence to the ten pair-hitting conditions and every coefficient of the polynomial. Its complete polynomial has 59,049 feasible subsets.

`verify_symmetry.py` separately rebuilds the graph, constructs all 120 automorphisms from rooted distance signatures, proves full enumeration by a 120-possibility upper bound, checks distance-sphere transitivity, computes all 20 orbits, and verifies that each minimum set has ten jump-neighbors and no slide-neighbors. Exact commands and expected deterministic output appear in `VERIFICATION.md`. Both files use only C++17 or the Python standard library, with no remote dependencies or data tables.

## Relationship to prior work

González, Hernando and Mora introduced distance-equalizer sets in the 2021 preprint `arXiv:2107.10805`, later published in 2022, and treated complete and complete multipartite graphs, bistars, paths, cycles, and Johnson graphs; they did not give this dodecahedral classification in the inspected full text. Kratica, Čangalović and Kovačević-Vujčić studied Johnson and Kneser families in `arXiv:2406.17870`; their general empty-witness necessary condition agrees with step 1, but neither proves the finite sufficiency lemma nor enumerates dodecahedral solutions. Savić, Maksimović, Bogdanović and Kratica studied other families of graph-theoretic convex polytopes (`arXiv:2407.15307`), not the regular dodecahedron. Later Cartesian-product results do not cover this cubic girth-five graph.

An earlier complete **metric resolving** polynomial for the dodecahedral graph depends on hitting at least three antipodal pairs, whereas distance equalization here requires hitting **all ten**. Resolving witnesses have *unequal* distances, the opposite predicate, so the prior result does not imply this polynomial or reconfiguration structure. These comparisons indicate no identified direct coverage; a search cannot establish global publication priority.

## Limitations

This is an exact theorem for one canonical finite graph, with an explicitly enumerated finite witness lemma and orbit census. It does not determine the invariant for an infinite generalized Petersen family or prove that no unpublished or unindexed equivalent result exists. The proof is reproducible from the supplied finite code and stated combinatorial reductions; independent mathematical audit has not been carried out.

## References

1. A. González, C. Hernando, M. Mora, *The Equidistant Dimension of Graphs*, first public 22 July 2021, `arXiv:2107.10805`, https://arxiv.org/abs/2107.10805; *Bulletin of the Malaysian Mathematical Sciences Society* (2022), https://doi.org/10.1007/s40840-022-01295-z.
2. J. Kratica, M. Čangalović, V. Kovačević-Vujčić, *Equidistant dimension of Johnson and Kneser graphs*, first public 25 June 2024, `arXiv:2406.17870`, https://arxiv.org/abs/2406.17870.
3. A. Savić, Z. Maksimović, M. Bogdanović, J. Kratica, *The equidistant dimension of some graphs of convex polytopes*, first public 22 July 2024, `arXiv:2407.15307`, https://arxiv.org/html/2407.15307v1.
4. A. Gispert-Fernández, J. A. Rodríguez-Velázquez, I. G. Yero, *Equidistant dimension of Cartesian product graphs*, first published 20 April 2026, https://doi.org/10.1007/s40840-026-02088-4.
