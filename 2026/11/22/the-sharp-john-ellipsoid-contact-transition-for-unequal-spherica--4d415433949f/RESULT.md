# The sharp John-ellipsoid contact transition for unequal spherical lenses

## Finding
Let \(R\ge r>0\) and \(R-r<s<R+r\). In \(\mathbb R^3\) consider the unequal spherical lens
\[
K=\overline B((0,0,0),R)\cap\overline B((s,0,0),r).
\]
Its unique maximum-volume inscribed ellipsoid, **among all centers and orientations**, has the rotational form
\[
E=\left\{(x,y,z):\frac{(x-m)^2}{a^2}+\frac{y^2+z^2}{b^2}\le1\right\}.
\]
All three positive geometric parameters \(m,a,b\) have the following complete exact determination.

**Unequal radii, polar-contact regime.** For \(R>r\), put \(s_c=3(R^2-r^2)/(2R)\) and \(\delta=s-R\). If \(s\le s_c\), then
\[
a=\frac{\sqrt{\delta^2+3r^2}-2\delta}{4},\qquad
b=\sqrt{4a^2+3a\delta},\qquad m=R-a.
\]
In ellipsoid-normalized coordinates, contact with the larger ball occurs at the positive axial pole \(t=1\), and contact with the smaller ball is the latitude circle \(t=-1/3\). If \(R\ge3r\), this regime occupies **every** nonnested separation \(R-r<s<R+r\).

**Unequal radii, two-latitude regime.** This occurs precisely when \(r<R<3r\) and \(s_c<s<R+r\). Let \(T\in(R/(3r),1)\) be the unique root
\[
s^2=\frac{(R^2-r^2)^2(3T+1)}{(3T-1)\{R^2-r^2+r^2T-R^2/(9T)\}}.
\]
Set \(u=\sqrt T\), \(v=-1/(3u)\), and
\[
B=\frac{r^2u^2-R^2v^2}{u^2-v^2},\qquad
J=\frac{R^2-r^2}{u^2-v^2}.
\]
Then \(B,J>0\) and
\[
a=\frac{B}{\sqrt{B+J}},\qquad b=\sqrt B,\qquad
m=\frac{Ju}{\sqrt{B+J}}.
\]
The complete boundary contact orbits are the larger ball's latitude \(t=u\) and the smaller ball's latitude \(t=v\), with the universal product \(uv=-1/3\). The formulas agree continuously with the polar-contact branch at \(s=s_c\).

**Equal radii.** If \(R=r\), let
\[
m=s/2,\qquad a=\sqrt{R^2+s^2/12}-s/\sqrt3,\qquad
b=\sqrt{a^2+(\sqrt3/2)as}.
\]
The two contact latitudes are \(t=\pm1/\sqrt3\). This agrees with the known symmetric-lens formula and is given here only to close the classification.

Thus the sharp radius imbalance \(R/r=3\) separates lenses whose maximizer always touches the larger sphere at its axial pole from those with a genuine interior separation-dependent transition to two nondegenerate latitude contacts. The optimum volume is exactly \(4\pi a b^2/3\) in all regimes.

## Assumptions and scope
A bar denotes a closed Euclidean ball; \(s\) is the distance between the centers, not a radius. The inequality \(R-r<s<R+r\) excludes complete containment and external tangency and guarantees a full-dimensional lens bounded by portions of both spheres. The semiaxis \(a\) is axial and \(b\) is the common transverse semiaxis. A normalized contact latitude \(t\) means \(x=m+at\) and \((y,z)=b\sqrt{1-t^2}\,\omega\) with \(\omega\in S^1\). At \(t=1\) this circle collapses to one pole. The maximizing ellipsoid is unrestricted: neither centering nor rotational symmetry is imposed on competitors. Only Euclidean dimension three is claimed.

## Proof
**1. Exact ball-containment test.** For an ellipsoid with \(a<b\), write a boundary point as \((m+at,b\sqrt{1-t^2}\,\omega)\). Its squared distance to the center \((c,0,0)\) is
\[
F_c(t)=(m-c+at)^2+b^2(1-t^2),\qquad -1\le t\le1.
\]
The strictly concave quadratic has its stationary maximum at
\[
t_c=\frac{a(m-c)}{b^2-a^2}.
\]
If \(t_c\in[-1,1]\), its maximum is \(b^2[1+(m-c)^2/(b^2-a^2)]\); otherwise its maximum is attained at the endpoint \(t=\operatorname{sgn}(m-c)\). Thus \(E\subseteq K\) is established by checking \(\max F_0\le R^2\) and \(\max F_s\le r^2\). The interior of the ellipsoid is also contained when its entire boundary is contained, by convexity of both balls.

