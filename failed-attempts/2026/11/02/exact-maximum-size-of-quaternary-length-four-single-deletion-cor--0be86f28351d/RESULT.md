# Exact maximum size of quaternary length-four single-deletion-correcting codes

## Finding

Let \(A_4(4,1)\) be the maximum number of length-four words over a four-symbol alphabet for which one deletion can always be corrected, i.e. the sets of distinct length-three deletion descendants of different codewords are disjoint. Then
\[
\boxed{A_4(4,1)=24.}
\]
The upper bound is proved by a fractional packing certificate of weight \(25\) together with an integral parity obstruction that rules out equality. An explicit 24-word code attains the result.

## Assumptions and scope

The alphabet is the labeled set \(\Sigma=\{0,1,2,3\}\). For \(w=w_1w_2w_3w_4\in\Sigma^4\), let
\[
D(w)=\{w_1w_2w_3,w_1w_2w_4,w_1w_3w_4,w_2w_3w_4\},
\]
understood as a **set**, with repeated descendants counted once. A code \(\mathcal C\subseteq\Sigma^4\) is single-deletion-correcting precisely when \(D(u)\cap D(v)=\varnothing\) for all distinct \(u,v\in\mathcal C\). No linearity or algebraic field structure is assumed.

## Proof

**1. A sharp fractional certificate.** Give each word \(y=y_1y_2y_3\in\Sigma^3\) weight
\[
\omega(y)=\begin{cases}
1,&y_1=y_2=y_3,\\
\tfrac12,&y_1=y_2\ne y_3\text{ or }y_1\ne y_2=y_3,\\
\tfrac14,&\text{otherwise}.
\end{cases}
\]
There are respectively \(4\), \(24\), and \(36\) words in these three classes, so
\[
\sum_{y\in\Sigma^3}\omega(y)=4+12+9=25.
\]
For any length-four word \(w\), put \(W(w)=\sum_{y\in D(w)}\omega(y)\). Its value depends only on the equality pattern among the four coordinates. Normalize a pattern by renaming symbols in order of first appearance, so the 15 patterns and values of \(4W\) are

| Pattern | 0000 | 0001 | 0010 | 0011 | 0012 | 0100 | 0101 | 0102 | 0110 | 0111 | 0112 | 0120 | 0121 | 0122 | 0123 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(4W\) | 4 | 6 | 7 | 4 | 5 | 7 | 6 | 5 | 5 | 6 | 5 | 4 | 5 | 5 | 4 |

Thus \(W(w)\ge1\) always, with equality exactly for the four patterns `0000`, `0011`, `0120`, `0123`. The table is independently reproducible by `verify.py`, which enumerates all \(4^4=256\) words in exact rational arithmetic. The table can also be checked directly using the four deletion positions for each equality pattern.

For any correcting code, descendant sets are disjoint. Hence
\[
|\mathcal C|\le\sum_{w\in\mathcal C}W(w)
=\sum_{y\in\bigcup_{w\in\mathcal C}D(w)}\omega(y)
\le25.
\]

**2. Equality at 25 is impossible.** Assume \(|\mathcal C|=25\). Every displayed inequality must be an equality. Therefore every selected word has one of the four tight patterns, and, since every weight \(\omega(y)\) is positive, every length-three word \(y\in\Sigma^3\) occurs in the deletion set of *exactly one* selected codeword.

Fix an outer symbol \(a\in\Sigma\). There are three nonconstant palindromes \(aba\) with \(b\in\Sigma\setminus\{a\}\), and all three must be covered. Among tight four-letter patterns, only `0120` can produce a nonconstant palindrome: a word \(abca\), with \(a,b,c\) pairwise distinct, has the two such descendants \(aba\) and \(aca\), both with the same outer letter \(a\). The other tight patterns `0000`, `0011`, `0123` produce no nonconstant palindrome. Consequently the three palindromes with outer letter \(a\) must be partitioned into blocks of size two, an impossibility. Thus \(|\mathcal C|\le24\).

**3. Attainment.** The following \(24\) four-letter words constitute a code:

```
0000 0011 0022 0033 0213 0320
1010 1111 1122 1133 1230 1321
2031 2102 2200 2211 2222 2233
3012 3103 3232 3300 3311 3333
```

Their pairwise deletion-descendant sets are disjoint; indeed they partition all \(64\) length-three words, making this witness a perfect single-deletion-correcting code. The standalone `verify.py` lists every length-three descendant, asserts absence of a cross-codeword collision, and confirms that the union contains all \(64\) possible length-three words. Therefore \(|\mathcal C|\ge24\), completing the proof.

## Verification

Run `python3 verify.py` using Python's standard library. The program independently regenerates all \(64\) length-three words and \(256\) length-four words, computes exact rational weights, checks the 15 equality patterns and all 24 witness codewords, and validates the special palindrome property used in the parity contradiction. Its exact recorded output is `verification_output.txt`. The upper-bound reasoning is symbolic and does not rely on numerical optimization.

## Relationship to prior work

Kulkarni and Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1 (2012), formulate deletion correction as hypergraph packing. Their Table I(c) at \(q=4,n=4\) reports a fractional-matching upper bound \(25\) and a Tenengolts-family construction of size \(20\). The present exact answer \(24\) rules out equality in that fractional bound and gives an explicit larger packing. Their tabulated LP value is used as a historical comparison, not as a substitute for the certificate above.

Chee, Ge and Ling, arXiv:1008.1343 (2010), consider perfect deletion codes and neighboring parameter regimes, including one deletion at length three and two deletions at length four, not the present four-symbol, length-four, one-deletion optimum. Xie, Sun and Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1 (first public June 13, 2026), study the related but different covering objective. Covering and correction are not interchangeable. The present claim is an exact **packing** optimum, not a covering-code bound.

## Limitations

Only length four, alphabet size four, and exactly one deletion are determined. The argument does not classify all maximum codes, or give a formula for larger blocklengths or alphabet sizes. Complete priority cannot be certified from accessible published literature; an unindexed prior exact computation or construction could exist. Verification is not independent mathematical refereeing.

## References

- A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1, 2012. https://arxiv.org/abs/1211.3128
- Y. M. Chee, G. Ge and S. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, arXiv:1008.1343, 2010. https://arxiv.org/abs/1008.1343
- C. Xie, Y. Sun and G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1, first publicly available 2026-06-13. https://arxiv.org/abs/2606.15379
