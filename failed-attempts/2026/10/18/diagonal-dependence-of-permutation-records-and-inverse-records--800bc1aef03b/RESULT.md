# Diagonal dependence of permutation records and inverse records

## Finding

For a uniformly random permutation \(\pi\in S_n\), with \(n\ge2\), define the upper-record indicator at position \(i\) and the upper-record indicator at position \(j\) of the inverse permutation by
\[
R_i=\mathbf1\{\pi_i=\max_{1\le k\le i}\pi_k\},\qquad
S_j=\mathbf1\{\pi^{-1}(j)=\max_{1\le k\le j}\pi^{-1}(k)\}.
\]
Then, simultaneously for every \(1\le i,j\le n\),
\[
\boxed{\mathbb P(R_i=1,S_j=1)=\frac1{ij}+\mathbf1_{\{i=j\}}\frac{i-1}{i^2\binom ni}}.
\]
In particular,
\[
\boxed{\operatorname{Cov}(R_i,S_j)=\mathbf1_{\{i=j\}}\frac{i-1}{i^2\binom ni}}.
\]
The entire cross-covariance matrix is diagonal, has rank exactly \(n-1\), and its nonzero diagonal is positive. Every pair \((R_i,S_j)\) at distinct indices is independent, even though the two complete vectors are not claimed to be independent.

Writing \(U_n=\sum_{i=1}^nR_i\) and \(V_n=\sum_{j=1}^nS_j\), the exact covariance and asymptotics are
\[
\boxed{\operatorname{Cov}(U_n,V_n)=\sum_{i=2}^n\frac{i-1}{i^2\binom ni}
=\frac1n+\frac1{2n^2}+O(n^{-3}).}
\]
Since \(\operatorname{Var}(U_n)=\operatorname{Var}(V_n)=H_n-H_n^{(2)}\), where \(H_n=\sum_{i=1}^n1/i\) and \(H_n^{(2)}=\sum_{i=1}^n1/i^2\), it follows that
\[
\boxed{\operatorname{Corr}(U_n,V_n)\sim\frac1{n\log n}}.
\]

## Assumptions and scope

A permutation is sampled uniformly from the \(n!\) permutations of \(\{1,\ldots,n\}\). Upper records are strict left-to-right maxima. The inverse is written in one-line notation as \((\pi^{-1}(1),\ldots,\pi^{-1}(n))\). Both first indicators equal one deterministically. Indices always lie between one and \(n\), inclusive; the theorem is finite-sample and assumes no limiting distribution, bias, or conditioning beyond the displayed law.

## Proof

Fix \(i,j\), and set \(A=\{\pi_1,\ldots,\pi_i\}\). It is a uniform subset of size \(i\). Conditional on \(A\), the orders within the initial block and its complement are independent uniformly random permutations. The event \(R_i=1\) means that the largest element of \(A\) is at the final position of the initial block. Hence
\[
\mathbb E(R_i\mid A)=\frac1i,
\]
independently of the realized set \(A\).

We now compute conditional covariance with \(S_j\), using the interpretation that \(S_j=1\) iff value \(j\) appears *later* than every value in \(\{1,\ldots,j-1\}\).

**Case 1:** If \(j\notin A\), then the event \(S_j=1\) depends only on the relative order in the complementary suffix. All values at most \(j\) lying in the initial block precede \(j\) automatically. Conditional independence of initial and complementary orders implies \(\operatorname{Cov}(R_i,S_j\mid A)=0\).

**Case 2:** If \(j\in A\) but \(\{1,\ldots,j\}\nsubseteq A\), then at least one smaller value appears in the suffix, later than \(j\), forcing \(S_j=0\). Again the conditional covariance vanishes.

**Case 3:** Suppose \(\{1,\ldots,j\}\subseteq A\). If \(\max A>j\), the unique largest element of \(A\) is outside this set. In a uniform ordering of \(A\), its position is independent of the relative ordering of the \(j\) smallest values. Thus \(R_i\) and \(S_j\) are conditionally independent, with respective conditional probabilities \(1/i\) and \(1/j\). The only remaining possibility is \(\max A=j\), which together with the inclusion forces \(A=\{1,\ldots,j\}\) and \(i=j\). On this event the two indicators coincide: \(R_i=S_i=\mathbf1\{\pi_i=i\}\) conditionally, a Bernoulli variable of parameter \(1/i\). Its conditional covariance is \((i-1)/i^2\).

