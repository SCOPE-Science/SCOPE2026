# A Poisson-kernel law and exact eccentricity tomography on an ellipse's director circle

## Finding

Let \(E=\{(x,y):x^2/a^2+y^2/b^2\le1\}\) with \(a\ge b>0\). Independently choose a tangent orientation \(\Theta\) uniformly on \([0,2\pi)\). Let \(T_\theta\) be the *supporting tangent* with outward unit normal \(u_\theta=(\cos\theta,\sin\theta)\). Form \(Q=T_\Theta\cap T_{\Theta+\pi/2}\), and let \(\Psi=\arg Q\) in the axes of the ellipse. Put
\[
R=\sqrt{a^2+b^2},\qquad c=\frac{a^2-b^2}{a^2+b^2}\in[0,1).
\]
Then \(\|Q\|=R\) identically, and the pushforward of *uniform normal angle* is the exactly normalized density
\[
\boxed{f_c(\psi)=\frac{1-c\cos 2\psi}{2\pi(1-2c\cos2\psi+c^2)}
=\frac1{4\pi}\left[1+\frac{1-c^2}{1-2c\cos2\psi+c^2}\right]},\quad 0\le\psi<2\pi.
\]
In particular it is an exact equal-weight mixture of uniform circular measure and the Poisson-kernel measure in doubled angle. Its nonzero positive Fourier moments satisfy
\[
\boxed{\mathbb E(e^{2ik\Psi})=\frac{c^k}{2}\quad(k=1,2,\ldots),\qquad
\mathbb E(e^{i(2k+1)\Psi})=0\quad(k\in\mathbb Z)}.
\]
Also, with \(U\) denoting uniform circular probability measure,
\[
\boxed{\|\mathcal L(\Psi)-U\|_{\mathrm{TV}}=\frac{\arcsin c}{\pi}}.
\]
Thus a single second circular moment identifies the semiaxis ratio. For an ellipse rotated through \(\alpha\), the moment \(m=\mathbb E(e^{2i\Psi})=(c/2)e^{2i\alpha}\); for \(c>0\), \(\alpha\) is determined modulo \(\pi\) by \(\arg m/2\). Together with the director-circle radius, the entire ellipse is recovered by
\[
\boxed{c=2|m|,\quad a=R\sqrt{(1+c)/2},\quad b=R\sqrt{(1-c)/2}}.
\]
At \(c=0\) the ellipse is a circle and its axis orientation is undefined.

In the degenerating slender-ellipse limit \(c\uparrow1\), the angular measures converge weakly to
\[
\boxed{\frac12U+\frac14\delta_{0}+\frac14\delta_{\pi}}.
\]
More sharply, in the Poisson half of the exact mixture, condition on \(\Psi\in(-\pi/2,\pi/2)\) modulo \(2\pi\). Then \(2\Psi/(1-c)\) converges **in total variation** to the standard Cauchy distribution on \(\mathbb R\).

## Assumptions and scope

The sampling unit is the *outward normal direction*, not boundary arclength, contact-point eccentric anomaly, or an unordered pair of tangents. The pair \((T_\Theta,T_{\Theta+\pi/2})\) is ordered by a fixed positive quarter-turn. The ellipse is nondegenerate, \(0<b\le a<\infty\), and the origin is its center. Angle \(\alpha\) accounts for arbitrary rotation of its principal axes. All probability statements concern the pushforward of normalized Lebesgue measure \(d\theta/(2\pi)\). The weak and Cauchy limits refer to a family with \(b/a\to0\), without including a degenerate ellipse as a theorem case.

## Proof

