# The eight shattering profiles of perfect-matching-deleted four-cubes

## Finding

Let \(Q_4\) have vertex set \(\mathbb F_2^4\), with edges joining words at Hamming distance one. For each perfect matching \(M\) of \(Q_4\), delete its eight edges to obtain \(G_M=Q_4\setminus M\). Let \(\mathcal C_M\) be the family of all *inclusion-maximal*, not necessarily maximum-cardinality, independent sets of \(G_M\). A vertex support \(S\subseteq V(G_M)\) is shattered if \(\{I\cap S:I\in\mathcal C_M\}=2^S\). Write \(\Phi_M(z)=\sum_{S\text{ shattered}}z^{|S|}\).

**Finite classification.** The 272 perfect matchings fall into eight orbits under the 384 automorphisms of \(Q_4\). In the canonical lexicographic orbit order defined below, every \(\Phi_M\) begins with \(1+16z+96z^2\), has degree at most five, and its remaining coefficients are as follows. The table also gives the numbers of inclusion-maximal *shattered supports* (facets) of sizes three, four, five. The complete representatives, including all eight matching edges, appear in `orbit_data.json`.

| Class | Number of matchings | Coefficients \((a_3,a_4,a_5)\) | Facets \((f_3,f_4,f_5)\) |
|:---:|---:|:---:|:---:|
| 1 | 4 | (256,256,0) | (0,256,0) |
| 2 | 48 | (240,168,0) | (24,168,0) |
| 3 | 24 | (224,88,0) | (64,88,0) |
| 4 | 48 | (232,120,0) | (24,120,0) |
| 5 | 96 | (240,169,0) | (16,169,0) |
| 6 | 12 | (256,256,0) | (0,256,0) |
| 7 | 32 | (248,209,36) | (12,77,36) |
| 8 | 8 | (272,296,48) | (0,128,48) |

Exactly 40 of the 272 deletions have \(\operatorname{VCdim}(\mathcal C_M)=5\) (classes 7 and 8); the remaining 232 have dimension four. Exactly 16 yield a pure shattered-support complex (classes 1 and 6), and all others yield nonpure complexes. Class 8 is the Möbius–Kantor graph, isomorphic to \(GP(8,3)\), and has
\[
\Phi_M(z)=1+16z+96z^2+272z^3+296z^4+48z^5.
\]
The eight orbit classes are also distinct as unlabeled graphs: their maximal-independent-set cardinality distributions, shown in `orbit_data.json`, are pairwise distinct.

## Assumptions and scope

All graphs are finite, simple and undirected. Coordinates \(u\in\{0,\ldots,15\}\) encode vectors in \(\mathbb F_2^4\), and the neighbors of \(u\) in \(Q_4\) are \(u\oplus2^j\), for \(j=0,1,2,3\). Perfect matchings contain eight pairwise disjoint cube edges covering all sixteen vertices. For counting orbits, edge pairs and their lists are sorted lexicographically; repeatedly select the least unassigned perfect matching as the orbit representative. All group actions are \(u\mapsto t\oplus P(u)\), for a translation \(t\in\mathbb F_2^4\) and a permutation \(P\) of the four coordinates. The power \(2^S\) means the collection of all subsets of \(S\).

The classification is of Boolean shattering by **maximal independent sets** after *one entire perfect matching is deleted*. It does not concern maximum independent sets, the ordinary independence complex, edge-membership shattering of matchings, or arbitrary edge deletions.

## Proof

**Step 1: a complete matching and group certificate.** Every perfect matching can be produced once by choosing the smallest as-yet-uncovered vertex and pairing it with one of its uncovered cube neighbors; recursive calls cover the remaining vertices. This exhaustive recursion returns 272 distinct matchings. An automorphism of \(Q_4\) is uniquely specified by the image of the zero vertex (16 choices) and a permutation of its four neighbors (24 choices), giving precisely 384 actions. Acting on each currently least unused matching enumerates its full orbit. Exhaustive orbit partitioning gives the eight disjoint class sizes in the table, whose sum is 272. Both verification programs independently reconstruct the partition.

**Step 2: exactly enumerate the hypothesis family.** A vertex subset \(I\) is an inclusion-maximal independent set if and only if (i) no retained edge has both ends in \(I\), and (ii) every vertex outside \(I\) has a retained neighbor inside \(I\). The Python certificate checks these two quantified predicates on every one of the \(2^{16}\) possible \(I\). Independently, the C++ certificate enumerates maximal cliques of the graph complementary to \(G_M\) by a Bron–Kerbosch search; these are exactly the required sets. Their independently obtained size distributions agree. In particular, in every class there are fewer than 128 hypotheses.

