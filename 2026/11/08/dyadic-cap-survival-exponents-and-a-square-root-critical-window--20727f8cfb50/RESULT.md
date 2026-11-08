# Dyadic cap-survival exponents and a square-root critical window for normalized affine sphere maps

## Finding

Fix an integer \(d\ge 2\), a unit vector \(u\in\mathbb R^{d+1}\), and \(0<t<1\). On the unit sphere \(S^d\), consider the normalized affine homeomorphism
\[
 F_t(x)=\frac{x+t u}{\|x+t u\|}.
\]
Draw \(X\) from normalized Euclidean surface area on \(S^d\). For a cap angular radius \(\varepsilon\in(0,\pi)\), define its first entrance time
\[
 \tau_{t,\varepsilon}(X)=\inf\{j\in\mathbb Z_{\ge0}:\arccos\langle F_t^j(X),u\rangle\le\varepsilon\},
\]
where an empty infimum is infinity. Let \(S_{d,t,n}(\varepsilon)=\Pr(\tau_{t,\varepsilon}>n)\), \(n\in\mathbb Z_{\ge0}\). Define
\[
 Q_t(\theta)=\theta+\arcsin(t\sin\theta),\quad
 I_d=\int_0^\pi\sin^{d-1}v\,dv=\frac{\sqrt\pi\,\Gamma(d/2)}{\Gamma((d+1)/2)},\quad A_d=\frac1{d I_d}.
\]
The exact **all-iteration cap-survival law** is
\[
 \boxed{S_{d,t,n}(\varepsilon)=\frac1{I_d}\int_{Q_t^{\circ n}(\varepsilon)}^\pi\sin^{d-1}v\,dv.}
\]

The singular regime \(t\uparrow1\) has a sharp dyadic staircase. For fixed \(\varepsilon\), set
\[
 m=\left\lceil\log_2(\pi/\varepsilon)\right\rceil,\qquad
 \alpha=2^{m-1}\varepsilon\in[\pi/2,\pi),\qquad \delta=1-t.
\]
For each fixed integer \(0\le n<m\),
\[
 \lim_{\delta\downarrow0}S_{d,1-\delta,n}(\varepsilon)
 =\frac1{I_d}\int_{2^n\varepsilon}^\pi\sin^{d-1}v\,dv.
\]
For **nonresonant cap sizes** \(\alpha>\pi/2\), for each fixed integer \(n\ge m\),
\[
 \boxed{S_{d,1-\delta,n}(\varepsilon)\sim
 A_d(-\tan\alpha)^d\delta^{d(n-m+1)}.}
\]
For **dyadic resonant sizes** \(\varepsilon=\pi/2^m\), for each fixed \(n\ge m\),
\[
 \boxed{S_{d,1-\delta,n}(\varepsilon)\sim
 A_d 2^{d/2}\delta^{d(n-m+1/2)}.}
\]
Most notably, resonance admits an explicit square-root angular crossover. Fix \(m\ge1\), \(z\in\mathbb R\), and take the varying cap
\[
 \varepsilon_\delta=\frac\pi{2^m}+\frac{z\sqrt\delta}{2^{m-1}}.
\]
Then, for every fixed \(n\ge m\),
\[
 \boxed{\lim_{\delta\downarrow0}\frac{S_{d,1-\delta,n}(\varepsilon_\delta)}{\delta^{d(n-m+1/2)}}
 =A_d\bigl(\sqrt{z^2+2}-z\bigr)^d.}
\]
All limits hold with \(d,m,n,\varepsilon,z\) fixed, within the stated regimes. They are not uniform in iteration counts tending to infinity.

## Assumptions and scope

The sphere has its standard round metric and normalized Euclidean surface-area probability. The parameter \(t\) is strictly below one, so \(F_t\) is a homeomorphism. The cap is centered at \(u\), and entrance at iteration zero counts as entrance. The polar angle \(\theta(x)=\arccos\langle x,u\rangle\) ranges over \([0,\pi]\). The endpoint \(x=-u\) has area zero and is the unique singular point of the limiting map at \(t=1\); no map on that endpoint is asserted. The angular inverse \(Q_t\) is iterated as a function \([0,\pi]\to[0,\pi]\). The cap-dependent integer \(m\) is at least one.

