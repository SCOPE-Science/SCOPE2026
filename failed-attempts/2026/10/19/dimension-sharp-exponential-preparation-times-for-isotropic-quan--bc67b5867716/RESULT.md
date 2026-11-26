# Dimension-sharp exponential preparation times for isotropic quantum-state diffusion

## Finding
Fix an integer \(n\ge2\). For the isotropic Fubini–Study Brownian motion on \(\mathbb{CP}^{n-1}\), started from a ray orthogonal to a prescribed target ray, let \(T_b\) be the first time the target fidelity reaches \(b\in(0,1)\). If the geometric diffusion generator is \(D\Delta_{\mathrm{FS}}\), put \(\tau_b=4DT_b\), \(m_n(b)=\mathbb E[\tau_b]\), and \(Y_b=\tau_b/m_n(b)\). Define the harmonic-number coefficient
\[
\alpha_n=\frac{H_{n-1}}{n-1},\qquad H_{n-1}=\sum_{j=1}^{n-1}\frac1j.
\]
For every \(b\in(0,1)\) and \(\theta>0\) satisfying \(\theta\alpha_n<m_n(b)\),
\[
0<\frac1{1+\theta}-\mathbb E[e^{-\theta Y_b}]
\le
\frac{\alpha_n\theta^2}{m_n(b)(1+\theta)^2[1-\alpha_n\theta/m_n(b)]}.
\tag{1}
\]
At \(\theta=0\) both sides of the difference are zero. The coefficient is *dimension-sharp* in the high-fidelity limit: for every fixed \(\theta>0\),
\[
\lim_{b\uparrow1}m_n(b)\left(\frac1{1+\theta}-\mathbb E[e^{-\theta Y_b}]\right)
=\frac{H_{n-1}}{n-1}\frac{\theta^2}{(1+\theta)^2}.
\tag{2}
\]
Thus \(Y_b\) converges in distribution to a unit exponential random variable, with an explicit, sharp first correction in the Laplace transform. Its coefficient of variation obeys the strict finite-threshold inequality \(\operatorname{CV}^2(\tau_b)<1\), with exact asymptotic deficit
\[
1-\operatorname{CV}^2(\tau_b)\sim\frac{2H_{n-1}}{(n-1)m_n(b)}.
\tag{3}
\]
Writing \(\varepsilon=1-b\), this is \(2/\log(1/\varepsilon)\) for \(n=2\), and \(2(n-2)H_{n-1}\varepsilon^{n-2}\) for every integer \(n\ge3\). These asymptotics hold with \(n\) fixed.

## Assumptions and scope
The fidelity coordinate \(X_t=|\langle\psi_t,\eta\rangle|^2\) has physical-time generator
\[
4D\left[x(1-x)\partial_x^2+(1-nx)\partial_x\right].
\]
Equivalently, after multiplication of time by \(4D\), its generator is
\[
\mathscr L=x(1-x)\partial_x^2+(1-nx)\partial_x.
\]
The initial fidelity is exactly \(X_0=0\); the first upward hitting time of \(b\) is almost surely finite. The boundary at zero is the canonical regular/entrance boundary inherited from Brownian motion on projective space, not an added sticky or killing boundary. All statements assume isotropic *Brownian-limit* dynamics with no drift, resetting, Hamiltonian forcing, or measurement backaction; the result does not extend automatically to a finite-step isotropic random walk or a Lindblad unraveling.

The known mean first-passage formula, written in our dimensionless normalization, is
\[
m_n(b)=\frac1{n-1}\left[\log\frac1{1-b}+\sum_{j=1}^{n-2}\frac{(1-b)^{-j}-1}{j}\right],
\tag{4}
\]
where the sum is empty when \(n=2\). Equation (4), the radial generator, spectral formulas, and the existence of an exponential *long-time tail at fixed threshold* are established ingredients rather than originality claims.

