# Locating domination and relocation geometry of the five-regular Clebsch graph

## Finding
For the standard five-regular Clebsch graph \(C\), the minimum size of a locating-dominating set is \(5\). There are exactly \(416\) such sets. Their induced subgraphs consist of precisely three types: \(16\) independent five-sets, \(320\) sets inducing a single edge together with three isolated vertices, and \(80\) sets inducing a four-leaf star.

In the one-vertex token-jump reconfiguration graph on these \(416\) minimum sets, two states are joined when one selected vertex is replaced by an arbitrary unselected vertex, preserving the locating-dominating condition. This graph has \(2,960\) edges, is connected, and has radius \(5\) and diameter \(6\). Its degrees on the three types (independent, single-edge, star) are respectively \(25,15,9\).

Requiring each replacement to follow an edge of \(C\) defines token sliding. Its graph has \(1,360\) edges, is connected, has radius \(6\) and diameter \(7\), and has respective type-degrees \(25,7,1\). Thus all \(80\) star states are pendant vertices in the slide graph, while no state is isolated. The exact distributions of eccentricities and intertype edges are given below and reproduced by two standalone verification programs.

## Assumptions and scope
All graphs are finite, simple, and undirected. In \(C\), the vertices are the sixteen even-parity five-bit words; words \(u,v\) are adjacent exactly when their Hamming distance is four. Equivalently \(C\) is the Cayley graph on \(\mathbb F_2^4\) with generator set \(\{1,2,4,8,15\}\), using four-bit integer labels.

For \(S\subseteq V(C)\), write \(N(v)\) for the open neighborhood. We call \(S\) locating-dominating if for every \(v\notin S\) the trace \(N(v)\cap S\) is nonempty, and these traces are pairwise distinct as \(v\) varies over the complement. This condition imposes no trace comparison for vertices inside \(S\). All relocation graphs discussed here have only minimum locating-dominating sets as their vertices, and each move exchanges exactly one selected vertex for one unselected vertex.

## Proof
**Minimum cardinality.** If \(|S|\le3\), the \(16-|S|\) outside vertices cannot receive distinct nonempty subsets of \(S\): there are at most \(2^{|S|}-1\) such subsets. If \(|S|=4\), twelve outside vertices would require twelve different nonempty signatures on four selected vertices. The smallest possible total incidence count of twelve such subsets is \(4\cdot1+6\cdot2+2\cdot3=22\). But the sum of outside-neighbor incidences is at most \(4\cdot5=20\), a contradiction. Therefore every locating-dominating set has at least five vertices.

**Exact classification.** Label the even-weight five-bit words in increasing numeric order as \(w_0,\ldots,w_{15}\). Define the adjacency masks \(a_i=\sum_{j:d_H(w_i,w_j)=4}2^j\). For each five-subset represented by bitmask \(s\), test the eleven outside signatures \(a_i\mathbin{\&}s\). The set is locating-dominating if and only if all eleven masks are positive and pairwise unequal. Exhaust all \(\binom{16}{5}=4,368\) masks by increasing five-index combinations. Sorting the five induced degrees \(\operatorname{popcount}(a_i\mathbin{\&}s)\), the exhaustive identity is:

| Induced type | All five-sets of this type | Locating-dominating five-sets |
| --- | ---: | ---: |
| \(5K_1\) | 16 | 16 |
| \(K_2\sqcup3K_1\) | 320 | 320 |
| \(K_{1,4}\) | 80 | 80 |
| Other types | 3,952 | 0 |

These are exact complete finite calculations, not extrapolations. They are reproduced by `verify_even5.py` with assertions testing the equivalence on *each* five-subset and independently by `verify_folded4.cpp`, which iterates every sixteen-bit subset mask in the isomorphic four-bit Cayley representation. They verify existence of a five-set and hence the matching lower bound.

The structural counts have independent explanations. The independent five-sets are exactly the sixteen open neighborhoods; this is directly checked against the full enumeration. The stars are obtained by choosing one of sixteen centers and four of its five neighbors, giving \(16\binom{5}{4}=80\). For each of the forty edges \(uv\), the vertices outside \(N[u]\cup N[v]\) induce three disjoint edges on six vertices (this finite property is directly checked on each edge). Thus a five-set whose only internal edge is \(uv\) consists of \(u,v\) and one endpoint of each of these three other edges; there are \(2^3=8\) choices per edge, hence \(40\cdot8=320\). The exhaustive trace test proves that these constructions are exactly the feasible ones and that no other induced type qualifies.

