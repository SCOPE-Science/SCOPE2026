# First branching in symmetric quotients of complete directed-forest complexes

## Finding

Let \(\Delta_n\) be the simplicial complex of directed forests in the complete loopless bidirected graph on the labeled vertex set \([n]\). Its simplicial vertices are directed arcs \(i\to j\) for distinct labels, and its nonempty faces are arc sets with at most one incoming arc at each label and with no directed cycle. The symmetric group \(S_n\) acts by simultaneously permuting all labels. Define the **ordinary geometric quotient** \(Y_n=|\Delta_n|/S_n\).

For the complete initial nontrivial range \(2\le n\le5\), the homotopy types are

\[
Y_2\simeq\{\mathrm{pt}\},\quad
Y_3\simeq S^1,\quad
Y_4\simeq S^2,\quad
Y_5\simeq S^3\vee S^3.
\]

Thus five labels provide the first branching into multiple positive-dimensional spheres in this range. These are homotopy equivalences over the integers, not merely equalities of rational Betti numbers.

## Assumptions and scope

The graph has **both** arcs between any two distinct graph vertices, but no loops. A face is a rooted directed forest, including isolated graph vertices: each component is an out-arborescence. The simplex for a set of \(k\) arcs has dimension \(k-1\); hence \(\dim\Delta_n=n-2\). Only the ordinary topological quotient of geometric realizations is under consideration, not a Borel construction or the simplicial complex built naively from face-orbit vertices.

We restrict the homotopy classification to the four integers \(2\le n\le5\). Nothing about the homotopy types for larger \(n\) follows from this finite calculation.

## Proof

**A stabilizer-aware cell model.** Let \(P_n\) be the poset of all nonempty directed-forest faces ordered by proper inclusion. The barycentric subdivision \(\operatorname{sd}\Delta_n\) has a simplex for every strict flag of faces \(F_0\subsetneq\cdots\subsetneq F_d\). Relabeling preserves face cardinalities, so any group element stabilizing such a flag fixes its barycenters individually. The action on the subdivision therefore has no inversions. Its quotient admits a finite \(\Delta\)-complex structure, with one oriented \(d\)-simplex per \(S_n\)-orbit of strict flags of length \(d+1\). If \([F_0,\ldots,F_d]\) denotes an orbit, its integral cellular boundary is

\[
\partial [F_0,\ldots,F_d]
=\sum_{j=0}^{d}(-1)^j[F_0,\ldots,\widehat{F_j},\ldots,F_d].
\]

Here the brackets on the right mean the orbit of the **entire shortened flag**, not merely the ordered sequence of individual face orbits. This distinction accounts for stabilizers correctly.

**Exact finite enumeration.** Enumerate all nonempty arc subsets with at most \(n-1\) arcs; retain an arc set precisely when all target labels are distinct and following parent pointers produces no cycle. For each flag, minimize its tuple of arc-bitmasks over all \(n!\) simultaneous label permutations. Apply the boundary formula above, obtaining integral boundary matrices. The following table lists, in order, the number of quotient cells by dimension and ranks of the consecutive integral differentials. Every *nonzero* Smith invariant factor is \(1\), including all 123 factors of the last differential for \(n=5\).

| \(n\) | Quotient cells by dimension | Boundary ranks \(\operatorname{rank}\partial_1,\ldots\) | Integral Betti numbers |
|---|---|---|---|
| 2 | \((1)\) | none | \((1)\) |
| 3 | \((3,3)\) | \((2)\) | \((1,1)\) |
| 4 | \((8,22,16)\) | \((7,15)\) | \((1,0,1)\) |
| 5 | \((19,121,226,125)\) | \((18,103,123)\) | \((1,0,0,2)\) |

The exact Smith forms and \(\partial^2=0\) give the integral homology, with no hidden torsion. As an independent check on cell enumeration, the signed Burnside–Lefschetz sum of the original oriented simplex action gives quotient Euler characteristics \(1,0,2,-1\), matching the alternating sums of these quotient cell counts.

