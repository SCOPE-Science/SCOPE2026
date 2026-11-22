# Exact static and adaptive shattering of minimum dominating sets in the Desargues graph

## Finding

Let \(G\) be the twenty-vertex Desargues graph. Let \(\mathcal D\) consist of the characteristic functions of all *minimum-cardinality ordinary dominating sets* of \(G\), with vertex-membership queries. Then \(\gamma(G)=6\), there are exactly \(130\) such sets, and the complete shattered-support polynomial is
\[
\Phi_{\mathcal D}(z)=1+20z+190z^2+560z^3+360z^4.
\]
Consequently \(\operatorname{VCdim}(\mathcal D)=4\), whereas \(\operatorname{Ldim}(\mathcal D)=6\). The shattered-support complex has \(30\) maximal faces of size two, \(80\) of size three, and \(360\) of size four, so it is nonpure. Its only nonzero reduced Betti numbers over \(\mathbb F_2\) are
\[
\widetilde\beta_1=30,\qquad \widetilde\beta_2=119,\qquad \widetilde\beta_3=60.
\]
This provides a strict two-query separation of static from adaptive learning and a three-degree homology signature for a natural finite domination concept class.

## Assumptions and scope

The twenty vertices are all subsets of \(\{0,1,2,3,4\}\) having cardinality two or three, ordered by their five-bit integer encodings. Vertices \(A\) and \(B\) are adjacent if and only if \(A\subset B\) or \(B\subset A\). The equivalent generalized Petersen graph \(GP(10,3)\) has outer edges between consecutive indices, inner edges of step three, and spokes between corresponding indices. The file `vertex_isomorphism.json` explicitly matches these descriptions.

A set \(S\) dominates if each vertex lies in \(S\) or has a neighbor in \(S\). The concepts are the *minimum* such sets, not all dominating sets, inclusion-minimal sets, total dominating sets, or the graph's separate dominance complex. A vertex support \(Q\) is shattered if for every \(T\subseteq Q\) some \(S\in\mathcal D\) satisfies \(S\cap Q=T\). Littlestone dimension is the maximum full binary adaptive-query tree depth with a concept realizing each root-to-leaf label path.

## Proof

All claims are finite exact statements proved by the complete integer-mask enumeration algorithms in the accompanying standalone Python and C++17 sources. They are checkable by executing the complete loops, without sampling, statistical inference, or dependence on the resulting log text. The proof has the following independently verifiable steps.

First construct the closed-neighborhood bit mask \(N[v]\) for each of the twenty vertices. For each \(k=0,1,\ldots,6\) and *every* size-\(k\) mask \(s\), compute the bitwise union of \(N[v]\) over the selected vertices. The first cardinality attaining the complete twenty-bit mask is exactly six, with precisely 130 satisfying masks. This exhausts every smaller-cardinality possibility and establishes both \(\gamma(G)=6\) and the exact concept family.

Next, for each integer \(k=0,1,2,3,4,5\) enumerate every \(k\)-vertex support. For each concept compute the \(k\)-bit restriction trace and count distinct traces; shattering occurs exactly when all \(2^k\) traces appear. The resulting support counts are \((1,20,190,560,360,0)\). Because shattering is hereditary, the zero coefficient at size five excludes every larger shattered support. A support is an inclusion-maximal face exactly when adjoining no omitted vertex remains shattered. Testing this condition on every shattered support gives the maximal-face counts \(30,80,360\) at sizes two, three, four.

For homology, construct the augmented simplicial chain complex over \(\mathbb F_2\) on these exact faces, with a unique empty face. The ranks of the boundary maps in dimensions one through four are exactly \((1,19,141,300)\), obtained by full binary Gaussian elimination on all boundary columns. The face dimensions and consecutive boundary ranks give reduced Betti ranks \(0,30,119,60\) in degrees zero through three, and all remaining reduced Betti ranks vanish by the absence of higher faces.

