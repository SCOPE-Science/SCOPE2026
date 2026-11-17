# Density-gradient impulse and a renormalized collision clock for a gravitational segment

## Finding

Consider a finite, fixed material segment with strictly positive \(C^1\) line density. At **every finite-time collision into an interior point**, the transverse speed has a finite renormalized kinetic-energy limit, the remaining flight time has an explicit two-term logarithmic expansion, and the tangential velocity has a smaller, universal logarithmic impulse determined by the derivative of the density at the impact point. These assertions hold for arbitrary colliding initial energy and do not require an invariant equatorial plane or a symmetric density.

More precisely, choose nondimensional length and time units and let \(a<b\), \(G>0\), and \(\sigma\in C^1([a,b])\) satisfy \(\min\sigma>0\). The Newtonian potential of the segment is
\[
U(x,\rho)=-G\int_a^b\frac{\sigma(s)}{\sqrt{(s-x)^2+\rho^2}}\,ds,\qquad\rho>0.
\]
A collision trajectory, after its invariant-plane reduction, solves \(\ddot x=-U_x\), \(\ddot\rho=-U_\rho\) and has conserved energy \(H=\frac12(\dot x^2+\dot\rho^2)+U\). Suppose its maximal forward time \(T<\infty\) satisfies \((x(t),\rho(t))\to(x_*,0)\) with \(a<x_*<b\), approaching on one side so that \(\rho(t)>0\) just before \(T\).

