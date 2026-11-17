# Two resonance accumulation scales for conservative complex rocking

## Finding
For the conservative complex rocking system below, there are two distinct infinite families of **genuinely noncircular closed complex trajectories**. At any fixed parameter below the loss-of-well threshold, their normalized energies accumulate exponentially at the saddle barrier as the integer angular winding increases. At any fixed relative energy strictly inside the well, there are closed trajectories whose parameters accumulate at the well-disappearance threshold at an exact fourth-power rate. The latter rate has a complete elliptic-integral coefficient.

Write \(\beta_*=27/256\), and for \(0<\beta<\beta_*\) define
\[
V_\beta(r)=-\frac{r^2}{2}+r+\frac{\beta}{2r^2},\qquad
r''=-V_\beta'(r),\qquad
\psi'=\frac{\sqrt\beta}{r^2},\qquad Z=r e^{i\psi}.
\]
The prime denotes differentiation in the original dimensionless time, not a time-reparameterized polynomial compactification. Let \(r_m\in(0,3/4)\) be the unique potential minimum, \(r_s\in(3/4,1)\) its outer saddle, and set \(E_m=V_\beta(r_m)\), \(E_s=V_\beta(r_s)\). For each \(u\in(0,1)\), take the bounded radial orbit of energy
\[
E_\beta(u)=E_m+u(E_s-E_m),
\]
with least radial period \(T_\beta(u)\) and positive angular advance \(\Phi_\beta(u)\) in one radial period.

**Fixed parameter: exponential resonance accumulation.** For each fixed \(\beta\in(0,\beta_*)\), put
\[
\lambda_s=\sqrt{4-3/r_s},\qquad \Omega_s=\frac{\sqrt\beta}{r_s^2}.
\]
Then
\[
\Phi_\beta(u)=\frac{\Omega_s}{\lambda_s}\log\frac1{1-u}+O_\beta(1)
\quad (u\uparrow1).
\]
For every sufficiently large integer \(m\), there exists at least one \(u_m\in(0,1)\) giving \(\Phi_\beta(u_m)=2\pi m\), hence a closed, noncircular trajectory with least radial period and winding number \(m\). Any choices of such solutions satisfy
\[
\lim_{m\to\infty}\frac1m\log(1-u_m)
=-\frac{2\pi\lambda_s}{\Omega_s}.
\]

**Fixed relative energy: fourth-power parameter accumulation.** Fix \(u\in(0,1)\), and put \(\delta=\beta_*-\beta\). Define
\[
a=\frac{2\sqrt2}{3},\quad F(z)=\frac{64}{27}z-\frac89 z^3,\quad
c=F(a)=\frac{256\sqrt2}{243},\quad e_u=(2u-1)c.
\]
Let \(z_1<z_2<z_3\) be the three real roots of \(F(z)=e_u\), and let
\[
\mathsf K(m)=\int_0^{\pi/2}\frac{dt}{\sqrt{1-m\sin^2t}},\qquad
\mathcal T(u)=\frac{3}{\sqrt{z_3-z_1}}\,
\mathsf K\!\left(\frac{z_2-z_1}{z_3-z_1}\right).
\]
Then the actual time and angular advance obey
\[
\lim_{\beta\uparrow\beta_*}\delta^{1/4}T_\beta(u)=\mathcal T(u),\qquad
\lim_{\beta\uparrow\beta_*}\delta^{1/4}\Phi_\beta(u)=\frac{\mathcal T(u)}{\sqrt3}.
\]
For any fixed \(\beta_0\in(0,\beta_*)\) and every sufficiently large integer \(m\), there exists \(\beta_m\in(\beta_0,\beta_*)\) such that \(\Phi_{\beta_m}(u)=2\pi m\). Every choice of these solutions inside the stated fixed interval satisfies
\[
\boxed{\displaystyle
\beta_*-\beta_m\sim
\left(\frac{\mathcal T(u)}{2\pi\sqrt3}\right)^4 m^{-4}.}
\]
For example at \(u=1/2\),
\[
\mathcal T(1/2)=\frac{3\mathsf K(1/2)}{\sqrt{2\sqrt{8/3}}}
=3.07780638471545\ldots,
\]
and the fourth-power coefficient is \(0.00639739552266523\ldots\).

