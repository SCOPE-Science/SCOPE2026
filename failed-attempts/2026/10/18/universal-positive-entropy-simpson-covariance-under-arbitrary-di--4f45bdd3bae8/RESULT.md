# Universal positive entropy–Simpson covariance under arbitrary Dirichlet heterogeneity

## Finding
Let \(X\) be a Dirichlet-distributed random probability vector with any strictly positive, not necessarily equal, parameters. Write its Shannon entropy as \(H=-\sum_i X_i\log X_i\), its collision concentration as \(Q=\sum_iX_i^2\), and Gini–Simpson diversity as \(G=1-Q\). The covariance \(\operatorname{Cov}(H,G)\) is strictly positive for all dimensions at least two. More precisely, put \(A=\sum_i\alpha_i\), \(S_2=\sum_i\alpha_i^2\), \(w_i=\alpha_i/A\), and let \(\psi\) denote the digamma function. Then

\[
\operatorname{Cov}(H,Q)=-\frac{A^2-S_2}{A(A+1)^2(A+2)}-\frac{2}{(A+1)(A+2)}\operatorname{Cov}_{i\sim w}\big(\alpha_i,\psi(\alpha_i+1)\big)<0.
\]

Since the weighted covariance on the right is nonnegative, this yields the sharp bound

\[
\operatorname{Cov}(H,G)\ge\frac{A^2-S_2}{A(A+1)^2(A+2)}>0,
\]

with equality in the first inequality if and only if all concentration parameters coincide. In the symmetric case \(\alpha_i=\alpha\), this reads

\[
\operatorname{Cov}(H,Q)=-\frac{(k-1)\alpha}{(k\alpha+1)^2(k\alpha+2)}.
\]

These identities hold unchanged when the parameters are positive Dirichlet posterior concentrations after categorical observations.

## Assumptions and scope
Fix an integer \(k\ge2\), parameters \(\alpha_i>0\) for all \(1\le i\le k\), and \(X\sim\operatorname{Dirichlet}(\alpha_1,\ldots,\alpha_k)\). Logarithms are natural and \(0\log0=0\) by continuity. The Dirichlet law has positive coordinates almost surely, so every quantity is finite. Weighted covariance uses \(\Pr\{I=i\}=w_i\) on the discrete index set; it is not a posterior covariance of the random vector itself. No balance, integer-shape, asymptotic, or fixed-total-concentration restriction is imposed.

## Proof
**1. Gamma-moment derivative.** The Dirichlet moment formula, valid whenever the indicated exponents admit finite expectation, is

\[
\mathbb E\prod_iX_i^{s_i}=\frac{\Gamma(A)}{\Gamma(A+\sum_i s_i)}\prod_i\frac{\Gamma(\alpha_i+s_i)}{\Gamma(\alpha_i)}.
\]

Differentiation in one exponent gives a logarithmic factor and a multiplier \(\psi(\alpha_i+s_i)-\psi(A+\sum_i s_i)\). All required derivatives are justified by the integrable positive-parameter Dirichlet density and logarithmic moments.

**2. First and mixed moments.** Set \(B=\sum_i\alpha_i(\alpha_i+1)=A+S_2\) and \(D=A(A+1)(A+2)\). The moment identity gives

\[
\mathbb EH=\psi(A+1)-\frac1A\sum_i\alpha_i\psi(\alpha_i+1),\qquad \mathbb EQ=\frac{B}{A(A+1)}.
\]

For distinct \(i,j\),

\[
\mathbb E[X_iX_j^2\log X_i]=\frac{\alpha_i\alpha_j(\alpha_j+1)}{D}\big[\psi(\alpha_i+1)-\psi(A+3)\big],
\]

while, for \(i=j\),

\[
\mathbb E[X_i^3\log X_i]=\frac{\alpha_i(\alpha_i+1)(\alpha_i+2)}{D}\big[\psi(\alpha_i+3)-\psi(A+3)\big].
\]

Using the digamma recurrence \(\psi(z+1)-\psi(z)=1/z\), summing over \(i,j\) yields

\[
\mathbb E[HQ]=\frac{B}{A(A+1)}\psi(A+3)-\frac{\sum_i\alpha_i\{[B+2(\alpha_i+1)]\psi(\alpha_i+1)+2\alpha_i+3\}}{D}.
\]

