# Complete two-point descent law under increasing-subsequence size bias

## Finding
Let \(\pi\) be a uniform permutation of \(n\ge4\) symbols and let \(Z_{n,k}\) count its increasing subsequences of length \(2\le k\le n\). Weight each permutation by \(Z_{n,k}\), yielding \(\mu_{n,k}(\pi)=Z_{n,k}(\pi)/(n!\,\mathbb E_U Z_{n,k})\). For descents \(D_i=\mathbf 1\{\pi(i)>\pi(i+1)\}\), define \(x=(k)_{\underline 2}/(n)_{\underline 2}\) and \(y=(k)_{\underline 4}/(n)_{\underline 4}\). Then, at every admissible position,
\[
\mathbb P_\mu(D_i=1)=\frac{1-x}{2},
\qquad
\mathbb P_\mu(D_i=D_{i+1}=1)=\frac16\left[1-\frac{k(k-1)(3n-2k-2)}{n(n-1)(n-2)}\right],
\]
while for \(|i-j|\ge2\),
\[
\mathbb P_\mu(D_i=D_j=1)=\frac{1-2x+y}{4},\qquad
\operatorname{Cov}_\mu(D_i,D_j)=\frac{y-x^2}{4}<0\quad\text{if } k<n.
\]
When \(k=n\), the measure is concentrated on the identity and this covariance is zero. For the total descent count \(D=\sum_{i=1}^{n-1}D_i\),
\[
\mathbb E_\mu D=\frac{n-1}{2}-\frac{k(k-1)}{2n},
\]
\[
\operatorname{Var}_\mu(D)=\frac{(n-k)(n-k+1)(3k^2+2kn-3k+n^2-n)}{12n^2(n-1)}.
\]
Consequently, if \(k/n\to\alpha\in[0,1]\), then
\[
\frac{\operatorname{Var}_\mu(D)}{n}\longrightarrow\frac{(1-\alpha)^2(3\alpha^2+2\alpha+1)}{12}.
\]
Under the original uniform law, descents at nonadjacent positions are independent; the subsequence-weighted law creates strictly negative long-range pairwise covariance.

## Assumptions and scope
The distribution \(U\) is uniform on the finite symmetric group. Increasing subsequences are chosen by index sets, not required to be consecutive. The size-biased law is well defined because \(\mathbb E_U Z_{n,k}=\binom nk/k!>0\). The notation \((a)_{\underline r}\) means a falling factorial, zero when \(0\le a<r\). For binomial coefficients, \(\binom ab=0\) if \(b<0\) or \(b>a\). All probabilities, covariances, and variances without an explicit \(U\) subscript are under \(\mu_{n,k}\). The adjacent-pair equation applies only where \(i+2\le n\); the distant-pair equation applies only where both descents exist.

## Proof
**The block-symmetrization lemma.** Fix disjoint blocks of consecutive positions and impose a specific strict ordering on the values inside each block. Every value ordering within the blocks has the same conditional probability, and therefore a prescribed ordering has probability equal to the reciprocal of the product of the block factorials. For any increasing subsequence using at most one position from each block, the sum of its indicators over all such subsequences is invariant under permutations of the entries within each block: the set of candidate positions outside the blocks lies wholly before or after each consecutive block, and the contributions from choosing one block entry sum symmetrically over its block values. Thus the conditional expectation of this restricted subsequence count equals its unconditional expectation; the latter is the number of eligible index sets divided by \(k!\), since every selection of \(k\) distinct indices has an equally likely increasing value ordering.

For one descent at \(i\), the two positions in the adjacent block are decreasing, so no increasing subsequence can use both. The block lemma and the probability \(1/2\) of the prescribed order imply
\[
\mathbb E_U[Z_{n,k}D_i]=\frac1{2k!}\left[\binom nk-\binom{n-2}{k-2}\right].
\]
Dividing by \(\mathbb E_U Z_{n,k}\) gives \(\mathbb P_\mu(D_i=1)=(1-x)/2\).

