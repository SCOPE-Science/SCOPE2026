# Two periodic annuli born at a sharp quadratic-torus threshold, with a surviving weighted area and arcsine latitude law

## Finding

Fix any real \(a>1\), any real \(b,c\) with \(b^2+c^2>0\), and any real \(d\). Consider the homogeneous quadratic polynomial vector field
\[
\dot x=(bx+cy+dz)y,\qquad \dot y=-(bx+cy+dz)x,\qquad \dot z=0
\]
on the smooth invariant algebraic torus
\[
\mathcal T_a=\{(x,y,z)\in\mathbb R^3:(x^2+y^2-a^2)^2+z^2=1\}.
\]
Set \(s=a^2>1\), \(R=\sqrt{b^2+c^2}>0\), \(\eta=|d|/R\), \(\tau=\sqrt{s^2-1}\), and
\[
\eta_*^2=\frac{s+\tau}{2},\qquad u_*=-s+\tau,\qquad v_*=\sqrt{1-u_*^2}>0.
\]
Then the following assertions all hold in *original physical time*.

**Exact existence threshold and global classification.** If \(\eta\le\eta_*\), there is no nonstationary periodic trajectory on \(\mathcal T_a\). If \(\eta>\eta_*\), there are exactly two connected open annuli containing nonstationary periodic trajectories, one with \(z>0\) and one with \(z<0\). Each annulus is foliated by simple closed periodic latitude circles. Every other latitude contains equilibria and no nonstationary periodic trajectory. At the threshold there are exactly two degenerate-equilibrium latitude circles, and above it there are exactly four annular boundary latitude circles containing equilibria.

**Exact periods and critical scaling.** Write \(u=\cos\theta\) in the standard torus parametrization given below. A latitude is periodic precisely when
\[
F_\eta(u):=\eta^2(1-u^2)-s-u>0,
\]
and its minimal physical period is \(T_\eta(u)=2\pi/(R\sqrt{F_\eta(u)})\). Above threshold define
\[
D=1-4\eta^2(s-\eta^2),\quad u_0=-\frac1{2\eta^2},\quad
h=\frac{\sqrt D}{2\eta^2},\quad \xi=\frac{u-u_0}{h}.
\]
The periodic latitudes are exactly \(-1<\xi<1\), on both sides of the torus, and
\[
T_\eta=\frac{2\pi}{R\eta h\sqrt{1-\xi^2}}.
\]
For \(\delta=\eta^2-\eta_*^2\downarrow0\), the scaled periods converge uniformly on every compact subset of \((-1,1)\):
\[
\sqrt\delta\,T_\eta(\xi)\longrightarrow
\frac{2\pi}{Rv_*\sqrt{1-\xi^2}}.
\]

**Area collapse but finite total period-weighted area.** Let \(\mathcal P_\eta\) be the union of both periodic annuli and let \(dA\) be ordinary Euclidean surface area on \(\mathcal T_a\). Put \(\mathcal A_\eta=\int_{\mathcal P_\eta}dA\) and \(\mathcal W_\eta=\int_{\mathcal P_\eta}T_\eta\,dA\) for \(\eta>\eta_*\). Define the positive geometric factor
\[
J(u)=\sqrt{(s+u)u^2+\frac{1-u^2}{4}},\qquad J_*=J(u_*).
\]
Then
\[
\boxed{\lim_{\delta\downarrow0}\frac{\mathcal A_\eta}{\sqrt\delta}
=\frac{8\pi J_*}{\eta_*}},\qquad
\boxed{\lim_{\delta\downarrow0}\mathcal W_\eta
=\frac{8\pi^3J_*}{R\eta_*v_*}
=\frac{8\pi^3J_*}{R\sqrt\tau}>0}.
\]
Thus the periodic region shrinks to zero surface area while its time-weighted area tends to a strictly positive finite limit.

**Universal period-weighted latitude distribution.** Normalize \(T_\eta dA\) on \(\mathcal P_\eta\) to a probability measure. Under this measure, the two signs of \(z\) have probability exactly \(1/2\) each and are independent of \(\xi\). As \(\delta\downarrow0\), the law of \(\xi\) converges in total variation to
\[
\boxed{\frac{d\xi}{\pi\sqrt{1-\xi^2}}\quad(-1<\xi<1)}.
\]
No claim is made that the total time-weighted area stays constant above threshold; only the limit is asserted.

## Assumptions and scope

All variables and parameters are real; \(a>1\) guarantees an embedded nonsingular torus, and \(b^2+c^2>0\) ensures a nonzero angular sinusoid. No normalization changes the original-time vector field. The periodic trajectories counted exclude stationary equilibria, which may be regarded as constant solutions but not as nonstationary cycles. Annuli are connected components of the set of periodic points within \(\mathcal T_a\). Surface area is the intrinsic two-dimensional Euclidean area induced from \(\mathbb R^3\), not flat parameter area. The limits hold for each fixed \(a,b,c\) with \(R>0\), allowing \(d\) to vary through \(|d|/R>\eta_*\).

