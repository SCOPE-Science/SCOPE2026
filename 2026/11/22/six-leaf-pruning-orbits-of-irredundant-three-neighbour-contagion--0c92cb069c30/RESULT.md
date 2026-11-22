# Six leaf-pruning orbits of irredundant three-neighbour contagion on \(Q_4\)

## Finding

For synchronous, irreversible three-neighbour bootstrap percolation on the labelled four-dimensional binary cube \(Q_4\), there are exactly \(936\) inclusion-minimal percolating seed sets. They have size \(6\) or \(7\), with joint seed-size and completion-time enumerator

\[
\mathcal M_{Q_4}(z,u)=8z^6u^2+160z^7u^3+768z^7u^4.
\]

Under all \(384\) automorphisms of \(Q_4\), the sets form exactly six orbits. Each orbit is identified by a representative seed bitmask (in hexadecimal; bit \(v\) denotes cube vertex \(v\)), an orbit size, and the shape of the induced graph on the initially healthy vertices:

| Seed mask | Size | Completion rounds | Orbit size | Healthy tree orders | Maximum tree diameter |
|---|---:|---:|---:|---|---:|
| `0x1668` | 6 | 2 | 8 | 5, 5 | 2 |
| `0x1696` | 7 | 3 | 64 | 7, 2 | 4 |
| `0x16a9` | 7 | 3 | 96 | 7, 1, 1 | 4 |
| `0x1699` | 7 | 4 | 192 | 8, 1 | 6 |
| `0x16ac` | 7 | 4 | 192 | 9 | 6 |
| `0x169a` | 7 | 4 | 384 | 9 | 7 |

The eight size-six sets are precisely one parity class with an antipodal pair omitted. The size-six optimum and this optimum class are already reflected in earlier work on percolating seeds and maximum induced forests, and are *not* asserted to be new. The additional result here is the complete joint orbit/leaf-pruning-time classification, including all \(928\) inclusion-minimal seven-seed sets.

## Assumptions and scope

Vertices are the integers \(0,\ldots,15\), interpreted as four-bit vectors. Vertices \(v,w\) are adjacent when their bitwise XOR has exactly one nonzero coordinate. The open neighborhood of \(v\) is \(N(v)\). Starting with an arbitrary seed set \(A_0\), define simultaneously

\[
A_{t+1}=A_t\cup\{v\notin A_t:|N(v)\cap A_t|\ge3\}.
\]

A set percolates if \(A_t=V(Q_4)\) for some finite \(t\). Its completion time is the smallest such \(t\), including \(t=0\) for the full initial set. A percolating set is inclusion-minimal if deleting any nonempty subset destroys percolation. All counts refer to distinct labelled subsets of the fixed sixteen-vertex graph, not isomorphism types. The symmetry group comprises all maps obtained by permuting the four coordinates and XOR-translating by an arbitrary four-bit vector.

## Proof

**Forest reduction.** The graph is four-regular. Write \(U_t=V(Q_4)\setminus A_t\). A currently healthy vertex is infected at the next step exactly when it has at most one neighbor in \(U_t\). Thus each update removes all degree-zero and degree-one vertices from the induced graph on \(U_t\). This process empties a finite graph exactly when that graph is a forest: an induced cycle survives forever, while any nonempty finite forest has a leaf or an isolated vertex. Consequently, \(A_0\) percolates if and only if \(Q_4[U_0]\) is a forest. In a tree with diameter \(d\), repeated synchronous leaf deletion takes exactly \(1+\lfloor d/2\rfloor\) rounds; for a forest, take the maximum of this value over the tree components (the empty forest needs zero rounds).

**Minimality criterion.** Monotonicity of percolation implies that \(A_0\) is inclusion-minimal if and only if it percolates and each single-seed deletion fails. Equivalently, \(U_0\) must be an inclusion-maximal induced forest. Given an induced forest \(H=Q_4[U_0]\), adjoining a vertex \(v\notin U_0\) creates a cycle exactly when \(v\) has two neighbors belonging to the same connected component of \(H\). Therefore maximality can be tested without simulating infection.

