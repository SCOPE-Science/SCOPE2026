# Dyadic two-binomial rigidity of the period-doubling word

## Finding

Let \(\mathbf p=p(0)p(1)\cdots\) be the binary period-doubling fixed point defined by \(0\mapsto01\), \(1\mapsto00\). For every integer \(k\ge1\), put \(N=2^k\). The map
\[
 u\longmapsto\left(|u|_1,\ \sum_{\substack{0\le j<N\\u(j)=1}}j\right)
\]
is injective on the set \(\mathcal F_{\mathbf p}(N)\) of distinct length-\(N\) contiguous factors. Consequently, if \(b_{\mathbf p,r}(N)\) denotes the number of equivalence classes of these factors under equality of all scattered-subsequence counts of orders at most \(r\), and \(P_{\mathbf p}(N)=|\mathcal F_{\mathbf p}(N)|\), then
\[
 \boxed{b_{\mathbf p,1}(2^k)=2,\qquad b_{\mathbf p,2}(2^k)=P_{\mathbf p}(2^k)=3\cdot2^{k-1}\quad(k\ge1).}
\]
Thus two scattered-subsequence statistics, the number of ones and the number of scattered occurrences of `01`, distinguish every dyadic-length factor, although the number of ones alone takes only two values. The minimal separating binomial order at every such length is exactly two. At length one all three complexities are two.

This assertion is restricted to dyadic lengths. In particular, distinct length-five factors `10001` and `01010` both have two ones and sum of one-positions four; hence they are two-binomially equivalent.

## Assumptions and scope

All positions are zero-based. For a binary integer word \(u=u(0)\cdots u(N-1)\), write \(m(u)=\sum_j u(j)\), \(S(u)=\sum_j j u(j)\), and \(\binom{u}{v}\) for the number of occurrences of \(v\) as an increasing-index subsequence of \(u\). Two words are \(r\)-binomially equivalent if these counts agree for every binary word of length at most \(r\). This differs from \(r\)-abelian equivalence, which counts contiguous factors.

The fixed-point symbol identity is
\[
 p(n)=\nu_2(n+1)\pmod2,
\]
where \(\nu_2\) is the two-adic valuation on positive integers. Equivalently, \(p(2j)=0\) and \(p(2j+1)=1-p(j)\). No probabilistic assumption or computationally obtained infinite certificate is used.

## Proof

**1. Complete dyadic factor language.** Fix \(k\ge1\), let \(N=2^k\), and define
\[
 V_k=p(0)p(1)\cdots p(N-2),\qquad W_k^a=V_ka\quad(a\in\{0,1\}).
\]
For any \(q\ge0\), the aligned block \(p(qN)\cdots p((q+1)N-1)\) equals \(W_k^{a(q)}\), where
\[
 a(q)=\bigl(k+\nu_2(q+1)\bigr)\pmod2.
\]
Indeed, for \(0\le j<N-1\), the valuation of \(qN+j+1\) equals the valuation of \(j+1\). The final position has valuation \(k+\nu_2(q+1)\). Both endpoint values occur (take \(q=0\) and \(q=1\)). If a length-\(N\) factor starts at \(qN+r\), \(0\le r<N\), it consists of the last \(N-r\) letters of one aligned block followed by the first \(r\) letters of the next. Both blocks have prefix \(V_k\); since \(r\le N-1\), this factor is the left cyclic rotation by \(r\) of \(W_k^{a(q)}\). Conversely every rotation of each of the two words occurs in this way. Thus
\[
 \mathcal F_{\mathbf p}(N)=\operatorname{Rot}(W_k^0)\sqcup\operatorname{Rot}(W_k^1),
\]
where the union is disjoint since the words have weights differing by one.

**2. Primitive and doubled blocks.** The initial words are \(W_1^0=00\), \(W_1^1=01\). For \(k\ge2\), put \(e=(k-1)\bmod2\). The valuation identity gives
\[
 W_k^a=W_{k-1}^{e}W_{k-1}^a.
\]
Therefore \(W_k^e=(W_{k-1}^e)^2\), while the word \(W_k^{1-e}\) has odd weight, because the two level-\(k-1\) words differ only in their final bit:
\[
 m(W_k^{1-e})=2m(W_{k-1}^{e})+1-2e.
\]
At level one the nondoubled word \(W_1^1\) has odd weight. At each successive level, \(W_{k-1}^{e}\) is exactly the preceding level's nondoubled, odd-weight word. A binary word of power-of-two length and odd weight cannot be a proper power: any repetition multiplicity would divide both its length and its weight. Hence the nondoubled level-\(k\) word has \(N\) distinct rotations, and the doubled level-\(k\) word has exactly \(N/2\) distinct rotations. This proves
\[
 P_{\mathbf p}(N)=N+N/2=3N/2.
\]
The two weights \(m(W_k^0)\) and \(m(W_k^1)\) differ by one, proving \(b_{\mathbf p,1}(N)=2\).

**3. A first-moment criterion for two-binomial equivalence.** For a length-\(N\) binary word of weight \(m\), the number of scattered `01` subsequences is
\[
 \binom{u}{01}=S(u)-\binom{m}{2}.
\]
Indeed, each one at position \(j\) has \(j\) preceding positions, of which the preceding ones account in total for \(\binom m2\). The other order-two counts are \(\binom{u}{00}=\binom{N-m}{2}\), \(\binom{u}{11}=\binom{m}{2}\), and \(\binom{u}{10}=m(N-m)-\binom{u}{01}\). Therefore, at fixed length, two-binomial equivalence is **equivalent** to equality of \((m,S)\).

