# Unique phase staggering for two half-wave generators behind one export cap

## Finding
For every midday price-premium parameter \(0<\eta\le1\), two equal half-wave power profiles behind a shared export cap equal to one generator's peak have a **unique** optimal symmetric phase half-separation \(a_*(\eta)\). It satisfies \(\pi/4<a_*(\eta)<\pi/3\) and a scalar equation given below. The optimal half-separation strictly decreases with the premium, and as \(\eta\downarrow0\),
\[
\frac{\pi}{3}-a_*(\eta)=\frac{\pi^2}{72\sqrt3}\eta^2+o(\eta^2).
\]
With \(\eta=1\), \(a_*=1.025464201385760\ldots\) radians (full separation \(117.5095415623\ldots\) degrees). The zero-premium case is different: every \(a\in[\pi/3,\pi/2]\) is optimal, so even an arbitrarily small positive premium selects a unique interior separation.

## Assumptions and scope
Fix one dimensionless daily cycle \(t\in[-\pi,\pi)\), and define \(h(t)=\max\{0,\cos t\}\). The two equal generators supply \(h(t-a)\) and \(h(t+a)\), with controlled symmetric phase half-separation \(0\le a\le\pi/2\). Their sum feeds a common lossless exporter of capacity \(1\), so delivered output is \(\min\{1,h(t-a)+h(t+a)\}\). A common known nonnegative time-dependent value weight is \(1+\eta h(t)\), \(0\le\eta\le1\). There are no additional network, storage, electrical-mismatch or phase-dependent construction costs. Optimize precisely
\[
U_\eta(a)=\frac1{2\pi}\int_{-\pi}^{\pi}(1+\eta h(t))\min\{1,h(t-a)+h(t+a)\}\,dt.
\]
The phase variable is an idealized timing offset, **not** a geographic distance, a PV-panel azimuth, or an empirically calibrated installation angle.

## Proof
1. By symmetry and the overlap geometry, when \(0\le a<\pi/3\), clipping occurs exactly for \(|t|<u(a)\), where
\[
u(a)=\arccos\!\left(\frac1{2\cos a}\right),\qquad 0<u(a)\le\pi/3.\]
Indeed, on the simultaneous-positive interval \(|t|\le\pi/2-a\), the unconstrained sum is \(2\cos a\cos t\); outside it at most one half-wave contributes and it is at most one. The clipping interval is contained in the simultaneous-positive interval because \(u(a)\le\pi/2-a\), equivalently \(\cos(\pi/2-a)=\sin a\le1/(2\cos a)\), which follows from \(\sin2a\le1\). For \(a\ge\pi/3\), clipping never occurs.

