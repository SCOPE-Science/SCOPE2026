# The first nonpure maximal-independent-set shattering complex in the Boolean-cube sequence

## Finding
Let \(Q_d\) be the graph on binary words of length \(d\), adjacent when they differ in exactly one coordinate, and let \(\mathcal M_d\) denote the family of all inclusion-maximal independent vertex sets. Its membership concept class has ground set \(V(Q_d)\), and each concept is one set \(M\in\mathcal M_d\). A support \(S\subseteq V(Q_d)\) is *shattered* when \(\{M\cap S:M\in\mathcal M_d\}=2^S\).

For the four-cube, the exact complete polynomial of shattered supports is
\[
\Phi_{Q_4}(z)=1+16z+88z^2+160z^3+104z^4.
\]
No support of five or more vertices is shattered. Thus \(\operatorname{VCdim}(\mathcal M_4)=4\). The complex of shattered supports is **nonpure**: its inclusion-maximal faces are exactly the eight antipodal vertex pairs and 104 four-vertex supports. The latter split into precisely three orbits of sizes 16, 24, and 64 under all 384 cubical automorphisms.

A particularly compact *necessary and sufficient* characterization is given by four orbit representatives. Write vertices as integers \(0,\ldots,15\) whose four-bit binary expansions are their coordinates. A support is shattered if and only if it is a subset of an image, under any composition of bit translations and coordinate permutations, of one of
\[
\{0,15\},\quad\{0,3,5,6\},\quad\{4,7,9,10\},\quad\{3,5,6,8\}.
\]
These four orbits have, respectively, 8, 16, 24, and 64 members. In particular, a three-vertex support is shattered exactly when all three pairwise Hamming distances belong to \(\{2,3\}\); an antipodal pair, although shattered, cannot extend to a shattered triple.

This is the first nonpure case in the sequence \(Q_1,Q_2,Q_3,Q_4\): the earlier shattering polynomials are \(1+2z\), \(1+4z\), and \(1+8z+16z^2\), with every maximal shattered support having its respective maximum dimension.

## Assumptions and scope
All sets are finite and labeled. Maximal means inclusion-maximal, not maximum-cardinality. The underlying \(Q_4\) has 16 labeled binary words and 32 graph edges; there are 42 distinct maximal independent sets, with size distribution 24 of size four, 16 of size five, and two of size eight. These 42-set counts are background, not a novelty claim. The polynomial counts *labeled query supports*, rather than concepts or concept cardinalities. The facet-orbit classification is for the full group \(\operatorname{Aut}(Q_4)\cong (\mathbb Z/2\mathbb Z)^4\rtimes S_4\).

## Proof
**(1) Exhaustion of concepts.** An independent set \(M\) is inclusion-maximal if and only if it dominates all vertices: every vertex \(v\) belongs to \(M\) or has a neighbor belonging to \(M\). This equivalence holds in every finite graph: otherwise an undominated vertex could be adjoined to \(M\). Represent \(M\) by a sixteen-bit word, test all \(2^{16}=65,536\) words against the 32 edges and the sixteen closed neighborhoods, and retain exactly the independent dominating ones. The complete loop is implemented in `verify_census.py`, with no external input. It yields 42 distinct concepts and the stated size distribution.

**(2) Exhaustion of Boolean traces.** For each of the same \(65,536\) candidate supports \(S\), compute the distinct restrictions \(M\mathbin{\cap}S\) over all 42 concepts. The support is shattered precisely when this collection contains \(2^{|S|}\) different bit masks. This is a finite exhaustive equivalence, not a statistical sample; every concept and support occurs in the loops. The resulting face counts in degrees zero through four are \((1,16,88,160,104)\), with no higher degrees. Directly testing whether a shattered support has a one-vertex shattered extension yields exactly eight facets of size two and 104 of size four. These eight pairs are precisely the antipodal pairs \(\{v,v\oplus15\}\), one for each complement pair of binary words. No maximal triples occur.

