# Exact row-sum criterion for Gaussian vectors conditioned on their total
## Finding
Let
\[
X=(X_1,\ldots,X_d)^\top\sim N_d(\mu,\Sigma),
\qquad d\ge2,
\]
with positive-definite covariance matrix \(\Sigma\), and define
\[
S=\mathbf 1^\top X.
\]
Then the conditional vector family
\[
[X\mid S=s]
\]
is nondecreasing in the usual multivariate componentwise stochastic order as \(s\) increases if and only if
\[
\Sigma\mathbf 1\ge0
\]
componentwise.

Equivalently, for every coordinate,
\[
\operatorname{Cov}(X_i,S)\ge0.
\]

Write
\[
\tau=\mathbf 1^\top\Sigma\mathbf 1,
\qquad
\beta=\frac{\Sigma\mathbf 1}{\tau}.
\]
Then
\[
X\mid S=s
\stackrel d=
\mu+\beta(s-\mathbf 1^\top\mu)+Z,
\tag{1}
\]
where \(Z\) is centered Gaussian with covariance
\[
C=
\Sigma-
\frac{\Sigma\mathbf 1\mathbf 1^\top\Sigma}{\tau},
\tag{2}
\]
and its law is independent of \(s\).

For each coordinate separately, there is also an exact likelihood-ratio criterion:
\[
[X_i\mid S=s]
\text{ is nondecreasing in likelihood-ratio order in }s
\]
if and only if
\[
(\Sigma\mathbf 1)_i\ge0.
\tag{3}
\]

This sharpens the sufficient Gaussian condition in the motivating paper. That condition requires
\[
\sum_{j\ne i}\operatorname{Cov}(X_i,X_j)\ge0,
\]
whereas (3) only requires
\[
\operatorname{Var}(X_i)
+
\sum_{j\ne i}\operatorname{Cov}(X_i,X_j)\ge0.
\]

A useful consequence is that every nonsingular unit-variance equicorrelated Gaussian vector,
\[
-\frac1{d-1}<\rho<1,
\]
has the full multivariate stochastic monotonicity property when conditioned on its total. Indeed every row sum is
\[
1+(d-1)\rho>0.
\]
Thus admissible negative equicorrelation is completely allowed, even though the sufficient condition based only on the sum of off-diagonal covariances fails whenever \(\rho<0\).

## Assumptions and scope
The covariance matrix \(\Sigma\) is positive definite, so \(S\) is nondegenerate and every conditional coordinate variance is positive for \(d\ge2\). The order on vectors is the usual componentwise stochastic order: expectations of bounded increasing functions are ordered.

The result is specific to Gaussian vectors and conditioning on the unweighted total \(S=\mathbf 1^\top X\). The same proof immediately applies to conditioning on a general nondegenerate Gaussian linear statistic after replacing \(\mathbf 1\) by its coefficient vector, but that extension is not part of the stated finding.

The theorem does not claim multivariate likelihood-ratio or total-positivity ordering of the singular conditional vector laws on different affine hyperplanes.

## Proof
Joint Gaussian conditioning gives
\[
E[X\mid S=s]
=
\mu+
\frac{\operatorname{Cov}(X,S)}
{\operatorname{Var}(S)}
(s-E[S]).
\]
Since
\[
\operatorname{Cov}(X,S)=\Sigma\mathbf 1,
\qquad
\operatorname{Var}(S)=\tau
=
\mathbf 1^\top\Sigma\mathbf 1,
\]
this is exactly
\[
m(s)=
\mu+\beta(s-\mathbf 1^\top\mu).
\tag{4}
\]
The conditional covariance is
\[
C=
\Sigma-
\frac{\Sigma\mathbf 1\mathbf 1^\top\Sigma}{\tau},
\]
which does not depend on \(s\). Therefore there is a single centered Gaussian residual \(Z\), supported on
\[
\{z:\mathbf 1^\top z=0\},
\]
such that (1) holds for every \(s\).

Suppose first that
\[
\Sigma\mathbf 1\ge0.
\]
Because \(\tau>0\), this is equivalent to \(\beta\ge0\). For \(s_1\le s_2\), couple the two conditional laws with the same residual \(Z\):
\[
X^{(1)}
=
m(s_1)+Z,
\qquad
X^{(2)}
=
m(s_2)+Z.
\]
Then
\[
X^{(2)}-X^{(1)}
=
\beta(s_2-s_1)\ge0
\]
coordinatewise almost surely. This pathwise coupling proves
\[
[X\mid S=s_1]\le_{\mathrm{ST}}[X\mid S=s_2].
\]

