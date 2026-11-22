# Prescribed-triple synchronization spectrum of eight-state circular defect-one automata

## Finding

Let \(Q=\mathbb{Z}/8\mathbb{Z}\). Fix \(a(i)=i+1\pmod 8\) and let \(b:Q\to Q\) range over all maps of rank seven. For each three-element state set \(S\), define \(t_b(S)\) to be the least length of a word over \(\{a,b\}\) mapping every state of \(S\) to one state; use \(\infty\) if no such word exists. The **worst prescribed-triple merging time** is \(T_3(b)=\max_{|S|=3}t_b(S)\). This is distinct from the minimum merging time of *some* triple and from the full-state reset threshold \(R(b)\).

Conjugate transformations by the eight cyclic rotations that preserve \(a\). Each class has exactly one representative with omitted output \(0\), so \(b(Q)=\{1,\ldots,7\}\). There are exactly \(141120\) such classes. Of these, \(1856\) have \(T_3(b)=\infty\). For the other \(139264\), the **complete exact distribution** is:

| \(T_3(b)\) | Number of classes | \(T_3(b)\) | Number of classes | \(T_3(b)\) | Number of classes |
|---:|---:|---:|---:|---:|---:|
| 6 | 887 | 7 | 12574 | 8 | 12941 |
| 9 | 24449 | 10 | 33351 | 11 | 27856 |
| 12 | 15546 | 13 | 6841 | 14 | 2896 |
| 15 | 1100 | 16 | 456 | 17 | 181 |
| 18 | 69 | 19 | 60 | 20 | 29 |
| 21 | 9 | 22 | 2 | 23 | 5 |
| 24 | 6 | 26 | 2 | 31 | 1 |
| 33 | 2 | 37 | 1 |  |  |

All missing finite lengths have frequency zero. **The sharp maximum is \(37\), achieved by a unique rotation class**, represented by the output tuple \(b=(1,1,2,3,4,5,6,7)\) in input order. Every other synchronizing class has \(T_3(b)\le33\). The two classes with \(T_3(b)=33\) have tuples \((1,2,3,4,5,6,7,1)\) and \((2,2,3,4,5,6,7,1)\). Only one class attains the next value \(31\). Thus the upper tail contains an isolated worst case and a gap of four letters.

The triple-time distribution is not determined by the full reset threshold. For example, \(b=(2,2,6,3,4,1,7,5)\) and \(b=(1,1,7,6,5,4,3,2)\) both have full reset threshold \(28\), but their worst prescribed-triple times are respectively \(12\) and \(24\). The supplied `joint_spectrum.csv` gives all \(205\) nonzero triple-time/reset-time frequency pairs, in addition to `triple_spectrum.csv`.

## Assumptions and scope

Both letters are deterministic total state transformations, and the directed cycle letter \(a\) is distinguished. Cyclic state relabelings are the only equivalence, not letter swaps or arbitrary conjugation of the fixed cycle. The rank condition is **exactly seven**. Subsets are sets of distinct states, and words act left to right. We take \(t_b(S)=\infty\) precisely when no word merges the selected triple. All finite lengths count both letters with unit cost. The computations characterize the fixed eight-state family only; no assertion is made for arbitrary orders or ranks.

## Proof

**1. Exhaustive nonredundant parameterization.** Each rank-seven map omits one output. A unique conjugating power of the full cycle sends the omitted output to \(0\). Since no nontrivial cycle rotation fixes \(0\), the normalization is unique within each conjugacy class. A normalized map chooses its doubled output in seven ways, its two distinct preimages in \(\binom82\) ways and a bijection from the remaining six inputs to the remaining six outputs in \(6!\) ways. Consequently there are exactly

\[
7\binom82\,6! =141120
\]

normalized maps, without omitted cases or duplicate rotation classes.

**2. An exact finite-state computation of prescribed-triple distance.** Identify each nonempty subset \(S\subseteq Q\) with its eight-bit mask \(M(S)=\sum_{i\in S}2^i\). There are only \(255\) nonempty masks, and applying a letter acts by pointwise image on subsets. The shift letter rotates the mask by one; the rank-seven letter replaces all occupied inputs by their mapped outputs. Construct the directed subset transition graph on the \(255\) nonempty subsets. Its reverse graph, started simultaneously from the eight singleton vertices, has distance \(d_b(S)\) equal to the shortest word length merging the given subset \(S\), with distance undefined exactly when no such word exists. This is the standard multi-source breadth-first-search distance invariant; each edge is one letter and every word corresponds to a directed path.

The first standalone program `count_reverse.cpp` applies this exact reverse search to every normalized transformation from Step 1, obtains \(T_3(b)\) by checking **all \(\binom83=56\) three-element masks**, and tabulates both \(T_3(b)\) and the distance \(R(b)=d_b(Q)\). It regenerates every row of the two CSV tables. Its output identifies the unique maximum \(37\) and the two second-place classes, with the full frequencies displayed above. Each candidate is examined to completion: there is no time cutoff, random sampling, truncated table or convergence assumption.

