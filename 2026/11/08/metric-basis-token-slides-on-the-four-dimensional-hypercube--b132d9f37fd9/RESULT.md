# Metric-basis token slides on the four-dimensional hypercube

## Finding

Let \(Q_4\) be the four-dimensional binary hypercube and let \(\mathcal R\) have one vertex for each minimum resolving set (metric basis) of \(Q_4\). Join two bases when one landmark is moved along one hypercube edge to an unoccupied vertex, with all other landmarks held fixed. Then \(\mathcal R\) is connected, has exactly \(928\) vertices and \(3584\) edges, and has radius \(8\) and diameter \(10\). Its degree distribution is \(7:512,\ 8:384,\ 16:32\), and its eccentricity distribution is \(8:64,\ 9:592,\ 10:272\).

More precisely, \(\mathcal R\) has **eight orbits** under the natural coordinate-permutation and bit-translation group of \(Q_4\). Here integers \(0\) through \(15\) denote four-bit vertices; the table lists one unordered representative per orbit, its population, the common degree, and the common eccentricity:

| Representative | Orbit size | Degree | Eccentricity |
| --- | ---: | ---: | ---: |
| \(\{0,1,2,4\}\) | 64 | 7 | 10 |
| \(\{0,1,2,5\}\) | 192 | 8 | 10 |
| \(\{0,1,2,7\}\) | 192 | 7 | 9 |
| \(\{0,1,6,10\}\) | 192 | 7 | 9 |
| \(\{0,1,6,11\}\) | 192 | 8 | 9 |
| \(\{0,3,5,6\}\) | 16 | 16 | 9 |
| \(\{0,3,5,9\}\) | 16 | 16 | 10 |
| \(\{0,3,5,14\}\) | 64 | 7 | 8 |

In particular, two size-sixteen symmetry classes attain the maximum degree of \(16\) but have *different eccentricities*, \(9\) and \(10\). All four-landmark resolving sets are exactly the nonsingular collections of four sign vectors in \(\{\pm1\}^4\); the constrained relocation graph is therefore a geometrically defined subgraph of a real vector-matroid basis-exchange graph.

## Assumptions and scope

The hypercube is the simple undirected graph with vertex set \(\{0,1\}^4\); two vertices are adjacent exactly when they differ in one coordinate. Distances are Hamming distances. A set \(S\) resolves \(Q_4\) if every two distinct vertices have different vectors of distances to the landmarks in \(S\). A metric basis has minimum cardinality. An allowed move replaces one landmark by one *adjacent unoccupied* hypercube vertex, and the resulting set must remain a metric basis. The landmarks are unlabelled; different move descriptions yielding the same set count only once. All counts refer to this single fixed finite graph, not to arbitrary-dimensional hypercubes.

## Proof

**Signed-matrix lemma.** For a vertex \(s=(s_1,\ldots,s_4)\), put \(m(s)=(1-2s_1,\ldots,1-2s_4)\). For \(x,y\in\{0,1\}^4\),
\[
d(x,s)-d(y,s)=m(s)\cdot(x-y).
\]
Every nonzero vector of \(\{-1,0,1\}^4\) is realizable as \(x-y\) for some distinct binary vertices. Thus a landmark set \(S\) is resolving precisely when the matrix with rows \(m(s)\), \(s\in S\), has no nonzero ternary null vector.

Any \(3\times3\) matrix of signs has determinant in \(\{0,-4,4\}\): subtract the first row from the two other rows to see divisibility by \(4\), and apply the Hadamard bound \(3^{3/2}<6\). Let \(M\) be any matrix of sign rows having rank at most \(3\). Extend its row space, if necessary, to a three-dimensional space spanned by sign rows (possible since all sign vectors span \(\mathbb R^4\)). Take three independent sign rows and form their four signed \(3\times3\) cofactors. This gives a nonzero kernel vector whose entries belong to \(\{0,-4,4\}\); dividing by \(4\) gives a nonzero ternary kernel vector for \(M\). Consequently, no set of at most three landmarks resolves \(Q_4\), and a four-element set resolves if and only if its \(4\times4\) sign matrix is invertible. For example \(\{0,1,2,4\}\) is invertible, so the minimum cardinality is exactly four.

