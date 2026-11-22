# Sharp side slimness and contact bifurcation of ideal hyperbolic quadrilaterals

## Finding

Let \(Q\) be a nondegenerate ideal geodesic quadrilateral in the hyperbolic plane of curvature \(-1\). Define its *side slimness* by
\[
\delta(Q)=\max_{S\text{ side of }Q}\ \sup_{p\in S}
\operatorname{dist}_{\mathbb H^2}\!\left(p,\bigcup_{T\ne S}T\right).
\]
There is a hyperbolic isometry taking its cyclic ideal vertices to \((0,1,\lambda,\infty)\), with \(\lambda>1\), in the upper half-plane. The change of the starting vertex replaces \(\lambda\) by \(\lambda/(\lambda-1)\). Hence
\[
\kappa=\max\left\{\lambda,\frac{\lambda}{\lambda-1}\right\}\in[2,\infty)
\]
is an unmarked isometry invariant. The exact **complete one-parameter profile** is
\[
\boxed{\sinh^2\delta(Q)=
\begin{cases}
\kappa,&2\le\kappa\le3,\\[2pt]
\displaystyle\frac{\kappa}{\kappa-2},&\kappa\ge3.
\end{cases}}
\]
Consequently,
\[
\boxed{\delta(Q)\le\operatorname{arsinh}\sqrt3,}
\]
with equality **exactly** for the single unmarked isometry class \(\kappa=3\), equivalently \(\lambda=3\) or \(\lambda=3/2\) under a suitable side labeling. The regular ideal quadrilateral, \(\kappa=2\), is a strict local minimum within moduli, with \(\delta=\operatorname{arsinh}\sqrt2\). In the degenerating limit \(\kappa\to\infty\), \(\delta(Q)\downarrow\operatorname{arsinh}1\).

There is a further **maximizing-point/contact transition**. On a side corresponding to the larger cross-ratio parameter \(\kappa\), its distance from the other three sides has a unique maximizer when \(2\le\kappa\le3\), and exactly two distinct maximizers when \(\kappa>3\). At \(\kappa=3\) the unique maximizer is equally distant from all three other sides; above that value, each of the two maxima has the opposite side and one neighboring side at the same least distance. The two opposite sides of this type realize the global value.

## Assumptions and scope

All vertices are distinct ideal endpoints on the boundary at infinity, and each polygon side is the **entire** hyperbolic geodesic between its two ideal endpoints. The hyperbolic metric is \(ds=|dz|/\operatorname{Im}z\). In particular, no assertions about finite-vertex geodesic quadrilaterals, intrinsic four-point hyperbolicity, or the distance between opposite sides are implied. The use of \(\sup\) is important because the sides have infinite length; the proof shows the supremum in fact occurs at finite interior points.

The normalization to \((0,1,\lambda,\infty)\) follows from three-transitivity of hyperbolic boundary Möbius maps. Choosing the other pair of opposite sides as the distinguished pair replaces the parameter by \(\lambda/(\lambda-1)\). Thus \(\kappa\) parametrizes the unoriented/unmarked isometry classes.

## Proof

**1. Hyperbolic point-to-geodesic distance.** In the upper half-plane, for \(z=x+iy\) and real \(u<v\), let \(G_{u,v}\) be the geodesic semicircle with those endpoints. Reflection in that circle or a Möbius normalization gives
\[
\sinh\operatorname{dist}_{\mathbb H^2}(z,G_{u,v})
=\frac{|(x-u)(x-v)+y^2|}{(v-u)y}.
\]
For the vertical geodesic \(G_{v,\infty}\), the corresponding formula is \(\sinh\operatorname{dist}(x+iy,G_{v,\infty})=|x-v|/y\). These formulas describe distances to the *full* geodesics; these coincide with the entire ideal sides used here.

**2. Exact distance profile along a designated side.** Take \(S=G_{0,\infty}\), parametrize it by \(z=iy\), and write \(\lambda>1\). Its neighboring sides are \(G_{0,1}\) and \(G_{\lambda,\infty}\), and its opposite side is \(G_{1,\lambda}\). By step 1, the hyperbolic sine of the distance from \(iy\) to the union of the three sides is
\[
F_{\lambda}(y)=\min\left\{y,\frac{\lambda}{y},\frac{\lambda+y^2}{(\lambda-1)y}\right\},\qquad y>0.
\]
Put \(y=\sqrt\lambda\,x\). Then
\[
F_{\lambda}(\sqrt\lambda x)
=\sqrt\lambda\min\left\{x,x^{-1},\frac{x+x^{-1}}{\lambda-1}\right\}.
\]
This expression is unchanged under \(x\mapsto x^{-1}\), so it suffices to analyze \(0<x\le1\). There the first neighboring-side term equals \(x\), while the second is no smaller. The opposite-side term divided by \(x\) is \((1+x^{-2})/(\lambda-1)\). For \(1<\lambda\le3\), this ratio is at least one. Thus the profile equals \(\sqrt\lambda x\) until \(x=1\), where it has its **unique** maximum \(\sqrt\lambda\).