**2. The polar-contact solution.** For \(\delta=s-R\), the displayed positive root \(a\) satisfies
\[
16a^2+16a\delta+3\delta^2=3r^2,
\quad b^2-a^2=3a(a+\delta)>0.
\]
The latter positivity follows directly since \(a+\delta=[\sqrt{\delta^2+3r^2}+2\delta]/4>0\) for \(-r<\delta<r\). With \(m=R-a\), the smaller ball has stationary latitude
\[
t_s=\frac{a(m-s)}{b^2-a^2}=-\frac13,
\]
and direct substitution of the quadratic identity yields \(F_s(-1/3)=r^2\). The larger ball has stationary parameter
\[
t_0=\frac{a(R-a)}{3a(a+\delta)}=\frac{R-a}{3(a+\delta)}.
\]
Its maximum is at the pole \(t=1\), where \(F_0(1)=R^2\), exactly when
\[
t_0\ge1\iff R\ge4a+3\delta
\iff R\ge\sqrt{\delta^2+3r^2}+\delta
\iff s\le\frac{3(R^2-r^2)}{2R}=s_c.
\]
All squared inequalities are legitimate because \(R-\delta>0\) throughout the overlap interval. This proves containment and the asserted contact orbits, with the two contact types meeting at the threshold. Moreover \(s_c\ge R+r\) is equivalent to \(R\ge3r\). For \(R>r\), \(s_c>R-r\); hence the branch is always nonempty.

**3. The two-latitude construction and unique root.** Suppose \(r<R<3r\). For \(u>0\), write \(v=-1/(3u)\) and \(T=u^2\). Demand that the two spheres be tangent to the ellipsoid at their respective interior stationary latitudes \(u\) and \(v\), and that their squared distances equal \(R^2\) and \(r^2\). Define \(J=b^2(b^2-a^2)/a^2\) and \(B=b^2\). The two equalities become
\[
R^2=B+Ju^2,\qquad r^2=B+Jv^2,
\]
which uniquely yield the positive displayed \(B,J\) for \(T>R/(3r)\). Solving \(b^2-a^2=a^2J/B\) gives \(a=B/\sqrt{B+J}\). The stationary conditions give
\[
m=\frac{Ju}{\sqrt{B+J}},\qquad
s=\frac{J(u-v)}{\sqrt{B+J}}.
\]
Squaring the latter and eliminating \(u,v,B,J\) yields the displayed scalar equation for \(T\).

Let \(\Delta=R^2-r^2>0\), and define
\[
G(T)=\Delta^2\frac{3T+1}{3T-1}
\left[\Delta+r^2T-\frac{R^2}{9T}\right]^{-1}.
\]
On \(R/(3r)<T\le1\), both denominators are positive; the factor \((3T+1)/(3T-1)\) decreases strictly and the bracket increases strictly. Therefore \(G\) is continuous and strictly decreasing, with exact endpoint limits
\[
G(R/(3r)+)=(R+r)^2,\qquad G(1)=s_c^2.
\]
Since \(s_c<s<R+r\), one and only one root exists. It has \(1/3<T<1\), so \(0<u<1\), \(-1<v<0\), and \(B,J>0\) imply \(0<a<b\). The quadratic containment test proves both ball constraints with equality at those two interior latitudes. At \(T\uparrow1\), the larger-ball latitude becomes the pole; the unique optimum identified below proves coincidence with the preceding branch.

**4. Equal-ball branch.** For \(R=r\), symmetry fixes the center \(m=s/2\). Set \(b^2-a^2=(\sqrt3/2)as\), giving stationary latitudes \(t_0=1/\sqrt3\) and \(t_s=-1/\sqrt3\). Either ball's maximal squared distance equals \(R^2\) precisely when
\[
a^2+\frac{2s}{\sqrt3}a+\frac{s^2}{4}=R^2.
\]
Its unique positive root gives the displayed \(a\); then \(b\) follows. Both containment inequalities hold with equality at the stated latitudes.

