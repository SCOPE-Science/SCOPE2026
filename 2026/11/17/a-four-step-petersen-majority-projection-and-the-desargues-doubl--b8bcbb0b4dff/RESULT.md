# A four-step Petersen majority projection and the Desargues double-cover basin spectrum

## Finding

For synchronous open-neighbor binary strict-majority updating on the Petersen graph \(P=KG(5,2)\), let \(T\) denote the global map on its ten labelled vertices. The exact identities are
\[
T^6=T^4,\qquad T^5\ne T^3.
\]
The recurrent set \(R=\operatorname{im}(T^4)\) has 124 configurations: 14 fixed configurations and 55 primitive temporal two-cycles. The projection \(T^4\) has exactly three fiber sizes: 72 recurrent states have fiber size 1, 50 have fiber size 10, and two have fiber size 226.

Let \(D\) be the Desargues graph, the bipartite double of \(P\), equivalently \(GP(10,3)\). For synchronous open-neighbor majority on its twenty vertices, write \(F\) for the global update. Then
\[
F^6=F^4,\qquad F^5\ne F^3,
\]
so the sharp maximum first-periodic-entry time is four. Its complete recurrent census consists of **124 fixed configurations and 7,626 primitive temporal two-cycle orbits**. The complete attraction-basin spectrum, counted by labelled starting configurations and without quotienting spatial symmetry, is:

| Eventual primitive period | Basin size per orbit | Number of orbits |
| ---: | ---: | ---: |
| 1 | 1 | 72 |
| 1 | 100 | 50 |
| 1 | 51,076 | 2 |
| 2 | 2 | 2,556 |
| 2 | 20 | 3,600 |
| 2 | 200 | 1,225 |
| 2 | 452 | 144 |
| 2 | 4,520 | 100 |
| 2 | 102,152 | 1 |

Thus 72 equilibria and 2,556 oscillatory orbits are dynamically isolated, while a unique two-cycle attracts 102,152 initial states. The total basin populations are 107,224 for fixed points and 941,352 for two-cycles. The exact first periodic-entry table is:

| First periodic update | Eventually fixed | Eventually two-cyclic |
| ---: | ---: | ---: |
| 0 | 124 | 15,252 |
| 1 | 2,940 | 129,140 |
| 2 | 24,480 | 442,720 |
| 3 | 32,640 | 169,920 |
| 4 | 47,040 | 184,320 |

## Assumptions and scope

Index the ten Petersen vertices by the two-element subsets of \(\{0,1,2,3,4\}\), listed lexicographically, with adjacency when the two subsets are disjoint. For a ten-bit state \(s\) and Petersen vertex \(e\), its next bit is one exactly when at least two of the three two-element subsets disjoint from \(e\) currently have bit one. This defines \(T\) without ties or self-loops. Configurations are **indexed**, so graph symmetries and global complementation are not identified.

For a graph \(G\) on ten vertices, its bipartite double has vertices \((i,0)\), \((i,1)\), and an edge from \((i,0)\) to \((j,1)\) precisely when \(i,j\) are adjacent in \(G\). Its majority map is
\[
F(x,y)=(T(y),T(x)).
\]
For the stated Petersen graph, this bipartite double is isomorphic to the twenty-vertex Desargues graph. An explicit isomorphism onto \(GP(10,3)\) is provided and checked in `check_petersen.py`.

A primitive two-cycle is an unordered pair of distinct states interchanged by one update; each is counted once. A basin is the set of initial indexed states eventually visiting that orbit, including its periodic members. The first-entry time is the minimum number of updates required to reach a temporally periodic configuration.

## Proof

**1. Finite geometric reduction.** A ten-bit state of \(P\) is a simple undirected graph on five labelled vertices, since the ten Petersen vertices are the ten edges of \(K_5\). Relabelling the five vertices gives the full \(S_5\)-action on the state space. This action commutes with \(T\). Consequently, to verify an identity between iterates of \(T\) on all 1,024 states it suffices to verify one representative of each of the 34 isomorphism classes of graphs on five vertices. These 34 representatives, their labelled-orbit sizes (summing to 1,024), their \(T^4\)-images, and their image-fiber sizes are enumerated explicitly by the standalone finite certificate `check_petersen.py`; its complete table is in `check_petersen_output.txt`. Each edge neighbourhood is computed from the disjointness condition stated above, and every integer operation is exact.

For each representative \(s\), the certificate directly evaluates the six iterates \(T(s),\ldots,T^6(s)\). All 34 satisfy \(T^6(s)=T^4(s)\). Since the calculation is equivariant under the entire \(S_5\)-action and covers every orbit, \(T^6=T^4\) for all states. The same exhaustive computation finds \(T^5\ne T^3\). Hence every orbit enters a temporal fixed point or two-cycle by update four, and four is sharp. This is a finite exhaustive proof for a specified ten-vertex object, not an extrapolation from small examples.

**2. The 124 recurrent symbols.** The set \(R=\operatorname{im}(T^4)\) is exactly the set fixed by \(T^2\), since \(T^6=T^4\). Its recurrent symbols split under \(S_5\) into the following eight classes. Representatives are hexadecimal masks in the lexicographic edge order above; the mask is part of a reproducible finite certificate, not an additional assumption.

