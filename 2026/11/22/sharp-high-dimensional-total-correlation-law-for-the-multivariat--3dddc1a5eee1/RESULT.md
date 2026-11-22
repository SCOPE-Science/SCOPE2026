# Sharp high-dimensional total-correlation law for the multivariate Raftery copula

## Finding

For fixed \(0<\theta<1\), put \(q=1-\theta\). In every integer dimension \(d\ge2\), take independent unit-rate exponential variables \(E_1,\ldots,E_d,Z\), an independent Bernoulli variable \(J\) with \(\Pr(J=1)=\theta\), and define
\[
 X_i=qE_i+JZ,\qquad i=1,\ldots,d.
\]
Each \(X_i\) is unit-rate exponential, and its joint copula is the homogeneous multivariate Raftery copula of Saali, Mesfioui and Shabri (2023). Let
\[
 T_d(\theta)=D_{\mathrm{KL}}\!\left(\mathcal L(X_1,\ldots,X_d)\;\middle\|\;\bigotimes_{i=1}^d\mathcal L(X_i)\right)
\]
be total correlation in *nats*. Set \(\varepsilon=q/d\) and define the one-dimensional probability density, for \(t\ge0\),
\[
 g_{d,\theta}(t)=\frac{q}{\varepsilon}e^{-t/\varepsilon}+\frac{\theta}{1-\varepsilon}\bigl(e^{-t}-e^{-t/\varepsilon}\bigr).
\]
Then the **exact finite-dimensional reduction** is
\[
 \boxed{T_d(\theta)=d\log(1/q)+1+\log\varepsilon-h(g_{d,\theta}),\qquad
 h(g)=-\int_0^\infty g(t)\log g(t)\,dt.}
\]
Moreover, as integer \(d\to\infty\) with \(\theta\) fixed,
\[
 \boxed{T_d(\theta)=d\log(1/q)-\theta\log(d/q)-H_b(\theta)+o(1),}
\]
where \(H_b(\theta)=-\theta\log\theta-q\log q\). Hence the coefficient of the logarithmic deficit is **exactly the common-shock activation probability** \(\theta\), with the explicit constant \(-H_b(\theta)+\theta\log q\) if the logarithmic term is written as \(-\theta\log d\).

More quantitatively, put \(R_d=T_d-d\log(1/q)+\theta\log(d/q)+H_b(\theta)\). For all sufficiently large \(d\),
\[
 -\theta\log(1+q/d)\le R_d\le
 H_b\!\left(qe^{-\sqrt d/q}+\theta d^{-1/2}\right),
\]
provided the displayed binary-entropy argument is at most \(1/2\). In particular the remainder is \(O_\theta(d^{-1/2}\log d)\). Both the exact one-dimensional formula and the sharp three-term expansion are part of the finding.

## Assumptions and scope

All logarithms are natural. The integer dimension satisfies \(d\ge2\) and the dependence parameter is held fixed in \(0<\theta<1\). The normalizations above use unit-rate exponential margins; replacing them by arbitrary positive marginal exponential rates leaves the copula and the total correlation unchanged under coordinatewise one-to-one rescaling. The endpoints are excluded from the asymptotic claim: \(\theta=0\) is independence, whereas \(\theta=1\) is singular comonotonicity. No uniform asymptotic statement is claimed when \(\theta\) varies with \(d\).

The original model is sometimes written in the survival-uniform coordinates \(U_i=e^{-X_i}\); invertible coordinatewise transforms preserve the relative entropy defining \(T_d\).

## Proof

**1. The margins are exactly exponential.** Let \(W=JZ\). For \(s\ge0\), independence gives
\[
 \mathbb E e^{-sX_i}=\frac{q+\theta/(1+s)}{1+qs}
 =\frac{1}{1+s},
\]
using \(q+\theta=1\). Thus \(h(X_i)=1\) and the product reference measure is the product of unit exponentials.

**2. The sample minimum contains all information about the shock.** Conditional on \(W=w\),
\[
 f_{\mathbf X\mid W=w}(x_1,\ldots,x_d)
 =q^{-d}\exp\!\left(-\frac{\sum_i x_i-dw}{q}\right)
 \mathbf1\{w\le\min_i x_i\}.
\]
The part of this likelihood depending on \(w\) depends on the observations only through \(M=\min_iX_i\). The factorization theorem (or direct Bayes formula) implies \(W\) and \(\mathbf X\) are conditionally independent given \(M\), so \(I(W;\mathbf X)=I(W;M)\). Independently, the minimum of \(d\) unit exponential noises is a unit exponential divided by \(d\). Thus
\[
 M\overset d=W+\varepsilon E,\qquad \varepsilon=q/d,
\]
for a fresh independent unit-rate exponential \(E\). Given \(J=0\), \(M=\varepsilon E\); given \(J=1\), \(M=Z+\varepsilon E\). Convolving the two exponential densities yields the stated \(g_{d,\theta}\). Since \(d\ge2\), \(0<\varepsilon<1\), so its formula is nonsingular.

