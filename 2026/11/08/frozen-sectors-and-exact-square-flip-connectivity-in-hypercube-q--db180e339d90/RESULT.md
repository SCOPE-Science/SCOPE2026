# Frozen sectors and exact square-flip connectivity in hypercube quantum-dimer configurations

## Finding
Let \(Q_d\) be the \(d\)-dimensional binary hypercube and let \(\mathcal F_d\) be the flip graph on its perfect matchings, with one allowed transition per alternating coordinate square of length four. A matching is **frozen** when no such flip is available. The following statements hold:

1. \(\mathcal F_2\) and \(\mathcal F_3\) have no frozen matchings.
2. \(\mathcal F_4\) has exactly 272 vertices and 768 undirected edges, partitioned into one connected component of size 264 and eight isolated frozen vertices.
3. Of the 589185 perfect matchings of \(Q_5\), exactly 120 are frozen.
4. For all integers \(d\ge5\), the frozen count \(F_d\) obeys
   \[
   F_d\ge 8\,3^{2^{d-5}}.
   \]

The inequality is a constructive bound on the number of strictly isolated configuration-space sectors under square flips, not a bound on their proportion among all dimer coverings. The known raw perfect-matching totals are not presented as novel; the claim concerns frozen counts, exact small-cube connectivity, and the dimension-uniform construction.

## Assumptions and scope
The graph \(Q_d\) has vertex set \(\{0,1\}^d\), with two vertices adjacent if and only if exactly one coordinate differs. A *perfect matching* contains exactly one incident edge per vertex. A coordinate square is formed by varying two coordinate bits and fixing the others. If a matching contains the two opposite edges of a coordinate square, they can be replaced by the other two opposite edges; this reversible transition defines the undirected *square-flip graph* \(\mathcal F_d\). No flips along hexagons or longer alternating cycles are permitted. Vertices, dimers, and flip states are labeled, with no quotient by cube automorphisms. Dimension \(d\) is an integer and the bound is asserted only for \(d\ge5\).

## Proof
**Finite counts.** For each of \(d=2,3,4,5\), enumerate perfect matchings recursively as follows: select the least unmatched vertex, pair it in turn with every currently unmatched Hamming neighbor, and recurse on the remaining vertices. A matching has a unique edge at the selected vertex; therefore the recursion is exhaustive and counts each matching exactly once. Each coordinate square has exactly two possible opposite-edge pairs; testing those pairs counts its available flips, so zero is exactly the condition of being frozen.

An independent enumeration pairs the even-parity vertices, in reversed order, with distinct odd-parity neighbors, recording chosen edges in a binary mask. It tests the two occupied-pair masks of every coordinate square. This bipartite recursion is also exhaustive and unique, uses a different order and representation, and agrees exactly with the first on the complete number of perfect matchings and the entire flip-degree histogram at every tested dimension. It finds respectively \(0,0,8,120\) frozen matchings for \(d=2,3,4,5\); for \(d=2\) the two coverings are both flippable, while \(d=3\) has nine matchings, six with two flips and three with four. The \(d=4\) histogram is \(\{0:8,3:32,4:12,5:96,6:48,8:72,12:4\}\), yielding 768 undirected flip edges by the handshake identity. Constructing every flip-neighbor matching and performing a complete graph traversal yields one component of size 264 and eight components of size one. The \(d=5\) histogram is regenerated in the verifier, and both enumerations agree on 120 zero-flip matchings out of 589185.

**Explicit frozen base and disjointness.** Encode vertices of \(Q_4\) by integers from zero through fifteen in binary. Four frozen matchings are specified by their partner arrays in order of vertex label:

```text
A: 1,0,6,11,12,7,2,5,10,13,8,3,4,9,15,14
B: 2,9,0,7,5,4,14,3,12,1,11,10,8,15,6,13
C: 4,3,10,1,0,13,7,6,9,8,2,15,14,5,12,11
D: 8,5,3,2,6,1,4,15,0,11,14,9,13,12,10,7
```

For each listed array, the map is an involution without fixed points; every pair differs in one binary coordinate. Directly check the 24 coordinate squares: none has both opposite edges occupied. Moreover these four matchings are pairwise edge-disjoint (for each vertex, the four listed partners are distinct). All those finite checks are repeated by the standalone verifier.