**Exhaustive finite partition.** The attached `check_a.py` enumerates every integer mask in \([0,65535]\), constructs the exact synchronous closure by sets of vertices, and uses the single-deletion criterion. The independent `check_b.cpp` repeats the complete calculation with bitwise neighbor masks and integer popcounts. Both obtain the three nonzero coefficients \((6,2):8\), \((7,3):160\), and \((7,4):768\), and no other minimal-seed sizes or times. The third checker, `check_forest.py`, instead enumerates all induced forests, applies the same-component cycle criterion, and uses breadth-first tree diameters, reproducing these results without any infection simulation.

For each of the six listed representative masks, the first two checkers explicitly generate its full orbit using all \(4!\cdot16=384\) coordinate-permutation/translation maps. They verify, for each orbit, its listed size and infection time; the six orbits are disjoint and their union is exactly the independently enumerated set of \(936\) minimal seeds. The forest checker independently verifies the indicated component-order and maximum-diameter data for every representative. Hence the table is a complete exhaustive finite classification, not a sample or probabilistic estimate.

The size-six parity assertion can also be seen directly: removing two opposite vertices from a single parity class leaves six initially infected vertices. Every vertex of the other parity class has at least three infected neighbors, since antipodal deleted vertices have disjoint neighborhoods. The other parity class is therefore infected in round one, followed by the omitted pair in round two. There are four antipodal pairs per parity class, yielding eight configurations. The exhaustive orbit certificate proves these are the only six-seed percolators.

## Verification

Run `python3 check_a.py`, `g++ -O2 -std=c++17 check_b.cpp -o check_b && ./check_b`, and `python3 check_forest.py`. No external Python packages are needed. All three checkers use fixed expected constants and terminate by assertions on failures. Successful execution confirms the exhaustive enumeration of all \(2^{16}=65536\) masks, the symmetry orbit partition, and the three finite counting methods described above. `check_forest.py` confirms the residual-tree diameters of the representative sets. The source code is part of this self-contained package.

## Relationship to prior work

Morrison and Noel, *Extremal Bounds for Bootstrap Percolation in the Hypercube*, arXiv:1506.04686v1 (public 2015-06-15), prove the general formula \(m(Q_d,3)=\lceil d(d+3)/6\rceil+1\) and explicitly exhibit one minimum configuration for dimension four in their Section 5. These results establish the six-seed optimum but do not specify the six-orbit census or the three-neighbor completion-time stratification. Riedl's 2010 work and Shende's 2015 work concern **two-neighbor** percolation and hence do not establish the threshold-three statement.

There is also relevant published work on minimum feedback vertex sets and induced forests of the four-cube. The forest equivalence above means that the number of minimal seed sets, and the eight six-seed optima in particular, are closely related to previously studied feedback-set counts; they should not be claimed as priority results independently of those works. The distinct assertion here is the *joint symmetry-and-diameter classification* of all maximal induced forests and its exact infection-time consequences. Indexed descriptions of the closest feedback-set and induced-forest works do not report that joint classification. Their complete published packages could not be accessed for whole-document comparison, so historical overlap in their appendices remains an explicit risk.

## Limitations

This is a finite theorem only for the fixed four-cube with threshold three; it makes no general claim for arbitrary dimension or other infection thresholds. Exhaustive checkers constitute a reproducible finite proof, not an analytic formula for all cubes. Published-literature priority is not certified, especially for older computations of induced-forest facets and supplementary material not available in full. The referenced formula for the minimum size and the eight minimum solutions are treated as known background; the timing and orbit refinement is the contribution under review.

## References

1. N. Morrison and J. A. Noel, *Extremal Bounds for Bootstrap Percolation in the Hypercube*, arXiv:1506.04686v1, 2015-06-15. https://arxiv.org/abs/1506.04686
2. E. Riedl, *Largest Minimal Percolating Sets in Hypercubes under 2-Bootstrap Percolation*, Electronic Journal of Combinatorics 17 (2010), R80. https://doi.org/10.37236/352
3. A. M. Shende, *Maximal induced paths and minimal percolating sets in hypercubes*, Journal of Algebra Combinatorics Discrete Structures and Applications 2 (2015), 17–24. https://doi.org/10.13069/jacodesmath.15518
