# Complete joint cyclic window-weight profiles of lexicographic first-order Reed–Muller codes

## Finding

For every integer \(m\ge1\), put \(n=2^m\). In the specified natural binary-index order, the binary code \(C_m=\mathrm{RM}(1,m)\) contains \(2^{m+1}\) codewords but realizes exactly \(2^{m-1}+2\) **distinct joint cyclic window-weight vectors**
\[
\bigl(W_1(w),W_2(w),\ldots,W_n(w)\bigr).
\]
Exactly two vectors have multiplicity one, exactly one has multiplicity two, and exactly \(2^{m-1}-1\) have multiplicity four. The singletons come from the all-zero and all-one codewords, and the doubleton comes from the two alternating codewords. This joint statement concerns all window lengths **on the same word**; separate marginal weight enumerators do not determine it.

More precisely, every nonconstant codeword has a cyclic multiset of zero-run lengths consisting of \(2^k-2t\) copies of \(r\) and \(t\) copies of \(2r\), with parameters
\[
0\le s<m,\quad r=2^s,\quad k=m-s-1,\quad
\begin{cases}
t=0,&k=0,\\
0\le t\le2^{k-1},&k\ge1.
\end{cases}
\]
If a displayed multiplicity is zero, that run length is absent. Thus for all \(1\le b\le n\), simultaneously,
\[
W_b(w)=n-(2^k-2t)\max(r-b+1,0)-t\max(2r-b+1,0).
\]
For a fixed \((s,t)\), the number of codewords is twice the coefficient of \(z^t\) in
\[
(1+z)(1+z+\cdots+z^{2^{k-1}-1}),\qquad k\ge1,
\]
and is two when \(k=0\). Different parameter pairs can represent the same pure-run vector; these coincidences are explicitly resolved in the proof.

## Assumptions and scope

The coordinate of \(w_{a,c}\in C_m\) at position \(0\le i<n\) is
\[
w_{a,c}(i)=c+\sum_{j=0}^{m-1} a_j i_j\pmod2,
\]
where \(a_j,c,i_j\in\{0,1\}\) and \(i_j\) is the \(j\)-th **least significant** binary digit of \(i\). A length-\(b\) cyclic window starting at \(i\) examines \(i,i+1,\ldots,i+b-1\) modulo \(n\); it has nonzero weight if at least one symbol is nonzero. Define \(Z_b(w)=n-W_b(w)\), the number of all-zero cyclic windows of length \(b\). In the nonconstant case, every zero-run has length at most \(n/2\). Multiplicity counts distinct codewords, not equivalence classes under coordinate permutations, reversal, or complement.

## Proof

**1. Reduction to complementary pairs.** Take a nonconstant affine word and put \(s=\min\{j:a_j=1\}\), \(r=2^s\), and \(k=m-s-1\). The word is obtained by replacing each symbol in a binary word \(h\) of length \(2^{k+1}\) by \(r\) consecutive copies. Write \(g\) for the affine truth table of the coefficients above \(s\), indexed by \(k\) bits. Consecutive symbols of \(h\), grouped into \(2^k\) pairs, satisfy
\[
(h_{2j},h_{2j+1})=(c+g_j,c+g_j+1)\pmod2.
\]
Every pair contains exactly one zero, so every zero-run in \(h\) has length one or two. A run of length two occurs across the boundary between pairs \(j\) and \(j+1\) exactly when \((c+g_j,c+g_{j+1})=(1,0)\), with indices taken cyclically. Denote the number of these transitions by \(t\). Since \(h\) contains exactly \(2^k\) zeros, it has \(t\) runs of length two and \(2^k-2t\) of length one. Repetition by \(r\) proves the advertised zero-run multiset.

**2. Exact cyclic transition enumeration.** For \(k=0\), the complementary pair is the whole reduced cyclic word, and \(t=0\). Suppose \(k\ge1\). Write the coefficients of \(g\) as \(d_0,\ldots,d_{k-1}\), and put \(q_j=d_0+\cdots+d_j\pmod2\). The map \((d_j)_j\mapsto(q_j)_j\) is invertible. On incrementing a \(k\)-bit integer, a carry through the first \(j\) bits flips the value of \(g\) precisely when \(q_j=1\). For \(0\le j<k-1\), this carry pattern occurs \(2^{k-j-1}\) times; for the last carry pattern, counting both the final ordinary increment and the cyclic wrap-around gives \(2\) occurrences. Thus the total number of toggles around the full cycle is
\[
T=\sum_{j=0}^{k-2}2^{k-j-1}q_j+2q_{k-1}.
\]
Every cyclic binary sequence has equally many upward and downward changes, so \(t=T/2\). Consequently
\[
t=\sum_{j=0}^{k-2}2^{k-j-2}q_j+q_{k-1}.
\]
As \((q_j)\) varies freely, the generating polynomial for \(t\) is
\[
P_k(z)=\prod_{e=0}^{k-2}(1+z^{2^e})(1+z)
=(1+z)(1+z+\cdots+z^{2^{k-1}-1}).
\]
The empty product convention covers \(k=1\). Its coefficients are one at the endpoints \(0\) and \(2^{k-1}\), and two at every intermediate integer. The independent constant term \(c\) doubles each multiplicity. There are therefore precisely two codewords for each endpoint \(t\), and four for each interior \(t\), at fixed \(s\).

