# Two-scale failure of Gaussian averaging under fast harmonic-trap switching

## Finding

For a stationary Brownian particle with diffusivity \(D>0\), alternating at equal Poisson rate \(q>0\) between two strictly confining trap relaxations \(0<\alpha<\beta\), the fast-switching Gaussian approximation is **not uniform in displacement**. At the rare scale \(x=\sqrt q\,y\), the exact stationary position density has the sharp limit

\[
\pi_q(\sqrt q\,y)=A(y)e^{-qI(y)}(1+o(1)),\qquad q\to\infty,
\]

for each fixed \(y\in\mathbb R\), with \(A(y)>0\) and \(I(y)\) defined explicitly below. The rate is strictly between the weak- and averaged-trap Gaussian costs for every \(y\ne0\):

\[
\frac{\alpha y^2}{2D}<I(y)<\frac{(\alpha+\beta)y^2}{4D}.
\]

**Gaussian averaging first loses relative accuracy already at the smaller quartic scale** \(x=tq^{1/4}\). Let \(v_0=2D/(\alpha+\beta)\) and \(\phi_{v_0}(x)=e^{-x^2/(2v_0)}/\sqrt{2\pi v_0}\). For every fixed real \(t\),

\[
\lim_{q\to\infty}\frac{\pi_q(tq^{1/4})}{\phi_{v_0}(tq^{1/4})}=\exp\left[\frac{(\alpha+\beta)(\beta-\alpha)^2}{64D^2}t^4\right].
\]

Thus there are **two distinct nested scales**: a \(q^{1/4}\) onset of a universal quartic correction to the averaged Gaussian, and a \(q^{1/2}\) nonlinear large-deviation saddle. The hidden variance conditioned on the latter rare displacement selects a **unique**, strictly increasing function of \(|y|\), and the probability that the trap is currently in its weak state converges to a strictly increasing function of \(|y|\), from \(1/2\) to \(1\). Thus arbitrarily fast switching leaves an order-one hidden-state fingerprint at the rare-displacement scale. If \(D\) is known, the curvature of \(I\) at the origin and its far-tail quadratic coefficient determine the two stiffnesses individually, whereas the central Gaussian law sees only their sum.

## Assumptions and scope

Consider the unique stationary solution of

\[
dX_t=-k_{J_t}X_t\,dt+\sqrt{2D}\,dW_t,
\]

where \(W\) is standard real Brownian motion and \(J\) is an independent irreducible two-state continuous-time Markov chain switching at rate \(q\) in both directions. Its weak and strong relaxation constants are \(k_0=\alpha\) and \(k_1=\beta\), respectively, with \(0<\alpha<\beta\). Write \(\pi_q\) for the stationary density of \(X\). No stationary Gaussianity at finite \(q\) is assumed.

Introduce

\[
a=\frac1{2\beta},\quad b=\frac1{2\alpha},\quad z_0=\frac{a}{a+b}=\frac\alpha{\alpha+\beta},\quad v(z)=\frac D\beta+\left(\frac D\alpha-\frac D\beta\right)z,\quad L=\frac D\alpha-\frac D\beta.
\]

Define \(W(z)=\alpha+(\beta-\alpha)z\) and the strictly convex cost

\[
h(z)=a\log\frac{z_0}{z}+b\log\frac{1-z_0}{1-z},\qquad F_y(z)=h(z)+\frac{y^2}{2v(z)},\qquad 0<z<1.
\]

Let \(z_y\) be the unique minimizer of \(F_y\), and put

\[
I(y)=F_y(z_y),\quad H_0=\frac a{z_0^2}+\frac b{(1-z_0)^2},\quad H_y=\frac a{z_y^2}+\frac b{(1-z_y)^2}+\frac{y^2L^2}{v(z_y)^3}.
\]

Then the **sharp asymptotic prefactor** is