**All dimensions.** Fix \(d\ge5\) and decompose \(Q_d=Q_4\mathbin\square Q_{d-4}\). A layer indexed by \(z\in\{0,1\}^{d-4}\) is a copy of \(Q_4\). In every even-Hamming-parity layer place \(A\). In every odd-Hamming-parity layer independently choose one of \(B,C,D\). Use no edges connecting distinct layers. These choices constitute perfect matchings. A coordinate square lying inside one layer cannot flip, since each of \(A,B,C,D\) is frozen. A square involving one base direction and one layer direction has no alternating dimer pair, since adjacent layers have edge-disjoint base matchings. A square involving two layer directions has no dimers, so also cannot flip. Every resulting matching is frozen. There are \(2^{d-5}\) odd-parity layers and each admits three independent choices. The number of configurations with the fixed even-layer choice is \(3^{2^{d-5}}\). Finally repeat the construction with each of the eight distinct frozen \(Q_4\) matchings in all even layers, using three disjoint frozen choices for adjacent odd layers. The eight frozen base matchings have edge-disjointness graph consisting of two copies of \(K_4\), as verified exhaustively, so each has exactly three choices. Different even-layer choices give disjoint configuration families. This proves \(F_d\ge8\,3^{2^{d-5}}\).

## Verification
The self-contained Python 3 file `verify_cube_plaquette.py` enumerates matching states by two distinct recursions, independently calculates the coordinate-square degree histograms, builds and traverses the entire 272-state flip graph, and checks the four explicit mutually disjoint frozen witnesses as well as all eight possible frozen bases. Running `python3 verify_cube_plaquette.py` finishes with `VERIFY_OK`. It uses only the Python standard library. A finite enumeration is used only for the explicit small dimensions and the four-dimensional construction witnesses; the statement for arbitrary dimensions is proved algebraically by the layering argument, not by extrapolation.

## Relationship to prior work
The square-plaquette quantum dimer model and its kinetic flip operator are established; see Syljuåsen's planar model (2005). Hartarsky, Lichev and Toninelli (arXiv:2304.10930, especially Section 1.3, Theorems 5–6) directly study the same hypercube dimer configuration space but allow alternating cycles of length increasing with the dimension when proving connectivity. They also recognize nonergodicity under short cycle updates and discuss related obstructions. Thus the general mere existence of nonergodic dynamics is **not** claimed as new. Their stated results do not determine the square-only \(Q_4\) component spectrum, the \(Q_5\) frozen count, or the quantitative square-only family constructed here; permitting longer cycles changes the adjacency relation.

Fink's hypercube matching connectivity result uses replacements whose symmetric difference is a Hamiltonian cycle, not a square flip. Existing tables of perfect-matching totals do not determine which matchings are frozen or their square-flip connected components. The present exact small-scale classification and quantitative local-move fragmentation supply information distinct from those prior statements.

## Limitations
No formula for the exact frozen count at arbitrary dimension is proved; the bound may be far from sharp. The result concerns isolated states of the four-cycle-only flip graph and does not assert isolation when six- or longer alternating cycles are allowed. The connected-component structure in dimension five beyond its isolated vertices is not determined. A comprehensive priority search cannot rule out an unindexed equivalent enumeration, and there has been no independent scientific audit.

## References
1. O. F. Syljuåsen, “The plaquette phase of the square lattice quantum dimer model,” first public arXiv posting 22 December 2005, arXiv:cond-mat/0512579, https://arxiv.org/abs/cond-mat/0512579.
2. I. Hartarsky, L. Lichev and F. L. Toninelli, “Local dimer dynamics in higher dimensions,” arXiv:2304.10930, https://arxiv.org/abs/2304.10930; journal DOI:10.4171/AIHPD/200.
3. J. Fink, “Connectivity of Matching Graph of Hypercube,” https://ktiml.mff.cuni.cz/~fink/publication/kreweras2.pdf.
4. OEIS A005271, counts of perfect matchings in hypercubes, https://oeis.org/A005271.
