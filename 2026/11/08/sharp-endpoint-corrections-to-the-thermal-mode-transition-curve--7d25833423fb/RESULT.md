# Two endpoint corrections for the thermal mode-transition curve of a trapped run-and-tumble particle

## Finding

Let \(s_c(a)\) be the thermal variance at the stationary mode transition of the harmonically trapped, symmetric one-dimensional run-and-tumble particle, with flip-to-trap rate ratio \(0<a<1\). The contributions are the following two endpoint expansions:
\[
s_c(a)=1-\sqrt{2\pi}\,e^{1/2}\operatorname{erf}(1/\sqrt{2})\,a+O(a^2),\qquad a\downarrow0,
\]
and, with \(\lambda_a=1/(2s_c(a))\) and \(L=\log(1/(1-a))\),
\[
\lambda_a=L+\frac32\log L+\log\!\left(\frac2{\sqrt\pi}\right)+O\!\left(\frac{\log L}{L}\right),\qquad a\uparrow1.
\]
These give the slope at the persistent endpoint and the logarithmic correction and constant beyond the known leading inverse-logarithmic behavior at the other endpoint. The stationary Gaussian convolution, the implicit curvature equation, the strict global geometry of the mode boundary, and the quartic critical maximum are prior results [1–4].

## Assumptions and scope

In \(dX_t=(-\kappa X_t+v\sigma_t)dt+\sqrt{2D}\,dW_t\), take \(\kappa,v,D,\rho>0\); the symmetric sign \(\sigma_t\) flips at rate \(\rho\), independently of \(W_t\). For \(Z=\kappa X/v\), the stationary law is that of \(Y_a+\sqrt{s}G\), where \(a=\rho/\kappa\), \(s=D\kappa/v^2\), \(G\) is independent standard normal, and \(Y_a\) has density proportional to \((1-y^2)^{a-1}\mathbf1_{|y|<1}\). All asymptotics are for this stationary marginal. In particular \(s\) is the Gaussian variance, not the temperature parameter \(2s\) used in [2].

## Proof

For \(\lambda=1/(2s)\), the sign of the curvature at the origin is that of \(H_a(\lambda)\), where
\[
J_a(\lambda)=\int_0^1t^{-1/2}(1-t)^{a-1}e^{-\lambda t}\,dt,\qquad
H_a(\lambda)=-2\lambda J'_a(\lambda)-J_a(\lambda).
\]
Indeed \(t=Y_a^2\) in the convolution integrals and the Gaussian second derivative is proportional to \(2\lambda t-1\). Use the known identification of the mode transition with the unique positive root [3,4]. For clarity, the uniqueness needed here also follows from the confluent-hypergeometric equation \(\lambda J_a''+(a+1/2+\lambda)J_a'+J_a/2=0\): at a positive zero of \(g_a=H_a/J_a\), direct substitution gives \(g'_a=(1-a)/\lambda>0\). At zero \(g_a=-1\), and at large \(\lambda\), \(H_a(\lambda)=(1-a)\sqrt\pi\lambda^{-3/2}+O_a(\lambda^{-5/2})\). The last estimate follows by expanding \((1-t)^{a-1}=1+(1-a)t+O_a(t^2)\) on \([0,1/2]\), extending the powers of \(t\) to infinity with exponentially small errors, and integrating against \((2\lambda t-1)t^{-1/2}e^{-\lambda t}\); the constant term integrates to zero. The remaining part on \([1/2,1]\) is exponentially small for fixed \(a\). This gives existence and excludes a second positive zero.

