# Exact Abelian-agreement depth of iterated tortoise sorting on the Thue–Morse word

## Finding

Let \(\mathbf t=(t_i)_{i\ge0}\) be the binary Thue–Morse word, \(t_i=s_2(i)\bmod2\), where \(s_2(i)\) counts ones in the binary representation of \(i\). Let \(\tau\) be the binary Defant–Kravitz tortoise map: delete the leftmost \(1\) and append a \(1\) (fix an all-zero word). For integer \(k\ge1\), let \(p_k(n)\) be the number of distinct \(\tau^k\)-images of length-\(n\) factors of \(\mathbf t\), and let \(a(n)\) be the number of distinct values of the number of ones in those factors.

**Theorem.** For every integer \(k\ge1\),
\[
 p_k(n)=a(n)\quad(0\le n\le2k),\qquad p_k(2k+1)=3>a(2k+1)=2.
\]
At the first divergent length, the complete image set is
\[
 \bigl\{0^{k+1}1^k,\ 0^k1^{k+1},\ 0^{k-1}10\,1^k\bigr\}.
\]
Consequently, in the notation of Campbell–Rampersad for the last initial length on which iterated tortoise complexity agrees with Abelian complexity,
\[
 \boxed{\operatorname{abel}_{\mathbf t}(k)=2k\quad\text{for every }k\ge1.}
\]

## Assumptions and scope

A factor means a contiguous finite word appearing in the one-sided infinite word \(\mathbf t\); distinct factors are counted once, irrespective of occurrence multiplicity. Factor length \(n\) and number of tortoise iterations \(k\) are integers; \(n\ge0\) and \(k\ge1\). The empty factor has one image and one Abelian class. A binary Abelian class is determined exactly by its number of ones. All equalities are exact, not asymptotic. The theorem determines the first divergence, not the full complexity after that length.

## Proof

**1. Binary tortoise iteration.** Write any binary word having \(m\) ones as
\[
 w=0^{e_0}1\,0^{e_1}1\cdots1\,0^{e_m}.
\]
A single tortoise step removes the first original \(1\) and places it at the right end. If \(m\le k\), then \(\tau^k(w)=0^{|w|-m}1^m\). If \(m>k\), after \(k\) steps the first \(k\) original ones have been shifted right, leaving
\[
 \tau^k(w)=0^{e_0+\cdots+e_k}1\,0^{e_{k+1}}1\cdots1\,0^{e_m}1^k.
\]
In the special case \(m=k+1\), let \(r=e_{k+1}\) be the number of trailing zeros; the identity becomes
\[
 \tau^k(w)=0^{|w|-m-r}1\,0^r1^k.
\]
Thus a word with \(k+1\) ones has its fully sorted image when its last character is \(1\); if it ends in exactly one zero, its image is the sorted zeros and ones interrupted by a single \(10\).

**2. Complementary pairs.** The Thue–Morse recursion gives \(t_{2i}=t_i\) and \(t_{2i+1}=1-t_i\). Every aligned pair \(t_{2i}t_{2i+1}\) therefore contains one \(1\). An odd-length factor of length \(2j+1\) consists of \(j\) complete aligned pairs and one extra symbol, hence contains \(j\) or \(j+1\) ones. An even-length factor of length \(2j\) starting at an even position has exactly \(j\) ones. Starting at position \(2i+1\), it has
\[
 (1-t_i)+(j-1)+t_{i+j}=j+t_{i+j}-t_i
\]
ones. It contains \(j+1\) ones only when \(t_i=0\) and \(t_{i+j}=1\); in that case its final character is \(1\).

**3. Equality through length \(2k\).** When \(n<2k\), the pair counts in Step 2 show that every factor contains at most \(k\) ones, so Step 1 sorts every factor completely. For \(n=2k\), a factor contains at most \(k+1\) ones. Any factor containing \(k+1\) ones starts at an odd position and ends in \(1\), by Step 2. Step 1 again shows its \(k\)-fold tortoise image is completely sorted. Therefore, at every length \(0\le n\le2k\), each factor has the image uniquely prescribed by its number of ones. Since tortoise preserves that number, \(p_k(n)=a(n)\).