| Representative mask | Labelled class size | Number of selected edges | \(T^4\)-fiber size |
| --- | ---: | ---: | ---: |
| `000` | 1 | 0 | 226 |
| `007` | 20 | 3 | 10 |
| `00f` | 5 | 4 | 10 |
| `03b` | 60 | 5 | 1 |
| `0b7` | 5 | 6 | 10 |
| `0bf` | 20 | 7 | 10 |
| `0dc` | 12 | 5 | 1 |
| `3ff` | 1 | 10 | 226 |

The certificate verifies these class sizes under all 120 permutations. Exactly the 12 configurations in class `0dc` and the two constant masks are fixed by \(T\). Each of the other 110 recurrent states belongs to a primitive temporal two-cycle, giving 55 such orbits on \(P\). The fiber multiplicities are exactly \(72\) of size \(1\), \(50\) of size \(10\), and \(2\) of size \(226\), with the independent checksum \(72+50\cdot10+2\cdot226=1,024\). The certificate also checks \(w(T(u))=w(u)\) for every \(u\in R\), where \(w(u)=\lvert(T^4)^{-1}(u)\rvert\).

**3. Doubling converts the recurrent map into a swap.** Since \(T^2\) is the identity on \(R\), every recurrent configuration of the bipartite double is uniquely represented as \((u,T(v))\) for \(u,v\in R\). Its evolution is
\[
F(u,T(v))=(v,T(u)).
\]
Thus \(F\) interchanges two 124-valued symbols. The configurations with \(u=v\) are fixed, and the unordered pairs \(\{u,v\}\), \(u\ne v\), each give one genuine two-cycle. This proves the counts \(124\) and \(\binom{124}{2}=7,626\). Moreover \(F^4(x,y)=(T^4(x),T^4(y))\), and therefore \(F^6=F^4\) while the sharpness witness for \(T\) gives \(F^5\ne F^3\).

**4. Attraction basins and first entry.** The fixed point \((u,T(u))\) has basin size \(w(u)w(T(u))=w(u)^2\). The two-cycle indexed by \(\{u,v\}\) has basin size
\[
w(u)w(T(v))+w(v)w(T(u))=2w(u)w(v).
\]
With 72 symbols of weight 1, 50 of weight 10, and two of weight 226, these two formulas yield every multiplicity in the basin table. For example the unique pair of weight-226 symbols has basin size \(2\cdot226^2=102,152\), and the 72 weight-one symbols yield \(\binom{72}{2}=2,556\) isolated two-cycles. The first-entry table follows from an independent 20-vertex functional-digraph traversal: the C++ certificate explicitly constructs the 30 edges of \(GP(10,3)\), evaluates all \(2^{20}=1,048,576\) input configurations, strips transient vertices by indegrees, and enumerates each periodic orbit and its complete predecessor tree. It checks all ten first-entry/period populations and the nine basin classes against the formulas above. The entry-time-four population is positive, proving sharpness once more.

## Verification

From the package directory, run `python3 check_petersen.py` and compare to `check_petersen_output.txt`; the checker uses only the Python standard library and tests all 34 \(S_5\)-orbits, all 1,024 labelled shore states, the exact isomorphism to \(GP(10,3)\), and all fiber identities. Run `g++ -std=c++17 -O2 -Wall -Wextra check_desargues.cpp -o check_desargues` followed by `./check_desargues`, and compare with `check_desargues_output.txt`. The latter program independently constructs the generalized Petersen graph and exhausts all 1,048,576 full configurations without using the shore reduction. Both programs terminate with `all_checks_passed` only when every asserted identity and count matches. All output records in this package were generated from the accompanying source files. The orbit tables are finite certificates for this graph, not claims about general graph families.

## Relationship to prior work

Goles and Olivos (1980) established the general eventual-period-two theorem for finite symmetric threshold dynamics. Benjamini, Chan, O'Donnell, Tamuz and Tan (first public preprint 2014) extend majority-dynamics convergence analysis to infinite and random graphs; Kaaser, Mallmann-Trenn and Natale (2016) study general voting-time bounds and complexity. These theorems do not imply a four-update cutoff, a 124-symbol projection, or exact orbit/basin numbers for the Petersen graph or its bipartite double.

The published Heawood-graph majority classification uses a 58-symbol incidence projection with a two-update cutoff, while the dodecahedral-graph majority classification has 118 fixed states and a seven-update cutoff. Neither concerns the bipartite double of the Petersen graph or implies the present 124-symbol/three-fiber structure. The Desargues graph's identification as the bipartite double of the Petersen graph is a standard graph-theoretic fact, not claimed as new. The contribution is its exact dynamical consequence and the geometric characterization via all 34 five-vertex graph classes.

## Limitations

This is a complete finite classification for exactly the specified Petersen and Desargues graphs, not a uniform theorem for arbitrary generalized Petersen graphs, arbitrary double covers, other thresholds, or asynchronous dynamics. The broad period-at-most-two property is classical. Absolute historical priority cannot be guaranteed by mathematical-record searches; differently indexed or unpublished prior enumerations may exist. No independent external mathematical audit has been performed.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, first publicly posted 2014-05-11, https://arxiv.org/abs/1405.2486 .
2. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, MFCS 2016, https://doi.org/10.4230/LIPIcs.MFCS.2016.55 .
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
4. E. W. Weisstein, *Desargues Graph*, MathWorld, https://mathworld.wolfram.com/DesarguesGraph.html (graph identification).
5. *A two-step majority projection and exact attraction basins on the Heawood graph*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-two-step-majority-projection-and-exact-attraction-basins-on-th--8cd2964a9d93 .
6. *Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-dodecahedral-majority-dynamics-an-exact-recurrent-basin-and-symm--095dfb0decea .
