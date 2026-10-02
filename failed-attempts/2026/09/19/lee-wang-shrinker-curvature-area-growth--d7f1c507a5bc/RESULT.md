# Exact curvature and Euclidean area-growth laws for Lee--Wang Lagrangian shrinkers

## Statement

Let \(p>q\ge 1\) be coprime integers and put
\[
 d=p-q,\qquad s=p+q,\qquad P=pq.
\]
Rescale the Lee--Wang Hamiltonian-stationary shrinker to the standard self-shrinker normalization
\[
Y_{p,q}(\mu,\theta)
=\sqrt{\frac{2d}{P}}\,
\bigl(\sqrt q\cosh\mu\,e^{ip\theta},\ i\sqrt p\sinh\mu\,e^{-iq\theta}\bigr),
\qquad (\mu,\theta)\in\mathbb R\times(\mathbb R/2\pi\mathbb Z),
\]
so that \(\mathbf H=-Y^\perp/2\). The following global geometric formulas hold for the parameterized cylinder (area is counted with immersion multiplicity when the image self-intersects).

### 1. Strict negative curvature and exact total curvature

Writing \(C=\cosh(2\mu)\), the induced metric and Gaussian curvature are
\[
 g=\frac{d(sC+d)}{P}\,d\mu^2+d(sC+d)\,d\theta^2,
\]
\[
 \boxed{
 K(\mu)=-\frac{2Ps\,(s+dC)}{d(sC+d)^3}<0 .
 }
\]
Moreover,
\[
 \boxed{\int K\,dA=-4\pi\sqrt{pq}.}
\]
Each of the two asymptotic Schoen--Wolfson cone links has length \(2\pi\sqrt{pq}\), so the absolute total Gaussian curvature is exactly the sum of the two link lengths.

### 2. Exact centered ball area and a unique area-ratio overshoot

The minimum Euclidean radius on the cylinder is
\[
 R_{\min}=\sqrt{\frac{2d}{p}}.
\]
For \(R\ge R_{\min}\), define \(a=a(R)\ge0\) by
\[
 \cosh(2a)=\frac{PR^2+d^2}{ds}.
\]
Then
\[
 \boxed{
 \operatorname{Area}\bigl(Y_{p,q}\cap B_R(0)\bigr)
 =\frac{2\pi d}{\sqrt P}\bigl(s\sinh(2a)+2da\bigr).
 }
\]
Equivalently,
\[
 \operatorname{Area}\bigl(Y_{p,q}\cap B_R(0)\bigr)
 =\frac{2\pi}{\sqrt P}
 \left[
 \sqrt{(PR^2-2qd)(PR^2+2pd)}
 +d^2\operatorname{arcosh}\!\left(\frac{PR^2+d^2}{ds}\right)
 \right].
\]
The centered Euclidean area ratio
\[
 \Theta_{p,q}(R)=\frac{\operatorname{Area}(Y_{p,q}\cap B_R(0))}{\pi R^2}
\]
therefore has the exact parameterization
\[
 \boxed{
 \Theta_{p,q}(a)
 =2\sqrt P\,\frac{s\sinh(2a)+2da}{s\cosh(2a)-d}.
 }
\]
It has exactly one critical point on \((0,\infty)\), which is its strict global maximum. The maximizing parameter \(a_*\) is the unique positive solution of
\[
 \boxed{ds\,a_*\sinh(2a_*)=2P.}
\]
The asymptotic cone density (counting the two parameterized ends) is \(2\sqrt P\). The ratio starts below this density, crosses it exactly once, and then approaches it from above. The unique crossing parameter \(a_0>0\) is characterized by
\[
 \boxed{2da_0+d=s e^{-2a_0}.}
\]
Thus the centered Euclidean area ratio is not monotone: every Lee--Wang shrinker in this family exhibits a single finite-radius overshoot above its conical density.

More precisely,
\[
 \boxed{
 \operatorname{Area}(Y_{p,q}\cap B_R)
 =2\pi\sqrt P\,R^2
 +\frac{4\pi d^2}{\sqrt P}\log R
 +\frac{2\pi d^2}{\sqrt P}
 \left(1+\log\frac{2P}{ds}\right)
 +O(R^{-2}).
 }
\]
In particular, the excess over the limiting two-cone area is positive and logarithmically divergent:
\[
 \operatorname{Area}(Y_{p,q}\cap B_R)-2\pi\sqrt P\,R^2
 =\frac{4\pi d^2}{\sqrt P}\log R+O(1).
\]

