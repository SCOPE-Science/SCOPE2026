# A parabolic fixed-point profile inside Spearman's permutation null
## Finding
Let \(\Pi\) be uniformly distributed on the symmetric group \(S_n\), with \(n\ge2\). Put
\[
I_i=\mathbf 1\{\Pi(i)=i\},\qquad F=\sum_{i=1}^n I_i,
\]
and define Spearman's rank correlation under the permutation null by
\[
\rho
=1-\frac{6\sum_{j=1}^n(j-\Pi(j))^2}{n(n^2-1)}.
\]
Then every fixed-point location has the exact conditional profile
\[
\boxed{
\mathbb E[\rho\mid I_i=1]
=\frac{3(2i-n-1)^2}{(n-1)^2(n+1)}
}
\]
and hence
\[
\boxed{
\operatorname{Cov}(I_i,\rho)
=\frac{3(2i-n-1)^2}{n(n-1)^2(n+1)}.
}
\]
Summing over the fixed-point locations gives
\[
\boxed{
\operatorname{Cov}(F,\rho)=\frac1{n-1}.
}
\]
Moreover, under the same permutation null,
\[
\mathbb EF=1,\qquad \operatorname{Var}(F)=1,
\qquad \mathbb E\rho=0,
\qquad \operatorname{Var}(\rho)=\frac1{n-1}.
\]
Therefore
\[
\boxed{
\operatorname{Corr}(F,\rho)=\frac1{\sqrt{n-1}}.
}
\]
Equivalently, the least-squares projection of the fixed-point count onto Spearman's rho is exactly
\[
\widehat F_{\mathrm{lin}}=1+\rho.
\]

The positional profile is parabolic. If \(n\) is odd, a fixed point at the central rank \(i=(n+1)/2\) leaves \(\mathbb E[\rho\mid I_i=1]=0\). At either endpoint,
\[
\mathbb E[\rho\mid I_1=1]
=\mathbb E[\rho\mid I_n=1]
=\frac3{n+1},
\]
which is the largest conditional mean over all fixed-point locations.

## Assumptions and scope
The permutation is uniform on \(S_n\), which is the ordinary no-ties permutation null for Spearman's rank correlation. A fixed point means an exact agreement between the two rank positions. The theorem concerns the dependence between that exact-match statistic and Spearman's quadratic rank-displacement statistic.

No assertion is made for tied ranks, nonuniform permutation models, Mallows models, or non-null rank dependence.

The primary subject is nonparametric rank testing and permutation-null calibration, classified here under MSC \(62G10\).

## Proof
Write
\[
A=\sum_{j=1}^n j\Pi(j),
\qquad
S_1=\sum_{j=1}^n j=\frac{n(n+1)}2,
\qquad
S_2=\sum_{j=1}^n j^2=\frac{n(n+1)(2n+1)}6.
\]
Because \(\Pi\) is a permutation,
\[
\sum_{j=1}^n(j-\Pi(j))^2
=2S_2-2A.
\]
Thus Spearman's rho is an affine function of \(A\).

Fix a location \(i\). Conditional on \(I_i=1\), the remaining \(n-1\) positions are uniformly matched to the remaining \(n-1\) values. Hence, for every \(j\ne i\),
\[
\mathbb E[\Pi(j)\mid I_i=1]
=\frac{S_1-i}{n-1}.
\]
It follows that
\[
\mathbb E[A\mid I_i=1]
=i^2+\frac{(S_1-i)^2}{n-1}.
\]
Substituting this into the affine expression for \(\rho\), followed by elementary simplification, gives
\[
\mathbb E[\rho\mid I_i=1]
=\frac{3(2i-n-1)^2}{(n-1)^2(n+1)}.
\]
Under a uniform permutation, \(\Pr(I_i=1)=1/n\) and \(\mathbb E\rho=0\). Therefore
\[
\operatorname{Cov}(I_i,\rho)
=\frac1n\mathbb E[\rho\mid I_i=1],
\]
which proves the coordinate formula.

Now use
\[
\sum_{i=1}^n(2i-n-1)^2
=\frac{n(n^2-1)}3.
\]
Summing the coordinate covariances yields
\[
\operatorname{Cov}(F,\rho)=\frac1{n-1}.
\]

