# A unique Poisson-reset optimum and sharp temperature-contrast scales for Gaussian endpoint divergence

## Finding

Fix a relaxation rate \(\lambda>0\), diffusivity \(D>0\), and finite reset-width ratio \(0<q<1\). Consider the one-dimensional Ornstein–Uhlenbeck diffusion between independent Poisson resetting events, each of which redraws the position from \(\mathcal N(0,qD/\lambda)\). At no-reset age \(t\geq0\), the conditional state is \(\mathcal N(0,(D/\lambda)u_q(2\lambda t))\), with \(u_q(s)=1-(1-q)e^{-s}\). Let \(G_q(s)\) be the Jeffreys divergence (sum of the two directed Kullback–Leibler divergences) between this conditional state and the reset state. Define the **endpoint-divergence reward per unit time**
\[
\mathcal K_q(r)=r\,\mathbb E[G_q(2\lambda T_r)],\qquad T_r\sim\operatorname{Exp}(r),\quad r>0.
\]
Then \(\mathcal K_q(r)\) has precisely one critical point, a strict global maximum \(r_*(q)\). It increases before and decreases after this optimum, and vanishes as \(r\downarrow0\) and as \(r\to\infty\). With \(k_*(q)=r_*(q)/(2\lambda)\),
\[
\lim_{q\uparrow1}k_*(q)=\sqrt2,\qquad
\lim_{q\uparrow1}\frac{\mathcal K_q(r_*(q))}{2\lambda(1-q)^2}
=\frac{\sqrt2}{(\sqrt2+1)(\sqrt2+2)}.
\]
In the sharply localized but still finite-width regime,
\[
\lim_{q\downarrow0}\sqrt q\,k_*(q)=1,\qquad
\frac{\mathcal K_q(r_*(q))}{2\lambda}
=\frac1{2q}-\frac1{\sqrt q}+o(q^{-1/2}).
\]
Equivalently, \(r_*(q)\sim2\lambda/\sqrt q\) when \(q\downarrow0\).

The exact optimizer is the unique positive root of
\[
\int_0^1\frac{y^k(1-y)[1+q-(1-q)y]}{[1-(1-q)y]^2}\,(1+k\log y)\,dy=0.
\]
This is a theorem about the specified **cycle-wise conditional endpoint-divergence rate**, not an identity for the physical resetting cost, time-reversed trajectory entropy production, or the Jeffreys divergence of the stationary non-Gaussian mixture.

## Assumptions and scope

The Ornstein–Uhlenbeck stochastic differential equation between resets is \(dX_t=-\lambda X_t\,dt+\sqrt{2D}\,dB_t\), and resetting times form an independent rate-\(r\) Poisson process. On each reset, \(X\) is sampled independently from \(\mathcal N(0,qD/\lambda)\). No restriction beyond \(\lambda,D,r>0\) and \(0<q<1\) is imposed. The comparison uses distributions **conditional on the duration of a single renewal interval**, not unconditional trajectories across intervals. A Gaussian variance calculation gives the stated \(u_q\). The standard centered-Gaussian Jeffreys formula gives
\[
G_q(s)=\frac12\left(\frac{u_q(s)}q+\frac q{u_q(s)}-2\right)
=\frac{(1-q)^2(1-e^{-s})^2}{2q[1-(1-q)e^{-s}]}.
\]
Set \(k=r/(2\lambda)\) and \(F_q(k)=\mathcal K_q(2\lambda k)/(2\lambda)\). Since \(2\lambda T_r\sim\operatorname{Exp}(k)\),
\[
F_q(k)=k^2\int_0^\infty e^{-ks}G_q(s)\,ds
=\frac{(1-q)^2k}{2q}\int_0^1\frac{y^k(1-y)[1+q-(1-q)y]}{[1-(1-q)y]^2}\,dy.
\]
The reference numerical normalization is dimensionless, so the result is independent of the particular positive value of \(D\).

## Proof

