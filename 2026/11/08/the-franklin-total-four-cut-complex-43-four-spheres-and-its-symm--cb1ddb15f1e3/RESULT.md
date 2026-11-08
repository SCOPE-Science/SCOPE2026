# The Franklin total four-cut complex: 43 four-spheres and its symmetry character

## Finding
Let \(F\) be the twelve-vertex Franklin graph, with vertex set \(\mathbb Z/12\mathbb Z\), cycle edges \(\{i,i+1\}\), and the six additional edges \(\{2j,2j+5\}\) for \(0\le j<6\), all subscripts taken modulo \(12\). Let \(X=\Delta^t_4(F)\) be the **total four-cut complex**: a subset \(\sigma\subseteq V(F)\) is a face precisely when the complement contains four pairwise nonadjacent vertices of \(F\).

**Theorem.** There is an integral homotopy equivalence
\[
  X\simeq \bigvee^{43}S^4.
\]
The complex is pure of dimension \(7\) and is not shellable. Its only nonzero reduced integral homology group is \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^{43}\). The full graph automorphism group has \(48\) elements; its rational degree-four homology character has the following values on the ten conjugacy classes. In the table, the cycle type is the cycle structure of the representative permutation of the twelve graph vertices.

| Conjugacy-class size | Vertex cycle type | Trace on \(\widetilde H_4(X;\mathbb Q)\) |
| ---: | --- | ---: |
| 1 | \(1^{12}\) | 43 |
| 3 | \(2^2 1^8\) | 5 |
| 3 | \(2^4 1^4\) | -1 |
| 6 | \(2^6\) | -7 |
| 6 | \(2^6\) | -5 |
| 1 | \(2^6\) | 1 |
| 8 | \(3^4\) | 1 |
| 6 | \(4^2 2^2\) | -1 |
| 6 | \(4^2 2^2\) | 1 |
| 8 | \(6^2\) | 1 |

In particular, the invariant rational subspace \(\widetilde H_4(X;\mathbb Q)^{\operatorname{Aut}(F)}\) has dimension zero.

## Assumptions and scope
The Franklin graph is simple, cubic, connected, and bipartite. The graph presentation above is the Hamiltonian LCF presentation \([5,-5]^6\). The vertex labels are part of the finite certificate but not of the homotopy invariant. A four-element set is independent if none of its six pairs is an edge. The total four-cut complex consists of all subsets contained in the complement of some independent four-set. It is an ordinary abstract simplicial complex, not the complex of minimal graph cuts.

There are exactly \(45\) independent four-subsets, and each gives an eight-vertex facet. These facets are distinct, so the complex is pure of dimension \(7\). The enumeration covers all \(2^{12}=4096\) vertex subsets.

## Proof
**1. Exact face poset.** Use a bitmask for a subset of the twelve vertices. Enumerate all \(\binom{12}{4}=495\) four-subsets and retain those in which every pair is nonadjacent. Exactly \(45\) remain. A bitmask is a face if and only if it is disjoint from at least one retained independent-four bitmask. This yields \(2533\) augmented faces (including the empty face), with the nonempty face vector in dimensions \(0\) through \(7\)
\[
 (12,66,220,495,792,638,264,45).
\]
The standalone scripts provide exact executable predicates for all these steps, rather than sampling.

**2. Acyclic matching.** On the full augmented face poset, apply successive elementary *element matchings* in vertex order
\[
 (7,9,11,2,4,5,1,8,0,3,10,6).
\]
At stage \(v\), among the currently unmatched faces pair each face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), when the latter is also currently unmatched. The algorithm produces \(1245\) disjoint matched covering pairs. Precisely \(43\) unmatched faces remain, and every one has five vertices (dimension \(4\)). In particular, the empty face is paired with vertex \(7\).

To certify acyclicity without relying on a heuristic, construct all \(12780\) covering incidences of the augmented face poset. Orient each matched incidence from its upper face to its lower face and every unmatched incidence from lower to upper. A complete topological sort processes all \(2533\) vertices of this directed graph, proving that there is no directed cycle. Remove the pair between the empty face and vertex \(7\); the corresponding ordinary face-poset orientation independently topologically sorts all \(2532\) nonempty faces. Therefore the ordinary acyclic matching has exactly one critical vertex, \(43\) critical four-cells, and no other critical cells.