\[
A(y)=\frac1{\sqrt{2\pi v(z_y)}}\sqrt{\frac{H_0}{H_y}}\,\frac{W(z_y)}{W(z_0)}\,\frac{z_0(1-z_0)}{z_y(1-z_y)}.
\]

The minimizer is characterized without optimization ambiguity by \(z_y=z_0\) for \(y=0\) and, for \(y\ne0\), by the unique \(z_y\in(z_0,1)\) satisfying

\[
\frac b{1-z_y}-\frac a{z_y}=\frac{Ly^2}{2v(z_y)^2}.
\]

## Proof

**1. Exact variance-mixture normalization.** In the pullback stationary construction, condition on the entire past of the two-state trap. The positional distribution is centered Gaussian with random variance

\[
V=2D\int_{-\infty}^0\exp\left[-2\int_s^0 k_{J_u}\,du\right]ds.
\]

This integral converges, and \(D/\beta<V<D/\alpha\) almost surely because both trap states have positive stationary holding time. Along each fixed trap path, \(dV/dt=2D-2k_{J_t}V\), so the scaled variance \(Z=(V-D/\beta)/L\) moves with velocities \(2\alpha(1-Z)\) in the weak state and \(-2\beta Z\) in the strong state. The two stationary transport equations have zero total flux through \((0,1)\). Their partial densities are therefore

\[
f_0(z)=\frac{K z^{aq}(1-z)^{bq}}{2\alpha(1-z)},\qquad
f_1(z)=\frac{K z^{aq}(1-z)^{bq}}{2\beta z}.
\]

The stationarity equations determine the exponents \(aq=q/(2\beta)\) and \(bq=q/(2\alpha)\), and normalization determines the sum:

\[
g_q(z)=f_0(z)+f_1(z)=\frac{\alpha+\beta}{2\alpha\beta B(aq,bq)}W(z)z^{aq-1}(1-z)^{bq-1}.
\]

Indeed, beta averaging gives \(\mathbb E_{\mathrm{Beta}(aq,bq)}[W(Z)]=W(z_0)=2\alpha\beta/(\alpha+\beta)\). Thus the **complete** stationary position density is the Gaussian mixture

\[
\pi_q(x)=\int_0^1\frac{g_q(z)}{\sqrt{2\pi v(z)}}\exp\left[-\frac{x^2}{2v(z)}\right]dz.
\]

This mixture (in an equivalent parameterization) is known from the fluctuating harmonic-trap literature and is the starting point, not the novelty claimed here.

**2. Singular fast-switching asymptotics.** The beta normalizer has the Stirling expansion, with \(a,b>0\) fixed,

\[
B(aq,bq)=\frac{e^{q[a\log z_0+b\log(1-z_0)]}}{z_0(1-z_0)}\sqrt{\frac{2\pi}{qH_0}}\,(1+O(q^{-1})).
\]

Therefore the integral defining \(\pi_q(\sqrt q\,y)\) has phase \(F_y\) and positive amplitude proportional to \(W(z)/[z(1-z)\sqrt{2\pi v(z)}]\). The phase has strictly positive second derivative on \((0,1)\), equal to \(H_y\) at its saddle, and diverges at both endpoints. For \(y\) in any fixed compact set the saddles stay in a common interior interval. The endpoint amplitude singularities cause no difficulty: multiplying the amplitude by \(e^{-h(z)}\) makes it integrable, and on sufficiently small endpoint neighborhoods \(F_y(z)-F_y(z_y)\) is uniformly bounded below by a positive number. There the remaining exponential after extracting one factor of \(e^{-F_y(z)}\) is exponentially small relative to its value at the saddle. The ordinary interior Laplace expansion thus gives the stated \(I(y)\) and \(A(y)\), uniformly for \(y\) in compact sets; no uniformity for \(|y|\to\infty\) is asserted.

