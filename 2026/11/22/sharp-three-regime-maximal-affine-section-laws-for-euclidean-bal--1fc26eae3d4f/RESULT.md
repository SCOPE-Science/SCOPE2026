# Sharp three-regime maximal affine-section laws for Euclidean ball caps

## Finding
For an integer \(d\ge3\) set \(q=d-1\), \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\), \(b=q\kappa_q/2\), and \(\sigma_{d-2}=2\pi^{(d-1)/2}/\Gamma((d-1)/2)\). Let the solid unit-ball cap be
\[
K_h=\{x\in\mathbb R^d:\|x\|\le1,\ x_d\ge h\},\qquad -1<h<1.
\]
Choose an affine hyperplane by the invariant rigid-motion measure conditioned to intersect \(K_h\). Write \(X_h\) for its intrinsic \((d-1)\)-volume, \(V_h=\max X_h\), and \(M_{d,h}\) for the unnormalized measure of intersecting hyperplanes under the convention specified below. Then
\[
V_h=\begin{cases}\kappa_q,&h\le0,\\\kappa_q(1-h^2)^{q/2},&h>0.\end{cases}
\]
For each fixed \(h<0\), put \(\alpha=\arcsin(-h)\) and \(\Omega_{d,h}=\sigma_{d-2}\int_0^\alpha\sin^{d-2}\theta\,d\theta\). The near-maximum laws exhibit three distinct exponents:
\[
\boxed{\begin{aligned}
\Pr(X_h\ge V_h-\varepsilon)&\sim \frac{2\Omega_{d,h}}{M_{d,h}\sqrt b}\,\varepsilon^{1/2},&&-1<h<0,\\
\Pr(X_0\ge V_0-\varepsilon)&\sim\frac{\sigma_{d-2}}{d(d-1)M_{d,0}b^{d/2}}\,\varepsilon^{d/2},&&h=0,\\
\Pr(X_h\ge V_h-\varepsilon)&\sim\frac{\sigma_{d-2}}{d(d-1)M_{d,h}\rho^{d-1}c^d}\,\varepsilon^d,&&0<h<1,
\end{aligned}}\]
where \(\rho=\sqrt{1-h^2}\) and \(c=q\kappa_q h\rho^{q-2}\) in the last line.

The distinct regimes are united by an exact critical scaling. For fixed \(\lambda\in\mathbb R\), put \(h=\lambda\sqrt\varepsilon\), \(a=1/\sqrt b\),
\[
T_\lambda=\sqrt{(\max\{\lambda,0\})^2+a^2},\qquad L_\lambda=\max\{\lambda,-a\}.
\]
Then
\[
\boxed{\Pr(X_{\lambda\sqrt\varepsilon}\ge V_{\lambda\sqrt\varepsilon}-\varepsilon)
\sim \varepsilon^{d/2}\Psi_d(\lambda),\quad
\Psi_d(\lambda)=\frac{\sigma_{d-2}}{d(d-1)M_{d,0}}
\big[(T_\lambda-\lambda)^d-(L_\lambda-\lambda)^d\big].}\]
The crossover changes its algebraic branch at \(\lambda=-1/\sqrt b\) and \(\lambda=0\). For \(d=3\) this profile is piecewise cubic. In addition, the critical rare-event mark has an explicit distribution: if \(s\) is the signed hyperplane offset and \(\theta\) the angle between its outward normal (chosen to have nonnegative axial component) and the vertical, then conditional on the above rare event, \((s/\sqrt\varepsilon,\theta/\sqrt\varepsilon)\) converges in law to probability density proportional to
\[
t^{\,0}r^{d-2}\,\mathbf1_{\{L_\lambda\le t\le T_\lambda,\ 0\le r\le t-\lambda\}},
\]
on the \((t,r)\)-plane. The normal's azimuth is independent uniform on \(S^{d-2}\).