## Proof

**1. Invariance and scalar angular dynamics.** The equations give \(\frac d{dt}(x^2+y^2)=2x\dot x+2y\dot y=0\) and \(\dot z=0\), so every latitude circle is invariant. Put
\[
(x,y,z)=\big(\sqrt{s+\cos\theta}\cos\phi,\sqrt{s+\cos\theta}\sin\phi,\sin\theta\big).
\]
Since \(s>1\), this is smooth and regular, and \(\theta\) is constant. Rotating the angular origin absorbs \((b,c)\) into the amplitude \(R\), and the unaltered physical-time equation reads
\[
\dot\phi=-\big(R\sqrt{s+\cos\theta}\cos\phi+d\sin\theta\big).
\tag{1}
\]
For fixed \(\theta\), a nonvanishing continuous angular velocity of constant sign gives one full periodic rotation, whereas a zero is an equilibrium that blocks rotations. It vanishes nowhere precisely when \(|d\sin\theta|>R\sqrt{s+\cos\theta}\), or \(F_\eta(u)>0\). By the elementary tangent-half-angle integral (or direct contour substitution), for \(|q|>|p|\), \(\int_0^{2\pi}d\phi/|q+p\cos\phi|=2\pi/\sqrt{q^2-p^2}\). Applying this to (1) proves the minimal original-time period formula. At equality \(|q|=|p|\ne0\) the circle has a unique degenerate equilibrium; for strict inequality in the other direction it has two distinct equilibria. Their inclusion does not turn other trajectories into closed orbits.

**2. Sharp threshold and two-band topology.** The function \(F_\eta(u)=\eta^2(1-u^2)-s-u\) is strictly concave for \(\eta>0\), and \(F_\eta(\pm1)=-(s\pm1)<0\). A positive interior value appears exactly when
\[
\eta^2>\min_{-1<u<1}\frac{s+u}{1-u^2}.
\]
The unique minimizing point is \(u_*=-s+\sqrt{s^2-1}\), since differentiation gives \(1+u^2+2su=0\) and only that root lies in \((-1,1)\). The minimum equals \((s+\sqrt{s^2-1})/2=\eta_*^2\). At equality \(F\) has a double zero at \(u_*\). Above threshold its two simple roots are \(u_\pm=u_0\pm h\) with the indicated positive discriminant \(D\). They lie in \((-1,1)\), and strict positivity is equivalent to \(u_-<u<u_+\). Each such \(u\) has two values of \(\theta\), with opposite signs of \(z\), and no trajectory can switch latitudes. Each connected component is an open annulus with periodic longitude circles. The complement has no nonstationary periodic trajectory, completing the global classification.

