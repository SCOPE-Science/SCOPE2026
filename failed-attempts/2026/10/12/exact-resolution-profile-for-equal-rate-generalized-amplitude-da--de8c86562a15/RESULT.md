# Exact resolution profile for equal-rate generalized amplitude damping discrimination
## Finding
Let \(\mu\ge 0\), and let the equal-rate generalized amplitude-damping Lindbladian on a qubit be
\[
\mathcal L_\mu(\rho)=\mu\!\left(\sigma_-\rho\sigma_++\sigma_+\rho\sigma_- -\rho\right),
\]
with \(\sigma_-=|0\rangle\!\langle1|\) and \(\sigma_+=|1\rangle\!\langle0|\). Take the identity semigroup as the null hypothesis and \(\mathcal L_\mu\) as the alternative. Using the base-two logarithm convention of arXiv:2610.03629v1, the resolution-constrained asymptotic Stein exponent defined there satisfies, for every \(s_{\min}>0\),
\[
\Gamma_{s_{\min}}(0\|\mathcal L_\mu)
=-\frac{2}{s_{\min}}\log_2\!\left(\frac{1+e^{-\mu s_{\min}}}{2}\right).
\]
Consequently the unrestricted Lindbladian Stein exponent is
\[
\gamma(0\|\mathcal L_\mu)=\mu\log_2 e.
\]
For \(\mu>0\), the fixed-resolution exponent is strictly decreasing as \(s_{\min}\) increases, and as \(s_{\min}\downarrow0\),
\[
\Gamma_{s_{\min}}(0\|\mathcal L_\mu)
=\mu\log_2 e-\frac{\mu^2s_{\min}}{4}\log_2 e+O(s_{\min}^3).
\]
Thus the equal-rate finite-exponent regime in arXiv:2610.03629v1 admits an exact temporal-resolution profile, rather than only the finiteness statement given there.

## Assumptions and scope
The system is a single qubit. The two jump rates are exactly equal, \(\mu_+=\mu_-=\mu\), there is no Hamiltonian part, and the null hypothesis is the identity semigroup. The discrimination model, total exposure-time accounting, arbitrary finite-dimensional ancillary systems, adaptive controls, and minimum evolution interval \(s_{\min}\) are exactly those of arXiv:2610.03629v1. All logarithms in the displayed exponents are base two. In natural logarithm units the unrestricted exponent is simply \(\mu\).

The formula concerns the asymptotic exponent \(\Gamma_{s_{\min}}\) at fixed positive resolution and the unrestricted exponent \(\gamma\). It does not give an exact finite-total-time type-II error probability, and it does not extend to unequal positive transition rates, for which the source proves that the unrestricted exponent is infinite.

## Proof
Write \(a=e^{-\mu s}\). Directly from the generator,
\[
\mathcal L_\mu(I)=0,\qquad
\mathcal L_\mu(X)=-\mu X,\qquad
\mathcal L_\mu(Y)=-\mu Y,\qquad
\mathcal L_\mu(Z)=-2\mu Z.
\]
Hence the time-\(s\) channel \(\mathcal N_s=e^{s\mathcal L_\mu}\) is the Pauli channel
\[
\mathcal N_s
=p_I\,\mathrm{id}+p_X\,\operatorname{Ad}_X+p_Y\,\operatorname{Ad}_Y+p_Z\,\operatorname{Ad}_Z,
\]
where \(\operatorname{Ad}_P(\rho)=P\rho P\) and
\[
p_I=\frac{(1+a)^2}{4},\qquad
p_X=p_Y=\frac{1-a^2}{4},\qquad
p_Z=\frac{(1-a)^2}{4}.
\]
These probabilities reproduce the Pauli eigenvalues \(a,a,a^2\), so the decomposition is exact.

