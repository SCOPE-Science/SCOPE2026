# Exactly 4,800 ternary surjection universal cycles in 410 symmetry classes

## Finding

Let \(\mathcal W\) be the set of length-four words on the labeled alphabet \(\{0,1,2\}\) containing each of the three symbols at least once. There are exactly \(36\) such words. A circular universal word lists every member of \(\mathcal W\) exactly once among its cyclic length-four windows, with no other windows. There are exactly **\(4{,}800\)** universal words modulo cyclic rotation, keeping the three symbol labels fixed.

Under alphabet relabeling by \(S_3\) and reversal, there are exactly **\(410\)** equivalence classes: **\(20\)** classes of size \(6\) and **\(390\)** classes of size \(12\). In particular, no universal word is rotation-equivalent to its reversal after any alphabet relabeling. Under alphabet relabeling alone, the \(4{,}800\) cycles form \(820\) classes, of which \(40\) have size \(3\) and \(780\) have size \(6\).

## Assumptions and scope

A cyclic word of length \(36\) has cyclic windows \(w_iw_{i+1}w_{i+2}w_{i+3}\), with indices modulo \(36\). Only cyclic rotation identifies words in the first enumeration. The group for the second enumeration is \(S_3\times C_2\): permutations of the alphabet and reversal of reading direction. No symbol relabeling or reversal is identified in the first count. This concerns the first nontrivial ternary surjective-word order, window length four; it is not an enumeration for larger orders or alphabets.

## Proof

**Overlap graph and forced-path contraction.** Build the directed overlap graph with an edge \(abcd\) from vertex \(abc\) to \(bcd\) for each \(abcd\in\mathcal W\). Its \(24\) vertices are precisely the ternary three-letter words with at least two different letters. Six vertices use all three letters, and each has indegree and outdegree \(3\). Each of the other \(18\) vertices uses exactly two letters and has indegree and outdegree \(1\): the omitted symbol is forced at either end. From any all-distinct three-letter vertex, following one outgoing edge through degree-one vertices reaches another all-distinct vertex within two intermediate vertices. Thus contracting these forced paths neither loses a vertex component nor changes the set of Euler circuits.

The six remaining vertices are \(012,021,102,120,201,210\). Their directed adjacency is the symmetric directed double of the triangular prism: one triangle consists of \(012,120,201\), another of \(021,102,210\), with matching edges \(012\leftrightarrow210\), \(120\leftrightarrow021\), and \(201\leftrightarrow102\). This is checked directly by tracing each of the three outgoing edges from each of the six vertices. Every contracted vertex has indegree and outdegree \(3\). The underlying prism is connected, so the directed graph is strongly connected.

**The rotation-class count.** The prism is the Cartesian product \(C_3\square K_2\); its Laplacian eigenvalues, with multiplicities, are \(0,2,3,3,5,5\). The matrix-tree theorem gives \(\tau=(2\cdot3^2\cdot5^2)/6=75\) spanning trees. For the bidirected prism each spanning tree uniquely orients toward any selected root, so there are \(75\) directed in-arborescences at that root. The BEST theorem gives \(\tau\prod_v(d^+(v)-1)!=75(2!)^6=4{,}800\) Euler tours having a specified first directed edge. Restoring each uniquely forced path gives a bijection with the original Euler tours. Every desired universal circle contains the edge \(0120\) exactly once, so choosing that edge first fixes one and only one representative of each rotation class. This establishes \(4{,}800\).

**The symmetry census.** The appended executable `verify.py` is an exhaustive integer certificate for the finite orbit assertions, and its finite domain is complete, not sampled. Fix \(0120\) as the first edge. At the vertex \(012\) the outgoing edge order then has \(2!\) possibilities; at each of the other five degree-three vertices it has \(3!\) possibilities. All eighteen degree-one vertex orders are forced. Enumerating the \(2!(3!)^5=15{,}552\) such local order tuples and following their deterministic Euler trails yields exactly \(4{,}800\) complete tours, each independently checked for the \(36\) required cyclic windows. Different tuples cannot generate the same rooted tour, and every tour provides exactly one tuple, proving completeness.

The verifier applies all twelve operations \(S_3\times C_2\), canonicalizing each image by the unique occurrence of \(0120\). It finds \(40\) fixed cycles for each of the three symbol transpositions; no three-cycle has fixed cycles, and no operation involving reversal has any fixed cycles. Thus Burnside's lemma yields \((4800+3\cdot40)/12=410\) classes. The verifier also forms every full orbit, yielding exactly \(20\) six-element and \(390\) twelve-element orbits. The color-only orbit sizes are independently recorded as \(40\) size-three and \(780\) size-six orbits. These exhaust all possibilities.

## Verification

Run `python3 verify.py` in a directory containing that file. It requires only Python's standard library. It independently constructs the constrained overlap graph, contracts all forced paths, evaluates a five-by-five Laplacian cofactor by exact Leibniz expansion (obtaining \(75\)), enumerates every normalized Euler tour, checks each word's cyclic-window set, tests all group-action fixed points, and exhaustively builds the symmetry orbits. Its expected final message begins `VERIFY_OK windows=36 contract_vertices=6 trees=75 cycles=4800 symmetry_classes=410`.

## Relationship to prior work

LaBounty-Lay, Bechel and Godbole (2008), Theorem 4, prove *existence* of universal cycles for surjections when the word length exceeds the alphabet size, and explain the same degree-one/degree-three phenomenon in general. The result here is an exact enumeration at the smallest ternary order together with a complete symmetry census, neither asserted in that existence theorem. Leitner and Godbole (2008), Theorem 4, restate this existence criterion. Blanca and Godbole (2010), Theorem 11, establish existence for the more general language of words containing specified required characters; this again does not imply a cycle count. The classical BEST and directed matrix-tree theorems are used as standard tools, not claimed as new results.

## Limitations

This is an exact finite-order result only: no general product formula for arbitrary alphabet size and window order is asserted. The symmetry census relies on a complete reproducible finite enumeration; its correctness depends on the enumerated normalization and exhaustive traversal, both explicitly checked in the delivered program. Novelty is relative to the accessible literature and does not exclude unindexed earlier exact enumerations. Independent external validation has not been performed.

## References

- B. LaBounty-Lay, A. Bechel, A. P. Godbole, *Universal Cycles of Discrete Functions*, 2008, arXiv:0805.1672, https://arxiv.org/abs/0805.1672 (first posted 2008-05-12).
- A. Leitner, A. Godbole, *Universal Cycles of Restricted Classes of Words*, 2008, arXiv:0808.1309, https://arxiv.org/abs/0808.1309.
- A. Blanca, A. P. Godbole, *On Universal Cycles for New Classes of Combinatorial Structures*, 2010, arXiv:1008.2251, https://arxiv.org/abs/1008.2251.
- BEST theorem and directed matrix-tree theorem, classical Euler-tour and spanning-tree enumeration results.
