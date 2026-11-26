# Joint shortest-reset-word census for rank-six eight-state circular automata

## Finding

Let \(Q=\mathbb Z/8\mathbb Z\) and let \(\mathcal A_b=(Q,\{a,b\})\), with \(a(i)=i+1\pmod8\) and \(b:Q\to Q\) any function with image cardinality six. Write \(L(b)\) for the shortest reset-word length, or \(-1\) when no word resets, and \(W(b)\) for the number of literal words over \(\{a,b\}\) of length \(L(b)\) that reset; let \(W(b)=0\) if there is no reset word. Identify second-letter maps only by cyclic conjugation \(b\mapsto a^s b a^{-s}\), keeping both letters distinguished.

The complete joint distribution of \((L(b),W(b))\), across every one of the \(670{,}608\) cyclic-conjugacy classes, is **exactly the 648-entry table** `data/joint_histogram.csv`. There are \(663{,}680\) synchronizing classes and \(6{,}928\) nonsynchronizing classes. Among the synchronizing classes, exactly \(388{,}869\) have a unique shortest reset word. There are \(121\) distinct multiplicity values including zero, tabulated in `data/word_histogram.csv`.

The largest shortest-word multiplicity is

\[
\max_{\operatorname{rank}(b)=6}W(b)=110{,}592.
\]

It is attained by exactly one rotation class, represented in state order \(0,1,\ldots,7\) by the image tuple

\[
(b(0),\ldots,b(7))=(1,2,3,4,5,1,2,0),
\]

and its shortest reset words have length \(30\). In contrast, the unique class with the largest reset length \(36\) has only eight shortest reset words, represented by \((0,1,2,3,4,0,1,7)\). Already among the classes of reset length \(10\), shortest-word multiplicities vary from \(1\) to \(32\), so reset length alone does not determine control-sequence redundancy.

The reset-length marginal, the number of rotation classes, and the length-36 extremizer also appear in the separate threshold census [3]; they are included for calibration and are **not claimed as new**. The contribution is the complete shortest-word multiplicity distribution jointly with length, including the exact unique maximum and the counts of classes with a unique shortest word.

## Assumptions and scope

This is a finite, exact result solely for **eight** labelled states, a designated cyclic permutation letter, one arbitrary rank-six second letter, and two distinguished alphabet symbols. Distinct letter strings count separately even when two letters induce the same transition on an intermediate subset. Rotations are the only allowed state relabelings: letter interchange and general permutations are not quotiented. Failure to synchronize is represented by the pair \((-1,0)\). No extrapolation to other orders, other ranks or arbitrary two-letter automata is asserted.

Each CSV row has columns `reset_length,shortest_word_count,rotation_classes`, and all unlisted joint pairs have zero classes. Values are integers, not samples or floating approximations.

## Proof

**Complete family and orbit reduction.** Every function \(b:Q\to Q\) is encoded uniquely as an eight-digit base-eight integer, with its digit in position \(i\) equal to \(b(i)\). Testing the number of different digit values to be six exhausts all

\[
\binom86\,6!\,\left\{\begin{matrix}8\\6\end{matrix}\right\}
=5{,}362{,}560
\]

eligible labelled maps (the braces denote a Stirling number of the second kind). Cyclic conjugation preserves \(a\) and acts on each map by \(b_s(i)=b(i-s)+s\pmod8\). Choosing the smallest base-eight encoding in each of the eight rotations visits precisely one member of each orbit. For an independent orbit-count check, a rotation by four fixes exactly \(\binom43\,3!\,\left\{\begin{matrix}4\\3\end{matrix}\right\}2^4=2{,}304\) eligible maps: it acts on four antipodal input pairs, maps onto exactly three antipodal output pairs, and assigns one phase bit per input pair. No other nonidentity rotation fixes a rank-six map, because a map commuting with an order-four or order-eight rotation has image cardinality divisible by four. Burnside's lemma gives \((5{,}362{,}560+2{,}304)/8=670{,}608\) orbits. (There are \(576\) size-four orbits and \(670{,}032\) size-eight orbits.)

