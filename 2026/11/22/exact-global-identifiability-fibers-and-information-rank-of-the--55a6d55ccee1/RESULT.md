# Exact global identifiability fibers and information rank of the bimodal beta family

## Finding

**Theorem (complete distributional fibers).** Let the bimodal beta distribution have parameters \(\alpha,\beta>0\), \(\rho\geq0\), \(\delta\in\mathbb R\) and density
\[
f_{\alpha,\beta,\rho,\delta}(x)=
\frac{x^{\alpha-1}(1-x)^{\beta-1}\{\rho+(1-\delta x)^2\}}
{B(\alpha,\beta)Z(\alpha,\beta,\rho,\delta)},\quad 0<x<1,
\]
where \(Z\) is the normalizing constant below. Two parameter vectors determine the same probability distribution **if and only if** either they are equal, or they lie in the same fiber
\[
\mathcal F_{\alpha,b}=
\{(\alpha,b,\rho,0):\rho\geq0\}
\;\cup\;
\begin{cases}
\{(\alpha,b-2,0,1)\},&b>2,\\
\varnothing,&0<b\leq2.
\end{cases}
\]
Every parameter vector outside the displayed beta fibers has a singleton fiber. In particular, for \(\delta\ne0\) away from \((\rho,\delta)=(0,1)\), the full parameter vector is globally identifiable. The normalized nonconstant quadratic factor uniquely determines \(\rho,\delta\).

For any \(\rho>0\) on the submodel \(\delta=0\), the ordinary per-observation Fisher information for \((\alpha,\beta,\rho,\delta)\) has rank **exactly three**, with a zero \(\rho\) score. Thus the original four-parameter model cannot admit estimators that are consistent at every admissible parameter vector: multiple parameter vectors produce identical observations at every sample size.

For example, \((\alpha,\beta,\rho,\delta)=(2,1,0,1)\) and \((2,3,7,0)\) both produce the exact \(\operatorname{Beta}(2,3)\) density, despite unequal \(\beta\) values.

## Assumptions and scope

The parameter domain is exactly \((0,\infty)^2\times[0,\infty)\times\mathbb R\). Equality of probability laws refers to equality of densities Lebesgue-almost everywhere on \((0,1)\). The beta function is \(B(\alpha,\beta)=\int_0^1 x^{\alpha-1}(1-x)^{\beta-1}\,dx\), and
\[
Z=1+\rho-\frac{2\delta\alpha}{\alpha+\beta}
+\frac{\delta^2\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)}.
\]
It is positive since it is the expectation under a positive beta density of the nonnegative polynomial \(Q(x)=\rho+(1-\delta x)^2\), which is not identically zero. The Fisher-rank statement is restricted to interior \(\rho>0\) and \(\delta=0\), where the usual smooth score definition applies. No claim is made that all parameter vectors with \(\rho=0\) possess a regular unconstrained information geometry.

## Proof

**1. Canonical endpoint factorization.** Write \(Q(x)=\rho+(1-\delta x)^2\). Its left endpoint satisfies \(Q(0)=1+\rho>0\). At the right endpoint,
\[
Q(1)=\rho+(1-\delta)^2=0
\quad\Longleftrightarrow\quad (\rho,\delta)=(0,1),
\]
because \(\rho\geq0\). In this exceptional case \(Q(x)=(1-x)^2\), and the beta-function recurrence gives
\[
f_{\alpha,\beta,0,1}(x)=
\frac{x^{\alpha-1}(1-x)^{\beta+1}}{B(\alpha,\beta+2)}
=f_{\operatorname{Beta}(\alpha,\beta+2)}(x).
\]
Indeed \(Z=B(\alpha,\beta+2)/B(\alpha,\beta)>0\). For every other parameter vector define \(b=\beta\) and \(P(x)=Q(x)/(1+\rho)\); in the exceptional case set \(b=\beta+2\) and \(P(x)=1\). In both cases the normalized density is a positive constant times
\[
x^{\alpha-1}(1-x)^{b-1}P(x),\qquad
P(0)=1,\quad P(1)>0,
\]
with \(P\) a polynomial of degree zero or two, and \(P(x)>0\) except possibly at a finite set of interior points.

**2. Uniqueness of the canonical data.** Suppose two densities agree a.e. Analyticity on \((0,1)\) makes the equality pointwise there. The ratio of their canonical density expressions is a constant. Taking \(x\downarrow0\), positivity of each \(P(0)=1\) forces equality of the left exponents \(\alpha\); otherwise this ratio tends to zero or infinity. Taking \(x\uparrow1\), positivity of each \(P(1)\) likewise forces equality of the right exponents \(b\). The remaining equality is \(cP(x)=c'P'(x)\); evaluating at \(x=0\) gives \(c=c'\), hence \(P=P'\) polynomially. Conversely, identical \(\alpha,b,P\) clearly give the same normalized law.