We next evaluate the amortized channel relative entropy in the source's Theorem A1. Since \(\mathcal N_s-p_I\,\mathrm{id}\) is completely positive,
\[
(\mathcal N_s\otimes\mathrm{id}_E)(\sigma)\succeq p_I\sigma
\]
for every ancillary system \(E\) and state \(\sigma\). For any input pair \(\rho,\sigma\) with finite \(D(\rho\|\sigma)\), operator monotonicity of the logarithm gives
\[
D\!\left(\rho\middle\|(\mathcal N_s\otimes\mathrm{id}_E)(\sigma)\right)-D(\rho\|\sigma)
\le -\log_2 p_I.
\]
Thus
\[
D_A(\mathrm{id}\|\mathcal N_s)\le-\log_2p_I.
\]
Equality is attained with a maximally entangled qubit pair and the same state under both hypotheses: the identity channel leaves the corresponding Bell state pure, whereas \(\mathcal N_s\) produces a Bell-diagonal Choi state whose weight on that Bell state is exactly \(p_I\). Therefore
\[
D_A(\mathrm{id}\|\mathcal N_s)
=-\log_2p_I
=-2\log_2\!\left(\frac{1+e^{-\mu s}}2\right).
\]

Theorem A1 of arXiv:2610.03629v1 identifies the fixed-resolution asymptotic exponent with
\[
\Gamma_{s_{\min}}(0\|\mathcal L_\mu)
=\sup_{s\ge s_{\min}}\frac{1}{s}D_A(\mathrm{id}\|\mathcal N_s),
\]
and the unrestricted exponent with the same supremum over \(s>0\). Put
\[
g(x)=-\ln\!\left(\frac{1+e^{-x}}2\right).
\]
Then \(g(0)=0\) and
\[
g''(x)=-\frac{e^x}{(1+e^x)^2}<0\qquad(x>0).
\]
Hence \(g\) is strictly concave, so \(g(x)/x\) is strictly decreasing on \((0,\infty)\). The fixed-resolution supremum is therefore attained at \(s=s_{\min}\), proving the first formula. Since \(g'(0)=1/2\), letting \(s\downarrow0\) gives
\[
\gamma(0\|\mathcal L_\mu)=\mu\log_2 e.
\]
Finally,
\[
g(x)=\frac{x}{2}-\frac{x^2}{8}+\frac{x^4}{192}+O(x^6),
\]
which yields the stated small-resolution expansion after substituting \(x=\mu s_{\min}\).

## Verification
The proof uses only exact Pauli-basis diagonalization, complete-positivity order, operator monotonicity of the logarithm, a Bell-state saturation argument, and the fixed-resolution variational formula proved in arXiv:2610.03629v1. The accompanying checker verifies the Pauli probabilities, channel eigenvalues, Taylor coefficients, and numerical monotonicity of the closed form at representative parameters. Those computations are corroborative; the proof does not rely on finite sampling or numerical extrapolation.

## Relationship to prior work
ArXiv:2610.03629v1 introduces the Lindbladian discrimination problem, proves the differential and fixed-resolution characterizations of the Stein exponent, and classifies equal-rate generalized amplitude damping as a finite-exponent regime. In its equal-transition-rate subsection it states only \(\gamma(0\|\mathcal L_{\mu,\mu})<\infty\); it evaluates a closed exponent for the depolarizing example but does not evaluate the equal-rate generalized amplitude-damping exponent or its \(s_{\min}\)-profile.

Wilde, Berta, Hirche, and Kaur, arXiv:1808.01498v2, develop amortized channel divergence and show that jointly covariant or jointly teleportation-simulable fixed channels reduce to state discrimination of their resource states. This general fixed-channel machinery is compatible with the Bell-state saturation used here, but it does not introduce the exposure-time optimization of the Lindbladian problem and does not state the equal-rate semigroup profile above. The present calculation combines the recent Lindbladian variational principle with the exact Pauli structure of this semigroup and performs the resulting optimization in closed form.

## Limitations
The equality of transition rates is essential. ArXiv:2610.03629v1 proves that unequal positive rates lie in a qualitatively different regime with infinite unrestricted Stein exponent. The result also assumes the source's idealized instantaneous-control model and asymptotic exposure-time limit. It does not prove an exact nonasymptotic error formula, an optimal control policy under costly or noisy interventions, or a corresponding formula for a general Lindbladian pair.

## References
1. R. Salzmann, L. Lami, M. B. Plenio, and S. F. Huelga, “Discriminating Lindbladian Dynamics,” arXiv:2610.03629v1 (first public 2026-10-02).
2. M. M. Wilde, M. Berta, C. Hirche, and E. Kaur, “Amortized Channel Divergence for Asymptotic Quantum Channel Discrimination,” arXiv:1808.01498v2; Letters in Mathematical Physics 110 (2020), 2277–2336.
