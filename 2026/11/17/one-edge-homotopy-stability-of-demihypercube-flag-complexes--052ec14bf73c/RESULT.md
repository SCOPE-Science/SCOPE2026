# One-edge homotopy stability of demihypercube flag complexes

## Finding

For every integer \(n\ge4\), let \(H_n\) be the graph of even-cardinality subsets of \([n]\), adjacent at symmetric-difference distance two. Put \(K_n=\operatorname{Cl}(H_n)\), the flag complex of this graph. For any graph edge \(e\), the flag complex after removing that edge obeys

\[
K_n^{\setminus e}:=\operatorname{Cl}(H_n-e)\simeq\bigvee^{B_n-(n-3)}S^3,
\qquad B_n=\sum_{i=4}^{n}(-1)^{i-4}2^{n-i}\binom{n}{i}.
\]

A wedge of zero spheres is interpreted as a contractible point. The integral homology inclusion is a split primitive injection

\[
H_3(K_n^{\setminus e};\mathbb Z)\hookrightarrow H_3(K_n;\mathbb Z)
\quad\text{with cokernel }\mathbb Z^{n-3}.
\]

Indeed, there is a homotopy equivalence \(K_n\simeq K_n^{\setminus e}\vee\bigvee^{n-3}S^3\) carrying the displayed inclusion to the first-wedge inclusion up to homotopy. The initial after-deletion sphere multiplicities for \(n=4,5,6,7\) are respectively \(0,7,46,205\); the intact multiplicities are \(1,9,49,209\). The intact values and their general formula are not claimed as new.

## Assumptions and scope

All graphs are finite and simple, and all complexes are ordinary abstract flag complexes; every clique, including those in dimensions greater than three, is retained. Set \(V_n=\{A\subseteq[n]:|A|\text{ even}\}\). Each edge of \(H_n\) is taken exactly once as an unordered pair; graph edge deletion means deleting that pair from the one-skeleton **and** all simplices containing it, not deleting either endpoint. The parameter \(n\) ranges over all integers at least four. Homology is integral unless a coefficient field is indicated. A wedge equivalence is non-equivariant; no canonical group-equivariant choice is asserted.

## Proof

**1. The intact space.** Green's Theorems 3.3.2 and 4.1.2, together with his identification of \(C_{n,4}\) as the half-cube graph's clique complex, give

\[
\widetilde H_j(K_n;\mathbb Z)=\begin{cases}\mathbb Z^{B_n},&j=3,\\0,&j\ne3.\end{cases}
\]

For completeness, \(K_n\) is simply connected: identify its vertices with the vector group of even vectors over \(\mathbb F_2\), and use as a basis the two-coordinate flips \(s_i=\{1,i\}\), \(2\le i\le n\). The corresponding Cayley edges form the one-skeleton of an \((n-1)\)-cube. Every cubical square is filled by two triangles of \(K_n\), using the diagonal of symmetric difference \(s_i\triangle s_j=\{i,j\}\). Every remaining graph edge \(\{i,j\}\), where \(i,j>1\), is homotopic through a flag triangle to a two-edge path of these basis flips. Thus all loops contract through these triangles and filled cubical squares. As the intact space is simply connected with only free \(H_3\), the Hurewicz and homological Whitehead theorems imply \(K_n\simeq\bigvee^{B_n}S^3\).

**2. The deleted edge's link.** Even-vector translation and coordinate permutation are transitive on graph edges, so take \(e=\{\varnothing,\{1,2\}\}\). A vertex adjacent to both endpoints is exactly one of

\[
a_j=\{1,j\},\qquad b_j=\{2,j\},\qquad 3\le j\le n.
\]

In the common-neighbor graph, the \(a_j\)'s form one complete graph, the \(b_j\)'s another, and the only cross-edges are the \(n-2\) pairs \(a_jb_j\). Hence the flag link \(L=\operatorname{lk}_{K_n}(e)\) consists of two simplices with corresponding vertices connected by a matching of \(n-2\) edges. Contracting a spanning tree in each simplex exhibits \(L\simeq\bigvee^{n-3}S^1\). An integral basis for \(H_1(L)\) consists of four-cycles \(a_3a_jb_jb_3a_3\), for \(4\le j\le n\).

**3. The relative map and its integral surjectivity.** Write \(A=K_n^{\setminus e}\). Then \(K_n=A\cup(e*L)\) and \(A\cap(e*L)=(\partial e)*L\). Consequently