**Exhaustive finite classification.** There are exactly \(\binom{16}{4}=1820\) unordered four-element subsets. The attached programs examine them all. `verification/check_direct.cpp` independently compares all sixteen distance profiles for each subset and constructs every legal move by replacing a selected vertex with one of its four bit-flip neighbors. This yields \(928\) resolving subsets, \(3584\) undirected edges, one component, and the complete degree and eccentricity distributions. For each state, breadth-first search visits all \(928\) states and computes the maximum shortest-path distance, establishing the exact radius and diameter without sample extrapolation.

`verification/check_signed.py` instead checks all \(80\) nonzero ternary displacement vectors against the signed-matrix separation criterion, and separately confirms the determinant test on all \(1820\) four-subsets. It constructs the moves independently, enumerates the group of all \(16\) bit translations and \(24\) coordinate permutations, and finds the eight disjoint orbits whose sizes sum to \(928\). It performs breadth-first search from all orbit states to check their eccentricities. The orbit representatives and metric values in the table are the exact output of that exhaustive check. Every symmetry preserves Hamming distances and legal slides, so the reported degree/eccentricity values are constant throughout an orbit.

The candidate space, adjacency rule, group actions, and breadth-first searches are all exhaustively specified, with standalone programs attached. The computations use exact integer operations, no randomization, and no timeouts or solver heuristics.

## Verification

Compile and run the C++17 source with `g++ -O2 -std=c++17 verification/check_direct.cpp -o check_direct && ./check_direct`. Run the independent Python 3 source with `python3 verification/check_signed.py`. Their recorded outputs are `verification/check_direct_output.txt` and `verification/check_signed_output.txt`. Both programs were executed from these exact source bytes, with all built-in assertions passing. The C++ code checks every one of the \(928\) breadth-first-search roots; the Python code checks all eight automorphism orbits and their statewise eccentricities. The signed-matrix lemma independently explains the mathematical completeness of the finite membership test.

## Relationship to prior work

Ganesan's 2011 note (arXiv:1106.3632, Lemma 2) already establishes that the metric dimension of \(Q_4\) equals four. That previously known minimum is a premise, not an originality claim. Beardon's 2013 work, and the later Laird–Tillquist–Becker–Lladser 2019 preprint, develop general sign/linear-system criteria for hypercube resolvability. The signed-matrix method is accordingly treated as a proof device here, not claimed as a newly invented general principle. Nikolić–Čangalović–Grujičić study symmetry properties and heuristic searches for hypercube resolving sets; their available abstract does not establish the adjacency-constrained relocation metric. The finding here concerns the specific *reconfiguration graph*, including its eight symmetry classes, exact eccentricities, and sharp diameter, rather than only the minimum size or resolution-testing criteria.

## Limitations

This is an exact finite-host theorem and makes no claim about relocation graphs in higher-dimensional cubes. The enumerative and metric portions depend on exhaustive reproducible integer computations, not a short closed-form derivation of each table entry. The full text of a potentially relevant 2014 study of hypercube metric-basis symmetry and of Beardon's 2013 article was not accessible for complete inspection; equivalent unpublished or unindexed structural classifications remain a historical-priority risk. No independent scholarly audit has been performed.

## References

- A. Ganesan, *Minimal resolving sets for the hypercube*, arXiv:1106.3632, first submitted 18 June 2011. https://arxiv.org/abs/1106.3632
- A. F. Beardon, *Resolving the hypercube*, Discrete Applied Mathematics 161 (2013), 1882–1887. https://doi.org/10.1016/j.dam.2013.02.012
- N. Nikolić, M. Čangalović, I. Grujičić, *Symmetry properties of resolving sets and metric bases in hypercubes*, Optimization Letters 11 (2017), 1057–1067, first online 2014. https://doi.org/10.1007/s11590-014-0790-2
- L. Laird, R. C. Tillquist, S. Becker, M. E. Lladser, *Resolvability of Hamming Graphs*, arXiv:1907.05974, 12 July 2019. https://arxiv.org/abs/1907.05974
