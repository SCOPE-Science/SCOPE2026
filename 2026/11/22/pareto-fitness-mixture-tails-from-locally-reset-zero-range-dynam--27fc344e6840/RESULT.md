# Pareto fitness-mixture tails from locally reset zero-range dynamics

## Finding

In the independent-state mean-field stationary law of a fitness-dependent locally reset nonconserving zero-range system, the occupation of a **uniformly selected fitness level**, taken after the critical-death-rate limit, has a precise Pareto tail despite finite mean population. Fix \(0<\nu<1\), \(C>0\), \(\alpha>0\), and a permitted mutation/hopping rate \(\beta>0\) as specified below. Let \(N\) be the limiting total occupation of the level sampled uniformly from \((0,1)\). Then, with \(a=1/\nu\),

\[
\lim_{n\to\infty}n^{a}\Pr(N>n)=C^{-a}\,\mathbb E[Y^a]\in(0,\infty),
\]

where the **universal**, nondegenerate positive random variable \(Y\) is specified by its Laplace transform, for every \(u>0\),

\[
\mathbb E[e^{-uY}]=\exp\!\left[-\int_0^\infty e^{-t}\log(1+ut)\,dt\right]
=\exp[-e^{1/u}E_1(1/u)],
\]

and \(E_1(z)=\int_z^\infty e^{-s}\,ds/s\). In particular, \(\mathbb E Y=1\), \(\mathbb E Y^2=3\), \(\mathbb E Y^3=19\). Hence the **exact** Pareto coefficients are \(3/C^2\) at \(\nu=1/2\) and \(19/C^3\) at \(\nu=1/3\). More generally, \(\mathbb E[N^p]<\infty\) precisely for \(0<p<1/\nu\); moments at equality also diverge.

The conditional high-fitness law determines the coefficient. If \(N_x\) is the critical-limit occupation of level \(1-x\), then

\[
Cx^\nu N_x\ \Longrightarrow\ Y\qquad (x\downarrow0).
\]

This conditional limit is used as a lemma and also follows from the related Bessel jump-intensity cutoff [4], as explained below. The claim here is the exact **unconditional uniform-fitness survival equivalent**, its coefficient and its complete moment frontier, not the conditional compound-Poisson law or cutoff.

## Assumptions and scope

The fitness \(l\) belongs to \((0,1)\). For each fixed \(l\), take \(v\to\infty\) independent, identically distributed microstates, each with population \(n\in\{0,1,2,\ldots\}\). Conditional on a deterministic stationary mean-field density \(\rho_\zeta\), its transitions are:

\[
\begin{aligned}
 n&\to n+1&&\text{at rate }ln+A_\zeta(l)/v,\\
 n&\to n-1&&\text{at rate }(1+\zeta)n,\\
 n&\to0&&\text{at rate }r(l)=C(1-l)^\nu.
\end{aligned}
\]

Here \(\zeta>0\) is the excess death-plus-hopping rate and

\[
q(l)=(\alpha+1)(1-l)^\alpha,\qquad A_\zeta(l)=l+\beta\rho_\zeta q(l).
\]

Define

\[
I_\zeta=\int_0^1\frac{l\,dl}{\zeta+1-l+C(1-l)^\nu},\qquad
J_\zeta=\int_0^1\frac{q(l)\,dl}{\zeta+1-l+C(1-l)^\nu},\qquad
\rho_\zeta=\frac{I_\zeta}{1-\beta J_\zeta}.
\]

Require \(0<\beta<1\) and \(\beta J_0<1\); then the physical annihilation rate is \(\delta=1+\zeta-\beta>0\), the density remains finite as \(\zeta\downarrow0\), and the mean-field closure is well-defined. For each \(\zeta>0\) and each fixed \(l\in(0,1)\), the infinite-microstate occupation \(N_{\zeta,l}\) is the weak limit of the sum of the \(v\) stationary microstate occupations. **Take limits in this order:** first \(v\to\infty\), then \(\zeta\downarrow0\) for almost every fixed \(l<1\), then sample \(l\) uniformly and study \(n\to\infty\). At the strictly critical finite-system endpoint \(l=1\), absence of resetting precludes claiming a finite-system stationary law; that isolated endpoint is excluded. No interchange of the high-occupation tail and finite-system critical limits is claimed.

## Proof

**1. One microstate's pre-reset distribution.** Write \(x=1-l\), \(\Delta=x+\zeta\), \(r=Cx^\nu\), and \(c=A_\zeta(l)/v\). With resetting suppressed and initial population zero, the linear birth-death-immigration process with birth rate \(ln+c\) and death rate \((l+\Delta)n\) has negative-binomial probability generating function

