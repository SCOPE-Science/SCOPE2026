# Gaussian fluctuations and two critical centering exponents for finite Zipf quorum times

## Finding

Consider the finite aligned-Zipf weighted quorum collector with a fixed exponent \(0<s<1\), quorum threshold \(0<\theta<1\), and global arrival rate \(\lambda>0\). Define independent first-discovery times \(T_{j,N}\sim\operatorname{Exp}(\lambda j^{-s}/H_{N,s})\), with \(H_{N,s}=\sum_{j=1}^N j^{-s}\). The strict quorum time \(\tau_N\) is the first time \(\sum_{j:T_{j,N}\le t}j^{-s}/H_{N,s}>\theta\). Write \(W_N=\lambda\tau_N/N\).

Put \(C=1-s\), \(C_N=N^{1-s}/H_{N,s}\), and \(x_{j,N}=j/N\). For \(u\ge0\), let
\[
F_N(u)=1-\frac{C_N}{N}\sum_{j=1}^N x_{j,N}^{-s}\exp(-C_Nu x_{j,N}^{-s}),
\]
with unique root \(u_N>0\) satisfying \(F_N(u_N)=\theta\). Define
\[
J_s(a)=\int_0^1x^{-s}e^{-a x^{-s}}\,dx,\quad
F(u)=1-CJ_s(Cu),\quad F(u_*)=\theta,\quad a_*=Cu_*.
\]
The positive constants
\[
L=C^2\int_0^1x^{-2s}e^{-a_*x^{-s}}\,dx,
\quad V=C^2\int_0^1x^{-2s}e^{-a_*x^{-s}}(1-e^{-a_*x^{-s}})\,dx,
\quad\sigma^2=V/L^2
\]
are finite. Then the exact-mean-centered quorum time satisfies
\[
\boxed{\sqrt N(W_N-u_N)\Longrightarrow\mathcal N(0,\sigma^2).}
\]