**3. Exact normal form and period crossover.** Completing the square gives, without approximation,
\[
F_\eta(u)=\eta^2\big(h^2-(u-u_0)^2\big)=\eta^2h^2(1-\xi^2).
\]
At criticality \(u_0\to u_*\), \(h\to0\). To evaluate its size, write \(e=\eta^2\) and \(e_*=\eta_*^2\). Then \(D(e)=4e^2-4se+1\), \(D(e_*)=0\), and \(D'(e_*)=8e_*-4s=4\tau\). Thus \(D=4\tau\delta+O(\delta^2)\) and \(\eta h/\sqrt\delta\to\sqrt\tau/\eta_*\). Since \(\eta_*v_*=\sqrt\tau\) (verified by substituting \(u_*=-1/(2\eta_*^2)\)), the latter limit equals \(v_*\). The exact period formula gives the uniform compact-subinterval limit. Its divergence at \(|\xi|=1\) is real and no uniform endpoint convergence is asserted.

**4. Actual geometric area element and finite critical weighted mass.** The tangent vectors with respect to \(\theta,\phi\) are orthogonal. Their cross-product has length
\[
\sqrt{(s+\cos\theta)\cos^2\theta+\frac{\sin^2\theta}{4}}=J(\cos\theta).
\]
Since the two hemispheres have the same induced density, the exact area and period-weighted area can be written, for every \(\eta>\eta_*\), as
\[
\mathcal A_\eta=4\pi h\int_{-1}^1\frac{J(u_0+h\xi)}{\sqrt{1-(u_0+h\xi)^2}}\,d\xi,
\tag{2}
\]
\[
\mathcal W_\eta=\frac{8\pi^2}{R\eta}\int_{-1}^1
\frac{J(u_0+h\xi)}{\sqrt{1-(u_0+h\xi)^2}\sqrt{1-\xi^2}}\,d\xi.
\tag{3}
\]
All integrands are positive; the period singularity is integrable since it has square-root order at both annular endpoints. In the critical limit, \(u_0\to u_*\in(-1,1)\), so the smooth factor \(J(u)/\sqrt{1-u^2}\) tends *uniformly* to \(J_*/v_*\) on the shrinking interval. The first integral tends to \(2J_*/v_*\) and the second to \(\pi J_*/v_*\). Together with \(h/\sqrt\delta\to v_*/\eta_*\), these yield both boxed limits. The equivalent coefficient \(R^{-1}\sqrt\tau^{-1}\) follows from \(\eta_*v_*=\sqrt\tau\).

**5. Arcsine law and total variation.** The normalized weighted-\(\xi\) density is exactly proportional to
\[
\frac{J(u_0+h\xi)}{\sqrt{1-(u_0+h\xi)^2}\sqrt{1-\xi^2}},\qquad-1<\xi<1.
\]
The first factor approaches a positive constant uniformly on \([-1,1]\). Dominated convergence, with the integrable majorant \((1-\xi^2)^{-1/2}\), gives convergence in \(L^1\) after normalization, hence convergence in total variation to the arcsine density. Equations (2)–(3) sum two congruent hemispheres; each contributes exactly half the mass at every supercritical parameter and the conditional law of \(\xi\) is the same. This proves the claimed independence and concludes the theorem.

## Verification

The standalone `CHECK.py` uses exact rational arithmetic to check the nontrivial explicit witness \(a=2\), \(b=1\), \(c=0\), \(d=2\): the periodic-root latitudes have \(u_-=-1/4\) and \(u_+=0\), the midpoint has \(F=1/16\), and its physical period is exactly \(8\pi\). It also uses numerical Simpson quadrature only as corroboration for the area constants and the first two arcsine moments near threshold. The general assertions are proved above without inferring an infinite theorem from finite checks. Run `python3 CHECK.py` from a directory containing the standalone file; no third-party packages are required.

## Relationship to prior work

Jana (2024), the originating work for the torus and pseudo-type polynomial flow framework, establishes integrability and structural statements on invariant parallels; those are not claimed as new here. Llibre and Rebollo-Perdomo (2013) study configurations of invariant meridians, parallels and limit cycles on algebraic tori. The closest explicitly inspected contemporary quantitative result treats *cubic axisymmetric* torus flows, where the angular speed does not depend on longitude and almost every latitude is already periodic; its period-tail transition does not imply the *quadratic longitudinally dependent* two-annulus birth or the limiting time-weighted area and arcsine law here. The inverse-square-root period divergence near a generic saddle-node-on-circle is classical; the present claim instead combines a global sharp threshold, both annuli, exact torus surface geometry, and a finite nonzero limiting weighted mass. A 2011 paper by Llibre and Medrado is bibliographically relevant, but its complete main text was unavailable for comparison, leaving a specific priority risk. No bibliographic search proves novelty against all possible literature.

## Limitations

The theorem assumes \(R>0\) and the precise quadratic homogeneous vector field, and it concerns only the fixed smooth torus. It does not address higher-degree angular dependence, perturbation-stable isolated limit cycles, ambient three-dimensional basin properties, or non-Euclidean weights. The total-variation claim holds only for the period-weighted distribution at the specified critical passage; the unweighted conditional latitude distribution has a different (uniform) critical limit. The critical rescaling is not uniform at the annular endpoints. An inaccessible plausible related paper and unindexed equivalences remain publication-priority risks.

## References

1. S. Jana, *Characterization and dynamics of certain classes of polynomial vector fields on the torus*, arXiv:2401.07843, first posted 2024-01-15, https://arxiv.org/abs/2401.07843 .
2. J. Llibre and S. Rebollo-Perdomo, *Invariant parallels, invariant meridians and limit cycles of polynomial vector fields on some 2-dimensional algebraic tori in* \(\mathbb R^3\), Journal of Dynamics and Differential Equations 25 (2013), 777–793, DOI:10.1007/s10884-013-9315-4; open manuscript https://ddd.uab.cat/pub/artpub/2013/gsduab_3215/InvParInvMeronTori.pdf .
3. J. Llibre and J. Medrado, *Limit cycles, invariant meridians and parallels for polynomial vector fields on the torus*, Bulletin des Sciences Mathématiques (2011), DOI:10.1016/j.bulsci.2010.06.005. Relevant abstract accessible; complete main text not inspected.
4. *Sharp period-tail bifurcation and crossover in cubic axisymmetric torus flows*, openly available 2026 research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-period-tail-bifurcation-and-crossover-in-cubic-axisymmetri--f21e276d03a0 . This separate cubic-model comparison is not a source of the current quadratic theorem.
