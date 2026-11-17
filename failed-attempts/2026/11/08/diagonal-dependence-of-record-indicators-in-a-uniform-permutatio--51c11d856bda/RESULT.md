# Diagonal dependence of record indicators in a uniform permutation and its inverse

## Finding

Let \(\Pi\) be uniformly distributed over the permutations of \(\{1,\ldots,n\}\), where \(n\ge2\). Write
\[
R_i=\mathbf1\{\Pi(i)=\max_{1\le a\le i}\Pi(a)\},\qquad
Q_j=\mathbf1\{\Pi^{-1}(j)=\max_{1\le b\le j}\Pi^{-1}(b)\}.
\]
For every \(1\le i,j\le n\),
\[
\boxed{\Pr(R_i=1,Q_j=1)=\frac1{ij}+\mathbf1_{\{i=j\}}\frac{i-1}{i^2\binom{n}{i}}.}
\]
Equivalently, the cross-covariance matrix is diagonal:
\[
\boxed{\operatorname{Cov}(R_i,Q_j)=\mathbf1_{\{i=j\}}\frac{i-1}{i^2\binom{n}{i}}.}
\]
Thus \(R_i\) and \(Q_j\) are independent when \(i\ne j\); when \(i=j\ge2\) their covariance is strictly positive. The first indicators are both deterministic, and no claim of mutual independence between entire indicator families is made.

As a consequence, for \(R=\sum_i R_i\), \(Q=\sum_j Q_j\), and \(H_n^{(2)}=\sum_{i=1}^n i^{-2}\),
\[
\operatorname{Cov}(R,Q)=\sum_{i=2}^n\frac{i-1}{i^2\binom{n}{i}}
=\frac1n+O(n^{-2}),\qquad
\operatorname{Corr}(R,Q)\sim\frac1{n\log n}.
\]
The aggregate formulas are consequences of the positionwise classification; joint distributions of aggregate extrema counts already have substantial literature antecedents.

## Assumptions and scope

The probability space is the finite symmetric group with its uniform law. Indices \(i,j\) range independently through \(\{1,\ldots,n\}\), and \(n\ge2\) is arbitrary. Both records are strict prefix maxima, with the inverse permutation indexed by **values** rather than original positions. The inverse-prefix condition means that value \(j\) occurs later than all smaller values. A record of the inverse at \(j\) is equivalently a right-to-left minimum of value \(j\) in the original permutation.

## Proof

For a fixed index \(i\), let \(S_i=\{\Pi(1),\ldots,\Pi(i)\}\). Conditional on the unordered set \(S_i\), the orders of the first \(i\) entries and the last \(n-i\) entries are independent and uniform on their respective value sets. In particular \(\Pr(R_i=1\mid S_i)=1/i\), regardless of the set.

First suppose \(i<j\). If \(j\in S_i\), there must be a value smaller than \(j\) outside \(S_i\): otherwise the \(j\) distinct values \(1,\ldots,j\) would lie in a set of size \(i<j\). Such a smaller value occurs later than \(j\), so \(Q_j=0\). If \(j\notin S_i\), the event \(Q_j=1\) is determined by \(S_i\) and the ordering of the suffix, since every member of the prefix occurs before \(j\). Therefore in either case \(Q_j\) is conditionally independent of the random prefix ordering. It follows that
\[
\Pr(R_i=1,Q_j=1)=\mathbb E[\Pr(R_i=1\mid S_i)\Pr(Q_j=1\mid S_i)]=\frac1i\Pr(Q_j=1)=\frac1{ij}.
\]
The case \(i>j\) follows by applying the same argument to the uniform inverse permutation: inversion interchanges \(R_i\) and \(Q_i\). This establishes the off-diagonal formula.

Now let \(i=j\). Outside the event \(S_i=\{1,\ldots,i\}\), the preceding conditional-independence argument still works: either \(i\notin S_i\) and \(Q_i\) depends only on the suffix and the set, or \(i\in S_i\) and a smaller value is in the suffix, forcing \(Q_i=0\). On the exceptional event \(S_i=\{1,\ldots,i\}\), both \(R_i\) and \(Q_i\) are the same Bernoulli event \(\{\Pi(i)=i\}\), whose conditional variance is \((i-1)/i^2\). The law of total covariance gives
\[
\operatorname{Cov}(R_i,Q_i)=\mathbb E[\operatorname{Cov}(R_i,Q_i\mid S_i)]
+\operatorname{Cov}(\mathbb E[R_i\mid S_i],\mathbb E[Q_i\mid S_i]).
\]
The second term is zero because the first conditional mean is the constant \(1/i\). The exceptional set has probability \(1/\binom{n}{i}\), proving the diagonal formula, including the zero case \(i=1\).

Finally, the prefix ranks are independent uniform ranks on their respective ranges, so the indicators \(R_i\) are mutually independent with \(\operatorname{Var}(R)=H_n-H_n^{(2)}\); the same holds for \(Q\). Summing the cross-covariance yields the stated finite formula. The \(i=n\) summand equals \((n-1)/n^2=1/n+O(n^{-2})\). The remaining terms are \(O(n^{-2})\): the term \(i=n-1\) is \(O(n^{-2})\); terms \(i=2\) and \(i=n-2\) are at most \(1/\binom{n}{2}=O(n^{-2})\); and for \(3\le i\le n-3\) their sum is at most \(n/\binom{n}{3}=O(n^{-2})\), with the small values of \(n\) absorbed into the bound. Since \(H_n-H_n^{(2)}\sim\log n\), the correlation asymptotic follows.

## Verification

Run `python verify.py` using Python's standard library. It enumerates every permutation for each \(2\le n\le9\), independently computes the two record-indicator vectors, and checks each of the \(n^2\) joint probabilities against the theorem using exact rational arithmetic. It also checks the resulting aggregate covariance. All 292 exact assertions passed. These finite checks do not replace the all-size conditional proof.

## Relationship to prior work

Gnedin's 2006 work on coherent random permutations and upper/lower records develops the record-value and initial-rank framework; Gnedin and Gorin's 2012 paper studies record-dependent measures and gives the classical independent initial-rank representation. Neither of their inspected stated results is a position-by-value cross-covariance classification for record indicators of a permutation and its inverse.

Jin's 2022 work establishes joint generating functions of aggregate Euler–Stirling permutation statistics, including left-to-right minima together with right-to-left maxima. By complementing permutation values, that aggregate pair corresponds to the total numbers of left-to-right maxima and right-to-left minima, hence to the two total record counts above. The total-count covariance is therefore not claimed as an independently novel distributional result. An aggregate generating function does not determine the labeled \(n\)-by-\(n\) matrix of cross-record covariances; the diagonal independence classification is the specific refinement here.

## Limitations

The theorem concerns uniform finite permutations; it does not assert an analogous diagonal law for nonuniform permutation measures, ties, or a joint factorization of all record indicators. Historical literature may contain an implicit equivalent of the positionwise law, especially through refined permutation-generating functions. No independent audit or external certification is claimed.

## References

1. A. Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538v1 (public 2006-11-17), https://arxiv.org/abs/math/0611538.
2. A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, arXiv:1202.3680v1 (public 2012-02-16), https://arxiv.org/abs/1202.3680.
3. E. Y. Jin, *Symmetric generating functions and Euler–Stirling statistics on permutations*, arXiv:2210.08789v1 (public 2022-10-17), https://arxiv.org/abs/2210.08789.
