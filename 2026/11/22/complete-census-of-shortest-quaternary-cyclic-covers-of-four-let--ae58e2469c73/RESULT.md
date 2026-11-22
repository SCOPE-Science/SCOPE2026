# Complete census of shortest quaternary cyclic covers of four-letter palindromes

## Finding

Let \(\Sigma=\{0,1,2,3\}\). A cyclic word is a word indexed modulo its length; its four-letter factors include those crossing the boundary. Require all sixteen distinct ordinary palindromes \(abba\), with \(a,b\in\Sigma\), to appear as oriented contiguous factors. Alphabet labels are fixed, rotations are identified, and reversal is **not** identified.

**The minimum circumference is \(44\), and exactly \(5{,}472\) distinct circular words attain it.** The optima form exactly \(124\) classes under alphabet permutations and reversal, with orbit-size distribution \(105\) classes of size \(48\), \(17\) of size \(24\), and \(2\) of size \(12\). Each optimum contains every required palindrome exactly once. A representative is

`00001102200211221001111331132222332233330033`.

The file `representatives.csv` contains one rotation-normalized, labeled representative of each of the \(124\) full symmetry classes and its orbit size.

## Assumptions and scope

The target language has sixteen four-letter words, not all \(4^4\) words. A cover may contain unrestricted additional nonpalindromic factors, and its length counts all cyclic symbols. Every circular word is normalized by rotating its unique factor `0000` to the beginning; exhaustive verification below establishes that this factor is indeed unique in each optimum. Reversal is allowed as a symmetry only in the second classification, not in the count \(5{,}472\).

This is a complete **fixed-alphabet** finite census. It makes no all-alphabet formula or independent assertion that the general shortest-superstring problem has a new solution.

## Proof

**1. Reduction to an exact finite weighted Hamiltonian problem.** Write the sixteen targets as \(P_{a,b}=abba\), in lexicographic order of the pair \((a,b)\). For two distinct targets \(X,Y\), let \(c(X,Y)\) be \(4\) minus their longest proper suffix-prefix overlap (length from \(0\) to \(3\)). The cost is \(2\) precisely when \(X=abba\), \(Y=baab\) and \(a\ne b\); otherwise it is \(3\) when the outer letters coincide, and \(4\) when they do not. No distinct pair overlaps in three positions.

For any circular cover choose one occurrence of each of the sixteen targets and list them in cyclic order. If successive selected occurrences begin \(d\) symbols apart, then \(d\ge c(X,Y)\): for \(d<4\) this follows from the required literal overlap, and for \(d\ge4\) it is automatic. Summing gives a lower bound of the minimum directed Hamiltonian-cycle cost \(H\) in the sixteen-target overlap graph. Conversely every Hamiltonian tour of total cost \(H\) spells a circular cover of length \(H\) by writing each next target's nonoverlapping suffix. Thus the minimum cover length equals \(H\).

**2. Exhaustive exact recurrence.** Label the lexicographic targets \(0,\ldots,15\), starting with target `0000`. For a visited-target bitmask \(M\) containing zero and a current last target \(j\), define the minimum remaining cost
\[
F(M,j)=\begin{cases}c(j,0),&M=\{0,\ldots,15\},\\
\min_{k\notin M}\bigl(c(j,k)+F(M\cup\{k\},k)\bigr),&\text{otherwise}.\end{cases}
\]
There are only \(16\cdot2^{15}\) possible states. The implementation `verify_dp.cpp` computes the exact same recurrence iteratively, accumulating the number of cost-minimizing paths by integer additions; it returns \(F(\{0\},0)=44\) with \(5{,}472\) optimal target tours. The independent `verify_enumeration.py` evaluates the displayed top-down recurrence with exact integer costs, again finding \(44\), and traverses **all** minimizing successor branches, yielding exactly \(5{,}472\) tours. These are full finite enumerations, not sampled computations.

