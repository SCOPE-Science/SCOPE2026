# Nine-move locality excess in minimum power-domination relocation on the Tutte eight-cage

## Finding
Let \(G\) be the Tutte–Coxeter graph, the 30-vertex cubic eight-cage. Let \(\mathcal P\) denote its minimum power-dominating vertex sets. Define \(J\) on \(\mathcal P\) by allowing one selected vertex to be replaced by any unselected vertex, and define \(T\) by requiring the removed and inserted vertices to be adjacent in \(G\). Every intermediate configuration must remain in \(\mathcal P\).

The complete, exact conclusions are:

1. \(\gamma_P(G)=4\) and \(|\mathcal P|=6{,}540\).
2. \(J\) is connected with \(126{,}240\) edges and every vertex has eccentricity \(4\), so its radius and diameter both equal \(4\).
3. \(T\) is connected with \(23{,}040\) edges, radius \(11\), and diameter \(13\). It has exactly \(1{,}680\) configurations of eccentricity \(11\), \(3{,}420\) of eccentricity \(12\), and \(1{,}440\) of eccentricity \(13\).
4. The maximum locality penalty \(d_T(S,U)-d_J(S,U)\) over distinct \(S,U\in\mathcal P\) equals exactly \(9\). Precisely \(1{,}440\) unordered pairs attain it; each such pair is at jump distance \(4\) and slide distance \(13\).

The full unordered-pair distribution of locality penalties is:

| Penalty \(d_T-d_J\) | Number of unordered configuration pairs |
|---:|---:|
| 0 | 335,700 |
| 1 | 1,331,640 |
| 2 | 3,617,640 |
| 3 | 5,764,080 |
| 4 | 5,759,640 |
| 5 | 3,341,580 |
| 6 | 1,037,400 |
| 7 | 175,680 |
| 8 | 17,730 |
| 9 | 1,440 |

These ten entries total \(\binom{6540}{2}=21{,}382{,}530\) unordered distinct pairs. The legal-move graph on all optimal four-sensor configurations has ten explicit symmetry orbits; their sizes, jump degrees, slide degrees, and slide eccentricities are given under Verification.

## Assumptions and scope
The graph is simple and unweighted. An initial sensor set \(S\subseteq V(G)\) observes \(N[S]\). Subsequently, in each synchronous round, every observed vertex that has **exactly one** as-yet-unobserved neighbor observes that neighbor; propagation repeats to a fixed point. A power-dominating set is one that eventually observes all 30 vertices. The minimum number of selected vertices is \(\gamma_P(G)\). The two reconfiguration graphs use precisely the minimum sets, not arbitrary larger successful sets. Their distances count one-vertex replacements, and neither operation permits temporarily using five sensors.

For an explicit labelled model, take the 15 duads (two-element subsets) of \(\{0,1,2,3,4,5\}\) and the 15 synthemes (perfect matchings that partition this set into three duads). Join a duad to each syntheme containing it. Sort duads and synthemes lexicographically; label duads \(0,\ldots,14\) and synthemes \(15,\ldots,29\). This is the incidence graph of the generalized quadrangle of order two and hence the Tutte–Coxeter eight-cage. The second verification program constructs its isomorphic symplectic incidence representation independently.

## Proof
This is an exact finite exhaustive proof with full standalone checking programs. No sampling or extrapolation is used. Each exhaustive step has a precisely bounded search space.

**Minimum and complete configuration family.** In `verify_duads.py`, the recursion `perfect_matchings` chooses the mate of the least remaining symbol and recursively partitions the other four symbols. The output therefore comprises every perfect matching exactly once. The incidence loop creates all edges and exactly 30 cubic vertices. For every cardinality \(1\le k\le4\), `combinations(range(30), k)` visits every candidate vertex set once. `power_dominates` implements the initial closed-neighborhood observation and then the simultaneous unique-unobserved-neighbor rule until no more vertices are added. Each iteration adds at least one observed vertex or terminates, so at most 30 strict expansions occur, and the terminal observed set is exactly the least closure under the rule. The counts are respectively \(0,0,0,6540\), proving \(\gamma_P(G)=4\) and the exact family size. The empty set plainly cannot observe any vertex.

**Exact legal-move graphs.** For each of the 6,540 successful four-sets, `moves` tries every possible removed selected vertex and inserted unselected vertex, retaining exactly the target sets in the precomputed complete successful family. The additional adjacency test is imposed for sliding. Thus no move can be missing or spurious. Checking reverse arcs establishes undirectedness. The enumerations yield exactly 126,240 jump edges and 23,040 slide edges.

**Reduction of every distance computation to ten searches.** Every permutation of the six underlying symbols induces an incidence-graph automorphism. The program also explicitly checks a point–line duality on all 30 neighborhoods. Composing all 720 symbol permutations with the identity or that duality gives 1,440 distinct verified automorphisms, which preserve power domination and both types of move. Acting on the enumerated optimum family partitions it into ten orbits of sizes \(720,240,1440,720,720,720,720,720,360,180\). A breadth-first search from one representative of each orbit obtains shortest-path distances to every optimum set because each edge is a unit move. An automorphism sends shortest paths to shortest paths, so a representative's distance shell and eccentricity apply to its whole orbit. Every BFS reaches all 6,540 sets, proving both graphs connected. Weighting shells by orbit sizes and dividing ordered nonidentity pair counts by two gives the exact all-pairs distance distributions; joint jump-and-slide distances similarly give the locality table. The maximum eccentricity in \(T\) is 13 and its minimum is 11, while all ten representatives have jump eccentricity 4. Both upper and lower distance claims follow from these exhaustive BFS certificates.