**3. Strict rate inequalities and the selected hidden state.** The unconstrained minimum of \(h\) is \(0\), attained only at \(z_0\). For \(y\ne0\), \(F_y'(z_0)=-Ly^2/[2v(z_0)^2]<0\), so \(z_y>z_0\). Since \(z_y<1\), positivity of \(h\) and the strict inequality \(v(z_y)<D/\alpha\) imply the lower Gaussian bound. Evaluating \(F_y\) at \(z_0\), and using \(z_y\ne z_0\), gives the strict upper bound. Implicit differentiation of the saddle equation yields

\[
\frac{dz_y}{d(y^2)}=\frac{L}{2v(z_y)^2H_y}>0.
\]

The conditional density of the latent variance under \(X=\sqrt q\,y\) is the above positive-amplitude Laplace law and concentrates at \(z_y\), with

\[
\sqrt q\,(Z-z_y)\mid (X=\sqrt q\,y)\quad\Longrightarrow\quad N(0,H_y^{-1}).
\]

The exact weak-state posterior at a fixed variance is \(\Pr(J=0\mid Z=z)=\beta z/W(z)\). Hence

\[
\lim_{q\to\infty}\Pr(J=0\mid X=\sqrt q\,y)=\frac{\beta z_y}{W(z_y)}.
\]

It is \(1/2\) at \(y=0\), strictly increases with \(|y|>0\), and tends to one as \(|y|\to\infty\).

**4. The earlier quartic crossover.** Expansion of the smooth minimizer near \(y=0\) yields

\[
I(y)=\frac{\alpha+\beta}{4D}y^2-\frac{(\alpha+\beta)(\beta-\alpha)^2}{64D^2}y^4+O(y^6).
\]

The Laplace expansion in step 2 is uniform with smoothly varying \(y\) near zero. Set \(y=tq^{-1/4}\). The displayed small-\(y\) expansion then gives \(qI(y)=(\alpha+\beta)t^2\sqrt q/(4D)-Kt^4+O(q^{-1/2})\), where \(K=(\alpha+\beta)(\beta-\alpha)^2/(64D^2)>0\); the prefactor tends to \(1/\sqrt{2\pi v_0}\). Thus

\[
\lim_{q\to\infty}\frac{\pi_q(tq^{1/4})}{\phi_{v_0}(tq^{1/4})}=e^{Kt^4}.
\]

The same estimate shows the ratio tends to one for \(|x|=o(q^{1/4})\), while for \(q^{1/4}\ll|x|\ll\sqrt q\), \(\log[\pi_q(x)/\phi_{v_0}(x)]\sim Kx^4/q\). This identifies the **first relative-error crossover**, which precedes the more extreme \(x=\sqrt q\,y\) large-deviation crossover.

**5. Fixed-rate tails and the inverse fingerprint.**

At the opposite extreme put \(v_+=D/\alpha\) and \(c=2bv_+^2/L=D\beta/[\alpha^2(\beta-\alpha)]\). With \(\delta=1-z_y\), the saddle equation first gives \(\delta=O(y^{-2})\) and then \(\delta=c/y^2+O(y^{-4})\). The Gaussian part of the cost satisfies \(y^2/(2v(z_y))=y^2/(2v_+)+b+O(y^{-2})\), because \(Lc/(2v_+^2)=b\). The entropy part equals \(2b\log|y|+a\log z_0+b\log(1-z_0)-b\log c+O(y^{-2})\). Adding the two contributions gives

\[
I(y)=\frac{\alpha y^2}{2D}+\frac1\alpha\log|y|+C+O(y^{-2}),\quad C=b+a\log z_0+b\log(1-z_0)-b\log c.
\]

In particular, \(I''(0)=(\alpha+\beta)/(2D)\) and \(\lim_{|y|\to\infty}2DI(y)/y^2=\alpha\); at known \(D\), these identify \(\alpha\) and \(\beta\) separately. For comparison, at **each fixed** finite \(q\), an endpoint Laplace expansion applied to the exact mixture gives

\[
\pi_q(x)\sim C_q|x|^{-q/\alpha}e^{-\alpha x^2/(2D)},\quad
C_q=\frac{\alpha+\beta}{2\alpha B(aq,bq)\sqrt{2\pi D/\alpha}}\Gamma(bq)\left(\frac{2(D/\alpha)^2}{L}\right)^{bq}.
\]

The fixed-\(q\) asymptotic is not uniform in \(q\); taking \(q\to\infty\) first at fixed \(x\) gives instead the Gaussian with variance \(2D/(\alpha+\beta)\). The \(q^{1/4}\) quartic crossover is the first failure of relative Gaussian accuracy; the \(q^{1/2}\) scale marks the further nonlinear large-deviation regime. These are distinct nested limits.

## Verification

The companion `checker.py` evaluates the Gaussian-mixture integral using log-stabilized quadrature, solves the unique saddle equation by root-finding, and compares its prefactor at several positive switching rates. It checks beta normalization, strict rate inequalities, weak-state posterior bounds, the quartic crossover, the small-distance quartic coefficient, and the leading large-distance scaling of \(1-z_y\). The additive constant in the large-distance expansion of \(I(y)\) is derived above, not tested by that checker. Run `python checker.py` with Python and SciPy. The finite calculations are corroborative only; the infinite-parameter statements use the analytic stationary representation and Laplace expansion.

For \(\alpha=D=1,\ \beta=3\), the saddle values at \(y=1\) are \(z_y\approx0.519933984250264\) and \(I(1)\approx0.836376344190687\); the limiting conditional probability of the weak state is approximately \(0.764658290064418\), compared with \(1/2\) for central observations.

## Relationship to prior work

Alston, Cocconi and Bertrand (2022), §4.2.2, study the symmetric two-positive-stiffness trap and its fast-switching entropy production. Santra, Das and Nath (2021), Eqs. (30)–(34), obtain the averaged Gaussian at fast switching and discuss tails for an on/off trap with zero weak-state stiffness. Biroli, Kulkarni, Majumdar and Schehr (2023), Eqs. (12)–(13) and (S49)–(S52), give the exact common-variance Gaussian mixture, including its rate-dependent mixing law. **That finite-parameter law is known and is not claimed as new.** The two-scale result is an asymptotic analysis of that law, not a competing stationary model. The rare-displacement prefactor and posterior refine the leading logarithmic cost; the quartic limit identifies where ordinary Gaussian averaging first loses relative accuracy. The large-particle-number extremes in Biroli et al. concern a different asymptotic regime, as do related fixed-switching-rate results on collective empirical energy and Gumbel edges.

## Limitations

The switching rates are symmetric, both stiffnesses are strictly positive and unequal, the motion is overdamped and one-dimensional, and the diffusion strength is common to both states. The sharp prefactor applies on compact rare-displacement scales, not when \(y\) itself diverges with \(q\). The separate fixed-rate far tail and fast-switching tail cannot be interchanged without a uniform approximation not proved here. Hidden-state selection concerns the current trap state, not its entire past path. Historical priority is not asserted exhaustively: earlier single-particle analyses and more general switching-diffusion or variance-mixture asymptotics may contain related limits.

## References

- H. Alston, L. Cocconi, T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, 2022, arXiv:2202.02630, https://arxiv.org/abs/2202.02630 (first public 2022-02-05).
- M. Biroli, M. Kulkarni, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, 2023, arXiv:2312.02570, https://arxiv.org/abs/2312.02570 (first public 2023-12-05).
- D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, 2026, arXiv:2607.05173, https://arxiv.org/abs/2607.05173 (related Gaussian variance-mixture framework; abstract compared only).
- I. Santra, S. Das, S. K. Nath, *Brownian motion under intermittent harmonic potentials*, 2021, arXiv:2104.00609, https://arxiv.org/abs/2104.00609v2.
