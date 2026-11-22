# Sharp stationary spatial-tail trichotomy under independent diffusivity switching and position resetting

## Finding

A bounded stochastic diffusivity coupled to *independent position-only* Poisson resetting produces a sharp three-regime stationary spatial-tail transition. Fix a refresh rate \(\lambda>0\), a position-reset rate \(r>0\), and define \(a=r+\lambda\). Let \(H=\int_0^1 W(d)/(1-d)\,\mathrm{d}d\) and \(r_c=\lambda(H-1)>0\). For the unique stationary positional density \(p_r\), as \(x\to+\infty\),

\[
p_r(x)\sim
\begin{cases}
K_{\mathrm{low}} e^{-\kappa_0 x},&0<r<r_c,\\
K_{\mathrm{crit}} x^{\nu-1}e^{-\sqrt a\,x},&r=r_c,\\
K_{\mathrm{high}} x^{-\nu-1}e^{-\sqrt a\,x},&r>r_c.
\end{cases}
\]

Here the unique \(\kappa_0\in(0,\sqrt a)\) solves
\[
\lambda\int_0^1\frac{W(d)}{a-\kappa_0^2d}\,\mathrm{d}d=1,
\]
and, writing \(\Delta=(r-r_c)/a\), the strictly positive amplitudes are

\[
\begin{split}
K_{\mathrm{low}}&=\frac{r}{2\kappa_0\lambda^2\displaystyle\int_0^1\frac{d\,W(d)}{(a-\kappa_0^2d)^2}\,\mathrm{d}d},\\
K_{\mathrm{crit}}&=\frac{r a^{1+\nu/2}\sin^2(\pi\nu)\Gamma(1-\nu)}{2^\nu\lambda^2 C\pi^2},\\
K_{\mathrm{high}}&=\frac{rC\,2^\nu\Gamma(\nu+1)}{a^{1+\nu/2}\Delta^2}.
\end{split}
\]

The boundary exponential moment distinguishes the regimes exactly:
\[
\mathbb E\!\left[e^{\sqrt a\,X}\right]
=\begin{cases}rH/(r-r_c),&r>r_c,\\ +\infty,&r\le r_c.\end{cases}
\]
For the natural beta-diffusivity family \(W(d)=(\nu+1)(1-d)^\nu\), the critical reset rate simplifies to \(r_c=\lambda/\nu\).

## Assumptions and scope

Let \(D_t\in[0,1]\) be a stationary, càdlàg Markov refresh process: at the events of a Poisson clock of rate \(\lambda\), independently draw a new diffusivity from the probability density \(W\). Independently, \(X_t\) solves \(\mathrm{d}X_t=\sqrt{2D_t}\,\mathrm{d}B_t\) between events of a second Poisson clock of rate \(r\); at each such event only \(X_t\) is reset to \(0\), while \(D_t\) is untouched. All noises and initial draws are independent except for the prescribed coupling through \(D_t\). We assume \(W\) is a normalized density, strictly positive on \((0,1)\), bounded near \(0\), continuously differentiable on \((0,1)\), and for \(u\downarrow0\),
\[
W(1-u)=Cu^\nu+O(u^{\nu+\eta}),\quad
\frac{\mathrm{d}}{\mathrm{d}u}W(1-u)=C\nu u^{\nu-1}+O(u^{\nu+\eta-1})
\]
for \(C,\eta>0\) and \(0<\nu<1\). These conditions imply finite \(H>1\). The assertion concerns the stationary **position marginal**, not first-passage times, relaxation eigenvalues or a finite-time large-deviation rate. The distribution is even in \(x\); the displayed one-sided asymptotics therefore describe both tails.

The position marginal is stationary and unique: independent Poisson position resets provide regeneration of \(X\), while the independent diffusivity-refresh process has its unique equilibrium \(W\). Equivalently, a stationary sample is the Gaussian stochastic integral over an independent exponential backward reset age and stationary diffusivity history.

## Proof