**5. Exact global optimality without a symmetry restriction.** Apply the affine map taking the proposed ellipsoid to the unit ball \(B^3\). In normalized coordinates, the unit ball lies in the transformed lens, and each displayed contact latitude or pole is a supporting contact, since a contained ball and a convex body sharing a boundary point have the same supporting tangent plane there. For any two latitudes \(u>0\), \(v<0\) with \(uv=-1/3\), put weights
\[
p_u=\frac{-v}{u-v},\qquad p_v=\frac{u}{u-v}.
\]
Choose on each latitude a uniform circular distribution of total mass \(3p_u\) or \(3p_v\), interpreting the pole as a single point. Their combined weighted vector sum is zero, and their weighted covariance matrix is the identity: the axial variance is \(-uv=1/3\), while rotational symmetry gives each transverse variance \((1+uv)/2=1/3\). At the pole branch \(u=1,v=-1/3\); in the equal case \(u=1/\sqrt3,v=-1/\sqrt3\). These are therefore exact positive contact certificates.

For completeness, the certificate proves unrestricted uniqueness directly. Any inscribed competing ellipsoid, after this normalization, has the form \(z+A B^3\) with \(A\) positive definite and symmetric. Each unit contact \(w\) supplies its supporting inequality \(w\cdot z+\|Aw\|\le1\). Integrate using the weighted contact distribution: the mean-zero and identity-moment identities give
\[
\operatorname{tr}A=\int w\cdot Aw\,d\mu(w)
\le\int\|Aw\|\,d\mu(w)\le3.
\]
The arithmetic–geometric mean inequality gives \(\det A\le(\operatorname{tr}A/3)^3\le1\). Equality forces \(A=I\); the supporting equalities and spanning contact set force \(z=0\). Thus the constructed ellipsoid is uniquely maximum-volume among all ellipsoids contained in the lens. This also proves the claim of continuous coincidence at the threshold, by taking limits and uniqueness. No numerical optimization is used as a proof.

## Verification
The standalone `verify.py` reproduces the scalar root by bisection, samples different radius ratios and overlap separations, checks the exact maximum of each sphere-distance quadratic (not merely a boundary grid), checks the contact-latitude covariance equations and regime endpoints, and compares the equal-radius formula against its known symmetric-lens specialization. Execute `python verify.py` with Python 3; only the standard library is required. These finite diagnostics do not replace the exact derivation and contact-certificate proof. The physical volume follows from an axisymmetric ellipsoid's standard volume formula, not a Monte Carlo estimate.

## Relationship to prior work
Güler and Gürtuna (2007, arXiv:0709.0707) give general extremal-ellipsoid contact methods and exact examples for parallel-plane truncations, cones and ellipsoidal cylinders. Their inspected treatment does not specialize to two offset balls with unequal radii. Gruber and Schuster (2012, arXiv:1207.7246) prove John's classical contact characterization, which underlies but does not supply the present parameter classification. Finch (2013, arXiv:1301.5515) gives volume, area and mean-width data for equal-ball lens geometry, not asymmetric-lens John semiaxes. The separately published exact John ellipsoid of equal-radius two-ball lenses has \(R=r\) as a hypothesis and is recovered only by the displayed equal-ball branch. Another published result on the Löwner ellipsoid of the **convex hull** of unequal balls has the opposite optimization direction and a different convex body; it is not a covering theorem for this intersection. Kahan's 1968 study concerns circumscribed ellipsoids for a centered intersection of ellipsoids, not an inscribed ellipsoid for balls at distinct centers. No claim of exhaustive historical priority is made.

## Limitations
The result concerns two full-dimensional overlapping Euclidean balls in dimension three and exact radii and separation. The nested-ball case, external tangency and all higher dimensions lie outside its strict hypotheses. The construction gives exact population parameters, not a noisy-measurement inverse estimate. The originality comparison is based on inspected archival papers and the accessible published record; an undiscovered equivalent classical solution remains a residual risk. No independent mathematical audit is claimed.

## References
- O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707, first public version September 5, 2007, https://arxiv.org/abs/0709.0707.
- P. M. Gruber and F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246, first public version July 31, 2012, https://arxiv.org/abs/1207.7246.
- S. R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515, first public version January 23, 2013, https://arxiv.org/abs/1301.5515.
- M. J. Weber and H.-P. Schröcker, *Davis' Convexity Theorem and Extremal Ellipsoids*, arXiv:0907.1158, first public version July 7, 2009, https://arxiv.org/abs/0907.1158.
- *Exact John ellipsoids and contact latitudes of symmetric ball lenses in all dimensions*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-john-ellipsoids-and-contact-latitudes-of-symmetric-ball-le--02e413e91d3d.
- *A sharp contact bifurcation for the Löwner ellipsoid of two unequal balls*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-contact-bifurcation-for-the-l-wner-ellipsoid-of-two-uneq--424a15eeef51.
