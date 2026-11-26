# Long-range inversions suppress cycle count in uniform permutations
## Finding
Let \(\Pi\) be uniform on the symmetric group \(S_n\), where \(n\ge 2\), and let \(C_n\) denote its number of cycles. For positions \(1\le a<b\le n\), put \(I_{a,b}=\mathbf 1\{\Pi(a)>\Pi(b)\}\) and \(d=b-a\). Then
\[
\mathbb E[C_n\mid I_{a,b}=1]
=H_n-\frac{2d-1}{n(n-1)},
\qquad
\operatorname{Cov}(C_n,I_{a,b})
=-\frac{2d-1}{2n(n-1)}.
\]
Thus inversions spanning more positions have strictly stronger negative covariance with cycle count. Summing over all position pairs gives, for the usual inversion count \(\operatorname{Inv}_n\),
\[
\operatorname{Cov}(C_n,\operatorname{Inv}_n)
=-\frac{2n-1}{12}.
\]
For the Mallows family \(\mathbb P_q(\pi)\propto q^{\operatorname{Inv}(\pi)}\), if \(\mu_n(q)=\mathbb E_q C_n\), then
\[
\mu_n'(1)=-\frac{2n-1}{12}.
\]
Equivalently, under the inverse-temperature parameterization \(q=e^{-\beta}\),
\[
\mu_n(e^{-\beta})=H_n+\frac{2n-1}{12}\,\beta+O(\beta^2)
\quad\text{as }\beta\to0.
\]

## Assumptions and scope
The permutation is uniform on \(S_n\) for the covariance statements, with \(n\ge2\). The local statistic \(I_{a,b}\) refers to positions, not values. The Mallows derivative is the ordinary finite-state derivative at \(q=1\), so no interchange of an infinite limit and differentiation is used. Here \(H_n=\sum_{j=1}^n j^{-1}\).

## Proof
First use a completion lemma for partial permutations. Prescribe \(r\) distinct images at \(r\) distinct domain points. The resulting directed partial permutation consists of forced directed cycles and open directed path components, with isolated vertices counted as open paths. If \(c_0\) forced cycles are already present, contraction of every open path turns a uniform completion into a uniform permutation on \(n-r\) contracted components. Hence
\[
\mathbb E[C_n\mid\text{the prescribed edges}]=c_0+H_{n-r}.
\]

Apply this with the two prescribed edges \(a\mapsto x\) and \(b\mapsto y\), where \(x\ne y\). The forced-cycle count is
\[
c_0(x,y)=\mathbf 1\{x=a\}+\mathbf 1\{y=b\}+\mathbf 1\{x=b,\ y=a\}.
\]
Consequently
\[
\mathbb E[C_n\mid\Pi(a)=x,\Pi(b)=y]=H_{n-2}+c_0(x,y).
\]
Among the \(n(n-1)/2\) ordered value pairs satisfying \(x>y\), the total contribution of \(c_0\) is
\[
(a-1)+(n-b)+1=n-(b-a)=n-d.
\]
It follows that
\[
\mathbb E[C_n I_{a,b}]
=\frac12H_{n-2}+\frac{n-d}{n(n-1)}.
\]
Since \(\mathbb E C_n=H_n\), \(\mathbb E I_{a,b}=1/2\), and
\[
H_n-H_{n-2}=\frac{2n-1}{n(n-1)},
\]
subtraction gives
\[
\operatorname{Cov}(C_n,I_{a,b})
=-\frac{2d-1}{2n(n-1)}.
\]
The displayed conditional mean follows by doubling \(\mathbb E[C_n I_{a,b}]\).

Finally,
\[
\operatorname{Inv}_n=\sum_{1\le a<b\le n}I_{a,b},
\]
and grouping pairs by \(d=b-a\) yields
\[
\sum_{d=1}^{n-1}(n-d)(2d-1)=\frac{n(n-1)(2n-1)}6.
\]
Summing the local covariance therefore gives \(\operatorname{Cov}(C_n,\operatorname{Inv}_n)=-(2n-1)/12\).

For Mallows permutations,
\[
\frac{d}{dq}\mathbb E_q C_n
=\frac1q\operatorname{Cov}_q(C_n,\operatorname{Inv}_n),
\]
which at \(q=1\) proves the stated linear response.

## Verification
The accompanying exact-arithmetic checker independently exhausts all permutations through \(n=9\), verifies the two-edge completion formula through \(n=7\), checks every local position pair through \(n=9\), and checks the global covariance for each \(2\le n\le9\). It reports 1,624 partial-completion checks, 240 local conditional-mean/covariance checks, 8 global covariance checks, and 409,112 enumerated permutation states. These finite checks are consistency tests; the all-\(n\) result is established by the analytic proof above.

## Relationship to prior work
The standard Mallows model weights a permutation by a power of its inversion count. Gladkich and Peled, *On the Cycle Structure of Mallows Permutations* (arXiv:1601.06991), study cycle structure and give order-of-magnitude behavior for the expected number of cycles across Mallows regimes. He, Müller, and Verstraaten, *Cycles in Mallows random permutations* (arXiv:2201.11610), develop further asymptotic cycle-count results. The inspected statements do not give the finite-\(n\) derivative at \(q=1\) or the distance-resolved covariance above.

A related bivariate equidistribution is proved by Chen, Gong, and Guo, *The Sorting Index and Permutation Codes* (arXiv:1206.0503): the pair consisting of sorting index and cycle count is equidistributed with inversion number and right-to-left minima. This does not identify the joint law, or even the covariance, of inversion number with cycle count itself.

## Limitations
The theorem is a first-order dependence statement. It does not determine the full joint distribution of \(C_n\) and \(\operatorname{Inv}_n\), higher mixed moments, or the sign of every nonlinear dependence functional. The originality search was broad but cannot rule out an older equivalent mixed-moment identity written under different permutation-statistic notation.

## References
1. H. Chen, G. Gong, and J. Guo, *The Sorting Index and Permutation Codes*, arXiv:1206.0503, first submitted 2012-06-04.
2. A. Gladkich and R. Peled, *On the Cycle Structure of Mallows Permutations*, arXiv:1601.06991, first submitted 2016-01-26.
3. J. He, T. Müller, and T. Verstraaten, *Cycles in Mallows random permutations*, arXiv:2201.11610.