**Upgrade from homology to homotopy.** At \(n=2\), the original complex has two isolated arc vertices exchanged by \(S_2\), so its quotient is a point. At \(n=3\), the quotient is a connected graph with three vertices and three edges, hence is a circle up to homotopy.

For \(n=4,5\), the original complex is pure shellable: the complete directed graph has a complete source, so the theorem of Kozlov, elaborated by Jojić, applies. Thus \(|\Delta_n|\) is homotopy equivalent to a wedge of \((n-1)^{n-1}\) spheres of dimension \(n-2\), hence is simply connected for these two values. Every transposition \((a\ b)\in S_n\) fixes the barycenter of any arc \(c\to d\) supported on two labels outside \(\{a,b\}\). Such labels exist for \(n\ge4\). Transpositions generate \(S_n\), so Armstrong's orbit-space fundamental-group theorem gives

\[
\pi_1(|\Delta_n|/S_n)=1\qquad(n=4,5).
\]

For \(n=4\), the quotient is a simply connected two-dimensional CW complex with \(\widetilde H_2\cong\mathbb Z\) and vanishing other reduced homology; by Hurewicz and the simply connected homology Whitehead theorem it is homotopy equivalent to \(S^2\). For \(n=5\), the quotient is simply connected and has \(H_2=0\), hence is two-connected by Hurewicz; the Hurewicz map \(\pi_3\to H_3\cong\mathbb Z^2\) is an isomorphism. Choose two spherical maps realizing a basis. The induced \(S^3\vee S^3\to Y_5\) is an integral homology equivalence between simply connected CW complexes, hence a homotopy equivalence by Whitehead's theorem.

## Verification

Run `python verify.py` with Python 3.10 or later and SymPy installed. The program enumerates directed forests and *whole-flag orbits* from the definitions, builds integer boundary matrices, checks each composition \(\partial_{d-1}\partial_d=0\), computes Smith normal forms over \(\mathbb Z\), independently recomputes Euler characteristics by the signed Burnside–Lefschetz formula, and checks all table entries. `verification_output.txt` gives the actual output of the embedded program. These exact finite checks establish the integral homology and Euler assertions; the cited shellability, orbit-space fundamental-group theorem, and Hurewicz–Whitehead argument establish the stronger homotopy classification.

## Relationship to prior work

Engström (first publicly posted August 8, 2005) defines directed-forest complexes and studies their shellability and decomposition methods. Jojić (first posted September 21, 2011) proves a shelling for complexes with a complete source, calculates the labeled complete-digraph \(h\)-vector in Corollary 4, and describes sphere subcomplexes in Proposition 8 and Corollary 9. Those labeled-complex results imply simple connectivity here, but do not themselves specify the ordinary symmetric-label orbit spaces. Armstrong (1965) gives the orbit-space fundamental-group theorem used above. The distinguishing computation concerns flag orbits and their **integral** boundary maps.

## Limitations

The scope is \(2\le n\le5\); in particular, it does not assert any all-size recurrence or eventual stability. The code requires an installed exact-arithmetic SymPy implementation, but does not rely on floating-point rank tests. The homotopy conclusion uses established external theorems rather than a direct equivariant collapse. Bibliographic searches cannot rule out an equivalent result in unindexed material; a related later thesis on Cayley digraph forest complexes was not fully accessible.

## References

1. A. Engström, *Complexes of Directed Trees and Independence Complexes*, first posted 2005-08-08, arXiv:math/0508148, https://arxiv.org/abs/math/0508148 (definitions and directed-tree methods).
2. D. Jojić, *Shellability of Complexes of Directed Trees*, first posted 2011-09-21, arXiv:1109.4475, https://arxiv.org/abs/1109.4475 (complete-source shelling; Corollary 4; Proposition 8; Corollary 9).
3. M. A. Armstrong, *On the fundamental group of an orbit space*, Proc. Cambridge Philos. Soc. **61** (1965), 639–646, https://doi.org/10.1017/S0305004100038974.