**3. Cancellation.** Subtract \(\mathbb EH\,\mathbb EQ\), apply \(\psi(A+3)-\psi(A+1)=1/(A+1)+1/(A+2)\), and collect coefficients. The constant term simplifies to \(-(A^2-S_2)/[A(A+1)^2(A+2)]\). The digamma term simplifies to

\[
-\frac{2}{(A+1)(A+2)}\left[\frac1A\sum_i\alpha_i^2\psi(\alpha_i+1)-\frac{S_2}{A^2}\sum_i\alpha_i\psi(\alpha_i+1)\right].
\]

The bracket is exactly \(\operatorname{Cov}_{I\sim w}(\alpha_I,\psi(\alpha_I+1))\), establishing the exact identity.

**4. Strict sign and equality.** The digamma function is strictly increasing on \((0,\infty)\). Consequently

\[
2\operatorname{Cov}_{I\sim w}(\alpha_I,\psi(\alpha_I+1))=\sum_{i,j}w_iw_j(\alpha_i-\alpha_j)(\psi(\alpha_i+1)-\psi(\alpha_j+1))\ge0,
\]

with equality exactly when all positive-weight parameters \(\alpha_i\) coincide. Since \(A^2-S_2=2\sum_{i<j}\alpha_i\alpha_j>0\), the covariance with concentration is strictly negative. Negating it proves the sharp positive-diversity bound; substitution of equal parameters gives the symmetric formula. This completes the proof for all admissible parameter values.

## Verification
Run `python verify.py` with Python 3.10 or later and `numpy` and `scipy` installed. The verifier reports 266 assertions: exact rational independent comparisons of the unsimplified gamma-derivative joint moment with the displayed formula for 117 integer parameter tuples, checks of symmetric fractional-parameter cases, numerical beta-integral checks, and exploratory independent random sampling. The infinite-domain proof is analytic; numerical quadrature, simulation, and finite enumeration are not used to establish its unrestricted sign.

The covariance sign is not a deterministic inverse ordering of Shannon entropy and concentration: on the three-simplex, the vectors \((0.49,0.49,0.02)\) and \((0.7,0.15,0.15)\) exhibit an increase in both quantities. The result is an exact distributional covariance law.

## Relationship to prior work
Wolpert and Wolf (1994), Parts I and II, develop Dirichlet-integration methods for Bayesian entropy moments and other statistics. Cerquetti (first posted 2014) studies the marginal moments of Shannon and Tsallis/Simpson diversity under a broad partition-prior family. Those techniques explain how to compute moments, and the present first-moment identities are classical. The contribution assessed here is the evaluated *mixed* Shannon–collision covariance for every finite asymmetric Dirichlet parameter vector, its strict universal sign, and the sharp parameter-heterogeneity decomposition. The inspected sources did not state this theorem; a derivation implicit in more general published moment formulae remains possible.

## Limitations
The claim is about **covariance**, not samplewise monotonicity, stochastic order, or all higher joint moments. It requires a finite number of positive Dirichlet parameters and natural logarithms (changing the entropy log base rescales covariance by a positive constant). It makes no claim for arbitrary priors, general Pitman–Yor laws, or unbounded alphabets. Bibliographic priority remains subject to independent historical assessment, especially derivations implicit in general Dirichlet integral identities. No independent scientific audit has been performed.

## References
1. D. H. Wolpert and D. R. Wolf, *Estimating Functions of Probability Distributions from a Finite Set of Samples, Part I: Bayes Estimators and Shannon Entropy*, arXiv:comp-gas/9403001 (first posted 1994-03-08). https://arxiv.org/abs/comp-gas/9403001
2. D. R. Wolf and D. H. Wolpert, *Estimating Functions of Probability Distributions from a Finite Set of Samples, Part II: Bayes Estimators for Mutual Information, Chi-squared, Covariance, and Other Statistics*, arXiv:comp-gas/9403002 (first posted 1994-03-08). https://arxiv.org/abs/comp-gas/9403002
3. A. Cerquetti, *Bayesian nonparametric estimation of Tsallis diversity indices under Gnedin–Pitman priors*, arXiv:1404.3441 (first posted 2014-04-14). https://arxiv.org/abs/1404.3441
