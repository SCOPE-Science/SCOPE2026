# Complete joint reset-threshold and transition-monoid-size spectrum of four-state binary automata

## Finding

Fix the four-state set \(Q=\{0,1,2,3\}\) and the ordered two-letter alphabet \(\Sigma=\{a,b\}\). For any complete deterministic semiautomaton \(\mathcal A=(Q,\Sigma,\delta)\), let \(\ell(\mathcal A)\) be the shortest length of a word whose action is constant, or \(\infty\) if no such word exists. Let \(m(\mathcal A)\) be the number of **distinct state transformations induced by words**, including the identity induced by the empty word.

The attached `joint_spectrum.csv` specifies the exact joint multiplicity
\[
H(r,s)=|\{\mathcal A:\ell(\mathcal A)=r,\ m(\mathcal A)=s\}|
\]
for **all** \(4^8=65{,}536\) ordered labeled two-letter automata. There are precisely \(179\) nonzero cells; the file lists every cell once, and encodes \(\infty\) by `-1` in its first column. The total is exactly \(65{,}536\).

The notable sharp boundary is that exactly \(96\) automata have \(\ell=9\): precisely \(48\) have \(m=128\), and precisely \(48\) have \(m=145\). These are exactly **two orbits** under state relabeling and exchange of letters. There is **no** automaton with \(\ell=9\) and \(m=176\), whereas \(176\) is the largest possible generated monoid size and is attained at each of the thresholds \(3,4,5,6,7,8\). Thus the greatest monoid size drops sharply by \(31\) at the longest reset threshold.

Represent a map by its image tuple in the order \((f(0),f(1),f(2),f(3))\). The two \(\ell=9\) orbit representatives are
\[
\begin{array}{c|cc|c}
& a & b & m\\\hline
\mathrm{I}&(2,3,1,0)&(0,1,2,0)&128\\
\mathrm{II}&(2,1,0,0)&(0,3,1,2)&145.
\end{array}
\]
A witness for \(\ell=8,m=176\) is \(a=(2,1,0,0)\), \(b=(3,0,1,2)\).

The marginal census, all ordered labeled automata, is:

| \(\ell\) | Number | Minimum \(m\) | Maximum \(m\) |
|---:|---:|---:|---:|
| \(\infty\) | 14,016 | 1 | 28 |
| 1 | 2,032 | 2 | 8 |
| 2 | 22,032 | 3 | 40 |
| 3 | 17,616 | 4 | 176 |
| 4 | 4,896 | 12 | 176 |
| 5 | 3,072 | 17 | 176 |
| 6 | 1,008 | 31 | 176 |
| 7 | 528 | 67 | 176 |
| 8 | 240 | 128 | 176 |
| 9 | 96 | 128 | 145 |

## Assumptions and scope

All four states and both input letters are labeled; the two transitions are arbitrary **total** functions from \(Q\) to \(Q\), independently chosen. The count includes inaccessible, non-strongly-connected, unsynchronizing, and duplicate-letter automata. Empty words contribute the identity to \(m\), but do not reset four states. No equivalence-class weighting is imposed on the joint table. Only the last-threshold subset is separately classified up to simultaneous state conjugacy and input-letter exchange. These statements are finite at exactly four states and two letters; no assertion for higher state counts or larger alphabets is made.

## Proof

**Complete finite encoding.** Every transformation \(f:Q\to Q\) is represented uniquely by the integer \(c(f)=\sum_{i=0}^3f(i)4^i\) in \(\{0,1,\ldots,255\}\). Every ordered automaton corresponds bijectively to one pair \((c(a),c(b))\) in the full Cartesian square of these 256 encodings. The exhaustive programs enumerate exactly this square.

**Transformation closure and shortest reset word.** Precompute \(C(f,g)=g\circ f\). Start a breadth-first search at the identity transformation, and give each visited transformation the outgoing edges \(f\mapsto C(f,a)\) and \(f\mapsto C(f,b)\). Every word supplies a path by induction on length; every path represents a word, so the reached transformations are exactly the transition monoid. Breadth-first distance from the identity is the minimum length of a word inducing that transformation. A transformation is constant exactly when its four image digits agree. Thus the number of reached transformations is exactly \(m\), and the earliest constant transformation gives exactly \(\ell\). If no constant transformation is reached, \(\ell=\infty\). This is an **exhaustive proof**, not a sample experiment: every word, however long, acts as one of the finitely enumerated reachable transformations, and the search closes under both generators.