## Proof
**1. Positive inverse of the backward generator.** Put \(w(y)=(1-y)^{n-2}\). For each continuous function \(g\) on a compact interval \([0,b]\), define
\[
(Kg)(x)=\int_0^x\frac{\displaystyle\int_0^u w(y)g(y)\,dy}{u(1-u)^{n-1}}\,du,
\qquad 0\le x\le b.
\tag{5}
\]
The apparent singularity at \(u=0\) is removable. Direct differentiation gives \(\mathscr L(Kg)=g\), \((Kg)(0)=0\), with the regular boundary condition at \(x=0\). For nonnegative \(g\), \(Kg\ge0\). Let \(m(x)=(K1)(x)\), which agrees with (4); it solves the standard mean-hitting-time boundary problem because \(m(b)-m(x)\) solves \(\mathscr L u=-1\) with \(u(b)=0\).

**2. Exact harmonic-number norm bound.** Write \(M=n-1\), \(W(u)=\int_0^u w(y)\,dy\), and \(J(u)=\int_0^u w(y)m(y)\,dy\). Since \(m\) increases strictly, the weighted moving average \(J(u)/W(u)\) is strictly increasing for \(0<u<1\). A Fubini exchange and the explicit expression \(W(u)=[1-(1-u)^M]/M\) show
\[
J(1)=\int_0^1(1-y)^{M-1}m(y)\,dy
=\frac1M\int_0^1\frac{W(u)}u\,du
=\frac{H_M}{M^2}.
\tag{6}
\]
The final identity follows from \(\int_0^1[1-(1-u)^M]u^{-1}\,du=H_M\). Hence \(J(u)/W(u)<\alpha_n=H_M/M\), increasing to \(\alpha_n\) at the right endpoint. Differentiating (5) yields
\[
\frac{(Km)'(u)}{m'(u)}=\frac{J(u)}{W(u)}<\alpha_n.
\]
Both functions vanish at zero, so integration gives the *strict* bound
\[
0<(Km)(x)<\alpha_n m(x)\quad (0<x<1).
\tag{7}
\]
Because \(m(x)\uparrow\infty\) and the ratio of derivatives tends to \(\alpha_n\), l'Hôpital's rule gives
\[
\lim_{x\uparrow1}\frac{(Km)(x)}{m(x)}=\alpha_n.
\tag{8}
\]
This is the sharp model-specific step. Repeated positivity of \(K\) and (7) imply \(0\le K^j1(x)\le\alpha_n^{j-1}m(x)\) for every integer \(j\ge1\).

**3. Hitting-time Laplace transform.** For \(s\in[0,1/\alpha_n)\), the series \(f_s(x)=\sum_{j=0}^{\infty}s^j(K^j1)(x)\) converges uniformly for \(0\le x\le b\); its terms are nonnegative. It satisfies \(f_s(0)=1\) and \(\mathscr Lf_s=sf_s\). Stopping the bounded local martingale \(e^{-s(t\wedge\tau_b)}f_s(X_{t\wedge\tau_b})\), and letting \(t\to\infty\), establishes
\[
\mathbb E_0[e^{-s\tau_b}]=\frac1{f_s(b)}.
\tag{9}
\]
The identity also holds at \(s=0\). In particular, setting \(s=\theta/m\), where \(m=m_n(b)\), gives
\[
f_{\theta/m}(b)=1+\theta+R_b(\theta),\quad
0<R_b(\theta)\le\frac{\alpha_n\theta^2}{m(1-\alpha_n\theta/m)}.
\tag{10}
\]
Subtract \(1/f_{\theta/m}(b)\) from \(1/(1+\theta)\). Since its denominator is at least \((1+\theta)^2\), (10) gives (1).

**4. Sharpness and weak convergence.** The leading remainder is
\[
R_b(\theta)=\frac{\theta^2(Km)(b)}{m^2}+O\!\left(\frac{\theta^3}{m^2}\right)
\quad\text{for fixed \(\theta\) as \(b\uparrow1\)},
\]
where the remainder follows from the positive-geometric bound in step 2. Equations (8) and (10) yield \(mR_b(\theta)\to\alpha_n\theta^2\). Replacing the denominator by its limit \((1+\theta)^2\) proves (2). The continuity theorem for Laplace transforms of laws on \([0,\infty)\) then proves \(Y_b\Rightarrow\operatorname{Exp}(1)\).