**Independent representation and all-pairs verification.** `verify_symplectic.cpp` instead uses the nonzero four-bit vectors over \(\mathbb F_2\) as 15 points. Its 15 lines are the triples \(\{u,v,u+v\}\) with \(u\ne v\) and zero symplectic pairing under \(B(u,v)=u_0v_1+u_1v_0+u_2v_3+u_3v_2\pmod2\). A verified explicit 30-vertex bijection in `verify_duads.py` matches this incidence graph to the duad–syntheme graph edge by edge. The C++ program independently enumerates all successful sets and both move graphs, then performs BFS from **each** of the 6,540 states in each graph, without using symmetry orbit reduction. It independently recomputes the complete locality penalty distribution. Thus the 1,440 extremal pairs and exclusion of any penalty above nine are independently exhaustively certified.

## Verification
Run with Python 3 and a C++17 compiler from the directory containing these files:

```sh
python3 verify_duads.py
c++ -O3 -std=c++17 verify_symplectic.cpp -o verify_symplectic
./verify_symplectic
```

The output files `duad_results.txt` and `symplectic_results.txt` contain the actually executed computations. They agree on optimum cardinalities, minimum-set count, both move-edge counts, full degree distributions, both eccentricity distributions, full all-pairs shortest-path distributions, and all ten locality excess counts.

The ten checked symmetry representatives (using the duad–syntheme indexing above) have these invariants:

| Representative | Orbit size | Jump degree | Slide degree | Slide eccentricity |
|---|---:|---:|---:|---:|
| (0,1,2,24) | 720 | 44 | 8 | 11 |
| (0,1,5,22) | 240 | 47 | 9 | 11 |
| (0,1,6,22) | 1,440 | 35 | 7 | 12 |
| (0,1,12,28) | 720 | 29 | 7 | 13 |
| (0,1,15,22) | 720 | 30 | 4 | 13 |
| (0,1,21,22) | 720 | 39 | 8 | 12 |
| (0,1,21,25) | 720 | 50 | 8 | 11 |
| (0,1,22,25) | 720 | 38 | 6 | 12 |
| (0,1,22,26) | 360 | 56 | 8 | 12 |
| (0,9,19,20) | 180 | 28 | 8 | 12 |

An explicit 13-slide geodesic from the first eccentricity-13 orbit is printed as `extremal_13_slide_path` in `duad_results.txt`. Its optimality is certified by the BFS distance, not merely by the existence of the 13-move sequence. The complete distance-pair distribution in \(T\), for distances \(1\) through \(13\), is \((23040,104400,380880,1093860,2469600,4226400,5237280,4477500,2406960,793680,151200,16290,1440)\). The corresponding distribution in \(J\), for distances \(1\) through \(4\), is \((126240,1635120,7681620,11939550)\).

## Relationship to prior work
Bjorkman et al., *Power domination reconfiguration* (public January 5, 2022), establish the general token-jump and token-addition/removal framework, with results for complete graphs, complete bipartite graphs, paths, cycles, wheels, and other constructions. The relevant full-text sections do not give the present Tutte eight-cage minimum-family or token-slide metrics. Anderson and Kuenzel, *Power domination in cubic graphs and Cartesian products* (public September 8, 2022), give general cubic bounds and product results; their sharper claw-free cubic theorem does not apply to this girth-eight graph, which has induced claws. Neither source determines the claimed optimum enumeration, ten movement symmetry types, sharp distance profile, or nine-slide excess.

A published mathematical-record search also identified work on metric bases, majority dynamics, and coordinate controllability of the same thirty-vertex graph. These properties involve, respectively, distance resolution, synchronous majority evolution, and linear-system controllability. Their reported counts do not imply the power-domination closure or the present optimal-relocation distances. Published work on other named Coxeter or incidence graphs likewise does not imply a result on this specific 30-vertex graph. These are comparisons of predicates and implications, not merely titles.

## Limitations
This is a finite theorem about one canonical graph, not a formula for arbitrary generalized quadrangles or cubic cages. The result establishes exact distances within the minimum-budget feasible family; it does not address paths allowed to carry extra sensors. Originality is a literature-comparison judgment, not proof of historical priority: a sufficiently obscure or unindexed equivalent enumeration could exist. The finite proof is fully reproducible from the accompanying code but has not been independently audited or formally verified in a proof assistant.

## References
1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob, C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798, first public January 5, 2022. https://arxiv.org/abs/2201.01798
2. S. E. Anderson and K. Kuenzel, *Power domination in cubic graphs and Cartesian products*, arXiv:2209.03931, first public September 8, 2022. https://arxiv.org/abs/2209.03931
3. W. Tutte's eight-cage, duad–syntheme and generalized-quadrangle realization: https://mathworld.wolfram.com/Tutte8-Cage.html
