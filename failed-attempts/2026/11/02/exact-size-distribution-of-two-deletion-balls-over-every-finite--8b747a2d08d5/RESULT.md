# Exact size distribution of two-deletion balls over every finite alphabet

## Finding

Fix integers \(q\ge 2\) and \(n\ge 2\), and let \(D_2(w)\) be the **set** of distinct words obtained by deleting exactly two positions from \(w\in\Sigma_q^n\). The following gives the full distribution, not merely its minimum, maximum, or average. Put \(N=n-1\), and for a binary pattern \(b=(b_0,\ldots,b_{N-1})\) define
\[
m(b)=\sum_{i=0}^{N-1}b_i,\qquad a(b)=\sum_{i=0}^{N-2}b_ib_{i+1},\qquad r(b)=m(b)-a(b),\qquad e(b)=b_0+b_{N-1}.
\]
The endpoint indicator counts the same bit twice when \(N=1\). Then the exact enumerator is
\[
\boxed{H_{n,q}(z):=\sum_{w\in\Sigma_q^n}z^{|D_2(w)|}=q\sum_{b\in\{0,1\}^{N}}(q-1)^{m(b)-a(b)}z^{1+\binom{m(b)}2+2r(b)-e(b)}\bigl(1+(q-2)z\bigr)^{a(b)}.}
\]
In particular, the coefficient of \(z^j\) is exactly the number of length-\(n\), \(q\)-ary words with \(j\) different two-deletion descendants.

An equivalent explicit binomial-sum formula avoids enumeration of binary patterns. For integers \(s\ge0\), \(r\ge1\), and \(e\in\{0,1,2\}\), set
\[
G(s,r,e)=\begin{cases}
\binom{s-1}{r},&e=0,\\
2\binom{s-1}{r-1},&e=1,\\
\binom{s-1}{r-2}+\mathbf1_{\{s=0,r=1\}},&e=2,
\end{cases}
\]
with every inadmissible binomial coefficient interpreted as zero. Then
\[
\boxed{H_{n,q}(z)=qz+q\sum_{m=1}^{N}\sum_{r=1}^{m}\binom{m-1}{r-1}\sum_{e=0}^{2}G(N-m,r,e)(q-1)^r z^{1+\binom m2+2r-e}\bigl(1+(q-2)z\bigr)^{m-r}.}
\]
For a uniformly random word, write \(p=(q-1)/q\) and \(u=1/q\). If \(B=|D_2(w)|\), the first two moments follow:
\[
\mathbb E B=1+(n-2)p+\binom{n-1}{2}p^2,
\]
\[
\boxed{\operatorname{Var}(B)=(n-1)(n-2)^2p^3u+\binom{n-2}{2}p^2u^2+(n-2)(u-2u^2+u^4).}
\]
These identities hold for every \(q\ge2\), including \(n=2\) when all balls have size one. The binary specialization of the variance is already known and is **not** asserted to be new.

## Assumptions and scope

The alphabet consists of \(q\) distinct symbols. Every ordered word is counted separately; deleting two positions does not substitute, reorder, or relabel symbols. Multiple deletion-position pairs producing the same resulting word count as one descendant. The zero-length word is permitted when \(n=2\). No limiting assumption on \(n\) or prime-power assumption on \(q\) is made.

For a fixed word, define its adjacent-change vector by \(b_i=\mathbf1_{\{w_i\ne w_{i+1}\}}\). Let \(T(w)\) count indices \(0\le i\le n-3\) such that the three letters \(w_i,w_{i+1},w_{i+2}\) are pairwise distinct. The central structural identity is
\[
|D_2(w)|=1+\binom{m(b)}2+2\bigl(m(b)-a(b)\bigr)-e(b)+T(w).
\]

## Proof

**1. Unique canonical deletion pairs.** Every resulting subsequence has a unique lexicographically earliest embedding: scan the original word from left to right and retain the earliest possible match of the next subsequence symbol. Its two omitted indices, denoted \(i<j\), are therefore a unique canonical representative of the descendant. If \(j<n-1\) and \(i<j-1\), then this pair is canonical exactly when both skipped letters differ from their immediate successor. Such pairs number \(\binom m2-a\). If \(j=n-1\) and \(i<n-2\), the pair is canonical exactly when the first skip is an adjacent change; there are \(m-b_{N-1}\) such pairs. If \(j=i+1<n-1\), both deleted symbols must differ from the next retained symbol. Among these, \(m-b_0-a\) have equal first two letters followed by a distinct third, and \(T(w)\) have three pairwise distinct letters. Finally \((n-2,n-1)\) is always canonical. Summing yields
\[
1+(\binom m2-a)+(m-b_{N-1})+(m-b_0-a+T)=1+\binom m2+2(m-a)-e+T.
\]
This also checks the terminal-edge case \(n=2\).

