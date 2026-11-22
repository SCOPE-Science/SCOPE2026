# Critical Poisson–Gaussian arrivals and logarithmic survivor fluctuations in mortal Brownian search

## Finding

Fix a source–target distance \(d>0\), diffusivity \(D>0\), and a real critical-window parameter \(c\). Release \(N\) independent Brownian searchers together at distance \(d\) from an absorbing origin. Each is independently killed at rate \(\mu_N\), with
\[
q_N=d\sqrt{\mu_N/D}=\log N+c>0,\qquad m=e^{-c}.
\]
For a successful searcher, let \(u\) be its arrival time divided by \(t_0=d^2/D\), and mark that arrival by
\[
v=2q_N^{3/2}\left(u-\frac1{2q_N}\right).
\]
Let \(\Xi_N\) be the point measure of **all** such successful arrival marks, omitting searchers killed before reaching the target. Denote by \(\varphi\) and \(\Phi\) the standard normal density and distribution function. Then the following constitute one joint critical-window theorem.

**The complete arrival cloud.** As \(N\to\infty\), \(\Xi_N\) converges in total variation, as a probability law on finite point measures on \(\mathbb R\), to a Poisson point process of intensity \(m\varphi(v)\,dv\). In particular the total number of successes tends to \(\operatorname{Poisson}(m)\); the probability of no successful arrival tends to \(e^{-m}\). The finite-population total-variation convergence has the **sharp order** \((\log N)^{-1/2}\). More precisely, if \(\nu_q\) is the law of one standardized mark conditioned on a successful arrival, then
\[
\delta_q:=d_{\rm TV}(\nu_q,\mathcal N(0,1))
=\frac{C_*}{\sqrt q}+O(q^{-1}),\qquad
C_*=\frac{1+4e^{-3/2}}{2\sqrt{2\pi}}=0.3775032500\ldots,
\]
and, with \(\Pi_m\) denoting the Poisson point process just defined,
\[
me^{-m}\delta_{q_N}-O_m(N^{-1})
\ \le\ d_{\rm TV}\bigl(\mathcal L(\Xi_N),\mathcal L(\Pi_m)\bigr)
\ \le\ m\delta_{q_N}+\frac{m^2}{N}.
\]
Here \(O_m\) refers to a constant depending only on the fixed parameter \(m>0\). Thus the process-level error really has order \((\log N)^{-1/2}\), rather than merely a stated upper bound.

**First success and the living population.** Let \(V_N=\min\Xi_N\), with \(V_N=+\infty\) if \(\Xi_N\) is empty; let \(T_N\) be the physical time of the first successful arrival. For every real \(z\),
\[
\Pr(V_N>z)\longrightarrow e^{-m\Phi(z)},\qquad
\Pr(T_N=+\infty)\longrightarrow e^{-m}.
\]
Conditioning on at least one success, \(V_N\) tends to a finite random variable \(V_*\) with
\[
\Pr(V_*>z)=\frac{e^{-m\Phi(z)}-e^{-m}}{1-e^{-m}}.
\]
Let \(A_N\) be the number of **other searchers still alive and diffusing immediately before** the first successful arrival. It is defined on \(\{T_N<\infty\}\). With \(\log(A_N\vee1)\) used for finite-population rigor, the joint limit, conditional on success, is
\[
\boxed{\quad\left(V_N,\frac{2}{\sqrt{q_N}}\left[\log(A_N\vee1)-\log N+\frac{q_N}{2}\right]\right)
\ \Longrightarrow\ (V_*,-V_*)\quad}.
\]
Moreover \(\Pr(A_N=0\mid T_N<\infty)\to0\). Thus the random arrival-time mark is reproduced with its sign reversed by the **logarithmic survivor count**. The unscaled living population is of order \(\sqrt N\), multiplied by a nontrivial factor exponentially sensitive to \(\sqrt{\log N}\) times the first-arrival mark; it does **not** have a deterministic multiplicative limit on the \(\sqrt N\) scale.

## Assumptions and scope

