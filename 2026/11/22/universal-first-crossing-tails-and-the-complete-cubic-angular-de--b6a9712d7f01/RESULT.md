# Universal first-crossing tails and the complete cubic angular-degeneracy spectrum

## Finding
Consider a planar polynomial star-node flow with a strictly radially contracting odd-degree homogeneous nonlinear part. In every forward angular sector born at an angular equilibrium of finite multiplicity, the **original-physical-time first crossing** of a fixed downstream ray has a universal sharp late-time law for initial conditions sampled on any compact radial annulus. The principal exponent is determined by the multiplicity of the upstream angular zero, and its leading constant depends on the local radial equilibrium but **not** on the radial starting distribution except for its total boundary density.

More precisely, under the assumptions below, put \(v_*=a_0/\lambda\), \(\rho_a=v_*^{-1/(2p)}\), and \(C_k=v_*/((k-1)c)\) when \(k\ge2\). Uniformly across every allowed starting radius, the first-crossing time \(T\) satisfies
\[
\lim_{\delta\downarrow0}\frac{T(r,\delta)}{\log(1/\delta)}=\frac{v_*}{c}\quad (k=1),
\qquad
\lim_{\delta\downarrow0}T(r,\delta)\,\delta^{k-1}=C_k\quad (k\ge2).
\]
For an initial angle-radius density \(w\) with positive integrated density \(q_0\) along the upstream ray, these uniform laws give
\[
\lim_{t\to\infty}\frac{\log\Pr(T>t)}t=-\frac{c}{v_*}\quad(k=1),
\qquad
\Pr(T>t)\sim q_0\,C_k^{1/(k-1)}t^{-1/(k-1)}\quad(k\ge2).
\]
Consequently, for every \(s>0\), all moments \(\mathbb E(T^s)\) are finite for \(k=1\); for \(k\ge2\), the moment is finite **if and only if** \(s<1/(k-1)\), and diverges at the endpoint as well as above it.

In the cubic case, the angular field is the restriction of a homogeneous quartic, so the finite-zero orders can be only \(1,2,3,4\), and **all four orders occur in explicit strictly contracting cubic polynomial flows**. For these examples, sampled with a uniform initial angle on a quadrant and any independent compactly supported positive radial distribution, the three heavy-tail exponents are exactly \(1,1/2,1/3\), with a fully explicit coefficient given below; the simple zero gives exponential rather than power-law first-crossing tails. The multiplicity ceiling and qualitative policycle types themselves are established background, not an originality claim.

## Assumptions and scope
Fix an integer \(p\ge1\), a real \(\lambda>0\), and a homogeneous real polynomial vector field \(Q:\mathbb R^2\to\mathbb R^2\) of degree \(2p+1\). For \(u_\theta=(\cos\theta,\sin\theta)\) and \(Ju_\theta=(-\sin\theta,\cos\theta)\), set
\[
 f(\theta)=\langle u_\theta,Q(u_\theta)\rangle,\qquad
 a(\theta)=-f(\theta),\qquad
 g(\theta)=\langle Ju_\theta,Q(u_\theta)\rangle.
\]
Assume \(a(\theta)>0\) for every real \(\theta\). Consider the original-time differential equation \(\dot z=\lambda z+Q(z)\). Choose two lifted real angular coordinates \(\theta_a<\theta_c<\theta_a+2\pi\) such that \(g(\theta_a)=0\), \(g(\theta)>0\) for every \(\theta\in(\theta_a,\theta_c]\), and for some integer \(k\ge1\) and real \(c>0\),
\[
 g(\theta_a+\delta)=c\delta^k+O(\delta^{k+1})\qquad(\delta\downarrow0).
\]
Fix real \(0<r_-<r_+<\infty\) and a real \(h\) with \(0<h<\theta_c-\theta_a\). The starting coordinates are \((r,\theta_a+\delta)\) with \(r\in I=[r_-,r_+]\) and \(0<\delta\le h\). The hitting time \(T(r,\delta)\) means the **first original physical time** that the continuously lifted angle reaches \(\theta_c\). We do not reparametrize physical time by angle in defining \(T\).