**1. Exact orthoptic map.** The supporting-line equation is
\[
T_\theta:\quad x\cos\theta+y\sin\theta=h(\theta),\qquad
h(\theta)=\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}.
\]
The two perpendicular lines intersect at
\[
Q(\theta)=h(\theta)u_\theta+h(\theta+\pi/2)u_{\theta+\pi/2}.
\]
Since \(h(\theta)^2+h(\theta+\pi/2)^2=a^2+b^2=R^2\), every \(Q\) lies on the director circle. Its argument \(\psi(\theta)\) has the continuous derivative
\[
\psi'(\theta)=1+\frac{(a^2-b^2)\sin2\theta}{2h(\theta)h(\theta+\pi/2)}.
\]
The fraction has absolute value at most \(c<1\): square both sides and use \(4h(\theta)^2h(\theta+\pi/2)^2=R^4-(a^2-b^2)^2\cos^2(2\theta)\). Therefore \(\psi'(\theta)>0\) throughout. Furthermore \(Q(\theta+2\pi)=Q(\theta)\) with winding number one, because its factor \(h(\theta)+ih(\theta+\pi/2)\) remains in the open first quadrant. Consequently \(\theta\mapsto\psi\) is a circle diffeomorphism.

**2. Inverse Jacobian.** At \(Q=(R\cos\psi,R\sin\psi)\), a supporting unit normal \((\cos\theta,\sin\theta)\) satisfies \(Q\cdot u_\theta=h(\theta)>0\). Squaring and using \(\|Q\|^2=R^2\) gives
\[
(\cos2\psi-c)\cos2\theta+\sin2\psi\sin2\theta=0.
\]
Thus \(2\theta\equiv\arg(e^{2i\psi}-c)-\pi/2\pmod\pi\), and differentiating its continuous branch yields
\[
\frac{d\theta}{d\psi}=\operatorname{Re}\frac{e^{2i\psi}}{e^{2i\psi}-c}
=\frac{1-c\cos2\psi}{1-2c\cos2\psi+c^2}>0.
\]
Pushforward of \(d\theta/(2\pi)\) proves the displayed density, and also verifies its normalization directly.

**3. Harmonic moments and inversion.** Write \(P_c(t)=(1-c^2)/(1-2c\cos t+c^2)\). The elementary Poisson series
\[
P_c(t)=1+2\sum_{k\ge1}c^k\cos(kt)
\]
converges uniformly for each \(0\le c<1\). Hence
\[
f_c(\psi)=\frac1{2\pi}\left[1+\sum_{k\ge1}c^k\cos(2k\psi)\right].
\]
Fourier orthogonality gives the moments. Rotating the ellipse by \(\alpha\) rotates \(Q\) by \(\alpha\), multiplying the second moment by \(e^{2i\alpha}\); the reconstruction formula follows by solving \(a^2+b^2=R^2\) and \(a^2-b^2=cR^2\).

**4. Exact total variation.** Since \(f_c-1/(2\pi)=(P_c(2\psi)-1)/(4\pi)\), the density difference is positive precisely when \(\cos2\psi>c\). Put \(v=\arccos c\). Over one full period of \(t=2\psi\), direct tangent-half-angle integration gives
\[
\int_{-v}^{v}P_c(t)\,dt=\pi+2\arcsin c,
\qquad \int_{-v}^{v}1\,dt=\pi-2\arcsin c.
\]
Taking the integral of the positive part yields the total-variation formula \(\arcsin(c)/\pi\), including \(c=0\) by continuity.

**5. Flattening and the local law.** The exact mixture is \(\tfrac12U+\tfrac12\nu_c\), where \(\nu_c(d\psi)=P_c(2\psi)d\psi/(2\pi)\). The approximate-identity property of the Poisson kernel yields \(\nu_c\Rightarrow\tfrac12(\delta_0+\delta_\pi)\). Restrict \(\nu_c\) to the interval \((-\pi/2,\pi/2)\) and normalize; this event has probability exactly \(1/2\), by period \(\pi\). With \(\delta=1-c\), the density of \(X_c=2\Psi/\delta\), extended by zero outside its support, is
\[
 g_c(x)=\frac{\delta}{2\pi}P_c(\delta x)\,\mathbf1_{\{|x|<\pi/\delta\}}.
\]
For each real \(x\), \(g_c(x)\to1/[\pi(1+x^2)]\). Both \(g_c\) and the limit integrate to one, so Scheffé's lemma proves convergence in total variation.

## Verification

The derivation is analytical, not inferred from numerical sampling. The standalone script `verify.py` checks the two-line intersection, monotone Jacobian, pushforward density identity, second and fourth Fourier moments, the exact total-variation expression, and the Cauchy scaled-limit density on deterministic grids for multiple axis ratios. `checks.txt` contains the actual run output; numerical integration is supplementary and cannot certify the infinite Fourier series or total-variation limit.

## Relationship to prior work

The classical director-circle locus and its radius are established in Odehnal's 2010 account of isoptics of conics; no priority is asserted for that circle. Csima–Szirmai (2013) review isoptic constructions in constant-curvature planes. Cieślak–Mozgawa (2021) present the general support-function parametrization of an orthoptic and characterize curves with a circular orthoptic, including nonellipses; their equations give a general starting point but not this normal-angle pushforward, its Poisson mixture, sharp total variation, inverse moment or singular probabilistic limit. The 2008 Csima–Szirmai–Tóth interactive ellipse-isoptic parametrization likewise describes locations, not a normal-angle probability law. This report claims only the explicit *sampling-induced distribution and consequences*; the general parametrization is prior work.

## Limitations

Uniformity with respect to arclength would yield a different law. The inverse formula is asserted only among ellipses and does not characterize ellipses among every oval with circular orthoptic. The formula only covers the specified normal-angle sampling and not arclength or eccentric-anomaly sampling. It does not classify arbitrary nonelliptic ovals with circular orthoptics. Historical reports may contain unexamined angular parametrizations with consequences for priority.

## References

1. Boris Odehnal, *Equioptic curves of conic sections*, dated 16 August 2010, https://www.geometrie.tuwien.ac.at/odehnal/tr200.pdf ; journal version *Journal for Geometry and Graphics* 14 (2010), 29–43, https://www.heldermann-verlag.de/jgg/jgg14/j14h1odeh.pdf .
2. Géza Csima and Jenő Szirmai, *Isoptic curves of conic sections in constant curvature geometries*, arXiv:1301.6991, first submitted 29 January 2013, https://arxiv.org/abs/1301.6991 .
3. Waldemar Cieślak and Witold Mozgawa, *On curves with circles as their isoptics*, first published 28 June 2021, https://doi.org/10.1007/s00010-021-00828-4 .
4. Géza Csima, Jenő Szirmai and János Tóth, *Iso-Optic Curve of the Ellipse*, Wolfram Demonstrations Project (2008), https://demonstrations.wolfram.com/IsoOpticCurveOfTheEllipse/ .