## Assumptions and scope
The equations are the conservative \(\gamma=0\), positive phase-momentum \(p=\sqrt\beta\) subfamily of the smooth radial complex-regularization model in Prieto-Castrillo, Pérez-González and Pérez del Río (2026). The radius is strictly positive. Each closed orbit concerns \(Z=r e^{i\psi}\), not the discontinuous physical rigid-block impact limit. The energy fraction \(u\) is normalized between the potential minimum and its outer barrier, and all limits use the model's original dimensionless time. No monotonicity or uniqueness of resonance parameters or resonance energies is claimed.

## Proof
**1. A compact period annulus and continuous angular return.** The equilibrium relation is
\[
V_\beta'(r)=\frac{r^3(1-r)-\beta}{r^3}=0.
\]
The cubic–quartic profile \(r^3(1-r)\) increases to its unique maximum \(27/256\) at \(r=3/4\), then decreases to zero at \(r=1\). Hence for the stated range there is one minimum \(r_m<3/4\) and one saddle \(r_s>3/4\), with \(V_\beta''(r_m)>0\), \(V_\beta''(r_s)<0\). For \(E_m<E<E_s\), the component of \(\frac12(r')^2+V_\beta(r)=E\) around the minimum has two simple turning points \(r_-<r_m<r_+<r_s\). Its least radial period and full angular return are exactly
\[
T=\sqrt2\int_{r_-}^{r_+}\frac{dr}{\sqrt{E-V_\beta(r)}},\qquad
\Phi=\sqrt{2\beta}\int_{r_-}^{r_+}
\frac{dr}{r^2\sqrt{E-V_\beta(r)}}.
\]
Replacing the integration variable by \(r=r_-+(r_+-r_-)\sin^2t\) removes both endpoint square roots. This shows continuity in \((\beta,u)\) on the open parameter rectangle and a finite positive extension at \(u=0\) for fixed \(\beta\). Closure after one radial cycle occurs precisely when \(\Phi\in2\pi\mathbb Z\). Since \(u>0\), the resulting complex trajectory is not circular; since the radius has minimal period \(T\), so does the closed complex trajectory.

**2. Fixed-parameter logarithmic saddle passage.** At fixed \(\beta\), expansion about the outer potential maximum gives
\[
V_\beta(r_s-h)=E_s-\tfrac12\lambda_s^2h^2+O(h^3),
\qquad \lambda_s^2=4-3/r_s>0.
\]
With \(\eta=E_s-E=(1-u)(E_s-E_m)\), the upper turning point has \(r_s-r_+=\sqrt{2\eta}/\lambda_s+O(\eta)\). Splitting the period integral at a fixed radius strictly below \(r_s\), and using a smooth nondegenerate-maximum coordinate, shows
\[
T=\lambda_s^{-1}\log(1/\eta)+O_\beta(1).
\]
The difference between \(\sqrt\beta/r^2\) and \(\Omega_s\) is \(O(r_s-r)\), whose weighted passage integral stays bounded. Thus \(\Phi=(\Omega_s/\lambda_s)\log(1/(1-u))+O_\beta(1)\). Continuity, boundedness on every \(0<u\le1-\epsilon\), and divergence at \(u=1\) yield a solution of \(\Phi=2\pi m\) for every large \(m\); all possible solution sequences tend to \(u=1\). Substitution in the logarithmic law proves the asserted exponent without presuming uniqueness.

**3. Saddle–center scaling.** Set \(r_*=3/4\), \(\delta=\beta_*-\beta\), and \(r=r_*+\sqrt\delta\,z\). Uniformly on compact \(z\)-intervals,
\[
V_\beta(r)=V_\beta(r_*)+\delta^{3/2}
\left(\frac{64}{27}z-\frac89z^3\right)+O(\delta^2).
\]
This follows directly by expanding \(V_\beta'(r)=(r^3(1-r)-\beta)/r^3\). The stable and unstable critical radii satisfy
\[
r_m=r_*-a\sqrt\delta+O(\delta),\qquad
r_s=r_*+a\sqrt\delta+O(\delta),
\]
and therefore \(E_s-E_m=2c\delta^{3/2}+O(\delta^2)\). At the energy \(E_m+u(E_s-E_m)\), the rescaled bounded turning points converge to \(z_1,z_2\); the third root \(z_3\) lies beyond the saddle. These roots are simple because \(0<u<1\).

Rescaling the original-time period quadrature gives
\[
\delta^{1/4}T_\beta(u)\longrightarrow
\sqrt2\int_{z_1}^{z_2}\frac{dz}{\sqrt{e_u-F(z)}}.
\]
The substitution by \(\sin^2t\) from Step 1 justifies dominated convergence, including the endpoints, since the limiting roots are simple. Factoring \(e_u-F(z)=\frac89(z-z_1)(z_2-z)(z_3-z)\) and reducing to Legendre normal form yields exactly \(\mathcal T(u)\) displayed above. Along these shrinking radial trajectories, \(\sqrt\beta/r^2\to \sqrt{\beta_*}/r_*^2=1/\sqrt3\) uniformly. Multiplying the period integral by this uniformly convergent angular speed gives \(\delta^{1/4}\Phi\to\mathcal T(u)/\sqrt3\).

**4. Closing and locating the critical sequence.** For any fixed \(u\in(0,1)\), \(\Phi_\beta(u)\) is continuous, finite at each \(\beta<\beta_*\), and tends to \(+\infty\) at \(\beta_*\). Choosing any fixed \(\beta_0\in(0,\beta_*)\) and applying the intermediate-value theorem gives, for every sufficiently large integer \(m\), a \(\beta_m\in(\beta_0,\beta_*)\) with \(\Phi_{\beta_m}(u)=2\pi m\). Every such solution must converge to \(\beta_*\), because the continuous return is bounded on every interval \([\beta_0,\beta_*-\epsilon]\) with \(0<\epsilon<\beta_*-\beta_0\). Inserting \(\Phi_{\beta_m}(u)\sim\mathcal T(u)(\beta_*-\beta_m)^{-1/4}/\sqrt3\) and solving yields the exact fourth-power coefficient. No global twist or monotonicity assertion is needed.

## Verification
The accompanying `verify_rocking_resonance.py` independently evaluates the exact finite-parameter radial turning points, period, and angular phase by high-precision quadratures of a factored quartic. It checks the elliptic scaling profile at three energy fractions, computes four closed noncircular winding resonances, and checks the fixed-parameter logarithmic slope. It uses `mpmath`; run `python verify_rocking_resonance.py` in the directory containing this file. The tests are finite corroboration of the proof, not a proof of the all-parameter limits.

## Relationship to prior work
Prieto-Castrillo, Pérez-González, and Pérez del Río (2026) derived the radial potential, its saddle–center boundary, and the rational angular-advance closure criterion; they did **not** derive an explicit sequence of closed trajectories, either resonance accumulation exponent, or the elliptic coefficient. General apsidal-angle treatments (Santos, Soares, and Tort, 2009; Castelli, 2015) cover central-force angle integrals and selected power-law families, not the parameter-specific coupled saddle–center scaling here. The general logarithmic saddle passage and cubic normal-form mechanism are standard and are not asserted to be new. The claimed addition is their exact combination in this newly studied complex rocking model, including both different resonance ladders and model-specific constants.

## Limitations
This result concerns the conservative smooth complex reconstruction, not a dissipative attractor or physical impacts. Neither uniqueness nor monotonicity of individual resonance branches is proved. The full historical priority of exact special-function treatments of related central-force systems is not certified; the 2005 original rocking article was not obtainable in full text in the accessible sources, leaving a limited comparison risk. No independent mathematical audit is asserted.

## References
- F. Prieto-Castrillo, S. Pérez-González, and J. S. Pérez del Río, *From Complex Regularization to Polynomial Flow: Capture and Escape in Rocking Dynamics* (2026), first public November 10, 2026, arXiv:2611.13861, https://arxiv.org/html/2611.13861v1 (especially equations 11, 33–39 and Sections 4–6).
- F. Prieto and P. B. Lourenço, *On the rocking behavior of rigid objects*, Meccanica 40 (2005), 121–133, DOI:10.1007/s11012-004-5875-z (original regularization; full-text comparison not available).
- F. C. Santos, V. Soares, and A. C. Tort, *Determination of the apsidal angles and Bertrand's theorem*, Physical Review E 79 (2009), 036605, https://doi.org/10.1103/PhysRevE.79.036605.
- R. Castelli, *The monotonicity of the apsidal angle in power-law potential systems* (2015), arXiv:1509.08662, https://arxiv.org/abs/1509.08662.