Forman's discrete Morse theorem supplies a CW complex homotopy equivalent to \(X\) with one zero-cell and \(43\) four-cells and no cells in dimensions \(1,2,3\). Every four-cell attaches to the zero-skeleton, so the CW complex is the wedge of \(43\) four-spheres. In particular, this is an **integral homotopy** conclusion, not an extrapolation from finite-field Betti numbers. Since \(X\) is pure of dimension \(7\) yet has nonzero degree-four reduced homology, pure shellability is impossible.

**3. Complete rational character.** Enumerate all graph automorphisms as permutations preserving the explicitly listed eighteen edges. There are \(48\). Their conjugation orbits give ten conjugacy classes, of the listed sizes. For each automorphism \(g\), its action on the augmented simplicial chains yields the reduced Lefschetz formula
\[
\operatorname{tr}\bigl(g_*\mid\widetilde H_4(X;\mathbb Q)\bigr)
= -1+\sum_{\substack{\emptyset\ne\sigma\in X\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g\mid_\sigma).
\]
Here \(\operatorname{sgn}(g\mid_\sigma)\) denotes the sign of the permutation that carries the increasing order of the vertices of \(\sigma\) into the increasing order of their images. The initial \(-1\) is the augmented empty-face term. This equality holds because the Morse computation has already proved that all reduced homology other than degree four vanishes. Direct enumeration of every invariant face gives the ten traces in the table. The class-size-weighted sum of the traces is zero, so averaging over the full group gives zero invariant rank.

## Verification
Run `python verify_franklin_four_cut.py` using only Python's standard library. It regenerates the graph, all independent four-sets and simplicial faces, the entire matching, both augmented and ordinary Hasse acyclicity checks, all \(48\) automorphisms, the exact ten conjugacy classes, and each signed homology trace; the expected terminal marker is `ALL_VERIFY_OK`.

Independently run `python verify_franklin_homology.py` for the original simplicial boundary matrices, without the Morse matching. Over each of \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), the boundary ranks from dimensions one through seven are
\[
 (11,55,165,330,419,219,45),
\]
and the unreduced Betti vector is \((1,0,0,0,43,0,0,0)\). Its terminal marker is `ALL_HOMOLOGY_OK`. These field calculations corroborate the topology; the integral statement comes from the checked acyclic matching.

## Relationship to prior work
The total cut construction originates in Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue, *Total Cut Complexes of Graphs* (first posted September 27, 2022), which gives general properties, complete bipartite cases, and graph-grid Betti data. Carnero Bravo's *Total cut complexes and their duals* (first posted February 24, 2026) adds Alexander-dual comparisons, complete multipartite families, powers of cycles, and results for Cartesian products, including an open question about higher-parameter Cartesian-product complexes. Neither inspected manuscript provides the four-cut homotopy type or the full automorphism character of this particular non-Cartesian, four-cycle-containing cubic graph.

The known three-robust clique theorem for *all* connected bipartite graphs gives a result at the adjacent parameter \(3\); through Alexander duality it cannot directly determine the present four-cut invariant at parameter \(4\). Published results for the ordinary **matching** complex of the Franklin graph address subsets of graph edges rather than complements of independent vertex four-sets. Another published calculation for a four-cut complex concerns a different graph, the triangular graph \(J(5,2)\). These results explain the nearby landscape but are not equivalent to the present statement. Available searches did not establish global uniqueness; see `REVIEW.md` for the remaining priority risk.

## Limitations
This is an exact result for a single, canonically named twelve-vertex graph and the total four-cut parameter. No all-order or all-cubic-graph classification, integral equivariant lattice decomposition, or equivariant wedge splitting is claimed. The automorphism result is a rational character, not an independently determined integral module. Independent audit has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503 (first public version September 27, 2022), https://arxiv.org/abs/2209.13503.
2. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first public version February 24, 2026), https://arxiv.org/abs/2602.21427.
3. E. W. Weisstein, *Franklin Graph*, MathWorld, https://mathworld.wolfram.com/FranklinGraph.html (LCF presentation and standard graph identification).
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, cited for the discrete Morse homotopy theorem.
