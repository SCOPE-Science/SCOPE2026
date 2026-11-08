# Exactly three minimal unique substrings in finite Stewart choral words

## Finding

Let \(\varphi\) be the binary uniform morphism \(\varphi(0)=001\), \(\varphi(1)=011\), and let \(W_k=\varphi^k(0)\). For every integer \(k\ge2\), set \(m=3^{k-1}\). The word \(W_k\), of length \(3m\), has **exactly three minimal unique substrings (MUSs)**. Using zero-based starting positions and lengths, the complete set is

\[
\left\{\left(m-1,\frac{m+3}{2}\right),\quad
\left(\frac{11m-3}{6},\frac{2m}{3}+1\right),\quad
\left(\frac{5m-1}{2},\frac{m}{3}+1\right)\right\}.
\]

No other nonempty factor occurrence of \(W_k\) is a MUS. In particular, the number of MUSs stays equal to three while the word length tends to infinity. The two-sided minimality condition is essential: an occurrence is a MUS precisely when its factor occurs once, but its length-one-shorter prefix and suffix each occur at least twice.

## Assumptions and scope

All words are finite, binary, and indexed from zero; \(W_0=0\). An interval \([i,j]\) includes both endpoints. Occurrences may overlap. A factor of length one has the empty word as both proper prefix and suffix, which occurs repeatedly under the standard convention; the theorem begins at \(k=2\), so this convention does not affect the three exhibited MUSs.

Write
\[
 c=\frac{m-1}{2},\quad C=m+c=\frac{3m-1}{2},\quad
 a=\frac{11m+3}{6},\quad b=\frac{m+3}{6},\quad
 d=\frac{5m-1}{2},\quad N=3m.
\]
Every displayed quantity used as a position is an integer for \(m=3^{k-1}\) and \(k\ge2\).

## Proof

**1. Single-flip block structure.** Let \(A=\varphi^{k-1}(0)\), \(B=\varphi^{k-1}(1)\). The two words differ at exactly one index, their common center \(c=(m-1)/2\): at the first substitution \(001\) and \(011\) differ at their center, and every subsequent substitution transfers a single discrepancy to the middle position of its image. Also,
\[
W_k=AAB.
\]
The last letter of each nonempty morphic image is \(1\); thus \(A\) ends in \(1\). The first \(c\) letters of \(A,B\) agree, and their last \(m-c-1\) letters agree.

