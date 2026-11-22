# Exact directional fragmentation of quantum dimers on the four-cube

## Finding
Let \(Q_4\) be the labelled binary four-cube, and let \(S\subseteq\binom{\{1,2,3,4\}}2\) specify which **coordinate-plane orientations** of alternating-square dimer flips are permitted. Every perfect matching is a state; a move replaces the two occupied opposite edges of a coordinate square by its other opposite-edge pair, but only for a square whose two varying coordinates constitute a pair in \(S\). There are exactly 272 matching states and 64 orientation repertoires. **Their complete connected-component spectra are determined by the eleven rows below.**

Define the *orientation graph* \(G_S\) on vertices \(\{1,2,3,4\}\), with edges \(S\). In the table \(d(G_S)\) is its decreasing degree sequence, \(m\) is the number of labelled sets \(S\) in the row, and \(a^b\) denotes **exactly \(b\) components of size \(a\)**, not exponentiation of a state count. All entries count labelled dimers without quotienting by symmetry.

| \(d(G_S)\) | \(m\) | Component sizes (size: multiplicity) |
|---|---:|---|
| \((0,0,0,0)\) | 1 | 1:272 |
| \((1,1,0,0)\) | 6 | 16:1, 4:20, 2:16, 1:144 |
| \((1,1,1,1)\) | 3 | 16:2, 4:40, 2:32, 1:16 |
| \((2,1,1,0)\) | 12 | 49:1, 9:4, 7:4, 4:12, 2:16, 1:79 |
| \((2,2,2,0)\) | 4 | 81:1, 9:12, 4:6, 1:59 |
| \((2,2,1,1)\) | 12 | 82:1, 12:8, 4:12, 2:16, 1:14 |
| \((3,1,1,1)\) | 4 | 108:1, 7:12, 2:24, 1:32 |
| \((2,2,2,2)\) | 3 | 132:1, 32:4, 1:12 |
| \((3,2,2,1)\) | 12 | 140:1, 12:8, 4:2, 2:8, 1:12 |
| \((3,3,2,2)\) | 6 | 198:1, 32:2, 1:10 |
| \((3,3,3,3)\) | 1 | 264:1, 1:8 |

In particular, the fully enabled six-orientation system has the previously known 264-state mobile component and eight frozen states. **Every one of the six orientations is indispensable to the connectivity of that 264-state set.** Turning off *any one* orientation splits its former mobile component into components of sizes \(198,32,32,1,1\), while the eight previously frozen states remain isolated. Exactly ten states are frozen and the whole matching space has thirteen components when exactly five orientations are enabled. The eleven spectra distinguish every isomorphism class of the orientation graph.

