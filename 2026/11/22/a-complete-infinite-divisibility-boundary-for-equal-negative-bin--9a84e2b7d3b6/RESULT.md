# A complete infinite-divisibility boundary for equal negative-binomial row totals

## Finding
Let \(c,r\) be positive integers, let \(q_1,\ldots,q_r\in(0,1)\), and let \(U_i\), independently, have negative-binomial law \(\Pr(U_i=n)=\binom{n+c-1}{n}(1-q_i)^c q_i^n\), \(n\ge0\). Define \(N=U_1\) conditional on \(U_1=\cdots=U_r\), and put \(w=\prod_{i=1}^r q_i\). Then \(N\) is infinitely divisible under ordinary addition **if and only if**
\[
\boxed{c=1\quad\text{or}\quad r=1\quad\text{or}\quad(c,r)=(2,2).}
\]
This classification is independent of all individual \(q_i\). In the exceptional \((2,2)\) case the law is compound Poisson with a strictly positive intensity at every jump size \(k\ge1\):
\[
\boxed{\nu_k=\frac{[3+(-1)^{k-1}]w^k}{k}.}
\]
Outside those cases, the obstruction already occurs in the quadratic logarithmic probability-generating-function coefficient; it is strictly negative for every \(0<w<1\).

## Assumptions and scope
All row shapes are the *same positive integer* \(c\); there are \(r\ge1\) independent rows; the row parameters \(q_i\) may differ but lie strictly between zero and one. Only the **zero-difference fiber** \(U_1=\dots=U_r\) is treated. Infinite divisibility means that for every integer \(m\ge1\) the law is an additive convolution of \(m\) identical probability laws, with no restriction imposed on the summands in the definition. The atom at zero is positive; thus any additive root must itself be supported on nonnegative integers, as explained below.

## Proof
The fiber law follows directly from independence, or from DeSalvo's hyper-negative-binomial formula for zero offsets. Put
\[
B_{c,r}(z)=\sum_{n\ge0}\binom{n+c-1}{n}^{r}z^n,\qquad G(z)=\frac{B_{c,r}(wz)}{B_{c,r}(w)}.
\]
The normalizer is finite for \(0<w<1\), and \(G\) is the probability generating function of \(N\). Its expansion at zero has the form
\[
\log G(z)=\operatorname{constant}+c^r w z+\left[\binom{c+1}{2}^{r}-\frac{c^{2r}}2\right]w^2z^2+O(z^3).
\]
For a nonnegative integer law with positive mass at zero, infinite divisibility forces every positive-degree Taylor coefficient of \(\log G\) to be nonnegative. To see the needed degree-two assertion without invoking a general theorem, let \(m\) be a proposed number of iid additive summands. Because \(N\) is nonnegative with \(\Pr(N=0)>0\), the essential infimum of each iid summand is zero and each has an atom at zero. Since the sum is integer-valued, any positive-support value of one summand paired with zeros in the other \(m-1\) summands must be integer; hence each summand is nonnegative integer-valued. Its generating function must equal \(G(z)^{1/m}\), using the branch positive at zero. Writing \(G(z)=p_0(1+a_1z+a_2z^2+\cdots)\), the quadratic coefficient of this root is
\[
p_0^{1/m}\frac1m\left[a_2-\frac{1-1/m}{2}a_1^2\right].
\]
If \(a_2-a_1^2/2<0\), this becomes negative for sufficiently large integer \(m\), a contradiction.

Here \(a_1=c^r w\) and \(a_2=\binom{c+1}{2}^rw^2\). Therefore a strictly negative quadratic coefficient is equivalent to
\[
\left(\frac{c+1}{2c}\right)^r<\frac12.
\]
For \(c\ge3,r\ge2\), the left side is at most \((2/3)^2=4/9\). For \(c\ge2,r\ge3\), it is at most \((3/4)^3=27/64\). Both are strictly below \(1/2\). Thus none of these laws is infinitely divisible.

For \(c=1\), \(B_{1,r}(z)=(1-z)^{-1}\), so \(N\) is geometric and infinitely divisible. For \(r=1\), \(B_{c,1}(z)=(1-z)^{-c}\), so \(N\) is negative binomial and infinitely divisible. Explicitly the two cases have compound-Poisson rates \(w^k/k\) and \(cw^k/k\), respectively.

The only remaining integer pair is \((c,r)=(2,2)\). The identity
\[
B_{2,2}(z)=\sum_{n\ge0}(n+1)^2z^n=\frac{1+z}{(1-z)^3}
\]
gives
\[
G(z)=\frac{(1-w)^3}{1+w}\frac{1+wz}{(1-wz)^3},\quad
\log G(z)=\sum_{k\ge1}\frac{[3+(-1)^{k-1}]w^k}{k}(z^k-1).
\]
All rates \(\nu_k\) are positive; their sum converges since \(0<w<1\). This is the generating function of an ordinary compound-Poisson count with intensity measure \(\{\nu_k\}_{k\ge1}\). All cases are covered, proving the theorem.

## Verification
The accompanying standalone `check.py` uses exact integer/Fraction arithmetic to check the shape-region inequalities and quadratic Taylor coefficients for a finite parameter census, verifies the exact exceptional Eulerian identity and initial compound-Poisson coefficients, and checks normalization in several exact rational instances. Finite checks do not replace the general inequalities and power-series proof. Reproduce with `python3 check.py` (Python 3 standard library only).

## Relationship to prior work
DeSalvo (2026, arXiv:2611.00275, Theorem 3.2) supplies the general hyper-negative-binomial conditional count law and its normalizer, but does not state the infinite-divisibility classification established here. The standard compound-Poisson criterion for nonnegative-integer infinitely divisible laws and negative-binomial divisibility are classical; the proof above needs only a direct convolution-root argument for the obstruction and explicit exponentials for the positive cases. The distinct published classification for maxima of geometric samples, with a different probability-generating function, does not imply this result by a stochastic mapping or parameter substitution. The related 2016 generalized negative-binomial coherent-state model has a different probability mass function and its quasi-infinite-divisibility statements do not establish this fiber classification.

## Limitations
No claims are made for noninteger row shape, unequal row shapes, or nonzero observed differences. The result classifies ordinary infinite divisibility of the conditioned row total, not finite additive decomposability, multiplicative divisibility or independence of geometric entries after conditioning. Novelty assessment is limited to the inspected literature and retrieved records; a previously unlocated polynomial-weighted discrete-distribution theorem may imply the same classification. Independent review has not been performed.

## References
1. Stephen DeSalvo, *Stein's method for negative binomial and hyper-negative-binomial laws, with applications*, arXiv:2611.00275 (first posted 2026-10-30), especially §3 and Theorem 3.2, https://arxiv.org/html/2611.00275v1 .
2. F. W. Steutel and K. van Harn, *Infinite Divisibility of Probability Distributions on the Real Line* (2004), discrete compound-Poisson theory, https://www.nzdr.ru/data/media/biblio/kolxoz/M/MV/Steutel%20F.%2C%20van%20Harn%20K.%20Infinite%20divisibility%20of%20probability%20distributions%20on%20real%20line%20%28Dekker%2C%202004%29%28ISBN%200824707249%29%28546s%29_MV_.pdf .
3. Hassan Chhaiba, Nizar Demni, Zouhair Mouayn, *Analysis of generalized negative binomial distributions attached to hyperbolic Landau levels*, arXiv:1602.01371 (2016), https://arxiv.org/abs/1602.01371 .
