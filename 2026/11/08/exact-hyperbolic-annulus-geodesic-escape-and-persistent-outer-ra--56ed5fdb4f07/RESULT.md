# Exact hyperbolic-annulus geodesic escape and persistent outer-radius visibility loss

## Finding
Let \(o\in\mathbb H^2\) in the complete hyperbolic plane of constant curvature \(-1\), and let \(0<a<b<\infty\). Sample \(X,Y\) independently with normalized hyperbolic area measure on the open geodesic annulus \(A_{a,b}=\{z:a<d(o,z)<b\}\). Set \(P(a,b)=\Pr([X,Y]_{\mathbb H}\cap B_a(o)\ne\varnothing)\), where \([X,Y]_{\mathbb H}\) is the unique minimizing ambient hyperbolic geodesic segment and \(B_a(o)\) is the *open* radius-\(a\) ball. Tangency events have probability zero. Define
\[
\theta_{a,b}=\arccos\!\left(\frac{\tanh a}{\tanh b}\right),\qquad
J_{a,b}=\cosh b\,\theta_{a,b}-\arctan\!\left(\frac{\sqrt{\cosh^2b-\cosh^2a}}{\sinh a}\right).
\]
Then the exact probability is
\[
\boxed{P(a,b)=1-\frac{2J_{a,b}}{\pi(\cosh b-\cosh a)}.}
\]
For each fixed \(a>0\), \(P(a,b)\) is strictly decreasing in \(b>a\), and has the sharp limiting regimes
\[
\boxed{1-P(a,a+\varepsilon)=\frac4{3\pi}\sqrt{\frac{2\varepsilon}{\sinh a\cosh a}}+O_a(\varepsilon^{3/2}),\quad\varepsilon\downarrow0,}
\]
\[
\boxed{\lim_{b\to\infty}P(a,b)=\frac2\pi\arcsin(\tanh a)>0.}
\]
Thus **a fixed positive-radius disk obstructs a strictly positive fraction of ambient geodesics joining independently area-uniform points in arbitrarily large hyperbolic annuli**, unlike Euclidean annuli. For Euclidean annuli, the corresponding probability is
\[
P_E(a,b)=1-\frac{2}{\pi}\frac{b^2\arccos(a/b)-a\sqrt{b^2-a^2}}{b^2-a^2},\qquad \lim_{b\to\infty}P_E(a,b)=0.
\]
The formulas are for area-uniform *endpoints*, not randomly selected complete geodesics with Liouville measure, and use the geodesic in the ambient plane, not the shortest path constrained to the annulus.

## Assumptions and scope
The curvature is \(-1\), all radii are dimensionless hyperbolic distances, \(0<a<b\), and independently sampled endpoints follow normalized Riemannian area, not uniform radius. Hyperbolic polar coordinates about \(o\) have area element \(\sinh r\,dr\,d\vartheta\). The induced radius \(R=d(o,X)\) has density
\[
f_{a,b}(r)=\frac{\sinh r}{\cosh b-\cosh a}\,\mathbf1_{(a,b)}(r),
\]
and the endpoint angles are independent Haar-uniform on \([0,2\pi)\). Closed/open annulus conventions have the same probability by boundary nullity. For curvature \(-\kappa^2\), \(\kappa>0\), replace \(a,b\) by \(\kappa a,\kappa b\) in \(P\).

## Proof
**1. The deterministic tangent criterion.** In the Klein disk model, hyperbolic geodesics are Euclidean line segments and the Euclidean radius of a point at hyperbolic radius \(r\) is \(\rho=\tanh r\). The hyperbolic ball \(B_a(o)\) is the Euclidean central disk of radius \(t=\tanh a\). For endpoints with radial coordinates \(r,s>a\), let \(\Delta\in[0,\pi]\) be their smaller angular difference. The segment intersects the open central disk exactly when
\[
\Delta>\psi_a(r)+\psi_a(s),\qquad
\psi_a(r)=\arccos\!\left(\frac{\tanh a}{\tanh r}\right).
\]
Indeed, from a point of radius \(\rho>t\), the two tangents to the disk touch it at polar angles displaced by \(\arccos(t/\rho)\) from the point's polar angle. Increasing the angular separation of two fixed-radius endpoints first produces disk contact when the two inward tangents form the same line, precisely at the sum of these two angles. Below this threshold the segment is separated from the disk by a tangent line; above it the segment crosses the disk. Endpoint and tangent degeneracies are null under the sampling law.

**2. Average over angles and independent radii.** Conditional on \(r,s\), \(\Delta\) is uniform on \([0,\pi]\). Moreover \(0<\psi_a(r),\psi_a(s)<\pi/2\), so the criterion yields
\[
\Pr(\text{escape}\mid r,s)=1-\frac{\psi_a(r)+\psi_a(s)}\pi.
\]
Independence and the radial density give
\[
P(a,b)=1-\frac2{\pi(\cosh b-\cosh a)}\int_a^b\sinh r\,\psi_a(r)\,dr.\tag{1}
\]

**3. Elementary evaluation.** Put \(c=\cosh a\), \(s=\sinh a\), \(x=\cosh r\) and \(\psi(r)=\psi_a(r)\). Direct differentiation gives
\[
\psi'(r)=\frac{\sinh a}{\sinh r\sqrt{\cosh^2r-\cosh^2a}}.
\]
Integrate (1) by parts, using \(\psi(a)=0\):
\[
\int_a^b \sinh r\,\psi(r)\,dr
=\cosh b\,\psi(b)-\int_a^b\cosh r\,\psi'(r)\,dr.
\]
For the last integral, substitute \(u=\sqrt{\cosh^2r-\cosh^2a}\). Since \(\sinh^2r=u^2+s^2\), its differential becomes \(s\,du/(u^2+s^2)\), whose integral from \(0\) to \(\sqrt{\cosh^2b-c^2}\) is \(\arctan(\sqrt{\cosh^2b-c^2}/s)\). This is exactly \(J_{a,b}\), proving the closed formula without numerical approximation.