**3. Independent exhaustive implementation.** The second program `count_forward.cpp` enumerates normalized maps in a different way: for each duplicated output it lexicographically enumerates every permutation of the corresponding output multiset. For each map, it performs a separate **forward** breadth-first search from every one of the \(56\) triples until a singleton is first reached, or until the reachable subset graph is exhausted. It directly recomputes the complete \(T_3\) histogram, the count of nonsynchronizing maps and the unique maximizer. The two implementations use different enumeration strategies and opposite BFS directions, and their full tabulations agree exactly. The agreement checks the exhaustive calculation; correctness additionally depends on the elementary enumeration and shortest-path invariants proved in Steps 1 and 2.

**4. Explicit boundary witnesses and a genuine non-implication.** For the unique extremizer \(b=(1,1,2,3,4,5,6,7)\), the hardest triple is \(S=\{1,4,6\}\). `witness.py` independently finds a length-\(37\) merging word. Both exhaustive searches establish no shorter merging word for this triple and that no triple needs longer. For the two specified maps sharing full reset threshold \(28\), a direct forward check confirms that their worst triple times are \(12\) and \(24\), proving that the known full-reset spectrum cannot by itself determine the triple-time invariant.

For a rank-seven map, all triples are mergeable if and only if the full state set is synchronizable: the forward implication implies that every pair is mergeable (extend it to a triple), and successive pair-merging words reduce the whole image to a singleton. The reverse implication is immediate. The \(1856\) nonmergeable cases match the independently published nonsynchronizing count, an additional consistency check.

## Verification

With a C++17 compiler and Python 3, run the following standalone commands in the directory containing the included files:

```sh
c++ -std=c++17 -O2 count_reverse.cpp -o count_reverse
./count_reverse > reverse_output.txt
c++ -std=c++17 -O2 count_forward.cpp -o count_forward
./count_forward > forward_output.txt
python3 witness.py > witness_output.txt
python3 verify_tables.py reverse_output.txt forward_output.txt
```

Both C++ programs must report `TOTAL 141120 NON 1856 MAX 37 EXTREMA 1` and identical `TRIPLE_HIST` lines matching `triple_spectrum.csv` (omitting the unmergeable CSV row). `count_reverse.cpp` also reports `JOINT_DISTINCT 205` and its `J` lines reproduce `joint_spectrum.csv` exactly. The witness check ends with `WITNESS_OK`, and `verify_tables.py` ends with `TABLES_OK` after comparing both independent outputs against the CSV distributions and their marginals. In both C++ programs each of the \(141120\) transformations and all \(56\) triples are included. This is a complete finite verification rather than evidence for an infinite claim.

## Relationship to prior work

Behague and Johnson, *Synchronizing Times for k-sets in Automata* (first public 2020), study worst and best synchronization times of prescribed subsets and motivate exactly this kind of invariant. The published *Complete reset-threshold spectrum for eight-state circular defect-one automata* gives the exhaustive **full-state** reset-time distribution for the very same \(141120\) transformations, including the count \(1856\) and the \(49\)-letter Černý extremizer; neither that count nor the \(49\)-letter reset threshold is claimed as new. The published *An exact circular-gap formula for every Černý subset rendezvous time* already implies the prescribed-triple distance \(37\) for the standard eight-state Černý transformation; the new statement is **the all-map distribution and unique global extremality within the rank-seven circular family**, including the gap to second place and the joint-spectrum non-implication. General shortest-reset algorithms, and published results about *some* triple rather than the worst prescribed triple, do not imply these \(139264\) class frequencies.

The distinction between minimizing over chosen triples and maximizing their individual shortest merging times is essential. A recent triple-rendezvous work (Zhang, 2026) is about the former; its supplemental full text could not be inspected, so possible additional overlapping tables are recorded as a residual originality risk. No known published theorem in the inspected sources supplies the claimed complete distribution.

## Limitations

This is a complete finite computational classification for eight states with a fixed distinguished cycle letter and rank-seven companion, not an all-order theorem or asymptotic estimate. The underlying shortest-subset-path algorithm is standard. The standalone programs and results are subject to ordinary software and arithmetic reliability, mitigated by independent enumerations and cross-checks; no external mathematical validation is asserted. No claim is made that an unindexed or unpublished table cannot duplicate these coefficients. A plausible 2026 supplemental document was not fully accessible and remains an identified originality risk.

## References

1. N. C. Behague and J. R. Johnson, *Synchronizing Times for k-sets in Automata*, first public 2020-08-27, arXiv:2008.12166, https://arxiv.org/abs/2008.12166, later *Electronic Journal of Combinatorics* 29(3), P3.41 (2022).
2. M. Szykuła and A. Zyzik, *An Improved Algorithm for Finding the Shortest Synchronizing Words*, 2022, arXiv:2207.05495, https://arxiv.org/abs/2207.05495.
3. *Complete reset-threshold spectrum for eight-state circular defect-one automata*, publicly available exact computation: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-reset-threshold-spectrum-for-eight-state-circular-defec--d2476f0a726f.
4. *An exact circular-gap formula for every Černý subset rendezvous time*, publicly available result: https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-an-exact-circular-gap-formula-for-every-ern-subset-rendezvous-ti--660b6553bb5e.
5. E. Zhang, *The triple rendezvous time of a synchronizing automaton can be floor(4n/3)*, 2026, Zenodo record and supplemental material: https://zenodo.org/records/22663347.
