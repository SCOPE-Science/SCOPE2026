# The 175 optimal rubbling distributions of the Petersen graph

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, on the ten two-element subsets of \(\{0,1,2,3,4\}\), adjacent when disjoint. A pebble distribution is a nonnegative integer vector \(p\) on these ten vertices, and is *solvable* when, for every target vertex separately, some finite legal sequence of rubbling moves leaves a pebble on that target.

**Theorem.** There are exactly \(175\) solvable distributions of total weight four on \(P\). Of these, exactly \(10\) are solvable without strict rubbling moves, that is, by ordinary pebbling alone. The complete partition-by-multiplicity classification is:

| Nonzero pebble multiplicities | Rubbling-solvable distributions | Pebbling-solvable distributions |
|---|---:|---:|
| \((4)\) | 10 | 10 |
| \((3,1)\) | 0 | 0 |
| \((2,2)\) | 45 | 0 |
| \((2,1,1)\) | 30 | 0 |
| \((1,1,1,1)\) | 90 | 0 |
| **Total** | **175** | **10** |

All \(45\) placements of two pebbles at each of two distinct vertices are rubbling-solvable. A distribution with two pebbles on the vertex \(\{a,b\}\) and one pebble on each of two other vertices is rubbling-solvable **if and only if** those other vertices are \(\{a,c\}\) and \(\{b,c\}\) for some distinct \(a,b,c\in\{0,1,2,3,4\}\). For four singleton pebbles, solvability depends only on the induced graph on their support:

| Induced four-vertex graph | Number of supports | Rubbling-solvable? |
|---|---:|---|
| \(4K_1\) | 5 | Yes |
| \(K_2\sqcup2K_1\) | 60 | Yes |
| \(2K_2\) | 15 | Yes |
| \(K_{1,3}\) | 10 | Yes |
| \(P_3\sqcup K_1\) | 60 | No |
| \(P_4\) | 60 | No |

These are all six possible induced types: the Petersen graph has girth five, so every induced subgraph on four vertices is a forest. The \(715\) weight-four distributions form exactly \(17\) orbits under the natural action of \(S_5\); exactly eight of those orbits are solvable. No distribution of total weight at most three is solvable, recovering the already-known optimal rubbling number \(\rho_{\mathrm{opt}}(P)=4\) rather than claiming it as new. The known ordinary optimal pebbling number is also \(\pi_{\mathrm{opt}}(P)=4\).

## Assumptions and scope
All configurations are *labelled vertex distributions*, not classes modulo automorphisms. Distinct pebbles at the same vertex are indistinguishable. The graph is fixed as \(\operatorname{KG}(5,2)\); there is no extrapolation to a generalized Petersen family. A standard pebbling move consumes two pebbles from a vertex \(u\) and places one at a neighbor \(v\). A strict rubbling move consumes one pebble from each of two **distinct** neighbors of \(v\) and places one at \(v\). Both operations require sufficient nonnegative inventories at every step. Every move decreases total weight by exactly one. For each chosen target, the executable move sequence may differ; simultaneous occupation of all targets is **not** required.

## Proof
We give a finite exhaustive proof with two independent implementations of the exact state-reachability recurrence, not an inference from sampling.

Index the graph vertices lexicographically by \(01,02,03,04,12,13,14,23,24,34\); two indices are neighboring precisely when the corresponding pairs are disjoint. For a nonnegative state \(p\), let \(R(p)\) be the set of vertices at which a pebble can occur after zero or more legal rubbling moves. If \(p\to q\) ranges over **all** legal single moves, then

\[
R(p)=\{v:p(v)>0\}\;\cup\!\bigcup_{p\to q}R(q).
\]

The recurrence is exact by first-move decomposition: a target is already occupied or any successful nonempty sequence has a first move \(p\to q\). Since each move reduces the total pebble count by one, the recurrence terminates and induction on that count proves that its computed set equals the operationally reachable set. The pebbling-only recurrence is the same, restricting both consumed pebbles to one vertex. Neighbors are enumerated directly from disjointness of the index pairs; consumed pairs of neighbors are enumerated as unordered pairs with repetition, including the standard-pebbling case.