**3. From tours to distinct circles.** For each minimizing tour the second implementation concatenates the nonoverlapping suffixes at the calculated costs, cyclically normalizes its occurrence of `0000`, and independently scans all cyclic four-windows. Every one of the sixteen target words occurs **exactly once** in every produced circle. Therefore a circle has exactly one induced cyclic order of selected target occurrences, and two distinct optimal tours cannot represent the same circle. The exhaustive traversal also finds \(5{,}472\) distinct normalized circles, which proves the claimed count without a hidden multiplicity factor. Since every minimum circular cover induces one minimizing tour, this exhausts the entire optimum set.

**4. Complete symmetry quotient.** The second implementation applies every one of the \(24\) global alphabet permutations and reversal to all \(5{,}472\) circles, normalizes the unique `0000`, and partitions the resulting set into full orbits. It obtains exactly \(105\) orbits of size \(48\), \(17\) of size \(24\), and \(2\) of size \(12\). The orbit-size check \(105(48)+17(24)+2(12)=5472\) verifies that the classes partition the complete enumeration. All representatives and sizes are reproduced in `representatives.csv` and rechecked against the fresh enumeration by the program.

## Verification

With Python 3 (standard library), run `python verify_enumeration.py` in the directory containing `representatives.csv`. Expected output begins `ENUMERATION_OK 44 5472 5472 124`. Independently compile `verify_dp.cpp` with `g++ -O2 -std=c++17 verify_dp.cpp -o verify_dp` and run `./verify_dp 4`; its expected output is `q=4 n=16 min=44 optimal target orders=5472`. Both were executed against the exact included source files. The CSV provides all \(124\) class representatives, and the first checker checks them against the reconstructed orbits, not merely a stored claimed total.

The recurrence is exact and terminates over a fully specified finite state space. It proves the stated finite theorem; its results are not asserted to generalize to arbitrary alphabet sizes.

## Relationship to prior work

Kari and Xu's *De Bruijn Sequences Revisited* (2012) explains the relation between pseudo de Bruijn sequences of order two and Euler tours of complete graphs with loops, including a parity obstruction over even alphabets. Those results motivate the present **four-symbol, length-four palindromic cover** question but neither enumerate these optimal forty-four-symbol circles nor classify their equality cases. Fici et al. (first public arXiv version 2015-11-26) study approximation for shortest common superstrings with reversals; their general framework supplies no exact palindrome-cover census. Published research results on four-letter reverse-complement palindromes, length-five ordinary palindrome covers, and four-letter tandem squares concern different target families or only cover lengths, and do not imply these optimal equality counts. The general graph-tour and overlap machinery itself is classical and is not claimed as new.

## Limitations

The result is a finite exact classification only for four labeled alphabet symbols and all ordinary four-letter palindromes. It does not count longer palindromes, reverse-complement motifs, or covers on larger alphabets. Source indexing may omit an older equivalent optimized-circuit enumeration; historic priority is qualified. Independent validation beyond the same set of proof and code checks has not been performed.

## References

1. L. Kari and Z. Xu, *De Bruijn Sequences Revisited*, *International Journal of Foundations of Computer Science* 23 (2012), 1307–1322, DOI:10.1142/S0129054112400540; public author full text: https://www.researchgate.net/publication/221465555_DE_BRUIJN_SEQUENCES_REVISITED
2. G. Fici, T. Kociumaka, J. Radoszewski, W. Rytter, T. Waleń, *On the Greedy Algorithm for the Shortest Common Superstring Problem with Reversals*, arXiv:1511.08431, first public 2015-11-26. https://arxiv.org/abs/1511.08431
3. *Sharp cyclic and linear covers of reverse-complement four-palindromes*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-cyclic-and-linear-covers-of-reverse-complement-four-palind--1c5013f138d2
4. *Exact ternary length-five palindromic covers*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-ternary-length-five-palindromic-covers-66-cyclic-and-68-li--11abece62ea8
