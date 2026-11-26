# First finite-size correction to critical Curie–Weiss pair dependence

## Finding

For the zero-field critical Curie–Weiss Gibbs measure
\[
\mu_N(\sigma)\propto\exp\!\left[\frac{1}{2N}\left(\sum_{i=1}^N\sigma_i\right)^2\right],\qquad
\sigma_i\in\{-1,+1\},
\]
let \(c_N=\mathbb E_{\mu_N}[\sigma_1\sigma_2]\) for distinct sites and define
\[
a=\sqrt{12}\,\frac{\Gamma(3/4)}{\Gamma(1/4)}.
\]
Then
\[
\boxed{c_N=aN^{-1/2}-\left(1+\frac{a^2}{5}\right)N^{-1}+O(N^{-3/2})}
\qquad (N\to\infty).
\]
The \(N^{-1}\) term is the first finite-size correction beyond the critical quartic-fluctuation limit.

## Assumptions and scope

The spins are exchangeable, the external field is zero, and the inverse temperature is exactly the Curie–Weiss critical value \(\beta=1\) in the normalization above. The observable is the correlation of two distinct spins. The result is asymptotic as integer \(N\to\infty\); it does not assert the same coefficients away from criticality, for nonzero field, or for finite-dimensional short-range Ising models.

## Proof

Write \(M_N=\sum_{i=1}^N\sigma_i\) and \(m_N=M_N/N\). If \(m=(2k-N)/N\), its unnormalized probability is
\[
w_N(m)=\binom{N}{N(1+m)/2}\exp(Nm^2/2).
\]
The binary entropy function has the expansion
\[
\frac{(1+m)\log(1+m)+(1-m)\log(1-m)}{2}
=\frac{m^2}{2}+\frac{m^4}{12}+\frac{m^6}{30}+O(m^8).
\]
Stirling's formula supplies the prefactor \((1-m^2)^{-1/2}\) up to relative error \(1+O(N^{-1})\) uniformly on shrinking central windows. Put \(x=N^{1/4}m\). On \(|x|\le N^\varepsilon\), for a fixed sufficiently small \(\varepsilon>0\), the scaled weight therefore has the form
\[
w_N(x)\propto e^{-x^4/12}\left[1+N^{-1/2}g(x)+O\!\left(N^{-1}P(x)\right)\right],
\qquad g(x)=\frac{x^2}{2}-\frac{x^6}{30},
\]
where \(P\) is a fixed polynomial bound on the central window. The complement is negligible to every algebraic order: the entropy remainder satisfies \(I(m)-m^2/2\ge m^4/12\) for \(|m|<1\), and the binomial tails at the endpoints are exponentially smaller. The mesh in \(x\) is \(2N^{-3/4}\); symmetric sum-to-integral errors are below the displayed order.

Let \(X\) have density proportional to \(e^{-x^4/12}\), and write \(\mu_r=\mathbb E[X^r]\) for even \(r\). Direct integration gives
\[
\mu_2=a=\sqrt{12}\,\frac{\Gamma(3/4)}{\Gamma(1/4)},\qquad
\mu_{r+4}=3(r+1)\mu_r.
\]
Consequently \(\mu_4=3\), \(\mu_6=9a\), and \(\mu_8=45\). Expanding the normalized expectation, not just the unnormalized weight, yields
\[
\begin{aligned}
\mathbb E[m_N^2]
&=N^{-1/2}\left(\mu_2+N^{-1/2}\operatorname{Cov}(X^2,g(X))+O(N^{-1})\right),\\
\operatorname{Cov}(X^2,g(X))
&=\frac12(\mu_4-a^2)-\frac1{30}(\mu_8-a\mu_6)\\
&=\frac12(3-a^2)-\frac1{30}(45-9a^2)=-\frac{a^2}{5}.
\end{aligned}
\]
Thus
\[
\mathbb E[m_N^2]=aN^{-1/2}-\frac{a^2}{5}N^{-1}+O(N^{-3/2}).
\]
Exchangeability and spin-flip symmetry give
\[
\mathbb E[M_N^2]=N+N(N-1)c_N,
\qquad c_N=\frac{N\mathbb E[m_N^2]-1}{N-1}.
\]
Substitution and expansion of \((N-1)^{-1}\) prove the stated formula.

## Verification

The proof reduces the asymptotic to Stirling's expansion, the quartic entropy bound, the Gaussian-free quartic moment recurrence, and the exact exchangeability identity. The attached standard-library script evaluates the finite sum directly using log weights, and checks that \(N(c_N-aN^{-1/2})\) approaches \(-(1+a^2/5)\). This computation is corroborative only; it is not used as a proof of the asymptotic remainder.

## Relationship to prior work

Jalowy, Kabluchko, and Löwe prove a critical Curie–Weiss approximation by mixtures of product measures and identify the quartic limiting density proportional to \(e^{-x^4/12}\) (Theorem 4.4 of the cited article). That limiting law explains the leading constant \(a\), but a weak limit alone does not determine the next normalized moment correction. The result here gives the explicit \(N^{-1}\) coefficient for the two-site correlation. Earlier critical limit-theorem and propagation-of-chaos literature is relevant; the full text of the cited 1978 limit-theorem paper and the 2023 propagation-of-chaos paper was not inspected in this run, so novelty is not claimed to be exhaustive against every higher-order expansion.

## Limitations

This is a finite-size asymptotic for the zero-field critical Curie–Weiss model only. It does not establish a new phase transition result, a statement for off-critical parameters, or a result for local lattice interactions. The remainder estimate follows from the central Stirling expansion and quartic tail control; the numerical check is not a substitute for that argument. A residual literature risk remains that older higher-order Curie–Weiss expansions contain an equivalent coefficient.

## References

1. J. Jalowy, Z. Kabluchko, and M. Löwe, “Propagation of Chaos and Residual Dependence in Gibbs Measures on Finite Sets,” *Mathematical Physics, Analysis and Geometry* **28** (2025), article 6. DOI: 10.1007/s11040-025-09503-5. Published 15 March 2025.
2. J. Jalowy, Z. Kabluchko, M. Löwe, and A. Marynych, “When does the chaos in the Curie-Weiss model stop to propagate?” *Electronic Journal of Probability* **28** (2023), 1–17. Cited in Ref. 1; full text not inspected here.
3. R. S. Ellis and C. M. Newman, “Limit theorems for sums of dependent random variables occurring in statistical mechanics,” *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete* **44** (1978), 117–139. Cited in Ref. 1; full text not inspected here.