For \(\lambda>3\), there is precisely one switch in \((0,1)\), at \(x_*=(\lambda-2)^{-1/2}\). Below it the minimum is \(\sqrt\lambda x\), strictly increasing; above it the minimum is \(\sqrt\lambda(x+x^{-1})/(\lambda-1)\), strictly decreasing up to \(x=1\). By reciprocal symmetry, the only two maxima are \(x_*\) and \(x_*^{-1}\), both with value \(\sqrt{\lambda/(\lambda-2)}\). Therefore the squared hyperbolic sine of the maximum distance from a point of this side to the other three sides is
\[
H(\lambda)=\begin{cases}
\lambda,&1<\lambda\le3,\\[2pt]
\lambda/(\lambda-2),&\lambda\ge3.
\end{cases}
\]
The contact identities asserted above follow directly from which terms in the minimum are equal at these points. At \(\lambda=3\) all three terms agree at \(x=1\).

**3. All four sides and invariance.** The half-turn Möbius map \(z\mapsto(z-\lambda)/(z-1)\) interchanges the two sides \(G_{0,\infty}\) and \(G_{1,\lambda}\), so both have the same profile and maxima. A Möbius transformation followed if necessary by reflection takes either adjacent side to \(G_{0,\infty}\) in a normalized quadrilateral with parameter \(\tau=\lambda/(\lambda-1)\). Consequently
\[
\sinh^2\delta(Q)=\max\{H(\lambda),H(\tau)\}.
\]
Let \(\kappa=\max(\lambda,\tau)\). Since \(\lambda\tau=\lambda+\tau\), the smaller of these two values is exactly \(\kappa/(\kappa-1)\in(1,2]\), whose \(H\)-value is the parameter itself. For \(\kappa\in[2,3]\), \(H(\kappa)=\kappa\) dominates \(\kappa/(\kappa-1)\). For \(\kappa>3\), \(H(\kappa)=\kappa/(\kappa-2)>\kappa/(\kappa-1)\). The boxed profile follows, with the stated global maximizing sides.

**4. Sharpness, uniqueness and limiting behavior.** The function \(\kappa\mapsto H(\kappa)\) increases strictly from \(2\) to \(3\) on \([2,3]\), then decreases strictly from \(3\) to \(1\) on \((3,\infty)\). Since \(\operatorname{arsinh}\sqrt{t}\) is increasing for \(t>0\), the sharp global upper bound and unique extremizing unmarked isometry class follow. The regular square is the unique \(\kappa=2\) class; it is locally minimizing, though not a global minimum because the degenerating values approach the smaller limiting constant. The points of maximum are the ones identified in step 2, transported by the side symmetries. \(\square\)

## Verification

The accompanying `verify.py` uses the hyperbolic point-to-point distance
\[
\operatorname{arcosh}\left(1+\frac{|z-w|^2}{2\operatorname{Im}z\operatorname{Im}w}\right)
\]
for an **independent** numerical minimization along each geodesic semicircle. It compares those distances with the analytic point-to-side formula across thirteen cross-ratio values, verifies the predicted maximizers, checks the global envelope at over five thousand sample points and tests relabeling invariance. Run `python3 verify.py` with Python 3.9 or newer; it requires only the standard library. Numerical sampling supports the formulas but is not an exhaustive proof over continuous parameters. Steps 1–4 supply that proof.

## Relationship to prior work

Tselekidis (2026), *Logarithmically Slim Polygons*, §2.2 and §§3–5, develops the slimness notion for geodesic polygons and coarse dimension theorems. It does not give a cross-ratio-dependent formula for the slimness of ideal quadrilaterals. Wang, Vuorinen and Zhang (2019), *On cyclic quadrilaterals in Euclidean and hyperbolic geometries*, particularly Theorem 1.2 and its discussion, and Vuorinen–Wang (2013), Corollary 1.4, study **infimal pairwise distances between opposite sides** and related quantities. The present invariant instead maximizes, over a point on one side, the *minimum over its three other sides*; the two optimization orders are different and the older opposite-side bounds do not supply the formula or the \(\kappa=3\) contact transition. The known regular ideal-square value is a specialization and is not asserted as independently new.

## Limitations

The statement is restricted to ideal geodesic quadrilaterals in constant curvature \(-1\); changing the curvature scale multiplies all distances by the inverse square root of the curvature magnitude. The numerical verifier is supplementary and cannot replace the analytic proof. The novelty comparison covers the cited primary papers and focused mathematical-index queries; it does not exclude uncatalogued classical calculations of an equivalent invariant. Independent mathematical audit has not been performed.

## References

1. P. Tselekidis, *Logarithmically Slim Polygons*, arXiv:2611.05429v1, first posted 3 November 2026, https://arxiv.org/html/2611.05429v1.
2. G. Wang, M. Vuorinen and X. Zhang, *On cyclic quadrilaterals in Euclidean and hyperbolic geometries*, arXiv:1908.10389, https://arxiv.org/abs/1908.10389.
3. M. Vuorinen and G. Wang, *Hyperbolic Lambert quadrilaterals and quasiconformal mappings*, Ann. Acad. Sci. Fenn. Math. **38** (2013), 433–453, DOI:10.5186/aasfm.2013.3845, https://www.acadsci.fi/mathematica/Vol38/vol38pp433-453.pdf.