**3. Finite-dimensional entropy reduction.** Conditional independence of \(X_i\) given \(W\) gives
\[
 h(\mathbf X\mid W)=d(1+\log q),\qquad
 h(\mathbf X)=d(1+\log q)+I(W;\mathbf X).
\]
On the other hand, \(h(M\mid W)=1+\log\varepsilon\), hence
\[
 I(W;\mathbf X)=I(W;M)=h(g_{d,\theta})-1-\log\varepsilon.
\]
Subtracting the joint entropy from \(\sum_i h(X_i)=d\) proves the exact one-dimensional formula. No finite-dimensional entropy integration over \(\mathbb R^d\) is needed.

**4. Exact asymptotic decomposition.** Put \(Y_\varepsilon=Z+\varepsilon E\) and \(\delta_\varepsilon=h(Y_\varepsilon)-1\). Because conditioning cannot increase differential entropy,
\(h(Y_\varepsilon)\ge h(Y_\varepsilon\mid\varepsilon E)=h(Z)=1\). As \(Y_\varepsilon\ge0\) has mean \(1+\varepsilon\), the maximum-entropy property of the exponential gives
\[
 0\le\delta_\varepsilon\le\log(1+\varepsilon).
\]
For the discrete mixture indicator \(J\), the entropy-of-mixtures identity reads
\[
 h(M)=q\,[1+\log\varepsilon]+\theta\,h(Y_\varepsilon)
 +H_b(\theta)-H(J\mid M).
\]
Combining this identity with Step 3 gives the *exact* decomposition
\[
 T_d=d\log(1/q)-\theta\log(d/q)-H_b(\theta)
 -\theta\delta_\varepsilon+H(J\mid M).
\]

**5. Quantitative vanishing of the posterior binary entropy.** Classify \(J=1\) when \(M>d^{-1/2}\), otherwise classify \(J=0\). Given \(J=0\), the false-positive probability equals \(e^{-\sqrt d/q}\). Given \(J=1\), \(M\ge Z\), so the false-negative probability is at most \(\Pr(Z\le d^{-1/2})\le d^{-1/2}\). The classifier therefore has error at most
\[
 p_d=qe^{-\sqrt d/q}+\theta d^{-1/2}.
\]
For sufficiently large \(d\), \(p_d\le1/2\). The binary conditional-entropy inequality then yields \(0\le H(J\mid M)\le H_b(p_d)\), and \(H_b(p_d)=O_\theta(d^{-1/2}\log d)\). Together with \(\delta_\varepsilon\le\log(1+q/d)\), this proves the stated finite remainder bounds and the limit. The argument is uniform across every integer \(d\) once \(\theta\) is fixed.

## Verification

The companion `check.py` evaluates the exact one-dimensional integral with separate quadrature intervals adapted to the narrow \(\varepsilon\)-scale peak, checks normalization and mixture-entropy identities, and tests the asymptotic envelope at several parameters and dimensions. In particular, it checks \(T_2(1/2)\approx0.315467309390\), \(T_{100}(1/2)\approx66.013754179575\) and \(T_{1000}(1/2)\approx688.661456244993\) nats. Its numerical tests are reproducibility checks, not substitutes for the all-dimensional analytic proof. Required environment: Python 3 with SciPy.

## Relationship to prior work

Saali, Mesfioui and Shabri (2023) introduce the homogeneous multivariate Raftery copula using the same Bernoulli-common-exponential construction and establish its copula density, rank concordance, Pearson correlation and tail dependence. The new statement does **not** claim to originate this family or the common-shock representation. Rather, it gives a precise information-theoretic identity and its constant-order high-dimensional asymptotic; those are not among the cited paper's results.

Saali, Mesfioui and Shabri (2024) extend the family to heterogeneous dependence parameters. Their construction includes the homogeneous model but provides moments, rank dependence and estimation rather than the exact relative-entropy asymptotics above. General total-correlation identities (e.g. Rowe and Day, 2019) are used as standard tools, not claimed as new. The result cannot be deduced from pairwise correlations alone: the nonlinear mixture entropy contributes the logarithmic term and its binary-entropy constant.

## Limitations

This is a self-review, not an independent validation. Claims of historical novelty are based on the inspected literature and similarity searches, not an exhaustive publication census. The sharp asymptotics require a *fixed interior* \(\theta\); behavior close to either parameter endpoint, other multivariate shock laws and the heterogeneous extension are not classified. The numerical checker evaluates finitely many examples only and does not certify the theorem independently.

## References

1. Saali, T., Mesfioui, M., and Shabri, A. (2023), “Multivariate Extension of Raftery Copula,” *Mathematics* **11**, 414. First published 12 January 2023. https://doi.org/10.3390/math11020414 ; open full text: https://pdfs.semanticscholar.org/200d/f5e1c9da1e7d088352ddb1b7394211c0ff32.pdf
2. Saali, T., Mesfioui, M., and Shabri, A. (2024), “A novel multivariate copula of Raftery type with multiple dependence parameters and its neutrosophic application in finance,” *International Journal of Neutrosophic Science* **23**(2), 296–307. https://doi.org/10.54216/IJNS.230224 ; full text: https://www.americaspg.com/article/2404/pdf/stream
3. Rowe, T., and Day, T. (2019), “The Sampling Distribution of the Total Correlation for Multivariate Gaussian Random Variables,” *Entropy* **21**, 921. https://doi.org/10.3390/e21100921
4. Ma, J. and Sun, Z. (2008), “Mutual information is copula entropy,” arXiv:0808.0845. https://arxiv.org/abs/0808.0845
