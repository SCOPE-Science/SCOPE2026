# Exact output languages of two alternating binary shuffles

## Finding

Fix an integer \(n\ge 1\), and write \(A_n=(01)^n\) and \(B_n=(10)^n\). For finite words \(u,v\), let \(\operatorname{Sh}(u,v)\) be the **set of distinct output words** obtainable by interleaving \(u\) and \(v\) while preserving the order within each input. Different source-position masks producing the same word contribute just once. For a binary word \(w\), define its prefix excess \(h_t(w)=|w_1\cdots w_t|_0-|w_1\cdots w_t|_1\), including \(h_0=0\).

The following complete output-language classifications hold:

\[
\operatorname{Sh}(A_n,A_n)=\{w\in\{0,1\}^{4n}:h_{4n}(w)=0,\quad 0\le h_t(w)\le2\text{ for }0\le t\le 4n\},
\]
\[
\operatorname{Sh}(A_n,B_n)=\{01,10\}^{2n}.
\]

Consequently their respective cardinalities, intersection, and union are
\[
|\operatorname{Sh}(A_n,A_n)|=2^{2n-1},\qquad
|\operatorname{Sh}(A_n,B_n)|=2^{2n},
\]
\[
\operatorname{Sh}(A_n,A_n)\cap\operatorname{Sh}(A_n,B_n)=\{(01)^{2n}\},\qquad
|\operatorname{Sh}(A_n,A_n)\cup\operatorname{Sh}(A_n,B_n)|=3\cdot2^{2n-1}-1.
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), the two input words have length \(2n\) each, and \(n\) is any positive integer. The result counts **distinct words**, not shuffle masks or probability-weighted outputs. The word \(B_n\) is the opposite-phase alternating input. The characterization of \(\{01,10\}^{2n}\) means concatenation of exactly \(2n\) blocks, each either \(01\) or \(10\). All counts and the intersection statement refer to the indicated two output languages, not the set of all binary shuffle squares.

## Proof

**1. Equal-phase necessity and realization.** Every prefix of \(A_n\) has excess either \(0\) or \(1\); adding the two source-prefix excesses forces \(0\le h_t\le2\), and the total excess is zero. Conversely take any length-\(4n\) binary word satisfying the displayed strip condition, and cut it into \(2n\) consecutive two-letter blocks. At every even position, \(h_t\) is even and lies in \(\{0,2\}\). A block starting at height zero is necessarily \(01\) (ending zero) or \(00\) (ending two); a block starting at height two is necessarily \(10\) (ending two) or \(11\) (ending zero).

Maintain two copies of the alternating source and record the number of *completed* \(01\) pairs in each. At even height zero both streams have no pending symbol. At even height two both have a pending \(0\). Allocate a block \(00\) to the first symbol of each stream, and \(11\) to the second symbol of each stream. Allocate \(01\) at height zero entirely to whichever stream has fewer completed pairs. Allocate \(10\) at height two entirely to whichever stream has fewer completed pairs: its pending \(0\) is completed by the first symbol \(1\) of the block, and the final \(0\) reopens the same stream. Each allocation is legal and preserves the invariant that the numbers of completed pairs differ by at most one. At the final height zero, both streams have completed pairs; altogether \(2n\) pairs have been completed, so each stream has exactly \(n\). This is a valid source mask for \(A_n,A_n\).

**2. Equal-phase enumeration.** At the \(2n+1\) even positions, the heights are in \(\{0,2\}\), with initial and final heights zero. Every choice of the next even height determines a unique intervening two-letter block, by the four possibilities above. The first \(2n-1\) next-height choices are independent and the final choice is forced to zero; therefore exactly \(2^{2n-1}\) words occur.

**3. Opposite-phase necessity.** Each prefix of \(A_n\) has excess \(0\) or \(1\), and each prefix of \(B_n\) has excess \(-1\) or \(0\). Every shuffle-output prefix therefore has excess between \(-1\) and \(1\). At an even prefix length the excess is even, hence zero. Thus every consecutive two-letter block has one zero and one one, proving inclusion in \(\{01,10\}^{2n}\).

**4. Opposite-phase realization.** Consider an arbitrary sequence of \(2n\) blocks \(s_1,\ldots,s_{2n}\), each \(01\) (type \(0\)) or \(10\) (type \(1\)). After each complete output block, the source streams are in one of two possible synchronization states: state \(N\), where both streams are at their own pair boundary, or state \(P\), where \(A_n\) has a pending \(0\) and \(B_n\) has a pending \(1\). Both states have combined excess zero. Set \(b_i=0\) or \(1\) for the state \(N\) or \(P\) after output block \(i\), and prescribe \(b_0=b_{2n}=0\). For each choice of intermediate \(b_i\), each output block has a unique legal source assignment. Explicitly, listing the ordered source labels as \(AA,AB,BA,BB\), the four state transitions \(N\to N,N\to P,P\to N,P\to P\) for a block \(01\) use respectively \(AA,AB,BA,BB\); for a block \(10\) they use respectively \(BB,BA,AB,AA\). These transitions are consistent with the source patterns. It remains to choose \(b_i\) so that both sources finish exactly \(n\) pairs rather than an unequal split.

