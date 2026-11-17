# Conditional law and exact variance of nonbinary two-deletion spheres

## Finding

Let \(q\ge 2\) and \(n\ge 2\). Let \(W=(W_0,\ldots,W_{n-1})\) be uniformly distributed on \(\Sigma_q^n\), and define the cardinality of the **distinct-output, exact-two-deletion sphere**
\[
B_2(W)=\bigl|\{(W_k)_{k\notin\{i,j\}}:0\le i<j<n\}\bigr|.
\]
The empty subsequence is counted once when \(n=2\). The following gives the full finite conditional distribution and the first two moments for every \(q,n\).

For \(n\ge3\), define \(T_i=\mathbf1\{W_i\ne W_{i-1}\}\) for \(1\le i\le n-1\), \(S=\sum_{i=1}^{n-1}T_i\), \(J=\sum_{i=1}^{n-2}T_iT_{i+1}\), and \(e=T_1+T_{n-1}\). Then \(T_i\) are independent Bernoulli with probability \(p=(q-1)/q\), and, **conditioned on their entire vector**, 
\[
\boxed{B_2(W)\ \overset{d}{=}\ 1+\frac{S(S+3)}2-e-J-\operatorname{Bin}\!\left(J,\frac1{q-1}\right).}
\]
The conditional binomial draw is independent of the given transition vector. In particular, this is a finite exact mixture formula for the complete distribution of \(B_2\), not merely its moments. At \(n=2\), \(B_2=1\) deterministically.

For all \(n\ge2\), writing \(p=(q-1)/q\),
\[
\boxed{\mathbb E B_2=1+(n-2)p+\frac{(n-1)(n-2)}2p^2,}
\]
\[
\boxed{\operatorname{Var}(B_2)=\frac{n-2}{q^4}\left((n-1)(n-2)(q-1)^3+\frac{n-3}{2}(q-1)^2+1+(q-2)q^2\right).}
\]
For \(q=2\), the latter specializes to \((n-1)(n-2)(2n-3)/32\), consistent with the earlier published binary case. The nonbinary conditional law and variance extend this case for all \(q\ge3\).

## Assumptions and scope

All alphabet symbols are equiprobable, and coordinates of \(W\) are independent. Deletion removes exactly two positions, with duplicate resulting words identified. No metric substitutions or insertions are allowed; source and received lengths are \(n\) and \(n-2\). The algebraic difference representation below uses a convenient identification of the alphabet with \(\mathbb Z/q\mathbb Z\), without requiring \(q\) to be prime.

## Proof

**1. Canonical embedding and a deterministic identity.** A scattered subsequence has a unique right-greedy embedding: choose its last letter at the rightmost possible position, then repeatedly choose the preceding required letter as far right as possible. Thus a two-element deletion set represents a distinct output exactly when its complement is that canonical embedding. With deleted positions \(i<j\), there are four cases, using zero-based indices:

* \((i,j)=(0,1)\) always gives a canonical embedding.
* When \(i=0\) and \(j\ge2\), canonicity holds precisely when \(W_j\ne W_{j-1}\).
* When \(1\le i\) and \(j\ge i+2\), it holds precisely when both \(W_i\ne W_{i-1}\) and \(W_j\ne W_{j-1}\).
* When \(1\le i\) and \(j=i+1\), it holds precisely when \(W_i\ne W_{i-1}\) **and** \(W_{i+1}\ne W_{i-1}\). There are now two discarded letters following the previous retained letter; either could otherwise provide a later copy of that retained letter.

Indeed, reading the greedy embedding from right to left, a deleted position is usable for the immediately preceding retained symbol exactly when their symbols coincide; if both deleted positions share the same gap, either deleted symbol can provide a later replacement. These are all possibilities because only two positions are deleted. Let
\[
R_i=\mathbf1\{W_{i-1}=W_{i+1}\ne W_i\},\qquad 1\le i\le n-2.
\]
The number of canonical pairs is the sum of the above disjoint cases. The nonadjacent cases contribute
\(1+(S-T_1)+(\binom S2-J)\); the remaining adjacent case contributes \(S-T_{n-1}-\sum_iR_i\). Therefore, for every fixed word of length \(n\ge3\),
\[
\tag{1} B_2=1+\frac{S(S+3)}2-T_1-T_{n-1}-J-\sum_{i=1}^{n-2}R_i.
\]
This pointwise identity does not assume randomness.

**2. Conditional binomial independence.** Identify \(\Sigma_q\) with \(\mathbb Z/q\mathbb Z\) and set \(\Delta_i=W_i-W_{i-1}\). The map from the uniform word to \((W_0,\Delta_1,\ldots,\Delta_{n-1})\) is bijective, so the increments are independent uniform residues and \(T_i=\mathbf1\{\Delta_i\ne0\}\) are independent Bernoulli \(p\). Conditioned on all the \(T_i\), the nonzero increments are independently uniform over the \(q-1\) nonzero residues. Moreover,
\[
R_i=T_iT_{i+1}\,\mathbf1\{\Delta_{i+1}=-\Delta_i\}.
\]
Within each maximal chain of nonzero increments, reveal increments sequentially. For each adjacent edge, exactly one of the \(q-1\) equally likely choices gives \(\Delta_{i+1}=-\Delta_i\), regardless of the previously revealed values or reversal events. Consequently the reversal indicators on the chain are mutually independent Bernoulli with parameter \(a=1/(q-1)\). Different chains are independent. There are exactly \(J\) eligible edges; hence \(\sum_iR_i\mid(T_i)\sim\operatorname{Bin}(J,a)\). Substituting in (1) proves the full conditional law. This includes \(q=2\), where \(a=1\) and the binomial variable is deterministic.

