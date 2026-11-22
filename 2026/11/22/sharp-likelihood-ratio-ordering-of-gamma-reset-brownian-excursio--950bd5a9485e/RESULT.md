# Sharp likelihood-ratio ordering of Gamma-reset Brownian excursions with ballistic returns

## Finding
Fix a Brownian diffusivity \(D>0\), Gamma reset rate \(r>0\), Gamma shape \(k>0\), and a positive deterministic return speed \(v>0\). During each cycle a Brownian particle diffuses from zero until an independent \(\operatorname{Gamma}(k,r)\) time, then returns linearly to zero at speed \(v\); cycles repeat independently. Write \(R_v=|X_v|\) for the absolute stationary position and \(f_v\) for its density on \((0,\infty)\).

**Theorem (all-threshold order).** For every pair \(0<v_1<v_2<\infty\), the likelihood ratio \(f_{v_2}(z)/f_{v_1}(z)\), as a function of \(z>0\), is strictly decreasing if \(k>1\) and strictly increasing if \(0<k<1\). Consequently, at **every** threshold \(z>0\),
\[
\begin{array}{ll}
\Pr(R_{v_2}>z)<\Pr(R_{v_1}>z), & k>1,\\[2pt]
\Pr(R_{v_2}>z)>\Pr(R_{v_1}>z), & 0<k<1.
\end{array}
\]
At \(k=1\), \(R_v\sim\operatorname{Exp}(\sqrt{r/D})\) for every \(v\), and neither inequality is strict. Thus Gamma shape one is the *sharp boundary* for the global ordering, not merely for behavior at the origin or in the far tail.

**Single-threshold inverse law.** Let \(B_t\) be Brownian motion of generator \(D\partial_{xx}\), let \(T\sim\operatorname{Gamma}(k,r)\) be independent, and let \(W=|B_T|\). For each \(z>0\), set
\[
\begin{aligned}
 a&=\mathbb ET=k/r, & b&=\mathbb EW=\frac{2\sqrt{D/r}\,\Gamma(k+1/2)}{\sqrt\pi\,\Gamma(k)},\\
 A(z)&=\frac{\mathbb E[(W-z)_+^2]}{2D}, & C(z)&=\mathbb E[(W-z)_+].
\end{aligned}
\]
Then the stationary tail probability \(q_v(z)=\Pr(R_v>z)\) is exactly
\[
 q_v(z)=\frac{vA(z)+C(z)}{va+b}.
\]
For \(k\ne1\), any fixed positive threshold has a strictly monotone response to return speed. Every observed tail probability strictly between its slow- and fast-return limiting values therefore identifies one and only one speed, through
\[
 \boxed{\displaystyle v=\frac{C(z)-q_v(z)b}{q_v(z)a-A(z)}.}
\]
The limiting probabilities at \(v\downarrow0\) and \(v\uparrow\infty\) correspond to return-phase and diffusion-phase occupancy, respectively; endpoints themselves are not finite-speed values.

## Assumptions and scope
All parameters \(D,r,k,v\) are strictly positive and finite. Brownian paths have independent increments and generator \(D\partial_{xx}\), so \(B_t\sim\mathcal N(0,2Dt)\). Each cycle starts at zero; at the end of its independent Gamma running interval, the particle moves directly toward zero at constant speed, taking exactly \(|B_T|/v\) units of time. It immediately starts a fresh independent cycle. The stationary position means sampling a typical time in the regenerative equilibrium, not the distribution at a reset instant. The mean cycle duration is \(a+b/v\in(0,\infty)\), establishing existence and uniqueness of this stationary occupation distribution. The theorem concerns the absolute displacement; the full signed law is symmetric. \(\operatorname{Gamma}(k,r)\) uses shape \(k\), rate \(r\), not scale \(r\).

## Proof
**1. Exact occupation density.** Let \(S(z)=\Pr(W>z)\) and \(H(z)=\mathbb E(W-z)_+=\int_z^\infty S(u)\,du\) for \(z>0\). During the return phase, a completed path with endpoint magnitude \(W\) spends \(dz/v\) in the radial interval \((z,z+dz)\) precisely when \(W>z\). Hence expected return occupation density is \(v^{-1}S(z)\).

