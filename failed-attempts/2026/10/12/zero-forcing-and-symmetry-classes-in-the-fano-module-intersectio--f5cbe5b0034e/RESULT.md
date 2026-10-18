# Zero forcing and symmetry classes in the Fano module-intersection graph

## Finding

Let \(V=\mathbb F_2^3\), and let \(\mathcal G(V)\) be Yaraneri's intersection graph whose vertices are all proper subspaces of \(V\), with distinct subspaces adjacent exactly when their intersection is nonzero. Then \(\mathcal G(V)\) has \(15\) vertices and zero forcing polynomial \[\mathcal Z(\mathcal G(V);u)=1204u^8+2100u^9+1792u^{10}+980u^{11}+364u^{12}+91u^{13}+14u^{14}+u^{15}.\] Moreover \(Z(\mathcal G(V))=M(\mathcal G(V))=8\) and the real symmetric minimum rank is \(7\). There are exactly \(1204\) minimum zero forcing sets. Under the natural \(\mathrm{GL}(3,2)\)-action, these minimum sets form exactly ten orbits, with orbit-size multiset \[\{28,84,84,84,84,168,168,168,168,168\}.\]

This is the smallest three-dimensional vector-space module over a finite field, so it is the first projective-plane case of the module-intersection construction. The ten symmetry classes refine the bare value of the zero forcing number by describing how minimum forcing configurations sit in the Fano incidence geometry.

## Assumptions and scope

Let
\[
V=\mathbb F_2^3.
\]
Following Yaraneri, \(\mathcal G(V)\) has one vertex for every proper subspace of \(V\), including the zero subspace, and two distinct vertices are adjacent when their intersection is nonzero.

There are seven one-dimensional subspaces and seven two-dimensional subspaces. The nonzero proper part is naturally the point-line geometry of the Fano plane: the one-dimensional subspaces are its points and the two-dimensional subspaces are its lines.

The standard zero forcing rule is used: a blue vertex with exactly one white neighbor may force that neighbor blue.

## Proof

The zero subspace is isolated. The seven one-dimensional subspaces are pairwise nonadjacent. Any two distinct two-dimensional subspaces of \(V\) meet in a one-dimensional subspace, so the seven two-dimensional vertices form a clique. A one-dimensional subspace is adjacent to a two-dimensional subspace exactly when it is contained in it. Thus the active fourteen-vertex component is the Fano point-line incidence graph with the line side completed to a clique.

We first prove the lower bound on zero forcing without enumeration. Label the seven one-dimensional subspaces by the seven nonzero vectors of \(\mathbb F_2^3\), and use the same vectors as normals for the seven two-dimensional subspaces. In \(\mathbb R^7\), assign to each point vertex the corresponding standard basis vector. Assign to each plane vertex its seven-coordinate Fano incidence vector. Two point vectors are orthogonal, a point vector has nonzero inner product with a plane vector exactly when the point lies in the plane, and two distinct plane incidence vectors have inner product one because two Fano lines meet in exactly one point. Assign the zero vector to the isolated zero-subspace vertex.

The resulting real symmetric Gram matrix has exactly the required off-diagonal graph pattern and rank \(7\). Therefore
\[
\operatorname{mr}(\mathcal G(V))\le7,
\qquad
M(\mathcal G(V))\ge15-7=8.
\]
The standard inequality \(M(G)\le Z(G)\) gives
\[
Z(\mathcal G(V))\ge8.
\]

For the matching upper bound, index the point vertices by
\[
(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)
\]
and the plane vertices by the same list of normal vectors, with incidence given by zero dot product over \(\mathbb F_2\). Take initially blue the zero subspace; the first four listed point vertices; and the planes with normals
\[
(0,0,1),(0,1,0),(1,0,0).
\]
The packaged verifier checks the following seven successive forces in its integer indexing:
\[
1\to13,
\quad2\to12,
\quad4\to10,
\quad3\to14,
\quad8\to6,
\quad9\to5,
\quad10\to7.
\]
Hence a zero forcing set of size \(8\) exists, and so
\[
Z(\mathcal G(V))=8.
\]
Combining this with the rank-seven witness and \(M\le Z\) gives
\[
\operatorname{mr}(\mathcal G(V))=7,
\qquad
M(\mathcal G(V))=8.
\]