Every nonnegative ten-coordinate distribution of weight \(k\) is generated exactly once by the ten-part weak compositions of \(k\). There are \(\binom{13}{4}=715\) of weight four, and \(\sum_{k=0}^{3}\binom{9+k}{k}=286\) of smaller weight. The recurrence reports zero solvable states among the latter, and the five rubbling and pebbling counts in the first table among the former. In particular, the \((2,1,1)\) successes are exactly the \(\binom{5}{3}\cdot3=30\) indicated three-edge triangles, and the six four-singleton forest-type counts yield \(5+60+15+10=90\) successes. The \((2,2)\) successes contribute \(\binom{10}{2}=45\), while the ten four-pebble piles contribute the remaining ten. This establishes every asserted value and the *if and only if* characterizations.

As a cross-check on the finite universe, all \(5!=120\) permutations of the five ground labels act by graph automorphisms. Their orbits partition the \(715\) weight-four states into \(17\) classes. The separate \(\texttt{orbits.csv}\) lists one ten-digit representative, orbit size, reachability count and solvability for each; the size sum is \(715\), and the eight successful orbit sizes sum to \(175\). The complete reproducible orbit generation, with an independent dynamic-programming reachability routine, is in \(\texttt{check_rubbling.py}\). This finite symmetry calculation is an internal consistency test; the full enumeration, not the group action by itself, establishes completeness.

## Verification
Run the self-contained Python program with \(\texttt{python3 check_rubbling.py}\). Independently compile and run the C++17 breadth-first-search verifier with \(\texttt{g++ -std=c++17 -O2 check_rubbling.cpp -o check_rubbling}\) followed by \(\texttt{./check_rubbling}\). The Python program uses recursive reachability memoization and all \(120\) natural label permutations; the C++ program uses explicit queues of reachable states and computes induced graph shapes directly. Both enumerate the entire ten-coordinate state space of weights zero through four, with no search truncation or probabilistic steps. The verified output agrees on \(175\), \(10\), all occupancy-partition counts, both four-singleton success/failure spectra, and absence of any sub-four solvable state. The orbit file is independently regenerated by the Python script; it is not a prerequisite input to either computation.

## Relationship to prior work
Belford and Sieben, *Rubbling and Optimal Rubbling of Graphs*, arXiv:0707.4256, first publicly submitted July 28, 2007, define the legal moves and give \(\rho_{\mathrm{opt}}(P)=4=\pi_{\mathrm{opt}}(P)\) in Proposition 9.2(d), proving that four pebbles stacked at one vertex work. This antecedent is not a new assertion here. Their proof does not enumerate all optimal distributions, their occupancy profiles, singleton support geometries, or the difference of \(175\) versus \(10\). The earlier rubbling thesis by Belford (December 2006) treats the universal Petersen rubbling number \(\rho(P)=5\) and general optimal rubbling definitions, not this four-pebble census. Katona and Papp (arXiv:1411.0923) study optimal values for ladders, prisms and Möbius ladders, not the Petersen optimum-placement classification. Searches of relevant published mathematical-result records for equivalent distribution counts, labelled configurations and geometry did not identify a covering statement; a failed search is not a proof of global priority.

## Limitations
This is a finite, computer-assisted exact classification for a fixed ten-vertex graph. The proof is only as reliable as the clear move specification and the two supplied implementations; it makes no claim about a general family or any unbounded state space. The integer minimum four was known; only the complete optimizer census and structural refinement are claimed as new. An unindexed prior computation or an unpublished catalogue may contain equivalent information, so independent literature review remains useful. The quotient-by-symmetry count \(17\) refers to all weight-four distributions, not only the successful ones.

## References
1. C. Belford and N. Sieben, *Rubbling and Optimal Rubbling of Graphs*, arXiv:0707.4256 (submitted July 28, 2007), https://arxiv.org/abs/0707.4256 and https://jan.ucc.nau.edu/~ns46/research/rubbling.pdf.
2. C. A. Belford, *Graph Rubbling: An Extension of Graph Pebbling*, M.S. thesis, Northern Arizona University, December 2006; available at https://nau.edu/wp-content/uploads/sites/145/2018/08/belford-ek.pdf.
3. G. Y. Katona and L. F. Papp, *The Optimal Rubbling Number of Ladders, Prisms and Möbius-ladders*, arXiv:1411.0923 (submitted November 4, 2014), https://arxiv.org/abs/1411.0923.