The dimension restriction \(d\ge2\) concerns higher-dimensional sphere maps. The same proof also applies to the circle with its angular probability density interpreted appropriately.

## Proof

**1. Angular dynamics and exact survival.** Write \(x=\cos\theta\,u+\sin\theta\,v\) with \(v\perp u\) unit. The image lies on the same meridian with polar angle
\[
 g_t(\theta)=\operatorname{atan2}(\sin\theta,\cos\theta+t).
\]
For \(0<t<1\), \(g_t\) is an increasing bijection of \([0,\pi]\) onto itself, fixes the endpoints, and satisfies \(g_t(\theta)<\theta\) for \(0<\theta<\pi\). If \(\psi=g_t(\theta)\), the equality of azimuthal components of \(x+t u\) and its normalized image yields
\[
 \sin(\theta-\psi)=t\sin\psi.
\]
Because \(0<\theta-\psi<\pi/2\), the unique solution is \(\theta=\psi+\arcsin(t\sin\psi)=Q_t(\psi)\). Thus \(g_t=Q_t^{-1}\). An orbit has not entered the cap through iteration \(n\) if and only if its starting polar angle is strictly above \(Q_t^{\circ n}(\varepsilon)\); strict versus nonstrict boundaries have surface measure zero. The normalized polar-angle density of uniform spherical area is \(I_d^{-1}\sin^{d-1}\theta\). Integration proves the exact formula.

**2. Boundary-distance recurrence.** Put \(r_j=\pi-Q_{1-\delta}^{\circ j}(\varepsilon)\), \(j\ge0\). The identity \(\sin(\pi-r)=\sin r\) gives the exact scalar recurrence
\[
 \boxed{r_{j+1}=r_j-\arcsin\bigl((1-\delta)\sin r_j\bigr).}
\]
It is nonnegative, and the tail law may equally be written
\[
 S_{d,1-\delta,n}(\varepsilon)=I_d^{-1}\int_0^{r_n}\sin^{d-1}v\,dv.
\]
At \(\delta=0\), the inverse polar map, away from the singular south pole, becomes \(Q_1(\theta)=\min(2\theta,\pi)\). Consequently \(Q_{1-\delta}^{\circ j}(\varepsilon)\to2^j\varepsilon\) for \(j<m\), proving the pre-collapse limits. Since \(m\) is the first iteration whose limiting inverse angle reaches or passes \(\pi\), the remaining survival probabilities vanish and require higher-order analysis.

**3. Nonresonant collapse.** For \(j\le m-1\), the limiting inverse angle remains \(2^j\varepsilon<\pi\), and for \(j<m-1\) in fact remains strictly below \(\pi/2\). Ordinary smooth perturbation of \(Q_t\) at those pre-collapse angles gives
\[
 Q_{1-\delta}^{\circ(m-1)}(\varepsilon)=\alpha+O(\delta).
\]
When \(\pi/2<\alpha<\pi\), the limiting function \(Q_1\) is constant equal to \(\pi\) in a neighborhood of \(\alpha\). Its derivative with respect to the angular argument vanishes there, so the preceding \(O(\delta)\) angular perturbation does not affect the first-order deficit. Expanding the inverse expression at the fixed angle \(\alpha\) yields
\[
 \pi-Q_{1-\delta}(\alpha)
 =\pi-\alpha-\arcsin((1-\delta)\sin\alpha)
 =(-\tan\alpha)\delta+o(\delta).
\]
Therefore \(r_m\sim(-\tan\alpha)\delta\).