**1. Exact stationary transform.** For real \(k\), let
\[
g_k(t)=\int_0^1e^{-dk^2t}W(d)\,\mathrm{d}d,
\quad h_k(t)=\mathbb E\!\left[e^{-k^2\int_0^tD_s\,\mathrm{d}s}\right]
\]
with the initial diffusivity drawn from \(W\). Conditioning on the first diffusivity-refresh time gives
\[
h_k(t)=e^{-\lambda t}g_k(t)+\lambda\int_0^t e^{-\lambda u}g_k(u)h_k(t-u)\,\mathrm{d}u.
\]
An independent stationary reset age is exponential of rate \(r\). Writing
\[
Q_r(z)=\int_0^1\frac{W(d)}{a+dz}\,\mathrm{d}d,
\]
the position characteristic function is consequently
\[
\Phi_r(k)=r\int_0^\infty e^{-rt}h_k(t)\,\mathrm{d}t
=\frac{rQ_r(k^2)}{1-\lambda Q_r(k^2)}.\tag{1}
\]
In particular \(\Phi_r(0)=r(1/a)/(1-\lambda/a)=1\).

**2. Exact positive spectral resolution.** Denote the Stieltjes function in (1) by \(F_r(z)\). For \(s>a\), the upper boundary value on its cut is
\[
Q_r(-s+i0)=\operatorname{PV}\!\int_0^1\frac{W(d)}{a-sd}\,\mathrm{d}d
-\frac{i\pi}{s}W(a/s).
\]
Therefore the positive continuous Stieltjes spectral density is
\[
\rho_r(s)=-\frac1\pi\operatorname{Im}F_r(-s+i0)
=\frac{rW(a/s)}{s\,|1-\lambda Q_r(-s+i0)|^2},\quad s>a.\tag{2}
\]
Off the negative real cut, the imaginary part of \(Q_r\) has a strict sign, so \(1-\lambda Q_r\) has no nonreal zeros. On \(s\in(0,a)\), \(Q_r(-s)\) increases strictly from \(1/a\) to \(H/a\); hence there is exactly one isolated pole at \(s_0=\kappa_0^2\in(0,a)\) precisely if \(\lambda H>a\), i.e. \(r<r_c\). Its positive residue is
\[
R_0=\frac{r}{\lambda^2\displaystyle\int_0^1\frac{d\,W(d)}{(a-s_0d)^2}\,\mathrm{d}d}.
\]
At equality the divergent edge derivative for \(0<\nu<1\) makes the endpoint atom vanish. Since \(F_r(z)\to0\) as \(z\to+\infty\), these are all spectral contributions. The Stieltjes identity \(1/(s+k^2)\longleftrightarrow e^{-\sqrt{s}|x|}/(2\sqrt{s})\) gives the exact positional representation
\[
p_r(x)=\frac{\mathbf 1_{r<r_c} R_0}{2\sqrt{s_0}}e^{-\sqrt{s_0}|x|}
+\frac12\int_a^\infty\frac{\rho_r(s)}{\sqrt{s}}e^{-\sqrt{s}|x|}\,\mathrm{d}s.\tag{3}
\]
The positivity and normalization follow from (1)–(3), with no hidden singular atom at \(x=0\).

**3. Sharp edge analysis.** Let \(\epsilon=s-a\downarrow0\). The given edge assumptions and the beta-integral Cauchy-transform expansion imply
\[
Q_r(-a-\epsilon+i0)
=\frac Ha-\frac{C\pi}{a^{1+\nu}}[\cot(\pi\nu)+i]\epsilon^\nu
+o(\epsilon^\nu).\tag{4}
\]
For completeness, subtract \(H/a\), substitute \(u=1-d\), split at a small fixed \(u\), and scale \(u=\epsilon v/a\). The singular leading part is \((C/a^{1+\nu})\epsilon^\nu\int_0^\infty v^{\nu-1}(v-1+i0)^{-1}\,\mathrm{d}v\). The principal value equals \(-\pi\cot(\pi\nu)\), and the pole contributes \(-i\pi\); the regular remainder is \(o(\epsilon^\nu)\). This proves (4), including its sign. For \(r>r_c\), \(1-\lambda H/a=\Delta>0\), so (2) yields
\[
\rho_r(a+\epsilon)\sim\frac{rC}{a^{1+\nu}\Delta^2}\epsilon^\nu.\tag{5}
\]
For \(r=r_c\), the constant denominator disappears; since \(\cot^2(\pi\nu)+1=\csc^2(\pi\nu)\),
\[
\rho_r(a+\epsilon)\sim
\frac{r a^{1+\nu}\sin^2(\pi\nu)}{\lambda^2C\pi^2}\epsilon^{-\nu}.\tag{6}
\]
As \(x\to\infty\), \(\sqrt{a+\epsilon}=\sqrt a+\epsilon/(2\sqrt a)+O(\epsilon^2)\). Applying the elementary Laplace endpoint integral \(\int_0^\infty\epsilon^\sigma e^{-x\epsilon/(2\sqrt a)}\,\mathrm{d}\epsilon=\Gamma(\sigma+1)(2\sqrt a/x)^{\sigma+1}\) for \(\sigma>-1\) to (3), with (5) or (6), gives exactly \(K_{\mathrm{high}}\) and \(K_{\mathrm{crit}}\). The distant continuum is exponentially smaller than the pole for \(r<r_c\), giving \(K_{\mathrm{low}}\). The edge remainder and all \(s>a+\delta\) contributions are controlled by the stated regularity and positivity of (2).

