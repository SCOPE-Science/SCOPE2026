# Rank-refined centralizers of corank-one contractions of a finite chain

## Finding
Let \(\mathcal C_n\) be the monoid of weakly increasing, \(1\)-Lipschitz full transformations of \([n]=\{1,\ldots,n\}\), and let \(n\ge3\). For \(1\le i<n\), define
\[
a_{n,i}(j)=\begin{cases}j,&j\le i,\\j-1,&j>i.\end{cases}
\]
These maps, together with their order-reflected conjugates, are **exactly all** the transformations in \(\mathcal C_n\) of image rank \(n-1\). The map \(a_{n,i}\) is nonidempotent for \(i\le n-2\); the endpoint \(i=n-1\) is an idempotent boundary case.

For the full-monoid centralizer \(Z_{n,i}=\{f\in\mathcal C_n: f\circ a_{n,i}=a_{n,i}\circ f\}\), its **complete image-rank generating polynomial** is
\[
P_{n,i}(z)=\sum_{f\in Z_{n,i}}z^{|\operatorname{im} f|}=
\begin{cases}
z\displaystyle\sum_{j=0}^{n-1}z^j,&i=1,\\[5pt]
z(i-1)(1+z)^{i-2}+z(1+z)^{i-1}\displaystyle\sum_{j=0}^{n-i}z^j,&2\le i<n.
\end{cases}
\]
Order reflection preserves this polynomial. Its evaluation at one gives the centralizer cardinality
\[
|Z_{n,i}|=2^{i-2}(2n-i+1),
\]
where for \(i=1\) the right side is interpreted literally and equals \(n\).

The centralizer-rank distributions are **strictly coefficientwise ordered below the top rank**: for \(1\le i<n-1\),
\[
[z^r](P_{n,i+1}-P_{n,i})>0\quad(1\le r<n),\qquad
[z^n](P_{n,i+1}-P_{n,i})=0.
\]
More explicitly, for \(2\le i\le n-2\), putting \(m=n-i\),
\[
P_{n,i+1}(z)-P_{n,i}(z)=z(1+z)^{i-2}\left(1+iz+(1+z)\sum_{j=1}^{m-1}z^j\right),
\]
while \(P_{n,2}(z)-P_{n,1}(z)=z\sum_{j=0}^{n-2}z^j\).

There is also a mixed atomic/continuous **asymptotic centralizer-rank law**. If \(i=i_n\) with \(1\le i_n<n\) and \(i_n/n\to\theta\in[0,1]\), and \(F_n\) is uniform in \(Z_{n,i_n}\), then
\[
\frac{|\operatorname{im}F_n|}{n}\ \Longrightarrow
\frac{\theta}{2-\theta}\,\delta_{\theta/2}
+\frac{2(1-\theta)}{2-\theta}\,\operatorname{Unif}[\theta/2,1-\theta/2].
\]
At \(\theta=0\) this is uniform on \([0,1]\), and at \(\theta=1\) it is the point mass at \(1/2\). In particular, the limit has a genuine atom and a nonzero absolutely continuous component whenever \(0<\theta<1\).

## Assumptions and scope
All transformations are **total** and order-preserving contractions for the ordinary metric on the labeled finite chain, equivalently each adjacent image increment is in \(\{0,1\}\). Composition is ordinary function composition. Image rank means the cardinality of the image, never semigroup generating rank. The centralizer is taken **inside \(\mathcal C_n\)**, not inside all maps on the chain. The theorem is stated for \(n\ge3\), when the nonidempotent part of the corank-one layer is nonempty. At \(n=2\), both corank-one maps are constants, and their centralizer polynomial is \(z+z^2\), agreeing with the formula in the \(i=1\) case; the claimed nonidempotent contribution is empty.