**4. Resonance and its square-root window.** If \(\alpha=\pi/2\), the first \(m-1\) iterations still give \(Q_{1-\delta}^{\circ(m-1)}(\varepsilon)=\pi/2+O(\delta)\). The elementary endpoint expansion
\[
 \arcsin(1-h)=\frac\pi2-\sqrt{2h}+O(h^{3/2})\quad(h\downarrow0)
\]
shows \(r_m\sim\sqrt{2\delta}\). More generally, for the varying input \(\varepsilon_\delta\), the finite pre-collapse composition gives
\[
 Q_{1-\delta}^{\circ(m-1)}(\varepsilon_\delta)
 =\frac\pi2+z\sqrt\delta+O(\delta).
\]
Since \((1-\delta)\sin(\pi/2+z\sqrt\delta+O(\delta))=1-(1+z^2/2)\delta+O(\delta^{3/2})\), we obtain
\[
 r_m=\bigl(\sqrt{z^2+2}-z\bigr)\sqrt\delta+o(\sqrt\delta).
\]
This includes the resonant constant at \(z=0\).

**5. Further iterations and spherical volume.** For \(r\to0\) and \(\delta\downarrow0\), the recurrence satisfies
\[
 \frac{r-\arcsin((1-\delta)\sin r)}{\delta r}\to1.
\]
Indeed the numerator vanishes identically at \(\delta=0\); the mean-value formula in \(t\) makes it exactly \(\delta\sin r/\sqrt{1-\xi^2\sin^2r}\) for a \(\xi\in(1-\delta,1)\), and the quotient tends to one. Applying this at each fixed additional iteration gives \(r_n\sim\delta^{n-m}r_m\) for \(n\ge m\). Finally,
\[
 \frac1{I_d}\int_0^r\sin^{d-1}v\,dv\sim A_d r^d\quad(r\downarrow0).
\]
Substitution of the two collapse laws and the boundary-layer law proves every stated asymptotic, including exact constants, angular crossover and powers.

## Verification

The standalone `checker.py` tests the forward/inverse angular conjugacy at independent angles and parameters, matches the exact cap integral to elementary area formulas in dimensions two and three, and evaluates the sharp asymptotics in dimensions two through four, for nonresonant sizes and resonant windows with several iteration counts. Its success marker is `SPHERICAL_CAP_SURVIVAL_EXACT_AND_CRITICAL_LIMITS_OK`. It uses high precision to avoid cancellation near the singular parameter. These finite checks do not establish the limiting assertions: the proof above does.

## Relationship to prior work

The normalized affine sphere-map family and its homeomorphism condition were introduced by Shah and Yadav (first public preprint 2016). Choudhuri, Faraco and Yadav subsequently studied topological distality, expansivity, and fixed/periodic behavior for these maps, including higher-dimensional spheres (first public preprint 2022). The polar inverse is also consistent with the independently known inverse formula for normalized translation flows in directional statistics and normalizing flows. Those are prior ingredients, not new claims.

The theorem here instead quantifies **initial surface-area mass surviving a prescribed cap for an exact number of iterations** as normalization approaches its singular value, distinguishing every dyadic threshold by an exponent jump and resolving it on a square-root angular scale. The preceding cited works do not state the cap-survival distribution, its full staircase or the crossover. The simple angle and spherical-area identities are used transparently; no exclusivity of the method or general normalized-affine-map theorem is claimed.

## Limitations

Only the isotropic translation family \(F_t\) and caps centered at the translation axis are covered; general invertible linear parts, off-axis caps and nonspherical sampling are not. All asymptotic estimates fix dimension and iteration count. The boundary object at \(t=1\) is not a homeomorphism at the antipode. The result gives no uniform \(n\to\infty\) assertion and no invariant-measure uniqueness theorem. An unindexed equivalent calculation remains possible despite the inspected primary literature and public-record searches; publication priority is not independently certified.

## References

1. M. Choudhuri, G. Faraco, A. K. Yadav, *On the distality and expansivity of certain maps on spheres*, arXiv:2209.05236, first public version 2022-09-12. https://arxiv.org/abs/2209.05236 .
2. R. Shah, A. K. Yadav, *Dynamics of Certain Distal Actions on Spheres*, arXiv:1606.08797, first public version 2016-06-28; later Real Analysis Exchange 44 (2019), 77–88. https://arxiv.org/abs/1606.08797 .
3. Boulerice and Ducharme (1994), normalized-translation Jacobian as described in the normalized-translation-flow literature; used only as a cross-check of the map family, not for the claimed survival asymptotics.