The normalization \(M_{d,h}\) is an explicit one-dimensional integral. Put \(\rho=\sqrt{1-h^2}\), \(u=\cos\theta\). The oriented hyperplane offset interval intersecting \(K_h\) has width
\[
w_h(u)=\begin{cases}
2\rho\sqrt{1-u^2},&h\ge0,\ 0\le u<h,\\
1-hu+\rho\sqrt{1-u^2},&h\ge0,\ h\le u\le1,\\
2,&h<0,\ 0\le u\le-h,\\
1-hu+\rho\sqrt{1-u^2},&h<0,\ -h<u\le1.
\end{cases}
\]
Thus \(M_{d,h}=\sigma_{d-2}\int_0^{\pi/2}w_h(\cos\theta)\sin^{d-2}\theta\,d\theta>0\). In particular
\[
M_{d,0}=\sigma_{d-2}\left(\int_0^{\pi/2}\sin^{d-2}\theta\,d\theta+\int_0^{\pi/2}\sin^{d-1}\theta\,d\theta\right).
\]

## Assumptions and scope
All parameters \(d\ge3\), \(-1<h<1\) are fixed unless the critical scaling explicitly links \(h\) and \(\varepsilon\). An unoriented hyperplane is represented uniquely almost everywhere as \(H(n,s)=\{x:n\cdot x=s\}\) with \(n\cdot e_d\ge0\) and \(s\in\mathbb R\); the measure is spherical area \(d\omega(n)\) times Lebesgue offset \(ds\), conditional on intersection with \(K_h\). This is neither a central-plane/Haar-only section nor a random-plane law generated from random boundary points. Different constant normalizations cancel upon dividing by \(M_{d,h}\). Events of tangency have measure zero. The results concern solid ball caps, not spherical surface zones.

## Proof
**1. Section integral and exact normalization.** Let \(\theta\) be the polar inclination of \(n\) and \(s\) its signed offset. The full ball section has q-dimensional radius \(R=\sqrt{1-s^2}\) if \(|s|<1\). When \(\theta>0\), choose the in-section coordinate \(v\) pointing toward increasing vertical coordinate, so that vertical height on the section equals \(s\cos\theta+v\sin\theta\). Its intersection with \(K_h\) is therefore the q-ball cut at \(v=k=(h-s\cos\theta)/\sin\theta\). Its volume is exactly
\[
X_h(\theta,s)=\kappa_{q-1}\int_{\max\{k,-R\}}^R(R^2-v^2)_+^{(q-1)/2}\,dv,
\]
interpreted as zero for \(k\ge R\) and the full value \(\kappa_q R^q\) for \(k\le-R\). The \(\theta=0\) case is obtained by continuity except on measure-zero cut boundaries. The support function of the cap in a normal direction with positive axial coordinate \(u\) equals \(1\) for \(u\ge h\ge0\), and the spherical rim value \(hu+\rho\sqrt{1-u^2}\) for \(0\le u<h\); for \(h<0\) the negative normal's support equals \(1\) when \(u\le-h\) and the rim value \(-hu+\rho\sqrt{1-u^2}\) otherwise. Taking the sum of the positive and negative supports yields the displayed width formula, which by Fubini gives \(M_{d,h}\).

**2. Sharp maximum and maximizing manifold.** If \(h\le0\), every section lies in a unit q-ball and \(X_h\le\kappa_q\). Equality requires \(s=0\) and the entire great q-ball to lie above the cut, or \(\sin\theta\le-h\). Thus, when \(h<0\), maximizers form the positive-area polar normal cone \(\theta\le\arcsin(-h)\), while at \(h=0\) they collapse to the horizontal section. If \(h>0\), the key inclusion is
\[
K_h\subseteq B_d(h e_d,\rho),\qquad \|x-he_d\|^2\le1-2h x_d+h^2\le1-h^2=\rho^2.
\]
Every hyperplane section thus has q-volume at most \(\kappa_q\rho^q\). Equality requires its entire q-ball section of this enclosing ball to belong to \(K_h\); since the two spheres meet only on the horizontal rim \(x_d=h\), the unique maximizing hyperplane is \(x_d=h\), and its section is that rim's disk. This establishes \(V_h\).

