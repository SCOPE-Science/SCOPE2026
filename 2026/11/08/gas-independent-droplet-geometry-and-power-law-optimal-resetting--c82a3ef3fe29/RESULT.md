# Gas-independent droplet geometry and power-law optimal resetting in active matter

## Finding

For the one-dimensional two-velocity local-reset continuum model with a dilute gas and a dense central phase, the positive spatial mass flux is a complete coordinate on every monotone stationary branch. When the interface has a prescribed matched flux, the gas **does not determine** the dense-droplet width or dense mass: it only fixes the gas density profile outside the interface.

For a broad class of gas and liquid constitutive functions, put
\[
\Gamma=\sqrt{r(r+\alpha)},\qquad F_*=F_g(g)=F_\ell(\ell)>0,\qquad
\Gamma_c=\frac{2F_*}{M}.
\]
The unique symmetric decreasing two-phase profile in the specified class exists precisely for \(\Gamma>\Gamma_c\). If \(\rho_0\) is the density at the origin on the right, then
\[
F_\ell(\rho_0)=\frac{\Gamma M}{2},\qquad
b=\frac{1}{\Gamma}\int_\ell^{\rho_0}\frac{F_\ell'(u)}{u}\,du,\qquad
M_{\rm gas}=\frac{2F_*}{\Gamma},\qquad
M_{\rm dense}=M-\frac{2F_*}{\Gamma}.
\]

In particular, for \(F_\ell(u)=cu^p\) with \(c>0\), \(0<p\leq 1\), the dense-phase speed \(v_\ell(u)=cu^{p-1}\) is nonincreasing. For \(t=\Gamma/\Gamma_c>1\),
\[
b_p(t)=
\begin{cases}
\displaystyle\frac{cp\ell^{p-1}}{\Gamma_c(p-1)}
\left(t^{-1/p}-t^{-1}\right),&0<p<1,\\
\displaystyle\frac{c}{\Gamma_c}\frac{\log t}{t},&p=1.
\end{cases}
\]
Each width is strictly positive, vanishes at both ends of the interval \(1<t<\infty\), and has exactly one maximum:
\[
t_*(p)=p^{p/(p-1)}\quad(0<p<1),\qquad t_*(1)=e.
\]
The function \(p\mapsto t_*(p)\) increases strictly from \(1\) to \(e\), so the optimizing normalized rate is not universally \(e\) once the dense-core speed is allowed to decrease with density. In particular \(t_*(1/2)=2\).

## Assumptions and scope

Fix \(M,\alpha,r>0\), a liquid-side interface density \(\ell>0\), and a gas-side interface density \(g\in(0,\ell)\). Assume:

1. \(F_\ell:[\ell,\infty)\to(0,\infty)\) is continuously differentiable, \(F_\ell'(u)>0\) and \(\lim_{u\to\infty}F_\ell(u)=\infty\).
2. \(F_g:[0,g]\to[0,\infty)\) is continuously differentiable, \(F_g(0)=0\), \(F_g'(u)>0\) throughout \([0,g]\), including \(F_g'(0)>0\).
3. The interface fluxes match: \(F_\ell(\ell)=F_g(g)=F_*>0\). The gas branch is sampled only on \([0,g]\), the liquid branch only on \([\ell,\infty)\); the density jump from \(\ell\) to \(g\) is permitted.
4. The stationary state is even in total density, has an odd directional polarization, a single dense interval \([-b,b]\) with \(b>0\), and strictly decreasing density for \(x>0\). It decays to zero at spatial infinity. Its total mass is \(M\).
5. On each smooth phase and away from the resetting origin, the directional densities satisfy the stationary modified telegrapher equations
\[
0=-\partial_x(v\rho_+)-\frac\alpha2(\rho_+-\rho_-)-r\rho_+,
\qquad
0=+\partial_x(v\rho_-)+\frac\alpha2(\rho_+-\rho_-)-r\rho_-,
\]
where \(v=F_\ell(\rho)/\rho\) in the dense region and \(v=F_g(\rho)/\rho\) in the gas. The directional **transport fluxes** are continuous at the interfaces (there are no singular sources there). At \(x=0\), the mass removed by resetting is re-injected with equal probability into either direction, with a point-source rate \(rM\).

The theorem is a classification **within this phase arrangement**. It does not establish that every microscopic active-particle model produces this constitutive equation, or that the two-phase branch is dynamically selected.

## Proof

Define total density and polarization by \(\rho=\rho_++\rho_-\) and \(\sigma=\rho_+-\rho_-\). Let \(R=v(\rho)\rho=F(\rho)\) and \(S=v(\rho)\sigma\). Summing and subtracting the two stationary equations yields
\[
S'=-r\rho,\qquad R'=-(r+\alpha)\sigma.
\]
The first integral is
\[
\frac{d}{dx}\bigl(S^2-q^2R^2\bigr)=0,\qquad
q=\sqrt{\frac r{r+\alpha}}.
\]
In the far-field gas, \(R,S\to0\), hence the constant is zero. Since \(S'=-r\rho<0\) and \(S(\infty)=0\), the outward flux \(S>0\) on \(x>0\), which forces \(S=qR\) and \(\sigma=q\rho\) in the gas. Continuity of directional transport fluxes means continuity of both \(R\) and \(S\) at \(x=b\). The liquid first integral therefore also vanishes, with the same positive sign of \(S\), so
\[
S=qR,\quad \sigma=q\rho,\quad
R'=-(r+\alpha)q\rho=-\Gamma\rho
\]
throughout \(x>0\). Conversely these three identities imply both original stationary equations: \(S'=-q\Gamma\rho=-r\rho\) because \(q\Gamma=r\).

Integrating \(R'=-\Gamma\rho\) from the origin to infinity and using symmetry and total mass gives \(R(0^+)=\Gamma M/2\). A positive-width dense interval exists exactly when \(R(0^+)>R(b^-)=F_*\). As \(F_\ell\) is strictly increasing onto \([F_*,\infty)\), this is equivalent to \(\Gamma M/2>F_*\), and uniquely determines \(\rho_0>\ell\) by \(F_\ell(\rho_0)=\Gamma M/2\).

On either phase, the inverse-flux equation reads
\[
\frac{d\rho}{dx}=-\Gamma\frac{\rho}{F'(\rho)}.
\]
The strictly monotone liquid solution is therefore uniquely specified by
\[
\Gamma(b-x)=\int_\ell^{\rho(x)}\frac{F_\ell'(u)}u\,du,
\qquad 0\le x\le b.
\]
Putting \(x=0\) yields the claimed formula for \(b\). On the gas side it is uniquely given by
\[
\Gamma(x-b)=\int_{\rho(x)}^g\frac{F_g'(u)}u\,du,\qquad x\ge b.
\]
Since \(F_g'(0)>0\), the integral diverges logarithmically as \(\rho\downarrow0\); this solution is defined for every \(x\ge b\) and decays to zero. Flux matching gives \(R(b^-)=R(b^+)=F_*\), and \(S=qR\) ensures that both directional transport fluxes match.

Change variables using \(\rho\,dx=-F'(\rho)\,d\rho/\Gamma\). The one-sided gas mass is
\[
\int_b^\infty\rho(x)\,dx
=\frac{F_g(g)-F_g(0)}{\Gamma}
=\frac{F_*}{\Gamma}.
\]
The one-sided liquid mass is
\[
\int_0^b\rho(x)\,dx
=\frac{F_\ell(\rho_0)-F_\ell(\ell)}{\Gamma}
=\frac{M}{2}-\frac{F_*}{\Gamma}.
\]
These identities prove normalization and show that the gas law cannot affect \(b,\rho_0\), or the liquid mass as long as the matched contact flux remains fixed. At the origin, \(S(0^+)=q\Gamma M/2=rM/2\), and odd reflection gives the correct current jump \(rM\). Each directional transport flux has jump \(rM/2\), matching equal-probability direction assignment for the point re-injection. All directional densities are nonnegative because \(0<q<1\) and \(\rho_\pm=(1\pm q)\rho/2\) on \(x>0\), with the signs swapped on \(x<0\).

For \(F_\ell(u)=cu^p\), the center relation gives \(\rho_0=\ell t^{1/p}\). Direct integration produces the displayed \(b_p(t)\). For \(0<p<1\), differentiating \(t^{-1/p}-t^{-1}\) shows that the derivative changes sign only when \(t^{(p-1)/p}=p\). It is positive before and negative after \(t_*(p)=p^{p/(p-1)}\), because \(b_p(t)\) is positive and vanishes at the two endpoints. For \(p=1\), differentiation of \(\log(t)/t\) gives the unique maximum at \(t=e\). Finally,
\[
\frac{d}{dp}\log t_*(p)
=\frac{p-1-\log p}{(p-1)^2}>0\qquad(0<p<1)
\]
by the strict logarithm inequality \(\log p<p-1\). The limits follow from \(p\log p\to0\) at zero and l'Hôpital's rule at one. As \(\Gamma=\sqrt{r(r+\alpha)}\) is strictly increasing in \(r>0\), the unique optimizing reset rate is
\[
r_*=\frac{\sqrt{\alpha^2+4\Gamma_c^2t_*^2}-\alpha}{2}.
\]
This completes the claimed existence, uniqueness within the phase arrangement, flux independence, and optimal-rate classification.

## Verification

A standalone deterministic checker, `check_flux_core.py`, computes the flux integrals and verifies analytic mass and flux identities for dense-core exponents \(p=1/2,3/4,1\), twelve positive activity ratios, and two different dilute-gas flux functions (linear and nonlinear rational functions). It also checks three locations within each phase and the unique-maximizer inequalities. The checked computation reports 570 passed scalar assertions. Run `python check_flux_core.py`; Python 3.10+ and SciPy are required. The infinite classes and strict uniqueness statements are established by the proof, not finite numerical tests.

For a concrete distinct-gas comparison, take \(\ell=2\), \(g=2/5\), \(F_\ell(u)=1.1\,u^{1/2}\), and \(F_*=1.1\sqrt2\). Both
\[
F_g^{(1)}(u)=F_*\frac ug,\qquad
F_g^{(2)}(u)=F_*\frac{(1+g)u}{g(1+u)}
\]
satisfy the gas conditions and have different spatial profiles, but for fixed \(M,\alpha,r\) they have exactly the same dense center, width, and mass. The optimal normalized \(\Gamma\) is \(2\), not \(e\), for both.

## Relationship to prior work

Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, arXiv:2610.26149 (first posted 19 October 2026), introduces the same steady modified-telegrapher system and derives its flux first integral for arbitrary speed in Section 2. Sections 3 and 5 solve a particular piecewise slowdown, using **constant dense-phase speed** (hence **linear dense flux**). In that specialization the paper obtains the logarithmic droplet width and the optimum ratio \(e\). The present finding does **not** claim the steady equations, first integral, general resetting motivation, or the linear-core optimum as new.

The extension studied here changes the core flux itself and proves a general inverse-flux construction, a gas-law invariance principle at fixed matched flux, and a continuously variable sharp optimal-rate ratio for the decreasing-speed power-law family. The existing constant-core result is precisely the endpoint \(p=1\). Previous studies of local resetting on exclusion lattices and general density-dependent run-and-tumble motility provide related physical context, but do not supply an identified stronger result implying this power-law normalized optimum.

## Limitations

The classification is restricted to piecewise smooth, symmetric, decreasing, single-core stationary solutions with a fixed matched interface flux. Interface densities and coexistence are imposed constitutive inputs, not inferred from a microscopic phase-equilibrium free-energy criterion. Gas flux shape cannot affect the stated observables *when its contact flux and both interface densities satisfy the assumptions*; changing the contact flux may alter them. No claim is made about multibranch gas laws, unbounded gas densities, nonmonotone fluxes, other stationary arrangements, metastability, dynamical selection, fluctuations, stability or finite-particle microscopic convergence. The 2026 starting paper already provides the general conserved first-integral equation, making part of the construction accessible by extension; an unindexed subsequent derivation for nonlinear dense fluxes remains a priority risk.

## References

1. P. Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, arXiv:2610.26149, version 1 first posted 19 October 2026; version 2 posted 20 October 2026. https://arxiv.org/abs/2610.26149 (full HTML sections 2–5 and appendices examined).
2. A. G. Thompson, J. Tailleur, M. E. Cates and R. A. Blythe, *Lattice models of nonequilibrium bacterial dynamics*, Journal of Statistical Mechanics P02029 (2011), doi:10.1088/1742-5468/2011/02/P02029 (bibliographic record and abstract examined).
3. A. Pelizzola, M. Pretti and M. Zamparo, *Simple exclusion processes with local resetting*, Europhysics Letters 133, 60003 (2021) (repository record and abstract examined).