For ensemble statements let \(w(r,\theta)\) be a nonnegative continuous density with respect to the product coordinate measure \(dr\,d\theta\), normalized by \(\int_I\int_{\theta_a}^{\theta_a+h}w(r,\theta)\,d\theta\,dr=1\), and require
\[
 q_0=\int_I w(r,\theta_a)\,dr>0.
\]
If the initial law is specified with respect to Euclidean area, its polar Jacobian \(r\) must be absorbed into \(w\). All limits keep the polynomial, coefficients, downstream ray, radial interval and initial density fixed.

## Proof
**1. Polar and inverse-radial dynamics.** For every nonzero trajectory write \(z=r u_\theta\). Homogeneity gives the exact equations
\[
 \dot r=r(\lambda-a(\theta)r^{2p}),\qquad
 \dot\theta=r^{2p}g(\theta).
\]
Put \(v=r^{-2p}\). Crucially this removes the nonlinear radial power from the radial equation in **physical time**:
\[
 \dot v=-2p\lambda v+2p a(\theta),\qquad
 \dot\theta=\frac{g(\theta)}{v}.
\tag{1}
\]
Set \(a_{\min}=\min_\theta a(\theta)>0\) and \(a_{\max}=\max_\theta a(\theta)<\infty\). Variation of constants in (1), with \(r\in I\), places \(v(t)\) between the fixed positive constants
\[
 L=\min\{r_+^{-2p},a_{\min}/\lambda\},
 \qquad U=\max\{r_-^{-2p},a_{\max}/\lambda\}
\]
for all \(t\ge0\). These bounds prevent positive-radius degeneration and finite-time escape, uniformly across initial states. On the selected sector \(\dot\theta>0\), and \(d\theta/dt\ge g(\theta)/U\). Thus every \(\delta>0\) reaches \(\theta_c\) in finite time, with the entire crossing contained in the angular sector.

**2. Uniform equilibration close to the upstream ray.** Write \(a_0=a(\theta_a)>0\) and \(v_*=a_0/\lambda\). Fix an arbitrarily small \(\eta>0\). By continuity choose a fixed small angular window \([\theta_a,\theta_a+\varepsilon]\) so that \(|a(\theta)-a_0|<\eta\) there. While the solution remains in this window, the explicit variation-of-constants identity yields
\[
 |v(t)-v_*|\le |v(0)-v_*|e^{-2p\lambda t}+\frac{\eta}{\lambda}.
\tag{2}
\]
The initial difference is uniformly bounded for \(r\in I\). Therefore for any small desired error, there is a **fixed physical time** \(H\) independent of \(r,\delta\), after which the difference \(|v(t)-v_*|\) is as small as desired, provided the angle has not left the window. For sufficiently small \(\delta\), the angular trajectory remains inside the chosen window through \(H\), uniformly in \(r\), because \(g(\theta_a+\delta)\to0\) and \(v\ge L\). The angle \(\delta_H=\theta(H)-\theta_a\) is bounded above and below by fixed positive multiples of \(\delta\) when \(k=1\); for \(k\ge2\), the comparison \(\dot\delta=O(\delta^k)\) over a fixed physical interval gives \(\delta_H/\delta\to1\) uniformly. In either case the fixed initial physical time \(H\) does not affect the leading divergent crossing clock.

**3. Sharp flight-time integral.** At angular coordinate \(\theta\), equation (1) gives \(dt/d\theta=v/g(\theta)\). For the time from \(\theta_a+\delta_H\) to \(\theta_a+\varepsilon\), estimate (2) bounds \(v\) between \(v_*\) plus or minus an arbitrarily small error, and the zero expansion bounds \(g\) between \(c\xi^k\) times factors arbitrarily close to one, where \(\xi=\theta-\theta_a\). The remaining time from \(\theta_a+\varepsilon\) to \(\theta_c\) is bounded uniformly over the compact sector by \(U\int_{\theta_a+\varepsilon}^{\theta_c}d\theta/g(\theta)\). The divergent part is thus sandwiched between arbitrarily close multiples of
\[
 \frac{v_*}{c}\int_\delta^\varepsilon\xi^{-k}\,d\xi.
\]
When \(k=1\) this integral is \(\log(1/\delta)+O(1)\). When \(k\ge2\) it equals \(\delta^{1-k}/(k-1)+O(1)\). Letting \(\delta\downarrow0\), then making the relative error arbitrarily small, proves both asserted uniform first-crossing asymptotics. In particular the exponent and prefactor are unchanged by radial starting data within the compact annulus.