### 3. The stable embedded Möbius shrinker

For \((p,q)=(2,1)\), the standard normalization is already the parametrization used by Braxton--Lee--Zhu,
\[
 X(\theta,r)=(e^{2i\theta}\cosh r,\sqrt2\,e^{-i\theta}\sinh r),
\]
and the involution \((\theta+\pi,-r)\sim(\theta,r)\) gives the embedded Möbius shrinker \(M\). Since the cylindrical parametrization is a twofold cover of \(M\), the preceding area and curvature integrals halve. One obtains
\[
 \boxed{
 K(r)=-\frac{12(\cosh 2r+3)}{(3\cosh 2r+1)^3},
 \qquad
 \int_M K\,dA=-2\pi\sqrt2.
 }
\]
Here \(K(0)=-3/4\), and \(K\) increases strictly toward \(0\) with \(|r|\).

For \(R\ge1\),
\[
 \boxed{
 A_M(R)=\pi\sqrt2\left[
 \sqrt{(R^2-1)(R^2+2)}
 +\frac12\operatorname{arcosh}\!\left(\frac{2R^2+1}{3}\right)
 \right].
 }
\]
If \(a=\tfrac12\operatorname{arcosh}((2R^2+1)/3)\), then
\[
 \frac{A_M(R)}{\pi R^2}
 =\sqrt2\,\frac{3\sinh(2a)+2a}{3\cosh(2a)-1}.
\]
Its unique global maximum occurs at
\[
 3a_*\sinh(2a_*)=4,
\]
with
\[
 a_*\approx0.7000655576,\qquad
 R_*\approx1.6512789741,\qquad
 \boxed{\max_R\frac{A_M(R)}{\pi R^2}\approx1.8448061591.}
\]
The ratio crosses the asymptotic density \(\sqrt2\) once, at
\[
 a_0\approx0.3088212334,\qquad R_0\approx1.1381228651,
\]
and approaches \(\sqrt2\) from above. Its large-radius expansion is
\[
 \boxed{
 A_M(R)=\pi\sqrt2\left[
 R^2+\log R+\frac12\left(1+\log\frac43\right)+O(R^{-2})
 \right].
 }
\]
The link of the asymptotic cone has length \(2\pi\sqrt2\), so in this one-ended quotient
\[
 \left|\int_MK\,dA\right|=\operatorname{Length}(\text{asymptotic link}).
\]

Finally, the noncontractible systole of the induced metric on \(M\) is
\[
 \boxed{\operatorname{sys}(M)=2\pi,}
\]
attained by the core circle \(r=0\). It is the unique systolic closed geodesic up to reparametrization and orientation.

## Proof

Lee--Wang compute the unscaled metric
\[
 g_{\mu\mu}=p\cosh^2\mu+q\sinh^2\mu
 =\frac{s\cosh(2\mu)+d}{2},
 \qquad
 g_{\theta\theta}=P g_{\mu\mu}.
\]
Scaling by \(2d/P\) gives the displayed standard-normalization metric. Locally put \(y=\sqrt P\,\theta\); then
\[
 g=E(\mu)(d\mu^2+dy^2),
 \qquad E(\mu)=\frac{d(s\cosh2\mu+d)}{P}.
\]
The conformal-curvature formula \(K=-(2E)^{-1}(\log E)''\) gives the stated \(K\), which is strictly negative.

The area form is
\[
 dA=\frac{d}{\sqrt P}(s\cosh2\mu+d)\,d\mu\,d\theta.
\]
Hence
\[
 K\,dA
 =-2\sqrt P\,s\frac{s+d\cosh2\mu}{(s\cosh2\mu+d)^2}\,d\mu\,d\theta.
\]
With \(t=\tanh\mu\), the remaining one-dimensional factor becomes
\[
 s\frac{s+d\cosh2\mu}{(s\cosh2\mu+d)^2}\,d\mu
 =\frac{s}{2}\frac{p-qt^2}{(p+qt^2)^2}\,dt
 =\frac{s}{2}\,d\!\left(\frac{t}{p+qt^2}\right).
\]
Its integral from \(-1\) to \(1\) is \(1\), giving \(\int KdA=-4\pi\sqrt P\).

