# A sharp coarse-sampling resilience law for scalar saddle-to-sink flows

## Finding

For a scalar flow with a repelling basin boundary and an attracting equilibrium, the maximum bounded disturbance per sample approaches the distance between these equilibria at a sharp exponential rate. Normalizing the equilibria to \(0\) and \(1\), let \(\Phi_h\) denote the exact time-\(h\) map and \(\mu_h\) the largest uniform absolute kick amplitude for which every kicked orbit from \(1\) stays in a compact subset of its basin. Put

\[
\lambda=f'(0)>0,\qquad \nu=-f'(1)>0,\qquad
\kappa=\frac{\lambda\nu}{\lambda+\nu}.
\]

For any reference \(c\in(0,1)\), define the increasing transit-time coordinate and its two finite endpoint constants by

\[
T(x)=\int_c^x\frac{du}{f(u)},\qquad
A=\lim_{x\downarrow0}\left(T(x)-\frac{\log x}{\lambda}\right),\qquad
B=\lim_{x\uparrow1}\left(T(x)+\frac{\log(1-x)}{\nu}\right).
\]

The difference \(B-A\) is independent of \(c\). Set

\[
C_f=\frac{\lambda+\nu}{\lambda^{\lambda/(\lambda+\nu)}\nu^{\nu/(\lambda+\nu)}}
\exp\!\left(\kappa(B-A)\right).
\]

**Theorem.** Under the assumptions below,

\[
\boxed{\mu_h=1-C_f e^{-\kappa h}+o(e^{-\kappa h})\quad(h\to\infty).}
\]

If \(x_h\in(0,1)\) is *any* maximizer of \(\Phi_h(x)-x\), and \(y_h=\Phi_h(x_h)\), then simultaneously

\[
\boxed{\quad x_h\sim \frac{\nu}{\lambda+\nu}C_f e^{-\kappa h},\qquad
1-y_h\sim \frac{\lambda}{\lambda+\nu}C_f e^{-\kappa h}.\quad}
\]

Thus the exponential rate is the harmonic combination of the unstable and stable linearization rates, while the exact prefactor also remembers the nonlinear transit time across the intervening basin.

## Assumptions and scope

Assume \(f:\mathbb R\to\mathbb R\) is \(C^2\) with a forward-complete flow, \(f(0)=f(1)=0\), \(f>0\) on \((0,1)\), \(f<0\) on \((1,\infty)\), \(f'(0)=\lambda>0\), \(f'(1)=-\nu<0\), and \(f(x)\to-\infty\) as \(x\to+\infty\). Assume the basin of \(\{1\}\) is \((0,\infty)\); it follows from the stated sign conditions for positive initial data, together with exclusion of negative initial data from the basin (for instance from forward uniqueness and the fixed state \(0\)).

A *kicked orbit* is \(X_0=1\), \(X_{n+1}=\Phi_h(X_n)+e_n\) with arbitrary real \(e_n\) satisfying \(|e_n|<\varepsilon\). We define \(\mu_h\) as the supremum of \(\varepsilon\) for which all such orbits stay in one common compact subset of \((0,\infty)\). Sampling time \(h\) varies, but \(f\) is fixed. This is an exact-flow, absolute-displacement result, not a numerical Euler-step or stochastic escape probability assertion. At the supremum endpoint there may be non-strictly confined trajectories; the formula concerns the supremum.

## Proof

**1. Exact finite-sampling reduction.** Scalar uniqueness makes \(\Phi_h\) increasing. By the one-sided reachability characterization of Yu and Wang, Proposition 3.12 (or directly using the barriers described next),

\[
\mu_h=\max_{0\le x\le1}(\Phi_h(x)-x)=:\Delta_h.
\]

Indeed \(\Delta_h>0\), with interior maximizers. For \(\varepsilon<\Delta_h\) choose \(c_\varepsilon\in(0,1)\) where \(\Phi_h(c_\varepsilon)-c_\varepsilon>\varepsilon\). Then the order-preserving perturbed maps leave \([c_\varepsilon,\infty)\) forward invariant. As \(f\to-\infty\) on the positive half-line, an upper barrier \(M\) with \(\Phi_h(M)+\varepsilon<M\) exists, making \([c_\varepsilon,M]\) uniformly invariant for all kicks. Conversely, for any \(\varepsilon>\Delta_h\), a constant negative kick of size strictly between \(\Delta_h\) and \(\varepsilon\) decreases states by a fixed amount on \((0,1]\), crossing \(0\) in finitely many steps. This proves the exact formula without assuming the maximizing point is unique.

**2. Both endpoints control a large sample.** As \(h\to\infty\), set \(u_h=\Phi_{-h/2}(c)\) for a fixed \(c\in(0,1)\). Backward flow between the equilibria exists for all times and tends to \(0\), whereas \(\Phi_h(u_h)=\Phi_{h/2}(c)\to1\). Therefore \(\Delta_h\ge\Phi_{h/2}(c)-\Phi_{-h/2}(c)\to1\). Since every \(0\le x\le y=\Phi_h(x)\le1\) obeys \(y-x\le1\), one has \(\Delta_h\to1\). At every interior maximizer \(x_h\) we consequently have \(x_h\to0\) and \(y_h:=\Phi_h(x_h)\to1\).

