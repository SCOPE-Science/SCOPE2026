# Sharp high-dimensional total correlation for the multivariate Raftery copula

## Finding

Fix \(0<\theta<1\), put \(q=1-\theta\), and let \(d\ge2\) be an integer. Let \(E_1,\ldots,E_d,Z\) be independent unit-rate exponential variables and let \(J\) be independent Bernoulli with \(\Pr(J=1)=\theta\). Set \(X_i=qE_i+JZ\). Each \(X_i\) is a unit-rate exponential. The law of \((e^{-X_1},\ldots,e^{-X_d})\) is the homogeneous multivariate Raftery copula of Saali, Mesfioui and Shabri [1]: it is the **survival copula** of \(\mathbf X\), not its ordinary distribution copula. Coordinatewise inversion between \(X_i\) and \(e^{-X_i}\) preserves relative entropy against the product of the corresponding margins, so these two joint laws have the same total correlation \(T_d(\theta)\).

With \(\varepsilon=q/d\), set
\[
g_{d,\theta}(t)=\frac q\varepsilon e^{-t/\varepsilon}+
\frac{\theta}{1-\varepsilon}(e^{-t}-e^{-t/\varepsilon}),\qquad t\ge0.
\]
For \(h(g)=-\int_0^\infty g\log g\), the exact finite-dimensional reduction and fixed-parameter asymptotic are
\[
T_d(\theta)=d\log(1/q)+1+\log\varepsilon-h(g_{d,\theta}),
\qquad
T_d(\theta)=d\log(1/q)-\theta\log(d/q)-H_b(\theta)+o(1).
\]
Here \(H_b(s)=-s\log s-(1-s)\log(1-s)\) with the convention \(0\log0=0\). Thus the coefficient of the logarithmic deficit is exactly \(\theta\) and the constant in the expansion using \(-\theta\log d\) is \(\theta\log q-H_b(\theta)\). In fact the remainder \(R_d=T_d-d\log(1/q)+\theta\log(d/q)+H_b(\theta)\) satisfies
\[
-\theta\log(1+q/d)\le R_d\le H_b\bigl(q e^{-\sqrt d/q}+\theta d^{-1/2}\bigr)
\]
whenever the binary-entropy argument is at most \(1/2\). This yields \(R_d=O_\theta(d^{-1/2}\log d)\).

## Assumptions and scope

Logs are natural and total correlation is in nats. The expansion and error order take integer \(d\to\infty\) at fixed interior \(\theta\). Coordinatewise positive rescaling gives arbitrary positive exponential marginal rates without changing total correlation or the survival copula. At \(\theta=0\) there is independence; at \(\theta=1\) the model is singular and comonotone. The stated asymptotic does not cover the endpoints or dimension-dependent parameters.

## Proof

Let \(W=JZ\). The Laplace transform of \(X_i\) is \((q+\theta/(1+s))/(1+qs)=1/(1+s)\) for \(s\ge0\), so the marginal entropy is 1. The variables \(e^{-X_i}\) are therefore uniform. Equation (8) and Proposition 1 of [1] identify their joint law as the Raftery survival copula. Coordinatewise bijections push the joint and the product reference forward together, preserving their KL divergence.

With \(M=\min_i X_i\), the conditional joint density given \(W=w\) is
\[
q^{-d}\exp(-\textstyle\sum_i x_i/q)\exp(dw/q)\,\mathbf1\{w\le M\}.
\]
The posterior of \(W\) given \(\mathbf X\) thus depends on \(\mathbf X\) only through \(M\), so \(I(W;\mathbf X)=I(W;M)\). The minimum of the \(d\) independent exponential noises has scale \(q/d=\varepsilon\), and is independent of \(W\); hence \(M\) has the law of \(W+\varepsilon E\) for a fresh independent unit-rate exponential \(E\). When \(J=0\) its density is \(\varepsilon^{-1} e^{-t/\varepsilon}\); when \(J=1\) convolution gives \((e^{-t}-e^{-t/\varepsilon})/(1-\varepsilon)\). This proves the mixture formula for \(g_{d,\theta}\). The densities have exponential tails and finite differential entropies for these parameters.

The conditional joint entropy given \(W\) is \(d(1+\log q)\), while \(h(M\mid W)=1+\log\varepsilon\). Subtracting the joint entropy from the sum of marginal entropies gives
\[
T_d=d\log(1/q)-I(W;\mathbf X)
=d\log(1/q)+1+\log\varepsilon-h(g_{d,\theta}).
\]

Set \(Y=Z+\varepsilon E\), \(\delta_\varepsilon=h(Y)-1\). Conditioning on \(E\) gives \(h(Y)\ge h(Z)=1\); the exponential maximizes entropy of a nonnegative variable of given mean, so \(h(Y)\le1+\log(1+\varepsilon)\). Conditioning on the mixture indicator gives
\[
h(M)=q(1+\log\varepsilon)+\theta(1+\delta_\varepsilon)
       +H_b(\theta)-H(J\mid M).
\]
Substitution shows \(R_d=H(J\mid M)-\theta\delta_\varepsilon\). Classify \(J=1\) when \(M>d^{-1/2}\). The false-positive probability conditional on \(J=0\) is \(e^{-\sqrt d/q}\). The false-negative probability conditional on \(J=1\) is at most \(\Pr(Z\le d^{-1/2})\le d^{-1/2}\). Given \(M\), the binary error indicator determines \(J\); its entropy is at most the binary entropy of the classifier's error probability. When the bound on the error probability is at most \(1/2\), monotonicity of binary entropy there gives the displayed upper bound. The lower bound follows from \(H(J\mid M)\ge0\) and the bound on \(\delta_\varepsilon\). For fixed \(\theta\) the upper bound is \(O_\theta(d^{-1/2}\log d)\) and the lower bound is \(O_\theta(d^{-1})\) in magnitude, establishing the expansion.

## Verification

The unchanged `check.py` uses SciPy quadrature of the scalar density, tests its normalization and the entropy identities, and compares with the finite remainder bounds. Benchmarks in nats at \(\theta=1/2\) are \(T_2\approx0.315467309390\), \(T_{100}\approx66.013754179575\), and \(T_{1000}\approx688.661456244993\). Finite quadrature illustrates the formula; it is not the proof of the asymptotic.

## Relationship to prior work and limitations

The homogeneous Raftery law and its Bernoulli common-exponential shock representation are from [1], which studies the copula, concordance, Pearson correlation, tail dependence and estimation. The heterogeneous model [2] concerns varying dependence parameters. The general identity between total correlation and negative copula entropy is standard [3]. The contribution here is the exact reduction to the scalar sample-minimum density for this model, and the dimension-dependent logarithmic and constant terms with an explicit error envelope. The derivation does not depend on pairwise correlations alone; the posterior uncertainty of the mixture contributes to the remainder. No claim is made for the heterogeneous model, other shock laws, or varying-parameter limits. The comparisons above do not establish exhaustive historical priority.

## References

1. T. Saali, M. Mesfioui and A. Shabri, “Multivariate Extension of Raftery Copula,” *Mathematics* **11** (2023), 414. https://doi.org/10.3390/math11020414.
2. T. Saali, M. Mesfioui and A. Shabri, “A novel multivariate copula of Raftery type with multiple dependence parameters and its neutrosophic application in finance,” *International Journal of Neutrosophic Science* **23** (2024), 296–307. https://doi.org/10.54216/IJNS.230224.
3. J. Ma and Z. Sun, “Mutual information is copula entropy,” arXiv:0808.0845. https://arxiv.org/abs/0808.0845.