**4. Exact first divergence and witnesses.** A length-\((2k+1)\) factor has either \(k\) or \(k+1\) ones, because it comprises \(k\) complete aligned pairs and one extra symbol. If it has \(k\) ones, its image is \(0^{k+1}1^k\). If it has \(k+1\) ones, its rightmost \(1\) is in one of the final two positions: an even-starting high-weight factor ends in \(1\), and an odd-starting factor ends with an aligned complementary pair. Step 1 shows that its image is one of \(0^k1^{k+1}\) and \(0^{k-1}10\,1^k\).

All three displayed images occur. Choose an integer \(r\) with \(2^r>k\) and \(r\equiv s_2(k-1)\pmod2\), and put \(i=2^r-k\). The binary identity \(i=(2^r-1)-(k-1)\) gives \(s_2(i)=r-s_2(k-1)\), so \(t_i=0\); also \(t_{i+k}=t_{2^r}=1\). The factor of length \(2k+1\) starting at \(2i\) has \(k\) aligned pairs followed by \(t_{i+k}=1\), hence \(k+1\) ones and last symbol \(1\), yielding the sorted high-weight image. The factor of the same length starting at \(2i+1\) begins with \(1-t_i=1\), is followed by \(k\) aligned pairs, and ends in the complementary pair \(10\) because \(t_{i+k}=1\). It has \(k+1\) ones and yields \(0^{k-1}10\,1^k\). Finally, an even-starting factor ending with \(t_{j+k}=0\) has exactly \(k\) ones and yields \(0^{k+1}1^k\); such \(j\) exist because \(t\) contains zeros. The three images are distinct. Hence \(p_k(2k+1)=3\), while \(a(2k+1)=2\). Together with Step 3, this proves the theorem.

## Verification

The self-contained `verify.py` exhaustively compares the direct \(k\)-fold operator with its deleted-prefix formula on every binary word of lengths one through eleven, across \(49{,}150\) tested word/iterate pairs. It independently constructs the complete factor sets at a fixed length by expanding all four adjacent source pairs under a sufficient Thue–Morse substitution power, justified by the constant-length block decomposition. It checks the two lengths \(2k\) and \(2k+1\) for each \(1\le k\le128\), checks all lengths at most \(2k\) for \(1\le k\le20\), and checks the explicit witness coordinates and images. Run `python3 verify.py`; the stored `verification-output.txt` records the successful result. These finite checks supplement, and do not replace, the all-integer proof above.

## Relationship to prior work

Defant and Kravitz introduced the word-sorting operator. Campbell and Rampersad define the iterated tortoise complexity and the initial Abelian-agreement length; their 2026 paper computes one-step complexities and explicitly asks for the corresponding Thue–Morse agreement-depth sequence. The present theorem answers that precise all-iterate question by a linear formula and identifies all images at the first failure. The same paper's one-pass complexity theorem does not imply the all-iterate initial cutoff without additional reasoning. Previously published studies of two-pass Thue–Morse image deficits at large factor lengths and maximum two-pass fiber cardinality address different quantities and do not state this all-\(k\) result. The classical Thue–Morse complementary-pair identity is used as a premise and is not claimed as new.

## Limitations

The claim is specific to the binary Thue–Morse word and the Defant–Kravitz tortoise operation. It does not classify later divergences, nor arbitrary automatic words. The proof is elementary in the complementary-pair identity; other formulations may already imply the numerical cutoff. An unindexed equivalent result remains a publication-priority risk.

## References

1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, first publicly submitted April 28, 2026, especially Definitions 1–2 and Section 7. https://arxiv.org/html/2604.25811v3
2. C. Defant and N. Kravitz, *Stack-sorting for Words*, arXiv:1809.09158, first submitted September 24, 2018. https://arxiv.org/abs/1809.09158
3. *Exact two-tortoise complexity of the Thue–Morse word from length eighteen*, published-finding corpus public research record, November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-two-tortoise-complexity-of-the-thue-morse-word-from-length--d15dd17f32d1
4. *Exact maximal two-tortoise fiber spectrum of Thue–Morse factors*, published-finding corpus public research record, November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-maximal-two-tortoise-fiber-spectrum-of-thue-morse-factors--5c1539333494