**3. Localization and the clipping boundary.** A full ball section occurs precisely when
\[
s\cos\theta-R\sin\theta\ge h.
\]
Whenever \(s\) and \(\theta\) approach a maximizing configuration, this reduces at first nonzero order to \(s-h\ge\rho\theta+o(|s-h|+\theta)\) if \(h\ge0\). The region failing this inequality has less than full ball volume. Its deficit is the volume of a spherical q-cap with cap depth \(\tau=(R+k)_+\), which satisfies, uniformly for \(R\) bounded away from zero,
\[
\kappa_qR^q-X_h=\Theta(\tau^{(q+1)/2})\qquad(\tau\downarrow0).
\] This bounds the discarded transition-layer measure and shows that strict full-section inequalities determine the leading rare-event measure. The null boundary of the limiting inequalities is negligible. Away from maximizing configurations, compactness of the space of intersecting planes and continuity give a positive gap from \(V_h\). These observations justify the rescalings and dominated-convergence steps below.

**4. Fixed negative cut.** Put \(s=\sqrt\varepsilon\,t\). The full-ball deficit is \(\kappa_q-\kappa_q(1-s^2)^{q/2}=b s^2+O(s^4)\), uniformly on compact rescaled intervals. Thus, to leading order \(|t|\le1/\sqrt b\) and normals lie in the polar cap \(0\le\theta\le\alpha\). Their product measure is \(2\Omega_{d,h}\varepsilon^{1/2}/\sqrt b\). Cut-contact boundary strips shrink and contribute lower order, proving the first line.

**5. Semicircle-type cut in all dimensions.** At \(h=0\), the only maximizer is \((s,\theta)=(0,0)\). Set \(s=\sqrt\varepsilon\,t\), \(\theta=\sqrt\varepsilon\,r\). Full-section and volume constraints become \(0\le r\le t\le1/\sqrt b\). Spherical area near the pole is \(\sigma_{d-2}\theta^{d-2}d\theta\). The limiting unnormalized integral is
\[
\sigma_{d-2}\varepsilon^{d/2}\int_0^{1/\sqrt b}\int_0^t r^{d-2}\,dr\,dt
=\frac{\sigma_{d-2}\varepsilon^{d/2}}{d(d-1)b^{d/2}}.
\]
Dividing by \(M_{d,0}\) proves the second line.

**6. Fixed positive cut.** Let \(s=h+\varepsilon t\), \(\theta=\varepsilon r\). The unclipped section volume satisfies
\[
\kappa_q(1-s^2)^{q/2}=V_h-c\varepsilon t+O(\varepsilon^2),\qquad c=q\kappa_q h\rho^{q-2}>0.
\]
The limiting full-section wedge is \(0\le r\le t/\rho\), \(0\le t\le1/c\). Therefore
\[
\sigma_{d-2}\varepsilon^d\int_0^{1/c}\int_0^{t/\rho}r^{d-2}\,dr\,dt
=\frac{\sigma_{d-2}\varepsilon^d}{d(d-1)\rho^{d-1}c^d},
\]
as required.

**7. Critical window and conditional marks.** Take \(h=\lambda\sqrt\varepsilon\), \(s=\sqrt\varepsilon\,t\), \(\theta=\sqrt\varepsilon\,r\). Relative to the correct cap-dependent maximum \(V_h\), the unclipped volume constraint is
\[
b\bigl[t^2-(\max\{\lambda,0\})^2\bigr]\le1+o(1).
\]
The full-section constraint is \(t\ge\lambda+r+o(1)\). Together they give \(L_\lambda\le t\le T_\lambda\) and \(0\le r\le t-\lambda\); there are no negative-offset branches satisfying both constraints outside this region. Integrating the limiting Jacobian \(\sigma_{d-2}\varepsilon^{d/2}r^{d-2}\,dr\,dt\) proves \(\Psi_d\). The same rescaling, boundedness, and negligible transition layers prove weak convergence of the marked conditional density and independent uniform azimuth. In particular \(\Psi_d\) is positive for every fixed finite \(\lambda\).

