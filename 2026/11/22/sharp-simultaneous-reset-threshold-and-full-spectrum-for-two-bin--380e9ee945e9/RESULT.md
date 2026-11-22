# Sharp simultaneous reset threshold and full spectrum for two binary three-state automata

## Finding

Let \(\mathcal A\) and \(\mathcal B\) range independently over all complete deterministic three-state automata on the **same ordered binary alphabet** \(\{a,b\}\), with each state set separately labeled \(Q=\{0,1,2\}\). Their synchronous direct product has state set \(Q\times Q\) and acts coordinatewise under each common input letter. Write \(r(\mathcal A,\mathcal B)\) for its shortest reset-word length, with value \(\infty\) if no reset exists.

**Theorem (complete finite classification).** Exactly \(549\) of the \(729\) three-state binary automata synchronize. Among the \(549^2=301401\) ordered pairs with both components synchronizing, the product reset-length distribution is:

| Reset length \(\ell\) | Number of ordered labeled pairs |
|---:|---:|
| 1 | 13041 |
| 2 | 154008 |
| 3 | 87552 |
| 4 | 37872 |
| 5 | 7488 |
| 6 | 1440 |

In particular, **every synchronous product of two synchronizing three-state binary automata has a reset word of length at most six, and six is sharp**. The \(1440\) sharp pairs form exactly **eleven orbits** under independent renaming of the two state sets, simultaneous interchange of \(a,b\), and interchange of the two components: nine orbits have size \(144\) and two have size \(72\). Exactly \(576\), \(576\), and \(288\) of the sharp ordered pairs have individual reset-threshold profiles \((3,4)\), \((4,3)\), and \((4,4)\), respectively.

The pair with transition tables below has threshold six; the word `baabab` resets its product:

| Component | Letter \(a\): images of \(0,1,2\) | Letter \(b\): images of \(0,1,2\) |
|---|---|---|
| \(\mathcal A\) | \((2,1,0)\) | \((1,0,0)\) |
| \(\mathcal B\) | \((2,0,1)\) | \((1,0,0)\) |

## Assumptions and scope

All automata are total functions \(\delta:Q\times\{a,b\}\to Q\); states and letters are labeled, so different transition tables are counted separately. There are no initial or final states. A reset word sends the entire state set to one state; a product reset must reset **both** component state sets using the **same** word. The domain includes nonstrongly-connected and nonsynchronizing automata, though the finite spectrum table conditions on both components being synchronizing. Empty words do not reset a three-state automaton.

## Proof

**Encoding and coverage.** Give each transition table a unique integer \(i\) with \(0\le i<729\), and set
\[
\delta_i(s,c)=\left\lfloor\frac{i}{3^{3c+s}}\right\rfloor\bmod3,
\quad s\in\{0,1,2\},\quad c\in\{0,1\},
\]
where input \(c=0\) is \(a\) and \(c=1\) is \(b\). These six independent base-three digits exhaust all \(3^6=729\) total transition tables without omissions or repetitions.

**Reduction to finite word intersections.** For \(1\le\ell\le6\), define the finite set
\[
R_i(\ell)=\{w\in\{a,b\}^{\ell}:|\delta_i(Q,w)|=1\}.
\]
Because the product action preserves Cartesian rectangles,
\[
\delta_{i\times j}(Q\times Q,w)
   =\delta_i(Q,w)\times\delta_j(Q,w).
\]
Thus \(w\) resets the product precisely when it is in both \(R_i(|w|)\) and \(R_j(|w|)\). In particular, the shortest common reset length through six is the first \(\ell\) for which \(R_i(\ell)\cap R_j(\ell)\ne\varnothing\). If one component never synchronizes, neither can the product; if both synchronize, concatenation of their reset words also resets the product, so the product is synchronizing.

**Exhaustive finite certificate.** The accompanying file `check_words.py` enumerates every \(i\in\{0,\dots,728\}\) and every one of the \(2^{\ell}\) words of each length \(1\le\ell\le6\), directly propagating each of the three starting states. It stores \(R_i(\ell)\) as a \(2^\ell\)-bit integer in lexicographic word order. An independent reachability search over all nonempty subsets of \(Q\) checks, for every \(i\), whether some reset word exists at **any** length. It agrees exactly with the finite-word test and finds \(180\) nonsynchronizing tables and \(549\) synchronizing tables, whose individual shortest lengths are distributed as \(153,324,48,24\) at lengths \(1,2,3,4\). Consequently, a reset word of length at most six exists for each synchronizing table; no unexamined longer component reset can have been missed.