**3. Reconstruction and exhaustive fibers.** In any nonexceptional representation,
\[
P(x)=1+px+qx^2,\qquad
p=-\frac{2\delta}{1+\rho},\qquad q=\frac{\delta^2}{1+\rho}.
\]
If \(P\not\equiv1\), then \(\delta\ne0\) and both \(p\) and \(q\) are nonzero; inversion gives
\[
\delta=-\frac{2q}{p},\qquad
\rho=\frac{4q}{p^2}-1.
\]
Thus the original parameters are determined uniquely by \(\alpha,b,P\). If \(P\equiv1\), either the nonexceptional parameter has \(\delta=0\), yielding \(\operatorname{Beta}(\alpha,b)\) independently of \(\rho\), or it is the exceptional parameter \((\rho,\delta)=(0,1)\), which requires \(\beta=b-2>0\). This proves *all* fibers and both directions of the theorem.

**4. Rank of the information.** At \(\delta=0\), the distribution is \(\operatorname{Beta}(\alpha,\beta)\) for all \(\rho\); in particular its score in the \(\rho\) direction is identically zero. Differentiating the log density shows that the other three centered score functions are
\[
S_{\alpha}(x)=\log x-\mathbb E\log X,\quad
S_{\beta}(x)=\log(1-x)-\mathbb E\log(1-X),\quad
S_{\delta}(x)=-\frac{2}{1+\rho}\left(x-\frac{\alpha}{\alpha+\beta}\right).
\]
All lie in \(L^2\) under the positive beta density. If a linear combination vanishes in \(L^2\), continuity forces \(A\log x+B\log(1-x)+Cx\) to be constant on \((0,1)\). Differentiation gives \(A/x-B/(1-x)+C=0\). Multiplication by \(x(1-x)\) yields a quadratic polynomial whose coefficient comparison forces \(A=B=C=0\). Hence these three scores are linearly independent, and their covariance Gram matrix is positive definite. Adding the zero \(\rho\) score gives rank exactly three.

Finally, distinct vectors in a fiber induce the same joint law for every sample size. A hypothetical estimator converging in probability to the true vector at both of two such parameter values would have two different probability limits under the same sequence of laws, which is impossible. This proves the stated global consistency obstruction.

## Verification

The companion `check_identifiability.py` uses SymPy to check, by exact symbolic identities, the normalizer, the right-endpoint beta shift, the reconstruction formulas, and the zero-tilt score identities; it also runs several exact rational beta-function examples and pointwise comparisons. Run `python check_identifiability.py` with SymPy available. It returned PASS. The infinite-domain and exhaustive statements are established by the analytical four-step proof above; finite symbolic examples are supporting checks, not an exhaustive enumeration.

## Relationship to prior work

Vila, Alfaia, Menezes, Çankaya and Bourguignon introduced the model, its exact density and the fact that \(\delta=0\) reduces to a standard beta law. The 18 August 2021 preprint (§4.3, Proposition 4.4) asserts global one-to-one parameterization. The later full journal paper (§4.2, Proposition 4.2) gives a qualified identifiability statement relying on finite-mixture components with pairwise distinct right-shape parameters; its displayed three-component decomposition actually shares the same right-shape parameter in all three components. In particular, the explicit equality of \(\operatorname{Beta}(2,3)\) laws above has distinct baseline right-shape parameters, contrary to an unrestricted two-vector uniqueness inference. The new contribution is the exhaustive *if and only if* classification of all equal-law parameter fibers, the nonexceptional recovery formula, and the exact Fisher rank and consistency consequences.

The generic beta-mixture identifiability references discussed in that paper do not determine this exact constrained quadratic tilt's fibers: these follow from endpoint orders and polynomial coefficients. Searches for this particular equality classification found no directly covering earlier result, but that search outcome is not a proof of priority.

## Limitations

The result describes the specified four-parameter unconditional distribution family, not a covariate-varying regression identifiability theorem, finite-sample optimization convergence, or identifiability of arbitrary signed beta mixtures. The Fisher-rank claim is interior to \(\rho>0\) at \(\delta=0\). Literature access cannot exclude unindexed or unpublished previous derivations. No independent audit or external certification has been performed.

## References

1. R. Vila, L. Alfaia, A. F. B. Menezes, M. N. Çankaya and M. Bourguignon, *A Model for Bimodal Rates and Proportions*, arXiv:2108.07934 (first publicly posted 2021-08-18), https://arxiv.org/abs/2108.07934 . See §§2, 4.3.
2. The same authors, *A model for bimodal rates and proportions*, *Journal of Applied Statistics* 51 (2024), 664–681, first journal online 2022-11-18; DOI https://doi.org/10.1080/02664763.2022.2146661 . Lawful author-hosted full text: https://andrmenezes.github.io/pdf/papers/2022__beta_bimodal.pdf . See §§2, 4.2.
