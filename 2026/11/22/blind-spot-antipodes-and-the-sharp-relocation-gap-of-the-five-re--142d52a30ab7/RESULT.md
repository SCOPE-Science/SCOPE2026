# Blind-spot antipodes and the sharp relocation gap of the five-regular Clebsch graph

## Finding

Let \(G\) be the **five-regular** Clebsch graph (the folded five-cube, not its ten-regular complement). A power-dominating placement is a vertex set whose closed neighborhood, followed by ordinary zero-forcing propagation, observes every vertex. Then:

1. The power-domination number is \(\gamma_P(G)=3\). A three-vertex set succeeds **if and only if** it induces an independent triple or a three-vertex path. There are \(160\) of each, hence \(320\) minimum placements; every successful triple finishes in one propagation wave following initial closed-neighborhood observation.
2. For any minimum placement \(S\), let \(U(S)=V(G)\setminus N_G[S]\), its initially unobserved *blind-spot triple*. The map \(U\) is a fixed-point-free involution on the minimum placements and switches the independent-triple and path-triple types.
3. The unrestricted one-token-jump reconfiguration graph \(R_J\) is connected and \(21\)-regular with \(3{,}360\) edges, radius and diameter \(3\). The adjacency-restricted token-slide graph \(R_S\) is also connected, has \(1{,}120\) edges, and has radius and diameter \(6\). An independent triple has slide degree \(9\), while a path triple has slide degree \(5\).
4. For every optimum \(S\), **its unique configuration at slide distance \(6\) is \(U(S)\)**, and the jump distance from \(S\) to \(U(S)\) is \(3\). Over all \(\binom{320}{2}=51{,}040\) unordered optimum pairs, the largest extra distance imposed by sliding is exactly \(3\) moves, attained by exactly the \(160\) involution pairs \(\{S,U(S)\}\); the counts with extra distances \(0,1,2,3\) are respectively \(12{,}560,27{,}520,10{,}800,160\).

This is an exact finite graph theorem. The graph, feasible configurations and all shortest-path constraints are specified below.

## Assumptions and scope

Write the vertex set as the sixteen binary four-vectors, encoded by the integers \(0,\ldots,15\). Addition is bitwise XOR \(\oplus\). Put
\[
C=\{1,2,4,8,15\},\qquad
E(G)=\{\{a,a\oplus c\}:a\in\{0,\ldots,15\},\ c\in C\}.
\]
This is the Cayley form of the five-regular Clebsch graph, with \(16\) vertices and \(40\) undirected edges.

For a nonempty initial set \(S\), define \(P^0[S]=S\), \(P^1[S]=N_G[S]\), and for \(t\ge1\)
\[
P^{t+1}[S]=P^t[S]\cup\{w:\exists v\in P^t[S],\ N_G(v)\setminus P^t[S]=\{w\}\}.
\]
A set power dominates when \(P^t[S]=V(G)\) for some \(t\). Let \(\mathcal M\) be the family of minimum-cardinality power-dominating sets. The vertices of \(R_J\) and \(R_S\) are \(\mathcal M\); they join distinct sets \(S,T\) when \(|S\setminus T|=|T\setminus S|=1\), and additionally, for \(R_S\), the removed and inserted vertices must be adjacent **in the original graph** \(G\). All graph distances below refer to these reconfiguration graphs, not to \(G\).

## Proof

**I. Symmetry reduction and optimum-set classification.** The five generators in \(C\) sum to zero and any four are linearly independent. Thus every permutation of them extends to a linear automorphism of \(G\); translations by vertices are also automorphisms. The resulting group acts transitively on one- and two-vertex configurations of each adjacency type, and on triples inducing any specified one of the three possible edge counts \(0,1,2\). Here is a direct justification of the triple assertion. After translating a vertex to \(0\), its five neighbors correspond to the five generators. Its ten nonneighbors correspond uniquely to unordered sums of two distinct generators. Two such nonneighbors are adjacent precisely when their two-element generator-index sets are disjoint. Permutations of five indices are transitive on (a) two distinct neighbors, (b) intersecting pairs of two-element subsets, and (c) disjoint pairs of two-element subsets. Since \(G\) has no triangles, these are precisely the three induced triple types.

One can therefore test all one- and two-element sets, and all three triple types, by the following complete list of representatives. The fourth column gives whether some observed vertex has *exactly one* initially unobserved neighbor; whenever the answer is yes, all initially unseen vertices are forced in the same wave.