\[
H_q(K_n,A;\mathbb Z)\cong\widetilde H_{q-2}(L;\mathbb Z)
=\begin{cases}\mathbb Z^{n-3},&q=3,\\0,&q\ne3.\end{cases}
\]

For every \(j=4,\ldots,n\), hold coordinates outside \(\{1,2,3,j\}\) fixed at zero and take the eight even vertices in those four coordinates. Their induced subcomplex is the boundary of a four-dimensional cross-polytope, a three-sphere \(S_j\subseteq K_n\), containing \(e\). Its edge link is the four-cycle \(a_3a_jb_jb_3a_3\). In relative simplicial chains, quotienting by faces not containing \(e\) identifies the fundamental cycle of \(S_j\) with that oriented link cycle, up to sign. These \(n-3\) cycles form a \(\mathbb Z\)-basis of \(H_1(L)\). Therefore the natural map \(H_3(K_n;\mathbb Z)\to H_3(K_n,A;\mathbb Z)\) is **surjective over the integers**, not merely over a field.

The long exact homology sequence now gives a short exact sequence

\[
0\longrightarrow H_3(A;\mathbb Z)\longrightarrow\mathbb Z^{B_n}\longrightarrow\mathbb Z^{n-3}\longrightarrow0,
\]

with all other reduced homology of \(A\) zero. In particular \(H_3(A;\mathbb Z)\cong\mathbb Z^{B_n-(n-3)}\) and the inclusion has primitive split image.

**4. Homotopy and compatibility.** Since \(L\) is connected, the intersection \((\partial e)*L\simeq\Sigma L\) is simply connected. The other gluing piece \(e*L\) is contractible. Van Kampen, together with simple connectivity of \(K_n\), shows \(A\) is simply connected. Its vanishing \(H_2\) implies it is two-connected, and homological Whitehead upgrades its free third-homology calculation to the displayed wedge of three-spheres. Finally, maps between wedges of three-spheres are determined up to homotopy by the integral degree matrix on \(H_3\). The primitive split inclusion matrix can be diagonalized over \(\mathbb Z\) to the standard summand inclusion, establishing the homotopy-compatible splitting. This proves the claim for every edge and every \(n\ge4\).

## Verification

The standalone verifier `VERIFY.py` constructs the half-cube graph from even-cardinality bit sets with Hamming-two adjacency, recursively enumerates every clique, deletes the edge \(\{0,3\}\), and independently computes simplicial mod-two boundary ranks for \(n=4,5,6\). It also checks the exact two-clique/matching link description in each case. Observed intact/deleted third Betti ranks are respectively \((1,0)\), \((9,7)\), and \((49,46)\), with no other positive-degree homology. Complete enumerated face vectors and ranks are in `VERIFY_OUTPUT.txt`. These finite checks support, but do not replace, Green's integral theorem and the unrestricted relative-chain argument. No claim about infinite parameters is based solely on enumeration.

## Relationship to prior work

Green [1], Theorems 3.3.2 and 4.1.2, already establishes the intact half-cube clique complex's integral homology and the formula for \(B_n\). The intact-sphere homotopy deduction is preparatory, not the original claim. Bendersky–Elia–Grbić [2] studies the full Hamming cube's Vietoris–Rips topology and explicit cross-polytope cycles; its reported results concern the full cube rather than an even-parity induced complex after removing one graph bond. Adamaszek–Adams [3] classifies the full cube's scale-two complex, which does not imply this parity-restricted edge-deletion response. Here the new information is the exact link with its canonical cycle basis, the integral surjectivity of the relative map, and the compatible split homotopy type after deleting any single edge.

## Limitations

This result treats exactly one deleted edge and retains both endpoints. It neither classifies simultaneous edge failures nor determines the full integral equivariant representation of the surviving summand. The homotopy splitting is only asserted up to non-equivariant homotopy. The finite checks use mod-two coefficients, while the integral and all-parameter conclusions follow from the written proof. Unindexed equivalent literature remains a bibliographic risk.

## References

[1] R. M. Green, *Homology representations arising from the half cube*, arXiv:0806.1503 (2008), Theorems 3.3.2 and 4.1.2, https://arxiv.org/abs/0806.1503 .

[2] M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips complex of a hypercube graph*, arXiv:2605.00705, first posted 2026-05-01, https://arxiv.org/abs/2605.00705 .

[3] M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (2021), https://arxiv.org/abs/2103.01040 .
