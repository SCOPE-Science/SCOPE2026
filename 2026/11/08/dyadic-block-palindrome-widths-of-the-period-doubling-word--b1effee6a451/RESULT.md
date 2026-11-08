# Dyadic block-palindrome widths of the period-doubling word

## Finding

Let \(p=p(0)p(1)\cdots\) be the binary period-doubling fixed point of the morphism \(\mu(0)=01\), \(\mu(1)=00\), indexed from zero, and put \(P_k=p(0)p(1)\cdots p(2^k-1)\) for every integer \(k\geq0\). A **block-palindrome factorization** of a nonempty finite word is a decomposition
\[
U=B_t B_{t-1}\cdots B_1 C B_1\cdots B_{t-1}B_t,
\]
where every \(B_j\) is nonempty, the two copies of each \(B_j\) are literally equal (not reversed), and the central block \(C\) may be empty. The **width** is \(2t+\mathbf 1_{\{C\ne\varepsilon\}}\). Define \(L_k\) as the maximum width of such a decomposition of \(P_k\).

**Theorem.** For all integers \(m\geq0\),
\[
\boxed{L_{2m}=L_{2m+1}=\frac{2\cdot4^m+1}{3}.}
\]
For \(m\geq1\), the unique maximum-width factorization of \(P_{2m}\) consists of mirrored outer blocks of length one or two and the central word \(10\). That of \(P_{2m+1}\) is obtained by applying \(\mu\) to every block, with central word \(0001\). For \(m=0\), the corresponding central words are \(0\) and \(01\).

In particular, the widths normalized by the lengths of the dyadic prefixes have two distinct limits:
\[
\lim_{m\to\infty}\frac{L_{2m}}{2^{2m}}=\frac23,
\qquad
\lim_{m\to\infty}\frac{L_{2m+1}}{2^{2m+1}}=\frac13.
\]

## Assumptions and scope

The symbol \(\nu_2(j)\) is the ordinary exponent of two in a positive integer \(j\). The word has the equivalent digit-valuation description
\[
p(i)=\nu_2(i+1)\bmod 2\qquad(i\geq0).
\]
All claims concern **the particular dyadic prefixes** \(P_k\), not all factors of the infinite word and not arbitrary prefix lengths. Blocks in a block palindrome agree in the same orientation; replacing them by reversals would define another invariant. The maximum is over all finite mirrored block decompositions with an optional unpaired central block.

## Proof

**1. Shortest-border optimality.** A border of a word \(U\) is a nonempty proper prefix also occurring as suffix. The shortest border \(B\), when present, is unbordered: a shorter border of \(B\) would be a shorter border of \(U\). Consequently, its prefix and suffix occurrences cannot overlap; hence \(2|B|\leq |U|\). In a candidate factorization whose outermost repeated block is a longer border \(D\), the word \(B\) is both a prefix and suffix of \(D\), and the two occurrences of \(B\) inside \(D\) cannot overlap. Thus \(D=BVB\) for a possibly empty \(V\). Refining both outer blocks \(D\) into \(B,V,B\) (or into \(B,B\) when \(V\) is empty) strictly increases the number of blocks, a contradiction. Therefore each outer block of the maximum-width factorization is the shortest border of the remaining central word. Repeatedly removing equal shortest borders determines its unique maximum-width factorization; stop at an unbordered center.

**2. Even exponents.** Fix \(m\geq1\), write \(n=2^{2m}\), and let \(h=n/2\). For integers \(a\) with \(1\leq a<n\), the elementary valuation identity \(\nu_2(n-a)=\nu_2(a)\) gives
\[
p(n-1-a)=\nu_2(a)\bmod2,
\qquad p(n-1)=0.
\]
The first and last letters of \(P_{2m}\) are both \(0\), so the greedy decomposition first removes the one-letter border \(0\), leaving the symmetric boundary at \(a=1\).

Now let \(j\) run through \(1\leq j\leq h/2-1\), and suppose the next left boundary is \(a=2j-1\). The rightmost letter of the central remainder is \(p(n-1-a)=0\), whereas its leftmost letter is \(p(a)=\nu_2(2j)\bmod2\). If this valuation is even, the shortest border is a single \(0\); the next boundary \(a+1=2j\) also has matching leftmost and rightmost letters \(0\), since \(p(2j)=0\) and \(p(n-1-2j)=\nu_2(2j)\bmod2=0\). This group of two indices therefore supplies **two** paired length-one blocks.

If instead \(\nu_2(2j)\) is odd, the first letters disagree, but the two-letter prefix and suffix of the remaining word are both \(10\):
\[
p(a)p(a+1)=10,
\qquad p(n-2-a)p(n-1-a)=10.
\]
Thus the shortest border has length two, and this group supplies **one** paired length-two block. In either case the next boundary is \(a=2j+1\). This proves inductively that all these groups are processed exactly as stated and that the rightmost letter of every visited central remainder is \(0\).

After the final group, the boundary is \(a=h-1\), so the two-letter center is
\[
p(h-1)p(h)=10.
\]
This word is unbordered, and the greedy procedure stops.

