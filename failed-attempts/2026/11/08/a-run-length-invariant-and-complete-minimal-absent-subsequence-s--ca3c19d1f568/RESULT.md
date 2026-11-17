# A run-length invariant and complete minimal-absent-subsequence spectrum for periodic binary words

## Finding

Fix the ordered binary alphabet \(\Sigma=\{0,1\}\). For every integer \(r\ge2\), \(k\ge1\), let \(W_{r,k}=(0^r1)^k\). A *minimal absent scattered subsequence* (MAS) of \(W_{r,k}\) is a nonempty binary word \(v\) which is not a subsequence of \(W_{r,k}\), although deleting any one occurrence of a letter from \(v\) produces a subsequence of \(W_{r,k}\). Let \(m_r(k,\ell)\) count distinct such words of length \(\ell\), not their embeddings.

For each fixed integer \(r\ge2\), the full bivariate generating function is

\[
\boxed{F_r(z,t)=\sum_{k\ge1}\sum_{\ell\ge1}m_r(k,\ell)z^kt^\ell
=\frac{zt\bigl(t^r+2t-2t^{r+1}z+2t^{r+2}z\bigr)}{1-(t+t^r)z+(t^{r+1}-t^{r+2})z^2}.}
\]

In particular, the total number is **independent of the zero-run length**:

\[
\boxed{\sum_{\ell\ge1}m_r(k,\ell)=3\cdot2^{k-1}\quad(r\ge2,\ k\ge1).}
\]

This is a sharp distinction from the alternating case \(r=1\), whose minimal-absence totals begin \(3,5,9,16\), rather than \(3,6,12,24\). For example, when \(r=2\), the first three length spectra are \(2t^2+t^3\), \(2t^3+t^4+3t^5\), and \(2t^4+t^5+5t^6+4t^7\).

## Assumptions and scope

The ambient alphabet is always binary; a subsequence is scattered, allowing arbitrary gaps but preserving order. Length counts identify words, not choices of matching positions. Both parameters \(r\) and \(k\) range over all integers in the stated domain. The formal variable \(z\) marks the number of complete blocks \(0^r1\) and \(t\) marks the absent word's length. The result concerns finite host words and is an exact, all-parameter identity; no asymptotic or statistical assumptions enter.

## Proof

**1. A greedy bridge criterion.** Let \(H\) be a finite binary word of length \(N\), and let \(v=v_1\cdots v_m\), with \(m\ge2\). Greedily match \(v_1\cdots v_{m-1}\) at positions \(i_1<\cdots<i_{m-1}\) of \(H\), numbered from one, with \(i_0=0\). Then \(v\) is an MAS precisely when all three statements hold:

- the greedy prefix match exists;
- \(v_m\) does not occur after position \(i_{m-1}\);
- for each \(2\le j\le m\), the letter \(v_j\) occurs in the interval \(H[i_{j-2}+1:i_{j-1}]\).

For sufficiency, after deleting \(v_j\), embed the preceding letters at their greedy positions and embed each subsequent letter \(v_s\) into the preceding greedy interval \((i_{s-2},i_{s-1}]\). These intervals occur in the necessary order, and the last letter is covered by the final bridge interval. The second statement gives absence of the undeleted word. For necessity, if a bridge letter \(v_j\) were missing from \((i_{j-2},i_{j-1}]\), deleting \(v_{j-1}\) would force the greedy match of \(v_j\) strictly beyond \(i_{j-1}\); all subsequent matches would be no earlier than the corresponding original greedy matches, so the last letter would still be absent, contradicting minimality. This is also the interval characterization of Kosche--Koß--Manea--Siemer (2021), with its hypotheses made explicit here.

**2. Reachable states of a periodic greedy embedding.** Let \(P=(0^r1)^\omega\) and \(L=r+1\). The cursor is the zero-based index of the next unscanned position in \(P\). Each greedily consumed interval ends with the newly matched symbol. To satisfy the bridge condition, the next letter must belong to the set of letters in that interval. Only the following states are reachable after one or more letters of an MAS prefix, for \(r\ge2\):

- \(A_j\), \(1\le j\le r\): cursor congruent to \(j\pmod L\), and last consumed interval contains only \(0\);
- \(D\): cursor congruent to \(1\pmod L\), and last interval contains both symbols;
- \(B\): cursor congruent to \(0\pmod L\), and last interval contains both symbols.

The first input \(0\) leads to \(A_1\), consuming no complete period; the first input \(1\) leads to \(B\), consuming one period. Subsequent allowed transitions, labeled by the matched symbol and the number of newly crossed complete periods, are exactly

\[
B\xrightarrow{0,0}A_1,\quad B\xrightarrow{1,1}B,\quad
A_j\xrightarrow{0,0}A_{j+1}\ (1\le j<r),\quad
A_r\xrightarrow{0,1}D,\quad
D\xrightarrow{0,0}A_2,\quad D\xrightarrow{1,1}B.
\]