\[
H_t(s)=\big[1+B_t(1-s)\big]^{-c/l},\qquad
B_t=\frac{l}{\Delta}(1-e^{-\Delta t}),\quad 0\le s\le1.
\]

This follows directly by substituting into its forward generating-function equation, with initial condition \(H_0=1\). A stationary local Poisson reset has independent backward age \(T\sim\mathrm{Exp}(r)\). Hence the one-microstate stationary generating function is \(\mathbb E H_T(s)\).

**2. Infinitely many independently reset microstates.** The generating function of their total number is \([\mathbb E H_T(s)]^v\). Expanding the expectation to first order in \(c=A_\zeta(l)/v\), and sending \(v\to\infty\), gives the legitimate probability generating function

\[
G_{\zeta,x}(s)=\exp\left[-\frac{A_\zeta(l)}{l}\int_0^\infty e^{-t}\log\left(1+\frac{l}{\Delta}(1-e^{-\Delta t/r})(1-s)\right)dt\right].\tag{1}
\]

Existence follows also by convergence of probability generating functions at all \(0\le s\le1\). This is a full distributional formula, not merely a mean-field mean.

**3. Critical parameter limit.** Because \(0<\nu<1\), the function \((x+Cx^\nu)^{-1}\) is integrable near zero; moreover \(q(1-x)=O(x^\alpha)\). Dominated convergence gives \(\rho_\zeta\to\rho_0<\infty\). At each fixed \(0<x<1\), (1) therefore converges to a proper generating function \(G_x\), defining \(N_x\). The uniform-fitness mixture \(N=N_X\), \(X\sim\mathrm{Uniform}(0,1)\), is then proper by integration of generating functions. Its mean is \(\int_0^1 A_0(1-x)/(x+Cx^\nu)\,dx<\infty\).

**4. Universal conditional edge law.** In (1) at \(\zeta=0\), choose \(s=e^{-u r}\). For every fixed \(t,u>0\),

\[
\frac{l}{x}(1-e^{-xt/r})(1-e^{-ur})\longrightarrow ut
\]

because \(r=Cx^\nu\to0\), \(x/r\to0\), and \(l\to1\). The expression is bounded above by \(ut\). Also \(A_0(l)/l\to1\) because \(q(l)=O(x^\alpha)\). Dominated convergence in (1) proves \(rN_x\Rightarrow Y\) with the advertised Laplace transform. Integration by parts gives \(\int_0^\infty e^{-t}\log(1+ut)\,dt=e^{1/u}E_1(1/u)\). Positivity and nondegeneracy follow from the Laplace formula and its first two derivatives at zero. Its factorial-cumulant limit gives ordinary cumulants \(\kappa_k(Y)=k!(k-1)!\) for all integers \(k\ge1\), proving the three displayed moments.

**5. Uniform moment domination.** For any integer \(k\ge1\), the \(k\)-th factorial cumulant of the nonnegative integer \(N_x\), obtained by differentiating \(\log G_x\), is

\[
\kappa_k^{(F)}(N_x)=\frac{A_0(l)}{l}(k-1)!\int_0^\infty e^{-t}\left[\frac l x(1-e^{-xt/r})\right]^kdt.
\]

Since the bracket is bounded by \(lt/r\),

\[
r^k\kappa_k^{(F)}(N_x)\le A_0(l)l^{k-1}k!(k-1)!\le M'_k<\infty,
\]

uniformly over \(0<x<1\). Because factorial moments are nonnegative-coefficient Bell polynomials in the nonnegative factorial cumulants, and ordinary moments are nonnegative-coefficient Stirling combinations of factorial moments, the boundedness of \(r\le C\) implies, for every integer \(k\),

\[
\sup_{0<x<1}\mathbb E[(Cx^\nu N_x)^k]<\infty.\tag{2}
\]

**6. Uniform-fitness Pareto tail.** Fix \(a=1/\nu>1\) and choose an integer \(k>a\). With the change of variable \(y=nCx^\nu\),

\[
n^a\Pr(N>n)=C^{-a}a\int_0^{nC}y^{a-1}\Pr\big((y/n)N_{(y/(nC))^a}>y\big)\,dy.
\]

At every fixed \(y>0\), step 4 gives weak convergence of the variable inside the probability to \(Y\). The limiting law has no atoms: its Lévy density, obtained by writing the logarithm as a positive Laplace integral, is \(2K_1(2\sqrt z)/\sqrt z\) on \(z>0\), and is infinite near zero (an infinitely divisible distribution with infinite Lévy mass has no atoms). Independently, discontinuities of a distribution function are at most countable, which would suffice for the integration. By (2), the integrand is dominated by \(y^{a-1}\min(1,M_k/y^k)\), integrable on \((0,\infty)\). Dominated convergence and the layer-cake identity give

