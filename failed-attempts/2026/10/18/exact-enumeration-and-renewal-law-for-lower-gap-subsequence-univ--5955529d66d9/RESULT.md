# Exact enumeration and renewal law for lower-gap subsequence universality

## Finding
Fix an alphabet \(\Sigma\) of \(q\ge2\) symbols and integers \(g\ge1\), \(k\ge1\). A word \(w\) is *\(g\)-spaced \(k\)-universal* if every pattern in \(\Sigma^k\) can be read at positions \(i_1<\cdots<i_k\) satisfying \(i_{r+1}-i_r\ge g+1\). Let \(U_{q,g,k}(n)\) be the number of such \(n\)-letter words. Define the rational power series
\[
A_q(t)=\frac{q!t^q}{\prod_{j=1}^{q-1}(1-jt)}.
\]
Then, as an identity of formal power series,
\[
\boxed{\sum_{n\ge0}U_{q,g,k}(n)t^n=\frac{A_q(t)^k(qt)^{g(k-1)}}{1-qt}.} \tag{1}
\]
In particular, deleting the prescribed \(g\)-letter spacers in the canonical decomposition gives an exact \(q^{g(k-1)}\)-to-one map from the \(g\)-spaced \(k\)-universal length-\(n\) words onto ordinary \(k\)-subsequence-universal length-\(n-g(k-1)\) words, whenever this set is nonempty.

Put \(I_g(w)=\max\{k\ge0:w\text{ is }g\text{-spaced }k\text{-universal}\}\), with the empty pattern universal. If \(N_{q,g}(n,j)=|\{w\in\Sigma^n:I_g(w)=j\}|\), their **complete bivariate distribution** is
\[
\boxed{\sum_{n,j\ge0}N_{q,g}(n,j)t^nu^j=\frac{1-A_q(t)+uA_q(t)(1-(qt)^g)}{(1-qt)(1-uA_q(t)(qt)^g)}.} \tag{2}
\]
The minimum length is \(qk+g(k-1)\), and the words attaining it consist of \(k\) independently chosen permutations of the alphabet separated by \(k-1\) arbitrary \(g\)-letter spacers. Thus their exact number is \((q!)^kq^{g(k-1)}\). At one position beyond this minimum, the number is
\[
(q!)^kq^{g(k-1)}\frac{q((q-1)k+2)}2.
\]
For a uniformly random infinite i.i.d. source over \(\Sigma\), the universality index of its first \(n\) letters satisfies almost surely
\[
\lim_{n\to\infty}\frac{I_g(W_1\cdots W_n)}n=\frac{1}{qH_q+g},\qquad H_q=\sum_{a=1}^q\frac1a.
\]
This last limit measures the achievable length of an arbitrary prescribed pattern under compulsory minimum spacing.

## Assumptions and scope
The alphabet is the full ambient \(q\)-letter alphabet, not the observed support of an individual word. All words, including the empty word, are counted. A position gap means at least \(g\) **unselected** intervening positions; no upper gap bound is imposed. The parameters \(q,g,k\) are fixed positive integers in the stated ranges; equations (1)–(2) are exact for all word lengths, not only asymptotic statements. The case \(g=0\) is recovered by the same proof but represents the classical model, rather than the new positive-gap claim. Formulas involving the minimum length are understood for \(k\ge1\).

## Proof
**Step 1: the first-arch equivalence.** Given a finite word \(w\), let \(e_a\) be the first occurrence of \(a\in\Sigma\). If some symbol is absent, the word is not universal for any positive pattern length. Otherwise set \(r=\max_{a\in\Sigma}e_a\). The prefix ending at position \(r\) is the unique shortest prefix containing the alphabet; call it the first *arch* \(P\). Its final symbol occurs for the first time precisely at position \(r\).