Also
\[
 |Y_{p,q}|^2=\frac dP(s\cosh2\mu-d),
\]
so \(B_R\) cuts out exactly \(|\mu|\le a(R)\). Integrating the area form on that strip gives the ball-area formula. The radical form follows from
\[
 d^2s^2\sinh^2(2a)
 =(PR^2-2qd)(PR^2+2pd).
\]
Dividing by \(\pi R^2\) yields \(\Theta_{p,q}\). Direct differentiation gives
\[
 \Theta_{p,q}'(a)
 =\frac{8\sqrt P\,[2P-ds\,a\sinh(2a)]}{(s\cosh(2a)-d)^2}.
\]
Since \(a\sinh(2a)\) is strictly increasing from \(0\) to \(\infty\), there is exactly one critical point and it is the strict global maximum. Likewise,
\[
 \Theta_{p,q}(a)-2\sqrt P
 =\frac{2\sqrt P\,[2da+d-se^{-2a}]}{s\cosh(2a)-d}.
\]
The numerator is strictly increasing, starts at \(-2q\), and tends to \(+\infty\), proving the unique crossing. Expanding the exact radical/arcosh area formula at infinity gives the stated logarithmic correction.

For \((p,q)=(2,1)\), the quotient halves both area and total curvature. The special curvature formula follows by substitution. For the systole, lift to \((\theta,r)\in\mathbb R^2\), where the deck generator is
\[
 T(\theta,r)=(\theta+\pi,-r).
\]
Since \(\omega(r)=\sinh^2r+2\cosh^2r\ge2\),
\[
 g=2\omega\,d\theta^2+\omega\,dr^2\ge4\,d\theta^2+2\,dr^2.
\]
Any loop in the nontrivial primitive homotopy class lifts from a point to its image under \(T\), hence has length at least \(2\pi\). The core \(r=0\) realizes equality. Equality forces \(r\equiv0\) and no angular backtracking, giving uniqueness of the systolic geodesic.

## Context and originality boundary

Lee--Wang constructed the \((p,q)\) Hamiltonian-stationary shrinkers, computed their induced metric and area form, and proved their asymptotics to Schoen--Wolfson cones. Braxton--Lee--Zhu recently proved that the \((2,1)\) Möbius quotient is \(F\)-stable; their paper records its metric, second fundamental form, asymptotic link, and an exact Gaussian entropy formula. Those are prior results and are not claimed here.

To the best of our knowledge, the exact Gaussian-curvature and total-curvature formulas above, the exact centered Euclidean ball-area profile, its unique finite-radius overshoot and crossing law, the positive logarithmic area excess, and the Möbius systole statement have not previously been stated for the Lee--Wang family. The closely related classification by Castro--Lerma was also checked for these formulations without locating an equivalent result.

A residual originality risk remains because the motivating stability preprint is very recent, and a forthcoming Braxton thesis on the same Möbius shrinker was cited there but was not available for inspection.

## Limitations

- The general \((p,q)\) area statements concern the parameterized Lee--Wang cylinder and therefore count immersion multiplicity; except for the \((2,1)\) Möbius quotient, the images are not embedded.
- These formulas do not prove nonlinear dynamical stability, occurrence as a singularity of a compact flow, or stability for the other \((p,q)\) shrinkers.
- The Euclidean centered area ratio is distinct from the Gaussian \(F\)-functional/entropy; the exact entropy of the stable Möbius shrinker is already known from Braxton--Lee--Zhu.
- The originality claim is to the best of our knowledge and retains the specific uninspected-source risk noted above.

## References

1. Y.-I. Lee and M.-T. Wang, *Hamiltonian Stationary Shrinkers and Expanders for Lagrangian Mean Curvature Flows*, J. Differential Geom. 83 (2009), 27--42. arXiv:0707.0239. DOI: 10.4310/jdg/1253804350.
2. K. Braxton, T.-K. Lee, J. J. Zhu, *A stable self-shrinking Möbius bundle in R^4*, arXiv:2609.19648 (2026).
3. I. Castro and A. M. Lerma, *Hamiltonian stationary self-similar solutions for Lagrangian mean curvature flow in complex Euclidean plane*, Proc. Amer. Math. Soc. 138 (2010), 1821--1832. arXiv:0906.3117.
