# Affine descent–inversion covariance and a sharp six-letter sign boundary

## Finding
Let \(W=(W_1,\ldots,W_n)\) be uniformly random among the distinct rearrangements of an ordered multiset with \(m_a\geq1\) copies of label \(a\in\{1,\ldots,d\}\), where \(n=\sum_a m_a\geq3\). Define the number of inversions \(I=\sum_{u<v}\mathbf1\{W_u>W_v\}\), descent indicators \(D_i=\mathbf1\{W_i>W_{i+1}\}\), and major index \(M=\sum_{i=1}^{n-1}iD_i\). Write
\[
T=\sum_{a<b}m_am_b,\qquad S=\sum_{a<b}m_am_b(m_b-m_a).
\]
Then the entire descent-location versus inversion covariance profile is **affine**:
\[
\boxed{\operatorname{Cov}(D_i,I)=\frac{T}{2n(n-1)}+\frac{(i-n/2)S}{n(n-1)(n-2)}\qquad(1\le i<n).}
\]
In particular, \(\operatorname{Cov}(D_i,I)+\operatorname{Cov}(D_{n-i},I)=T/[n(n-1)]\), the profile has at most one change of sign, and the first and last covariances are \((T-S)/[2n(n-1)]\) and \((T+S)/[2n(n-1)]\). Strict negative positional covariance occurs exactly when \(|S|>T\), and then at the first or last position according to the sign of \(S\).

The resulting major-index covariance is
\[
\boxed{\operatorname{Cov}(M,I)=\frac{3T+S}{12}.}
\]
Although \(M\) and \(I\) are equidistributed, their covariance can be negative: it is nonnegative for **every** ordered multiset of size at most five; at size five, among nonconstant words equality holds only for multiplicities \((4,1)\), with the larger multiplicity on the lower label. At size six, negativity occurs **only** for multiplicities \((5,1)\) in this order, giving \(\operatorname{Cov}(M,I)=-5/12\). For \((m_1,m_2)=(n-1,1)\), the covariance equals \((n-1)(5-n)/12\) and is negative for every \(n\ge6\).

## Assumptions and scope
The alphabet is totally ordered, all listed multiplicities are positive integers and the probability measure is uniform on distinct multiset words (not on compositions or independent draws). A one-label alphabet is permitted, with \(T=S=I=M=0\). For \(n=2\), the positional formula is replaced by \(\operatorname{Cov}(D_1,I)=T/4\), and the aggregate formula \((3T+S)/12\) remains valid; for \(n=1\) both statistics are zero. The claim concerns exact finite-population moments, not asymptotic independence, joint normality, or distributional stochastic ordering.

## Proof
**1. The descent probability and mirror identity.** Every pair of distinct positions samples without replacement from the same multiset, so \(p=\mathbb P(D_i=1)=T/[n(n-1)]\). Put \(U_i=\mathbf1\{W_i<W_{i+1}\}\) and \(c_i=\operatorname{Cov}(D_i,I)\). Swapping positions \(i,i+1\) is a bijection from descents to ascents and removes exactly one inversion; all other inversion pairs have unchanged combined contribution. Because \(\mathbb P(D_i=1)=\mathbb P(U_i=1)=p\), this gives \(c_i-\operatorname{Cov}(U_i,I)=p\). Reversing the word maps \(D_i\) to \(U_{n-i}\) and maps \(I\) to \(T-I\), so \(c_i=-\operatorname{Cov}(U_{n-i},I)\). Therefore \(c_i+c_{n-i}=p\).

**2. Consecutive location differences.** In the expansion of \(I\) into inversion-pair indicators, only pairs involving positions \(i\) or \(i+1\) can distinguish how many positions precede and follow that adjacent pair. Fix three distinct position indices carrying \(A=W_i\), \(B=W_{i+1}\), and \(C\) elsewhere. For one earlier position, the covariance contribution involving \(C\) is
\[
K_-=\operatorname{Cov}\big(\mathbf1\{A>B\},\mathbf1\{C>A\}+\mathbf1\{C>B\}\big).
\]
For one later position it is
\[
K_+=\operatorname{Cov}\big(\mathbf1\{A>B\},\mathbf1\{A>C\}+\mathbf1\{B>C\}\big).
\]
All remaining contributions, including the pair \((i,i+1)\) and pairs disjoint from it, are independent of \(i\) by exchangeability of the uniformly shuffled multiset. Consequently \(c_{i+1}-c_i=K_- -K_+\) for every \(1\le i\le n-2\). Let \(\operatorname{sgn}(0)=0\). Since \(A,B,C\) are exchangeable, \(\mathbb E[\operatorname{sgn}(C-A)+\operatorname{sgn}(C-B)]=0\). Thus
\[
K_- -K_+=\mathbb E\big[\mathbf1\{A>B\}(\operatorname{sgn}(C-A)+\operatorname{sgn}(C-B))\big].
\]
Count ordered triples of **distinct physical copies**. When \(A,B,C\) have three different label values \(a<b<c\), their contributions cancel in pairs: if \((A,B)\) is the descending pair \((b,a),(c,a),(c,b)\), the sign sums are \(+2,0,-2\), respectively. When \(A>B\) and \(C=A\), the sign sum is \(+1\) and the count is \(m_bm_a(m_b-1)\) for \(A=b,B=a\). When \(C=B\), it is \(-1\) with count \(m_bm_a(m_a-1)\). The net numerator is precisely \(S\). Dividing by the ordered triple count \(n(n-1)(n-2)\), one obtains
\[
c_{i+1}-c_i=\frac{S}{n(n-1)(n-2)}.
\]
An affine sequence whose mirror-pair sum is \(p\) must satisfy the boxed positional formula. The strict-sign and at-most-one-transition assertions follow from its slope and endpoints.

