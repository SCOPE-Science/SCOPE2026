# Sharp multivisit geometric completeness for circular-orbit direct imaging

## Finding

**Theorem (exact optimal phase gaps and completeness edge).** Fix an integer \(m\ge3\), a normalized inner working radius \(0<t<1\), and \(m\) instantaneous visits to a unit-radius circular orbit. The orbital plane is isotropically oriented and the initial orbital phase is uniform. The period is known; all visits are freely schedulable, with no elapsed-time or brightness constraints. Detection succeeds if and only if at least one visit has projected star–planet separation strictly greater than \(t\).

Regard visit phases modulo \(\pi\), order them cyclically on this projective phase circle, and let their consecutive gaps be \(g_1,\ldots,g_m\ge0\), summing to \(\pi\). Define \(h=\sqrt{1-t^2}\) and \(b_t(z)=\arcsin(h/\sqrt{1-z^2})\) for \(0\le z<t\). The exact miss probability is

\[
M_t(g_1,\ldots,g_m)=\frac{1}{\pi}\int_0^t\sum_{j=1}^m [g_j-2b_t(z)]_+\,dz,
\]

where \([u]_+=\max(u,0)\). The global minimum is attained by uniform projective gaps \(g_j=\pi/m\) for all \(j\). Put \(c_m=\cos(\pi/(2m))\). If \(t<c_m\), precisely the schedules with \(\max_j g_j\le2\arccos t\) achieve the perfect geometric completeness \(M_t=0\). If \(t\ge c_m\), uniform projective gaps are the **unique** minimizers as unordered phase configurations, up to global rotation and phase multiplicities. At \(t=c_m\) this unique minimizer still has zero miss probability, whereas at \(t>c_m\) every schedule has strictly positive miss probability.

More sharply, as \(t\downarrow c_m\) from above,

\[
\min_g M_t(g)=K_m(t-c_m)^{3/2}+O_m((t-c_m)^{5/2}),\qquad
K_m=\frac{4m\sqrt{2c_m}}{3\pi\sin^2(\pi/(2m))}>0.
\]

Consequently, for a fixed normalized inner working radius, the smallest number of freely scheduled visits guaranteeing geometric completeness is \(\left\lceil\pi/(2\arccos t)\right\rceil\), with one visit sufficient for \(t\le0\) outside the theorem's positive-radius domain; for \(0<t<1\) the ceiling is at least two. In particular, three visits have the sharp guarantee cutoff \(t=\sqrt3/2\).

## Assumptions and scope

Choose planar orbital position vectors \(u(\phi)=(\cos\phi,\sin\phi,0)\). An isotropic orbit orientation and independent uniform initial phase are represented by a uniformly random sightline \(n\) on the unit sphere, while the deterministic relative visit phases are \(\phi_1,\ldots,\phi_m\). The projected separation is \(\sqrt{1-(n\cdot u(\phi_j))^2}\). The observations are not assumed statistically independent, since all share the same orbit and sightline. Visits separated by half an orbit have identical projected separations, explaining the quotient phase circle of circumference \(\pi\). All orbital parameters except the nuisance orientation/phase are fixed. This is a geometric visibility model, not an instrumental signal-to-noise or orbital-reconstruction model.

## Proof

Write \(z=|n_z|\), which is uniform on \([0,1]\), and let the azimuth of \(n\) be uniform modulo \(\pi\), independently of \(z\). For \(z\ge t\), the length of the azimuthal projection of \(n\) is at most \(h\), so separation exceeds \(t\) at every scheduled phase, except zero-measure equality boundaries. For \(0\le z<t\), a visit at phase \(\phi_j\) detects precisely when \(|\cos(\theta-\phi_j)|<h/\sqrt{1-z^2}\). This is an arc of radius \(b_t(z)\) about quadrature \(\phi_j+\pi/2\) modulo \(\pi\). The complement of the union of these equal-radius arcs has total length exactly \(\sum_j[g_j-2b_t(z)]_+\). Averaging its fraction of the \(\pi\)-circumference over uniform \(z\) proves the stated integral.

For any real \(q\), the map \(x\mapsto[x-q]_+\) is convex. Since the gaps have mean \(\pi/m\), Jensen's inequality gives, pointwise in \(z\),

\[
\sum_j[g_j-2b_t(z)]_+\ge m[\pi/m-2b_t(z)]_+.
\]

Integration proves global optimality. The function \(2b_t(z)\) is strictly increasing from \(2\arccos t\) at \(z=0\) to \(\pi\) at \(z=t\). For zero integrated miss, its minimum implies \(g_j\le2\arccos t\) for every gap; conversely these inequalities give zero integrand. An equal-gap schedule meets them exactly when \(\pi/m\le2\arccos t\), equivalently \(t\le c_m\). At \(t\ge c_m\), any nonconstant gap vector has at least one gap above its mean; choose an arc length strictly between the smallest and largest gap and at least \(2\arccos t\). On an open set of \(z\), some gap contributions are positive and others vanish, making the Jensen inequality strict. Thus only the uniform gap vector minimizes. For \(t>c_m\), its integrand is positive near \(z=0\), proving positive miss.

