# Eight is the sharp support threshold for failure of integer-mean medianity under discrete log-concavity

## Finding

**Theorem (sharp support threshold).** Let \(X\) be an integer-valued random variable whose probability mass function has finite, contiguous support and is log-concave: whenever three consecutive points belong to its support, their probabilities \(p_j\) satisfy \(p_j^2\ge p_{j-1}p_{j+1}\). Suppose that \(\mathbb E X=m\in\mathbb Z\).

If the support contains at most seven points, then
\[
\Pr(X<m)<\frac12<\Pr(X\le m),\qquad
\Pr(X>m)<\frac12<\Pr(X\ge m).
\]
In particular, \(m\) is the unique median. The support-length cutoff is sharp: there is an eight-point, strictly positive log-affine mass function with integer mean \(5\) and \(\Pr(X\le5)<1/2\). Therefore eight is the smallest contiguous support cardinality on which an integer-mean discrete log-concave distribution can fail to have its mean as a median.

The eight-point example was already described by Alqasem, Aravinda, Marsiglietti and Melbourne [1]. The additional assertion established here is **minimality**: all supports of length at most seven necessarily retain the median property.

## Assumptions and scope

A log-concave mass function has support \(\{a,a+1,\ldots,b\}\subset\mathbb Z\), with every supported mass strictly positive and \(p_j^2\ge p_{j-1}p_{j+1}\). Its support size is \(n=b-a+1\). An integer \(m\) is a median when both \(\Pr(X\le m)\ge 1/2\) and \(\Pr(X\ge m)\ge1/2\). Here, the expectation is required to be an integer; the theorem does not assert an analogous result for noninteger expectations or infinite support.

For integers \(r\ge2\) and \(1\le j\le r-2\), define
\[
Z_r(q)=\sum_{i=0}^{r-1}q^i,\quad
H_{r,j}(q)=\sum_{i=0}^{r-1}(i-j)q^i,\quad
D_{r,j}(q)=\sum_{i=j+1}^{r-1}q^i-\sum_{i=0}^{j}q^i.
\]
The sign of \(H_{r,j}(q)\) is the sign of the difference between the expectation of the truncated geometric distribution with weights \(q^i\) and \(j\). The sign of \(D_{r,j}(q)\) determines whether its upper-tail mass above \(j\) exceeds one half.

## Proof

**1. Localization to truncated geometric laws.** Translation permits the original support to lie inside \(\{0,\ldots,n-1\}\), where \(n\le7\), with integer mean \(m\). Consider the collection of all log-concave laws on that finite ambient support satisfying \(\mathbb E X\le m\), and maximize the linear functional \(\Pr(X>m)\). The discrete localization theorem of Marsiglietti and Melbourne [2, Theorem 2.10] states that this maximum is attained by a log-affine law on some contiguous subinterval \(\{a,\ldots,b\}\): its masses are proportional to \(q^{i-a}\) for some \(q>0\). The assumption of a linear *half-space* moment constraint, rather than fixed equality, is deliberate: it is precisely the setting of that theorem.

If \(b\le m\), the upper tail is zero. If \(a=m\), the moment constraint forces the point mass at \(m\), also with zero upper tail. Otherwise, \(a<m<b\). Set \(r=b-a+1\le7\) and \(j=m-a\), so \(1\le j\le r-2\). Let \(I\) have the truncated geometric law
\[
\Pr_q(I=i)=\frac{q^i}{Z_r(q)},\qquad 0\le i\le r-1,\ q>0.
\]
Its expectation \(M_r(q)=\sum_i i q^i/Z_r(q)\) has derivative with respect to \(\log q\) equal to \(\operatorname{Var}_q(I)>0\). Therefore there is a unique \(q_*\in(0,\infty)\) with \(M_r(q_*)=j\), and the feasible parameters satisfy \(q\le q_*\).

The upper-tail probability \(T_{r,j}(q)=\Pr_q(I>j)\) is strictly increasing with \(\log q\): its derivative is \(\operatorname{Cov}_q(\mathbf1_{\{I>j\}},I)>0\), since both sides of the threshold have positive mass. Consequently, its largest feasible value occurs at \(q_*\), where \(H_{r,j}(q_*)=0\). This reduction is valid for every possible subinterval, not just for the original full support.

**2. Exact exhaustive rational certificates through seven support points.** The following table gives one rational \(q_0\) for each of the 15 possible pairs \((r,j)\) with \(3\le r\le7\) and \(1\le j\le r-2\). Direct rational evaluation yields \(H_{r,j}(q_0)>0\) and \(D_{r,j}(q_0)<0\) in every entry.

