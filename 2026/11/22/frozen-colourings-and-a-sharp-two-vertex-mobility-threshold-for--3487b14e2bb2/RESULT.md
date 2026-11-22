# Frozen colourings and a sharp two-vertex mobility threshold for the Heawood incidence graph

## Finding
Let \(H\) be the point–line incidence graph of the Fano plane, and let the palette be the four *named* colours \(\{0,1,2,3\}\). A proper locally identifying colouring \(c\) satisfies \(c(u)\ne c(v)\) and \(c(N[u])\ne c(N[v])\) for each edge \(uv\), where \(c(X)\) denotes the set of colours on \(X\). Two valid colourings are adjacent in \(\mathcal R_1(H)\) when they differ on exactly one vertex.

The complete, named-palette census is
\[
|V(\mathcal R_1(H))|=54\,264,\qquad |E(\mathcal R_1(H))|=185\,808,
\]
and its connected-component multiset is exactly
\[
\boxed{6048\,K_1\ \sqcup\ 8\,\mathcal C_{882}\ \sqcup\ 6\,\mathcal C_{6860}},
\]
where each \(\mathcal C_s\) denotes a connected component on \(s\) valid colourings (not an assertion that components of the same order are isomorphic). The eight \(882\)-vertex components are distinguished by the choice of a monochromatic incidence shore and its single colour. The six \(6860\)-vertex components are distinguished by a two-colour *point core*, described below. Every other colouring is isolated: there are exactly \(6048\) such frozen optimal assignments.

Define \(\mathcal R_{\le2}(H)\) by permitting replacement of the colours at one or two vertices in one move, provided only the resulting assignment must be locally identifying. Then \(\mathcal R_{\le2}(H)\) is **connected**. More strongly, even the graph of moves that change **exactly two** vertices is connected, with \(897\,456\) edges. Thus the threshold for global mobility is sharply two changed vertices. The locally identifying chromatic number \(\chi_{\mathrm{lid}}(H)=4\) follows from earlier general work together with the non-two-colourability of the Fano plane; it is not asserted to be new.

## Assumptions and scope
The Fano incidence model has points \(p_0,\ldots,p_6\) and lines \(\ell_0,\ldots,\ell_6\), indexed modulo seven, with
\[
p_j\sim\ell_i\quad\Longleftrightarrow\quad j-i\in\{0,1,3\}\pmod 7.
\]
The graph has fourteen labelled vertices and twenty-one edges. Names of colours and vertex labels are retained: global permutations of the colour names are **not** identified. Every edge joins a point to a line and has distinct endpoint closed neighbourhoods. A move changing exactly two vertices allows simultaneous recolouring, with no requirement that either individual intermediate change be valid. The finding makes no assertion about any larger graph family or about more than four palette colours.

For a colouring, let \(P\) and \(L\) denote the sets of colours used on the seven points and seven lines. The exact support-profile counts \((|P|,|L|,|P\cap L|)\) are

| Support profile | Named valid colourings |
|---|---:|
| \((1,3,0)\) | 3528 |
| \((3,1,0)\) | 3528 |
| \((2,2,0)\) | 29064 |
| \((2,3,1)\) | 6048 |
| \((3,2,1)\) | 6048 |
| \((3,3,2)\) | 6048 |

Every \((3,3,2)\) colouring is frozen, and these are all the frozen colourings. In the \((2,2,0)\) and \((2,3,1)\) profiles define the point core as \(P\); in the \((3,2,1)\) profile define it as \(P\setminus L\). This always has two colours. Each of the six possible point cores labels one entire \(6860\)-vertex connected component, containing \(4844\) assignments of profile \((2,2,0)\), \(1008\) of profile \((2,3,1)\), and \(1008\) of profile \((3,2,1)\). Each \(882\)-vertex component is monochromatic on one shore, with the other shore using the remaining three colours.

## Proof
**The known four-colour minimum.** Any locally identifying three-colouring of a connected, bipartite, triangle-free graph with an edge has the property that the colours in closed neighbourhoods have alternately two and three distinct entries across every edge. Indeed, each closed neighbourhood has at least two colours; endpoints of an edge cannot both have signature size three (both would contain all three colours), and they cannot both have size two (both would have exactly the two endpoint colours). Thus one entire shore has signature size three, the other size two. Applying the properness condition along length-two paths forces the former shore to have one constant colour. All vertices of the other shore use the remaining two colours, and every Fano triple must be bichromatic. But the Fano plane is not two-colourable: if its seven lines were all non-monochromatic, each would contain exactly one monochromatic pair, giving seven monochromatic point pairs in total. For a partition into colour classes of sizes \(a\) and \(7-a\), the actual number of such pairs is \(\binom a2+\binom{7-a}2\ge9\), since every pair of points lies on exactly one line. This contradiction proves the lower bound four. The explicit finite census below exhibits valid four-colourings. This minimum also follows from the framework of Esperet et al. and is included only for context.