2. Without clipping, integrate each half-wave and its overlap with \(h(t)\):
\[
U_\eta^{\rm free}(a)=\frac2\pi+\frac{\eta}{2\pi}\left[(\pi-a)\cos a+\sin a\right].
\]
For \(a<\pi/3\), subtract the exact clipped excess:
\[
U_\eta(a)=U_\eta^{\rm free}(a)-\frac1\pi\big[2\cos a\sin u-u+\eta\{\cos a(u+\sin u\cos u)-\sin u\}\big].
\]
Because the clipped excess vanishes at its moving boundary, differentiating gives
\[
U_\eta'(a)=\frac{\sin a}{\pi}B_\eta(a),\quad
B_\eta(a)=2\sin u+\eta\left[u+\sin u\cos u-\frac{\pi-a}{2}\right].
\]
For \(a\ge\pi/3\), differentiation of the free expression gives \(U_\eta'(a)=-\eta(\pi-a)\sin a/(2\pi)<0\) for \(\eta>0\) and \(a<\pi/2\).

3. If \(0\le a\le\pi/4\), then \(u\ge\pi/4\), whence \(2\sin u\ge\sqrt2\) and \(u+\sin u\cos u-(\pi-a)/2\ge-\pi/4\). Therefore \(B_\eta(a)\ge\sqrt2-\eta\pi/4>0\). If \(\pi/4\le a<\pi/3\), differentiate using \(u'(a)=-\tan a/(2\cos a\sin u)\):
\[
B_\eta'(a)=-\frac{(1+\eta\cos u)\tan a}{2\cos^2a\sin u}+\frac\eta2
\le-\sqrt2+\frac12<0.
\]
Here \(\tan a\ge1\), \(2\cos^2a\le1\) and \(\sin u\le1/\sqrt2\). Finally, \(B_\eta(\pi/3^- )=-\eta\pi/3<0\). Thus it crosses zero at exactly one \(a_*\in(\pi/4,\pi/3)\), and derivative signs show that this is the unique global maximum on \([0,\pi/2]\).

4. At the root, the bracket multiplying \(\eta\) in \(B_\eta\) is \(-2\sin u/\eta<0\). Because \(B_\eta'<0\) at the root, implicit differentiation gives \(a_*'(\eta)<0\). As \(\eta\downarrow0\), root uniqueness forces \(a_*\uparrow\pi/3\). Writing \(\varepsilon=\pi/3-a_*\), one has \(u=\sqrt{2\sqrt3\,\varepsilon}\,[1+o(1)]\) and the root relation \(2u=\eta\pi/3+o(\eta)\). Hence \(\varepsilon=\pi^2\eta^2/(72\sqrt3)+o(\eta^2)\).

5. At \(\eta=0\), each generator provides mean output \(1/\pi\), so \(U_0\le2/\pi\). This bound is attained precisely when there is no clipping, namely \(a\in[\pi/3,\pi/2]\), proving the stated boundary case.

## Verification
Reproduce the diagnostic calculations with Python 3 standard library: `python CHECKER.py`. It independently integrates the original positive-part and clipped objective at multiple parameters, evaluates the closed formula and root, checks approximate global rankings and the small-premium asymptotic. The script reports 848 passed diagnostics and yields full separation \(117.5095415623151\ldots\) degrees for \(\eta=1\). These finite checks are supplementary; the monotonic derivative inequalities in the proof establish the infinite-parameter claim.

## Relationship to prior work
Photovoltaic spatial smoothing was studied by Marcos et al. (first public online 21 July 2011). Hummon, Denholm and Margolis (first online 10 May 2012) studied price-driven photovoltaic orientation numerically, and Staudacher discussed the beneficial power-profile staggering of paired east-west arrays on a shared inverter. Those works motivate the common-cap and time-value mechanism. The exact bounded-premium uniqueness, root equation and quadratic approach to the clipping boundary are not implied by the specific results inspected. This is a narrow analytic result for the explicit idealized function, not a claim of priority over all power-system design models.

## Limitations
The derivation does not represent a physically calibrated array-orientation map, seasonal variation, cloud noise, mismatch/maximum-power-point tracking, geographic transport cost, dynamic price setting, demand constraints, or storage. A positive price weight is imposed rather than solved for. Alternative cap ratios or nonsinusoidal profiles can have different optima. Full text of the closest price-orientation paper was not obtained, leaving residual priority uncertainty.

## References
- J. Marcos, L. Marroyo, E. Lorenzo and M. García, *Smoothing of PV power fluctuations by geographical dispersion*, Progress in Photovoltaics, DOI: https://doi.org/10.1002/pip.1127 (first published 2011-07-21).
- M. Hummon, P. Denholm and R. Margolis, *Impact of photovoltaic orientation on its relative economic value in wholesale energy markets*, Progress in Photovoltaics, DOI: https://doi.org/10.1002/pip.2198 (first published 2012-05-10).
- D. Staudacher, *Efficient east-west orientated PV systems with one MPP tracker*, technical paper, https://www.energymatters.com.au/images/news/2013/east-west-solar-paper.pdf (date of first public release not verified).
- K. Sinapis et al., *Outdoor characterization and comparison of string and MLPE under clear and partially shaded conditions*, Energy Science & Engineering, DOI: https://doi.org/10.1002/ese3.97 (first published 2015-10-06).
