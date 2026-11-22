# Sharp ternary short-block synchronization and single-substitution correction through length six

## Finding
Let \(\Sigma=\{0,1,2\}\), and, for positive integers \(n\), let \(M_n\) be the largest cardinality of a fixed-length code \(C\subseteq\Sigma^n\) that is **non-overlapping** and has minimum Hamming distance at least three. Non-overlapping means that no nonempty proper prefix of any word in \(C\) equals the same-length suffix of any word in \(C\), **including the word itself**. Then the exact capacity and labeled optimizer counts for \(2\le n\le6\) are

| Length \(n\) | Maximum \(M_n\) | Number of labeled maximum codebooks |
|---:|---:|---:|
| 2 | 1 | 6 |
| 3 | 1 | 18 |
| 4 | 2 | 108 |
| 5 | 4 | 300 |
| 6 | 8 | 528 |

At length five, every maximum four-word code is *equidistant*: all six pairwise Hamming distances equal three. Its 300 maxima form 29 classes under simultaneous permutations of the three symbols and global word reversal: 21 classes of size 12 and eight of size six. At length six, the 528 maximum eight-word codebooks form exactly 49 classes under the same group: 39 of size 12 and ten of size six. The tables `OPTIMA_5.tsv`, `OPTIMA_6.tsv`, `ORBIT_REPRESENTATIVES_5.tsv` and `ORBIT_REPRESENTATIVES_6.tsv` contain every labeled equality case and one representative per symmetry class.

Since \(M_1=1\) trivially, length six is the **shortest ternary blocklength capable of carrying eight distinct messages (three bits)** while meeting both requirements. This concerns correction of one substituted symbol *once the block boundary is known*; it does not assert that a corrupted streaming frame can itself be located without ambiguity.

## Assumptions and scope
The alphabet is exactly the labeled three-element set \(\Sigma\). Word length is uniform within each codebook, and exactly one or zero substitutions are allowed within an aligned block; the received word can be any element of \(\Sigma^n\). Two radius-one Hamming balls are disjoint exactly when the centers have Hamming distance at least three. Frame synchronization here is the uncorrupted cross-bifix-free property, with all proper overlap lengths from one through \(n-1\) excluded in both orientations, including self-overlap. Codes are unordered sets, and counting is on a fixed labeled alphabet. Only global alphabet relabelings and whole-word reversal, not arbitrary coordinate permutations, define the reported equivalence.

## Proof
**Exact finite reduction.** For each \(n\in\{2,3,4,5,6\}\), enumerate the entire set \(V_n\) of \(3^n\) ternary words and discard a word \(w\) if \(w_1\ldots w_k=w_{n-k+1}\ldots w_n\) for some \(1\le k<n\). Let \(U_n\) be the surviving words. On \(U_n\), make a simple undirected compatibility graph, connecting \(u\ne v\) if \(d_H(u,v)\ge3\) and for every \(1\le k<n\) neither the \(k\)-prefix of \(u\) equals the \(k\)-suffix of \(v\) nor the \(k\)-prefix of \(v\) equals the \(k\)-suffix of \(u\). Every admissible code is exactly a clique of this graph: the single-word tests are exhaustive for self-overlaps and the pair tests are precisely the remaining hypotheses. This is an equivalence, not a relaxation.

The exact graph sizes, edge counts and maximum-clique sizes are:

| \(n\) | \(|U_n|\) | Edges | Maximum clique |
|---:|---:|---:|---:|
| 2 | 6 | 0 | 1 |
| 3 | 18 | 0 | 1 |
| 4 | 48 | 108 | 2 |
| 5 | 144 | 2,070 | 4 |
| 6 | 414 | 24,156 | 8 |

The complete **maximal**-clique size census, computed without search cutoffs, is \(\{2:48,3:1752,4:300\}\) at length five and \(\{3:48,4:4752,5:289464,6:507546,7:56568,8:528\}\) at length six. At the shorter lengths all maximal cliques have size one (respectively six and eighteen of them) or size two (108 at length four). Thus no clique of size five or more exists at length five, and no clique of size nine or more exists at length six. The listed 300 and 528 maximum cliques attain the upper bounds.