To check exhaustiveness, from a cursor within the \(r\) zeros, a forced next zero usually advances one position; from the residue of the following \(1\), the next zero skips that \(1\), producing state \(D\). A next \(1\) is allowed only from a previously mixed interval, namely \(B\) or \(D\). Consequently a hypothetical state with only \(1\) in the consumed interval is unreachable. The restriction \(r\ge2\) is used in the transition \(D\xrightarrow{0,0}A_2\).

**3. Exactly which paths are terminal.** The finite host \(W_{r,k}\) is the first \(kL\) symbols of \(P\). An MAS arises when its complete greedy match in \(P\) first passes the boundary \(kL\), while its penultimate greedy match lies on or before it. At state \(B\), if \(a\ge1\) periods have been completed, either next symbol \(0\) or \(1\) crosses the boundary at \(aL\); these are two terminal choices for \(k=a\). At state \(A_r\), if \(a\ge0\) periods have been completed, the forced next zero skips the intervening \(1\) and crosses the boundary at \((a+1)L\); this is the single terminal choice for \(k=a+1\). No transition from \(A_j\) for \(j<r\) or from \(D\) crosses a boundary strictly. These conditions are necessary and sufficient by Step 1. A word determines a unique greedy path, so this enumeration does not overcount.

**4. Weighted path generating functions.** Attach weight \(t\) to each new letter and \(z\) to each completed block. Let \(b,d,a_1,\ldots,a_r\) count legal accepting continuations from the corresponding states, including the terminal choices but not the initial matched letter. The exact equations are

\[
\begin{aligned}
b&=2t+t a_1+tzb,\\
d&=t a_2+tzb,\\
a_j&=t a_{j+1}\quad(1\le j<r),\\
a_r&=tz(1+d).
\end{aligned}
\]

The two initial choices yield \(F_r=t a_1+tzb\). Solving these equations gives

\[
b=\frac{2t-t^{r+1}z}{1-(t+t^r)z+(t^{r+1}-t^{r+2})z^2}
\]

and, upon substitution, the displayed rational function for \(F_r\). The expressions are formal power series in \(z\); each coefficient has a finite polynomial in \(t\). Setting \(t=1\) cancels the parameter \(r\) and leaves

\[
F_r(z,1)=\frac{3z}{1-2z}=\sum_{k\ge1}3\cdot2^{k-1}z^k,
\]

which proves the claimed invariance for all parameters, without extrapolation from finite computation.

## Verification

The included standalone standard-library script `verify.py` independently generates all binary candidates and tests every single-letter deletion against the literal finite host, with no reliance on the state graph. It compares the resulting MAS sets with the grammar-derived enumeration for \((r,k)\) in \(r=2,1\le k\le7\); \(r=3,1\le k\le4\); \(r=4,1\le k\le3\); \(r=5,1\le k\le3\); and \(r=6,1\le k\le2\). It also compares length spectra against exact coefficients of the stated rational function for \(r\in\{2,3,4,5,6,8,12\}\) and \(1\le k\le16\). All 131 parameter/spectrum comparisons passed, including 11,133,114 directly enumerated candidate words. Independent symbolic elimination of the displayed state equations yielded identical numerator and denominator. These computations corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work

Kosche, Koß, Manea and Siemer (arXiv:2108.13968, first posted 2021-08-31) proved a general greedy-interval characterization of minimal absent scattered subsequences; their Theorem 3.1 supplies a useful baseline. Their Proposition 3.8 concerns the permutation-block family, with each symbol appearing once per block; the repeated-zero blocks here are not within that class and their text does not state this two-parameter spectrum or the run-length-invariant total. The present proof reconstructs the greedy criterion and specializes it to a four-type finite transition graph.

Manea, Ringleb, Siemer and Winkler (arXiv:2504.21471) provide general efficient enumeration algorithms, but do not state the all-parameter formula for these repeated-zero blocks. Adamson et al. (arXiv:2407.18599) optimize counts of *all* absent subsequences of a prescribed length, which is different from the minimal-absent antichain counted here. Troníček's 2023 chapter studies counting algorithms for minimal absent subsequences; its complete text could not be inspected, so overlap with an unindexed example remains a documented bibliographic risk.

## Limitations

The theorem does not cover the alternating case \(r=1\), arbitrary binary periods, or contiguous minimal absent **factors**. It provides exact finite counts but does not claim a new general-purpose enumeration algorithm. Full equivalence with inaccessible or unindexed literature has not been ruled out; independent scientific audit has not been performed.

## References

1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first public posting 2021-08-31. https://arxiv.org/abs/2108.13968
2. F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, 2025. https://arxiv.org/abs/2504.21471
3. D. Adamson et al., *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599, 2024. https://arxiv.org/abs/2407.18599
4. Z. Troníček, *On Problems Related to Absent Subsequences*, COCOA 2023, pp. 351–363, DOI:10.1007/978-3-031-49614-1_26. https://doi.org/10.1007/978-3-031-49614-1_26
