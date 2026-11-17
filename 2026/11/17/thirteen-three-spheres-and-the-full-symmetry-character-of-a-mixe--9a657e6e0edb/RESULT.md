# Thirteen three-spheres and the full symmetry character of a mixed three-petal strong-Morse complex

## Finding
Let \(G\) be the one-dimensional unfilled simplicial graph consisting of two triangles and one four-cycle, all meeting in exactly one central vertex and otherwise vertex-disjoint. Let \(\mathcal{SM}(G)\) be the **full** strong discrete-Morse matching complex, namely the downward closure of the matching-incidence sets produced by strict vertex filtrations (not the pure subcomplex). Then
\[
|\mathcal{SM}(G)|\simeq\bigvee^{13}S^3.
\]
In particular the only nonzero reduced integral homology group is \(\widetilde H_3\cong\mathbb Z^{13}\), with no torsion.

The complete graph automorphism group is \((C_2\wr S_2)\times C_2\), of order sixteen. Its rational character on \(H_3(\mathcal{SM}(G);\mathbb Q)\) is as follows. The first factor permutes the two two-vertex triangle branches, and the final \(C_2\) reverses the four-cycle while fixing its central and opposite vertices.

| Triangle-branch action | Elements in the first factor | Square fixed | Square reversed |
|---|---:|---:|---:|
| Identity | 1 | 13 | -9 |
| Flip exactly one triangle branch | 2 | -7 | 3 |
| Flip both triangle branches | 1 | 5 | -1 |
| Exchange branches, with equal internal flips | 2 | -7 | 3 |
| Exchange branches, with unequal internal flips | 2 | 5 | -1 |

The column entries are rational traces, not fixed-subspace dimensions. This determines the full representation character on all sixteen automorphisms.

## Assumptions and scope
Use graph vertices \(V=\{0,1,2,3,4,5,6,7\}\), with \(0\) the common central vertex, and undirected edges
\[
\{01,12,20,03,34,40,05,56,67,70\}.
\]
An edge \(ab\) here denotes the unordered pair \(\{a,b\}\). All cycles are unfilled: there are graph edges but no two-dimensional faces in the original simplicial graph. The vertex set of \(\mathcal{SM}(G)\) consists of oriented incidences \((v,w)\) along graph edges, representing a pair of simplices \((\{v\},\{v,w\})\). For each permutation \(\pi\) of the eight graph vertices, scan vertices in that order; include \((v,w)\) exactly when \(w\) is the **unique** neighbor of \(v\) preceding \(v\). The resulting incidence set is a generator; every subset of every generated incidence set is a face. This matches the strict-filtration definition: the descending link of a vertex in a one-dimensional simplicial graph is a discrete set of earlier neighbors, which is a nonempty simplicial cone exactly when it contains one point.

## Proof
There are exactly \(8!=40320\) strict vertex orders. The self-contained certificate `verify_mixed_cactus.py` iterates over **all** of them, obtains exactly 345 distinct incidence sets, and takes their full downward closure. This yields 493 faces including the empty face, with nonempty face vector
\[
(f_0,f_1,f_2,f_3)=(20,108,220,144).
\]
No face of higher dimension is present, because every face was generated and checked in the finite enumeration.

Order the twenty oriented incidences lexicographically and apply the following succession of toggles (zero-based incidence indices):

`14, 6, 18, 8, 5, 16, 19, 9, 7, 10, 13, 12, 2, 0, 11, 15, 4, 3, 1, 17`.

At a toggle, match each still-unmatched face not containing that incidence with its still-unmatched one-incidence extension, if present. This constructs exactly 239 distinct pairs of faces of adjacent dimensions. The certificate constructs the entire Hasse diagram of the 492 nonempty faces, reverses the 239 matched cover relations, and topologically sorts the directed diagram. It visits all 492 nodes, proving **acyclicity**, rather than assuming greedy selection is always acyclic. The 14 unmatched faces consist of one zero-dimensional face and thirteen three-dimensional faces, with none in dimensions one or two. Forman's discrete Morse theorem therefore supplies a CW model with one zero-cell and thirteen three-cells, and no intermediate cells; their attaching maps are constant, so its homotopy type is exactly the displayed wedge of thirteen three-spheres.

For the character statement, the central vertex is the unique degree-six vertex. Removing it leaves two graph edges and a three-vertex path; this forces every automorphism to permute the two triangle branches, possibly reverse each, and independently reverse the square branch. All sixteen combinations occur. The induced action on oriented incidences preserves the set of generated faces. For each automorphism \(g\), the certificate sums the signed permutation traces on all oriented simplicial chain groups:
\[
L(g)=\sum_{d=0}^{3}(-1)^d\operatorname{tr}(g\mid C_d(\mathcal{SM}(G);\mathbb Q)).
\]
A face contributes zero unless it is preserved as a set; a fixed face contributes the sign of the permutation induced on its ordered incidence vertices, with the degree sign. Since the homotopy calculation gives \(H_0\cong\mathbb Q\) and only \(H_3\cong\mathbb Q^{13}\) otherwise, the Hopf trace formula gives
\[
\operatorname{tr}(g\mid H_3)=1-L(g).
\]
Exhausting all sixteen actual graph automorphisms gives precisely the table above. Thus the character calculation is a consequence of explicit signed chain traces, independent of selecting equivariant Morse pairs.

## Verification
Run `python3 verify_mixed_cactus.py` using Python's standard library only. The expected transcript is embedded as `verification_output.txt`. The script asserts graph preservation by all group actions, exhaustive generation, full face counts, acyclic Hasse orientation, the number and dimensions of critical faces, and the class-by-class signed Lefschetz traces. Independent mod-two boundary ranks on the uncollapsed complex are \((19,89,131)\) in dimensions one through three, yielding reduced Betti ranks \((0,0,0,13)\); these checks corroborate but do not replace the integral homotopy proof.

## Relationship to prior work
Knudson and Owens-White, *Complexes of strong discrete Morse matchings* (arXiv:2609.06844, first submitted September 6, 2026), introduce and study these full matching complexes, including paths, stars, cycles, simplices and their boundaries. The graph here is instead a three-petal mixed cactus, with two triangular petals and one quadrilateral petal. Known uniform friendship-graph cases give thirteen circles for the two-triangle bouquet; adding one quadrilateral raises the degree to three **without changing the sphere count**, a distinction not implied by the uniform-case formula. Previously computed triangle-plus-one-cycle cases have only two petals, not the present three-petal graph. The explicit full sixteen-element symmetry character is also not determined by those homotopy equivalences. Literature and semantic-record searches did not locate an equivalent result, but cannot prove absolute priority.

## Limitations
This is an exhaustive **finite** theorem for the specified eight-vertex graph, not an infinite-family formula or a classification of all mixed cacti. It concerns the full strong-Morse matching complex, not the ordinary or pure Morse matching complex. The character determines the rational representation up to isomorphism but does not specify an integral equivariant lattice or an equivariant homotopy equivalence. Scientific checks and a reproducible certificate do not constitute independent validation; further bibliographic comparison may expose unindexed coverage.

## References
1. K. P. Knudson and A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (2026-09-06), https://arxiv.org/abs/2609.06844 .
2. X. Fernández, *Strong discrete Morse theory*, Proceedings of the Royal Society of Edinburgh Section A (2026), https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/strong-discrete-morse-theory/DD4EB8F8EF04FF8A5CE06F5F58DD7532 .
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145.
