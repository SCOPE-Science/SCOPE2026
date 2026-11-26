# The full Crofton caustic law of an ellipse and its logarithmic separatrix

## Finding

Fix a noncircular Euclidean ellipse \(E_{a,b}=\{(x,y):x^2/a^2+y^2/b^2\leq1\}\), with \(a>b>0\), circumference \(P\), and focal half-distance \(c=\sqrt{a^2-b^2}\). Choose an unoriented Euclidean line from translation-and-rotation invariant line measure, conditioned to intersect \(E_{a,b}\). Let \(\Lambda\) be the squared-length parameter of its unique confocal conic tangency, defined by \(x^2/(a^2-\Lambda)+y^2/(b^2-\Lambda)=1\) for regular parameters (including confocal hyperbolas when \(b^2<\Lambda<a^2\)). Then \(\Lambda\) has support \([0,a^2]\), no atoms, and the **exact density**

\[
f_\Lambda(z)=\begin{cases}
\dfrac{2}{P\sqrt{a^2-z}}K\!\left(\sqrt{\dfrac{a^2-b^2}{a^2-z}}\right),&0<z<b^2,\\[5pt]
\dfrac{2}{Pc}K\!\left(\sqrt{\dfrac{a^2-z}{a^2-b^2}}\right),&b^2<z<a^2.
\end{cases}
\]

Here \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2v)^{-1/2}\,dv\) is the complete elliptic integral of the first kind, with modulus \(0\leq k<1\). The density has precisely one interior singularity, a two-sided logarithmic divergence at the focal-segment caustic \(z=b^2\):

\[
f_\Lambda(b^2+\eta)=\frac{1}{Pc}\log\!\left(\frac{16c^2}{|\eta|}\right)+o(1)\qquad (\eta\to0,\ \eta\ne0).
\]

The exact probability of a hyperbolic caustic, equivalently a line meeting the segment between the ellipse foci, is
\[
\Pr(\Lambda>b^2)=\frac{4c}{P}.
\]
The upper-endpoint density is finite: \(f_\Lambda(z)\to\pi/(Pc)\) as \(z\uparrow a^2\), hence \(\Pr(\Lambda>a^2-\varepsilon)\sim\pi\varepsilon/(Pc)\). The full law determines both semiaxes: \(a^2\) is its upper support endpoint and \(b^2\) its unique interior logarithmic singularity.

For the circular boundary \(a=b=R\), the formula instead reduces to \(f_\Lambda(z)=1/[2R\sqrt{R^2-z}]\), for \(0<z<R^2\); in particular its upper tail has square-root, rather than linear, order. This establishes the sharp qualitative contrast between circular and noncircular cases.

## Assumptions and scope

Lines are sampled using the invariant unoriented-line measure \(d\theta\,dp\), with \(\theta\in[0,\pi)\) the normal angle and \(p\) the signed offset, restricted to lines intersecting the ellipse and normalized by total mass \(P\). A line tangent to the boundary has zero measure. The resulting measure is also the invariant billiard collision measure: arclength \(\ell\in[0,P)\) uniform and tangential unit-velocity component \(u\in[-1,1]\) uniform, independently. The caustic parameter is a *squared-length parameter*, not the axis length of the confocal curve. At the separatrix \(z=b^2\), the caustic degenerates and the density is infinite at a single point, which carries no probability mass. The limit \(a=b\) is treated separately.

## Proof

**1. The invariant-line and billiard-boundary measures coincide.** For each normal angle \(\theta\), the lines intersecting the ellipse have offsets \(|p|\le h(\theta)=\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}\). Cauchy's perimeter identity gives \(\int_0^\pi 2h(\theta)\,d\theta=P\). The standard incidence Jacobian from a line to its first boundary point is \(|v\cdot n_{\rm in}|\,d\ell\,d\alpha\), where \(\alpha\) is the incidence angle with the inward normal. With \(u=\sin\alpha\), this becomes \(d\ell\,du\). Thus the normalized oriented-incidence probability is \(d\ell\,du/(2P)\). Orientation reversal has no effect on \(\Lambda\), so it is the same law as the unoriented Crofton sample.