**4. Pushforward to the two-dimensional ensemble.** Let \(q(\delta)=\int_Iw(r,\theta_a+\delta)\,dr\). Continuity yields \(q(\delta)\to q_0>0\). The uniform first-crossing asymptotics imply that for any fixed relative error, and all sufficiently small \(\delta\), the survival event \(\{T>t\}\) is squeezed between the events where \(\delta\) is below the corresponding upper and lower inverse clocks. For \(k\ge2\) the inverse clock is \((C_k/t)^{1/(k-1)}\). Integrating \(q(\delta)\) over these small initial-angle intervals and letting the relative error vanish gives
\[
 \Pr(T>t)\sim q_0(C_k/t)^{1/(k-1)}.
\]
For \(k=1\), the uniform logarithmic clock yields \(\log\Pr(T>t)/t\to-c/v_*\), hence exponential upper and lower bounds on the survival probability with rates arbitrarily close to \(c/v_*\). Finally the tail-integral identity \(\mathbb E(T^s)=s\int_0^\infty t^{s-1}\Pr(T>t)dt\) establishes the exact moment threshold, including divergence at equality. All initial conditions with positive angular separation have finite individual crossing times; the heavy tails come solely from the density of starting points arbitrarily close to the invariant upstream ray.

**5. Complete realizable cubic spectrum.** For \(p=1\), the polynomial \(g\) is the restriction to the unit circle of the degree-four homogeneous polynomial \(\langle J(x,y),Q(x,y)\rangle\). In a nonsingular local slope coordinate a nonidentically zero homogeneous quartic has a finite zero of order at most four. Hence \(k\in\{1,2,3,4\}\). The **multiplicity classification is standard background**; the exact ensemble laws for these order types are the quantitative conclusion.

For each \(k\in\{1,2,3,4\}\) define
\[
 Q_k(x,y)=\bigl(-x(x^2+y^2),\;-y(x^2+y^2)+P_k(x,y)\bigr),
\]
where \(P_1=x^2y\), \(P_2=xy^2\), \(P_3=-x^2y\), \(P_4=x^3\). The angular polynomial is exactly \(xP_k\), and on the unit circle \(f_k=-1+yP_k\). For all four polynomials, \(|yP_k|\le3\sqrt3/16<1/3\) except the still smaller \(|x^2y^2|\le1/4\) terms. Consequently \(f_k<-2/3\) on the circle, proving strict radial contraction.

For \(k=1,2\) choose \(\theta_a=0\); for \(k=3,4\) choose \(\theta_a=\pi/2\). In every case take \(\theta_c=\theta_a+\pi/4\), with \(g_k>0\) throughout the intervening open sector and at its right endpoint. Direct trigonometric substitution gives the **exact** local identity
\[
 g_k(\theta_a+\delta)=\frac{\tan^k\delta}{(1+\tan^2\delta)^2},\qquad
 f_k(\theta_a)=-1.
\]
Thus \(a_0=c=1\), \(v_*=1/\lambda\), and \(C_k=1/((k-1)\lambda)\). If the starting angle is uniform on the open quadrant, independently of any radial law on \(I\), then \(q_0=4/\pi\). The resulting **exact leading tail coefficients** for \(k=2,3,4\) are
\[
 \boxed{\Pr(T>t)\sim\frac4\pi\left(\frac{1}{(k-1)\lambda}\right)^{1/(k-1)}t^{-1/(k-1)}.}
\]
For \(k=1\), the sharp logarithmic exponential rate is \(\lim_{t\to\infty}t^{-1}\log\Pr(T>t)=-\lambda\). This explicitly realizes all cubic nonzero finite-zero multiplicities as distinct physical-time first-passage tail regimes.

