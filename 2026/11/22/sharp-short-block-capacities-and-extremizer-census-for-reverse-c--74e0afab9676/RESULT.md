# Sharp short-block capacities and extremizer census for reverse-complement-closed binary non-overlapping codes

## Finding
For binary length-\(n\) words, write \(\rho(w)\) for reversal followed by complementation of each bit. Call a code **non-overlapping** if no nonempty proper prefix of any codeword equals an equally long suffix of any codeword, including the same word. Require **strand closure** \(\rho(C)=C\). Let \(M_n\) be its largest possible number of codewords and \(T_n\) the number of distinct labeled codebooks attaining that maximum, counting the empty codebook when no nonempty code exists.

**Theorem (complete initial census).** For every integer \(1\le n\le12\), these quantities are exactly:

| \(n\) | Maximum \(M_n\) | Optimizers \(T_n\) | Valid reverse-complement orbits |
| ---: | ---: | ---: | ---: |
| 1 | 2 | 1 | 1 |
| 2 | 1 | 2 | 2 |
| 3 | 0 | 1 | 0 |
| 4 | 1 | 2 | 2 |
| 5 | 0 | 1 | 0 |
| 6 | 2 | 2 | 4 |
| 7 | 0 | 1 | 0 |
| 8 | 5 | 2 | 8 |
| 9 | 2 | 4 | 4 |
| 10 | 14 | 6 | 24 |
| 11 | 10 | 96 | 24 |
| 12 | 42 | 1134 | 80 |

At length \(12\), there are **exactly \(1134\) labeled optimal codebooks**, all containing \(42\) words. Every optimum contains \(16\) reverse-complement pairs and \(10\) reverse-complement-fixed words. At length \(11\) the maximum drops to \(10\), while length \(10\) permits \(14\): the short-length capacity is not monotone in blocklength.

## Assumptions and scope
The alphabet is the labeled binary set \(\{0,1\}\) with bitwise complement. For \(w=w_1\cdots w_n\), define \(\rho(w)=\overline{w_n}\cdots\overline{w_1}\). Non-overlap forbids all equality of proper prefix/suffix pairs at lengths \(1\le k<n\), both between distinct words and from a word to itself. Count *literal subsets* of \(\{0,1\}^n\), not symmetry orbits of codebooks; no further Hamming-distance or biochemical constraint is imposed. In the table, a single reverse-complement orbit is retained if the entire orbit is internally non-overlapping. An orbit may have one or two members. The theorem makes **no** statement about exact optimal sizes beyond length \(12\).

## Proof
**Finite reduction.** For each length \(n\ge2\), partition all \(2^n\) binary words into disjoint orbits \(O(w)=\{w,\rho(w)\}\), retaining an orbit precisely when all its ordered word-pairs satisfy the proper-prefix/suffix non-overlap condition. Construct an undirected simple graph \(G_n\) with one vertex per retained orbit, and an edge between two orbits exactly when *every* pair of their member words satisfies non-overlap. Weight each vertex by \(\lvert O(w)\rvert\in\{1,2\}\).

Any strand-closed code must be a union of whole orbits. Its own internal non-overlap forces every included orbit to be a graph vertex, and the between-orbit requirement forces all selected vertices to form a clique. Conversely, a clique gives a unique strand-closed, non-overlapping code, of cardinality precisely the sum of its vertex weights. This is a bijection, not only a bound. Since all weights are positive, every code of maximum cardinality comes from a **maximal** clique in the ordinary unweighted inclusion sense. It therefore suffices to enumerate all maximal cliques of each \(G_n\) and take both the largest total weight and the number attaining it.

**Exact exhaustion.** `verify_exhaustive.py` constructs every word, every orbit, and every graph edge directly by comparing all proper prefixes and suffixes. It performs recursive maximal-clique enumeration on bitsets with disjoint candidate and excluded sets; a subtree is pruned only when its current weight plus the weight of *every* remaining candidate is strictly smaller than the best weight already found. This strict inequality retains *all* ties. The program counts each maximal clique once and checks a corresponding maximum codebook directly. Its complete integer output is the displayed table, including \(80\) retained orbit vertices, maximum weight \(42\), and \(1134\) maximizing cliques at length \(12\). No extrapolation from finite samples is used: the claimed range contains exactly twelve lengths and each finite graph is exhausted.