**Step 3: test every possible support.** For each representative matching \(M\) and every of the \(2^{16}\) subsets \(S\) of vertices, form the distinct intersections \(I\cap S\), for all \(I\in\mathcal C_M\). The support is shattered precisely when their number equals \(2^{|S|}\). The code skips only supports for which shattering is logically impossible: a support containing a retained edge (the all-positive trace is impossible), and a support with at least seven vertices (there are fewer than 128 concepts). The separate implementations represent traces as bitmask sets and as compact bit-position signatures, respectively. Their exact complete enumerations yield the face coefficient vectors in the table.

**Step 4: facets, purity, and dimensions.** Shattered supports form a downward-closed complex: if \(S\) is shattered, every subset of \(S\) is shattered. Thus a face is inclusion-maximal if and only if no extension by one omitted vertex is shattered. Exhaustively testing each such extension gives the facet coefficient vectors. The largest nonzero face degree gives the VC dimension. A finite complex is pure exactly when all its facets have equal size; applying this test gives the stated 16 pure matching deletions. Orbit invariance upgrades the eight representative computations to all 272 matchings.

**Step 5: canonical graph identification.** For the eighth representative, `verify_q4_matching.cpp` implements a fixed bijection between the sixteen cube-word vertices and the standard \(GP(8,3)\) outer and inner vertices, then checks equality of *all* retained edges with the standard generalized Petersen edge set. Thus the Möbius–Kantor example is explicitly included. The eight inequivalent maximal-independent-set cardinality distributions provide a graph-isomorphism invariant separating all eight classes.

The listed code and JSON data are finite, complete proof certificates for this bounded assertion. No assertion about general \(Q_d\) for \(d>4\) follows.

## Verification

Run `python3 check_matching_profiles.py` (Python 3 standard library only). Separately compile `verify_q4_matching.cpp` with `g++ -std=c++17 -O2 verify_q4_matching.cpp -o verify` and execute `./verify`. Each program deterministically regenerates the 272 matching sets, the 384 automorphisms, all eight representative shattering polynomials and facets, and checks the counts \(40\) and \(16\). The programs use distinct methods to generate maximal independent sets and distinct trace encodings. They terminate with `PYTHON_Q4_MATCHING_SHATTER_PASS` and `Q4_MATCHING_SHATTER_PASS`, respectively. `orbit_data.json` contains the explicit representatives, maximal-independent-set size distributions, and all coefficient counts. A successful run uses no stochastic sampling.

## Relationship to prior work

The independent-domination polynomial counts inclusion-maximal independent sets by cardinality; this standard distinction and terminology are described by Jahari and Alikhani (2018). Counts of the 272 four-cube perfect matchings and their eight automorphism orbits occur in prior work on *anti-forcing* and are **not claimed to be new** here. A research-index synopsis of that work was inspected, but its linked full text could not be retrieved; it studies forcing and anti-forcing invariants. The mathematical contribution here is the exact coefficientwise *Boolean vertex-support shattering* classification, its facet-size breakdown, and the resulting 40/16 VC-dimension/purity dichotomy, not the known matching orbit count.

Neighborhood VC dimension (Coudert et al., 2024) uses a different concept class, namely graph neighborhoods, and does not imply maximal-independent-set membership shattering. Hypercube inducibility (Goldwasser and Hansen, 2023) studies subgraph patterns rather than the exact traces of these concept families. The known exact shattering polynomial for the intact four-cube concerns the different graph \(Q_4\), and neither its value nor an elementary monotonicity principle determines what happens when different perfect matchings are deleted.

## Limitations

This is an exact finite enumeration for dimension four only, with independent executable cross-checks but no independently commissioned mathematical audit. It is not a theorem for all hypercube dimensions. The eight orbit counts were already published; priority of the shattering coefficient and facet table is only claimed relative to inspected evidence, not guaranteed against unindexed earlier calculations. The available synopsis of the closest anti-forcing record did not permit a complete full-text comparison, which remains a documented priority risk. The Python and C++ verification paths both apply exhaustive finite operations; they do not establish a symbolic dimension-independent structural explanation.

## References

1. S. Jahari and S. Alikhani, *On the independent domination polynomial of a graph*, arXiv:1808.07369, first publicly posted 2018-08-21, https://arxiv.org/abs/1808.07369 . Full arXiv HTML manuscript inspected: https://arxiv.org/html/1808.07369v3 .
2. Coudert, Csikós, Ducoffe and Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588, first posted 2024-05-13, https://arxiv.org/abs/2405.07588 .
3. Goldwasser and Hansen, *Inducibility in the hypercube*, 2023, DOI:10.1002/jgt.23053, https://onlinelibrary.wiley.com/doi/10.1002/jgt.23053 .
4. *First gapped anti-forcing spectrum in the hypercube sequence*, published research record dated 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-first-gapped-anti-forcing-spectrum-in-the-hypercube-sequence--5cd5b9de4a8b . Its indexed synopsis was compared, but full text was inaccessible; it gives the known 272 perfect matchings and their eight symmetry orbits.