| Configuration type | Representative \(S\) | \(V(G)\setminus N_G[S]\) | Propagation outcome |
|---|---|---|---|
| One vertex | \(\{0\}\) | Ten vertices | Stalled |
| Adjacent pair | \(\{0,1\}\) | \(\{6,7,10,11,12,13\}\) | Stalled |
| Nonadjacent pair | \(\{0,3\}\) | \(\{5,6,9,10,13,14\}\) | Stalled |
| Induced path | \(\{0,1,2\}\) | \(\{7,11,12\}\) | All three forced next wave |
| Single edge plus isolate | \(\{0,1,6\}\) | \(\{10,11,12,13\}\) | Stalled |
| Independent triple | \(\{0,3,5\}\) | \(\{6,9,14\}\) | All three forced next wave |

The assertions in the last column follow by listing the five XOR-neighbors of each observed vertex. For example, from \(\{0,1,2\}\), vertices \(5,9,13\) each uniquely force respectively \(7,11,12\); for \(\{0,3,5\}\), vertices \(2,8,10\) uniquely force \(6,9,14\). Each stalled representative has no observed vertex with just one unseen neighbor. Thus no set of size at most two succeeds, while exactly the induced independent triples and paths succeed.

The number of induced paths is \(16\binom52=160\) (choose the unique center and two neighbors). The number of induced triples with exactly one edge is \(40\cdot6=240\), since a chosen edge has exactly six vertices adjacent to neither endpoint. As there are \(\binom{16}{3}=560\) triples and no triangles, the independent triples number \(560-160-240=160\). This proves the first assertion.

**II. Blind-spot involution.** All optimum sets have three vertices outside their closed neighborhood. For the two orbit representatives above,
\[
U(\{0,1,2\})=\{7,11,12\},\quad
U(\{0,3,5\})=\{6,9,14\}.
\]
Direct substitution into the same XOR-neighborhood formula gives
\[
U(\{7,11,12\})=\{0,1,2\},\quad
U(\{6,9,14\})=\{0,3,5\}.
\]
In each case the blind-spot triple has the opposite induced type. The operation \(U\) commutes with every graph automorphism, so the two orbit representatives establish the involution and type-switching assertions for all \(320\) optima. Furthermore \(S\cap U(S)=\varnothing\).

**III. Reconfiguration counts.** Each unrestricted one-token replacement can be enumerated by retaining two members of the triple and selecting a new vertex from the thirteen not currently selected; the slide rule further requires an original edge. The two symmetry representatives give all replacement-degree counts:

| Source type | Jump: same type | Jump: other type | Slide: same type | Slide: other type |
|---|---:|---:|---:|---:|
| Independent triple | 15 | 6 | 6 | 3 |
| Induced path | 15 | 6 | 2 | 3 |

For unrestricted jumping, the degree is \(21\) in either class, whence \(|E(R_J)|=320\cdot21/2=3360\). For sliding, the degree is \(9\) on the \(160\) independent triples and \(5\) on the \(160\) paths, whence \(|E(R_S)|=(160\cdot9+160\cdot5)/2=1120\). The slide graph has \(480\) independent-to-independent, \(160\) path-to-path, and \(480\) cross-type edges.

**IV. Certified distances and unique antipodes.** For either legal-move graph, the shortest-distance layers from a source \(s\) are computed by the finite exact recurrence
\[
L_0(s)=\{s\},\quad
L_{j+1}(s)=\Bigl(\bigcup_{x\in L_j(s)}N_R(x)\Bigr)
\setminus\Bigl(\bigcup_{i=0}^{j}L_i(s)\Bigr).
\]
Here \(N_R(x)\) is constructed directly from the explicit triple classification and original Cayley edges. The following **complete layer cardinalities**, independently reproduced by the attached programs, are from the two exhaustive orbit representatives; blank entries mean zero:

| Move rule and source | Layer \(0\) | \(1\) | \(2\) | \(3\) | \(4\) | \(5\) | \(6\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Jump; either representative | 1 | 21 | 126 | 172 | 0 | 0 | 0 |
| Slide; independent \(\{0,3,5\}\) | 1 | 9 | 45 | 122 | 118 | 24 | 1 |
| Slide; path \(\{0,1,2\}\) | 1 | 5 | 28 | 108 | 141 | 36 | 1 |

Every row sums to \(320\); hence both move graphs are connected. The jump graph is self-centered with eccentricity \(3\), and the slide graph is self-centered with eccentricity \(6\). The unique last-layer triples are respectively \(\{6,9,14\}\) and \(\{7,11,12\}\), exactly the computed blind spots. Automorphism transitivity on the two triple types proves the same uniqueness for every optimum. Since \(S\) and \(U(S)\) are disjoint triples, their jump distance is at least \(3\), and the jump layer table proves it is exactly \(3\).

Finally, applying the same recurrence to all \(320\) sources, and comparing the two distance matrices for all \(51{,}040\) unordered pairs, gives the following **exact certificate values**:

| Distance | Jump pair count | Slide pair count |
|---|---:|---:|
| 1 | 3,360 | 1,120 |
| 2 | 20,160 | 5,840 |
| 3 | 27,520 | 18,400 |
| 4 | 0 | 20,720 |
| 5 | 0 | 4,800 |
| 6 | 0 | 160 |

The distribution of \(d_{R_S}(S,T)-d_{R_J}(S,T)\) is \(12{,}560,27{,}520,10{,}800,160\) for values \(0,1,2,3\). The exactly \(160\) pairs with excess \(3\) are all the unique blind-spot antipode pairs established above. For a concrete witness,
\[
\{0,1,2\}\to\{1,2,4\}\to\{2,4,9\}\to\{3,4,9\}
\to\{3,4,11\}\to\{3,11,12\}\to\{7,11,12\}
\]
is a valid six-slide path. A three-jump path is
\[
\{0,1,2\}\to\{1,2,7\}\to\{2,7,11\}\to\{7,11,12\}.
\]
The finite exhaustive recurrence rules out shorter slide paths. This completes the proof.

## Verification

The attached `check_cayley.py` constructs the graph from bitwise XOR, tests all \(16+\binom{16}{2}+\binom{16}{3}=696\) nonempty candidate sets of sizes at most three, classifies all successful triples, constructs both reconfiguration adjacency lists, and computes all pairwise shortest-path distances. It checks the involution and its unique-antipode property for every configuration, and asserts all published counts and distance distributions.

The independent implementation `check_setmodel.py` constructs the same graph from the empty set, five singleton labels and ten two-label subsets. Its adjacency is empty-to-singleton, singleton-to-incident-pair, and between disjoint pairs. It uses a separate observation procedure, constructs the move graphs by **pairwise configuration comparison**, and independently checks all shortest distances and blind spots. Both scripts need only Python 3's standard library and can be run separately:

```bash
python3 check_cayley.py
python3 check_setmodel.py
```

Both produced `PASS` and the numerical tables reported above. Exact finite enumeration supports the finite claims here; no extension to all strongly regular graphs or higher-dimensional folded cubes is asserted.

## Relationship to prior work

Bjorkman et al., *Power domination reconfiguration* (arXiv version first publicly posted 2022-01-05, later journal publication in 2026), develops the general minimum-set token-jump framework and definitions. Its Section 5.1 treats complete graphs, complete bipartite graphs, paths, cycles and wheels. The inspected preprint and journal full text do **not** give the five-regular Clebsch optimum-set classification, the induced-type mobility degrees, or the neighborhood-complement antipodal involution. The general reconfiguration definitions and universal statements are foundational inputs here, not claimed as new.

Clebsch graph references such as MathWorld determine the graph's construction and strongly regular parameters, but these parameters alone do not determine the power-domination closure or the two relocation metrics. Indexed exact Clebsch classifications for locating domination, vertex-metric resolution and edge-metric resolution concern different feasibility predicates; none of their stated conclusions implies the claim here. The comparisons establish a reasonable current priority assessment, not mathematical uniqueness or a guarantee that no obscure historical equivalent exists.

## Limitations

This is a theorem about one fixed sixteen-vertex graph and its minimum power-dominating configurations. The exhaustive searches are complete for that explicitly specified graph, not for any broader graph class. The two code paths are algorithmically different but do not amount to an external independent scientific audit. Historical priority may be affected by literature not indexed or not found in the documented search. No claim is made that sensor relocation on an actual electrical grid has the same edge-cost model.

## References

1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob, C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798v1, 2022-01-05, https://arxiv.org/html/2201.01798v1 .
2. Same authors, *Power Domination Reconfiguration*, La Matematica 5, article 8 (2026), https://doi.org/10.1007/s44007-025-00187-5 . This is a later version of Reference 1, not a distinct first-publication date.
3. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html .
4. A. E. Brouwer, *Clebsch graph* (including explicit naming distinction for the folded cube and its complement), https://jaanos.github.io/tables/graphs/Clebsch.html .