**5. Variance and its sharp deficit.** Differentiate (9) twice at \(s=0\):
\[
\mathbb E[\tau_b]=m,\qquad \mathbb E[\tau_b^2]=2[m^2-(Km)(b)].
\]
Thus \(\operatorname{CV}^2=1-2(Km)(b)/m^2\). Positivity of \(Km\) makes this strictly less than one; positivity of the variance follows from nondegeneracy of the diffusion's hitting time. Equation (8) proves (3). Finally, from (4), \(m_2(b)=\log(1/\varepsilon)\) and \(m_n(b)\sim\varepsilon^{2-n}/[(n-1)(n-2)]\) for \(n\ge3\), yielding the two explicit infidelity laws.

## Verification
The embedded `verification/check.py` separately evaluates the regular backward-ODE solution
\[
f_s(b)={}_2F_1\left(\frac{n-1-\sqrt{(n-1)^2-4s}}2,
\frac{n-1+\sqrt{(n-1)^2-4s}}2;1;b\right)
\]
using high-precision hypergeometric evaluation. It compares exact means with first parameter derivatives, computes second derivatives to check the strict variance gap, tests (1) at multiple allowed parameters, numerically integrates the weighted integral in (6), and samples convergence to (8). It uses `mpmath`, Python 3, and reproduces **186 passing numerical assertions**. These finite tests do not prove the quantified theorem: steps 1–5 provide that proof.

## Relationship to prior work
Tóth (2026), arXiv:2606.11438v1, derives the Fubini–Study Brownian-limit fidelity process, the explicit first-passage *mean* (its equation 17), its high-fidelity divergence (equation 18), and a spectral density / large-time exponential *tail* (equations 20–21). The present claim concerns the *whole mean-rescaled law* as target fidelity tends to one, its sharp harmonic-number first Laplace correction, a finite-threshold one-sided bound, and the precise variance deficit. A fixed-threshold large-time tail by itself does not imply these statements.

D'Onofrio, Tamborrino, and Lansky (2018) obtain general Jacobi hitting-time hypergeometric transforms and finite moments, including a coefficient of variation. These powerful classical formulas imply that moment values are in principle computable; no novelty is claimed for the mere availability of the Laplace transform or the second moment. Our quantified model-specific estimate and exact threshold-asymptotic coefficient require the additional positive-resolvent comparison (6)–(8). Demni (2014) provides existing projective-space Brownian heat-kernel distributions, not the specific rare-target approximation. Aldous (1982) and related rare-hitting literature establish generic near-exponential phenomena and error bounds in rapidly mixing systems; neither generic exponential convergence nor its qualitative proof is claimed as new here.

An implicit specialization of broader Jacobi or rare-event bounds remains a literature risk; the originality claim is limited to the displayed sharp quantitative formulae in this physical normalization.

## Limitations
The result is pointwise in each fixed finite Hilbert-space dimension, not uniform in \(n\). It concerns ideal continuous isotropic Brownian diffusion, not discrete steps, nonisotropic dynamics, noisy measurements, or a physical state preparation protocol with control restrictions. The bound (1) is one-sided and only applies when \(\alpha_n\theta<m_n(b)\); it does **not** claim the finite-threshold upper envelope is globally optimal. The sharpness assertion refers precisely to the coefficient of \(1/m_n(b)\) as \(b\uparrow1\), and does not imply a uniform-in-\(\theta\) distributional distance bound. The CV statement concerns ideal population moments, not finite-sample estimators. The proof does not assert that a specific experimental Lindblad trajectory realizes the isotropic diffusion model.

## References
1. Gyula I. Tóth, *Isotropic random walks and Brownian diffusion on complex projective space*, arXiv:2606.11438v1, first posted 2026-06-09; especially Section 3.3 and Appendix. https://arxiv.org/abs/2606.11438
2. Giuseppe D'Onofrio, Massimiliano Tamborrino, Petr Lansky, *The Jacobi diffusion process as a neuronal model*, Chaos **28** (2018), 103119, DOI 10.1063/1.5051494; especially Laplace and moment formulas (8)–(12). https://doi.org/10.1063/1.5051494
3. Nizar Demni, *Distributions of truncations of the heat kernel on the complex projective space*, Ann. Math. Blaise Pascal **21** (2014), 1–20, DOI 10.5802/ambp.339. https://doi.org/10.5802/ambp.339
4. David J. Aldous, *Markov chains with almost exponential hitting times*, Stochastic Processes and their Applications **13** (1982), 305–310, DOI 10.1016/0304-4149(82)90016-3.
