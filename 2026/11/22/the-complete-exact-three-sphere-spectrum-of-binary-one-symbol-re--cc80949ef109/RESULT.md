# The complete exact-three sphere spectrum of binary one-symbol reverse-complement duplication

## Finding
For every integer \(n\ge1\) and every binary word \(x\in\{0,1\}^{n}\), let \(D_t(x)\) be the set of **distinct** words obtained by exactly \(t\) sequential reverse-complement duplications of one symbol. Each operation replaces a selected symbol \(a\) by \(a\bar a\), where \(\bar0=1\) and \(\bar1=0\); subsequent operations may act on inserted symbols. Define \(r(x)\) as the length of the initial constant run of \(x\). Then

\[
\boxed{|D_3(x)|=\binom{n+2}{3}+r(x)(n+2)-\binom{r(x)}2.}
\]

This is the full source-specific exact-three sphere law, not just a maximum. Its \(n\) different values (one for each \(r=1,\ldots,n\)) are strictly increasing. For \(1\le r<n\), exactly \(2^{n-r}\) labeled binary words attain the value indexed by \(r\); the maximum, indexed by \(r=n\), is attained by exactly the two constant words. The sharp minimum is \(\binom{n+2}{3}+n+2\), and the sharp maximum is \(\binom{n+2}{3}+\frac{n(n+5)}2\). At \(n=1\), the two words coincide in sphere size because there is only one possible run length.

## Assumptions and scope
The alphabet is binary with fixed-point-free bit complement. The duplication length is exactly one. Errors are sequential and unrestricted, so later errors can duplicate newly inserted letters. The initial word has positive length. The sphere counts unique resulting words of length \(n+3\), not histories; the same terminal word reached via several histories contributes once. We do not claim the formula for alphabets with more than two symbols, other duplication lengths, or four or more operations.

For any nonempty binary word \(u\), abbreviate \(\bar b\) by \(c\), where \(b\) is an arbitrary bit. A length-one duplication of \(u\) at position \(i\) inserts \(\overline{u_i}\) immediately after position \(i\), using zero-based indexing.

## Proof
**Block decomposition.** In a history beginning at \(xb\), descendants of original symbols in \(x\) and of the appended final original symbol \(b\) remain in two consecutive blocks, because each inserted child is placed immediately after its parent, inside the parent's block. Conversely, operations confined to each block can be interleaved arbitrarily. Hence, as sets of words,
\[
D_t(xb)=\bigcup_{s=0}^t D_{t-s}(x)D_s(b),
\]
where set concatenation means all concatenations, not a multiset sum. Also, a one-letter initial word has \(D_1(b)=\{bc\}\), \(D_2(b)=\{bcb,bcc\}\), and \(D_3(b)=\{bcbb,bcbc,bccb,bccc\}\). Here \(c=\bar b\).

**One-step injectivity and the terminal membership lemma.** Distinct positions of a source \(x\) produce distinct single-step outputs: if \(i<j\), position \(j+1\) of the output obtained by duplicating at \(i\) is the original \(x_j\), whereas the output obtained by duplicating at \(j\) has \(\bar x_j\) there. Consequently \(|D_1(x)|=n\), and every one-step descendant of \(x\) contains both bits.

The following sharper membership criterion holds:
\[
xb\bar b\in D_2(x)\quad\Longleftrightarrow\quad x\ne b^n.
\]
If \(x\) ends in \(\bar b\), append \(b\) after its final letter and then \(\bar b\) after the newly appended \(b\). If \(x\) ends in \(b\) but is not constant, locate its last transition \(\bar b\,b\) and duplicate that \(\bar b\), introducing an extra \(b\) immediately before the trailing \(b\)-run; next duplicate the final \(b\), appending \(\bar b\). Both yield \(xb\bar b\). Conversely, when \(x=b^n\), the initial run of \(b\) cannot increase under any positive number of such duplications: the first inserted letter is an opposite symbol, and subsequent insertions cannot move the earliest opposite symbol to the right. Therefore \(xb\bar b\), whose initial \(b\)-run has length \(n+1\), cannot be a descendant. This proves the criterion.

**The exact-two recurrence.** By the block decomposition,
\[
D_2(xb)=D_2(x)b\ \cup\ D_1(x)bc\ \cup\ \{xbcb,xbcc\}.
\]
The first set ends in \(b\), the second in \(bc\) and has \(n\) distinct words, while \(xbcc\) ends in \(cc\) and is new. The word \(xbcb\) belongs to the first set exactly when \(xbc\in D_2(x)\). Write \(I(x,b)=1\) if \(x=b^n\), and zero otherwise. Thus
\[
|D_2(xb)|=|D_2(x)|+n+1+I(x,b).
\]
As \(|D_2(a)|=2\) for a one-letter source, induction gives
\[
|D_2(x)|=\binom{n+1}{2}+r(x).
\]
Notice \(r(xb)=r(x)+I(x,b)\).

