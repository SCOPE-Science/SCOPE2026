# An entropy reversal for maxima of independent Poisson counts

## Finding

Fix an integer \(m\ge 2\). Let \(N_1,\ldots,N_m\) be independent \(\operatorname{Pois}(\lambda)\) random variables with common intensity \(\lambda>0\), let \(M_{m,\lambda}=\max_{1\le i\le m}N_i\), and use Shannon entropy in natural logarithm units. Set
\[
\Delta_m(\lambda)=H(M_{m,\lambda})-H(N_1).
\]
Then there is a **sign reversal** from positive entropy gain at low intensity to negative entropy gain at high intensity. Quantitatively, with \(m\) fixed,
\[
\Delta_m(\lambda)=(m-1)\lambda\log(1/\lambda)
+\bigl(m-1-m\log m\bigr)\lambda
+O_m\!\left(\lambda^2\log(1/\lambda)\right)
\quad(\lambda\downarrow0).
\]
Let \(Z_1,\ldots,Z_m\) be independent standard normal random variables and \(Y_m=\max_{1\le i\le m}Z_i\). Then
\[
\lim_{\lambda\to\infty}\Delta_m(\lambda)
=c_m:=\frac{\mathbb E[Y_m^2]-1}{2}
+1-\frac1m-\log m<0,
\]
where the exact constant is specified by the convergent integral
\[
\mathbb E[Y_m^2]=m\int_{-\infty}^{\infty}
 x^2\varphi(x)\Phi(x)^{m-1}\,dx.
\]
Here \(\varphi\) and \(\Phi\) denote the standard normal density and distribution function. In particular,
\[
 c_2=\frac12-\log2=-0.193147180559945\ldots.
\]
Consequently, for every fixed integer \(m\ge2\), there exists at least one \(\lambda_m\in(0,\infty)\) with \(\Delta_m(\lambda_m)=0\). **Neither uniqueness of a zero nor monotonicity of the difference is asserted.**

## Assumptions and scope

All samples have a deterministic fixed size \(m\), all constituent Poisson variables are independent with the same positive intensity, and the parameter limits keep \(m\) fixed. Discrete entropy is \(H(X)=-\sum_{k\ge0}\Pr(X=k)\log\Pr(X=k)\) with \(0\log0:=0\). Differential entropy is denoted \(h\), not \(H\). No uniform-in-\(m\) result is claimed.

## Proof

**1. Probability masses and an exact entropy identity.** Put
\[
p_k=e^{-\lambda}\frac{\lambda^k}{k!},\qquad
F_k=\sum_{j=0}^k p_j,\qquad F_{-1}=0.
\]
Since \(\Pr(M_{m,\lambda}\le k)=F_k^m\), the maximum has mass
\[
r_k=F_k^m-F_{k-1}^m=p_k A_{m,k},\quad
A_{m,k}=\sum_{j=0}^{m-1}F_k^{m-1-j}F_{k-1}^j.
\]
All masses are positive, the entropies converge absolutely, and therefore
\[
\Delta_m(\lambda)=
\mathbb E[\log p_{N_1}]-\mathbb E[\log p_{M_{m,\lambda}}]
-\mathbb E[\log A_{m,M_{m,\lambda}}].\tag{1}
\]
The subscript of \(p\) denotes the count at which the same Poisson mass function is evaluated, not a new law.

**2. Low-intensity expansion.** For fixed \(m\),
\[
\Pr(M_{m,\lambda}=0)=e^{-m\lambda}=1-m\lambda+O_m(\lambda^2),
\]
\[
\Pr(M_{m,\lambda}=1)=
[e^{-\lambda}(1+\lambda)]^m-e^{-m\lambda}
=m\lambda+O_m(\lambda^2).
\]
The total probability of counts at least two is \(O_m(\lambda^2)\). More strongly, their **total entropy contribution** is \(O_m(\lambda^2\log(1/\lambda))\): use \(r_k\le m p_k\le m\lambda^k/k!\) for \(k\ge2\), and the fact that \(-t\log t\) increases on \((0,e^{-1})\), followed by summing \(\sum_{k\ge2}(\lambda^k/k!)[1+k\log(1/\lambda)+\log(k!)]\). It follows that
\[
H(M_{m,\lambda})=m\lambda\bigl[1-\log(m\lambda)\bigr]
+O_m(\lambda^2\log(1/\lambda)).
\]
The same calculation at \(m=1\) gives
\[
H(N_1)=\lambda[1-\log\lambda]
+O(\lambda^2\log(1/\lambda)).
\]
Subtracting yields the first displayed asymptotic and its positive leading term.

