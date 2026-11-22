# Complete equality classification of strand-symmetric binary five-mer decycling sets

## Finding

Exactly ten reverse-complement-invariant decycling sets of cardinality twelve exist in the binary five-word de Bruijn graph \(B(2,5)\). No smaller invariant decycling set exists. Up to global complementation, these ten sets form exactly five pairs. Their exact longest retained directed-path vertex counts are distributed as \(6:4,\ 8:4,\ 10:2\), giving guaranteed-hit window lengths eleven, thirteen, and fifteen. The count of ten and the complete performance distribution are the new statements; the optimum cardinality twelve had already been reported by Marçais, Elder and Kingsford (2024).

## Assumptions and scope

A vertex is a binary string \(w_0w_1w_2w_3w_4\), and there is a directed edge from \(w\) to \(w_1w_2w_3w_4b\), for each \(b\in\{0,1\}\). Both self-loops are included. Let \(\rho(w)=\overline{w_4}\overline{w_3}\overline{w_2}\overline{w_1}\overline{w_0}\), with binary complement \(\overline0=1\), \(\overline1=0\). A set \(S\) is strand-symmetric when \(\rho(S)=S\), and is a decycling set when deleting its vertices leaves a directed acyclic graph. A path length \(L(S)\) is the largest number of vertices on any retained directed path; this is not the number of edges. The corresponding longest binary string avoiding every selected five-factor has length \(L(S)+4\), and every binary string of length \(L(S)+5\) contains a selected factor.

The random-hit statistic is defined separately: select an initial five-word uniformly from all 32 words, then repeatedly append independent fair bits and shift one position until a word in \(S\) first appears. The number of transitions before stopping is zero if the initial word belongs to \(S\). The mean is denoted by \(T(S)\). No assertion is made for larger de Bruijn orders or DNA alphabets with four symbols.

## Proof

For odd-length binary words, reverse complementation has no fixed word: a middle bit would need to equal its own complement. Thus the 32 five-words split into sixteen two-element orbits. Sort the orbits lexicographically by their pair of integer-encoded five-words, using \(0\) through \(31\) in usual binary order. The complete orbit list (one-based labels) is:

| Label | Reverse-complement pair |
|---:|---|
| 1 | `00000`, `11111` |
| 2 | `00001`, `01111` |
| 3 | `00010`, `10111` |
| 4 | `00011`, `00111` |
| 5 | `00100`, `11011` |
| 6 | `00101`, `01011` |
| 7 | `00110`, `10011` |
| 8 | `01000`, `11101` |
| 9 | `01001`, `01101` |
| 10 | `01010`, `10101` |
| 11 | `01100`, `11001` |
| 12 | `01110`, `10001` |
| 13 | `10000`, `11110` |
| 14 | `10010`, `10110` |
| 15 | `10100`, `11010` |
| 16 | `11000`, `11100` |

The two loops force label one, and the two-cycle formed by the alternating words forces label ten. Exhaustive examination of every choice of at most six orbits, including these forced choices, verifies that no choice of five or fewer orbits decycles the graph, and exactly ten choices of six orbits do. The finite exhaustion is rigorously specified by the two executable programs, both operating on the explicit 32-vertex graph, with no calls to numerical optimization or stochastic testing. For each candidate, the first uses Kahn topological elimination and the second uses a recursive three-color directed-cycle test. Since every invariant set has the form of a union of orbits, this is exhaustive and proves both optimality and completeness.

The following ten entries specify every selected set by the **one-based** orbit labels just defined. The column \(T(S)\) is the exact expected transition count.

| Orbit labels | \(L(S)\) | \(T(S)\) |
|---|---:|---:|
| 1, 2, 7, 10, 12, 14 | 6 | \(1201/1024\) |
| 1, 2, 9, 10, 11, 12 | 6 | \(1189/1024\) |
| 1, 3, 4, 7, 10, 14 | 8 | \(5341/4096\) |
| 1, 3, 4, 9, 10, 11 | 8 | \(5125/4096\) |
| 1, 4, 5, 6, 7, 10 | 10 | \(25253/16384\) |
| 1, 5, 10, 11, 15, 16 | 10 | \(25253/16384\) |
| 1, 7, 8, 10, 14, 16 | 8 | \(5125/4096\) |
| 1, 7, 10, 12, 13, 14 | 6 | \(1189/1024\) |
| 1, 8, 9, 10, 11, 16 | 8 | \(5341/4096\) |
| 1, 9, 10, 11, 12, 13 | 6 | \(1201/1024\) |

For each acyclic residual graph, compute its longest path from the topological order using \(L(v)=1+\max_{v\to u}L(u)\), taking \(L(u)=0\) at removed endpoints. Independently, the first-hit expected transitions satisfy \(t(v)=0\) for \(v\in S\), and \(t(v)=1+[t(u_0)+t(u_1)]/2\) otherwise. Acyclicity makes this a finite exact rational recursion. Averaging over all 32 initial vertices yields the displayed \(T(S)\). Finally, global bit complementation preserves the graph and commutes with reverse complementation. Mapping each of the ten listed sets by complement gives precisely five disjoint pairs, verified directly in the second program.

The residual longest-path bound translates to the factor-hitting window claim by the standard bijection between a binary word of length \(m\ge5\) and its \(m-4\) consecutive five-word vertices on a directed path. A path with \(L\) retained vertices is a word of length \(L+4\) avoiding the selected five-factors, but no longer such path is possible.

## Verification

Using Python 3 and only its standard library, run `python3 verify_orbits.py` and `python3 verify_paths.py` in the same directory. The first enumerates all \(\sum_{j=0}^{6}\binom{16}{j}=14893\) invariant orbit subsets of at most six orbits and independently evaluates the exact rational transition statistics. The second independently enumerates the same 14893 candidates through bit masks, uses depth-first cycle detection, and verifies the five complement classes. Both programs print distinct `VERIFY_OK` markers on complete success. Their source code, rather than a separately supplied log, is the reproducible finite certificate.

## Relationship to prior work

Burstein and Kitaev (2003) discuss unavoidable forbidden-word families and their de Bruijn graph formulation, including the classical minimum-size formula. Marçais, Elder and Kingsford (2024), Section 6, Table 3, report an exact symmetric minimum of twelve words for binary order five and an optimized residual maximum path length of six; those two facts are prior knowledge and are not claimed to be new. The table does not specify the ten equality cases or the complete distribution of their residual path lengths and exact rational first-hit expectations. A later general parity theorem (2026) treats existence and lower bounds by order parity, not the exact odd-order five-word equality census.

## Limitations

This is a finite exact classification at binary word length five, not a general characterization for all orders. The uniform fair-bit Markov statistic is mathematical and is not a biological distribution estimate; the source study reports its own path-length optimization convention. The precise number of equality cases might appear in unpublished code, unindexed computations, or uninspected supplementary materials, which remains an originality risk. Independent mathematical review has not been performed.

## References

1. A. Burstein and S. Kitaev, *On unavoidable sets of word patterns* (2003), arXiv:math/0311399, https://arxiv.org/html/math/0311399v1 (submitted 2003-11-23; MSC 68R15).
2. G. Marçais, C. S. Elder and C. Kingsford, *k-nonical space: sketching with reverse complements*, *Bioinformatics* 40 (2024), btae629, https://pmc.ncbi.nlm.nih.gov/articles/PMC11549021/, especially Sections 5–6 and Table 3.
3. O. Babanskyy, *A Parity Theorem for Reverse-Complement-Invariant Minimum Decycling Sets in q-ary de Bruijn Graphs* (2026), arXiv:2611.00240, https://hexagonmath.org/2611.00240v1.
