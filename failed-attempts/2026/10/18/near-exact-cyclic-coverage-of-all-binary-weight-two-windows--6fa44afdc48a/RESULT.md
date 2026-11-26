# Near-exact cyclic coverage of all binary weight-two windows

## Finding
For every integer \(k\ge4\), let \(B_2(k)\) be the minimum positive length of a cyclic binary word whose length-\(k\) contiguous circular factors include every binary length-\(k\) word with exactly two ones. Then
\[
\binom{k}{2}+2\lfloor k/2\rfloor-2\ \le\ B_2(k)\ \le\ \binom{k}{2}+k-1.
\]
The two bounds differ by one for even \(k\) and by two for odd \(k\). In particular, \(B_2(k)=\binom{k+1}{2}+O(1)\), with absolute error at most three, establishing the sharp linear correction to the number of prescribed windows. The upper bound is realized by a completely explicit cyclic word. For \(k=3\), the exact value is \(B_2(3)=3\).

## Assumptions and scope
The cyclic host is an indexed circular binary word, with factors read at all cyclic starting positions and with repetitions permitted. It is not required to have weight two itself; only the required length-\(k\) factors have weight two. Every binary length-\(k\) word containing precisely two ones must occur at least once. The results hold for all integer \(k\ge4\); the exceptional \(k=3\) case is stated separately. No exact value is claimed for arbitrary \(k\ge6\).

## Proof
Write \(N=\binom{k}{2}\) and \(c=\lfloor k/2\rfloor\). A length-\(k\) word containing two ones at positions \(a<b\) has cyclic-distance label \(d=\min(b-a,k-(b-a))\), which ranges through \(1,\ldots,c\). Every label occurs among the required factors.

**Lower bound.** Consider any cyclic host covering all required factors, and list in cyclic order those of its length-\(k\) windows containing precisely two ones. Take two consecutive such windows, starting \(t\ge1\) positions apart (so exactly \(t-1\) intervening windows do not have weight two), and let their labels be \(d,d'\). We claim \(|d-d'|\le t-1\). If \(t\ge k\), this is immediate from \(1\le d,d'\le c\). Otherwise identify the two pairs of one-positions modulo \(k\). The actual positions shared by the two overlapping length-\(k\) intervals remain at identical residues; all positions deleted from the first and newly entering the second reduce modulo \(k\) to the same arc \(\{0,\ldots,t-1\}\). If both ones are shared, their labels agree. If exactly one is shared, the other moves within that arc and the circle-distance-to-the-shared-one function is 1-Lipschitz, so its change is at most \(t-1\). If neither is shared, both pairs lie in that arc, and each of their circle distances belongs to \([0,t-1]\). This proves the claim.

Sum the inequality around the entire circular list of weight-two windows. The sum of the intervening-window counts is the total number \(E\) of non-weight-two windows. The label sequence meets both extreme values \(1\) and \(c\), so its cyclic total variation is at least \(2(c-1)\). Thus \(E\ge2(c-1)\). There are at least \(N\) weight-two windows because all \(N\) distinct prescribed factors occur. Hence the host length is at least \(N+2c-2\).

**Upper bound.** Form a cyclic list of positive integer gaps by listing, for \(d=1,\ldots,\lfloor k/2\rfloor\), the entries \(d,k-d\), omitting the second entry if \(d=k-d\), and finally appending one additional entry \(k-1\). Call this cyclic list \(g_1,\ldots,g_k\). It consists of \(1,\ldots,k-1\) once each, together with one extra \(k-1\). Construct the cyclic binary word
\[
W_k=\prod_{i=1}^{k}\bigl(1\,0^{g_i-1}\bigr).
\]
It has length \(\sum_i g_i=N+k-1\). For every gap of length \(d\), its two neighboring gaps each have length at least \(k-d\); this is immediate for the short entries \(d\le\lfloor k/2\rfloor\), whose neighboring entries are complementary large entries, and for the large entries, whose neighboring short entries are at least their complementary value. The appended final \(k-1\) supplies the boundary neighbor for \(d=1\).

Fix any prescribed length-\(k\) word whose two ones are distance \(d\in\{1,\ldots,k-1\}\) apart in linear order. Use the two consecutive ones of \(W_k\) separated by a gap of length \(d\). Place the desired window with its first one at position \(a\), where \(0\le a\le k-d-1\). The neighboring one before that pair is at least \(k-d\) positions to its left, exceeding \(a\); the neighboring one after the pair is at least \(k-d\) positions to its right, exceeding the desired trailing reach \(k-d-1-a\). Thus the window contains exactly those two ones and equals the prescribed word. Every required word occurs. This proves the upper bound.

For \(k=3\), the cyclic word `011` contains the three distinct weight-two length-three words, and three windows are necessary.

## Verification
The accompanying standalone `verify.py` directly builds the cyclic gap construction for every \(k=3,\ldots,200\) and checks its length, prescribed-factor coverage, and neighboring-gap inequalities. Independent enumeration verifies the exact minimum for \(k=3,4,5\) by searching shorter cyclic binary words. These finite computations supplement, but do not replace, the unrestricted proof.

## Relationship to prior work
Sawada, Williams and Wong (2013) construct universal cycles for binary windows whose weights lie in an interval, including weights one and two together. This gives a cycle of length \(\binom{k}{2}+k\), hence a weaker upper bound for the present weight-two covering problem, but does not give the sharp linear lower correction or the present shorter construction. King, Laubmeier, Orans and Godbole (arXiv:1405.5938v1, 2014, Section 3) prove existence of reduced-overlap cycles for fixed-weight words: their prescribed windows advance by at least two positions, so their construction does not imply the present near-minimal unit-shift covering result. The novelty claim is limited to the explicit additive-two interval and its sharp second-order asymptotic for freely padded cyclic hosts.

## Limitations
The exact optimum for all \(k\ge6\) remains unresolved by these bounds; the gap is one or two, and there may be earlier formulations of the same covering extremum under different terminology. The proof concerns circular binary hosts, not noncyclic superstrings or alphabets of greater size. No independent audit has been performed.

## References
- J. Sawada, A. Williams and D. Wong, “Universal cycles for weight-range binary strings,” *Combinatorial Algorithms*, IWOCA 2013, pp. 388–401, DOI:10.1007/978-3-642-45278-9_33. Author-hosted full text: https://www.socs.uoguelph.ca/~sawada/papers/den-range.pdf.
- A. King, A. Laubmeier, K. Orans and A. Godbole, “Universal and Overlap Cycles for Posets, Words, and Juggling Patterns,” arXiv:1405.5938v1, first posted 2014-05-23, especially Section 3, https://arxiv.org/pdf/1405.5938.