The replacement of the exact centering \(u_N\) by the first-order constant \(u_*\) has a sharp hierarchy. Define \(D_s(a)=J_s(a)+aJ_s'(a)=(J_s(a)-e^{-a})/s\), and
\[
B_1=-\frac{C^2\zeta(s)D_s(a_*)}{L},
\]
where \(\zeta\) is the analytic continuation of the Riemann zeta function. Uniformly for each fixed admissible \((s,\theta)\),
\[
\boxed{u_N-u_*=B_1N^{s-1}+O(N^{2s-2}+N^{-1}).}
\]
For every fixed \(s\in(0,1)\), there is exactly one critical threshold \(\theta_0(s)\). It is specified by the unique positive root \(a_0\) of \(J_s(a_0)=e^{-a_0}\), through \(\theta_0(s)=1-Ce^{-a_0}\). The coefficient \(B_1\) is positive for \(\theta<\theta_0(s)\), zero at equality, and negative above it.

For \(\theta\ne\theta_0(s)\), the limit of \(\sqrt N(W_N-u_*)\) is \(\mathcal N(0,\sigma^2)\) if \(s<1/2\), is \(\mathcal N(B_1,\sigma^2)\) if \(s=1/2\), and diverges in probability with the sign of \(B_1\) if \(s>1/2\).

At the unique cancellation threshold \(\theta=\theta_0(s)\), let \(a_*=a_0\) and set
\[
B_2=\frac{C^4\zeta(s)^2u_*D_s'(a_0)}{2L}<0.
\]
For \(s>1/2\) one has
\[
\boxed{u_N-u_*=B_2 N^{2s-2}+o(N^{2s-2}).}
\]
Consequently at the cancellation threshold the limit of \(\sqrt N(W_N-u_*)\) is \(\mathcal N(0,\sigma^2)\) for \(s<3/4\), \(\mathcal N(B_2,\sigma^2)\) for \(s=3/4\), and divergence to \(-\infty\) in probability for \(s>3/4\). These statements concern fixed \(s,\theta,\lambda\), not moving exponent or moving threshold sequences.

## Assumptions and scope

For each integer \(N\ge2\), the \(N\) exponential first-discovery times are independent. The probability/weight vectors coincide and are exactly \(w_{j,N}=p_{j,N}=j^{-s}/H_{N,s}\). The parameter \(s\) is any fixed real number in \((0,1)\), \(\theta\) any fixed real number in \((0,1)\), and \(\lambda>0\) is fixed. The event defining the quorum time uses strict inequality, not weak inequality. All asymptotics are along the integer sequence \(N\to\infty\), without restricting subsequences. The limit variance is positive. The displayed drifting limits mean convergence in probability to the indicated extended-real sign, not convergence to an ordinary real-valued probability distribution.

## Proof

**1. Means, derivatives, and regularity.** Write \(B_{j,N}(u)=\mathbf1\{T_{j,N}\le Nu/\lambda\}\). These are independent Bernoulli variables with failure probabilities \(q_{j,N}(u)=\exp(-C_Nu x_{j,N}^{-s})\). The observed mass \(M_N(u)=\sum_jw_{j,N}B_{j,N}(u)\) has expectation \(F_N(u)\), as displayed above. The functions \(F_N\) increase strictly from zero to one. The limit \(F(u)=1-CJ_s(Cu)\) does likewise, with \(F'(u)=C^2\int_0^1x^{-2s}e^{-Cu x^{-s}}dx>0\) for \(u>0\). Its unique root is \(u_*\). For every compact interval of positive \(u\), the integrands \(x^{-ks}e^{-au x^{-s}}\), with fixed \(a>0\) and any fixed \(k\), extend smoothly by zero at \(x=0\). Riemann sums and their needed derivatives therefore converge uniformly, and \(u_N\to u_*\).

**2. Triangular-array CLT and inversion.** For \(u=u_N+h/\sqrt N\) with any fixed real \(h\), the variance of \(\sqrt N(M_N(u)-F_N(u))\) converges to \(V\). The sum of third absolute centered moments is bounded by
\[
N^{3/2}\sum_{j=1}^Nw_{j,N}^3q_{j,N}(u)
=\frac{C_N^3}{N^{3/2}}\sum_{j=1}^Nx_{j,N}^{-3s}e^{-C_Nu x_{j,N}^{-s}}
=O(N^{-1/2}),
\]
where the last step uses the smooth integrable extension from Step 1 and \(u\to u_*>0\). Lyapunov's theorem yields a centered normal limit with variance \(V>0\). Moreover \(\sqrt N(F_N(u_N+h/\sqrt N)-\theta)\to hL\). Since \(\{W_N\le u\}=\{M_N(u)>\theta\}\), taking probabilities at these moving deterministic times gives
\(\Pr\{\sqrt N(W_N-u_N)\le h\}\to\Phi(hL/\sqrt V)\), proving the exact-centering normal law without assuming any functional CLT. Continuous exponential clocks make the threshold-time distribution atomless.

**3. First centering correction.** The generalized harmonic sum obeys the Euler--Maclaurin expansion
\[
H_{N,s}=\frac{N^{1-s}}{C}+\zeta(s)+O(N^{-s}),\qquad
C_N=C-C^2\zeta(s)N^{s-1}+O(N^{2s-2}+N^{-1}).
\]
For positive \(u\) in a neighborhood of \(u_*\), endpoint smoothness gives the uniform expansion
\[
F_N(u)=G(C_N,u)+O(N^{-1}),\qquad
G(c,u)=1-cJ_s(cu).
\]
Differentiation yields \(G_c(C,u_*)=-D_s(a_*)\), \(G_u(C,u_*)=L\). Taylor's theorem and implicit inversion now give
\[
u_N-u_*=-\frac{C^2\zeta(s)D_s(a_*)}{L}N^{s-1}+O(N^{2s-2}+N^{-1}).
\]
The remainder is an absolute bound with an implicit constant depending on the fixed \(s,\theta\). As \(\zeta(s)<0\) for \(0<s<1\), the sign of the leading coefficient is the sign of \(D_s(a_*)\).

**4. Unique cancellation threshold.** Substitution \(t=x^{-s}\) gives
\[
e^{a}J_s(a)=\frac1s\int_1^\infty t^{-1/s}e^{-a(t-1)}\,dt.
\]
This continuous function decreases strictly from \(1/C>1\) at \(a=0\) to zero at infinity, hence equals one exactly once at \(a_0>0\). An integration-by-parts identity gives \(D_s(a)=(J_s(a)-e^{-a})/s\), so \(D_s(a)\) changes sign from positive to negative exactly at \(a_0\). Because \(a_*=Cu_*\) increases strictly with \(\theta\), the corresponding unique threshold is \(\theta_0(s)=1-Ce^{-a_0}\). The first-order drift regimes then follow from the exact-centering CLT and Slutsky's theorem, including divergence in probability when \(\sqrt N|u_N-u_*|\to\infty\).

**5. Second correction on the cancellation curve.** At \(\theta=\theta_0(s)\), \(G_c(C,u_*)=0\) exactly and \(G_{cc}(C,u_*)=-u_*D_s'(a_0)\). Moreover,
\[
D_s'(a_0)=\frac{J_s'(a_0)+e^{-a_0}}s<0
\]
because \(-J_s'(a_0)=\int_0^1x^{-2s}e^{-a_0x^{-s}}dx>J_s(a_0)=e^{-a_0}\). Thus the quadratic Taylor term has positive second derivative in \(c\). When \(s>1/2\), its \(N^{2s-2}\) size dominates the \(O(N^{-1})\) endpoint Riemann-sum error, and the root expansion gives \(u_N-u_*=B_2N^{2s-2}+o(N^{2s-2})\), with \(B_2<0\). If \(s\le1/2\), the first correction is zero and the bound in Step 3 yields \(u_N-u_*=O(N^{2s-2}+N^{-1})=o(N^{-1/2})\). The exact-centering CLT again yields the \(3/4\) trichotomy.

## Verification

The reproducible accompanying `verify.py` uses independent quadrature, an exponential-integral identity for \(s=1/2\), numerical solutions of the exact finite-\(N\) centering equation, and exact finite-subset enumeration of Bernoulli mass moments. It verifies convergence of the predicted first and exceptional second centering constants at specified exponents and thresholds, and performs a reproducible simulation of the inverse-hitting-time fluctuation scale. Run with `OPENBLAS_NUM_THREADS=1 python verify.py` in an environment with NumPy and SciPy. The completed run returned `PASS 45 independent numerical assertions; seed=20260709`. This is a finite numerical consistency check only: the infinite-\(N\) conclusion rests on the analytic steps above.

## Relationship to prior work

Müller and Šebek (arXiv:2607.08551v1, July 9, 2026) introduce the aligned weighted-threshold collector and derive the first-order linear-time limit for \(0\le s<1\), whereas this result supplies the Gaussian time fluctuations, exact finite-size centering, a nonvanishing first centering shift at \(s=1/2\), and an additional \(s=3/4\) exceptional centering boundary. Their accessible abstract, introduction, model and moment formulas were inspected; later sections could not be directly re-opened, so that limitation remains a priority risk. Chebunin and Zuyev (2020 prepublication, 2022 issue) give a functional CLT for missing mass in a *fixed infinite* urn law with regularly varying frequencies. That work provides relevant Gaussian context but does not directly imply a triangular array of *finite Zipf-normalized* probabilities observed at linear times, nor the inverse-quorum drift coefficients and cancellation threshold. Classical Karlin infinite-urn CLTs similarly concern different fixed-frequency asymptotics. A generic inverse/delta argument can explain the final Gaussian inversion once the model-specific triangular-array variance is obtained, but not the two harmonic-normalization centering thresholds.

## Limitations

No result is asserted at \(s=1\), at \(s=0\), for moving \(s_N\) or \(\theta_N\), or for unpoissonized discrete-time coupon draws. The theorem is a weak limit at fixed parameters, not a uniform Berry--Esseen bound or convergence of moments of the hitting time. The special cancellation curve is defined implicitly, not in elementary closed form. General missing-mass inverse theorems and parts of the motivating manuscript not fully accessible in this inspection remain historical-priority risks. Numerical checks cannot certify the infinite statements. No independent mathematical audit has been performed.

## References

1. S. Müller and S. Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1, first posted July 9, 2026. https://arxiv.org/abs/2607.08551
2. M. Chebunin and S. Zuyev, *Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models*, Journal of Theoretical Probability **35** (2022), 1--19, first online November 23, 2020. https://doi.org/10.1007/s10959-020-01053-6
3. S. Karlin, *Central Limit Theorems for Certain Infinite Urn Schemes*, Indiana University Mathematics Journal **17** (1968), 373--401. https://doi.org/10.1512/iumj.1968.17.17020
