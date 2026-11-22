# A universal leading tail and a horocycle-length signature for random distances in a hyperbolic cusp

## Finding
For every boundary horocycle length \(\lambda>0\), take the complete-end metric cusp with boundary
\[
C_\lambda=\{(x\bmod\lambda,y):y\ge1\},\qquad ds^2=\frac{dx^2+dy^2}{y^2}.
\]
Choose two points independently according to normalized hyperbolic area, and write \(D_\lambda\) for their intrinsic shortest-path distance. Its *entire* law has the following independent-variable representation:
\[
\boxed{\cosh D_\lambda\ \overset d=\ \cosh S+\frac{\lambda^2}{8}e^{-S}Z},
\qquad S\sim\operatorname{Exp}(1),\quad
\Pr(Z>z)=(1-\sqrt z)^2\ (0\le z\le1),
\]
where \(S\) and \(Z\) are independent, and \(Z\) is supported in \([0,1]\). In particular, for every \(r\ge0\),
\[
\boxed{\Pr(D_\lambda>r)=e^{-r}+\int_0^r e^{-s}
\left(1-\frac{\sqrt{8e^s(\cosh r-\cosh s)}}{\lambda}\right)_+^2\,ds.}
\]
For fixed \(\lambda>0\), as \(r\to\infty\),
\[
\boxed{\Pr(D_\lambda>r)=e^{-r}+\frac{\lambda^2}{24}e^{-3r}+O_\lambda(e^{-5r}).}
\]
Thus the universal leading tail does not detect the cusp's horocycle length, but the first strictly positive correction does:
\[
\boxed{\lambda=\left[24\lim_{r\to\infty}e^{3r}(\Pr(D_\lambda>r)-e^{-r})\right]^{1/2}.}
\]
In fact the family is strictly ordered by first-order stochastic dominance: for \(0<\lambda<\mu\),
\(\Pr(D_\lambda>r)<\Pr(D_\mu>r)\) for every \(r>0\).

## Assumptions and scope
The cusp is the standalone intrinsic length space \(C_\lambda\), with its horocyclic boundary \(y=1\) included, curvature \(-1\), and finite area \(\lambda\). Distances are *intrinsic to the cusp*, not distances in an unspecified ambient finite-area surface; ambient shortcuts outside a cusp are not allowed. Normalized area density is \(dx\,dy/(\lambda y^2)\) on \(0\le x<\lambda\), \(y\ge1\). Both endpoints are independent. The statements hold for every fixed \(\lambda>0\); the asymptotic error need not be uniform as \(\lambda\) varies. A value at a threshold is immaterial because the distance law is continuous.