\[
\lim_{n\to\infty}n^a\Pr(N>n)=C^{-a}a\int_0^\infty y^{a-1}\Pr(Y>y)dy=C^{-a}\mathbb E[Y^a].
\]

The coefficient is finite by the moment bound and strictly positive because \(\mathbb EY=1\). The standard layer-cake criterion applied to this exact regularly varying survival tail proves precisely the asserted moment threshold.

## Verification

A standalone Python script `checker.py` checks the integral and exponential-integral representations of the universal Laplace transform, compares the model's exact finite-scale Laplace transform to the scaling limit, checks positivity of the self-consistent density in one admissible example, and reconstructs integer-moment anchors from cumulants. Run with `python checker.py` using Python 3 and `mpmath`. The script's 17 assertions passed on the final source content. These finite numerical checks are not used as an infinite-tail proof; the proof is the exact generating function and dominated-convergence argument above.

## Relationship to prior work

Grange (2023 preprint; 2024 journal article) specifies the fitness-dependent local-reset zero-range dynamics, derives its mean-field single-state generating-function evolution, and classifies the **mean-density** condensation threshold at \(\nu=1\). Grange (2019 preprint; 2020 journal article) studies global resetting. The co-occupation result [3] on the same local-reset model establishes a distinct \(\nu=1/2\) threshold for the integrated **within-site** ordered-pair intensity. This is not the factorial moment of the total occupation across all sites, and a second-moment asymptotic does not imply a regularly varying survival law.

The closely related Bessel-cutoff record [4] gives the exact fixed-level compound-Poisson law and the limit \(n\Lambda_n\to g(s)=2\sqrt{s}K_1(2\sqrt{s})\) when \(nr\to s>0\). This implies the conditional limit used here. In its one-founder integral for \(\Lambda_n\), dropping the resetting survival factor \(e^{-rt}\) and integrating the geometric mass in time gives \(n\Lambda_n\le (A_0(l)/l)l^n\) at criticality. Indeed, the derivative of the geometric ratio \(b_t=l(1-e^{-xt})/(1-le^{-xt})\) is \(l\) times the prefactor of \(b_t^{n-1}\) in the one-founder mass. The rescaled Laplace exponent therefore has contribution \(O(\varepsilon)\) from \(nr\le\varepsilon\), using \(1-e^{-urn}\le urn\), and contribution \(O(M^{-1})\) from \(nr>M\), using \(r\sum_n n\Lambda_n=rA_0(l)/(x+r)\). On compact subintervals of \((0,\infty)\), the joint cutoff limit gives a Riemann sum with density \(g(s)/s\), the same Lévy density as that of \(Y\). Equivalently, \(\int_0^\infty(1-e^{-us})g(s)\,ds/s=\int_0^\infty e^{-t}\log(1+ut)\,dt\). Step 4 above gives a direct proof without invoking this cutoff result. The two records have the same date; this overlap does not establish temporal priority.

The conditional cutoff concerns individual jump sizes at high fitness and does not give an unconditional survival equivalent for the sum sampled uniformly over fitness levels. The mixed-tail argument uses uniform bounds on **full occupations** and identifies the amplitude through the full limiting law. Neither the cutoff statement alone nor a collection of critical moment thresholds asserts this survival asymptotic.

## Limitations

The result is a sequential, infinite-microstate, mean-field critical-limit theorem, not a statement at a finite system's exactly critical unreset maximum-fitness site. It assumes uniform sampling of fitness **levels**, not size-biased sampling of individual microstates or particles, and uses \(q(l)=(\alpha+1)(1-l)^\alpha\). It does not establish finite-system scaling with microstate count, an explicit elementary constant for every noninteger \(1/\nu\), or any assertion about models with common (global) resets. Historical priority remains limited by the accessible literature.

## References

1. P. Grange, *Local resetting in non-conserving zero-range processes with extensive rates*, arXiv:2311.12414, first posted 2023-11-21, Journal of Physics Communications 8 (2024) 045004. https://arxiv.org/abs/2311.12414
2. P. Grange, *Non-conserving zero-range processes with extensive rates under resetting*, arXiv:1910.05991, first posted 2019-10-14, Journal of Physics Communications 4 (2020) 045006. https://arxiv.org/abs/1910.05991
3. *A hidden co-occupation threshold below fitness condensation*, dated 2026-11-08, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-a-hidden-co-occupation-threshold-below-fitness-condensation--b88c55090541 .
4. *A universal Bessel cutoff for immigrant clans under fitness-dependent local clearing*, dated 2026-11-22, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-universal-bessel-cutoff-for-immigrant-clans-under-fitness-depe--ea7ce4494856 .