For each sufficiently large integer \(N\), the particles solve \(X_i(t)=d+\sqrt{2D}\,B_i(t)\) until first hitting zero, with independent standard Brownian motions \(B_i\). Each particle has an independent exponential killing clock of rate \(\mu_N=Dq_N^2/d^2\). The clocks, Brownian paths, and initial particles are mutually independent. No restarting, immigration, interactions, boundaries other than the absorbing origin, or spatially varying killing are assumed. An unsuccessful searcher does not contribute an arrival point. No searcher is counted alive after it has been killed or has reached the origin. All limits hold for fixed finite real \(c\) (equivalently fixed \(m=e^{-c}\)); no uniformity over moving \(c\) is asserted. The population scale and diffusion parameters are deterministic.

The point-process total variation is between probability measures on the space of finite counting measures, *not* a pathwise coupling of the Brownian motions. The first-arrival/survivor statement is conditional on the event \(T_N<\infty\), whose limiting probability is \(1-e^{-m}>0\).

## Proof

**1. The single-particle defective law.** The standard Brownian first-hitting density and independent killing give the dimensionless defective density
\[
f_q(u)=\frac{1}{2\sqrt\pi\,u^{3/2}}\exp\left(-\frac{1}{4u}-q^2u\right),\qquad u>0.
\]
Its integral is \(p_q=e^{-q}\), by the Lévy first-passage Laplace transform. Thus a particle succeeds with probability \(p_q\), and the successful time conditional on success has density \(f_q(u)/p_q\). Its conditional mean and variance are respectively \(1/(2q)\) and \(1/(4q^3)\), as follows by differentiating the normalized Laplace transform \(\exp(q-\sqrt{q^2+s})\). The finite-parameter hitting density, success probability, and first two conditional moments are established inputs, not claimed new.

After the change of variable \(v=2q^{3/2}(u-1/(2q))\), write \(h=1+v/\sqrt q\); the exact conditional mark density is
\[
g_q(v)=\frac{\mathbf 1_{\{v>-\sqrt q\}}}{\sqrt{2\pi}\,h^{3/2}}
\exp\left(-\frac{v^2}{2h}\right).
\tag{1}
\]
The logarithm of its ratio to the normal density on this support is exactly
\[
\log\frac{g_q(v)}{\varphi(v)}=-\frac32\log(1+v/\sqrt q)
+\frac{v^3}{2\sqrt q(1+v/\sqrt q)}.
\tag{2}
\]

**2. Sharp conditional normal approximation.** For \(\lvert v\rvert\le q^{1/12}\), a Taylor expansion of (2) with uniform remainder gives
\[
g_q(v)=\varphi(v)\left[1+\frac{v^3-3v}{2\sqrt q}
+O\left(\frac{v^2+v^4+v^6}{q}\right)\right].
\tag{3}
\]
This expansion can be integrated with a controlled tail. In fact the conditional moment-generating function of the marked variable is exactly
\[
M_q(t)=\exp\left(q-\sqrt{q^2-2tq^{3/2}}-t\sqrt q\right),\qquad t<\sqrt q/2.
\]
For \(\lvert t\rvert\le\sqrt q/4\), the identity
\[
\log M_q(t)=\frac{2t^2}{(1+\sqrt{1-2t/\sqrt q})^2}\le t^2
\]
implies by Chernoff's inequality that \(\Pr_{\nu_q}(|v|>q^{1/12})\le2e^{-q^{1/6}/4}\) for sufficiently large \(q\). The same region has exponentially small normal tail. Thus, integrating (3) against the Gaussian density and using finite Gaussian moments, we obtain the **integrated** first-order expansion
\[
\int_{\mathbb R}\left|g_q(v)-\varphi(v)-\frac{v^3-3v}{2\sqrt q}\varphi(v)\right|dv=O(q^{-1}).
\tag{4}
\]
(The same bound applies to the normal mass below the lower support endpoint.) By \(\bigl||a+b|-|a|\bigr|\le|b|\), (4) yields
\[
\delta_q=\frac{1}{4\sqrt q}\mathbb E|Z^3-3Z|+O(q^{-1}),\qquad Z\sim\mathcal N(0,1).
\]
Splitting the absolute-value Gaussian integral at \(0\) and \(\sqrt3\) gives \(\mathbb E|Z^3-3Z|=2\varphi(0)(1+4e^{-3/2})\), proving the explicit constant \(C_*\) in the finding.

