# Sharp two-step sphere maximum for odd-length reverse-complement duplication

## Finding
Let \(\Sigma\) be a finite alphabet with a fixed-point-free involution \(a\mapsto\bar a\), and let \(k\ge1\) be odd. For a word \(x\in\Sigma^n\) with \(n\ge k\), form exactly two sequential fixed-length reverse-complement duplications, each inserting the reverse-complement of a selected contiguous length-\(k\) factor immediately after that factor. Denote the set of distinct resulting words of length \(n+2k\) by \(D_k^{(2)}(x)\). Then

\[
\max_{x\in\Sigma^n}|D_k^{(2)}(x)|
=(n-k+1)(n+1)-\binom{\max\{n-2k+2,0\}}{2}.
\]

Every constant source \(a^n\) attains this bound. This establishes an odd-length reverse-complement counterpart to the known even-length maximum. The assertion is about the maximum, not a classification of all maximizers.

## Assumptions and scope
A *complement* is a map \(a\mapsto\bar a\) such that \(\bar{\bar a}=a\) and \(\bar a\ne a\) for every symbol. Necessarily \(|\Sigma|\) is even and at least two. For \(x=u v w\) with \(|v|=k\), write

\[
T_k(u v w)=u v\,(\bar v)^R w,
\]

where \((\bar v)^R\) reverses the symbolwise complement of \(v\). Positions are zero-indexed, and both operations act on the current word; the second operation may use symbols created by the first. There is no deletion, substitution, noise, nor restriction that the two selected factors be disjoint. We count distinct *outputs*, not operation histories. All integer choices \(n\ge k\ge1\), with \(k\) odd, are covered, including \(n<2k\).

## Proof
**1. A universal history-collision upper bound.** The first operation has \(n-k+1\) start positions. The intermediate length is \(n+k\), so the second has \(n+1\) start positions. Thus the number of ordered two-step histories is

\[
H=(n-k+1)(n+1).
\]

Fix two nonoverlapping length-\(k\) windows of the *original* word, with start positions \(i<j\) and \(j-i\ge k\). Duplicating the first window then the second, whose start has moved to \(j+k\), produces the same word as duplicating the second window then the first, whose start remains \(i\). These are the distinct histories \((i,j+k)\) and \((j,i)\). Different pairs \(\{i,j\}\) produce disjoint pairs of histories: the first history has its second index strictly greater than its first, whereas the second has its second index strictly smaller; in either case the original pair is recoverable. There are

\[
P=\sum_{i=0}^{n-2k}(n-2k-i+1)
=\binom{\max\{n-2k+2,0\}}{2}
\]

such disjoint pairs (the sum is empty if \(n<2k\)). Each pair reduces the count of distinct outputs by at least one, independently of any further collisions. Consequently \(|D_k^{(2)}(x)|\le H-P\) for every source word.

**2. A constant source and its first descendant.** Choose \(a\in\Sigma\) and set \(b=\bar a\ne a\). The first operation at source position \(i\in\{0,\ldots,n-k\}\) gives

\[
y=a^A b^k a^B,\qquad A=i+k,\quad B=n-A.
\]

The second chosen factor is a length-\(k\) window in \(y\). Write \(t\) for its number of \(b\) symbols. Because the unique \(b\)-run has length \(k\), the selected window can meet it in either a prefix or suffix, or equal it. Its inserted reverse-complement has exactly \(k-t\) occurrences of \(b\). Every final word therefore has exactly \(2k-t\) occurrences of \(b\). Thus outputs with distinct values of \(t\) cannot be equal.

**3. Windows meeting the special run.** If \(t=k\), the chosen window is exactly \(b^k\), and the output is

\[
a^A b^k a^{B+k}.
\]

For each \(A\) this is distinct. Suppose \(1\le t\le k-1\). There are precisely two possible forms for a window having \(t\) symbols of \(b\): a window crossing the left boundary, or one crossing the right boundary. In the first case the final word is

\[
a^A b^t a^t b^{2(k-t)}a^B,
\]

while in the second case it is

\[
a^A b^k a^{k-t}b^{k-t}a^{B+2t-k},
\]

