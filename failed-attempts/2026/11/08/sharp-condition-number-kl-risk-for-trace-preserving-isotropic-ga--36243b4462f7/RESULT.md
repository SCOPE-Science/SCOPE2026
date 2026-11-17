# Sharp condition-number KL risk for trace-preserving isotropic Gaussian covariance approximations

## Finding

Let \(n\ge2\) and \(\kappa>1\). For a real symmetric positive-definite covariance \(\Gamma\in\mathbb R^{n\times n}\), use the **trace-preserving isotropic approximation** \(\widetilde\Gamma=\bar\omega I_n\), where \(\bar\omega=\operatorname{tr}(\Gamma)/n\). The forward divergence is taken in the explicit orientation
\[
D(\Gamma)=D_{\mathrm{KL}}\bigl(\mathcal N(0,\widetilde\Gamma)\,\|\,\mathcal N(0,\Gamma)\bigr).
\]
For all \(\kappa_2(\Gamma)\le\kappa\), its **exact** maximum is
\[
\boxed{D_{\max}(n,\kappa)=\frac n2\max_{1\le j\le n-1}\left[\frac{(\kappa-1)^2}{\kappa}\frac jn\left(1-\frac jn\right)+\frac jn\log\kappa-\log\left(1+(\kappa-1)\frac jn\right)\right].}
\]
All maximizing covariances have, up to orthogonal similarity and a common positive scale \(a\), exactly \(n-j\) eigenvalues \(a\) and \(j\) eigenvalues \(\kappa a\), for a maximizing integer \(j\). Conversely, every such spectrum attains the bound.

The maximizing integer is among \(\lfloor nq_*\rfloor\) and \(\lceil nq_*\rceil\), with endpoints excluded, where \(q_*\in(0,1)\) is the unique root of
\[
\frac{(\kappa-1)^2}{\kappa}(1-2q)+\log\kappa-\frac{\kappa-1}{1+(\kappa-1)q}=0.
\]
In the particularly interpretable case \(n=2\),
\[
D_{\max}(2,\kappa)=\frac{(\kappa-1)^2}{4\kappa}-\frac12\log\frac{(\kappa+1)^2}{4\kappa}.
\]
For each fixed \(n\),
\[
\lim_{\kappa\to\infty}\frac{D_{\max}(n,\kappa)}{\kappa}=\frac{\lfloor n^2/4\rfloor}{2n}.
\]
Furthermore, for every nontrivial \(\kappa>1\),
\[
\frac{D_{\max}(n,\kappa)}n<\frac{(\kappa-1)^2}{8\kappa}.
\]
Thus the worst-case normalized risk grows at most linearly in large \(\kappa\), rather than quadratically.

## Assumptions and scope

The covariance \(\Gamma\) is positive definite and real; dimension \(n\) is finite and at least two; the condition-number bound \(\kappa\) is in the spectral norm. Logarithms are natural. There is no freedom to optimize the isotropic scale: \(\bar\omega\) is required to preserve the covariance trace. The divergence orientation is essential: exchanging its arguments changes the optimization problem. This theorem applies in particular to the generic isotropic-inverse approximation \(\Gamma=B^{-1}\), \(\widetilde\Gamma=(\operatorname{tr} B^{-1}/n)I\) for SPD \(B\), as considered in the conditioning analysis of complement covariance surrogates.

## Proof

**1. Spectral form.** Write the positive eigenvalues of \(\Gamma\) as \(y_1,\ldots,y_n\), with \(m=n^{-1}\sum_i y_i\). The exact centered Gaussian KL identity gives
\[
2D(\Gamma)=m\sum_{i=1}^n\frac1{y_i}-n+\sum_{i=1}^n\log y_i-n\log m. \tag{1}
\]
This expression is invariant under scaling all \(y_i\) by the same positive number. Therefore every allowed spectrum can be represented inside the full box \([1,\kappa]^n\). Conversely, every vector in this box defines an allowed covariance.

**2. Endpoint lemma.** Fix all \(y_i\) except one variable \(y>0\) and set \(B=\sum_{i\ne j}y_i\), \(T=\sum_{i\ne j}y_i^{-1}\), both strictly positive. Differentiating (1) yields
\[
2\frac{\partial D}{\partial y}=\frac{P(y)}{n y^2(B+y)},\qquad P(y)=Ty^3+\bigl(BT-n(n-1)\bigr)y^2+(n-1)By-B^2.\tag{2}
\]
By Cauchy–Schwarz, \(BT\ge(n-1)^2\). Write \(a=BT-n(n-1)\). If \(a\ge0\), then \(P'(y)=3Ty^2+2ay+(n-1)B>0\). If \(a<0\), then \(-a\le n-1\), whereas \(3T(n-1)B\ge3(n-1)^3>(n-1)^2\ge a^2\). Hence the quadratic polynomial \(P'\) has negative discriminant and positive leading coefficient, so it is again positive for all \(y>0\). As \(P(0)=-B^2<0\) and \(P(y)\to\infty\), (2) shows that the one-variable divergence strictly decreases and then strictly increases, with one interior *minimum*. Its maximum on any closed interval occurs at an endpoint and is strictly larger than the value at every interior point. Applying this argument to each coordinate proves that every global maximizer on \([1,\kappa]^n\) is a vertex.