For the diffusive phase, let \(p_t(x)\) be the signed Gaussian heat kernel. Itô–Tanaka's formula, or the heat equation applied to \((x-z)_+\), gives for fixed \(t>0\)
\[
 D\int_0^t p_s(z)\,ds=\mathbb E(B_t-z)_+.
\]
Symmetry implies \(2\mathbb E(B_t-z)_+=\mathbb E(|B_t|-z)_+\), and the radial density of \(|B_s|\) is \(2p_s(z)\). Averaging over the independent \(T\), the expected diffusive occupation density is therefore \(H(z)/D\). Division by mean cycle time yields the exact identity
\[
 \boxed{\displaystyle f_v(z)=\frac{vH(z)/D+S(z)}{va+b}},\qquad z>0.
\]
This is correctly normalized, because \(\int_0^\infty H(z)\,dz=\mathbb EW^2/2=D\mathbb ET=Da\), and \(\int_0^\infty S(z)\,dz=b\). Integrating the density from \(z\) to infinity gives the asserted tail formula, since
\[
 \int_z^\infty H(u)\,du=\frac12\mathbb E[(W-z)_+^2],\qquad
 \int_z^\infty S(u)\,du=C(z).
\]

**2. Exact Gamma-difference endpoint law.** With \(\lambda=\sqrt{r/D}\),
\[
\mathbb Ee^{i\xi B_T}=\mathbb Ee^{-D\xi^2T}
=\left(\frac{r}{r+D\xi^2}\right)^k
=\left(\frac{\lambda}{\lambda-i\xi}\right)^k
 \left(\frac{\lambda}{\lambda+i\xi}\right)^k.
\]
Consequently \(B_T\) has the same law as \(G_1-G_2\), where \(G_1,G_2\) are independent Gamma variables of common shape \(k\) and rate \(\lambda\). The density \(g_k(z)\) of \(W=|G_1-G_2|\) for \(z>0\) is proportional to
\[
 e^{-\lambda z}\int_0^\infty
 y^{k-1}(y+z)^{k-1}e^{-2\lambda y}\,dy.
\]
The Gamma-difference representation and this integral hold for every \(k>0\), including shapes below one.

**3. Sharp log-curvature dichotomy.** If \(k>1\), the Gamma density \(t^{k-1}e^{-\lambda t}\mathbf1_{t>0}\) is log-concave, since its logarithm has second derivative \(-(k-1)/t^2<0\). Log-concavity is preserved under reflection and convolution (the standard Prékopa marginalization theorem). Thus the density of \(G_1-G_2\), and hence its restriction and rescaling \(g_k(z)\) on \((0,\infty)\), is log-concave. Integration over a positive half-line preserves log-concavity, so \(S(z)=\int_z^\infty g_k(u)\,du\) is log-concave.

If \(0<k<1\), use the positive Laplace representation
\[
 (y+z)^{k-1}=\frac{1}{\Gamma(1-k)}
 \int_0^\infty s^{-k}e^{-s(y+z)}\,ds.
\]
After integrating over \(y>0\), the density \(g_k(z)\) is a positive nondegenerate mixture of functions \(e^{-(\lambda+s)z}\), indexed by \(s>0\). Its survival \(S(z)\) is also a nondegenerate positive mixture of exponentials; by strict Cauchy–Schwarz, \(\log S\) is strictly convex on \((0,\infty)\). Finally, at \(k=1\), the Gamma difference is Laplace and \(S(z)=e^{-\lambda z}\) is exactly exponential.

In the log-concave case, \(S(z+t)/S(z)\) is nonincreasing in \(z\) for every fixed \(t>0\); in the strictly log-convex case it is strictly increasing. It is *strictly* decreasing overall for \(k>1\) as well: \(S\) is real analytic on \((0,\infty)\) and is not exponential on any interval, because \(g_k(z)\sim c_kz^{k-1}e^{-\lambda z}\) at infinity with \(k\ne1\). Therefore its log-concavity cannot be affine on an open interval. It follows that the mean residual magnitude
\[
 m(z)=\frac{H(z)}{S(z)}
 =\int_0^\infty\frac{S(z+t)}{S(z)}\,dt
\]
is strictly decreasing for \(k>1\), strictly increasing for \(0<k<1\), and constant \(1/\lambda\) at \(k=1\). All integrals converge because of the exponential endpoint tail.