**Independent reset-distance construction.** For a subset \(S\subseteq Q\), define \(Sg=\{g(i):i\in S\}\). A second program calculates monoid closure by tuple-valued transformations but calculates \(\ell\) separately using breadth-first search from \(Q\) among its 15 nonempty image subsets. Every reset word leads to a singleton subset, and every path to a singleton is a reset word. The first singleton depth is therefore \(\ell\), without referring to a constant-map depth. The independent census matches all 179 cells of `joint_spectrum.csv` **exactly**, and the cell counts sum to 65,536. The two different reachability constructions exclude a common mistake in conflating monoid depth with subset-image depth.

**Extremal symmetry classification.** Each permutation \(p\in S_4\) conjugates the two generators as \(p\circ a\circ p^{-1}\) and \(p\circ b\circ p^{-1}\); the two letters may also be exchanged. Both \(\ell\) and \(m\) are invariant. Direct application of these 24 permutations and two letter orders to each displayed \(\ell=9\) representative produces precisely 48 distinct labeled ordered pairs in each orbit. The independent exhaustive classification finds exactly these sets, one of monoid size 128 and the other of size 145, accounting for all 96 automata with \(\ell=9\). The witness \((a,b)=((2,1,0,0),(3,0,1,2))\) realizes \(\ell=8,m=176\); the full table confirms that 176 is the maximum throughout the domain and that all higher listed length–size combinations vanish. Consequently the maximum monoid-size drop of 31 at \(\ell=9\) is sharp.

## Verification

Both standalone checkers read the exact `joint_spectrum.csv` delivered with this report. They use only a C++17 compiler and the Python 3 standard library:

```text
c++ -std=c++17 -O2 -o verify_transforms verify_transforms.cpp
./verify_transforms
python3 verify_subsets.py
```

The first prints `VERIFY_TRANSFORMS_OK: 65536 complete automata, 179 cells, 96 at threshold 9`; the second prints `VERIFY_SUBSETS_OK: independent histogram and two 48-element extreme orbits`. Both passed when run on the delivered source files and dataset. The CSV has 179 data rows plus its header. All 65,536 distinct transition pairs are included. The two shortest-reset algorithms are complete because no transformation or image subset can occur outside their exhaustively explored finite reachable graphs.

## Relationship to prior work

Szykuła (first publicly posted August 25, 2026) surveys synchronizing automata and the still-open large-state behavior of shortest reset words. This census supplies an exact two-parameter small-state benchmark, **not** a solution of the asymptotic Černý problem. Kisielewicz, Kowalski and Szykuła (2016) conduct extensive reset-threshold experiments but do not give this joint table. East, Egri-Nagy and Mitchell enumerate transformation semigroups up to degree four by size and rank; a semigroup-size table has neither the prescribed generator pair nor its shortest constant-product length and therefore does not yield the joint distribution. Gonze, Gusev, Gerencsér, Jungers and Volkov study general reset bounds when the transition monoid is the *full* transformation monoid; the present binary generated monoids are necessarily smaller and the all-pair finite histogram is a different assertion.

The known four-state maximal reset length of nine, and the existence of a length-nine Černý example, are background, not new claims. The distinct contribution is the complete joint \((\ell,m)\)-population spectrum, especially the absence of maximal monoid size at maximal reset length and the two sharp symmetry types.

## Limitations

The work is restricted to complete labeled binary automata on four states. The proof is exact finite exhaustive enumeration, not a symbolic all-state formula. Its novelty comparison covers inspected available publications and indexed research records; equivalent unindexed datasets or unpublished generator-level classifications remain possible. No independent expert audit has been performed.

## References

1. M. Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245 (first public version August 25, 2026), https://arxiv.org/abs/2608.24245.
2. A. Kisielewicz, J. Kowalski, M. Szykuła, *Experiments with Synchronizing Automata*, arXiv:1607.04025 (2016), https://arxiv.org/abs/1607.04025.
3. J. East, A. Egri-Nagy, J. D. Mitchell, *Enumerating Transformation Semigroups*, arXiv:1403.0274; *Semigroup Forum* 95 (2017), 109–125, https://arxiv.org/abs/1403.0274.
4. F. Gonze, V. V. Gusev, B. Gerencsér, R. M. Jungers, M. V. Volkov, *On the Interplay Between Babai and Černý's Conjectures*, arXiv:1704.04047 (2017), https://arxiv.org/abs/1704.04047.