The program compares the six bitset intersections for every one of the \(549^2\) ordered synchronizing pairs, finds at least one nonempty intersection for every such pair by length six, and computes the six entries of the displayed distribution. No extrapolation is involved. The separate C++17 file `census.cpp` independently constructs the images of all nonempty subsets, then performs breadth-first search over the \(8\times8\) subset-pair graph for each table pair. Its distance histogram exactly agrees with the direct-word certificate. Both exhaustive methods cover every labeled transition table, including nongeneric degeneracies, and compute the first reachable singleton-pair distance, which by breadth-first optimality equals the shortest reset length.

**Extremal symmetry classification.** State relabelings in each component are independent copies of \(S_3\); the simultaneous alphabet swap is \(C_2\); swapping the two factors is another \(C_2\). The direct-word checker generates the complete set of \(1440\) extremal ordered pairs, applies all these transformations to each, takes the lexicographically least encoding, and counts the distinct canonical encodings. It obtains eleven orbits with sizes \(144\) in nine instances and \(72\) in two, exhausting \(9\cdot144+2\cdot72=1440\) extremal pairs. The enumeration of individual thresholds alongside product thresholds yields the three stated conditional counts.

**Sharp witness.** For the displayed pair, the sets of states reached from \(Q\) by successive prefixes of `baabab` are:

| Prefix | \(\mathcal A\) | \(\mathcal B\) |
|---|---|---|
| empty | \(\{0,1,2\}\) | \(\{0,1,2\}\) |
| `b` | \(\{0,1\}\) | \(\{0,1\}\) |
| `ba` | \(\{1,2\}\) | \(\{0,2\}\) |
| `baa` | \(\{0,1\}\) | \(\{1,2\}\) |
| `baab` | \(\{0,1\}\) | \(\{0\}\) |
| `baaba` | \(\{1,2\}\) | \(\{2\}\) |
| `baabab` | \(\{0\}\) | \(\{0\}\) |

The direct-word verifier checks that none of the \(62\) binary words of lengths one through five resets both components; hence six is necessary as well as sufficient.

## Verification

With Python 3, run `python3 check_words.py`. With a C++17 compiler, run `g++ -O3 -std=c++17 census.cpp -o census && ./census`. The saved expected outputs are `check_words.out` and `census.out`. Both complete their finite domains without sampling and independently report the length distribution \((13041,154008,87552,37872,7488,1440)\). The Python program additionally checks the eleven-orbit result and the length-six witness; the C++ program directly verifies the full breadth-first search. Both programs use only the files included with this result.

## Relationship to prior work

Fernau and Rystsov (2026) identify the exact intersection of component synchronizing languages for a direct product and establish the general bounds from the maximum to the sum of the component reset thresholds. Volkov's survey explains subset-automaton search and the sharp individual three-state reset upper bound of four. These facts supply the standard framework but do not give the present sharp product bound six, its \(301401\)-pair spectrum or eleven extremal symmetry classes. The present theorem is an explicit finite computation in that framework, not a new general algorithm or an all-state-size reset bound.

## Limitations

The universal bound, census and orbit counts are proved only for ordered **binary** input alphabets and **two components each having exactly three states**. Direct-product synchronization does not imply the resulting nine-state automaton is strongly connected. Code execution is required to reproduce the exhaustive certificate; the symbolic reduction and loop bounds explain why its coverage is exact. This work does not establish a formula in the number of component states, and it does not exclude possible unindexed prior presentations of the same census.

## References

1. H. Fernau and I. Rystsov, *Shortest Synchronizing Words on Product Automata*, arXiv:2611.09136v1, first submitted 2026-11-06, https://arxiv.org/abs/2611.09136 .
2. M. V. Volkov, *Synchronization of Finite Automata*, Russian Mathematical Surveys 77(5), 819–891, https://www.mathnet.ru/eng/rm10005 .