**4. Separation of all rotations.** Let \(z\) be a binary word of length \(H=2^h\) with odd weight \(m\). If \(R_dz\) is its left rotation by \(d\) places and \(t\) is the number of ones in its first \(d\) positions, then
\[
 S(R_dz)-S(z)=Ht-dm.
\]
If the moments agree, coprimality of \(H\) and odd \(m\) forces \(H\mid d\). Thus every two distinct rotations have different moments.

For the odd-weight (nondoubled) branch \(W_k^{1-e}\), this applies with \(H=N\). For the doubled branch at \(k\ge2\), \(W_k^e=UU\) with \(|U|=N/2\) and \(m(U)\) odd; every distinct rotation has the form \((R_dU)^2\), and
\[
 S\bigl((R_dU)^2\bigr)=2S(R_dU)+(N/2)m(U).
\]
The moments therefore also distinguish its \(N/2\) distinct rotations. Rotations belonging to different branches have unequal weights, and so cannot be two-binomially equivalent. The asserted injectivity and class count follow. For \(k=1\), the doubled word is `00` with only one distinct rotation, while the odd-weight word `01` has two rotations with different moments.

**5. Boundary at length five.** Both `10001` and `01010` occur (for instance at starts one and four). Each has weight two and moment four, so they are distinct but two-binomially equivalent. The theorem does not claim separation at arbitrary non-dyadic lengths.

## Verification

Run `python3 verify.py` in the same directory. The dependency-free verifier enumerates every dyadic factor from both complete aligned-block families for \(0\le k\le11\), compares exact weights and moments, checks the formula \(P_{\mathbf p}(2^k)=3\cdot2^{k-1}\) for \(k\ge1\), confirms the two weight classes, checks further positions and direct scattered-pair counts at small levels, and validates the length-five collision. Expected diagnostic summary:

`VERIFY_OK levels=0..11 windows_checked=24570 pair_checks=47 five_factor_collision=confirmed`

The complete infinite proof is Steps 1–4, not this finite run.

## Relationship to prior work

Lejeune, Leroy and Rigo (arXiv:1812.07330, initially submitted 2018-12-18) classify the binomial complexity of the **Thue–Morse** word, which eventually takes bounded values for any fixed binomial order. Lejeune, Rigo and Rosenfeld (2019) establish equality of two-binomial and factor complexities for **all lengths** of the **Tribonacci** word; the word and mechanism differ here. Lü, Chen, Wen and Wu (arXiv:2112.05347, initially submitted 2021-12-10) determine the two-binomial complexity of generalized, Parikh-constant Thue–Morse words, not this non-Parikh-constant period-doubling morphism. Parreau, Rigo, Rowland and Vandomme (arXiv:1405.3532) analyze **two-abelian complexity** for the same period-doubling word, using counts of **contiguous** length-two factors, which are not the scattered counts used here. Rigo, Stipulanti and Whiteland (arXiv:2201.04603) establish general results about binomial complexity for Parikh-collinear morphisms and several other families; the period-doubling images `01` and `00` have linearly independent Parikh vectors, so that bounded-complexity theory does not imply the present result. Vivion (arXiv:2509.11172) establishes global two-binomial reconstruction for four classes of words; the period-doubling word fails global reconstruction already at length five and is not covered by those hypotheses.

Richomme (arXiv:2510.07159) gives a general geometric description of binary two-binomial classes and explicitly notes the pre-existing identity relating scattered `01` counts and the sum of one-positions. Those identities are used, not claimed as new here; the result of this note is their sharp restriction to the dyadic factor language of the period-doubling word.

Thus the new claim is a dyadic-length, scattered-subsequence reconstruction theorem for the period-doubling word. No cited theorem's stated hypotheses directly imply it. Neither bibliographic searches nor the comparisons documented in the associated review prove absence of unindexed equivalent results.

## Limitations

The proof covers the exact dyadic lengths and no assertion of global two-binomial rigidity is made. The length-five example shows that extension to arbitrary lengths is false. The result does not characterize non-dyadic two-binomial complexity or any higher-order binomial spectrum. Diagnostic tests through the indicated finite lengths are not substituted for the symbolic proof. The scientific comparison is not an independent audit; an unindexed or differently formulated equivalent result remains possible.

## References

1. M. Lejeune, J. Leroy, M. Rigo, *Computing the k-binomial complexity of the Thue--Morse word*, arXiv:1812.07330, first public 2018-12-18. https://arxiv.org/html/1812.07330v1
2. M. Lejeune, M. Rigo, M. Rosenfeld, *Templates for the k-binomial complexity of the Tribonacci word*, WORDS 2019. https://orbi.uliege.be/bitstream/2268/240049/1/tribonacci.pdf
3. X.-T. Lü, J. Chen, Z.-X. Wen, W. Wu, *On the 2-binomial complexity of the generalized Thue-Morse words*, arXiv:2112.05347, first public 2021-12-10. https://arxiv.org/abs/2112.05347
4. A. Parreau, M. Rigo, E. Rowland, É. Vandomme, *A new approach to the 2-regularity of the ell-abelian complexity of 2-automatic sequences*, arXiv:1405.3532, first public 2014-05-14. https://arxiv.org/abs/1405.3532
5. M. Rigo, M. Stipulanti, M. A. Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, arXiv:2201.04603, first public 2022-01-12. https://arxiv.org/abs/2201.04603
6. L. Vivion, *New examples of words for which the binomial complexities and the subword complexity coincide*, arXiv:2509.11172, first public 2025-09-14. https://arxiv.org/abs/2509.11172
7. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159, first public 2025-10-08. https://arxiv.org/abs/2510.07159