For two consecutive descents \(D_i=D_{i+1}=1\), three consecutive positions must occur in strictly decreasing order, of unconditional probability \(1/6\). Any increasing subsequence then uses at most one of these three positions. The count of index sets that select at least two of the three is \(3\binom{n-3}{k-2}+\binom{n-3}{k-3}\); the two summands correspond to selecting exactly two, or all three, of the positions. Hence
\[
\mathbb E_U[Z_{n,k}D_iD_{i+1}]=\frac1{6k!}\left[\binom nk-3\binom{n-3}{k-2}-\binom{n-3}{k-3}\right].
\]
Dividing by the normalizing expectation and reducing the binomial ratios proves the adjacent formula.

For \(|i-j|\ge2\), the pairs of positions \(\{i,i+1\}\) and \(\{j,j+1\}\) are disjoint consecutive blocks. Both are decreasing with probability \(1/4\). An increasing subsequence then takes at most one position from each block. By inclusion-exclusion, the number of allowed index sets is \(\binom nk-2\binom{n-2}{k-2}+\binom{n-4}{k-4}\); hence
\[
\mathbb E_U[Z_{n,k}D_iD_j]=\frac1{4k!}\left[\binom nk-2\binom{n-2}{k-2}+\binom{n-4}{k-4}\right].
\]
The normalized ratios give \((1-2x+y)/4\), and subtracting the product of the two means yields \((y-x^2)/4\).

To prove strict negativity, choose a uniform \(k\)-subset of \(\{1,\ldots,n\}\) and let \(A\) denote the event that two designated elements are included. Then \(\mathbb P(A)=x\), while the probability that another pair of designated elements is also included, conditional on \(A\), is \((k-2)_{\underline2}/(n-2)_{\underline2}<k_{\underline2}/n_{\underline2}=x\) for \(2\le k<n\). Therefore \(y<x^2\); equality holds for \(k=n\).

There are \(n-1\) descent indicators, \(n-2\) unordered adjacent pairs, and \((n-2)(n-3)/2\) unordered disjoint pairs. With \(p=(1-x)/2\), \(q_a\) and \(q_f\) the two displayed pair probabilities, variance decomposition gives
\[
\operatorname{Var}_\mu(D)=(n-1)p(1-p)+2(n-2)(q_a-p^2)+(n-2)(n-3)(q_f-p^2).
\]
Substitution and expansion yield the stated rational formula; summing the individual means yields the stated expectation. Finally, divide the rational variance by \(n\) and substitute \(k/n\to\alpha\) to obtain the limit, including the endpoints.

## Verification
The standalone Python file `verify.py`, requiring no nonstandard dependencies, independently enumerates every permutation for \(2\le n\le8\), weights each by its exact increasing-subsequence count, and checks all one-point and two-point probabilities, total mean, total variance, and normalizations using rational arithmetic. It additionally tests strict separated-descent covariance and positive variance on a larger exact finite parameter grid. Run `python verify.py` from the extracted package directory. The recorded execution returned `PASS: 46232 permutations enumerated across n=2..8; 1600 exact-rational assertions.` Enumeration alone is not a proof for arbitrary \(n\); the block-symmetrization argument supplies the general proof.

## Relationship to prior work
Pinsky (2004) defines and studies precisely the increasing-subsequence-size-biased permutation law used here. Its law and expected increasing-subsequence counts are not new. Pinsky (2006) analyzes related detection and asymptotic questions. Kammoun (2018) studies descent dependence for a different, conjugation-invariant setting; the present size-biased law is neither the uniform law nor generally conjugation-invariant. In the inspected material, these sources do not determine the complete descent-pair law or its finite-parameter variance. This statement does not claim exhaustive historical priority.

## Limitations
The conclusions require the specified increasing-subsequence weight and uniform base measure. Pairwise negative covariance does not establish joint negative association or a central limit theorem. The explicit variance does not by itself prove a normal approximation. Historical coincidence with a more general permutation-statistic cross-moment formula remains possible; independent scholarly audit has not been performed.

## References
- R. G. Pinsky, *Law of large numbers for increasing subsequences of random permutations and an approximation result for the uniform measure*, arXiv:math/0407353v1 (first public 2004-07-21); the paper introduces the weighted increasing-subsequence measure.
- R. G. Pinsky, *When the law of large numbers fails for increasing subsequences of random permutations*, arXiv:math/0604067v1 (2006).
- M. Kammoun, *Monotonous subsequences and the descent process of invariant random permutations*, arXiv:1805.05253v1 (2018); a distinct permutation ensemble used for comparison.