Define, with dimensionless arguments,
\[
L=\log(1/\rho),\quad u=T-t,\quad A=4G\sigma(x_*),
\]
\[
B_*=\sigma(x_*)\log\!\left(4(x_*-a)(b-x_*)\right)
+\int_a^b\frac{\sigma(s)-\sigma(x_*)}{|s-x_*|}\,ds.
\]
The integral is absolutely convergent, with the integrand continuously extended at \(s=x_*\) on each side. Then the finite terminal tangential speed \(v_*:=\lim_{t\uparrow T}\dot x(t)\in\mathbb R\) exists. With \(C=2H+2GB_*-v_*^2\), the following **single impact-asymptotics theorem** holds:
\[
\boxed{\dot\rho(t)^2=A L+C+o(1)},\qquad
\boxed{u=\frac{\rho}{\sqrt{A L}}\left[1-\frac{1+C/A}{2L}+o(L^{-1})\right]},
\]
\[
\boxed{\lim_{t\uparrow T}\frac{v_*-\dot x(t)}{u\log(1/u)}=2G\sigma'(x_*)},
\qquad
\boxed{\lim_{t\uparrow T}\frac{x(t)-x_*+v_*u}{u^2\log(1/u)}=G\sigma'(x_*)}.
\]
In particular, \(\dot\rho<0\) eventually and \(\dot x/\dot\rho\to0\): the final approach is normal to the segment even though the tangential speed need not vanish. The coefficient of the tangential logarithmic correction depends only on the **local density gradient**; the transverse clock's next coefficient also records the **whole segment** through the finite part \(B_*\), together with the trajectory's energy and terminal tangential speed.

## Assumptions and scope

The source is a fixed straight segment in three-dimensional Euclidean space with Newtonian kernel \(1/r\), not a point mass, rotating rod, softened force, or surface-density model. A collision has zero conserved axial angular momentum and is planar, as established in the cited source; the theorem is stated in that invariant plane. Coordinates are fixed with the rod horizontal. Taking \(\rho>0\) loses no generality because the two sides are related by reflection. The density is differentiable with continuous derivative on the **closed** segment. Only interior impact points \(x_*\in(a,b)\) are covered. No assumption is made about the sign of the energy or the initial tangential velocity. The asymptotics are pointwise along each colliding orbit, not uniform over a family of initial conditions or over contact points approaching an endpoint.

All logarithms use fixed nondimensional units. Changing the reference length shifts \(L\) and \(B_*\) consistently, leaving the physical expansion invariant. The reference time in \(\log(1/u)\) changes only lower-order terms.

## Proof

**1. Transverse force and first scale.** Hamilton's equations give the exact identities
\[
\ddot\rho=-G\rho\int_a^b\frac{\sigma(s)}{((s-x)^2+\rho^2)^{3/2}}\,ds<0,
\]
\[
\ddot x=G\int_a^b\frac{\sigma(s)(s-x)}{((s-x)^2+\rho^2)^{3/2}}\,ds.
\]
Since \(x(t)\to x_*\in(a,b)\), the scaled substitution \(s=x+\rho y\) and dominated convergence yield
\[
\rho\ddot\rho\longrightarrow-2G\sigma(x_*),
\]
using \(\int_{\mathbb R}(1+y^2)^{-3/2}\,dy=2\). Because \(\rho(t)\downarrow0\) at finite \(T\) and \(\ddot\rho<0\), its velocity is eventually negative. Write \(w=-\dot\rho>0\). The exact differential identity along this monotone branch is \(d(w^2)/d\rho=2\ddot\rho\). Integration between a fixed small radius and \(\rho\) therefore gives
\[
\dot\rho^2=4G\sigma(x_*)\log(1/\rho)+o(\log(1/\rho)).
\]
(The error is the integral of a function tending to zero against \(d\rho/\rho\).) Consequently, integrating \(dt=-d\rho/w\) implies
\[
u\sim\frac{\rho}{\sqrt{A\log(1/\rho)}}.
\]
The last relation can be proved directly by sandwiching \(w\) between \((1\pm\varepsilon)\sqrt{A\log(1/\rho)}\) at small radii and substituting \(s=\rho y\).

**2. Logarithmic axial force and existence of terminal velocity.** Fix a neighborhood of \(x_*\) contained strictly inside the material interval. For \(x\) in this neighborhood, split the axial force integral at \(|s-x|=\delta\), where \(\delta>0\) is fixed and small. The odd integral of the constant term \(\sigma(x)\) on \([-\delta,\delta]\) vanishes. Uniformly in this neighborhood,
\[
\sigma(x+h)-\sigma(x)=\sigma'(x)h+o(|h|)\quad(h\to0).
\]
The linear term contributes
\[
G\sigma'(x)\int_{-\delta}^{\delta}\frac{h^2}{(h^2+\rho^2)^{3/2}}\,dh
=2G\sigma'(x)\log(1/\rho)+O(1).
\]
The remainder contributes \(o(\log(1/\rho))\), by splitting once more into \(|h|<\eta\) and \(\eta\le|h|\le\delta\) and sending \(\eta\downarrow0\); the outside integral is bounded. Thus
\[
\ddot x=2G\sigma'(x_*)\log(1/\rho)+o(\log(1/\rho))
\]
and, in particular, \(|\ddot x|\le K(1+\log(1/\rho))\) close to collision. By Step 1,
\[
\int^{T}|\ddot x(t)|\,dt
\le K'\int_0^{\rho_0}\frac{1+\log(1/r)}{\sqrt{\log(1/r)}}\,dr<\infty
\]
for a sufficiently small fixed \(\rho_0\). Hence \(\dot x(t)\to v_*\in\mathbb R\). Since the remaining time is \(u\), \(|x(t)-x_*|=O(u)=O(\rho/\sqrt L)\), and therefore \((\sigma(x(t))-\sigma(x_*))L\to0\).

**3. Uniform finite-part expansion of the potential.** For \(x\) near \(x_*\), write
\[
\begin{aligned}
\int_a^b\frac{\sigma(s)}{\sqrt{(s-x)^2+\rho^2}}\,ds
={}&\sigma(x)\left[\operatorname{arsinh}\!\left(\frac{b-x}{\rho}\right)+\operatorname{arsinh}\!\left(\frac{x-a}{\rho}\right)\right]\\
&+\int_a^b\frac{\sigma(s)-\sigma(x)}{\sqrt{(s-x)^2+\rho^2}}\,ds.
\end{aligned}
\]
The first line is \(2\sigma(x)L+\sigma(x)\log(4(b-x)(x-a))+o(1)\). The second converges, uniformly for \(x\) near \(x_*\), to \(\int_a^b(\sigma(s)-\sigma(x))/|s-x|\,ds\). Indeed, \(C^1\) regularity bounds the numerator by \(\|\sigma'\|_\infty|s-x|\), so dominated convergence applies, and the limiting integral is continuous in \(x\) by a fixed-interval local split. Substituting the estimate from Step 2 gives
\[
U(x(t),\rho(t))=-2G\sigma(x_*)L-GB_*+o(1).
\]
Now conserve \(H=\frac12(\dot x^2+\dot\rho^2)+U\), use \(\dot x\to v_*\), and rearrange to obtain
\[
\dot\rho^2=A L+2H+2GB_*-v_*^2+o(1)=A L+C+o(1).
\]
This proves the finite renormalized transverse kinetic energy, including its constant coefficient.

**4. Second-order clock.** As \(\dot\rho<0\) close to collision, the remaining time is
\[
u=\int_0^\rho\frac{dr}{\sqrt{A\log(1/r)+C+o(1)}}.
\]
The error is uniform as \(0<r\le\rho\) when \(\rho\downarrow0\). Substitute \(r=\rho y\). Expanding at large \(L\), and using \(\int_0^1\log(1/y)\,dy=1\), yields
\[
\int_0^1\left(1+\frac{\log(1/y)+C/A+o(1)}{L}\right)^{-1/2}\,dy
=1-\frac{1+C/A}{2L}+o(L^{-1}).
\]
To justify the expansion under the integral, split at \(y=e^{-\sqrt L}\); the small portion is exponentially negligible, while Taylor's remainder on the other portion is dominated by a fixed multiple of \((1+\log(1/y))^2/L^2\), whose integral is finite. This proves the clock formula.

**5. Axial impulse and position.** From Step 1, \(u\sim\rho/\sqrt{A L}\), so \(\log(1/\rho)/\log(1/u)\to1\). Step 2 becomes \(\ddot x=2G\sigma'(x_*)\log(1/u)+o(\log(1/u))\). Time integration from \(t\) to \(T\), using the integrability of the acceleration and \(\int_0^u\log(1/s)\,ds=u\log(1/u)+u\), gives
\[
v_*-\dot x(t)=2G\sigma'(x_*)u\log(1/u)+o(u\log(1/u)).
\]
A second integration, \(\int_0^u s\log(1/s)\,ds=\frac12u^2\log(1/u)+\frac14u^2\), gives
\[
x(t)-x_*+v_*u=G\sigma'(x_*)u^2\log(1/u)+o(u^2\log(1/u)).
\]
All four assertions are proved.

## Verification

A standalone checker, `check_impact.py`, provides two finite cross-checks. First, it compares exact elementary potential/force formulas for a linear density \(\sigma(s)=1+0.35s\) on \([-1,1]\) with independent numerical quadrature at four interior points. Second, it integrates an inward-colliding trajectory in the logarithmic radius \(z=\log(\rho_0/\rho)\), for which the stiff final radial scale is resolved without integrating through the singular endpoint. It compares the predicted finite part \(C\) of \(\dot\rho^2-A\log(1/\rho)\) and the coefficient \(2G\sigma'(x_*)\) of the tangential acceleration at four scales. Run `python check_impact.py` with NumPy and SciPy installed. The program prints `VERIFY_OK` when its algebraic/finite tests pass. It is not a substitute for the infinite-time argument above.

For that test, the asymptotic constants are approximately \(A=4.009095885536\), \(B_*=1.384856503375\), and \(C=-7.523155644583\); the final contact point is approximately \(x_*=0.006497061097\). The numerical value of the terminal speed and the finite-part constant depend on the initial condition. All printed digits are numerical, not exact closed forms.

## Relationship to prior work

Crespo, Martínez, Vidarte, Zapata and Abdrabou (arXiv:2611.08625v1, November 5, 2026) establish the planar reduction, classify finite-time singularities, and prove the interior collision force limit \(\rho\ddot\rho\to-2G\sigma(x_*)\) and normal-incidence velocity ratio \(\dot x/\dot\rho\to0\) in Theorem 5.5. These are credited as prerequisites. Their Sections 5–5.1 give a one-sided linear collision-time bound and, for homogeneous density, a conditional quadratic bound; they do not state the finite renormalized kinetic constant, the second-order logarithmic flight-time correction, or the density-derivative tangential impulse proved here. The difference is one of exact dynamical observables, not just terminology.

Martínez's earlier AAS 24-333 conference manuscript develops a closed form for *linear* density and singularity/relative-equilibrium results, but the inspected fixed-segment singularity section does not provide these impact asymptotics. Alberti and Vidal (2010) treat singularities with constant density; that paper was verifiable at the journal abstract level but its full text could not be accessed here, so historical priority relative to it is not completely resolved. Further general singular-potential asymptotic literature could also subsume individual intermediate lemmas. The full variable-density tangential impulse and explicit global-density clock coefficient are the comparisons relevant to this result.

## Limitations

The theorem is conditional on finite-time **interior** collision; it does not prove a global collision basin, endpoint-impact law, uniformity as the contact point approaches an endpoint, or the possibility of a post-collision continuation. At merely continuous density the finite terminal axial velocity and the finite potential part need not follow from this proof. No claim is made for rotating line distributions or nonsymmetric three-dimensional motions with nonzero axial angular momentum. The leading radial \(\sqrt{\log}\) law alone is directly accessible from the source's force limit; the contribution assessed here is the combined finite-part clock and density-gradient tangential signature under \(C^1\) regularity. Historical priority is provisional and no independent mathematical audit has occurred.

## References

1. F. Crespo, E. Martínez, J. Vidarte, J. L. Zapata and A. Abdrabou, *Singularities and Collision Criteria in the Gravitational Straight-Segment Problem with Arbitrary Positive Density*, arXiv:2611.08625v1 (first posted November 5, 2026), especially §2 and Theorem 5.5. https://arxiv.org/html/2611.08625v1
2. E. Martínez, *Dynamics of a Particle around a Non-Homogeneous Straight Segment*, AAS 24-333, Astrodynamics Specialist Conference (2024), publicly uploaded February 5, 2025. https://www.researchgate.net/publication/388722631_DYNAMICS_OF_A_PARTICLE_AROUND_A_NON-HOMOGENEOUS_STRAIGHT_SEGMENT
3. A. Alberti and C. Vidal, *Singularities in the gravitational attraction problem due to massive bodies*, Discrete & Continuous Dynamical Systems 26 (2010), 805–822. DOI: 10.3934/dcds.2010.26.805. https://www.aimsciences.org/article/doi/10.3934/dcds.2010.26.805