**Exhaustiveness argument.** The standalone `verify.py` implements a deterministic Bron–Kerbosch recursion on integer bitsets. At every call, \(R\) is a clique, \(P\) consists of vertices able to extend \(R\), and \(X\) consists of already explored such vertices. A maximal clique is recorded iff both \(P\) and \(X\) are empty. Recursion selects a pivot from \(P\cup X\), explores every vertex in \(P\setminus N(\text{pivot})\), and then moves that vertex from \(P\) to \(X\). The standard clique-recursion invariant ensures every maximal clique is enumerated once and none is omitted; a larger clique would necessarily appear among the maximal ones. The distinct C++17 implementation `alternate.cpp` instead visits every clique in increasing lexical vertex order and checks that the count in the top layer agrees and the next layer is empty. Its edge predicate and enumeration order are independently implemented.

**Code witnesses and equality classification.** The lexicographically first six-symbol row in `OPTIMA_6.tsv` is the explicit eight-codeword witness

`000001, 002111, 020121, 021011, 201101, 202221, 220211, 222001`.

The corresponding first five-symbol row in `OPTIMA_5.tsv` is

`00001, 00212, 02022, 02111`.

Both rows pass all overlap and Hamming tests. The finite clique census produces exactly all equality cases in the two complete tables. For each maximum code, apply all \(3!\) alphabet permutations and both reversal choices; the resulting 12 transformations preserve each defining property. Partitioning the actual maximum-code tables by their orbits gives the stated 29 and 49 classes. At length five the checker also tests each of the six Hamming distances of all 300 maximum codes, establishing the uniform distance-three assertion.

## Verification
From the directory containing the six data and source artifacts run `python3 verify.py`, requiring Python 3.9 or later and only its standard library. Separately run `g++ -std=c++17 -O2 alternate.cpp -o alternate && ./alternate`. Both must complete with `VERIFY_OK` and `ALTERNATE_OK`, respectively. The Python program checks all four TSV certificate tables, clique counts, orbit counts and distance-three rigidity. The C++ program regenerates all admissible words and compatibility edges, recursively visits all cliques without a fixed target size, and verifies every maximum and its labeled multiplicity. Tests were executed on the embedded sources before delivery; source code and all data necessary to reproduce them are included.

## Relationship to prior work
Chee, Kiah, Purkayastha and Wang (arXiv:1209.0236, first posted 2012-09-03) introduce general cross-bifix-free constructions and asymptotic bounds; their Theorem 1.1 and construction do not determine this joint Hamming-distance-three finite optimum. Blackburn (arXiv:1303.1026, first posted 2013-03-05) gives general non-overlap bounds and exact unrestricted results only through length three, not the imposed distance condition. The published complete ternary length-five non-overlapping census establishes 17 codewords *without* error correction, and a published ternary length-five non-overlapping **one-substitution-detecting** result establishes nine words at minimum distance two. Neither implies the eight-word six-symbol correction optimum or the length-five distance-three optimizer census. Wang, Fang and Feng, *q-ary (1,k)-overlap-free codes with given restrictions* (2025), investigate Hamming-distance-constrained partial overlap and provide general bounds; its accessible article preview did not exhibit this particular exact enumeration. That latter comparison is incomplete, so prior coverage in inaccessible text remains a risk.

## Limitations
The completeness proof is exhaustive only through length six. It does not give a closed form at larger lengths, an asymptotic result, or guarantees for block-boundary recovery after a symbol error. The known general coding bounds and restricted-overlap literature could conceal another earlier derivation not present in the accessible material; the numerical novelty is qualified accordingly. The exact certificate is a transparent finite enumeration, not a symbolic proof independent of computation.

## References
1. Y. M. Chee, H. M. Kiah, P. Purkayastha and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, submitted 2012-09-03. https://arxiv.org/abs/1209.0236.
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, submitted 2013-03-05; IEEE Transactions on Information Theory 61 (2015), 4890–4894. https://arxiv.org/abs/1303.1026.
3. *Exact size and enumeration of maximum length-five non-overlapping codes*, public research record, 2026-09-20, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-length-five-non-overlapping-code-optima--e8e2fd1a9e7a.
4. *Exact ternary length-five non-overlapping codes detecting one substitution*, public research record, 2026-10-12, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-ternary-length-five-non-overlapping-codes-detecting-one-su--d72ce427d800.
5. X. Wang, Y. Fang and T. Feng, *q-ary (1,k)-overlap-free codes with given restrictions*, Discrete Mathematics 348 (2025), 114236, DOI:10.1016/j.disc.2024.114236.
