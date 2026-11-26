# Fixed-composition subsequence-universality enumerator for binary palindromes

## Finding

For a finite binary word \(w\), let \(\iota(w)\) be the greatest integer \(k\geq0\) for which every binary word of length \(k\) occurs as a scattered subsequence of \(w\). The alphabet is **fixed as** \(\{0,1\}\), including for constant or empty words. Let \(p_{n,j,k}\) be the number of binary palindromes of length \(n\), with exactly \(j\) ones and universality index \(k\). Then the complete joint generating function is

\[
\boxed{\displaystyle
\Phi(x,y,u)=\sum_{n,j,k\ge0}p_{n,j,k}x^ny^ju^k
=\frac{1-y^2x^4+x(1+y)\bigl(1+(u-1)yx^2-uy^2x^4\bigr)}
{1-(1+y^2)x^2+y^2(1-2u^2)x^4+u^2y^2(1+y^2)x^6}.}
\]

This is an identity of formal power series in \(x\) with coefficients in \(\mathbb Z[y,u]\), valid at every length and every Hamming weight. The coefficient \([x^ny^ju^k]\Phi\) is the exact count without any identification under complementation or a further symmetry. As a nonminimal-length example, among the \(70\) palindromes of length \(16\) and weight \(8\), the numbers at universality indices \(2,4,6,8\) are respectively \(2,16,36,16\), with all other indices absent.

## Assumptions and scope

Words have finite length \(n\ge0\) over the labeled binary alphabet. A palindrome equals its reversal as a linear word, not a necklace. A scattered subsequence retains the order of chosen positions but need not be contiguous. By convention the empty word has index zero, and index zero also applies to nonempty words missing one of the two binary symbols. The three variables \(x,y,u\) mark length, number of ones, and universality index. There is no bound on the parameters \(n,j,k\) other than those forced by the definitions.

## Proof

**1. Greedy arches.** Read an arbitrary half-word \(h\) from left to right and cut immediately after the first occurrence of both binary letters, then restart. Each completed piece (an *arch*) is uniquely either \(0^a1\) or \(1^a0\) with \(a\ge1\); the leftover *rest* is empty or a single constant run. If there are \(r\) completed arches, then \(\iota(h)=r\). Indeed, selecting one letter of a prescribed length-\(r\) subsequence from each arch shows \(r\)-universality. Conversely, the arch-terminal letters followed by a symbol absent from the rest form an absent subsequence of length \(r+1\): greedy terminal positions can only be matched at or after their arch ends. This includes \(r=0\).

**2. The center rule.** The established palindrome-arch criterion (Barker, Fleischmann, Harwardt, Manea, Nowotka, *Scattered Factor-Universality of Words*, Proposition 15) gives

\[
\iota(hh^{\mathrm R})=2r,\qquad
\iota(hch^{\mathrm R})=2r+\mathbf1\{\operatorname{rest}(h)\ne\varepsilon,
\ c\notin\operatorname{alph}(\operatorname{rest}(h))\},
\]

for every center \(c\in\{0,1\}\), with the fixed-alphabet zero-arch boundary verified directly. In the binary case the indicator says exactly that the nonempty constant rest and the center have opposite letters. To see why the rule holds, the \(r\) complete arches on each side yield \(2r\) complete blocks, and any extra complete block must straddle the center. Since no half alone admits \(r+1\) complete blocks, an extra block is possible precisely when the middle rest together with the center contains both letters.

**3. Joint weights.** In the palindrome, one letter in \(h\) contributes twice to its total length and twice to its number of ones. Thus a completed arch, counted together with its reversed partner, contributes the generating polynomial

\[
H=u^2y^2x^4\left(\frac1{1-x^2}+\frac1{1-y^2x^2}\right).
\]

The two summands count the arches \(0^a1\) and \(1^a0\), respectively. Since successive arches are free choices, the factor for any finite sequence of arches is \((1-H)^{-1}\).

For even palindromes the optional remainder is empty, \(0^a\), or \(1^a\), hence its generating function is

\[
R=1+\frac{x^2}{1-x^2}+\frac{y^2x^2}{1-y^2x^2}.
\]

The even-length contribution is \(E=R/(1-H)\).

For odd palindromes, with a single central bit, there are three disjoint remainder cases. An empty rest allows center \(0\) or \(1\) with weight \(x(1+y)\). A positive zero rest allows center zero (no additional arch) or center one (one additional arch), giving \(x(1+yu)x^2/(1-x^2)\). A positive one rest similarly gives \(x(y+u)y^2x^2/(1-y^2x^2)\). The odd-length contribution is therefore

\[
O=\frac{x\left((1+y)+(1+yu)\frac{x^2}{1-x^2}+(y+u)\frac{y^2x^2}{1-y^2x^2}\right)}{1-H}.
\]

Set \(D=(1-x^2)(1-y^2x^2)-u^2y^2x^4(2-(1+y^2)x^2)\). Then \(E=(1-y^2x^4)/D\) and

\[
O=\frac{x(1+y)(1+(u-1)yx^2-uy^2x^4)}{D}.
\]

Adding the disjoint even and odd cases and expanding \(D\) proves the displayed rational expression. Every step is an exact word-to-weight bijection, so no finite test or limiting argument is needed.

## Verification

The companion standalone program `VERIFY.py` computes coefficients of the rational function using its cleared polynomial denominator and independently enumerates every binary palindrome through length \(20\), classifying each by length, Hamming weight, and its greedy-arch universality index. It matches all coefficient triples in this range. Through length \(12\), it additionally checks each universality index by explicit enumeration of **all** binary scattered subsequences of every candidate length, without using the arch-counting algorithm. Its completion marker is `VERIFY_OK_GF_ALL_COMPOSITION_LENGTHS_0_20_SUBSEQ_INDEPENDENT_0_12`. These computations are checks, not a substitute for the all-length proof.

## Relationship to prior work

Karandikar, Kufleitner, and Schnoebelen investigate Simon's congruence, defined through sets of scattered subwords, and count congruence classes, rather than the present palindromic, composition-refined universality classes. Barker and collaborators' Proposition 15 already supplies the key **per-word palindrome center rule**; that rule is not claimed to be new. The present contribution is the exact trivariate enumeration after counting the two compositions of binary arches and the composition-sensitive central cases. The later \(\alpha\)-\(\beta\) factorization literature analyzes scattered-subword equivalence, not this displayed joint generating function. A published unweighted binary universality-index law concerns all binary words, not palindromes stratified by Hamming weight. Existing shortest palindromic universal-word constructions determine a minimum-length edge of the distribution, not all its composition strata.

## Limitations

The formula is for the labeled binary alphabet and linear palindromes only; it is not asserted for larger alphabets or necklaces. It enumerates universality-index classes rather than complete Simon-congruence classes. The per-word palindrome rule is explicitly prior work, and an equivalent composition-refined generating function could exist under different terminology in literature not indexed by the searches. No independent scientific audit has been performed.

## References

1. P. Karandikar, M. Kufleitner, P. Schnoebelen, *On the index of Simon's congruence for piecewise testability*, arXiv:1310.1278, initial public posting October 3, 2013; https://arxiv.org/abs/1310.1278.
2. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629, March 10, 2020, especially Proposition 15; https://arxiv.org/abs/2003.04629.
3. P. Fleischmann, J. Höfer, A. Huch, D. Nowotka, *\(\alpha\)-\(\beta\)-Factorization and the Binary Case of Simon's Congruence*, arXiv:2306.14192, 2023; https://arxiv.org/abs/2306.14192.
