# The exact reset-threshold spectrum of eight-state circular rank-six automata

## Finding

Let \(Q=\mathbb Z/8\mathbb Z\), let \(a(i)=i+1\pmod 8\), and let \(b:Q\to Q\) range over **all maps with image size exactly six**. A reset word is a word over \(\{a,b\}\) mapping \(Q\) to a singleton; \(\tau(b)\) is its shortest length, with \(\tau(b)=-1\) when no reset word exists. Equivalence is conjugation by powers of the fixed cycle \(a\), not arbitrary relabeling or interchange of letters.

**Complete exact classification.** There are \(5{,}362{,}560\) labeled maps and \(670{,}608\) cyclic-rotation classes. Exactly \(6{,}928\) classes are non-synchronizing and \(663{,}680\) are synchronizing. The complete spectrum, including every nonzero count, is:

| Reset threshold | Rotation classes | Labeled maps |
|---:|---:|---:|
| not synchronizing | 6,928 | 53,120 |
| 4 | 7,560 | 60,480 |
| 5 | 20,876 | 167,008 |
| 6 | 47,159 | 377,272 |
| 7 | 52,203 | 417,624 |
| 8 | 72,285 | 578,280 |
| 9 | 95,612 | 764,896 |
| 10 | 95,214 | 761,712 |
| 11 | 88,342 | 706,736 |
| 12 | 64,180 | 513,440 |
| 13 | 46,341 | 370,728 |
| 14 | 31,079 | 248,632 |
| 15 | 19,574 | 156,592 |
| 16 | 11,017 | 88,136 |
| 17 | 5,829 | 46,632 |
| 18 | 3,005 | 24,040 |
| 19 | 1,648 | 13,184 |
| 20 | 942 | 7,536 |
| 21 | 450 | 3,600 |
| 22 | 201 | 1,608 |
| 23 | 87 | 696 |
| 24 | 44 | 352 |
| 25 | 9 | 72 |
| 26 | 8 | 64 |
| 27 | 4 | 32 |
| 28 | 4 | 32 |
| 29 | 1 | 8 |
| 30 | 1 | 8 |
| 31 | 3 | 24 |
| 35 | 1 | 8 |
| 36 | 1 | 8 |


The maximum finite reset threshold is exactly **\(36\)**, attained by **one** rotation class, with canonical representative

\[
b=(0,1,2,3,4,0,1,7).
\]

The next-highest thresholds are \(35\) (one class) and \(31\) (three classes); no class has threshold \(32,33,\) or \(34\). Exactly seven classes have threshold at least \(29\). The exact mean over synchronizing rotation classes is \(3322203/331840\).

Every map commuting with the antipodal shift \(a^4\) is non-synchronizing, and there are exactly \(2{,}304\) such labeled rank-six maps, forming \(576\) rotation classes of size four. All other rotation classes have size eight.

## Assumptions and scope

The automaton is complete, deterministic, binary, and has eight labeled states. One input letter is the prescribed forward eight-cycle, and the other is an arbitrary rank-six function; no assumption of idempotence, monotonicity, or injectivity elsewhere is made. Its reset threshold is computed from the full state set, not from a chosen subset. Reversal of the direction of the first cycle and exchange of alphabet letters are **not** part of the specified equivalence. The table uses the marker \(-1\) for the non-synchronizing case.

The guiding source concerns exact algorithms for shortest reset words, first publicly released on **2022-07-03**. This classification is a distinct, complete finite claim and does not assert an infinite-state-number bound.

## Proof

**Counting all maps.** Choose the six-element image of \(b\) in \(\binom86=28\) ways. For a fixed six-element image, the number of surjections from eight labeled inputs is \(6!\,S(8,6)=720\cdot266=191{,}520\), where \(S(8,6)\) is a Stirling number of the second kind. Therefore there are precisely \(5{,}362{,}560\) labeled maps. Both enumerators visit exactly this set, using respectively all base-eight output tuples with a rank filter and a pruned recursive generation of rank-six mappings.

**Counting rotation classes.** A power \(a^k\) fixes \(b\) under conjugation exactly when \(b\) commutes with \(a^k\). Because its six-element image must be a union of orbits of \(a^k\), nonidentity rotations other than \(a^4\) are impossible stabilizers: their orbits have sizes eight or four, neither dividing six. A map commuting with \(a^4\) is determined by its outputs on \(0,1,2,3\), with \(b(i+4)=b(i)+4\). It has rank six precisely when those four outputs occupy exactly three of the four antipodal output pairs. The count is

\[
\binom43\bigl(3!S(4,3)\bigr)2^4=4\cdot36\cdot16=2304.
\]

Burnside's lemma now gives \((5{,}362{,}560+2{,}304)/8=670{,}608\) orbits. Each half-turn-invariant map is non-synchronizing because every word commutes with the fixed-point-free permutation \(a^4\), whereas a constant transformation cannot commute with it. The orbit classification has exactly \(576\) four-element orbits.