**(3) Independent orbit certificate.** For a separate computation, observe that maximal independent sets of \(Q_4\) are exactly the maximal cliques of its complementary graph. `verify_orbits.py` finds them by a Bron–Kerbosch maximal-clique search, which differs from the independent-dominating brute-force construction. The 384 cubical transformations are obtained by each of the 24 coordinate permutations followed by each of the 16 XOR translations. A cube automorphism sends zero to some vertex, and after translation fixes zero and must permute its four neighbors, so these are all automorphisms. The four representatives stated in the finding generate disjoint facet orbits with sizes \(8,16,24,64\). Their downward closure has degree counts \((1,16,88,160,104)\). The separate maximal-clique list is used to compute all actual Boolean traces for all \(65,536\) supports, and it matches the predicted downward closure *exactly*, not merely by equal coefficient counts. Thus the orbit characterization, nonpurity, and facet completeness follow. The same program checks the stated Hamming-distance criterion for every three-vertex support.

**(4) Boundary cases and consequence.** The direct census for \(d=1,2,3\) enumerates every possible vertex subset on two, four, and eight vertices and yields the polynomials given above and only maximum-dimensional facets. Since \(Q_4\) has both size-two and size-four maximal shattered faces, its shattering complex cannot be a matroid independence complex (all matroid bases have the same size). No statement is made about which larger cubes have nonpure complexes.

## Verification
Run from the directory containing the two supplied Python files: `python3 verify_census.py` and `python3 verify_orbits.py`. Both use only the Python standard library. The exact success markers are `Q4_MIS_SHATTER_CENSUS_PASS` and `Q4_MIS_SHATTER_ORBITS_PASS`. The first enumerates every concept by independent domination, every support, and every facet. The second independently constructs the concept class from maximal cliques and tests equality to an isometry-orbit downward closure for every support. The code is the complete finite certificate: a partial enumeration, sampled trace table, or unsigned log would not suffice.

## Relationship to prior work
Adler, Benediktsson, and Macpherson (2020) established VC bounds for *open neighborhoods* of Johnson and Hamming graphs, including binary Hamming cubes, rather than membership in the maximal independent sets. Kahn and Park (2019/2020) study asymptotic numbers of maximal independent sets in Hamming cubes, not the Boolean-query support complex. Ignatov (2023) studies maximal-independent-set size polynomials and formal concept lattices for cubes through dimension six; the abstract and code description establish overlap of objects but do not establish these specific Boolean trace or facet-orbit statements. Its complete chapter text was not accessible for inspection, so exact coverage remains a residual historical-priority risk. Liu, Shangguan, Skokan, and Xu (2024) explicitly construct a set system from maximal independent sets of any graph and prove general VC bounds via bipartite induced matchings (Lemma 2.20 in arXiv:2403.17910v3); those facts are acknowledged rather than claimed. They do not specify the four-cube's complete shattered-support complex. Separately, indexed results for maximal independent sets of *cycles*, *forests*, *threshold graphs*, and *whiskered graphs* concern other graph families and do not imply these orbit counts for unwhiskered \(Q_4\).

## Limitations
This is an exact finite classification, not an infinite-dimensional theorem. The independent verifiers are two implementations, not independent human certification. There is no asserted originality for the 42 hypotheses or their size distribution, for general VC facts, or for generic nonpure shattered complexes. The unavailable full chapter of Ignatov (2023), possible unpublished data tables, and unindexed equivalent reports remain priority risks. These calculations do not determine Littlestone dimension, homology of the shattered complex, or an all-dimensional cube formula.

## References
1. I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, first public arXiv v1, 31 July 2020. https://arxiv.org/abs/2007.16042
2. J. Kahn, J. Park, *The number of maximal independent sets in the Hamming cube*, arXiv:1909.04283 (2019). https://arxiv.org/abs/1909.04283
3. D. Ignatov, *On the Maximal Independence Polynomial of the Covering Graph of the Hypercube up to n=6*, International Conference on Formal Concept Analysis (2023), DOI:10.1007/978-3-031-35949-1_11. Full text not inspected.
4. H. Liu, C. Shangguan, J. Skokan, Z. Xu, *Beyond chromatic threshold via the (p,q)-theorem, and a sharp blow-up phenomenon*, arXiv:2403.17910 (2024), Section 2.2 and Lemma 2.20. https://arxiv.org/abs/2403.17910
5. OEIS A284707, earlier total counts of maximal independent sets in binary cubes. https://oeis.org/A284707