**2. Identify the conserved caustic label.** Write the boundary point as \(q(t)=(a\cos t,b\sin t)\) and the boundary speed as \(s(t)=\sqrt{a^2\sin^2 t+b^2\cos^2 t}\), giving \(d\ell=s(t)\,dt\). Let \(n\) be a unit normal to the selected line through \(q(t)\), so its offset is \(p=n\cdot q(t)\). The tangency condition to a confocal conic is \(p^2=(a^2-\Lambda)n_x^2+(b^2-\Lambda)n_y^2\). Consequently
\[
\Lambda=n^T[\operatorname{diag}(a^2,b^2)-q(t)q(t)^T]n=(n\cdot q'(t))^2=s(t)^2(1-u^2).
\]
The middle equality uses the exact rank-one identity \(\operatorname{diag}(a^2,b^2)-q(t)q(t)^T=q'(t)q'(t)^T\). The last equality follows because the unit line normal's tangential component has squared length \(1-u^2\). It proves the asserted range, positivity, and regular conic classification almost surely.

**3. Compute the entire pushforward.** Conditional on \(t\), the variable \(u\) is uniform on \([-1,1]\), so for \(0\le z\le a^2\)
\[
F_\Lambda(z)=\frac1P\int_0^{2\pi}\left[s(t)-\sqrt{(s(t)^2-z)_+}\right]dt,
\qquad (x)_+=\max(x,0).
\]
For \(0<z<a^2\) except \(z=b^2\), differentiation under the integral on the allowed arcs gives
\[
f_\Lambda(z)=\frac{1}{2P}\int_{s(t)^2>z}\frac{dt}{\sqrt{s(t)^2-z}}.
\]
For \(z<b^2\) all angles contribute; writing \(s(t)^2=a^2-c^2\cos^2t\), the fourfold-symmetric integral is \(4K(c/\sqrt{a^2-z})/\sqrt{a^2-z}\), giving the first branch. For \(z>b^2\) only \(|\sin t|>\sqrt{z-b^2}/c\) contributes. An elementary substitution on each of the two surviving arcs, or the standard complete elliptic integral reduction, gives \(\int_{s^2>z}(s^2-z)^{-1/2}dt=(4/c)K(\sqrt{(a^2-z)}/c)\), giving the second branch. The integral CDF establishes normalization and absence of atoms, including at the separatrix.

**4. Singularities, focal mass, and inverse recovery.** The classical asymptotic \(K(k)=\log(4/\sqrt{1-k^2})+o(1)\) as \(k\uparrow1\) applied on either side of \(b^2\) gives the displayed sharp logarithmic coefficient. At \(a^2\), the second branch gives \(K(0)=\pi/2\), hence the terminal linear tail. To identify the caustic-type probability, a line \(n\cdot x=p\) meets the focal segment \(\{(x,0):|x|\le c\}\) exactly when \(|p|\le c|n_x|\). Using \(\Lambda=a^2n_x^2+b^2n_y^2-p^2\), this condition is equivalent to \(\Lambda\ge b^2\). The focal-segment line measure is \(\int_0^\pi2c|\cos\theta|\,d\theta=4c\), while the ellipse-meeting line measure is \(P\). This proves the probability \(4c/P\). Since \(a^2\) is the upper support endpoint and \(b^2\) the unique *interior* density divergence, both axes are determined by the law. Finally, if \(a=b=R\), then \(s(t)=R\) is constant and \(\Lambda=R^2(1-u^2)\); its elementary pushforward gives the asserted circular density and square-root tail.

## Verification

A standalone Python checker `check_caustic.py` independently integrates the explicit density and the direct conditional-geometric CDF, checks hyperbolic mass by two formulas and tests logarithmic and endpoint coefficients. It additionally samples random incident boundary angles with the correct arclength weighting, and separately samples invariant Euclidean lines through their normal angle and offset with the appropriate Crofton weighting. Agreement of both simulations with the analytic CDF tests the measure equivalence; simulations do not substitute for the proof. Run `python check_caustic.py` with NumPy and SciPy installed.

## Relationship to prior work

The Jacobi–Chasles/confocal caustic integral, separation into elliptical and hyperbolic caustics, and the billiard phase-space parametrization are classical, and in particular appear explicitly in Casas–Ramírez-Ros (2011, section 4.1, formula (11)), with the relevant preprint first public on 2010-04-30. Bialy (2022, section 3.2) discusses the same integral and its links to Mather's beta function. Corvaja–Zannier (2023, section 2.8) study an invariant measure restricted to an individual fixed caustic, not the global probability measure across confocal parameters. These known statements supply the geometric input, but the inspected materials do not state the two-branch Crofton pushforward density, its exact logarithmic coefficient, or inverse recovery from that density. The focal-segment crossing mass itself follows from classical Crofton/Cauchy integral geometry and is included as a consequence, not claimed independently new. Possible prior equivalent pushforward formulas in older integrable-systems literature remain a priority risk.

## Limitations

This theorem uses the Euclidean invariant-line ensemble (equivalently the billiard collision invariant measure), **not** endpoint-uniform chords, uniform points inside the ellipse, or a uniformly selected caustic parameter. It applies to axis-aligned ellipses up to rigid motion, with exact observations. It does not establish finite-sample recovery stability, quantitative near-circular uniform approximations, or higher-dimensional confocal joint laws. Mathematical priority is provisional; no independent audit has been performed.

## References

1. P. S. Casas and R. Ramírez-Ros, *The Frequency Map for Billiards inside Ellipsoids*, SIAM J. Applied Dynamical Systems **10** (2011), 278–324, DOI: 10.1137/10079389X; first public preprint 2010-04-30, arXiv:1004.5499. Full text: https://web.mat.upc.edu/rafael.ramirez/res/pdf/siads11.pdf
2. M. Bialy, *Mather β-Function for Ellipses and Rigidity*, Entropy **24** (2022), 1600, DOI: 10.3390/e24111600. https://www.mdpi.com/1099-4300/24/11/1600
3. P. Corvaja and U. Zannier, *Finiteness theorems on elliptical billiards and a variant of the dynamical Mordell–Lang conjecture*, Proceedings of the London Mathematical Society **127** (2023), 1268–1337, DOI: 10.1112/plms.12561. https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.12561
4. H. Stachel, *The geometry of billiards in ellipses and their Poncelet grids*, Journal of Geometry **112** (2021), article 40, DOI: 10.1007/s00022-021-00606-2. https://link.springer.com/article/10.1007/s00022-021-00606-2