**Exact reset computation.** Encode each nonempty subset \(S\subseteq Q\) as an eight-bit mask. Its two successors are \(A(S)=\{i+1\bmod8:i\in S\}\) and \(B(S)=\{b(i):i\in S\}\). Every word induces precisely a path from the full mask \(255\); conversely every such path is a word. Breadth-first search therefore returns the shortest possible reset length upon first reaching any singleton, and returns \(-1\) precisely when all reachable masks have been exhausted without reaching a singleton. There are at most \(255\) reachable nonempty masks, so each search terminates exhaustively. The `orbit_census.cpp` program enumerates all rank-six maps, retains exactly one lexicographically least member of each rotation class, and runs this search. Its complete counts appear in `spectrum.csv`.

The separately implemented `labeled_crosscheck.cpp` instead generates **all** rank-six maps directly with a recursion pruning too-few/too-many distinct images, uses a different subset-image implementation scanning all eight positions for both letters, and runs its own breadth-first search. For each threshold, it counts labeled maps and, separately, the half-turn-fixed maps. By Burnside's lemma their sum divided by eight is the number of rotation classes. Its results match every coefficient of the independently collected canonical-orbit histogram, including the non-synchronizing class.

For the extremal map above, a third Python breadth-first search independently reconstructs the length-\(36\) word `baaaaabaaaabaaaaaabaaaaabaaaaabaaaab`, which ends in state zero. The breadth-first-search distance certificate excludes all shorter words for that map. Since the complete two-way census finds no greater threshold and exactly one rotation class at \(36\), this witnesses and establishes the claimed unique maximum.

## Verification

The delivery contains `orbit_census.cpp`, `labeled_crosscheck.cpp`, `spectrum.csv`, and `verify_spectrum.py`. With Python 3 and a standard C++17 compiler, run from their common directory:

```sh
python3 verify_spectrum.py
```

The driver independently compiles and runs both full exhaustive enumerators, compares every histogram coefficient with the CSV, checks the Burnside weights, verifies the total count \(5{,}362{,}560\), the \(2{,}304\) fixed-point maps, the \(670{,}608\) classes, and reproduces the length-\(36\) witness by a third state-search implementation. Successful execution prints `VERIFIED 31 threshold entries; 670608 orbits; 5362560 labeled maps; extremal length 36`. These checks were executed from the included source files and verified before delivery.

## Relationship to prior work

Szykuła and Zyzik (2022) develop efficient shortest-reset-word algorithms and study sampled binary automata, but do not publish this eight-state rank-six conditional spectrum. The closest specifically comparable prior finite table, *Complete reset-threshold spectrum for eight-state circular defect-one automata* (2026), treats the **disjoint** class of rank-seven second letters: its \(141{,}120\) rotation classes and maximal threshold \(49\) do not imply the rank-six spectrum. Kisielewicz, Kowalski and Szykuła (2016) verify general small-state conjectures, rather than enumerating this conditional histogram. Don, Zantema and de Bondt (2017 preprint) give exact critical-frequency counts for automata on at most six states and discuss larger-state critical cases, but no exact rank-six circular eight-state table. General synchronizing-automata bounds do not force the sharp value \(36\) or the coefficient table. The names *defect-two circular automata*, *rank-six cyclic automata*, and *one full-cycle permutation plus a rank-six transformation* all describe the same object here.

## Limitations

This is a finite exhaustive classification for **eight** states, not a proof about all numbers of states or arbitrary noncycle first letters. The complete histogram is computationally certified by exhaustive independent algorithms; the analytic part establishes the parameter and orbit counts and the half-turn obstruction. No abstract closed form for all alphabet sizes is asserted. No inference of historical uniqueness is made: an unindexed exact computer enumeration could precede this classification. Only self-review has been performed, and independent expert audit has not been performed.

## References

1. M. Szykuła and A. Zyzik, *An Improved Algorithm for Finding the Shortest Synchronizing Words*, first public 2022-07-03, arXiv:2207.05495, https://arxiv.org/abs/2207.05495; ESA 2022, DOI 10.4230/LIPIcs.ESA.2022.85.
2. A. Kisielewicz, J. Kowalski and M. Szykuła, *Experiments with Synchronizing Automata*, first public 2016-07-14, arXiv:1607.04025, https://arxiv.org/abs/1607.04025.
3. H. Don, H. Zantema and M. de Bondt, *Slowly synchronizing automata with fixed alphabet size*, first public 2016-09-22, arXiv:1609.06853, https://arxiv.org/abs/1609.06853.
4. *Complete reset-threshold spectrum for eight-state circular defect-one automata*, publicly accessible finding https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-reset-threshold-spectrum-for-eight-state-circular-defec--d2476f0a726f.
5. S. Hoffmann, *State Complexity of the Set of Synchronizing Words for Circular Automata and Automata over Binary Alphabets*, arXiv:2011.14404, first public 2020-11-29, https://arxiv.org/abs/2011.14404.