**4. Moment boundary.** For \(r>r_c\), the supercritical tail is integrable after multiplication by \(e^{\sqrt a x}\). Evaluate the analytic continuation of (1) at \(k=i\sqrt a\) to obtain \(Q_r(-a)=H/a\) and \(\mathbb E[e^{\sqrt aX}]=rH/(r-r_c)\). For \(r=r_c\), the critical tail times that exponential is asymptotic to \(K_{\mathrm{crit}}x^{\nu-1}\), which is not integrable. For \(r<r_c\), the pole decays more slowly, so the same moment diverges.

## Verification

The standalone file `verify_reset_edge.py` (Python with NumPy and SciPy) independently integrates the real-axis renewal expression (1) and the complex-cut spectral formula (2), and checks their agreement at twelve parameter pairs for \(W(d)=\tfrac32\sqrt{1-d}\) and \(\lambda=1\). It additionally checks normalization, pole existence, positive densities, asymptotic ratios in all three regimes, a finite boundary exponential moment, and four edge-coefficient comparisons for two other beta laws. Running `python verify_reset_edge.py` yields `PASS`. Finite numerical quadrature checks are supporting diagnostics; the assertions for all admissible parameters and arbitrarily large \(x\) follow from the proof.

## Relationship to prior work

The key continuously refreshed diffusivity model, its renewal formulation and a **BBP-type secular spectral threshold** were developed by Guéneau, Schorlepp, Majumdar and Schehr (2026), following Guéneau, Majumdar and Schehr (2025). Those works concern fixed observation times and displacement large deviations; the secular pole/edge mechanism is not claimed as new here. Evans and Majumdar (2014) establish ordinary constant-diffusivity Poisson-reset stationary laws. Bressloff (2020) studies finite-state switching diffusivity with a jointly reset internal state, resulting in a finite sum of exponentials rather than a continuous upper-edge algebraic transition. Arutkin and Reuveni (2025) switch the *reset rate*, not the diffusivity. Santra, Basu and Sabhapandit (2022) reset both the position and a different unbounded stochastic diffusivity, with stretched-exponential stationary tails. The specific continuous-refresh, **position-only** reset stationary kernel and its three sharp spatial asymptotics and evaluated prefactors are not stated in those inspected materials; mathematical priority is not certified by a nonexhaustive search.

## Limitations

The theorem assumes a bounded diffusivity support normalized to \([0,1]\), a positive density, and \(0<\nu<1\) with edge regularity; other edge exponents, discontinuous supports, reset protocols and higher spatial dimensions are not classified. The original diffusivity BBP mechanism and general resetting-renewal machinery are established prior work. A relevant 2020 finite-switching-state paper could not be inspected in complete full text; this leaves an explicit source-access uncertainty, although its published description specifies a different finite-state model. No independent scientific audit has been performed.

## References

- M. Guéneau, T. Schorlepp, S. N. Majumdar, G. Schehr, *Large Deviations in Switching Diffusion: Dynamical Condensation and Diffusivity BBP Transition* (first public 2026-10-18), https://arxiv.org/abs/2610.25072, especially Section 3 and equations (30)–(36).
- M. Guéneau, S. N. Majumdar, G. Schehr, *Large Deviations in Switching Diffusion: from Free Cumulants to Dynamical Transitions* (2025), https://arxiv.org/abs/2501.13754.
- P. C. Bressloff, *Switching diffusions and stochastic resetting* (2020), https://doi.org/10.1088/1751-8121/ab97e0.
- M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting* (2025), https://arxiv.org/abs/2509.25365.
- I. Santra, U. Basu, S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient* (2022), https://arxiv.org/abs/2205.00549.
- M. R. Evans and S. N. Majumdar, *Diffusion with resetting in arbitrary spatial dimension* (2014), https://arxiv.org/abs/1404.4574.