**3. The whole marked arrival process and its optimal rate.** Put \(q_N=\log N+c\), so \(p_{q_N}=m/N\) exactly. Each of the \(N\) independent particles contributes either no point (probability \(1-m/N\)) or one mark with law \(\nu_{q_N}\) (probability \(m/N\)). The number of points is \(\operatorname{Bin}(N,m/N)\), and conditional on the number their marks are independent \(\nu_{q_N}\) variables. Couple these marks optimally with independent standard normal marks. The probability of at least one mismatch is at most \(m\delta_{q_N}\). Le Cam's elementary binomial-to-Poisson coupling contributes at most \(m^2/N\) more in total variation, proving the upper bound and process convergence.

For the matching lower bound, define \(E_q=\{v:g_q(v)>\varphi(v)\}\), so \(\nu_q(E_q)-\Phi(E_q)=\delta_q\). Consider the event that a counting measure has **exactly one point, lying in \(E_q\)**. Its probabilities under \(\Xi_N\) and \(\Pi_m\) are respectively \(m(1-m/N)^{N-1}\nu_q(E_q)\) and \(me^{-m}\Phi(E_q)\). Their absolute difference is at least \(me^{-m}\delta_q-O_m(N^{-1})\), establishing the lower bound. This is why the \(q^{-1/2}\) order cannot be improved for the *complete process*.

**4. The first successful arrival.** Let \(H_q(z)=\int_{-\infty}^{z}g_q(v)dv\). Since each particle has a mark at or below \(z\) with probability \((m/N)H_q(z)\),
\[
\Pr(V_N>z)=[1-(m/N)H_{q_N}(z)]^N.
\]
Equation (4) gives \(H_{q_N}(z)\to\Phi(z)\), and the displayed formula tends to \(e^{-m\Phi(z)}\). The probability of no point is exactly \((1-m/N)^N\to e^{-m}\). Subtracting this no-point mass and dividing by \(1-(1-m/N)^N\) proves the asserted proper conditional law \(V_*\).

**5. The living population is slaved to the first arrival.** Suppose the first successful arrival occurs at dimensionless time \(u>0\), from one identified particle. All other \(N-1\) particles are conditionally independent given that they have no successful arrival by \(u\). For each of them, the probability of still being alive and diffusing at that time, conditional on no previous successful arrival, is
\[
a_q(u)=\frac{e^{-q^2u}\,\operatorname{erf}(1/(2\sqrt u))}{1-F_q(u)},
\qquad F_q(u)=\int_0^u f_q(s)ds.
\tag{5}
\]
Consequently \(A_N\), conditional on the first successful arrival at \(u\), has distribution \(\operatorname{Bin}(N-1,a_{q_N}(u))\). Formula (5) is an exact finite-population conditioning identity; it is not asserted as a novel identity.

On the event \(V_N=v\) with \(|v|\le M\),
\[
u=\frac1{2q_N}+\frac{v}{2q_N^{3/2}},\qquad
q_N^2u=\frac{q_N}{2}+\frac{v\sqrt{q_N}}2.
\]
Uniformly over any fixed compact set of \(v\), one has \(\operatorname{erf}(1/(2\sqrt u))\to1\) and \(0\le F_{q_N}(u)\le m/N\). Thus the binomial conditional mean \(M_N(u)=(N-1)a_{q_N}(u)\) obeys
\[
\log M_N(u)=\log N-\frac{q_N}{2}-\frac{v\sqrt{q_N}}{2}+o(1).
\tag{6}
\]
Since \(q_N=\log N+c\), this mean grows uniformly to infinity on every compact \(v\)-window. Conditional Chebyshev gives \(\Pr(|A_N/M_N(u)-1|>\varepsilon\mid u)\le [\varepsilon^2M_N(u)]^{-1}\), so \(\log(A_N\vee1)=\log M_N(u)+o_{\Pr}(1)\) there. The success-conditioned laws of \(V_N\) are tight by Step 4; let \(M\) increase to remove the compact-window restriction. Substituting (6) yields
\[
\frac2{\sqrt{q_N}}\left[\log(A_N\vee1)-\log N+\frac{q_N}{2}\right]+V_N\xrightarrow{\Pr}0
\]
conditional on successful arrival, and also \(\Pr(A_N=0\mid T_N<\infty)\to0\). Joint convergence to \((V_*,-V_*)\) follows by Slutsky's theorem. This completes the proof.