## Proof
**1. Parametrization of the corank-one layer.** Every \(f\in\mathcal C_n\) has a binary word of \(n-1\) adjacent increments, and its image is a consecutive integer interval of cardinality one plus the sum of these increments. Rank \(n-1\) forces exactly one zero increment; the initial value is then either \(1\) or \(2\). Initial value \(1\) gives exactly the maps \(a_{n,i}\), one for each zero-increment position \(i\). Initial value \(2\) gives their order reversals. This partitions the entire corank-one layer into \(2(n-1)\) distinct maps. For \(i<n-1\), the element \(a_{n,i}\) sends \(i+2\) to \(i+1\) and then to \(i\), so is not idempotent; \(a_{n,n-1}\) retracts only the final point and is idempotent.

**2. The commutation constraint.** Fix \(a=a_{n,i}\) and \(f\in\mathcal C_n\). Since every \(j\le i\) is fixed by \(a\), commutation implies \(a(f(j))=f(j)\), and hence \(f(j)\le i\) for all \(j\le i\). Put \(x=f(i)\). If \(x<i\), then \(a^{-1}(x)=\{x\}\). Evaluating commutation at \(i+1\) forces \(f(i+1)=x\); induction at subsequent points forces the entire right tail to equal \(x\). Conversely, any weakly increasing binary-step prefix ending at some \(x<i\), followed by this constant tail, commutes with \(a\). If the prefix has \(h\) one-increments, there are \(\binom{i-1}{h}\) such prefixes for each permitted \(x\in\{h+1,\ldots,i-1\}\). Thus the contribution at rank \(h+1\) is \((i-1-h)\binom{i-1}{h}\). The identity
\[
(i-1-h)\binom{i-1}{h}=(i-1)\binom{i-2}{h}
\]
for \(0\le h\le i-2\) gives the first polynomial summand.

If \(x=i\), commutation at \(i+1\) forces \(f(i+1)\) to lie in \(a^{-1}(i)=\{i,i+1\}\). In general, once a right-tail value exceeds \(i\), all subsequent values increase by precisely one, as the preimage under \(a\) of each value greater than \(i\) is a singleton. Hence the right tail consists of \(s\in\{0,\ldots,n-i\}\) initial zero-increments followed by all one-increments; each \(s\) is possible, and these are all possibilities. The \(i-1\) prefix increments are arbitrary, contributing \(\binom{i-1}{h}\) choices with \(h\) ones. The full image cardinality is \(1+h+(n-i-s)\). Summing independently over \(h\) and \(s\) gives
\[
z(1+z)^{i-1}\sum_{j=0}^{n-i}z^j.
\]
For \(i=1\) only this second case exists. The two cases are disjoint and exhaustive, establishing the polynomial.

**3. Cardinality and strict rank monotonicity.** Evaluating at \(z=1\) yields \((i-1)2^{i-2}+(n-i+1)2^{i-1}=2^{i-2}(2n-i+1)\), also valid for \(i=1\). Direct subtraction of the explicit formulas yields the two displayed positive-factor forms of \(P_{n,i+1}-P_{n,i}\). In each case every coefficient of degree \(1,\ldots,n-1\) is strictly positive, and the degree-\(n\) terms cancel. No coefficientwise statement beyond this corank-one layer is asserted.

**4. Asymptotic law.** Split the centralizer into the two cases in step 2. For \(i\ge2\), the first class has size \(A=(i-1)2^{i-2}\) and image rank distribution \(1+\operatorname{Bin}(i-2,1/2)\); the second has size \(B=(n-i+1)2^{i-1}\) and image rank distribution \(1+\operatorname{Bin}(i-1,1/2)+U\), where \(U\) is independent and uniform on \(\{0,1,\ldots,n-i\}\). For \(i=1\), the first class is empty and the second rank is uniform on \(\{1,\ldots,n\}\). Since \(A/(A+B)\to\theta/(2-\theta)\), the law of large numbers implies that both scaled binomials converge in probability to \(\theta/2\), and the scaled uniform term converges to \(\operatorname{Unif}[0,1-\theta]\). The mixture then converges to the stated law. The endpoint cases follow by the same argument without requiring both mixture weights to be nonzero.