**The exact-three recurrence.** The four families furnished by the block decomposition are
\[
\begin{aligned}
A&=D_3(x)b,\\
B&=D_2(x)bc,\\
C_1&=D_1(x)bcb,\\
C_2&=D_1(x)bcc,\\
E&=\{xbcbb,xbcbc,xbccb,xbccc\}.
\end{aligned}
\]
The sets \(A,B,C_2\) are pairwise disjoint because their terminal patterns are respectively \(b\), \(bc\), and \(cc\), and their sizes are respectively \(|D_3(x)|,|D_2(x)|,n\). The fourth family \(C_1\) is contained in \(A\): for \(u\in D_1(x)\), the word \(u\) is nonconstant, so the membership lemma applied to \(u\) gives \(ubc\in D_2(u)\subseteq D_3(x)\), and hence \(ubcb\in A\).

In \(E\), the word \(xbccc\) belongs to none of \(A,B,C_1,C_2\) (compare terminal patterns \(b\), \(bc\), \(bcb\), \(bcc\), respectively), and is always new. If \(x\ne b^n\), the membership lemma gives \(xbc\in D_2(x)\). Duplicating the final \(c\) appends \(b\) and produces \(xbcb\in D_3(x)\), while duplicating the preceding final \(b\) inserts \(c\) and produces \(xbcc\in D_3(x)\). Therefore \(xbcbb\) and \(xbccb\) are already in \(A\), while \(xbcbc\) is in \(B\). If \(x=b^n\), all these three words have an initial \(b\)-run of length \(n+1\) or their membership in \(B\) would require \(xbc\in D_2(x)\); either way they are new. Thus precisely \(1+3I(x,b)\) words of \(E\) remain new, and
\[
|D_3(xb)|=|D_3(x)|+|D_2(x)|+n+1+3I(x,b)
=|D_3(x)|+\binom{n+2}2+r(x)+3I(x,b).
\]
The proposed expression for \(|D_3(x)|\) has base value \(4\) at \(n=r=1\). When appending \(b\), its increment is \(\binom{n+2}2+r(x)\) if \(I=0\), and \(\binom{n+2}2+n+3\) if \(I=1\), because then \(r(x)=n\) and \(r(xb)=n+1\). These are exactly the recurrence increments. Induction proves the boxed formula for every positive \(n\).

**Spectrum.** Consecutive run-indexed values differ by \(n+2-r>0\) for \(r<n\). For \(r<n\), the first symbol has two choices, the next \(r-1\) symbols are forced equal, the following symbol is forced opposite, and the remaining \(n-r-1\) bits are free, giving \(2^{n-r}\) words. For \(r=n\), only the two constant words remain. The claimed extrema follow.

## Verification
The attached `verify_forward.py` independently enumerates all forward histories, deduplicates after each operation and checks every binary source of lengths 1 through 10 (2046 source words). `verify_inverse.py` instead enumerates every received word and repeatedly removes one symbol whose immediate predecessor is its complement, recovering all possible length-\(n\) ancestors after exactly three reverse steps; it independently verifies all 510 binary sources of lengths 1 through 8. Both programs completed and reproduced the full spectrum. These finite computations verify boundary cases and provide reproducible cross-checks, while the block-decomposition recurrences above establish the all-length theorem without relying on finite enumeration.

## Relationship to prior work
The September 1, 2026 manuscript *Coding for Multiple Reverse-Complement and Palindromic Duplications* studies finite error counts and gives the sharp maximum of exact-two spheres for even block lengths. An independently published November 2026 result extends the sharp exact-two maximum to odd block lengths, including one-symbol duplications. A separate prior result determines the **entire exact-two binary one-symbol sphere spectrum** by the initial run length, \(\binom{n+1}2+r(x)\). The present claim is not that earlier exact-two statement: it gives the full exact-**three** sphere spectrum, with a new collision analysis and a second-order term in \(r\). The 2025 full-text article by Yohananov and Schwartz establishes the unbounded-error coding capacity and a one-symbol descendant-cone criterion, not an exact-three fixed-error enumerator. Sun and Ge (2026) construct correction codes for fixed error counts, without providing this source-specific sphere formula in the accessible abstract. The 2021 Ben-Tolila–Schwartz paper addresses expressiveness and one-error correction, and its complete text was not accessible in this review.

## Limitations
The classification is restricted to binary, fixed-length-one reverse-complement duplication and exactly three errors; it does not give optimal correcting code sizes or multi-symbol alphabet spectra. An equivalent theorem in unindexed literature is possible. Independent audit has not been performed. The proof is symbolic; checker runs are additional finite evidence, not its substitute.

## References
1. A. L. Zabokritskiy (Yohananov), *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779, first posted 2026-09-01, https://arxiv.org/abs/2609.00779 .
2. L. Yohananov and M. Schwartz, *On the coding capacity of reverse-complement and palindromic duplication-correcting codes*, Designs, Codes and Cryptography 93 (2025), https://doi.org/10.1007/s10623-025-01627-7 .
3. Y. Sun and G. Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151, first posted 2026-02-01, https://arxiv.org/abs/2602.01151 .
4. E. Ben-Tolila and M. Schwartz, *On the Reverse-Complement String-Duplication System*, arXiv:2112.11811, first posted 2021-12-22, https://arxiv.org/abs/2112.11811 .
5. *Sharp two-step sphere maximum for odd-length reverse-complement duplication*, published research result dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-step-sphere-maximum-for-odd-length-reverse-complement--a03a87770ec6 .