For the edge expansion put \(\gamma=\pi/(2m)\), \(s=\sin\gamma\), \(c=\cos\gamma\), and \(\delta=t-c>0\). Uniform gaps have half length \(\gamma\). Taylor expansion of the smooth trigonometric argument near \((\delta,z)=(0,0)\), valid uniformly on the eventual support, gives

\[
2(\gamma-b_t(z))=\frac{2\delta-sz^2}{c}+O_m(\delta^2+\delta z^2+z^4).
\]

The positive part is supported exactly on \(0\le z<z_0=\sqrt{t^2-c^2}/s=\sqrt{2c\delta}/s+O_m(\delta^{3/2})\). Therefore

\[
\min_g M_t(g)=\frac{m}{\pi c}\int_0^{\sqrt{2c\delta}/s}(2\delta-sz^2)\,dz+O_m(\delta^{5/2})
=\frac{4m\sqrt{2c}}{3\pi s^2}\delta^{3/2}+O_m(\delta^{5/2}).
\]

The error follows from integration over an interval of length \(O_m(\delta^{1/2})\) of a uniformly \(O_m(\delta^2)\) remainder; the boundary-location replacement has an even smaller contribution because the leading integrand vanishes at its endpoint. The visit-count formula and the three-visit threshold follow by solving \(\pi/m\le2\arccos t\) for the least positive integer \(m\).

## Verification

The accompanying standalone `VERIFY.py` numerically evaluates the exact one-dimensional formula with adaptive-free composite Simpson quadrature and checks unequal-gap designs, the threshold, and the \(3/2\)-power coefficient for several visit counts. It also independently evaluates the visible-arc complement directly from circular gaps and tests Jensen's inequality on deterministic finite configurations. It does **not** replace the proof of global optimality, equality cases, or the asymptotic expansion.

For \(m=3\) and \(t=0.92\), uniform gaps give miss probability approximately \(0.10286909\). Gaps \((\pi/6,\pi/3,\pi/2)\) instead give approximately \(0.19408187\). These are illustrative quadrature values, not empirical observations.

## Relationship to prior work

Direct-imaging observation models and survey revisits are established topics. Brown and Soummer (2010) give a realistic multivisit completeness framework and scheduling methods, including iterative selection rather than the all-projective-phase exact scheduling theorem. Kane, Meshkat and Turnbull (2018) derive epochs of maximum projected separation for known orbits; their inverse-ephemeris problem differs from optimizing all phase gaps under isotropic unknown orientation. Dallant and colleagues (2023) derive a multiepoch signal-combination and orbital-inference pipeline, not this idealized coverage optimum. Plavchan and colleagues (2024) obtain analytic survey-yield relations but explicitly do not model revisits. A separately published two-visit result gives the quarter-orbit optimum and a \(3/2\)-onset for two observations; the present claim is the joint exact formula, global uniqueness/equality classification, critical radius, and sharp coefficient for each \(m\ge3\). Classical convexity/covering facts underlie the proof and are not claimed as novel.

## Limitations

This theorem assumes circular orbits with known periods, unconstrained visit times, isotropic unknown geometry, zero overhead, zero false detections and perfect detection whenever projected separation exceeds the threshold. Real missions have photometric phase functions, contrast curves, finite durations, observability windows, orbital uncertainty, eccentricity and correlated noise. The phase schedule is a mathematical benchmark, not an actual telescope scheduling recommendation. Novelty is assessed relative to inspected literature and indexed records, not certified as a universal historical priority claim. Independent validation has not been performed.

## References

- Brown, R. A. and Soummer, R. (2010), *New Completeness Methods for Estimating Exoplanet Discoveries by Direct Detection*, arXiv:1003.4700, https://arxiv.org/abs/1003.4700.
- Kane, S. R., Meshkat, T. and Turnbull, M. C. (2018), *Maximum Angular Separation Epochs for Exoplanet Imaging Observations*, arXiv:1810.07328, https://arxiv.org/abs/1810.07328.
- Dallant, J., Langlois, M., Flasseur, O. and Thiébaut, É. (2023), *PACOME: Optimal multi-epoch combination of direct imaging observations for joint exoplanet detection and orbit estimation*, arXiv:2309.08679, initially public 2023-09-15, https://arxiv.org/abs/2309.08679.
- Plavchan, P. et al. (2024), *Analytic relations assessing the impact of precursor knowledge and key mission parameters on direct imaging survey yield*, arXiv:2401.02039, https://arxiv.org/abs/2401.02039.
- *Exact two-visit direct-imaging completeness and its sharp quarter-orbit transition* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-two-visit-direct-imaging-completeness-and-its-sharp-quarte--26baa61dfac4. Indexed abstract inspected; complete document not accessible during this review.