For any \(k\ge2\), we assert that \(w\) is \(g\)-spaced \(k\)-universal if and only if the suffix beginning at position \(r+g+1\) is \(g\)-spaced \((k-1)\)-universal. The forward direction chooses the pattern whose first symbol is \(w_r\) and whose remaining \(k-1\) symbols are any specified pattern \(v\). Every occurrence of \(w_r\) lies at or after \(r\), so any allowed occurrence of \(w_rv\) places the suffix pattern entirely after \(r+g\). Hence every \(v\) is realized in that suffix. Conversely, for a pattern \(av\), take the first occurrence of \(a\), at position \(e_a\le r\), and then the prescribed realization of \(v\) in the suffix after \(r+g\). The resulting positions satisfy the required spacing. If fewer than \(g\) letters follow \(P\), the indicated suffix is empty and cannot be universal for \(k-1\ge1\); both sides are false. For \(k=1\), universality is simply existence of a full-alphabet first arch.

**Step 2: canonical factorization and bijection.** Iterate Step 1. A word is \(g\)-spaced \(k\)-universal exactly when it possesses a unique factorization
\[
w=P_1S_1P_2S_2\cdots P_{k-1}S_{k-1}P_kR,
\]
where each \(P_i\) is the shortest full-alphabet prefix of the remaining word at that stage, each \(S_i\in\Sigma^g\) is unconstrained, and \(R\in\Sigma^*\) is arbitrary. The factors are uniquely determined by the sequential first-occurrence algorithm, including for words admitting more than \(k\) arches. Deleting all the \(S_i\) leaves \(P_1\cdots P_kR\), an ordinarily \(k\)-universal word. Conversely, the unique greedy arch factorization of an ordinary \(k\)-universal word gives \(P_1,\ldots,P_k,R\), and inserting any \(k-1\) length-\(g\) spacers recovers a \(g\)-spaced \(k\)-universal word. This establishes the asserted constant-fiber bijection, including its statement about arbitrary suffixes.

**Step 3: arch enumeration.** The final symbol of an arch is the unique previously unseen symbol. For arch length \(\ell\ge q\), choose that final symbol in \(q\) ways and require the first \(\ell-1\) symbols to use every one of the other \(q-1\) symbols. The number of such prefixes is \((q-1)!\,S(\ell-1,q-1)\), where \(S\) denotes a Stirling number of the second kind. Thus the number of length-\(\ell\) arches is \(q! S(\ell-1,q-1)\). Since
\[
\sum_{m\ge q-1}S(m,q-1)t^m=\frac{t^{q-1}}{\prod_{j=1}^{q-1}(1-jt)},
\]
the ordinary generating function of arches is exactly \(A_q(t)\). A fixed-width spacer contributes \((qt)^g\), and an arbitrary suffix contributes \((1-qt)^{-1}\). Multiplication over the canonical factors proves (1).

**Step 4: the full distribution.** Let \(F_k(t)=\sum_{n\ge0}U_{q,g,k}(n)t^n\) for \(k\ge1\), with \(F_0(t)=(1-qt)^{-1}\). Since being \((k+1)\)-universal implies being \(k\)-universal, the generating function for words of exact index \(j\) is \(F_j-F_{j+1}\). Set \(B=(qt)^g\). Formula (1) gives \(F_k=A_q^kB^{k-1}/(1-qt)\), so summing the telescoping differences with the marker \(u\) yields
\[
F_0-F_1+\sum_{j\ge1}u^j(F_j-F_{j+1})
=\frac{1-A_q}{1-qt}+\frac{uA_q(1-A_qB)}{(1-qt)(1-uA_qB)}.
\]
Collecting the numerator gives (2). In particular at \(u=1\) the result equals \((1-qt)^{-1}\), as required because all \(q^n\) words are counted exactly once.

**Step 5: minimum length and first correction.** Each arch has length at least \(q\); each compulsory spacer has length \(g\). Equality in this lower bound requires every arch to be a permutation and the final remainder empty. This proves both the minimum length and the product count. The first two terms of the arch series are
\[
A_q(t)=q!t^q\left(1+\frac{q(q-1)}2t+O(t^2)\right).
\]
Taking the coefficient one above the minimum in (1) proves the displayed correction factor.