**3. Log-Poisson mass asymptotics in expectation.** Define
\[
T_{m,\lambda}=\frac{M_{m,\lambda}-\lambda}{\sqrt\lambda},
\qquad T_{1,\lambda}=\frac{N_1-\lambda}{\sqrt\lambda}.
\]
The multivariate central limit theorem and the continuous mapping theorem give \(T_{m,\lambda}\Rightarrow Y_m\) and \(T_{1,\lambda}\Rightarrow Z_1\). Uniform bounds on any fixed centered standardized Poisson moment, together with \(|T_{m,\lambda}|\le\max_i|(N_i-\lambda)/\sqrt\lambda|\), ensure convergence of the corresponding second moments. Stirling's formula, expanded on the interval \(|k-\lambda|\le\lambda/2\), gives
\[
\log p_k=-\frac12\log(2\pi\lambda)
-\frac{(k-\lambda)^2}{2\lambda}+R_\lambda(k)
\]
with
\[
|R_\lambda(k)|\le C\left(\lambda^{-1}+\frac{|k-\lambda|}{\lambda}
+\frac{|k-\lambda|^3}{\lambda^2}\right).
\]
The expected remainder tends to zero under either \(k=N_1\) or \(k=M_{m,\lambda}\) by third-moment bounds; on the complementary event the Poisson Chernoff tails are exponentially small and Stirling's global bound makes the remaining expectation negligible. Hence
\[
\mathbb E[\log p_{N_1}]-\mathbb E[\log p_{M_{m,\lambda}}]
\longrightarrow\frac{\mathbb E[Y_m^2]-1}{2}.\tag{2}
\]
This step controls the expectation, rather than merely applying a pointwise local limit approximation.

**4. Distribution-function contribution.** Define \(U_\lambda=F_{M_{m,\lambda}}\). For each \(u\in(0,1)\), because the maximum's CDF is \(F_k^m\),
\[
\Pr(U_\lambda\le u)\le u^m.
\]
The largest Poisson atom tends to zero as \(\lambda\to\infty\), so \(U_\lambda\Rightarrow U\), where \(U\) has \(\operatorname{Beta}(m,1)\) law. Since
\(F_{M_{m,\lambda}-1}=U_\lambda-p_{M_{m,\lambda}}\), it follows that
\[
A_{m,M_{m,\lambda}}\Rightarrow mU^{m-1}.
\]
The expectation of its logarithm also converges. Indeed,
\[
U_\lambda^{m-1}\le A_{m,M_{m,\lambda}}\le m,
\qquad
|\log A_{m,M_{m,\lambda}}|
\le\log m+(m-1)(-\log U_\lambda).
\]
The uniform tail inequality \(\Pr(-\log U_\lambda>t)\le e^{-mt}\) proves uniform integrability of these logarithms. Finally, \(\mathbb E[\log U]=-1/m\), whence
\[
\mathbb E[\log A_{m,M_{m,\lambda}}]
\longrightarrow\log m-\frac{m-1}{m}.\tag{3}
\]
Equations (1)–(3) prove the stated large-intensity limit.