**3. Weighted sum and sharp minimality.** Summing \(i c_i\) over all positions yields
\[
\operatorname{Cov}(M,I)=\frac T4+\frac S{12}=\frac{3T+S}{12},
\]
because \(\sum_{i=1}^{n-1}i(i-n/2)=n(n-1)(n-2)/12\). For each \(a<b\), the multiplicity gap \(m_b-m_a\) lies between \(-(n-2)\) and \(n-2\); therefore \(|S|\le(n-2)T\). Hence \(3T+S\ge(5-n)T\), proving nonnegativity through size five. With \(T>0\), equality at \(n=5\) forces \(m_b-m_a=-3\) for every contributing pair, possible only for exactly two distinct labels with multiplicities \((4,1)\). For \(n=6\), negativity requires \(S<-3T\). If there is more than one pair of distinct labels or both multiplicities exceed one, every gap is at least \(-3\), implying \(S\ge-3T\); the sole exception is a two-label profile \((5,1)\), for which \(S=-4T=-20\), giving covariance \(-5/12\). The claimed all-size \((n-1,1)\) identity follows by direct substitution. For \(n=2\), direct enumeration of the at most two distinct words supplies the boundary formula.

## Verification
The accompanying `CHECK.py` independently enumerates each distinct word and computes covariance from exact rational moments; it does not use the theorem's derivation. It checks 161 multiplicity vectors of total size at most eight with up to four labels, totaling 2,356 exact rational or symmetry assertions, plus the size-six uniqueness condition and the two-label all-size formula at twenty-five additional sizes. Run `python CHECK.py`. The finite checks corroborate but do not prove the all-size theorem; the argument above supplies that proof.

## Relationship to prior work
Conger and Viswanath (first publicly posted 2005) study random multiset permutations, their inversion and descent indicator joint probabilities, and normal approximation for the *marginal* total counts; their inversion-indicator probabilities already provide inputs from which moment sums can in principle be reconstructed. Thiel (first posted 2013) gives a joint inversion/major-index generating-function recurrence for multiset words and the leading mixed covariance of a growing-multiplicity regime. Thus neither the ordinary marginal moments nor the existence of a joint generating function is asserted as new. The specific finite, position-resolved affine covariance law, its single-transition classification, and the sharp six-letter negative-covariance boundary are the asserted contribution. Prior exact-moment methods constitute an implicit-coverage risk; no independent priority guarantee is made.

## Limitations
The sign boundary is for the *uniform fixed-multiplicity* law. It need not hold for iid categorical sequences or other nonexchangeable models. The signs depend on the order of labels, not merely the unordered multiplicity partition. The result is a second-moment identity; it does not establish conditional stochastic dominance, a joint limit theorem, or independence of \(M\) and \(I\). Explicit enumeration was performed only in the finite ranges stated. A general earlier multivariate generating function may imply the finite covariance after differentiation; this is not presented as a new generating function or a previously unknown marginal statistic.

## References
1. Mark Conger and D. Viswanath, *Normal Approximations for Descents and Inversions of Permutations of Multisets*, arXiv:math/0508242, first version 2005-08-14, https://arxiv.org/abs/math/0508242.
2. Marko Thiel, *The Inversion Number and the Major Index Are Asymptotically Jointly Normally Distributed on Words*, arXiv:1302.6708, first version 2013-02-27, https://arxiv.org/abs/1302.6708.
3. Andrew Baxter and Doron Zeilberger, *The Number of Inversions and the Major Index of Permutations Are Asymptotically Joint-Independently Normal*, arXiv:1004.1160, https://arxiv.org/abs/1004.1160.
