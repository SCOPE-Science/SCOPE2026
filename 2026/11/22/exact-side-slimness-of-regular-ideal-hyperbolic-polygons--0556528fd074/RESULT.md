# Exact side slimness of regular ideal hyperbolic polygons

## Finding

In the curvature-\(-1\) hyperbolic plane, let \(P_n\) be the regular ideal \(n\)-gon with vertices at equally spaced points of the ideal boundary, for any integer \(n\ge3\). Define its polygonal side slimness by
\[
\delta(P_n)=\max_{0\le j<n}\ \sup_{z\in E_j}\inf_{w\in\bigcup_{k\ne j}E_k}d_{\mathbb H}(z,w),
\]
where \(E_j\) are the complete geodesic sides, without adjoining their ideal endpoints. Then
\[
\boxed{\delta(P_n)=\operatorname{arsinh}\!\left(2\cos\frac{\pi}{n}\right).}
\]
The only maximizing point on each side is its hyperbolic midpoint, and its two adjacent sides are precisely the nearest other sides (for \(n=3\), these are all other sides). Consequently the exact sequence is strictly increasing with \(n\), yet bounded, with
\[
\delta(P_n)=\operatorname{arsinh}2-\frac{\pi^2}{\sqrt5\,n^2}+O(n^{-4}).
\]
Thus the regular ideal polygons furnish a bounded-slimness benchmark even when their number of sides tends to infinity; this does not bound the supremum over arbitrary geodesic polygons.

## Assumptions and scope

The curvature normalization is \(-1\); distances scale inversely with the square root of the absolute curvature. Vertices are *ideal*, so this concerns the unions of complete geodesic sides, not geodesic polygons with finite vertices. The side slimness is a finite real number because the distance from any side point to an adjacent side tends to zero at each common ideal endpoint. All assertions hold for integers \(n\ge3\), with no unspecified regularity assumptions.

## Proof

Write \(\theta=\pi/n\), and use the Poincaré unit disk. By symmetry choose the side \(E_0\) with endpoints \(e^{\pm i\theta}\). The Euclidean supporting circle of this hyperbolic geodesic has center \(c_0=\sec\theta\) and radius \(R=\tan\theta\); the hyperbolic midpoint is the real point
\[
r=\sec\theta-\tan\theta=\frac{\cos\theta}{1+\sin\theta}.
\]
The other supporting circles have centers \(c_k=\sec\theta\,e^{2ik\theta}\), \(k=1,\ldots,n-1\), and the same radius \(R\). The hyperboloid model, or a direct perpendicular-geodesic computation, gives the distance from a disk point \(z\) to the complete geodesic with Euclidean supporting center \(c\), radius \(R=\sqrt{|c|^2-1}\):
\[
\sinh d_{\mathbb H}(z,E)=\frac{\big|1+|z|^2-2\operatorname{Re}(\overline c z)\big|}{(1-|z|^2)R}.
\tag{1}
\]
Indeed, in hyperboloid coordinates the numerator divided by the denominator is the absolute Lorentz product with the unit spacelike normal of the geodesic, hence equals the hyperbolic sine of the perpendicular distance.

The point \(r\) lies on \(E_0\), so \(1+r^2=2r\sec\theta\). Substitute into (1), and use \(1-r^2=2\sin\theta/(1+\sin\theta)\): for \(1\le k\le n-1\),
\[
\sinh d_{\mathbb H}(r,E_k)
=2\cos\theta\,\frac{\sin^2(k\theta)}{\sin^2\theta}.
\tag{2}
\]
Since \(\sin(k\theta)\ge\sin\theta\) for these integers, with equality exactly when \(k=1\) or \(k=n-1\), the nearest other sides at the midpoint are the two adjacent ones, and their common distance equals \(\operatorname{arsinh}(2\cos\theta)\).

It remains to prove no different point on \(E_0\) has a larger nearest-side distance. An isometry to the upper half-plane sends \(E_0\) to the imaginary axis and its midpoint to \(i\). Parameterize its points as \(ie^s\), \(s\in\mathbb R\). One adjacent side is a vertical line sharing the ideal endpoint \(\infty\), and the other is a semicircle sharing the endpoint \(0\). The perpendicular-distance formulas in the upper half-plane give their distances from \(ie^s\) as
\[
\operatorname{arsinh}(C e^{-s}),\qquad\operatorname{arsinh}(C e^{s}),
\]
respectively, where symmetry about the midpoint makes the two positive constants equal, and (2) gives \(C=2\cos\theta\). Hence the distance to the union of *all* other sides is bounded above by
\[
\min\{\operatorname{arsinh}(Ce^s),\operatorname{arsinh}(Ce^{-s})\}
=\operatorname{arsinh}(Ce^{-|s|})\le\operatorname{arsinh}C,
\]
with strict inequality for \(s\ne0\). Formula (2) verifies equality at \(s=0\); rotational symmetry transfers it to every side. This proves the exact formula and unique maximizing points.

Finally, \(\cos(\pi/n)\) increases strictly with \(n\), while Taylor expansion of \(\operatorname{arsinh}(2\cos(\pi/n))\) at zero yields the stated \(n^{-2}\) correction. \(\square\)

## Verification

Run `python3 verify.py` with the included standalone standard-library script. It directly evaluates the Poincaré-disk geodesic distance formula for all other sides, checks (2) for every side in several polygon orders, and samples 401 interior points on a representative side for each of 11 orders. All checks passed. The finite tests corroborate the proof and are not used to infer its validity for arbitrary integers.

## Relationship to prior work

Tselekidis (2026a, 2026b) introduces and studies slimness of geodesic polygons and asymptotic slimness functions in hyperbolic and other spaces. Those results treat universal or large-scale bounds; they do not state the exact value for the family of regular ideal polygons. Earlier basic hyperbolic trigonometry supplies the distance identities used here. The known sharp slimness of an ideal triangle is recovered at \(n=3\), namely \(\operatorname{arsinh}1\), and is not independently asserted as new. A literature/index search did not identify the full regular ideal \(n\)-gon formula, but this does not rule out an unindexed classical equivalent.

## Limitations

The vertices lie on the ideal boundary, outside the hyperbolic plane. The result does not assert a sharp bound for arbitrary ideal polygons or for the global supremum of all finite-vertex geodesic \(n\)-gons. It does not establish a new quasi-isometric invariant. The historical-priority comparison is not an exhaustive bibliographic proof of originality.

## References

1. P. Tselekidis, *Logarithmically Slim Polygons*, arXiv:2611.05429v1, first posted 3 November 2026, https://arxiv.org/html/2611.05429v1.
2. P. Tselekidis, *Slim Polygons, Hyperbolicity, and a new Quasi-Isometric Invariant*, arXiv:2611.09078v1, first posted 6 November 2026, https://arxiv.org/abs/2611.09078.
3. Standard Poincaré disk and hyperboloid models of the hyperbolic plane; the distance identity is reproduced and justified in the proof rather than invoked as an unpublished result.