The clipping-layer justification can be made quantitative: for a small boundary displacement \(\eta>0\) from full-section contact at \(\theta=O(\sqrt\varepsilon)\), the q-ball clipping depth is of order \(\eta/\theta\), so any near-max cut plane requires \(\eta=O(\theta\varepsilon^{2/(q+1)})\). This produces a vanishing relative volume within the order-\(\sqrt\varepsilon\) critical wedge; the fixed-positive and fixed-negative regimes are controlled analogously. This excludes spurious dominant contributions from clipped sections and completes the asymptotic proof.

## Verification
A standalone numerical checker `verify.py` independently computes actual three-dimensional cap-section areas using the circular-segment identity and integrates the invariant hyperplane measure on a two-dimensional grid. It compares near-max probabilities with the three asymptotic constants and five critical-window values at two tolerances, and cross-checks the exact plane-measure normalizer against direct quadrature. All 25 numerical assertions passed. The numerical calculations corroborate, but do not substitute for, the exact geometric reduction, localization and limiting-integral proof.

## Relationship to prior work
Gille (2005) analyzes motion-invariant random **line chords** of a hemisphere, rather than section volumes of solid caps by codimension-one affine hyperplanes in dimensions three and above. Coleman (1992) treats stereological radii of sections of **spherical shells**, a distinct object and observable. Kim, Yaskin and Zvavitch (2015) study distribution functions of **central sections** of convex bodies; the general theory does not give the three fixed-height regimes or their affine-offset critical scaling. Moseeva, Tarasov and Zaporozhets (2020) treat **spherical surface** sections, not the present solid cap. Previously published calculations of random *central sections of capsules* and of *component counts for affine sections of spherical latitude zones* likewise concern different geometric distributions. The planar \(d=2\) analogous critical transition is already known and is excluded from the new claim; the present higher-dimensional exponents and conditional section-plane shape do not follow from that planar statement without a new dimensional analysis.

## Limitations
The probability law is specified by rigid-motion invariant affine hyperplanes conditioned to hit \(K_h\). Results for central sections, other random-plane schemes, cap boundaries, tangent limits \(h=\pm1\), non-round bodies, or simultaneous large-dimension limits are not claimed. Fixed-height asymptotics are pointwise in \(h\); the critical law is pointwise in \(\lambda\), without uniform error bounds. A published broad 1989 study of random sections of a sphere was accessible only in abstract; its complete contents were not checked, and independent historical-priority review remains necessary. The theorem is proved analytically, not formally certified; numerical checks are finite.

## References
1. W. Gille, *Chord Length Distributions of the Hemisphere*, Journal of Mathematics and Statistics 1 (2005), 24–28, publicly published 2005-03-31, https://www.thescipub.com/jmss/jmssp.2005.24.28 and https://www.thescipub.com/jmss/jmssp.2005.24.28.pdf.
2. R. Coleman, *The stereology of spherical shells*, Acta Stereologica 11 (1992), 137–142, https://ias-iss.org/acta/ActaStereologica_pdf/AS_1887.pdf.
3. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first public 2015-12-22, https://arxiv.org/abs/1512.07289.
4. T. Moseeva, A. Tarasov and D. Zaporozhets, *Random sections of spherical convex bodies*, arXiv:2007.07297, first public 2020-07-14, https://arxiv.org/abs/2007.07297.
5. R. Coleman, *Random sections of a sphere*, Canadian Journal of Statistics 17 (1989), 27–39, DOI:10.2307/3314760; abstract only inspected, https://doi.org/10.2307/3314760.