## Verification

Run the standalone file `verify_critical.py` with Python 3 and SciPy installed. It independently evaluates the exact conditional-mark density and cumulative distribution by numerical quadrature, checks normalization and first two moments, compares the moment-generating function against the transform, tests the sharp \(C_*\) total-variation prefactor at multiple large \(q\), tests finite-\(N\) critical survival/failure probabilities, and checks exact conditional survivor-count means against their logarithmic scaling. It prints `PASS: 239 deterministic consistency checks (not an infinite proof)` when its assertions succeed. A passing numerical checker corroborates finite identities and asymptotic scales; the limit theorem and sharp rate follow from the analytic argument above, not the finite checks.

## Relationship to prior work

Meerson and Redner (2015) derive the *same one-dimensional model's* one-particle defective hitting density, eventual success probability, conditional first two moments, and \(N\)-particle success probability. Those results, and the mortality/redundancy threshold itself, are **not new**; the present result uses them. Their exact finite-population formulas are strong inputs from which joint asymptotics may be derived, but the examined article does not state the marked critical-point-process limit with a sharp total-variation rate or the joint logarithmic-survivor law.

Paquin-Lefebvre, Delbreil and Holcman (2026) give general first-arrival, survival-population and first-exit formulas, and a fixed-killing large-population theory. Their finite-\(N\) survivor distribution (their Section 2.3, Eq. 2.25) is broader than the exact conditioning identity (5), which is therefore **not claimed as new**. Their stated large-population regime holds killing parameters fixed and explicitly warns that high-killing and high-population limits need not commute. The result here resolves a specific jointly diverging, critically balanced one-dimensional window with a new nondegenerate logarithmic survivor statistic.

Skorski (2023) explicitly proves total-variation normal approximation at order \(O(q^{-1/2})\) for standardized inverse-Gaussian laws. Neither that rate *alone* nor asymptotic normality is claimed as new here: the additional conclusions are the explicit leading coefficient in this physical normalization, process-level two-sided total-variation comparison, and the coupled logarithmic-survivor limit. A related published study of Poisson-*recruited* mortal searchers gives different first-arrival limits: searchers continually arrive, so it is not a finite initial population with a positive no-success atom.

## Limitations

The theorem concerns independent Brownian motion with spatially uniform exponential mortality and a perfectly absorbing point on a half-line, all particles started simultaneously. It does not apply directly to a bounded two-dimensional domain, a moving target, non-exponential lifetime laws, heterogeneous killing, simultaneous collective mortality shocks, recruitment, or correlated particle trajectories. It gives a distributional law and a process-level total-variation **order**, not the exact leading process-level TV constant. The explicit single-mark TV constant relies on normalizing by the *conditional* mean and variance. Although the general inputs and exact finite-population identities are classical, a previously unstated equivalent critical-window asymptotic could exist in earlier first-passage or inverse-Gaussian literature. No independent originality or correctness audit has been performed.

## References

1. F. Paquin-Lefebvre, É. Delbreil and D. Holcman, *From Distribution of Extremes With Degradation to the Stress Redundancy Principle*, arXiv:2611.14375v1, submitted 10 November 2026. https://arxiv.org/html/2611.14375v1
2. B. Meerson and S. Redner, *Mortality, Redundancy, and Diversity in Stochastic Search*, Physical Review Letters **114** (2015), 198101. https://doi.org/10.1103/PhysRevLett.114.198101 ; lawful full text: https://sites.santafe.edu/~redner/pubs/pdf/PhysRevLett.114.198101.pdf
3. M. Skorski, *Normality of Inverse Gaussian*, mathematical note, 3 December 2023. https://skorski.info/2023/12/03/normality-of-inverse-gaussian/
4. *Sharp mortality–recruitment threshold for first arrivals of independent Brownian searchers*, published-finding corpus, 18 October 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-sharp-mortality-recruitment-threshold-for-first-arrivals-of-inde--2f684bcae431/RESULT.md