For completeness, the fixed-point indicators satisfy
\[
\mathbb EI_i=\frac1n,
\qquad
\mathbb E[I_iI_j]=\frac1{n(n-1)}\quad(i\ne j),
\]
which gives \(\mathbb EF=1\) and \(\operatorname{Var}(F)=1\) for \(n\ge2\).

To compute the null variance of \(\rho\), center the ranks by
\[
a_i=i-\frac{n+1}{2}.
\]
Then
\[
\rho=\frac{12}{n(n^2-1)}\sum_{i=1}^n a_i a_{\Pi(i)}.
\]
The permuted centered ranks have
\[
\operatorname{Var}(a_{\Pi(i)})=\frac{n^2-1}{12},
\qquad
\operatorname{Cov}(a_{\Pi(i)},a_{\Pi(j)})=-\frac{n+1}{12}
\quad(i\ne j).
\]
Using \(\sum_i a_i=0\) and
\[
\sum_i a_i^2=\frac{n(n^2-1)}{12},
\]
a direct covariance expansion gives
\[
\operatorname{Var}(\rho)=\frac1{n-1}.
\]
Combining the two variances with the covariance proves the correlation formula. Finally, the least-squares slope of \(F\) on \(\rho\) is
\[
\frac{\operatorname{Cov}(F,\rho)}{\operatorname{Var}(\rho)}=1,
\]
and the intercept is \(\mathbb EF=1\), proving the projection identity.

## Verification
The accompanying `checker.py` exhaustively enumerates every permutation for \(2\le n\le9\), using exact rational arithmetic. It verifies the conditional mean of \(\rho\) at every fixed-point location, all coordinate covariances, the aggregate covariance, both marginal variances, and the orthogonality of the projection residual \(F-1-\rho\) to \(\rho\).

The exact replay covers \(409112\) permutations. Finite enumeration is supplementary; the theorem for every \(n\ge2\) follows from the conditional-permutation calculation above.

## Relationship to prior work
Spearman's coefficient is classical, and exact permutation-null distributions of the squared rank-difference statistic were studied early. Kendall, Kendall, and Babington Smith explicitly treat the universe in which all rankings occur equally often, while Olds tabulates the corresponding sum-of-squared-rank-difference distribution for small sample sizes. These sources determine the marginal null law of \(\rho\), not its joint dependence with fixed points.

Diaconis, Evans, and Graham give a full probability-theoretic treatment of the fixed-point random set of a uniform permutation and show a distributional equivalence with unseparated adjacent-value pairs. Their full public text does not introduce Spearman's rho or a squared rank-displacement statistic, so it does not state the parabolic fixed-point profile above.

A separate exact result on fixed points and descents resolves a different local permutation statistic. Descent indicators depend only on adjacent order comparisons, whereas Spearman's rho is a global quadratic displacement functional. Neither the fixed-point/descent covariance law nor the fixed-point random-set marginal determines the present mixed moment.

## Limitations
The proof uses the uniform permutation null and no ties. The exact profile does not determine the full joint distribution of \((F,\rho)\) or higher mixed moments.

A residual literature risk remains because older refined permutation-enumeration work may encode fixed points jointly with the Spearman squared-displacement statistic under another generating-function notation. The strongest exact-null sources located describe the marginal distribution of \(\rho\), and the strongest fully inspected fixed-point source describes the fixed-point random set, not their joint law.

## References
1. C. Spearman, “The Proof and Measurement of Association between Two Things,” *The American Journal of Psychology* 15 (1904), 72–101. DOI: 10.2307/1412159.
2. M. G. Kendall, S. F. H. Kendall, and B. Babington Smith, “The Distribution of Spearman's Coefficient of Rank Correlation in a Universe in Which All Rankings Occur an Equal Number of Times,” *Biometrika* 30 (1939), 251–273. DOI: 10.1093/biomet/30.3-4.251.
3. E. G. Olds, “Distributions of Sums of Squares of Rank Differences for Small Numbers of Individuals,” *The Annals of Mathematical Statistics* 9 (1938), 133–148. DOI: 10.1214/aoms/1177732332.
4. P. Diaconis, S. N. Evans, and R. Graham, “Unseparated pairs and fixed points in random permutations,” arXiv:1308.5459, first submitted 25 August 2013; later *Advances in Applied Mathematics* 61 (2014), 102–124.
