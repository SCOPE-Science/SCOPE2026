# Complete four-box classification of smallest attractors for three Tribonacci substitution words

## Finding

Let \(\tau(0)=01\), \(\tau(1)=02\), and \(\tau(2)=0\). For \(m\in\{8,9,10\}\), write \(T_m=\tau^{m-1}(0)\). Each of these finite words has a smallest string attractor of cardinality three. Every such attractor is represented by **exactly one** triple in the four disjoint Cartesian boxes listed below, in zero-based, increasing position order.

For \(m=8\), the four boxes (Cartesian products of permitted first, second, and third positions) are:
\(\{12,14\}\times\{23,27\}\times\{43,44,50,51\}\).
\(\{23,27\}\times\{36,38\}\times\{43,44,50,51\}\).
\(\{23,27\}\times\{43,44,50,51\}\times\{56,58\}\).
\(\{36\}\times\{43,44,50,51\}\times\{67,71\}\).
For \(m=9\), the four boxes (Cartesian products of permitted first, second, and third positions) are:
\(\{23,27\}\times\{43,44,50,51\}\times\{80,82,93,95\}\).
\(\{43,44,50,51\}\times\{67,71\}\times\{80,82,93,95\}\).
\(\{43,44,50,51\}\times\{80,82,93,95\}\times\{104,108\}\).
\(\{67\}\times\{80,82,93,95\}\times\{124,125,131,132\}\).
For \(m=10\), the four boxes (Cartesian products of permitted first, second, and third positions) are:
\(\{43,44,50,51\}\times\{80,82,93,95\}\times\{148,152,172,176\}\).
\(\{80,82,93,95\}\times\{124,125,131,132\}\times\{148,152,172,176\}\).
\(\{80,82,93,95\}\times\{148,152,172,176\}\times\{192,193,199,200\}\).
\(\{124,125\}\times\{148,152,172,176\}\times\{229,231,242,244\}\).

The lengths \((|T_8|,|T_9|,|T_{10}|)=(81,149,274)\) have exactly \((56,112,224)\) distinct smallest attractors, respectively. The corresponding full sets of distinct nonempty contiguous factors have sizes \((2135,7125,23914)\).

## Assumptions and scope

A string attractor of a finite word \(w=w_0\cdots w_{n-1}\) is a set \(\Gamma\subseteq\{0,\ldots,n-1\}\) such that for every **nonempty contiguous factor** \(f\) of \(w\), at least one occurrence of \(f\) occupies an interval meeting \(\Gamma\). Factors are counted as distinct strings, not by their number of occurrences. The substitutions and word orders above are literal; indices are zero based, boxes denote sets of ordered triples, and every Cartesian product entry is strictly increasing. Nothing is asserted for other substitution orders or arbitrary prefixes of the infinite Tribonacci word.

## Proof

**(1) A sharp three-position lower bound.** Each word \(T_m\) contains all three symbols \(0,1,2\). Its three one-symbol factors have disjoint occurrence-position sets, so any attractor must select at least one position bearing each symbol. Consequently every valid attractor has size at least three.

**(2) Finite exact hitting-set equivalence.** For every distinct nonempty factor \(f\) of a finite word \(w\), let \(H_f\) be the union of all index intervals occupied by occurrences of \(f\). By the attractor definition, a triple \(i<j<k\) is valid exactly when \(\{i,j,k\}\cap H_f\ne\varnothing\) for every such \(f\). Equivalently, if \(I_p\) is the set of factor IDs whose \(H_f\) contains position \(p\), then a triple is valid exactly when \(I_i\cup I_j\cup I_k\) is the full set of factor IDs. This equivalence makes a finite exhaustive certificate possible without a heuristic or oracle.

**(3) Exhaustive, reproducible upper bound and classification.** The program `verify_direct.py` generates the words from the literal substitution, enumerates every interval \([s,t)\) with \(0\le s<t\le n\), groups equal substrings by exact string equality, and forms the incidence bit set \(I_p\) by marking every position in **every** occurrence. It then visits all \(\binom n3\) increasing triples, accepts precisely the triples whose union of incidences contains every factor ID, separately forms the Cartesian union of the four printed boxes and checks exact **set equality**. Its complete loop counts and results are:

| \(m\) | \(|T_m|\) | Distinct factors | Tested triples | Valid triples |
|---:|---:|---:|---:|---:|
| 8 | 81 | 2135 | 85320 | 56 |
| 9 | 149 | 7125 | 540274 | 112 |
| 10 | 274 | 23914 | 3391024 | 224 |

The asserted equality is not deduced from the counts: the checker compares the **full sets** of triples with the disjoint box unions. Thus every displayed triple is an attractor and no other triple can be one. Combined with step (1), each is a smallest attractor, and none have smaller cardinality.

**(4) Independent finite search cross-check.** The program `verify_search.py` instead builds, for each distinct factor, a mask containing the union of indices of its occurrences and branches on a currently uncovered factor. Any valid size-three hitting set must contain some position in the coverage mask of that factor, so branching on every such position is complete; at most three selected positions are allowed. It independently obtains the identical sets and verifies the four-box equality for every \(m\) in the claim. Its pruning changes only search order and cannot discard a valid triple. Both checkers use Python's exact arbitrary-precision integer bit operations, not approximations.

## Verification

Run `python3 verify_direct.py` followed by `python3 verify_search.py` in a directory containing both files, using Python 3.8 or newer. Both checkers run with the Python standard library only, assert every displayed word length and factor count, and compare complete sets rather than relying on output logs alone. On their original complete sources the direct checker reported \(85320+540274+3391024=4010618\) visited triples and the independent search checker reported \(56,112,224\) solutions. The proof is finite and exhaustive for the three specified substitution orders; the observed doubling is **not** asserted for any later order.

## Relationship to prior work

Schaeffer and Shallit established that every Tribonacci prefix of length at least four has minimum attractor size three and provided one witnessing triple. That previously established size is used here, not presented as a new general fact; step (1) also provides a direct lower bound for these three words. Banbara and collaborators' February 2026 preprint and subsequent CPM 2026 paper classify **all** smallest attractors of Fibonacci and period-doubling finite words, prompting the analogous fine-grained classification for a ternary morphic family. Their October 2026 extended version additionally treats Thue–Morse but not the Tribonacci boxes reported here. Faro and collaborators likewise address Thue–Morse. The present result contributes the full three-position spectra at three canonical Tribonacci substitution stages and an explicit four-box description, not a theorem for every stage.

## Limitations

This is an exact finite classification for \(m=8,9,10\), not a proof of a recurrence or stabilization for all Tribonacci iterates. The four-box form and doubling in these three cases are experimentally motivated but certified only through the enumerated finite instances. The computational enumeration is accompanied by executable full-loop source; no independent external audit or definitive historical-priority certification has been performed. Search coverage cannot rule out equivalent work not indexed or not publicly accessible.

## References

1. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840, Theorem 6, https://arxiv.org/abs/2012.06840.
2. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno and Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152 (first public version February 18, 2026), https://arxiv.org/abs/2602.16152; CPM 2026, https://doi.org/10.4230/LIPIcs.CPM.2026.33.
3. *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words*, arXiv:2610.10950, https://arxiv.org/abs/2610.10950.