There are \(h/2-1\) groups. Let \(T\) count those with odd \(\nu_2(2j)\), equivalently with even \(\nu_2(j)\). Writing \(h=2^{2m-1}\), exact valuation counting gives
\[
T=\sum_{s=0}^{m-2}2^{2m-3-2s}=\frac{h-2}{3},
\]
where the sum is empty and zero when \(m=1\). The number of matched *pairs* of outer blocks is therefore
\[
1+2\left(\frac h2-1\right)-T
=h-1-\frac{h-2}{3}=\frac{2h-1}{3}.
\]
Including the nonempty center proves
\[
L_{2m}=2\cdot\frac{2h-1}{3}+1=\frac{2n+1}{3}.
\]

**3. Odd exponents.** From the valuation identity,
\[
p(2j)=0,\qquad p(2j+1)=1-p(j),
\]
so \(\mu(p(0)\cdots p(n-1))=p(0)\cdots p(2n-1)\); in particular, \(P_{2m+1}=\mu(P_{2m})\).

For every intermediate central factor \(X\) encountered in the greedy factorization of \(P_{2m}\), its last symbol is \(0\), as proved above (also true for \(P_0=0\)). In \(\mu(X)\), every even-indexed symbol is \(0\), but the last symbol is \(1\). A border of odd length is impossible: its prefix would end at an even index and hence end in \(0\), while its suffix would end in \(1\). Every border of even length \(2d\) in \(\mu(X)\) corresponds exactly to a border of length \(d\) in \(X\), because \(\mu\) is length-two, aligned, and injective (\(01\ne00\)). Accordingly the greedy border lengths in \(\mu(P_{2m})\) are exactly twice those in \(P_{2m}\), and their number is unchanged. The central factor \(10\) maps to \(0001\); for \(m=0\), the center \(0\) maps to \(01\). Therefore \(L_{2m+1}=L_{2m}\). The base case \(P_0=0\) has \(L_0=1\), completing the theorem for all \(m\geq0\).

**4. Limits.** Substitute the exact formula and the prefix lengths \(4^m\) and \(2\cdot4^m\) into the two ratios. Taking \(m\to\infty\) gives \(2/3\) and \(1/3\), respectively.

## Verification

The included standalone file `verify.py` uses ordinary Python 3, no dependencies, and is run with `python3 verify.py`. It independently constructs the word from integer valuations, greedily compares every candidate border, computes the valuation-predicted block sequences, and tests morphic doubling. It also exhaustively optimizes the width over **all possible non-overlapping outer borders** for dyadic prefixes through length \(256\), and for all \(2046\) nonempty binary words of lengths at most ten. It tests the exact formula for all \(0\leq k\leq13\), including a prefix of length \(8192\). The actual result was:

`VERIFY_OK dyadic_levels=14 max_prefix=8192 full_optimum_levels=9 all_binary_words=2046 border_steps=8172`

These tests are finite diagnostics only; the preceding argument supplies the all-exponents proof.

## Relationship to prior work

Goto, I, Bannai and Inenaga introduced and analyzed block-palindrome factorizations, including the shortest-border greedy characterization of the largest factorization [1]. Gabrić and Shallit developed enumeration and extremal results for shortest and largest block-palindrome factorizations of arbitrary finite words [2]. The present proof specializes the same invariant to every dyadic period-doubling prefix and derives a new closed form and a two-limit oscillation using the exact two-adic valuation structure. Neither [1] nor [2] states or implies that numerical specialization without the valuation analysis.

Barro, Kaboré and Bognini determined palindromic Ziv–Lempel and palindromic Crochemore factorizations for period-doubling words [3]. Their factors are selected by novelty or earlier occurrence of palindromes, not by mirrored equality of shortest borders around a central remainder, so these decompositions do not give the present width formula. Other studies of the same sequence and its attractors use different invariants. No equivalently covering theorem was identified in the examined primary texts or targeted mathematical-record searches; absence from the searches does not prove global novelty.

## Limitations

The explicit widths are proved only for dyadic prefixes. No assertion is made about longest block-palindrome widths of arbitrary factors or arbitrary prefix lengths. Plausible residual bibliographic risk remains from unindexed results and related string-factorization work; the 2022 period-doubling paper was read via accessible extracted text, but its direct page-image service was unavailable.

## References

[1] K. Goto, T. I, H. Bannai and S. Inenaga, *Block Palindromes: A New Generalization of Palindromes*, arXiv:1806.00198 (2018), https://arxiv.org/abs/1806.00198 .

[2] D. Gabrić and J. Shallit, *Smallest and Largest Block Palindrome Factorizations*, arXiv:2302.13147 (first posted 2023-02-25), https://arxiv.org/abs/2302.13147 .

[3] M. Barro, I. Kaboré and K. E. Bognini, *On the palindromic zl-factorization and c-factorization of the generalized period-doubling sequences*, Australasian Journal of Combinatorics 83 (2022), 435–447, https://ajc.maths.uq.edu.au/pdf/83/ajc_v83_p435.pdf .