**Exact shortest-word recurrence.** Represent a nonempty subset \(S\subseteq Q\) by an eight-bit mask. The letters induce directed edges from \(S\) to \(a(S)\) and \(b(S)\) in the 255-vertex nonempty-subset automaton, retaining both alphabet-labelled edges if their endpoints coincide. A word resets precisely if its path from \(Q\) reaches a singleton. Breadth-first search computes the shortest distance \(d(S)\) from \(Q\); the number \(c(S)\) of shortest labelled paths from \(Q\) to \(S\) obeys \(c(Q)=1\) and, for every letter-edge \(S\to T\) with \(d(T)=d(S)+1\), the update \(c(T)\leftarrow c(T)+c(S)\). Summing \(c(T)\) over singleton states at the minimum possible depth gives exactly \(W(b)\). A shortest word cannot have hit a singleton earlier, since all later images remain singleton, so there is neither premature-acceptance overcounting nor omission. This is a finite exhaustive proof, not sampling.

The `src/forward_census.cpp` program implements that recurrence on every canonical rank-six map and accumulates the joint histogram. The `src/reverse_census.cpp` program builds both reversed subset-transition edge lists, starts breadth-first search from **all eight singletons**, and counts shortest paths **backward** to the full state mask. The two recurrences produce identical counts for all \(648\) populated joint cells. The reverse program explicitly checks overflow on path-count additions; the forward program uses unchecked unsigned accumulators, so the forward output alone is not the arithmetic check. In the reverse program the class counters are bounded by the number of eligible maps.

## Verification

From a directory containing the embedded files, with a C++17 compiler and Python 3:

```sh
g++ -O2 -std=c++17 src/forward_census.cpp -o forward
g++ -O2 -std=c++17 src/reverse_census.cpp -o reverse
./forward > forward.json
./reverse > reverse.txt
python3 src/check_outputs.py forward.json reverse.txt data/joint_histogram.csv data/word_histogram.csv
```

The checker compares each of the \(648\) joint cells across the separately generated outputs and the embedded table, reconstructs the 121-entry shortest-word marginal, verifies the total number of classes, and checks the unique maximum and critical individual cells. It prints `VERIFY_OK` on success. The exact finite certificate is the source code plus the full machine-readable table; the reset-length marginal alone would not determine these entries.

For the unique maximal-multiplicity representative, one actual length-30 reset word is `baaaabaaabaaaaabaaaabaaaabaaab`, which maps the whole state set to \(\{1\}\). The number of distinct shortest words for that automaton is \(110{,}592\), not merely the existence of this example. For the largest-length representative, `baaaaabaaaabaaaaaabaaaaabaaaaabaaaab` is a shortest reset word of length \(36\).

## Relationship to prior work

Hoffmann's work on the synchronizing-word language of circular automata [1] studies complete reachability and maximal state complexity, particularly rank-\(n-1\) letters, rather than the number of shortest words for every rank-six map. Szykuła and Zyzik [2] develop exact shortest-length algorithms and report reset-length experiments, without this joint multiplicity classification. The separate exact enumeration [3] for the same rank-six family supplies the **reset-length marginal** and the longest threshold, not the counts of shortest literal words. Its date alone does not establish an order of publication. Neither the length marginal nor the known results about individual critical automata or rank-seven families determine this 670,608-class joint census.

## Limitations

This is a computer-assisted *finite* proof, and the full-breadth algorithms deliberately inspect every eligible eight-state map. It does not prove an infinite-family formula or a complexity bound for larger state sets. Originality comparisons cover the cited accessible literature and indexed related claims; an unindexed prior table with the identical multiplicity distribution cannot be excluded.

## References

1. S. Hoffmann, “State Complexity of the Set of Synchronizing Words for Circular Automata and Automata over Binary Alphabets,” arXiv:2011.14404, first publicly available 2020-11-29, https://arxiv.org/abs/2011.14404.
2. M. Szykuła and A. Zyzik, “An Improved Algorithm for Finding the Shortest Synchronizing Words,” arXiv:2207.05495, first publicly available 2022-07-03, https://arxiv.org/abs/2207.05495.
3. *The exact reset-threshold spectrum of eight-state circular rank-six automata*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-the-exact-reset-threshold-spectrum-of-eight-state-circular-rank--c9814c09eaa0/RESULT.md.