**5. Strict negativity of the constant.** The density of \(Y_m\) is \(m\varphi(x)\Phi(x)^{m-1}\), and the transformation \(\Phi(Y_m)\sim\operatorname{Beta}(m,1)\) gives exactly
\[
h(Y_m)-h(Z_1)=\frac{\mathbb E[Y_m^2]-1}{2}
+\frac{m-1}{m}-\log m=c_m.
\]
Gaussian Poincaré applied to the Lipschitz function \(f(z_1,\ldots,z_m)=\max_i z_i\) gives
\[
\operatorname{Var}(Y_m)\le\mathbb E\|\nabla f(Z)\|^2=1.
\]
Equality in Gaussian Poincaré is possible only for an affine function, as seen directly from the Hermite-chaos expansion (the derivative energy multiplies every homogeneous chaos of degree \(d\) by \(d\), while the variance multiplies it by one). The maximum function is not affine for \(m\ge2\), so the inequality is strict. The Gaussian maximum-entropy bound therefore gives
\[
h(Y_m)\le\tfrac12\log\bigl(2\pi e\operatorname{Var}(Y_m)\bigr)
<\tfrac12\log(2\pi e)=h(Z_1).
\]
Thus \(c_m<0\). For \(m=2\), symmetry and \(\max(Z_1,Z_2)^2+\min(Z_1,Z_2)^2=Z_1^2+Z_2^2\) give \(\mathbb E[Y_2^2]=1\), hence \(c_2=1/2-\log2\). Finally, \(\Delta_m\) is continuous for \(\lambda>0\) by locally uniform convergence of its absolutely summable entropy series (Poisson tails); the opposite endpoint signs imply at least one root by the intermediate value theorem.

## Verification

The accompanying standalone `checker.py` (Python standard library only) calculates the exact discrete mass \(r_k=p_k A_{m,k}\) via a stable factorized formula, evaluates finite-intensity entropies, and computes the Gaussian-second-moment integral by Simpson quadrature. It confirms small positive and large negative entropy differences for sample sizes two, three, five and ten; checks the small-intensity expansion numerically; and reproduces the exact two-sample limiting constant. Running `python checker.py` prints the numerical comparisons and exits successfully. These numerical checks corroborate, but do not replace, the analytical proof, which covers every fixed integer \(m\ge2\) and all limiting intensities.

## Relationship to prior work

Badiella, del Castillo and Puig (2023) prove that discrete order statistics preserve ultra-log-concavity and deduce that Poisson order statistics are underdispersed relative to their own means. Their paper gives the order-statistic mass representation used here, but does not compare Shannon entropy of a Poisson maximum to that of its parent over the intensity axis. Earlier results on Shannon entropy of the Poisson parent distribution concern the parent alone; Gaussian Poincaré and the normal maximum-entropy property are classical, independently used tools. Published research on variance transitions and high-intensity Fano factors for two Poisson extremes concerns moments, not the present fixed-sample-size Shannon-entropy sign reversal and exact Gaussian-maximum entropy constants. Entropy cannot in general be ordered from a variance comparison alone.

## Limitations

The theorem does not establish uniqueness or location of the entropy-equality intensity, nor an all-intensity ordering, and makes no claim when sample size grows with intensity. The normal-maximum second moments beyond \(m=2\) are represented by a convergent integral, not claimed to have elementary closed forms. Priority is based on the primary works and search coverage stated in the accompanying review; absence of a matching search result is not a proof of historical novelty. No independent external verification is asserted.

## References

1. L. Badiella, J. del Castillo and P. Puig, *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters 201 (2023), 109900, available online 26 June 2023. https://doi.org/10.1016/j.spl.2023.109900 ; lawful full text: https://ddd.uab.cat/pub/artpub/2023/283158/StaProLet_a2023v201n109900.pdf
2. V. Braiman, A. Malyarenko, Y. Mishura and Y. A. Rudyk, *Properties of Shannon and Rényi entropies of the Poisson distribution as the functions of intensity parameter*, Nonlinear Analysis: Modelling and Control 29 (2024), 802–815. https://doi.org/10.15388/namc.2024.29.35560
3. N. Balakrishnan, F. Buono and M. Longobardi, *On cumulative entropies in terms of moments of order statistics*, Methodology and Computing in Applied Probability 24 (2022), 345–359; first published 3 March 2021. https://doi.org/10.1007/s11009-021-09850-0 (distinct cumulative-entropy functional).
4. *Normal distribution maximizes differential entropy for fixed variance*, The Book of Statistical Proofs. https://statproofbook.github.io/P/norm-maxent