## Proof
**1. Quotient geodesic geometry.** The hyperbolic distance between upper-half-plane points is
\[
\cosh d_{\mathbb H^2}((x,y),(x',y'))=1+\frac{(x-x')^2+(y-y')^2}{2yy'}.
\]
For any two points with ordinates at least one, the hyperbolic geodesic segment joining them stays at height at least the lesser endpoint height: it is a vertical segment or an upper semicircle, and the height along the intermediate circular arc is no smaller than the smaller endpoint height. Therefore that segment lies in \(y\ge1\). Passing to horizontal translates by integer multiples of \(\lambda\), minimizing the distance amounts to taking the nearest circular displacement \(\Delta\in[-\lambda/2,\lambda/2]\); no alternative path through the cusp boundary can be shorter. Consequently
\[
\cosh D_\lambda=\cosh |\log y_1-\log y_2|+\frac{\Delta^2}{2y_1y_2}.
\]

**2. Independent exponential factorization.** Because the area law makes \(x\) uniform and \(y\) have density \(y^{-2}\) for \(y\ge1\), the variables \(H_i=\log y_i\) are independent exponential variables of rate one. The absolute difference \(S=|H_1-H_2|\) and minimum \(T=\min(H_1,H_2)\) have joint density \(2e^{-s-2t}\) for \(s,t\ge0\). Thus \(S\sim\operatorname{Exp}(1)\) and \(T\sim\operatorname{Exp}(2)\) independently. Also \(U=e^{-2T}\) is uniform on \((0,1)\). Independent circular differences imply \(W=2|\Delta|/\lambda\) is uniform on \((0,1)\) and independent of \((S,U)\). With \(Z=W^2U\), we obtain the asserted formula for \(\cosh D_\lambda\).

For \(0<z<1\), conditioning on \(W\) yields
\[
\Pr(Z>z)=\int_{\sqrt z}^1\left(1-\frac z{w^2}\right)dw=(1-\sqrt z)^2.
\]
This is an exact, normalized law; its density is \(z^{-1/2}-1\) on \((0,1)\).

**3. Full survival function.** If \(S>r\), necessarily \(D_\lambda>r\), contributing \(e^{-r}\). If \(0\le S=s\le r\), strict exceedance is exactly
\[
Z>\frac{8e^s(\cosh r-\cosh s)}{\lambda^2}.
\]
Integrating the displayed survival function of \(Z\) against the exponential density of \(S\) proves the one-dimensional formula for every \(r\ge0\).

**4. Sharp correction.** Put \(u=r-s\) and define
\[
B_r(u)=\frac{4e^{2r}}{\lambda^2}(1-e^{-u})(e^{-u}-e^{-2r}).
\]
The difference \(I_r=\Pr(D_\lambda>r)-e^{-r}\) equals
\[
I_r=e^{-r}\int_0^r e^u(1-\sqrt{B_r(u)})_+^2\,du.
\]
For each fixed \(\lambda\) and all sufficiently large \(r\), the set in \([0,r]\) on which \(B_r(u)<1\) is precisely \([0,u_r)\), with a unique endpoint near zero. This follows by factoring \(B_r\) as a concave quadratic in \(e^{-u}\); its other root lies beyond \(u=r\) for large \(r\). Taylor expansion at zero, with \(\lambda\) fixed, gives
\[
u_r=\frac{\lambda^2}{4}e^{-2r}\bigl(1+O_\lambda(e^{-2r})\bigr),\qquad
B_r(u_rt)=t\bigl(1+O_\lambda(e^{-2r})\bigr)
\]
uniformly for \(0\le t\le1\). The square root has the corresponding *multiplicative* error bound, including at zero. Hence
\[
I_r=e^{-r}u_r\left[\int_0^1(1-\sqrt t)^2dt+O_\lambda(e^{-2r})\right]
=e^{-r}u_r\left[\frac16+O_\lambda(e^{-2r})\right],
\]
which is \(\lambda^2 e^{-3r}/24+O_\lambda(e^{-5r})\). The inversion formula follows.

**5. Strict ordering.** Couple all \(D_\lambda\) by the same \((S,Z)\). The formula for \(\cosh D_\lambda\) is strictly increasing in \(\lambda>0\) almost surely because \(Z>0\) almost surely. To obtain strict survival inequalities at any fixed \(r>0\), choose \(s<r\) sufficiently close to \(r\); the positive continuously distributed \(Z\) then has positive probability of placing \(D_\lambda\) below and \(D_\mu\) above \(r\). This proves strict first-order stochastic order for every positive threshold.

## Verification
Run `python check_cusp_distance.py` after installing `requirements.txt`. The standalone checker samples 630,000 pairs directly in the upper-half-plane quotient and calculates the shortest distance by checking horizontal deck translates. It makes 12 distributional comparisons against independent one-dimensional numerical quadrature, nine large-distance correction comparisons, and product-law algebra checks. The observed correction ratios at \(r=5\) are \(1.00005448315\) for \(\lambda=1\) and \(1.00012714232\) for \(\lambda=3\). It terminates with `HYPERBOLIC_CUSP_DISTANCE_LAW_OK`. These finite computations corroborate the analytic argument, not replace it.

## Relationship to prior work
Haas (2005, 2007) studies cusp excursion depths and frequencies along typical *single geodesic trajectories* on finite-area hyperbolic orbifolds. That is different from the distribution of intrinsic distances between two independently area-uniform points in a fixed truncated cusp. Robertson (2013) develops hyperbolic Crofton formulas for distances in homogeneous spaces, not the quotient-cusp pair law or its width-sensitive tail. The classical hyperbolic distance formula and cusp coordinates are standard inputs. The present result's object-specific product factorization, full distribution and width-recovery correction are not claimed by those works. Related random-distance results for ideal polygons and flat finite cylinders do not imply this noncompact quotient-cusp calculation.

## Limitations
Only a standalone two-dimensional cusp, its intrinsic distance and normalized area sampling are addressed. A full finite-area surface may offer geodesic shortcuts through its compact part. No stability rate for estimating \(\lambda\) from finite noisy distance samples is proved; recovering the coefficient from far tails can be statistically delicate. Historical priority may depend on less-accessible sources; independent mathematical and historical validation is unperformed.

## References
- A. Haas, *The Distribution of Geodesic Excursions Out the End of a Hyperbolic Orbifold and Approximation with Respect to a Fuchsian Group*, Geometriae Dedicata 116 (2005), 129–155, https://doi.org/10.1007/s10711-005-9009-0 (first published 2005-11-29).
- A. Haas, *Geodesic cusp excursions and metric diophantine approximation*, arXiv:0709.0313, https://arxiv.org/abs/0709.0313 (first posted 2007-09-04); Math. Res. Lett. 16 (2009), 67–85.
- G. Robertson, *Crofton formulae and geodesic distance in hyperbolic spaces*, arXiv:1302.5790, https://arxiv.org/abs/1302.5790 (publicly posted 2013-02-23).