**Step 6: renewal limit.** For i.i.d. uniform letters, successive full-alphabet arch lengths \(L_1,L_2,\ldots\), constructed after skipping precisely \(g\) intervening letters between arches, are independent identically distributed coupon-collector waiting times: the skipped letters are disjoint from subsequent sampling. They have finite mean \(qH_q\). The strong law gives \(\sum_{i=1}^k L_i+g(k-1)=k(qH_q+g)+o(k)\) almost surely. Inverting the increasing hitting-time sequence proves the stated limit. This argument also yields the exact completion-time mean \(kqH_q+g(k-1)\) and variance \(k(q^2\sum_{a=1}^q a^{-2}-qH_q)\).

## Verification
The standalone `verify.py` derives expected generating-function coefficients from inclusion–exclusion arch counts and separately computes literal pattern occurrence by exhaustively enumerating admissible index tuples. It compares the literal language, the greedy-arch criterion, and formula (1) across binary, ternary, and four-letter samples, including the first two attainable lengths. It verifies the coefficient expansion of (2) by comparing exact-index histograms against differences of the cumulative counts. The successful execution reports `ALL CHECKS PASSED`. The finite checks corroborate the algebra, while Steps 1–6 prove the infinite and almost-sure assertions.

To reproduce: run `python3 verify.py` with a standard Python 3 installation; no external library is required.

## Relationship to prior work
Day, Kosche, Manea, and Schmid, *Subsequences With Gap Constraints: Complexity Bounds for Matching and Analysis Problems* (arXiv:2206.13896, first version 2022-06-28), establish the general gap-constrained framework and analyze hardness when gap constraints include finite upper bounds. The theorem here treats the all-pattern universality problem with a uniform **positive lower bound and no upper bound**, and shows this particular constrained language has an unexpectedly simple exact enumeration and a renewal law. Their general complexity results do not supply equations (1)–(2).

Barker and collaborators, *Scattered Factor-Universality of Words* (arXiv:2003.04629), introduce the ordinary (zero-gap) greedy-arch characterization. Adamson, *Ranking and Unranking k-subsequence universal words* (arXiv:2304.04583), counts and ranks ordinary universal words; these are the nearest premises for the reduction. Their objects permit consecutive selected positions and do not assert the canonical constant-fiber spacer-bijection for positive gaps. Once the new bijection is proved, the gapped enumerations can indeed be derived from the ungapped ones; this strong relationship is deliberate and is not claimed as an independent resolution of classical zero-gap counting.

Two closely related published research records were also inspected in full. *Closed-form law for binary subsequence universality* determines the full binary **zero-gap** distribution, and *Exact full-support insertion radius of subsequence universality* optimizes the number of symbol insertions to achieve ordinary universality. Neither states an all-alphabet positive-minimum-gap classification. The binary formula in the former agrees with the \(g=0,q=2\) specialization of (2), rather than subsuming the positive-gap assertion.

## Limitations
There is no finite **upper** bound on the gaps; inserting upper bounds generally invalidates Step 1. The formulas address universality against **all** patterns of each fixed length, not counts for an individual pattern or a restricted pattern collection. The result does not compute a closed form for the location of an arbitrary factor under a general gap language. The originality comparison includes full relevant texts and targeted research-record searches, but does not rule out an equivalent theorem published under different terminology. In particular, the positive-gap theorem is closely related to the known ungapped arch factorization, so a previously unindexed consequence of that literature is a residual novelty risk.

## References
1. Joel Day, Maria Kosche, Florin Manea, Markus L. Schmid, *Subsequences With Gap Constraints: Complexity Bounds for Matching and Analysis Problems*, arXiv:2206.13896 (first posted 2022-06-28), https://arxiv.org/abs/2206.13896.
2. Laura Barker, Pamela Fleischmann, Katharina Harwardt, Florin Manea, Dirk Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629 (2020-03-10), https://arxiv.org/abs/2003.04629.
3. Duncan Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583 (2023-04-10), https://arxiv.org/abs/2304.04583.
4. *Closed-form law for binary subsequence universality*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37.
5. *Exact full-support insertion radius of subsequence universality*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-full-support-insertion-radius-of-subsequence-universality--967f04fec949.