**3. Recovering the run data from the full signature.** If the cyclic zero-runs have positive lengths \(\ell\), then
\[
Z_b(w)=\sum_{\text{zero-runs}}\max(\ell-b+1,0).
\]
For a nonconstant word, the number of runs of length exactly \(b\) is the second finite difference
\[
\nu_b=Z_b-2Z_{b+1}+Z_{b+2},
\]
where \(Z_{n+1}=Z_{n+2}=0\) by convention. Hence the complete joint window-weight vector uniquely determines the multiset of zero-run lengths and vice versa. Substituting the counts obtained in step 1 proves the all-\(b\) formula.

**4. Collisions and multiplicities.** For \(k\ge2\), an interior parameter \(0<t<2^{k-1}\) gives both run lengths \(r\) and \(2r\) with positive multiplicity. Its shortest run determines \(s\), and the number of longer runs determines \(t\), so no such mixed profile is duplicated. It occurs four times. At \(t=0\) there are \(2^k\) runs of the single length \(r\), whereas at \(t=2^{k-1}\) there are \(2^{k-1}\) runs of the single length \(2r\). The latter is the same pure-run profile as \(t=0\) at index \(s+1\); these are the **only** collisions between different \((s,t)\). There are \(m\) distinct pure-run lengths, \(2^0,2^1,\ldots,2^{m-1}\) on the dyadic scale. The length-one profile is realized twice (the two alternating words), while each other pure-run profile is realized four times (two descriptions, two choices of \(c\) each). The number of mixed profiles is
\[
\sum_{k=2}^{m-1}(2^{k-1}-1)=2^{m-1}-m,
\]
with the empty sum interpreted as zero for \(m=1,2\). Thus there are \(m+(2^{m-1}-m)=2^{m-1}\) distinct nonconstant joint profiles. Add the all-zero and all-one words, which have joint weights \((0,\ldots,0)\) and \((n,\ldots,n)\), respectively, and cannot equal a nonconstant profile because \(W_1=n/2\) for every nonconstant word. The multiplicities are exactly those stated. This also checks the total \(2+2+4(2^{m-1}-1)=2^{m+1}\) codewords.

## Verification

The standalone Python script `code/check_profiles.py` independently enumerates every affine truth table and its cyclic zero-run lengths for dimensions \(1\le m\le8\). It checks the **entire joint distribution**, including individual multiplicities, against the closed form. A separate direct cyclic-window scan independently verifies every marginal enumerator for every \(1\le b\le2^m\), for \(1\le m\le7\). These are finite consistency tests, not substitutes for the all-dimensions proof. Run `python3 code/check_profiles.py`; only the standard Python library is required.

## Relationship to prior work

Ma and Luo (2019) computed symbol-pair and \(b\)-symbol weight distributions for simplex and related rearranged codes. Their cyclic simplex constructions have distinct coordinate sets/orderings from the full affine truth-table code of length \(2^m\) considered here, and their enumerators are marginal rather than complete joint signatures. Shi, Zhu, and Helleseth (2021) gave the general run-length identity linking cyclic \(b\)-symbol weights to zero-runs, used in step 3; that identity **is not claimed as new**. Zhu and Shi (2022) studied irreducible cyclic code distributions, also not the ordered full first-order Reed–Muller family. The contribution here is the infinite-family **joint** profile classification, the two-scale dyadic zero-run law, and the exact sizes of every profile fibre.

## Limitations

The ordering of the affine evaluation coordinates is essential; arbitrary coordinate permutations need not preserve these signatures. This result gives neither a general theorem for higher-order Reed–Muller codes nor new claims about simplex codes. Computational checks stop at the explicitly stated finite dimensions. Searches of relevant literature cannot establish absolute worldwide novelty; the comparisons in the review state their coverage limits.

## References

1. Junru Ma and Jinquan Luo, *Symbol-pair Weight Distributions of Some Linear Codes*, arXiv:1911.02184, first posted 2019-11-06, https://arxiv.org/abs/1911.02184.
2. Minjia Shi, Hongwei Zhu and Tor Helleseth, *The connections among Hamming metric, b-symbol metric, and r-th generalized Hamming metric*, arXiv:2109.13764, first posted 2021-09-28, https://arxiv.org/abs/2109.13764.
3. Hongwei Zhu and Minjia Shi, *The b-symbol weight distribution of irreducible cyclic codes and related consequences*, arXiv:2203.11567, first posted 2022-03-22, https://arxiv.org/abs/2203.11567.
4. Gerardo Vega, *The b-symbol weight distributions of all semiprimitive irreducible cyclic codes*, Designs, Codes and Cryptography 91 (2023), 2213–2221, first published 2023-03-01, https://doi.org/10.1007/s10623-023-01193-w.