The remaining assertions are finite exact classifications. The packaged checker tests all \(2^{15}=32768\) vertex subsets and obtains
\[
\begin{array}{c|rrrrrrrr}
k&8&9&10&11&12&13&14&15\\ \hline
z(\mathcal G(V);k)&1204&2100&1792&980&364&91&14&1.
\end{array}
\]
This is exactly the displayed zero forcing polynomial.

For the symmetry classification, the checker enumerates all \(168\) invertible \(3\)-by-\(3\) matrices over \(\mathbb F_2\). A matrix acts on point vectors in the usual way and on plane normals by inverse transpose; the zero subspace is fixed. The program applies these graph automorphisms to all \(1204\) minimum zero forcing sets and computes their complete orbit partition. The orbit sizes are
\[
28,84,84,84,84,168,168,168,168,168,
\]
which sum to \(1204\). Thus there are exactly ten orbits.

## Verification

The standalone `verify.py` is self-contained. It constructs the fifteen-vertex graph directly from \(\mathbb F_2^3\), verifies every incidence and clique edge, enumerates every subset for the full zero forcing polynomial, checks the explicit forcing trace, constructs the rank-seven Gram matrix and computes its exact rational rank, enumerates \(\mathrm{GL}(3,2)\), and partitions all minimum forcing sets into symmetry orbits.

Exact replay output:

```text
POLYNOMIAL {8: 1204, 9: 2100, 10: 1792, 11: 980, 12: 364, 13: 91, 14: 14, 15: 1}
MINIMUM_SETS 1204
EXPLICIT_WITNESS (0, 1, 2, 3, 4, 8, 9, 11)
FORCE_TRACE [(1, 13), (2, 12), (4, 10), (3, 14), (8, 6), (9, 5), (10, 7)]
GRAM_RANK 7
GL32_ORDER 168
MINIMUM_SET_ORBIT_SIZES [28, 84, 84, 84, 84, 168, 168, 168, 168, 168]
VERIFY_OK
```

The lower bound and minimum-rank statement have symbolic proofs independent of the enumeration. The polynomial coefficients and orbit classification are finite exhaustive statements, and their exhaustiveness is supplied by the checker.

## Relationship to prior work

Yaraneri introduced and studied the intersection graph of proper submodules in the form used here, with primary Mathematics Subject Classification \(16D10\). The paper studies connectedness, domination, finiteness, coloring, planarity, cycles, and clique structure; it does not study zero forcing. Its public preprint first appeared on 9 August 2012.

Earlier and later module-intersection literature commonly uses the nontrivial-submodule convention, which in this example is simply the fourteen-vertex active component obtained by deleting the isolated zero subspace. The present computation deliberately uses Yaraneri's all-proper-submodule convention, so the isolated vertex is part of the stated polynomial and zero forcing number.

Targeted searches for “zero forcing”, “minimum rank”, “intersection graph of a module”, “submodule intersection graph”, “Fano plane”, and “subspace intersection graph” did not locate the polynomial, the rank-seven theorem, or the ten-orbit classification. A highly relevant full publisher preview of Yaraneri's article and the standard module-intersection literature were inspected directly.

## Limitations

The finding is an exact classification for \(\mathbb F_2^3\); it does not assert the same polynomial pattern for \(\mathbb F_q^3\) at arbitrary \(q\).

The orbit classification is with respect to the natural linear group \(\mathrm{GL}(3,2)\). No claim is made here that this presentation is the only useful description of the minimum forcing sets.

The exhaustive computation is finite and complete for this graph, but it is not used as evidence for an infinite family.

## References

1. E. Yaraneri, “Intersection Graph of a Module,” *Journal of Algebra and Its Applications* 12 (2013), 1250218. DOI: 10.1142/S0219498812502180. Public preprint: arXiv:1208.1897, first posted 9 August 2012.
2. S. Akbari, H. A. Tavallaee, and S. Khalashi Ghezelahmad, “Intersection Graph of Submodules of a Module,” *Journal of Algebra and Its Applications* 11 (2012), 1250019. DOI: 10.1142/S0219498811005452.
3. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