## Verification
The standalone Python 3 script `check.py` uses only the standard library. It checks the exact angular zero factorizations and strict contraction on sampled directions and independently integrates the physical-time inverse-radial and angular equations with a fourth-order Runge–Kutta method for all four cubic examples. Finite diagnostic crossings match the predicted scaled constants and print `VERIFY_OK`. Run `python3 check.py`. This is a diagnostic, not a proof: the uniform radial bounds, exact polar identity, analytic comparison and density pushforward above establish the infinite-time conclusions.

## Relationship to prior work
Alarcón, Castro and Labouriau [1] establish the invariant circle, radial contraction, angular phase portrait, nonhyperbolic equilibria and cubic zero-multiplicity taxonomy for the same class of flows. Those qualitative facts and the quartic multiplicity ceiling are **not claimed as new**. Earlier work by Bendjeddou, Llibre and Salhi [2] also studies homogeneous polynomial star-node systems. General saddle-node bottleneck slowdown exponents have been studied by Kuehn [3], and neither ordinary one-dimensional slowing nor a scalar inverse-power integral is claimed as an original mechanism.

A published result [4] gives exact original-time periods and Floquet exponents when the angular factor never vanishes. Other distinct published studies [5,6] examine time occupation along attracting periodic orbits as a strictly positive angular rotation rate approaches zero, including quadratic and quartic bottlenecks. Their hypotheses concern rotating cycles and stationary time samples, not first-crossing times from a genuine invariant source ray with a two-dimensional distribution of initial conditions. The contribution here is the **uniform annular initial-data law with sharp first-passage tail constants, moment cutoff and complete explicitly realized cubic spectrum**. No claim of novelty for the phase portrait or generic delay exponents is made.

## Limitations
This theorem concerns deterministic forward first-crossing times, not stochastic noise, long-run invariant-probability laws, or the residence-time distribution along a periodic orbit. It requires radial strict contraction, a compact positive radial starting interval, a nonzero finite-order angular source zero with no other zeros before the target ray, and positive continuous boundary density. A density vanishing at the source can change the tail exponent. The coefficient of an exact exponential tail at a simple angular zero is not claimed, only its sharp logarithmic rate. A prior general theorem on parabolic waiting-time ensembles could subsume parts of the pushforward argument; publication priority remains subject to further expert comparison. No independent mathematical audit has been performed.

## References
1. B. Alarcón, S. B. S. D. Castro and I. S. Labouriau, *Global planar dynamics with a star node and contracting nonlinearity*, arXiv:2307.16020v1 (first posted July 29, 2023), https://arxiv.org/abs/2307.16020 ; full open preprint https://arxiv.org/html/2307.16020v2 ; journal https://doi.org/10.1007/s40687-024-00427-0 .
2. A. Bendjeddou, J. Llibre and T. Salhi, *Dynamics of the polynomial differential systems with homogeneous nonlinearities and a star node*, Journal of Differential Equations 254 (2013), 3530–3537, https://doi.org/10.1016/j.jde.2013.01.032 .
3. C. Kuehn, *Scaling of Saddle-Node Bifurcations: Degeneracies and Rapid Quantitative Changes*, arXiv:0807.1546 (2008), https://arxiv.org/abs/0807.1546 .
4. *Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-angular-return-and-physical-time-floquet-rigidity-for-cont--7c00337eaa41 .
5. *Four-gate physical-time concentration with unequal residence weights in a cubic star-node oscillator*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-four-gate-physical-time-concentration-with-unequal-residence-wei--41d1dd3d23ee .
6. *A quartic depinning cusp and a resolved physical-time occupation law for a contracting cubic star-node flow*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-quartic-depinning-cusp-and-a-resolved-physical-time-occupation--ca713ddee5f9 .