**3. Exact sharp constant.** A vertex with \(j\) entries equal to \(\kappa\) and \(n-j\) entries equal to one has \(m=1+q(\kappa-1)\), with \(q=j/n\). In (1),
\[
m\sum_i y_i^{-1}-n=n\frac{(\kappa-1)^2}{\kappa}q(1-q),\quad \sum_i\log y_i=nq\log\kappa.
\]
Substitution proves the displayed finite maximum. The uniform vertices give divergence zero; every mixed vertex gives strictly positive divergence, so only \(1\le j\le n-1\) can maximize. The statement about precisely the maximizing spectra follows from strict one-coordinate endpoint optimality.

**4. Location of the maximizing multiplicity.** Set \(F(q)=\frac{(\kappa-1)^2}{\kappa}q(1-q)+q\log\kappa-\log(1+(\kappa-1)q)\). Then
\[
F'(0)=\log\kappa-1+\kappa^{-1}>0,\quad F'(1)=\log\kappa-(\kappa-1)<0,
\]
and
\[
F''(q)=(\kappa-1)^2\left[\frac1{(1+(\kappa-1)q)^2}-\frac2\kappa\right].
\]
The last derivative is strictly decreasing in \(q\). If \(\kappa\le2\), \(F'\) decreases throughout; if \(\kappa>2\), \(F'\) initially increases and then decreases, but it begins positive. Therefore it crosses zero exactly once. Thus \(F\) is strictly increasing then strictly decreasing, and the finite maximizing multiplicity must be adjacent to \(nq_*\). The root may be found without a multidimensional optimization.

**5. Growth and simpler envelope.** At each fixed \(q=j/n\), \(F(q)/\kappa\to q(1-q)\) as \(\kappa\to\infty\), and maximization over finitely many \(j\) yields \(\max_j j(n-j)=\lfloor n^2/4\rfloor\), proving the stated limit. Finally, the Kantorovich bound gives \(m\,n^{-1}\sum_i y_i^{-1}\le(\kappa+1)^2/(4\kappa)\), and Jensen's strict logarithmic inequality gives \(\sum_i\log y_i-n\log m<0\) for every mixed spectrum. Inserting both into (1) proves the strict normalized envelope.

## Verification

Run `python3 verify.py` with Python 3. The deterministic checker verifies 385 exact rational vertex identities; enumerates 3,048 vertex cases; stress-tests 18,900 interior spectra against the exact maximum; checks positivity of 14,000 derivative instances; checks 180 continuous-root and neighboring-integer comparisons; and checks 16 large-contrast limits. It prints `VERIFY_OK` upon completion. The analytical endpoint lemma, rather than any finite test, establishes the universal quantifiers.

## Relationship to prior work

Fifen, Karambal and Hennig (arXiv:2609.10080, initial public version September 9, 2026) use a trace-preserving isotropic complement covariance and give a general dimension-normalized KL upper bound of \(\tfrac12(\kappa-1)^2\) in their Theorem 13. The present theorem solves the exact extremal problem for that abstract SPD covariance-surrogate model, including every finite dimension and the equality spectra; it does not claim that all equality spectra are realizable by a prescribed Lanczos run. The classical Kantorovich inequality bounds only the product-of-means term and produces a generally nonsharp \(O(\kappa)\) envelope, not the exact KL extremum with its logarithmic determinant penalty. General Gaussian KL approximation work by Pinski, Simpson, Stuart and Weber develops variational approximation but is not established here as an exact condition-number extremal theorem.

## Limitations

No assertion is made about convergence, cost, or exact attainment by a specific stochastic Lanczos implementation, about non-Gaussian distributions, about approximate covariance estimation, or about the reverse KL orientation. The eigenvalue condition number alone does not fix divergence for an individual matrix; the theorem gives the sharp worst-case envelope. The novel finite-dimensional optimization is supported by the given proof and finite tests, but independent mathematical validation and exhaustive historical-priority verification have not been performed.

## References

1. H. Fifen, I. Karambal and P. Hennig, *Stochastic Lanczos Quadrature for Computational Uncertainty in Linear Algebra*, arXiv:2609.10080v1 (2026), Sections 4.1–4.3, especially Theorem 13. https://arxiv.org/abs/2609.10080
2. F. J. Pinski, G. Simpson, A. M. Stuart and H. Weber, *Kullback–Leibler Approximation for Probability Measures on Infinite Dimensional Spaces*, SIAM J. Math. Anal. 47 (2015), 4091–4122; arXiv:1310.7845. https://arxiv.org/abs/1310.7845
3. Kantorovich inequality (classical arithmetic–harmonic mean product bound), stated at https://en.wikipedia.org/wiki/Kantorovich_inequality