**2. Counting symbol realizations.** For each fixed adjacent-change vector \(b\), choose the initial symbol in \(q\) ways. At every change there are \(q-1\) equiprobable options, whereas at a non-change the symbol is forced. Thus the total number of realizations of \(b\) is \(q(q-1)^m\). At any position with consecutive changes, the third symbol differs from both predecessors in exactly \(q-2\) of its \(q-1\) options and equals the first in the remaining option. Conditional on \(b\), the resulting rainbow-triple indicators are independent: at the second change of each tested pair, this one-versus-\(q-2\) split is the same even after all earlier choices are specified. Consequently, among those realizations, the weight generating polynomial of \(T(w)\) is
\[
q(q-1)^{m-a}\bigl(1+(q-2)z\bigr)^a.
\]
Inserting the structural identity proves the first boxed formula.

**3. Removing the pattern sum.** A nonzero binary vector with \(m\) ones and \(r\) maximal blocks of ones has \(\binom{m-1}{r-1}\) choices of positive block lengths. If it has \(s=N-m\) zeroes, then its internal \(r-1\) zero gaps are positive, while the outer two gaps encode whether the endpoint bits are one. With neither, one, or both endpoint bits equal to one, stars-and-bars gives \(G(s,r,0)\), \(G(s,r,1)\), and \(G(s,r,2)\), respectively. The extra term in \(G(s,r,2)\) handles the unique all-one vector. Grouping vectors by \((m,r,e)\) proves the second boxed formula.

**4. Moments.** Conditional on the change vector, \(T\) is binomial with \(a\) trials and success probability \((q-2)/(q-1)\). The changes themselves are independent Bernoulli variables with success probability \(p\), because each new letter independently agrees with the previous one with probability \(u\). Writing \(y_i=b_i-p\), the conditional mean has orthogonal multilinear expansion with constant term \(\mathbb EB\), uniform linear coefficient \((N-1)p\) at each \(y_i\), coefficient one at nonadjacent quadratic pairs, and coefficient \(1-1/p=-u/p\) at adjacent pairs. Orthogonality gives
\[
\operatorname{Var}(\mathbb E[B\mid b])=N(N-1)^2p^3u+\binom{N-1}{2}p^2u^2+(N-1)u^4.
\]
Moreover, \(\mathbb E\operatorname{Var}(B\mid b)=(N-1)(u-2u^2)\). Adding the two contributions proves the variance expression. Finally, direct expectation in the structural formula gives the claimed mean (alternatively count pairs of a word and one of its deletion descendants by insertion).

## Verification

The standalone standard-library script `verify.py` computes each actual descendant set directly and independently checks the structural identity, the two closed-form enumerators, and exact rational mean/variance for every \(2\le n\le10\) at \(q=2\), every \(2\le n\le8\) at \(q=3\), every \(2\le n\le7\) at \(q=4\), and every \(2\le n\le6\) at \(q=5\). The separate `crosscheck.py` checks the count using unique greedy embeddings rather than sets of resulting words. Both scripts use only Python's standard library and terminate with `VERIFY_OK` and `CROSSCHECK_OK` on success.

The scripts check finite instances; the proof above, not those finite checks, establishes the formulas for all parameters.

## Relationship to prior work

Swart and Ferreira (2003) give a run-length formula for binary double-deletion subsequence counts. Mercier, Khabbazian and Bhargava (2008) give per-word counting formulas, including nonbinary alphabets, for small deletion counts. Liron and Langberg (first public preprint February 8, 2012) study extremal run-constrained binary subsequence counts; Cullina and Kiyavash (2013) give asymptotic bounds for deletion-correcting codes. Li, Wang and Fu (first public preprint January 10, 2026) study nonbinary run-constrained extrema. None of these inspected statements supplies the **full distribution across all input words** or the explicit all-alphabet generating polynomial proved above. A separately indexed result already gives the binary specialization of the variance. Those earlier facts are acknowledged rather than presented as new. Deriving the present coefficients by expanding earlier per-word algorithms is possible in principle, but such generic computability does not itself provide the closed all-parameter distribution or the simplified nonbinary variance identity.

## Limitations

The analysis treats exactly two deletions and uniform counting of input words. It does not describe deletion probabilities, input-dependent output multiplicities, maximal error-correcting code sizes, or balls for three or more deletions. Unindexed prior algebraic formulas and unpublished tables remain historical-priority risks. The derivation is a mathematical proof supported by finite independent implementations; no third-party audit is claimed.

## References

1. T. G. Swart and H. C. Ferreira, “A note on double insertion/deletion correcting codes,” *IEEE Transactions on Information Theory* 49 (2003), 269–273. https://doi.org/10.1109/TIT.2002.806155
2. H. Mercier, M. Khabbazian and V. K. Bhargava, “On the number of subsequences when deleting symbols from a string,” *IEEE Transactions on Information Theory* 54 (2008), 3279–3285. https://doi.org/10.1109/TIT.2008.924730
3. Y. Liron and M. Langberg, “A characterization of the number of subsequences obtained via the deletion channel,” arXiv:1202.1644v1, posted 2012-02-08. https://arxiv.org/abs/1202.1644
4. D. Cullina and N. Kiyavash, “An improvement to Levenshtein's upper bound on the cardinality of deletion correcting codes,” arXiv:1302.6562v1, posted 2013-02-26. https://arxiv.org/abs/1302.6562
5. H. Li, X. Wang and F.-W. Fu, “On the number of subsequences in the nonbinary deletion channel,” arXiv:2601.06493v1, posted 2026-01-10. https://arxiv.org/abs/2601.06493