Conversely, suppose the conditional vector family is nondecreasing in the componentwise stochastic order. Then every coordinate marginal is stochastically nondecreasing. Since the conditional normal distributions are integrable, their means must be nondecreasing:
\[
E[X_i\mid S=s]
=
\mu_i+\beta_i(s-\mathbf 1^\top\mu).
\]
Thus
\[
\beta_i\ge0
\]
for every \(i\), hence
\[
\Sigma\mathbf 1\ge0.
\]
This proves the necessary-and-sufficient vector criterion.

For the coordinatewise likelihood-ratio statement, fix \(i\). Positive definiteness and \(d\ge2\) imply that
\[
v_i=
\Sigma_{ii}
-
\frac{(\Sigma\mathbf 1)_i^2}{\tau}
>0.
\]
Thus
\[
X_i\mid S=s
\sim
N\!\left(
\mu_i+\beta_i(s-\mathbf 1^\top\mu),
v_i
\right).
\]
For \(s_2>s_1\), the log density ratio is affine in \(x\), with slope
\[
\frac{\beta_i(s_2-s_1)}{v_i}.
\]
It is nondecreasing in \(x\) exactly when
\[
\beta_i\ge0,
\]
which proves (3).

Finally, in the unit-variance equicorrelated model,
\[
\Sigma\mathbf 1
=
\{1+(d-1)\rho\}\mathbf 1.
\]
Positive definiteness is equivalent to
\[
-\frac1{d-1}<\rho<1,
\]
and throughout this entire range the row sum is strictly positive. Hence the full conditional vector family is shifted upward in every coordinate as the total increases.

## Verification
The bundled `verify.py` uses exact rational arithmetic to check the Gaussian regression identities on deterministic positive-definite examples, verifies that the conditional covariance annihilates the all-ones direction, checks both positive and negative row-sum cases, and replays the equicorrelation consequence.

It also checks the \(d=3\), \(\rho=-2/5\) example:
\[
\Sigma\mathbf 1=\frac15\mathbf 1,
\qquad
\beta=\frac13\mathbf 1,
\]
while the sum of off-diagonal covariances in each row is
\[
-\frac45<0.
\]
Thus the motivating sufficient condition does not apply although the exact criterion proves multivariate stochastic monotonicity.

A successful run ends with
`VERIFY_OK equicorr_beta=0.333333333333 negative_row_beta=-0.250000000000`.

The computational checks replay algebraic consequences only; the theorem is proved analytically above.

## Relationship to prior work
Pellerey and Navarro study stochastic monotonicity of dependent variables conditioned on their sum. Their bivariate Proposition 2.2 gives vector stochastic monotonicity under total-positivity hypotheses. In the multivariate section they derive coordinatewise results and, for Gaussian vectors, give a sufficient condition based on the covariance of one coordinate with the sum of the remaining coordinates.

The same paper's conclusion explicitly identifies extension of the bivariate vector result to the multivariate case, and extension to stronger orders, as a main direction for future research. Its Proposition 3.3 supplies a multivariate vector result for a Schur-constant survival model, but not a general Gaussian vector characterization.

The theorem here resolves the Gaussian vector subproblem exactly: the relevant condition is the sign of
\[
\operatorname{Cov}(X_i,S),
\]
not the sign of covariance with only the other coordinates. The common conditional covariance makes the multivariate order equivalent to a coordinatewise sign test on the Gaussian regression vector.

Related work on Efron monotonicity in Gaussian domains of attraction and on copula-based sufficient conditions concerns different independence, asymptotic, or sufficient-condition settings and does not state this necessary-and-sufficient row-sum criterion in the inspected material.

## Limitations
The argument relies essentially on the fixed conditional covariance of a Gaussian linear regression. For non-Gaussian dependent vectors, increasing conditional means alone are not sufficient for multivariate stochastic order.

The result resolves the Gaussian subcase of the multivariate extension direction, not the full non-Gaussian question posed by the motivating paper.

A residual bibliographic risk is that the criterion may appear implicitly in older Gaussian comparison or stochastic-order literature as an immediate consequence of equal-covariance normal ordering, without being phrased as an Efron conditional-sum theorem.

## References
1. F. Pellerey and J. Navarro, “Stochastic monotonicity of dependent variables given their sum,” *TEST* 31 (2022), 543–561. DOI: 10.1007/s11749-021-00789-5. Published online 11 October 2021.
2. M. Denuit and C. Y. Robert, “Efron’s asymptotic monotonicity property in the Gaussian stable domain of attraction,” *Journal of Multivariate Analysis* 186 (2021), 104803. DOI: 10.1016/j.jmva.2021.104803.