where the right-crossing window exists only if \(B\ge k-t\). Within each form, \(A\) and \(t\) determine the word (the initial \(a\)-run has length \(A\)). Between the two forms, the first \(b\)-run has length \(t<k\) versus \(k\). Hence these outputs cannot collide, even if two first-step positions or the two boundary choices are compared. In particular, every history with \(t\ge1\) gives a unique output.

**4. Windows not meeting the special run.** If \(t=0\), the second window lies entirely inside one of the \(a\)-runs, and inserts \(b^k\). Every resulting word is of the form

\[
a^U b^k a^G b^k a^V,\qquad U,G,V\ge0,\quad U+G+V=n.
\]

If the insertion was in the leading \(a\)-run, then \(U\ge k\), and for each such triple there is exactly one such history. If it was in the trailing \(a\)-run, then \(G\ge k\), and for each such triple there is exactly one such history. Both descriptions can apply exactly when \(U\ge k\) and \(G\ge k\). To count these common triples, write \(U'=U-k\), \(G'=G-k\); the nonnegative equation \(U'+G'+V=n-2k\) has exactly \(\binom{n-2k+2}{2}\) solutions when \(n\ge2k\), and none otherwise. At \(G=0\), the adjacent \(b\)-runs merge into \(b^{2k}\), but this pattern still determines \(U,V\) uniquely, and it cannot equal an output with \(G>0\). Thus there are precisely \(P\) repeated histories, each with multiplicity exactly two, and no other repetitions in the \(t=0\) class.

**5. Conclusion.** Since the \(b\)-counts separate the cases \(t\), all histories for \(a^n\) have exactly \(P\) duplicate pairs and no additional collisions. Its output sphere has size \(H-P\), attaining the universal bound and proving the stated equality. The argument in fact works for every \(k\ge1\), but only odd \(k\) is claimed here because the even-length case is already covered in the motivating literature.

## Verification
A standalone Python 3 standard-library checker, `verify_rc_odd.py`, generates every history and deduplicates the resulting words. It tests exhaustive binary sources for selected small odd lengths, exhaustive quaternary sources at small lengths with complement \((0\leftrightarrow1,\,2\leftrightarrow3)\), and long constant binary sources through length \(38\). It checks the proposed sharp maximum, the exact excess \(P\), and that constant-word collision fibers have multiplicity at most two. The completed replay reported `ALL_TESTS_PASS sources= 32234 constant_histories= 272`. These finite checks test implementation and boundary conditions; the proof above supplies the infinite-parameter argument.

## Relationship to prior work
The September 2026 manuscript *Coding for Multiple Reverse-Complement and Palindromic Duplications* (arXiv:2609.00779) proves this count for even duplication lengths using palindromic duplication and an even-length conjugacy to reverse-complement duplication. Its general disjoint-window commutation argument supplies the upper-bound mechanism, acknowledged in Step 1. The odd-length reverse-complement case is not obtained by that even-length conjugacy; Steps 2–4 supply an explicit sharpness construction specific to a complement with no fixed points. The February 2026 work *On the Palindromic/Reverse-Complement Duplication Correcting Codes* (arXiv:2602.01151) studies correcting codes, not this exact odd-length two-step sphere maximum. The 2021 preprint *On the Reverse-Complement String-Duplication System* (arXiv:2112.11811) was available only incompletely for detailed comparison and remains a priority risk.

## Limitations
The result fixes the same block length in both operations and requires a fixed-point-free complement. It does not classify all maximizing source words, give code-size optima, treat noisy duplications, or describe three or more operations. Novelty was assessed against accessible materials and is not a guarantee of historical priority. Independent validation has not been performed.

## References
1. *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779, first publicly posted 2026-09-01. https://arxiv.org/abs/2609.00779
2. *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151, 2026. https://arxiv.org/abs/2602.01151
3. *On the Reverse-Complement String-Duplication System*, arXiv:2112.11811, 2021. https://arxiv.org/abs/2112.11811
4. *Coding for Tandem and Palindromic Duplications*, arXiv:1712.09345, 2017. https://arxiv.org/abs/1712.09345