**1. Exact transform and derivative.** Let \(\delta=1-q\), \(y=e^{-s}\), \(u=1-\delta y\), and \(g_q(s)=G_q'(s)\). Differentiating the explicit Gaussian expression gives
\[
g_q(s)=\frac{\delta}{2q}\,y\left(1-\frac{q^2}{(1-\delta y)^2}\right)
=\frac{\delta^2}{2q}\frac{y(1-y)(1+q-\delta y)}{(1-\delta y)^2}.
\]
Both endpoints of \(g_q\) are zero, while \(g_q(s)>0\) for all \(s>0\). Successive integrations by parts (all boundary terms vanish, except the first derivative of the bounded \(G_q\)) show
\[
F_q(k)=k\int_0^\infty e^{-ks}g_q(s)\,ds
=\int_0^\infty e^{-ks}g_q'(s)\,ds,
\qquad
F_q'(k)=-\int_0^\infty se^{-ks}g_q'(s)\,ds.
\]
The integral in the finding follows by differentiation of the finite \(y\)-integral.

**2. A single sign change, hence a single optimum.** Write \(g_q(s)=\delta f_q(e^{-s})/(2q)\), where
\[
f_q(y)=y\left(1-\frac{q^2}{(1-\delta y)^2}\right),\qquad
f_q'(y)=1-\frac{q^2(1+\delta y)}{(1-\delta y)^3}.
\]
The quotient subtracted from 1 is strictly increasing in \(y\in[0,1]\): its logarithmic derivative is \(\delta/(1+\delta y)+3\delta/(1-\delta y)>0\). Moreover \(f_q'(0)=1-q^2>0\) and \(f_q'(1)=1-(2-q)/q<0\). Thus there is exactly one \(s_0>0\) with \(g_q'(s)>0\) for \(0<s<s_0\) and \(g_q'(s)<0\) for \(s>s_0\).

For \(k>0\) put
\[
A(k)=\int_0^{s_0}se^{-ks}g_q'(s)\,ds,\qquad
B(k)=-\int_{s_0}^\infty se^{-ks}g_q'(s)\,ds.
\]
Both are strictly positive and finite, and \(F_q'(k)=B(k)-A(k)\). Differentiation under these integrals yields
\[
\frac d{dk}\log\frac{A(k)}{B(k)}
=\frac{\int_{s_0}^\infty s^2e^{-ks}[-g_q'(s)]\,ds}{B(k)}
-\frac{\int_0^{s_0}s^2e^{-ks}g_q'(s)\,ds}{A(k)}>0,
\]
because the first weighted mean of \(s\) exceeds \(s_0\) and the second is smaller. At \(k\downarrow0\), integration by parts and bounded convergence give \(F_q'(0+)=G_q(\infty)=\delta^2/(2q)>0\). At \(k\to\infty\), using \(g_q'(0)=\delta^2/q^2>0\), the Laplace endpoint asymptotics give \(F_q'(k)=-\delta^2/(q^2k^2)+o(k^{-2})<0\). As \(A/B\) increases strictly, it crosses 1 exactly once. Since \(G_q\) is bounded, \(F_q(k)\sim kG_q(\infty)\to0\) for \(k\downarrow0\); and since \(G_q(s)=O(s^2)\) near zero, \(F_q(k)=O(k^{-1})\to0\) as \(k\to\infty\). Therefore this sole critical point is the unique strict global maximum.

**3. Near-equal reset and bath widths.** For \(\delta=1-q\), the exact integrand and \(q\le1-\delta e^{-s}\le1\) give, uniformly over \(k>0\),
\[
\delta^2 h(k)\le F_q(k)\le\frac{\delta^2}{q^2}h(k),
\qquad h(k)=\frac{k}{(k+1)(k+2)}.
\]
Indeed the reference Laplace integral is \((k^2/2)\int_0^\infty e^{-ks}(1-e^{-s})^2ds=h(k)\). The function \(h\) tends to zero at both ends and has derivative with numerator \(2-k^2\), hence its unique maximizer is \(\sqrt2\). The uniform multiplicative squeeze, together with uniqueness and strictness of the reference maximum, proves convergence of the maximizers and maxima stated above.

**4. Narrow reset width.** Define
\[
H_q(k)=\int_0^\infty\frac{e^{-z}}{1-(1-q)e^{-z/k}}\,dz.
\]
An exact algebraic rearrangement of the Gaussian expression, with \(z=ks\), gives
\[
F_q(k)=\frac1{2q}-\frac{1-q}{2q(k+1)}-\frac{k+1}{2}+\frac{kq}{2}H_q(k).
\]
Differentiating,
\[
F_q'(k)=\frac{1-q}{2q(k+1)^2}-\frac12+\frac q2\big(H_q(k)+kH_q'(k)\big).
\]
The integrand of \(H_q\) is nondecreasing with \(k\), and the pointwise inequality \((1-q)e^{-s}s\le1-(1-q)e^{-s}\) (which follows from \((1+s)e^{-s}\le1\)) proves \(0\le kH_q'(k)\le H_q(k)\).

Fix \(K>0\) and take \(k=K/\sqrt q\). If \(Z\) is exponential with mean one, then
\[
qH_q(K/\sqrt q)=\mathbb E\left[\frac q{1-(1-q)e^{-\sqrt q Z/K}}\right]\longrightarrow0,
\]
by dominated convergence: the integrand is between 0 and 1, and tends to zero for every \(Z>0\). In fact this convergence is locally uniform in \(K>0\), by monotonicity of \(H_q\). Hence
\[
F_q'(K/\sqrt q)\longrightarrow\frac1{2K^2}-\frac12,
\]
and
\[
F_q(K/\sqrt q)=\frac1{2q}-\frac{K+K^{-1}}{2\sqrt q}+o(q^{-1/2})
\]
locally uniformly in \(K>0\). The derivative has positive limiting sign for \(K<1\) and negative for \(K>1\); by the already-proved uniqueness of its zero, \(\sqrt q\,k_*(q)\to1\). Substitute this into the locally uniform expansion to obtain the second-order maximum. This also shows why a singular \(q=0\) calculation cannot replace taking the small-positive-\(q\) limit.

## Verification

The accompanying `verify.py` uses Python 3 with `mpmath>=1.3` and reproduces 36 numerical consistency checks. It compares two algebraically equivalent Laplace representations at six positive width ratios, verifies the derivative and strict local peak inequalities, and checks the stated asymptotic scales. Run `python verify.py` in the directory containing this file and the script. Numerical quadrature is not the proof of global uniqueness; the sign-change/Laplace-transform argument above proves that result for every \(0<q<1\).

## Relationship to prior work

Farago's 2026 resetting heat-engine work introduces finite-width harmonic resetting and the symmetric Gaussian endpoint KL expression, and derives approximate Poisson and periodic rates in a restricted teleportation regime. Those foundations, the Gaussian formula, Poisson averaging, the qualitative occurrence of a turnover, and earlier renewal descriptions are not claimed as new. The present claim is the **all-positive-width, all-rate uniqueness theorem** for the exactly specified conditional endpoint functional, plus the two sharp contrasting width-ratio asymptotics. It does not follow from the source's approximate \(q\ll1\), \(r t_c\ll1\) expression, which explicitly excludes its own very-fast-reset regime.

The general thermodynamic literature on physical erasure/reset work addresses other operationally defined functionals, not automatically the same conditional endpoint divergence. Earlier analyses of Gaussian reset-cycle scheduling optimize distributions of cycle lengths at a fixed mean, or identify two peaks in multiscale multidimensional examples. Neither asserts the present single-scale Poisson frequency theorem, and the latter highlights a physically meaningful boundary to uniqueness. No claim of mathematical independence from unlocated general total-positivity/variation-diminishing results is made; a generic theorem could offer an alternative proof.

## Limitations

The theorem concerns an ideal, instantaneous, independent Gaussian redraw and a conditional endpoint-divergence **diagnostic**. It is not a claim about energy consumption, realized heat, implementation-dependent entropy production, or stationary-mixture divergence. It assumes one harmonic relaxation scale and \(0<q<1\); at \(q=1\) the endpoint divergence vanishes for every rate and uniqueness is false. The zero-width case \(q=0\) is singular and is excluded. No optimization over renewal-time distributions or multidimensional reset protocols is asserted. Numerical checks only test selected parameters. Literature comparisons establish best-knowledge distinction, not absolute publication priority; independently checked scientific verification has not occurred.

## References

- O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, arXiv:2605.28445, first submitted 2026-05-27. https://arxiv.org/abs/2605.28445 (especially Sections II.1–II.3, Gaussian endpoint formula and Poissonian approximation).
- D. Gupta, K. S. Olsen, and S. Krishnamurthy, *Thermodynamic Cost of Recurrent Erasure*, Communications Physics 8, 355 (2025), arXiv:2502.06014. https://arxiv.org/abs/2502.06014 ; https://www.nature.com/articles/s42005-025-02277-w (operational physical resetting work, distinct objective).
- F. Mori, K. S. Olsen, and S. Krishnamurthy, *Entropy production of resetting processes*, Physical Review Research 5, 023103 (2023). https://doi.org/10.1103/PhysRevResearch.5.023103 (a different entropy-production observable).
- S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, New Journal of Physics 18, 033006 (2016) (renewal background).