For adaptive lower bound, `depth6_tree.json` records every internal query and one concept index at each of its 64 leaves. `replay_certificates.py` independently reconstructs the full 130-concept list and checks all six query-answer constraints along every path, uniqueness of the 64 witnesses, and validity of the explicit graph-model isomorphism. Therefore \(\operatorname{Ldim}(\mathcal D)\ge6\). For upper bound, all twenty vertices occur in exactly 39 of the 130 minimum dominating sets, checked by exhaustive integer-mask enumeration in both models. A full depth-seven tree would, at its first query, require at least \(2^6=64\) distinct concepts in its positive child, which has only 39. Therefore \(\operatorname{Ldim}(\mathcal D)\le6\).

## Verification

The self-contained source files are `verify_middle_levels.py`, `verify_gp103.cpp`, and `replay_certificates.py`. The explicit witnesses are in `depth6_tree.json`, and the vertex relabeling in `vertex_isomorphism.json`. Run from the folder containing the extracted package:

```sh
python3 verify_middle_levels.py /tmp/desargues-generated-tree.json
c++ -O2 -std=c++17 verify_gp103.cpp -o /tmp/desargues-gp-check
/tmp/desargues-gp-check
python3 replay_certificates.py .
```

The first program independently regenerates a depth-six tree and verifies the enumerated faces, facets, and boundary ranks; the second uses a distinct generalized Petersen adjacency model and integer enumeration; the third replays the shipped certificates, not a regenerated tree. The expected numerical invariants are given in the finding, and both checkers print their own outputs. The exact finite loops, rather than pre-recorded outputs, are the certificates of exhaustive computation.

## Relationship to prior work

VinuPriya, Mageswari and Ameenal Bibi (2019), Theorem 3.15, describe the ordinary domination number six and study total and inverse total domination of the Desargues graph. The domination number itself is not claimed as novel. Knor, Škrekovski and Tepeh (first arXiv version, 26 October 2020) prove global domination-versus-independent-domination inequalities for regular graphs, but not the exact optimal-set concept family. Adler, Benediktsson and Macpherson (manuscript deposited 29 September 2021) analyze open-neighborhood VC dimensions for Johnson and Hamming graphs; a neighborhood hypothesis is distinct from the indicator of a minimum dominating set.

Published Desargues dominance-complex and matching-complex computations concern different simplicial complexes from the present *shattered-support complex*. Published minimum-dominating-set learning results on paths and the Heawood graph concern other graphs or concept families. Searches for the Desargues and generalized Petersen names, exact 130-set count, adaptive dimension, shattering polynomial and homology yielded no examined result implying the entire claim. This is qualified evidence of originality, not a proof of historical uniqueness.

## Limitations

The result concerns exactly this twenty-vertex graph and its ordinary minimum dominating sets; it does not assert a theorem for generalized Petersen graphs at other parameters. The homology computation is over \(\mathbb F_2\) only; integral homology and homotopy type are not established. Exhaustive computation is possible because the graph is finite, and both independent implementations assume ordinary fixed-precision integer arithmetic with twenty-bit masks. An unindexed exact table or earlier equivalent description could affect historical priority. The 2019 journal issue provides only a March–May issue window, not a verified exact day; the documented first *day-verified* source date for scope selection is the 26 October 2020 arXiv posting, without claiming it predates that issue.

## References

1. G. VinuPriya, M. Mageswari and K. Ameenal Bibi, *Total Domination and Inverse Total Domination Number of Some Special Classes of Graphs*, AIJRSTEM 26(1) (March–May 2019), pp. 47–57, especially Theorem 3.15. https://www.academia.edu/39262725/Total_Domination_and_Inverse_Total_Domination_Number_of_Some_Special_Classes_of_Graphs
2. M. Knor, R. Škrekovski and A. Tepeh, *Domination versus independent domination in regular graphs*, arXiv:2010.13467, first public version 26 October 2020. https://arxiv.org/abs/2010.13467
3. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, accepted-manuscript repository deposit 29 September 2021. https://eprints.whiterose.ac.uk/id/eprint/178584/
4. Relevant independent published Desargues dominance-complex record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-thirteen-nine-spheres-and-a-cyclic-homology-character-for-the-de--49798a534d1d (distinct concept and chain complex).