**3. Exact stationary-balance relation.** The variational equation of an autonomous scalar flow gives

\[
\Phi_h'(x)=\frac{f(\Phi_h(x))}{f(x)}\quad(0<x<1).
\]

At any interior maximizer, \(\Phi_h'(x_h)-1=0\), so \(f(y_h)=f(x_h)\). Endpoint linearization now yields

\[
\lambda x_h(1+o(1))=\nu(1-y_h)(1+o(1)).
\]

Thus if \(z_h=1-y_h\), then \(z_h/x_h\to\lambda/\nu\).

**4. Exact transit-time matching and coefficient.** By definition, \(h=T(y_h)-T(x_h)\). The \(C^2\) endpoint expansions of \(f\) imply convergent renormalized travel-time limits, giving

\[
T(x_h)=\frac{\log x_h}{\lambda}+A+o(1),\qquad
T(y_h)=-\frac{\log z_h}{\nu}+B+o(1).
\]

Therefore

\[
\frac{\log x_h}{\lambda}+\frac{\log z_h}{\nu}=B-A-h+o(1).
\]

Insert \(z_h/x_h\to\lambda/\nu\), then exponentiate and solve to obtain

\[
x_h=\left(\frac{\nu}{\lambda}\right)^{\lambda/(\lambda+\nu)}
 e^{\kappa(B-A)}e^{-\kappa h}(1+o(1)),
\]

\[
z_h=\left(\frac{\lambda}{\nu}\right)^{\nu/(\lambda+\nu)}
 e^{\kappa(B-A)}e^{-\kappa h}(1+o(1)).
\]

Their sum is \(1-\Delta_h\); elementary factorization of the two constants yields \(C_f\), completing every assertion for all maximizers. No finite computation is used to infer this limit.

## Verification

For the logistic vector field \(f(x)=x(1-x)\), \(\lambda=\nu=1\), \(A=B=0\), and \(\mu_h=\tanh(h/4)\). Consequently \(1-\mu_h\sim2e^{-h/2}\), exactly as predicted.

For the cubic vector field \(f(x)=x(1-x^2)\), \(\lambda=1\), \(\nu=2\), and \(B-A=-\tfrac12\log2\). Its exact sampled intensity (already derived by Yu and Wang) gives \(1-\mu_h\sim\tfrac32e^{-2h/3}\), again matching the theorem. These examples check the prefactor and rate but are not the proof for general \(f\).

The coefficient genuinely depends on nonlinear transit dynamics: in the family \(f_\alpha(x)=x(1-x)[1+\alpha x(1-x)]\) with \(-4<\alpha\le0\) on the positive half-line, the endpoint derivatives remain \(\lambda=\nu=1\), but

\[
B-A=-\alpha\int_0^1\frac{du}{1+\alpha u(1-u)},\qquad
C_{f_\alpha}=2\exp\!\left[-\frac{\alpha}{2}\int_0^1\frac{du}{1+\alpha u(1-u)}\right].
\]

A harmless \(C^2\) forward-complete extension can be chosen to the negative half-line. For \(\alpha<0\), the prefactor is strictly larger than its logistic value although both endpoint eigenvalues are unchanged. The standalone `CHECK.py` reproduces the logistic/cubic exact constants and independently checks the modified-flow large-\(h\) asymptotic numerically; its results are supplementary, not a substitute for the analytic proof.

## Relationship to prior work

Yu and Wang [1, Proposition 3.12] prove the exact scalar maximum-displacement identity; their primary focus is the small-sampling limit \(h\downarrow0\), including the higher-order correction for smooth drifts, and Section 6.1 gives the full exact cubic example. This work **takes that exact maximum identity as prior** and establishes a different general asymptotic regime: \(h\to\infty\), including a universal harmonic-combination decay exponent, the nonlinear transit prefactor and both optimizing endpoint positions. The cubic exponent and coefficient are not claimed as independently new since they follow from [1, Eq. (6.2)]. Meyer and McGehee [2] develop the continuous-control definition rather than this coarse sampled-flow asymptotic.

## Limitations

The theorem requires two hyperbolic endpoints, one-dimensional monotone flow, a one-sided escape basin and sufficient upper confinement. It says nothing about nonhyperbolic fold boundaries, multistable interior chains, multidimensional flows, continuous-time disturbance intensities at large \(h\), or stochastic almost-sure exit. The historical originality comparison is limited to accessible literature; an equivalent asymptotic in specialized scalar-flow or reachability literature could reduce priority, even though no such covering statement was found in the inspected sources.

## References

1. Jiguang Yu and Louis Shuo Wang, *From Flows to Maps: Sampling Laws for Attractor Intensity and Bounded-Noise Escape*, arXiv:2608.02933 (first posted 2026-08-03), https://arxiv.org/abs/2608.02933. Particularly Proposition 3.12, Section 6.1, Eq. (6.2).
2. Katherine J. Meyer and Richard P. McGehee, *Intensity—A Metric Approach to Quantifying Attractor Robustness in ODEs*, SIAM Journal on Applied Dynamical Systems **21** (2022), 960–981, DOI:10.1137/20M138689X; open preprint https://arxiv.org/abs/2012.10786.