**Relocation and distances.** Given two recorded feasible masks \(s,t\), test whether \(\operatorname{popcount}(s\mathbin\triangle t)=2\). This is exactly a legal token jump. It is a slide precisely when the unique removed and inserted vertices are adjacent in \(C\). Construct both finite graphs with these exact predicates and run complete breadth-first search from **every one** of the \(416\) states. The complete degree, adjacency and distance outputs are:

| Property | Jump | Slide |
| --- | ---: | ---: |
| Edges | 2,960 | 1,360 |
| Connected components | 1 | 1 |
| Radius | 5 | 6 |
| Diameter | 6 | 7 |
| Vertex eccentricity counts | \(e_5:16,\ e_6:400\) | \(e_6:336,\ e_7:80\) |
| Degrees on independent / single-edge / star states | 25 / 15 / 9 | 25 / 7 / 1 |

Among unordered pairs of different structural types, the jump graph has 320 independent--single-edge edges, 80 independent--star edges, and 320 single-edge--star edges; it also has 2,080 single-edge--single-edge and 160 star--star edges. The slide graph has 320 independent--single-edge, 80 independent--star, and 960 single-edge--single-edge edges and no others. In particular, each star has exactly one slide, and every state remains in the single connected component. The finite exhaustive calculation establishes the sharp reported distances because every source has been visited.

## Verification
The programs `verify_even5.py` and `verify_folded4.cpp` are standalone, require no input data, and use distinct graph constructions and enumeration methods. Run:

```text
python3 verify_even5.py > even5_output.json
g++ -std=c++17 -O2 -Wall -Wextra verify_folded4.cpp -o verify_folded4
./verify_folded4 > folded4_output.txt
```

Compare their output files to the embedded reference `even5_output.json` and `folded4_output.txt`. The former enumerates all \(\binom{16}{k}\) subsets for \(0\le k\le5\) and pairs all feasible five-sets. The latter visits all \(2^{16}=65,536\) subsets, constructs exchanges by remove/insert operations, and runs breadth-first search from all feasible minima. Both independently confirm the result. Their deterministic outputs were replayed from the packaged source files and matched the included reference outputs byte-for-byte. The programs are complete finite proofs of the enumerative portions when executed; they do not prove unrelated infinite statements.

## Relationship to prior work
Hernando--Mora--Pelayo (arXiv:1312.0772, public December 3, 2013) gives the standard locating-dominating definition and examines global location-domination; it does not provide the present five-regular Clebsch classification or reconfiguration results. Foucaud--Henning--Löwenstein--Sasse (arXiv:1412.2376, public December 2014) studies general bounds for twin-free graphs, not an exact optimal-state or relocation classification for this host. The symmetric \(2\!-(16,6,2)\) closed-neighborhood incidence design on the Clebsch graph gives a known smaller family of \(96\) optimal **identifying** codes; identifying codes require all sixteen closed-neighborhood traces to be distinct, unlike locating domination, which compares only unselected vertices. Those \(96\) sets (independent or star type) form a proper subset of the \(416\) locating-dominating minima. Likewise, a known classification of all \(1,056\) dominating five-sets in this graph employs a strictly weaker feasibility condition and does not determine the present smaller reconfiguration graphs or their distances.

## Limitations
This statement concerns the standard five-regular Clebsch graph, **not** its ten-regular complement. It concerns ordinary open-neighborhood locating domination, not identifying codes or total locating domination. Exact computed enumerations depend on transparent standalone deterministic programs and can be replayed without third-party packages; they constitute complete finite checks, not an independent scholarly audit. No absolute historical-priority claim is made; unindexed or inaccessible specialized calculations remain possible.

## References
1. C. Hernando, M. Mora and I. M. Pelayo, *On global location-domination in graphs*, arXiv:1312.0772 (first version December 3, 2013), https://arxiv.org/abs/1312.0772.
2. F. Foucaud, M. A. Henning, C. Löwenstein and T. Sasse, *Locating-dominating sets in twin-free graphs*, arXiv:1412.2376 (first version December 2014), https://arxiv.org/abs/1412.2376.
3. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html (graph parameters and equivalent presentation).