For a Rokhsar–Kivelson-type positive plaquette Hamiltonian \(H_S=\sum_{p\text{ enabled}}t_p(|M_p\rangle-|M'_p\rangle)(\langle M_p|-\langle M'_p|)\), where \(t_p>0\) and \(M_p,M'_p\) range over the two matchings paired by each available plaquette flip in each background, the exact zero-energy ground-space degeneracy is the **number of components** in the corresponding table row. The weights need not be equal. This is a direct corollary, not an assertion about excited-state gaps.

## Assumptions and scope
The sixteen vertices of \(Q_4\) are the binary words \(\{0,1\}^4\); edges connect words of Hamming distance one. A perfect matching chooses eight edges, touching every vertex once. For \(i<j\), a coordinate square varies bits \(i,j\) and fixes the two remaining bits, so each of the six coordinate pairs has exactly four squares. A square flip is legal only when one complete opposite-edge pair of that square is present. For a selected set \(S\), all four squares for each pair in \(S\) are enabled, while none for pairs outside \(S\) is enabled. The notion of a *component* refers to this undirected, unweighted matching flip graph. Its connectivity is unchanged if individual enabled flips have arbitrary strictly positive rates. Zero rates mean the corresponding moves are removed. No switches on six-cycles or other longer cycles are considered.

## Proof
**Exhaustion of matchings.** Encode vertices by four-bit integers and edges by their two endpoints. Choose the least unmatched vertex, pair it in turn with each still-unmatched Hamming neighbor, and recurse. Every perfect matching has a unique partner for the selected vertex, hence this is an exhaustive recursion without duplicates. It yields exactly 272 distinct eight-edge masks.

**Exhaustion of plaquettes and flips.** For every coordinate pair \(\{i,j\}\), choose one of the four assignments of the other two bits. Its four vertices define two opposite-edge pairs. A matching containing one pair and no edge of the other pair has exactly one possible flip at that face, obtained by symmetric difference with the four face edges. There are 24 square faces total. Comparing each of the 272 matching masks against each of the 24 faces constructs all legal directed moves and their coordinate-plane types. The full undirected flip graph has 768 edges, in agreement with the published isotropic census.

**Complete component classification.** For each of the \(2^6=64\) subsets of the six coordinate pairs, retain only the directed moves of the allowed types and run a complete graph traversal from every as-yet-unvisited state. The resulting multiset of component cardinalities is the table. This is a proof by finite exhaustive computation: the two preceding arguments show that the state list and transitions are complete, not samples. A second complete perfect-matching enumeration assigns all eight even-parity vertices to distinct neighboring odd-parity vertices, in reverse order, and recomputes every face transition by explicit edge-set replacement. A separate disjoint-set union computation independently reproduces the component spectra for all 64 subsets. Both exact programs are contained in `verify_directional_plaquettes.py` and must agree at every subset; its recorded assertions also independently check each of the eleven spectra and their multiplicities.

**Symmetry reduction.** Permutations of the four coordinate labels act on the matching-flip graph and permute the six face types. Consequently, the component multiset depends only on the isomorphism class of \(G_S\). There are eleven unlabeled simple graphs on four vertices, with the eleven distinct sorted degree sequences shown in the table. The complete 64-subset verification gives the listed number \(m\) of labelled representatives in each class. Summing those multiplicities yields 64. The particular five-orientation assertion follows from the six masks missing one coordinate pair. Their computed spectrum is \((198,32,32,1^{10})\); the eight original frozen states cannot gain edges when a type is removed, so exactly two additional mobile states become frozen, and the surviving mobile states occupy the three stated non-singleton components.

**Ground-space claim.** Each RK plaquette term is a nonnegative rank-one operator. Its quadratic form is \(t_p|\psi(M_p)-\psi(M'_p)|^2\). Since all included coefficients are strictly positive, zero energy holds exactly when the amplitude is constant along every allowed flip. Thus one arbitrary constant per connected component parametrizes the kernel, yielding the displayed ground-space degeneracy without additional spectral assumptions.

## Verification
Run `python3 verify_directional_plaquettes.py` with the Python 3 standard library. It prints `VERIFY_OK matchings=272 faces=24 labeled_repertoires=64 symmetry_types=11 all_full_6_only=TRUE` and the eleven table rows. It reconstructs all finite states and transitions rather than loading them from an external file; independent recursive matchings enumerators, explicit mask-based traversal, and explicit-edge-set disjoint-set union each verify the claimed counts. It also asserts that every one of the six five-orientation systems has non-singleton component sizes \((198,32,32)\) and ten singletons. All integer calculations are exact. `component_spectra.json` is a machine-readable copy of the eleven verified rows, not a prerequisite for running the program.

## Relationship to prior work
The quantum dimer and RK plaquette flip construction on square lattices is established in Syljuåsen (2005). Klivans and Saldanha (2020, Example 2.2) **already give** the 272 states, the 264-state mobile sector, and eight frozen states under all six types of square flips on the four-cube. Those isotropic quantities are explicitly credited, not claimed as new. Hartarsky, Lichev and Toninelli (2023, Sections 1.2–1.3) study the same hypercube perfect-matching configuration space and prove ergodicity if **longer** alternating cycles are also permitted. Previously published exact isotropic square-flip distance results likewise allow all six face orientations. None of these results gives the spectrum under removing coordinate-plane types, nor does isotropic connectivity imply which orientation subsets preserve it.

The new information is the **complete 64-repertoire anisotropic connectivity classification**, including the sharp six-type necessity and the 198–32–32 fragmentation upon removing a single orientation. It is a finite Hilbert-space fragmentation and zero-mode control result; it does not assert a new isotropic cube matching total or isotropic component census.

## Limitations
The classification is exact only for the labelled sixteen-vertex four-cube with the specified coordinate-plane-selective, four-cycle-only kinetic moves. It neither establishes analogous all-size results in dimensions five or more nor determines spectral gaps, dynamical mixing times, or perturbations introducing six-cycle moves. Within one fixed repertoire, strictly positive unequal plaquette rates leave the zero-mode multiplicity unchanged, but no claim is made about excited-state eigenvalues. Historical priority beyond the sources actually compared cannot be guaranteed; no independent scientific audit has been performed.

## References
1. O. F. Syljuåsen, “The plaquette phase of the square lattice quantum dimer model,” first public arXiv version 22 December 2005, arXiv:cond-mat/0512579, https://arxiv.org/abs/cond-mat/0512579.
2. C. Klivans and N. C. Saldanha, “Domino tilings and flips in dimensions 4 and higher,” first public arXiv version 16 July 2020, arXiv:2007.08474, Example 2.2, https://arxiv.org/abs/2007.08474.
3. I. Hartarsky, L. Lichev and F. L. Toninelli, “Local dimer dynamics in higher dimensions,” first public arXiv version 21 April 2023, arXiv:2304.10930, Sections 1.2–1.3 and Theorem 6, https://arxiv.org/abs/2304.10930.
4. “Frozen sectors and exact square-flip connectivity in hypercube quantum-dimer configurations,” published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-frozen-sectors-and-exact-square-flip-connectivity-in-hypercube-q--db180e339d90.
5. “Exact square-flip distances in the four-dimensional hypercube,” published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-square-flip-distances-in-the-four-dimensional-hypercube--84ee7ca2c7ef.