**Finite exhaustive identity.** For each assignment \(a\in\{0,1,2,3\}^{14}\), define a four-bit closed-neighbourhood mask
\[
S_v(a)=\bigvee_{w\in N[v]}(1\ll a_w).
\]
The assignment is admissible exactly when, for each of the twenty-one incidences \(uv\), \(a_u\ne a_v\) and \(S_u(a)\ne S_v(a)\). This is both necessary and sufficient by the definition. The exhaustive programs `fano_lid_exact.cpp` and `lcf_lid_independent.cpp` test this predicate over every possible named assignment: one performs a depth-first search on Fano incidences, pruning only when a completed edge or neighbourhood signature already violates the predicate; the other enumerates all proper assignments of an independently constructed cyclic graph and checks the signatures at completed leaves. Any violation detected by the first algorithm cannot be repaired by assigning currently unassigned vertices, so its pruning is sound and complete. Both programs produce exactly \(54\,264\) valid assignments and all six displayed support-profile totals.

**Component census.** Give an admissible assignment the base-four key \(\sum_{j=0}^{13}a_j4^j\). These keys are distinct and represent the full state set, with no symmetry quotient. For each state and each vertex, replace its colour by each of the other three palette values; include an undirected edge precisely when the resulting key belongs to the admissible set. Counting each edge once gives \(185\,808\) edges, and an exhaustive disjoint-set or breadth-first-search traversal produces component sizes \(1\) (6048 times), \(882\) (eight times), and \(6860\) (six times). An enumeration of the colour-support masks in each component verifies the core/shore identifications above. These results follow from finite loops with explicitly specified complete search domains, not from sampling or a numerical extrapolation.

**Sharp mobility threshold.** For every admissible state and each unordered pair of distinct vertices, replace both colours independently by any of the three other colours. Retain a move if its destination belongs to the admissible key table, counting edges only with increasing state index. This exhaustive graph has \(897\,456\) edges and one connected component, checked by a disjoint-set traversal in both independent constructions. The one-vertex graph is disconnected, so one vertex is insufficient; changing two vertices is sufficient. Connectivity for the at-most-two-move graph follows because it contains the exactly-two-move graph.

## Verification
The two independent graph encodings are explicitly isomorphic. The second uses a fourteen-cycle with chords \(i\sim i+5\pmod{14}\) for even \(i\), and the vertex bijection from cyclic labels to the Fano labels \(0,\ldots,6,7,\ldots,13\) is
\[
(0,7,3,9,2,13,6,10,4,8,1,12,5,11).
\]
`isomorphism_check.py` checks every mapped edge and the bijection. The independent programs use differing enumeration and component algorithms. Running both C++ files and the graph-isomorphism check reproduces `verification_output.txt`. Their source text and reference output are provided as standalone artifacts.

Compilation and execution:

```sh
g++ -O3 -std=c++17 fano_lid_exact.cpp -o fano_lid_exact
g++ -O3 -std=c++17 lcf_lid_independent.cpp -o lcf_lid_independent
./fano_lid_exact
./lcf_lid_independent
python3 isomorphism_check.py
```

## Relationship to prior work
Esperet, Gravier, Montassier, Ochem, and Parreau introduced locally identifying colouring and proved the four-colour upper bound for bipartite graphs, as well as an equivalence between three-colour feasibility and two-colourability of a shore-neighbourhood hypergraph. Applied to the Fano plane, that framework covers \(\chi_{\mathrm{lid}}(H)=4\), but not the complete four-colour configuration graph, the frozen-state census, the component cardinalities, or the sharp two-vertex reconfiguration threshold. Foucaud, Honkala, Laihonen, Parreau, and Perarnau prove a recolouring lemma for palettes with strictly more than \(2d(\Delta-1)\) colours; in a cubic graph this means more than twelve colours, so it does not imply connectivity or component structure at the four-colour optimum. Bhyravarapu, Kumari, and Reddy analyse colouring minima on Cartesian and tensor products of paths and cycles, not the Heawood incidence graph or its reconfiguration graph.

Related results on ordinary proper three-colouring reconfiguration of Heawood, dominated colourings of finite projective planes, and locally identifying colourings of a pair of joined cliques use different admissibility predicates or graphs and do not entail this classification. The proposed new contribution is only the exact named four-colour reconfiguration census and two-change threshold.

## Limitations
The finding concerns a fixed fourteen-vertex graph, with finite and complete enumeration proving its combinatorial claims; it does not supply an infinite-family classification or a closed-form formula for other projective planes. Although two different implementations and an explicit graph isomorphism reproduce the counts, independent scholarly validation has not occurred. Historical priority can be affected by publications or exact tables not accessible or not indexed in the searches described in the accompanying review; no claim of universal novelty certification is made. The computational proof assumes ordinary integer and compiler semantics, which are transparent in the supplied small programs and can be checked without proprietary dependencies.

## References
1. L. Esperet, S. Gravier, M. Montassier, P. Ochem, and A. Parreau, *Locally identifying coloring of graphs*, arXiv:1010.5624 (first public submission 2010-10-27); *Electronic Journal of Combinatorics* 19(2) (2012), P40. https://arxiv.org/abs/1010.5624 ; https://doi.org/10.37236/2417 .
2. F. Foucaud, I. Honkala, T. Laihonen, A. Parreau, and G. Perarnau, *Locally identifying colourings for graphs with given maximum degree*, arXiv:1108.2769 (2011); *Discrete Mathematics* 312 (2012), 1832–1837. https://arxiv.org/abs/1108.2769 .
3. S. Bhyravarapu, S. Kumari, and I. V. Reddy, *On Locally Identifying Coloring of Cartesian Product and Tensor Product of Graphs*, arXiv:2305.17536 (2023). https://arxiv.org/abs/2305.17536 .