## Verification
The standalone `verify.py` exhaustively enumerates every \(f\in\mathcal C_n\) for each \(2\le n\le10\), using its initial value and binary step word. It computes composition independently as literal values on all chain points. It checks every coefficient of the centralizer rank polynomial for all \(a_{n,i}\) and every reflected counterpart, along with cardinalities, coefficientwise differences, and the displayed positive-factor difference for all applicable \(i\). Run `python3 verify.py`. Successful output ends with `ALL_CORANK_COMMUTANT_TESTS_PASSED`. This is finite corroboration, not a proof of the infinite-parameter classification or the weak convergence theorem.

For an explicit check, when \(n=5\), the polynomials as \(i\) runs from one to four are
\[
\begin{aligned}
P_{5,1}&=z+z^2+z^3+z^4+z^5,\\
P_{5,2}&=2z+2z^2+2z^3+2z^4+z^5,\\
P_{5,3}&=3z+5z^2+4z^3+3z^4+z^5,\\
P_{5,4}&=4z+10z^2+9z^3+4z^4+z^5.
\end{aligned}
\]
Their sums are \(5,9,16,28\), respectively.

## Relationship to prior work
Adeshola and Umar (arXiv:1303.7428, first posted March 29, 2013) establish the elementary counting and fixed-point structure of the *same* order-preserving full contraction monoid, including its rank distributions; their enumerations do not include the commutation equation for a specified nonidempotent. Fernandes and Paulista (arXiv:2112.13427, first posted December 26, 2021) consider the same monoid as weak endomorphisms of a directed path, focusing on generating rank and regularity, rather than rank-refined nonidempotent centralizers.

A separate published result, *Centralizer profiles and a quadratic limit law for idempotent finite-chain contractions* (October 2026; URL below), gives complete centralizer **cardinalities of idempotents** and a limit law for logarithms of those cardinalities under uniformly sampled idempotents. The \(i=n-1\) boundary of the present cardinality formula is covered by that result and is **not claimed new**. The present nonidempotent corank-one rank polynomials, strict coefficientwise ordering, and mixed atomic/uniform rank distribution are distinct statements. Another related result, *Logarithmic power stabilization for finite-chain order-preserving contractions*, concerns repeated powers of random elements, not their centralizers. The previously published Bernoulli convolution theorem for the order-decreasing submonoid concerns independent products and does not determine the centralizer spectra here. Searches and full-text comparisons did not identify a dominating prior theorem, but this is not a proof of historical uniqueness.

## Limitations
The theorem treats only a fixed element of image rank \(n-1\) and its full-monoid centralizer. It does not classify centralizers of arbitrary lower-rank nonidempotents or arbitrary commuting pairs. It makes no assertion about centralizers in the full transformation monoid or non-monotone contractions. The mixed limit describes uniform elements **conditional on a specified corank-one map** with a scaling condition; it does not sample a uniform pair of commuting elements without that conditioning. The nonidempotent segment \(1\le i\le n-2\) is the intended new mathematical domain; the idempotent endpoint is retained for exact boundary consistency. The priority comparison is best-evidence and has not been independently audited.

## References
1. A. D. Adeshola and A. Umar, *Combinatorial results for certain semigroups of order-preserving full contraction mappings of a finite chain*, arXiv:1303.7428v1 (2013-03-29), https://arxiv.org/abs/1303.7428.
2. V. H. Fernandes and T. Paulista, *On the Rank of Monoids of Endomorphisms of a Finite Directed Path*, arXiv:2112.13427v1 (2021-12-26), https://arxiv.org/abs/2112.13427.
3. *Centralizer profiles and a quadratic limit law for idempotent finite-chain contractions*, public 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-centralizer-profiles-and-a-quadratic-limit-law-for-idempotent-fi--22387dfffecf.
4. *Logarithmic power stabilization for finite-chain order-preserving contractions*, public 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-logarithmic-power-stabilization-for-finite-chain-order-preservin--477eedb64580.
5. *Bernoulli convolution and logarithmic collapse in order-decreasing chain contractions*, public 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-bernoulli-convolution-and-logarithmic-collapse-in-order-decreasi--9b3cad5ffea5.