**Independent exhaustive formulation.** `verify_independent.cpp` independently constructs orbits and overlaps using bitwise operations on unsigned integers and uses pivoted Bron–Kerbosch recursion on \(128\)-bit adjacency masks, with a separate weighted bound and tie counter. For each length, its maximum and tie count coincide with the first verifier; at length \(12\), its recursion visits \(2048\) nodes. At length \(1\), there are no nonempty proper overlaps, and the unique full code \(\{0,1\}\) is optimal, giving \(M_1=2,T_1=1\). The other eleven entries follow from the exhaustive orbit graphs.

**Concrete lower-bound witness.** The following \(42\) length-\(12\) words form a strand-closed non-overlapping code; the tests above and the standalone verification scripts directly check closure and every ordered prefix/suffix pair:

```
000000011011 000000111011 000000111111 000001011011 000001011111 000001101011 000001111011
000010101111 000010111011 000011001111 000011100111 000011101011 000100011011 000100110111
000101010111 000101011011 000101100111 000101101011 000110001111 000110010111 000110011011
000110100111 000110101011 001000011011 001000011111 001000101111 001000111011 001000111111
001001010111 001001011011 001001011111 001001100111 001001101011 001001110111 001001111011
001001111111 001010001111 001010010111 001010011011 001010011111 001010100111 001010101011
```

The first verifier also records that each maximum length-\(12\) code uses exactly \(16\) two-word orbits, so the remaining \(10\) vertices of any maximum must be one-word fixed orbits. The same conclusion is verified by counting the selected-orbit-type distribution during enumeration.

## Verification
Run `python3 verify_exhaustive.py` with Python's standard library. Independently run `g++ -O3 -std=c++17 verify_independent.cpp -o verifier` followed by `./verifier`. Both rebuild the codeword universe from first principles, construct the orbit conflicts and enumerate maximal cliques. The first verifier checks its exemplar codebooks by direct prefix/suffix comparisons and agrees with the second on the full table. At length \(12\), the Python nonpivot recursion visits \(5,210,780\) nodes and the C++ pivoted version visits \(2048\); different search traversals produce the same weight and tied-optimum count. The witness above can also be independently tested by checking all \(42^2\) ordered word pairs and all eleven proper overlap lengths. No solver, database export, floating-point arithmetic, or external package is required.

## Relationship to prior work
Chee, Kiah, Purkayastha and Wang (first public 2012) establish general cross-bifix-free code constructions and bounds; Blackburn (2013) develops unrestricted non-overlapping code theory and short-length bounds. Stanovnik, Moškon and Mraz subsequently study unrestricted maximum non-overlapping codes, without imposing reverse-complement closure. The publicly available work *Reverse-complement-invariant binary synchronization: exact feasibility and full asymptotic rate* proves that a nonempty strand-closed binary non-overlapping code exists exactly outside lengths \(3,5,7\), and obtains an asymptotic rate-one construction, but **explicitly does not claim** the exact maxima \(M_n\) at every short length or numbers \(T_n\) of maximizing codebooks. Those results therefore do not supply the displayed finite census by immediate specialization, nor does the analogous quaternary/DNA strand-closed four-mer optimum imply it. The present finding concerns the exact size *and the number of equality cases* for all binary lengths through twelve, not a new general existence theorem.

## Limitations
The conclusion is finite, restricted to \(1\le n\le12\), and does not prove a formula for larger lengths or establish a new asymptotic rate. The enumeration is an executable exhaustive proof and not a short human-only structural classification of all \(1134\) optimizers. Literal codebook counts are not counts modulo reversal, complementation, or arbitrary coordinate symmetries. An overlooked older constrained-code table or unindexed repository calculation could have recorded the same numbers; historical novelty has not been independently certified. The binary reverse-complement involution is an abstract strand-symmetry model, not a complete DNA storage-channel model.

## References
- Y. M. Chee, H. M. Kiah, P. Purkayastha and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, first posted 2012-09-03, https://arxiv.org/abs/1209.0236.
- S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, first posted 2013-03-05, https://arxiv.org/abs/1303.1026.
- L. Stanovnik, M. Moškon and M. Mraz, *In search of maximum non-overlapping codes*, https://doi.org/10.1007/s10623-023-01344-z.
- *Reverse-complement-invariant binary synchronization: exact feasibility and full asymptotic rate*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-reverse-complement-invariant-binary-synchronization-exact-feasib--0c804986fafb/RESULT.md.