**2. Four repeated intervals.** Each of the following inclusive position intervals in \(W_k\) has a second occurrence of exactly the same factor:
\[
\begin{array}{c|c|l}
\text{interval}&\text{other occurrence interval}&\text{reason}\\
[0,C-1]&[m,d-1]&A A B\text{ and agreement before the flipped center}\\
[m,d-1]&[0,C-1]&\text{the same equality}\\
[a,a+m-2]&[b,b+m-2]&\text{the induction below}\\
[d+1,N-1]&[c+1,m-1]&\text{agreement after the flipped center}.
\end{array}
\]
Call these \(I_0,I_1,I_2,I_3\), in the indicated order. The third equality has length \(m-1\) and follows by induction on \(k\). For \(k=2\), \(W_2=001001011\), \(a=6\), \(b=1\), and the two factors of length two are both \(01\). In the next iterate, the corresponding parameters satisfy \(a'=3a-1\), \(b'=3b-1\), and \(m'=3m\). A factor of length \(3m-1\) starting at \(3a-1\) consists of the final symbol \(1\) of the preceding image block, the image under \(\varphi\) of the length-\(m-1\) factor at \(a\), and the initial symbol \(0\) of the next image block. The same decomposition holds at \(3b-1\). The inductive equality therefore survives as \(1\varphi(u)0=1\varphi(u)0\). This proves all four repeated-factor identities for every \(k\ge2\).

Their left and right endpoints are each strictly increasing. They cover all \(N\) positions: the first overlaps the second, the second overlaps the third, and the third meets or overlaps the fourth, including the \(m=3\) boundary case. Any factor wholly within one of these intervals repeats, so it cannot be unique.

**3. Interval bridge lemma.** Suppose inclusive intervals \(I_j=[L_j,R_j]\) have strictly increasing left and right endpoints and together cover \([0,N-1]\). If a factor-occurrence interval \(J\) is not contained in any \(I_j\), choose the largest \(j\) with \(L_j\le\min J\). As \(J\) is not contained in \(I_j\), its right endpoint is at least \(R_j+1\). As \(j\) is maximal, its left endpoint is at most \(L_{j+1}-1\). The last interval cannot be chosen because it ends at \(N-1\). Thus \(J\) contains the bridge \([L_{j+1}-1,R_j+1]\) for some adjacent pair. Applied to our four intervals, the only three bridges are
\[
U_0=W_k[m-1\ldots C],\qquad
U_1=W_k[a-1\ldots d],\qquad
U_2=W_k[d\ldots a+m-1].
\]
Their respective start positions and lengths are exactly the three pairs in the Finding. Deleting the last letter from a bridge leaves a factor inside its left repeated interval, and deleting the first letter leaves one inside its right repeated interval. Therefore each bridge is a MUS as soon as its occurrence is known to be unique. Moreover, every unique factor contains at least one of these bridges; hence **if all bridges are unique**, no other MUS can exist, because any strictly larger unique factor then has a proper unique subfactor.

**4. Recognizability of occurrences.** In an image \(\varphi(v)\), any length-three factor starting at a position congruent to \(0,1,2\) modulo three belongs respectively to the disjoint sets
\[
\{001,011\},\qquad\{010,110\},\qquad\{100,101\}.
\]
Consequently the residue of an occurrence start is determined by its first three symbols. The middle letter of an image block encodes its source symbol. Therefore, for any factor \(u\) of length at least two, occurrences of the trimmed image \(T(u)=\varphi(u)[1\ldots 3|u|-2]\) in \(\varphi(v)\) are in bijection with occurrences of \(u\) in \(v\), via \(i\mapsto3i+1\): such an occurrence necessarily starts at residue one, and its complete sequence of image-block middle letters reconstructs \(u\). Conversely every source occurrence yields the trimmed-image occurrence. The same principle applies to \(\varphi(u)\) with its final symbol removed, now at starts congruent to zero modulo three.

**5. The first bridge is unique.** Set \(P_k=W_k[0\ldots c]\), the prefix of length \((m+1)/2\). It occurs at exactly positions \(0\) and \(m\) in \(W_k\). For \(k=2\), \(P_2=00\), whose only starts in \(001001011\) are \(0,3\). The recurrence
\[
P_{k+1}=\varphi(P_k)\text{ with its final symbol removed}
\]
combined with the three disjoint residue classes above shows that all occurrences at the next level are exactly three times the previous starts: the trimmed image includes every source image-block middle letter, so no extra aligned occurrences occur. Thus the only starts are \(0\) and \(3m\) at level \(k+1\). Now \(U_0=1P_k\), since the preceding block \(A\) ends with \(1\). The occurrence of \(P_k\) at position zero cannot be preceded by a letter, while the one at \(m\) is preceded by \(1\). Hence \(U_0\) occurs only at \(m-1\).

**6. The remaining bridges are unique.** The formulas for \(a,d,m\) imply
\[
 U_1^{(k+1)}=T(U_1^{(k)}),\qquad
 U_2^{(k+1)}=T(U_2^{(k)}).
\]
Indeed the next starts and ends are respectively \(3(a-1)+1\), \(3d+1\), and \(3d+1\), \(3(a+m-1)+1\). At \(k=2\) the bridges are \(U_1^{(2)}=101\) and \(U_2^{(2)}=11\), each occurring exactly once in \(001001011\). The trimmed-image occurrence bijection proves that both remain unique at every later level. Together with Steps 2–5 and the bridge lemma, this proves the theorem. \(\square\)

## Verification

The accompanying standalone `verify.py` reconstructs the morphic words for \(2\le k\le9\) (lengths \(9\) through \(19683\)); obtains each suffix's longest common prefix with a distinct suffix using a rank-doubling suffix array and Kasai longest-common-prefix calculation; and enumerates all MUSs using the prefix/suffix repetition criterion. For \(k\le4\) it independently recomputes MUSs by a direct factor-occurrence search. Every level matches the three predicted starts and lengths. The script also checks all four repeated-factor intervals, the single-flip structure, the prefix occurrence starts, and the trimmed-image recurrences. Expected terminal marker: `STEWART_CHORAL_MUS_VERIFY_OK`.

These finite checks are supporting diagnostics, not an infinite proof. The interval-cover induction, synchronization argument, and preservation of uniqueness in Steps 1–6 establish the claim for every integer \(k\ge2\).

## Relationship to prior work

Stewart's choral word and its substitution are classical; see the OEIS entry A116178 and the treatment by Fici and Shallit. Fici and Shallit (2021) study a larger class of Stewart words, notably their critical exponent, avoidance, palindromes, subword complexity, and common factors. Kishi, Guo, Urbina and Bannai (2026) study occurrence-preserving morphisms and classify MUSs of finite Fibonacci and Thue–Morse words. The present theorem concerns a different specific fixed point and an exact three-MUS classification of its canonical finite substitution iterates. The occurrence argument here is derived explicitly for trimmed images and does not assert that the untrimmed substitution is globally occurrence-preserving for arbitrary factors.

## Limitations

The claim concerns only the exact iterates \(\varphi^k(0)\), not every finite prefix, every Stewart word, or arbitrary three-uniform substitutions. The theorem does not classify the minimal unique factors of the infinite limit itself (where 'unique in an infinite word' is a different notion). Independent mathematical validation and exhaustive historical-priority confirmation have not been performed. A previously unindexed equivalent MUS classification remains a possible priority risk.

## References

1. K. Kishi, P. Guo, C. Urbina and H. Bannai, *On Occurrence-Preserving Morphisms*, arXiv:2605.18034v1, first posted 2026-05-18, https://arxiv.org/abs/2605.18034 .
2. G. Fici and J. Shallit, *Properties of a Class of Toeplitz Words*, arXiv:2112.12125v1, first posted 2021-12-22, https://arxiv.org/abs/2112.12125 .
3. OEIS A116178, *Stewart's choral sequence*, https://oeis.org/A116178 .