Let \(z\) count type-\(0\) blocks, \(N_{00}\) the adjacent type-\(0\) pairs, and \(N_{11}\) the adjacent type-\(1\) pairs in the type sequence. Inspection of the above source assignments shows that the number \(C_A\) of pairs completed in stream \(A_n\) is
\[
C_A=z-\sum_{i:s_i=0}b_i+\sum_{i:s_i=1}b_{i-1}
=z-\sum_{i:(s_i,s_{i+1})=(0,0)}b_i+\sum_{i:(s_i,s_{i+1})=(1,1)}b_i.
\]
In the second expression the sums run over \(1\le i<2n\); the boundary bits vanish. Each coefficient is \(-1,0\), or \(+1\), with independent bits. Thus the achievable values of \(C_A\) are **every integer** between \(z-N_{00}\) and \(z+N_{11}\), inclusively. Their endpoints equal respectively the number of type-\(0\) runs and \(2n\) minus the number of type-\(1\) runs. In a binary type sequence of length \(2n\), the number of runs of either individual type is at most \(n\), except that a monochromatic word has one run, still at most \(n\). Hence the attainable interval contains \(n\). Choose the bits giving \(C_A=n\). Since \(2n\) pairs are completed in total and the final state is \(N\), stream \(B_n\) also completes \(n\) pairs. This produces the desired shuffle. (For \(n=1\), the same run bound holds.)

**5. Other exact assertions.** There are two choices for each of the \(2n\) opposite-phase blocks, giving \(2^{2n}\) outputs. If a word belongs to both output languages, its even-prefix excess is always zero by the opposite-phase characterization and its odd-prefix excess must be nonnegative by the equal-phase characterization. Therefore every block is \(01\), proving the singleton intersection. Inclusion–exclusion yields the stated union count.

## Verification

The standalone `checker.py` independently constructs distinct shuffle outputs by enumerating source-position masks and compares them with the two claimed descriptions for each \(1\le n\le5\). It checks both exact cardinalities, the unique intersection, and exact language equality. Run `python3 checker.py` using Python 3 standard library; expected final line is `PASS`. These finite tests detect mistakes but do not replace the proof for arbitrary \(n\).

## Relationship to prior work

Ma, Zhang and Hughes (2026) study minimum insertion degrees and mask exchange for fixed-source shuffles, emphasizing that different masks can have the same output. Their results give neither the two exact output languages nor the corresponding two counting formulas here. Grytczuk, Pawlik and Ruciński (2025) investigate recognizability and structural classifications for general binary shuffle squares, including words with constrained runs; those results concern the existence of some equal twin source and do not determine the output set for the prescribed alternating root \(A_n\), still less the opposite-phase shuffle and its intersection. Datko and Pawlik (2025) provide separate root-count and shuffle-square facts, but its accessible indexed discussion does not state this complete two-phase classification. A search for alternate formulations in shuffle products, bounded-height paths, balanced binary words, and alternating-source self-shuffles found no directly stronger stated result; it does not establish global historical priority.

## Limitations

No claim is made about shuffles of arbitrary binary sources, unequal source lengths, three or more source streams, enumerating masks with multiplicity, or the full language of shuffle squares. Earlier implicit derivations, particularly through lattice paths or general shuffle-product formalisms, may exist. Independent mathematical review has not been performed.

## References

1. Haobo Ma, Wenlin Zhang, and Charles E. Hughes, *Block-exchange descent for insertion: commuting projections and minimum masks*, arXiv:2610.39941v1, first public 2026-10-29, https://arxiv.org/html/2610.39941v1.
2. Jarosław Grytczuk, Bartłomiej Pawlik, and Andrzej Ruciński, *Shuffle squares and ordered nest-free graphs*, arXiv:2503.22043, original 2025, https://arxiv.org/html/2503.22043v2.
3. M. Datko and B. Pawlik, *Roots of Binary Shuffle Squares*, *Symmetry* 17 (2025), article 305, https://doi.org/10.3390/sym17020305.
4. Dane Henshall, Narad Rampersad, and Jeffrey Shallit, *Shuffling and Unshuffling*, arXiv:1106.5767, original 2011, https://arxiv.org/html/1106.5767v4.
5. Jarosław Grytczuk, Bartłomiej Pawlik, and Mariusz Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882, original 2023, https://arxiv.org/html/2308.13882v2.
