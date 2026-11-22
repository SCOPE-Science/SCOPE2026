# Exact eight-one enumeration of prefix-normal binary palindromes

## Finding

Write \(P_8(n)\) for the number of **indexed** binary palindromes of length \(n\) containing exactly eight ones and satisfying the prefix-normal property: for every length \(\ell\), the prefix of length \(\ell\) contains at least as many ones as any contiguous factor of length \(\ell\). For every integer \(n\ge8\),

\[
\boxed{\sum_{n\ge8}P_8(n)z^n=\frac{z^8}{1-z^7}\left(\frac{1}{(1-z)(1-z^2)^2}-\frac{z^2}{(1-z^2)(1-z^3)(1-z^4)}\right).}
\]

Equivalently, all such words are precisely
\[
1\,0^a1\,0^b1\,0^c1\,0^d1\,0^c1\,0^b1\,0^a1,
\qquad a,b,c,d\in\mathbb Z_{\ge0},
\]
with the four sharp conditions
\[
a\le b,\quad a\le c,\quad a\le d,\quad a+b\le c+d.
\]
There are no such palindromes of length less than eight. As \(n\to\infty\),
\[
P_8(n)=\frac5{1008}n^3+O(n^2),\qquad
\frac{P_8(n)}{\binom{\lfloor n/2\rfloor}{4}}=\frac{40}{21n}+O(n^{-2}).
\]
The second formula is the probability that a uniformly sampled binary palindrome with exactly eight ones is prefix normal.

## Assumptions and scope

Words are finite, linear, and indexed: no quotient by reversal, rotation, or alphabet complementation is taken. A palindrome is a word equal to its reversal; zero-runs may be empty. The prefix-normal property is with respect to ones. Counts use ordinary length \(n\), rather than half-length. The alphabet is \(\{0,1\}\), with exactly eight occurrences of \(1\).

## Proof

**Step 1: binary gap criterion.** Let a binary word begin with one and have \(r\) ones. Write its inter-one zero-run lengths as \(g_1,\ldots,g_{r-1}\). The word is prefix normal if and only if, for every \(1\le j\le r-1\) and every \(1\le i\le r-j\),
\[
\sum_{h=1}^j g_h\le\sum_{h=i}^{i+j-1}g_h.
\]
Indeed, an interval contains \(j+1\) ones if and only if its length is at least one plus the span of some \(j+1\) consecutive ones; the shortest such span is \(j+\sum g_h\) over the corresponding \(j\) gaps. If the first span is minimal for all \(j\), every factor with \(k\) ones is at least as long as the shortest prefix containing \(k\) ones, establishing prefix normality. Conversely, a shorter later span immediately gives a factor whose number of ones exceeds the equally long prefix. Comparisons for \(j=r-1\) are tautological.

**Step 2: palindrome reduction.** A nonzero prefix-normal word must begin with \(1\); palindromicity forces it to end with \(1\). With eight ones its seven inter-one gaps are \((a,b,c,d,c,b,a)\). For the one-gap comparisons, the complete requirements are \(a\le b\), \(a\le c\), \(a\le d\). The nontrivial two-gap comparisons add only \(a+b\le c+d\); the comparison with \(b+c\) reduces to \(a\le c\). For three gaps the possible nontrivial comparisons reduce to \(a\le d\) or \(a+b\le c+d\). For four and five gaps they reduce to \(a\le b\) or \(a\le c\); six gaps are tautological. Thus the four stated inequalities are necessary and sufficient, including equality and zero-gap boundaries.

**Step 3: exact series.** Write \(a=t,\ b=t+x,\ c=t+y,\ d=t+v\). The first three inequalities are equivalent to \(t,x,y,v\ge0\), and the remaining one is \(x\le y+v\). Every such tuple defines one distinct word of length \(8+7t+2x+2y+v\). Summing all nonnegative tuples gives
\[
\frac{z^8}{(1-z^7)(1-z^2)^2(1-z)}.
\]
The excluded tuples have \(x=y+v+1+k\) with \(y,v,k\ge0\), and have total series
\[
\frac{z^{10}}{(1-z^7)(1-z^4)(1-z^3)(1-z^2)}.
\]
Subtracting gives the boxed formula, an identity of formal power series for all \(n\ge8\).

**Step 4: sharp density.** At \(z=1\), the two summands have leading terms \(\frac1{28}(1-z)^{-4}\) and \(\frac1{168}(1-z)^{-4}\). Hence their difference is \(\frac5{168}(1-z)^{-4}+O((1-z)^{-3})\). Every other pole of the rational series is a root of unity of order at most three in its pole multiplicity, so coefficient extraction yields \(P_8(n)=\frac5{1008}n^3+O(n^2)\). Since an eight-one binary palindrome has a zero center if its length is odd, and its left half contains exactly four ones, there are exactly \(\binom{\lfloor n/2\rfloor}{4}=n^4/384+O(n^3)\) such palindromes. Division gives the conditional probability \(\frac{40}{21n}+O(n^{-2})\).

## Verification

The standalone programs `checks/verify_bruteforce.py` and `checks/verify_gap.py` are included. The first enumerates every binary palindrome containing eight ones at each length from 8 through 24 and directly checks every prefix against every factor; its counts match the generating function. The second compares the four inequalities with all sliding-gap inequalities for all \(8^4=4096\) gap quadruples, and independently checks every series coefficient from length 8 through 120 by an integer solution count. All reported checks passed. These finite checks corroborate but do not replace the four-step all-length proof.

The first coefficients \(P_8(8),\ldots,P_8(24)\) are \(1,1,2,3,5,5,8,10,13,15,20,23,28,32,39,44,52\).

## Relationship to prior work

Burcsi, Fici, Lipták, Ruskey and Sawada defined and studied binary prefix-normal words and generation algorithms in the 2014 literature. Their later treatment of fixed-density enumeration establishes rationality for the full prefix-normal-word class and gives concrete formulas at small densities, without restricting to palindromes. Fleischmann, Kulczynski and Nowotka explicitly investigate *prefix-normal palindromes* and their aggregate counts, but neither their enumerator nor the aggregate sequence specifies the fixed-eight-one subseries, its gap polyhedral criterion, or its conditional rare-event constant. Generic prefix-normal gap comparisons supply an ingredient; the coupled middle-gap inequality, exact rational subtraction and conditional asymptotics here require an additional specialization.

## Limitations

This theorem concerns only exactly eight ones, not arbitrary content, and does not determine the total number of prefix-normal palindromes at each length. Its leading constant is conditional on uniform fixed-weight palindromes and does not describe arbitrary random binary words. Although the cited and searched sources do not state the same eight-one series, an equivalent older representation or unindexed fixed-weight table could still exist; historical priority is not independently certified. The programs verify finite domains, while the proof establishes the infinite statement.

## References

1. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, and J. Sawada, *On Combinatorial Generation of Prefix Normal Words*, arXiv:1401.6346, first public January 24, 2014. https://arxiv.org/abs/1401.6346
2. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, and J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, first public November 28, 2016. https://arxiv.org/abs/1611.09017
3. P. Fleischmann, M. Kulczynski, D. Nowotka, and D. B. Poulsen, *On Collapsing Prefix Normal Words*, arXiv:1905.11847, first public May 28, 2019. https://arxiv.org/abs/1905.11847
4. OEIS A308465, *Number of prefix normal palindromes of length n*, https://oeis.org/A308465 (aggregate-length data, not fixed-composition counts).