**4. Strict outer-radius monotonicity.** Fix \(a\). The cdf of \(R\) when the outer radius is \(b\) is \((\cosh r-\cosh a)/(\cosh b-\cosh a)\) for \(a<r<b\). It is strictly stochastically increasing in \(b\), while \(\psi_a(r)\) is strictly increasing in \(r\). Equation (1) therefore makes \(P(a,b)\) strictly decreasing with \(b\).

**5. Two sharp limits.** If \(b=a+\varepsilon\), Taylor expansion at fixed \(a>0\) gives uniformly for \(0\le u\le\varepsilon\)
\[
\psi_a(a+u)=\sqrt{\frac{2u}{\sinh a\cosh a}}+O_a(u^{3/2}),\qquad
\sinh(a+u)=\sinh a+O_a(u).
\]
Their normalized integral has leading mean \(\frac23\sqrt\varepsilon\), and the weighted error is \(O_a(\varepsilon^{3/2})\). Substitution into (1) gives the announced thin-annulus coefficient.

For fixed \(a>0\), as \(b\to\infty\) the random \(R\) tends to infinity in probability: for any fixed \(T>a\), \(\Pr(R\le T)=(\cosh T-\cosh a)/(\cosh b-\cosh a)\to0\). The bounded continuous function \(\psi_a(R)\) tends in probability to \(\arccos(\tanh a)\). Bounded convergence then gives \(P(a,b)\to1-(2/\pi)\arccos(\tanh a)=(2/\pi)\arcsin(\tanh a)\). The limit is strictly between zero and one.

**6. Euclidean comparison.** In a Euclidean annulus the same tangent argument has \(\psi_E(r)=\arccos(a/r)\), and the area-uniform radial density is \(2r/(b^2-a^2)\). Integration by parts gives \(\int_a^b2r\psi_E(r)dr=b^2\arccos(a/b)-a\sqrt{b^2-a^2}\), which yields the displayed \(P_E\) and its zero outer-radius limit. The curvature-\(-\kappa^2\) law converges to \(P_E(a,b)\) for each fixed \(0<a<b\) as \(\kappa\downarrow0\), by the polar-area density and tangent-angle limits.

## Verification
The standalone `check_hyperbolic_annulus.py` calculates the closed form, an independently integrated one-dimensional expression (composite Simpson quadrature), and a second independent geometric test using hyperboloid coordinates to find the minimum radial distance along each ambient geodesic segment, *without using the Klein tangent threshold*. The script tests distinct ordinary, very thin and wide annuli, checks monotonicity and the two limiting laws, and uses a reproducible random seed. Its Monte Carlo checks are finite diagnostics, not a replacement for Steps 1–6. To run: `python3 check_hyperbolic_annulus.py` (Python standard library only). The paper's exact infinite claims rely on the explicit geometric and calculus proofs.

## Relationship to prior work
Binbin Xu, *On the Ambartzumian-Pleijel identity in hyperbolic geometry* (first arXiv version October 15, 2014), establishes hyperbolic Crofton/Pleijel identities and Liouville-random chord-length distributions for ideal polygons; those sample *geodesics*, not two independent area-uniform points of a finite nonconvex annulus. Cammarota–Orsingher, *Hitting spheres on hyperbolic spaces* (first arXiv version April 6, 2011), studies hyperbolic Brownian hitting and annular exit probabilities, not deterministic minimizing connections between two iid endpoints. Calka–Tykesson, *Asymptotics of visibility in the hyperbolic plane* (first arXiv version December 23, 2010), studies Poisson Boolean obstacle fields and rays from a fixed observer, not one fixed disk and a random pair. The earlier Euclidean concentric-hole Beer-index law is for Euclidean-area sampling with straight Euclidean segments and does not state this hyperbolic formula or the strictly positive infinite-radius limit. Spherical shell and band results concern different ambient geometries, metrics and sampling laws. The new claim is the explicit hyperbolic area-uniform annulus law together with its strict monotonicity and asymptotic curvature contrast; it is not a claim to invent tangent geometry, polar integration or general Crofton formulas.

## Limitations
The full conclusion is for constant negative curvature in dimension two, concentric geodesic disks and two independent area-uniform points. We do not assert novelty of the tangent criterion alone, a result for nonconcentric obstacles, other dimensions, or Liouville-distributed random complete geodesics. The strict positive limiting probability is *not* a claim about the probability of avoiding infinitely many random obstacles. Related specialized historical sources might contain an equivalent endpoint-sampling calculation despite no equivalent statement found in checked material. Independent audit has not been performed.

## References
1. P. Calka and J. Tykesson, *Asymptotics of visibility in the hyperbolic plane*, first public arXiv version December 23, 2010, arXiv:1012.5220, https://arxiv.org/abs/1012.5220.
2. V. Cammarota and E. Orsingher, *Hitting spheres on hyperbolic spaces*, first public arXiv version April 6, 2011, arXiv:1104.1043, https://arxiv.org/abs/1104.1043.
3. B. Xu, *On the Ambartzumian-Pleijel identity in hyperbolic geometry*, first public arXiv version October 15, 2014, arXiv:1410.4052, https://arxiv.org/abs/1410.4052.