**4. From residual-life order to likelihood-ratio order.** Define the normalized phase-conditional densities
\[
 f_D(z)=\frac{H(z)}{Da},\qquad f_R(z)=\frac{S(z)}b.
\]
Then
\[
 \frac{f_D(z)}{f_R(z)}=\frac{b}{Da}m(z),\qquad
 f_v(z)=\frac{va f_D(z)+b f_R(z)}{va+b}.
\]
For \(v_2>v_1\), the ratio \(f_{v_2}/f_{v_1}\) is a strictly increasing fractional-linear function of \(f_D/f_R\), because its derivative with respect to that argument is proportional to \(ab(v_2-v_1)>0\). Thus it is strictly decreasing in \(z\) for \(k>1\), strictly increasing for \(0<k<1\), and constant at \(k=1\). Since both densities integrate to one and are strictly positive, each strictly monotone likelihood ratio crosses one exactly once. Integrating the resulting single-crossing difference proves the stated strict stochastic tail ordering **at every positive threshold**. The tail-inversion formula follows by rearrangement; its denominator cannot vanish at an interior finite-speed observation when \(k\ne1\), by the strict ordering.

## Verification
The standalone `CHECKER.py` (Python 3, NumPy, SciPy) runs with `python CHECKER.py` and passed **114 deterministic assertions**. These independently compare original Brownian/Gamma cycle integrals against Gamma-difference/Bessel representations; verify normalization, exact Poisson-return invariance, the explicit Erlang-two formula, the sign of the tail response at multiple thresholds and rates, the likelihood-ratio direction, and inversion of synthetic single-threshold observations. In units \(D=r=1\), the explicit Erlang-two check is
\[
 \Pr(R_v>z)=e^{-z}\frac{v(z+4)+(z+3)}{4v+3},\qquad k=2.
\]
This formula is an algebraic consequence of already-published special-case densities and is used only as a verification anchor. Numerical checks do not establish a global all-parameter order; Steps 1–4 provide that proof. All assertions were replayed from the actual standalone checker before packaging.

## Relationship to prior work
Radice's Gamma-clock, finite-speed return model (arXiv:2201.01829, first public January 5, 2022) derives the stationary position density, shows exact speed invariance at the exponential shape, and compares the **origin and far-tail behavior** on the two sides of that shape (especially sections 3–4, Appendix B). Those established facts, including the speed-invariant case and the Erlang-two closed form, are not claimed as new. The finding here is stronger: a **strict likelihood-ratio ordering at every radius**, full strict stochastic ordering of all positive thresholds, and injectivity and an inverse formula for any one tail observation. Endpoint or asymptotic comparisons alone do not imply such an all-radius ordering.

Bodrova and Sokolov (arXiv:1907.12326, sections II–V) give the general regenerative two-phase stationary density and the condition for independence from the return speed; they focus on exponential/deterministic reset protocols rather than the Gamma-shape global likelihood-ratio theorem. Masó-Puigdellosas, Campos and Méndez (arXiv:1910.09927) compare transport under exponential and Pareto resets, and do not establish the Gamma-shape ordering. A related published study of extreme Gamma-reset excursions (published-finding corpus, October 26, 2026) determines hidden-phase and reset-age limits conditioned on distant excursions; its limiting laws and tail coefficient do not imply the finite-radius likelihood-ratio ordering. The standard log-concavity, convolution and hazard results used in the proof are mathematical background, not novelty claims.

## Limitations
The ordering is for a one-dimensional Brownian displacement phase, independent Gamma reset alarms and **constant-speed direct** returns, observed in regenerative stationarity. It does not automatically cover random velocities, nonlinear return paths, non-Gamma renewal clocks, intermediate-time positions, first-passage times or multidimensional radial returns. The inverse calibration assumes the Gamma parameters and diffusivity are already known and an exact stationary exceedance probability; estimation error and finite-sample uncertainty are not treated. Unindexed general stochastic-order comparisons of reset-return models remain a potential priority risk. There is no independent scientific audit of this result.

## References
- Mattia Radice, *Diffusion processes with Gamma-distributed resetting and non-instantaneous returns*, arXiv:2201.01829v1, first public 2022-01-05, especially sections 2–4 and Appendix B. https://arxiv.org/abs/2201.01829
- Anna S. Bodrova and Igor M. Sokolov, *Resetting processes with non-instantaneous return*, arXiv:1907.12326v1, first public 2019-07-29, sections II–V. https://arxiv.org/abs/1907.12326
- Axel Masó-Puigdellosas, Daniel Campos and Vicenç Méndez, *Transport properties of random walks under stochastic non-instantaneous resetting*, arXiv:1910.09927v1, first public 2019-10-22. https://arxiv.org/abs/1910.09927
- *Universal hidden-phase and Gaussian age laws for extreme Gamma-reset diffusion with finite-speed returns*, published-finding corpus, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-universal-hidden-phase-and-gaussian-age-laws-for-extreme-gamma-r--5c356dfeaeaf
- A. Prékopa, *Logarithmic concave measures and related topics*, in *Stochastic Programming*, Academic Press (1980), for closure under convolution and marginalization.