**Persistent endpoint.** Write \(m_a=-J'_a/J_a\). Uniformly for \(\lambda\) in a compact neighborhood of \(1/2\),
\[
J_a(\lambda)=e^{-\lambda}/a+O(1),\qquad
1-m_a(\lambda)=\frac{\int_0^1t^{-1/2}(1-t)^ae^{-\lambda t}\,dt}{J_a(\lambda)}.
\]
In the first formula, subtract the endpoint value \(e^{-\lambda}\) from \(t^{-1/2}e^{-\lambda t}\): the difference vanishes to first order at \(1\) and is integrable at \(0\). The numerator in the second formula differs from \(I(\lambda)=\int_0^1t^{-1/2}e^{-\lambda t}dt\) by \(O(a)\), using \(|(1-t)^a-1|\le a|\log(1-t)|\). Thus \(1-m_a=ae^\lambda I(\lambda)+O(a^2)\). The root is trapped near \(1/2\) by opposite signs of \(2\lambda m_a-1\) at fixed points on each side. At the root \(s_c=m_a(\lambda_a)=1+O(a)\), so \(\lambda_a=1/2+O(a)\); substituting into the coefficient of \(a\) costs only \(O(a^2)\). Finally \(I(1/2)=\sqrt{2\pi}\operatorname{erf}(1/\sqrt 2)\), which gives the first expansion.

**Endpoint at \(a=1\).** Set \(\epsilon=1-a\), with \(0<\epsilon<1/2\). Integrating \(-2(\sqrt t\,e^{-\lambda t})'\) gives \(H_1(\lambda)=-2e^{-\lambda}\). In \(H_{1-\epsilon}-H_1\), on \([0,1/2]\) expand \((1-t)^{-\epsilon}-1=\epsilon t+O(\epsilon t^2)\) uniformly. The leading integral extended to \([0,\infty)\) is
\[
\epsilon\int_0^\infty (2\lambda t-1)t^{1/2}e^{-\lambda t}\,dt
=\epsilon\sqrt\pi\,\lambda^{-3/2}.
\]
The bulk error is \(O(\epsilon\lambda^{-5/2})\). On \([1/2,1)\), use \((1-t)^{-\epsilon}-1\le\epsilon|\log(1-t)|(1-t)^{-1/2}\), an integrable bound apart from the explicit factor \(\epsilon\), to bound the remaining integral by \(O(\epsilon(1+\lambda)e^{-\lambda/2})\). The extension of the leading integral beyond \(1/2\) has at most this same order. It follows that, uniformly in the indicated \(\epsilon\) range as \(\lambda\to\infty\),
\[
H_{1-\epsilon}(\lambda)=-2e^{-\lambda}+\epsilon\sqrt\pi\,\lambda^{-3/2}\bigl(1+O(\lambda^{-1})\bigr).
\]
At \(\lambda=(1-\delta)L\) with fixed \(0<\delta<1\), the negative exponential term dominates; at \((1+\delta)L\) the positive term dominates. Thus \(\lambda_a/L\to1\). Taking logarithms of the equality of the two terms at the root yields
\[
\lambda_a=L+\tfrac32\log\lambda_a+\log(2/\sqrt\pi)+O(1/\lambda_a).
\]
First this gives \(\lambda_a=L+O(\log L)\), and then \(\log\lambda_a=\log L+O((\log L)/L)\). This proves the stated expansion with its constant and error scale.

## Verification and limitations

The analytic estimates prove the expansions. The accompanying `check_phase.py` tests selected shape parameters by hypergeometric evaluation, including both endpoint approximations; its finite numerical diagnostics are not a proof. Comparisons of the two endpoint limits are valid only with the above variance normalization. No extensions to other confinement laws or noises, or claims of historical priority for the known mode geometry, are made.

## Relationship to prior work

Sabhapandit and Majumdar [1] give the same smoothed density, critical equation and qualitative mode diagram. Guéneau, Majumdar and Schehr [2] give the limiting temperature at vanishing flip rate and the leading inverse log at the other endpoint. With their \(\alpha=2a\) and \(\theta=2s\), their near-critical leading \(\theta_c\sim 1/|\log(2-\alpha)|\) is equivalent to \(s_c\sim 1/(2L)\). The constant in the present expansion uses \(L=\log(1/(1-a))\); changing the logarithm's argument by a constant factor changes the displayed constant. Earlier exact boundary analyses [3,4] include the uniqueness, mode count and quartic boundary; [4] specifically establishes smooth strict decrease of the curve and the normalized fourth derivative \(-2(1-a)/s_c^2\). The present result concerns only the two corrections beyond the endpoint limits and leading equivalent.

## References

1. S. Sabhapandit and S. N. Majumdar, *Noninteracting particles in a harmonic trap with a stochastically driven center*, [arXiv:2404.02480](https://arxiv.org/abs/2404.02480), §4.1.1.
2. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential*, [arXiv:2602.08436](https://arxiv.org/abs/2602.08436), §V.1.1.
3. *Exact thermal unimodality threshold for a harmonically trapped run-and-tumble particle*, [published Resultary record](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-exact-thermal-unimodality-threshold-for-a-harmonically-trapped-r--6d553895bf81).
4. *Rigidity of the thermal mode boundary and exact peak opening*, [published Resultary record](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-rigidity-of-the-thermal-mode-boundary-and-exact-peak-opening-in--74aa462f03c1).