**3. Mean.** From \(\mathbb ES=(n-1)p\), \(\operatorname{Var}(S)=(n-1)p(1-p)\), \(\mathbb E J=(n-2)p^2\), \(\mathbb E e=2p\), and \((1+a)p=1\), taking expectations in the conditional law and simplifying gives the displayed mean for \(n\ge3\); the same expression equals one at \(n=2\).

**4. Variance by orthogonal Bernoulli monomials.** Put \(N=n-1\), \(X_i=T_i-p\), and \(v=p(1-p)\). Conditional on \(T\), the mean of \(B_2\) is
\[
g(T)=1+\frac{S(S+3)}2-e-(1+a)J,
\]
while \(\operatorname{Var}(B_2\mid T)=a(1-a)J\). Using \(T_i^2=T_i\) and \((1+a)p=1\), expansion yields the **exact orthogonal decomposition**
\[
\tag{2}g(T)-\mathbb Eg(T)=(N-1)p\sum_{i=1}^N X_i+
\sum_{\substack{1\le i<j\le N\\j-i\ge2}}X_iX_j-a\sum_{i=1}^{N-1}X_iX_{i+1}.
\]
Distinct centered square-free monomials have zero covariance, since independent centered variables leave at least one factor occurring exactly once. There are \((N-1)(N-2)/2\) nonadjacent pairs and \(N-1\) adjacent pairs. Hence
\[
\operatorname{Var}(g)=N(N-1)^2p^2v+(N-1)\left(\frac{N-2}{2}+a^2\right)v^2.
\]
The conditional-variance contribution is
\[
\mathbb E\operatorname{Var}(B_2\mid T)=a(1-a)(N-1)p^2.
\]
Adding these two terms and substituting \(p=(q-1)/q\), \(a=1/(q-1)\), \(N=n-1\) gives precisely the displayed variance formula. When \(n=2\), the only output is the empty word and both stated moment formulas give the correct boundary values. No asymptotic or sampling argument is used in the proof.

## Verification

Run `python3 checker.py` using Python's standard library. The script directly enumerates the distinct two-deletion outputs of every \(q\)-ary word for \((q,n)\) in \(\{(2,2),\ldots,(2,8),(3,2),\ldots,(3,7),(4,2),\ldots,(4,6)\}\). It compares each output cardinality with the pointwise formula (1), the exact empirical output-count distribution with the conditional Bernoulli/binomial mixture, and the resulting rational mean and variance with the formulas. It also verifies the known binary specialization for \(2\le n\le39\). Replayed result: `PASS: 9240 exhaustive pointwise cases; 18 exact finite-distribution and moment comparisons; 38 binary specialization comparisons.` These checks do not replace the all-parameter proof.

## Relationship to prior work

Li, Wang and Fu's January 10, 2026 work studies extremal cardinalities \(|D_t(w)|\) for nonbinary words with specified run structure and explicitly cites Mercier, Khabbazian and Bhargava (2008) for pointwise small-deletion formulas. Those works show why a purely pointwise two-deletion identity is not by itself a novelty claim. The present claim instead supplies the conditional distribution under the **uniform random input** and an exact all-alphabet variance, including the orientation-cancellation fluctuations absent in binary words. The existing binary two-deletion variance \((n-1)(n-2)(2n-3)/32\) is a proper specialization rather than an independently new result. The 2018 paper of Biers-Ariel, Godbole and Kelley addresses expectations for the total number of distinct subsequences of all lengths, rather than this fixed \(n-2\) output statistic. The 2026 multiset-deletion work deals with unordered rather than ordered received sequences. No inspected source establishes the stated nonbinary conditional binomial mixture or its all-parameter variance.

## Limitations

The distribution depends on uniform independent alphabet symbols; it is not asserted for nonuniform or Markov inputs. The theorem concerns exactly two deletions, distinct ordered outputs, and \(q\ge2\), not arbitrary deletion counts or decoding algorithms. The pointwise two-deletion enumeration alone has known historical antecedents. An inaccessible complete text of Mercier et al. (2008) leaves some historical-priority uncertainty; only its documented scope and the discussion of it in the accessible 2026 source were compared. Independent validation and definitive literature priority remain unperformed.

## References

- Han Li, Xiang Wang and Fang-Wei Fu, *On the Number of Subsequences in the Nonbinary Deletion Channel*, arXiv:2601.06493v1, first public January 10, 2026. https://arxiv.org/html/2601.06493v1
- H. Mercier, M. Khabbazian and V. K. Bhargava, *On the Number of Subsequences When Deleting Symbols From a String*, IEEE Transactions on Information Theory 54 (2008), 3279–3285. https://doi.org/10.1109/TIT.2008.924730
- Y. Biers-Ariel, A. Godbole and E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, Discrete Mathematics and Theoretical Computer Science 19 (2018). https://arxiv.org/abs/1704.08661
- A. Kreindel, I. B. Essayag and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322v1. https://arxiv.org/html/2603.18322v1