The law of total covariance now gives
\[
\operatorname{Cov}(R_i,S_j)=\mathbb E\bigl[\operatorname{Cov}(R_i,S_j\mid A)\bigr]
+\operatorname{Cov}\bigl(\mathbb E(R_i\mid A),\mathbb E(S_j\mid A)\bigr).
\]
The second term is zero because \(\mathbb E(R_i\mid A)=1/i\) is constant. The first term is zero unless \(i=j\) and \(A=\{1,\ldots,i\}\), whose probability is \(\binom ni^{-1}\). This proves the covariance formula. Both marginals are Bernoulli with success probabilities \(1/i\) and \(1/j\), so their zero covariance for distinct indices implies independence. The rank statement follows from the strictly positive diagonal entries for indices \(2,\ldots,n\), and the deterministic first coordinate.

Summing the entrywise covariances proves the exact formula for \(\operatorname{Cov}(U_n,V_n)\). For its expansion, the summands at \(i=n\), \(i=n-1\), and \(i=2\) are, respectively,
\[
\frac{n-1}{n^2}=\frac1n-\frac1{n^2},\quad
\frac{n-2}{n(n-1)^2}=\frac1{n^2}+O(n^{-3}),\quad
\frac1{2n(n-1)}=\frac1{2n^2}+O(n^{-3}).
\]
All other summands contribute \(O(n^{-3})\): the terms at \(i=3\), \(i=n-2\), and \(i=n-3\) individually have that order, while for \(4\le i\le n-4\) each is at most \(\binom n4^{-1}\), and there are at most \(n\) such indices. This proves the second-order expansion for large \(n\).

Under a uniform random permutation, the successive relative ranks \(\pi_i\) among \(\pi_1,\ldots,\pi_i\) are independent and uniform on \(\{1,\ldots,i\}\). Thus \((R_i)_i\) are independent Bernoulli variables with parameters \(1/i\); the same holds for \((S_j)_j\). The displayed variance identity follows, and since \(H_n-H_n^{(2)}\sim\log n\), division of the covariance expansion by this common variance proves the correlation limit.

## Verification

The accompanying self-contained script `verify_dual_records.py` enumerates every permutation through size eight, computes the inverse and both full record-indicator arrays directly, and compares all joint probabilities and covariances exactly using rational arithmetic. It also checks both total-record covariance identities and several asymptotic approximations numerically. Executing `python3 verify_dual_records.py` gave `PASS: 656 exact-rational assertions and 4 numerical comparisons; exhaustive permutations through n=8`.

These finite checks are corroboration; the conditional-prefix argument and elementary asymptotic bounds above establish the theorem for all permitted sizes.

## Relationship to prior work

Gnedin's 2006 work studies the distribution of upper and lower record values *within one permutation*, including a two-parameter record-biased family and the initial-rank representation. The distinction between record positions and values is important: that two-sided family does not assert the displayed upper-record/inverse-upper-record cross-covariance kernel.

Gnedin and Gorin's 2012 research develops record-dependent measures, coherent orders, and inverse-permutation constructions; its independent-rank representation explains the separate record marginals but does not directly state the indexwise dependence cancellation between a uniform permutation and its inverse. Gnedin and Marynych study planar Poisson records and related distributional symmetries, not this discrete finite covariance matrix.

Gessel and Zhuang's later two-sided permutation-statistic formulas apply to statistics of a permutation and inverse that are determined by descent compositions. Upper-record sets are not so determined; for example, \((1,4,2,3)\) and \((1,3,2,4)\) both have their only descent at position two, but different upper-record sets. Thus that stated framework does not directly encompass the claim here. It may still suggest a broader algebraic perspective.

## Limitations

The claim requires uniform permutations and strict upper records. Pairwise independence of the off-diagonal indicators does not assert joint independence of the two record vectors, or any special structure for biased permutation laws. The summed covariance is a direct consequence of the matrix formula and is not separately asserted to be a novel aggregate identity. Classical two-sided record enumerations or more general implicit joint-generating functions might imply the formula without using the same notation; this is a remaining priority risk. No independent validation of correctness or publication priority has been performed.

## References

1. A. Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538v1, publicly posted 2006-11-17. https://arxiv.org/abs/math/0611538
2. A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, arXiv:1202.3680v1, publicly posted 2012-02-16. https://arxiv.org/abs/1202.3680
3. A. Gnedin and A. Marynych, *Exponential–Uniform Identities Related to Records*, arXiv:1206.1080v1, publicly posted 2012-06-05. https://arxiv.org/abs/1206.1080
4. I. Gessel and Y. Zhuang, *Two-sided permutation statistics via symmetric functions*, arXiv:2306.15785v1, publicly posted 2023-06-27. https://arxiv.org/abs/2306.15785