| \(r\) | \(j\) | \(q_0\) | \(r\) | \(j\) | \(q_0\) |
|---:|---:|:---:|---:|---:|:---:|
|3|1|\(3/2\)|6|1|\(2/3\)|
|4|1|\(2/3\)|6|2|\(6/7\)|
|4|2|\(5/3\)|6|3|\(5/4\)|
|5|1|\(2/3\)|6|4|\(17/9\)|
|5|2|\(7/6\)|7|1|\(2/3\)|
|5|3|\(9/5\)|7|2|\(4/5\)|
| | | |7|3|\(13/12\)|
| | | |7|4|\(17/13\)|
| | | |7|5|\(31/16\)|

Because \(H_{r,j}(q_0)>0\), the strict monotonicity of \(M_r\) gives \(q_*<q_0\). Because \(D_{r,j}(q_0)<0\), the normalized upper tail satisfies \(T_{r,j}(q_0)<1/2\). Thus \(T_{r,j}(q_*)<T_{r,j}(q_0)<1/2\) for every possible extremizer. Localization proves \(\Pr(X>m)<1/2\) for every admissible law with \(\mathbb E X=m\).

Apply the same argument to \(-X\), whose support remains contiguous and whose mass function remains log-concave, with integer mean \(-m\). It follows that \(\Pr(X<m)<1/2\). Therefore \(\Pr(X\ge m)>1/2\) and \(\Pr(X\le m)>1/2\), establishing the unique-median assertion. If \(n=1\) or \(n=2\), an integer mean is necessarily a support endpoint and only the point-mass case is possible; the same conclusion holds.

**3. The sharp eight-point obstruction.** Let \(q_*\) be the unique positive solution of \(H_{8,5}(q_*)=0\), and define the eight-point law
\[
\Pr(X=i)=\frac{q_*^i}{Z_8(q_*)},\qquad i\in\{0,1,\ldots,7\}.
\]
The expectation is exactly \(5\). The exact rational evaluations
\[
H_{8,5}(34/25)=-\frac{5507579937}{6103515625}<0,
\qquad H_{8,5}(11/8)=\frac{416103}{1048576}>0
\]
locate \(q_*\) strictly between \(34/25\) and \(11/8\). Moreover,
\[
D_{8,5}(34/25)=\frac{819586169}{6103515625}>0.
\]
Hence \(T_{8,5}(34/25)>1/2\), and strict monotonicity gives \(T_{8,5}(q_*)>1/2\), or \(\Pr(X\le5)<1/2\). All eight masses are positive, and their constant successive ratio implies log-concavity with equality at every interior point. The eight-point example and the seven-point impossibility together prove the sharp cutoff. \(\square\)

## Verification

The file `verify.py` uses only the Python standard library and exact `Fraction` arithmetic. Running `python verify.py` checks that the witness table covers precisely all 15 pairs, verifies the two polynomial signs for every rational witness, and reproduces the exact eight-point rational signs and root bracket. Its successful execution is a finite rational certificate for the enumerated sign comparisons; the reduction from arbitrary log-concave distributions to these comparisons depends on the cited analytic localization theorem and the independently stated monotonicity arguments, not on exhaustive sampling of distributions.

## Relationship to prior work

Alqasem, Aravinda, Marsiglietti and Melbourne [1, Corollary 1.4] establish the general \(e^{-1}\) lower bound for mass at or below an integer mean and explicitly exhibit an eight-point log-affine example where the stronger one-half bound fails. That example establishes *sufficiency* of eight points, not that no shorter support can fail. Their statement does not contain the seven-point universal theorem proved here.

Marsiglietti and Melbourne [2, Theorem 2.10] provide the fundamental extremal localization argument; the reduction to truncated geometric laws is therefore prior work, not claimed as new. The additional support-optimality fact comes from combining this localization with the exhaustive, exact fifteen-case separation. A general one-half bound for Poisson, Poisson-binomial, or uniform examples is more specialized and does not imply the claim for every log-concave law of length at most seven.

## Limitations

The integer-mean and consecutive finite-support assumptions are essential to this statement. No claim is made for noninteger means, larger or infinite supports, or quantitative sharp improvements above one half. The eight-point example is previously known. The presently documented search did not locate an earlier proof of the seven-point impossibility, but a logically equivalent earlier formulation under other terminology cannot be excluded; no independent priority audit has been carried out.

## References

1. A. Alqasem, H. Aravinda, A. Marsiglietti, J. Melbourne, *On a Conjecture of Feige for Discrete Log-Concave Distributions*, arXiv:2208.12702 (first public version 2022-08-26), especially Corollary 1.4 and the following eight-point example. https://arxiv.org/html/2208.12702v2
2. A. Marsiglietti, J. Melbourne, *Geometric and Functional Inequalities for Log-Concave Probability Sequences*, arXiv:2004.12005 (first public version 2020-04-24), especially Theorem 2.10. https://arxiv.org/html/2004.12005v4
