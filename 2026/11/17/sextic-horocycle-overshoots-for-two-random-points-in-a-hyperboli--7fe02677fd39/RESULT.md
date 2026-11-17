# Sextic horocycle overshoots for two random points in a hyperbolic cusp

## Finding

Fix a width \(w>0\). In the curvature-\(-1\) truncated hyperbolic cusp
\[
C_w=\{(x\bmod w,y):y\ge1\},\qquad ds^2=\frac{dx^2+dy^2}{y^2},
\]
choose independent points \(P,Q\) from normalized hyperbolic area. Their heights \(Y_P,Y_Q\) have density \(y^{-2}\) on \([1,\infty)\). Let \(\gamma_{PQ}\) be an almost surely unique *intrinsic shortest geodesic* and \(M(P,Q)=\max_{z\in\gamma_{PQ}}\operatorname{height}(z)\). For \(H>1\) define the finite-endpoint *interior horocycle overshoot* event
\[
E_H=\{Y_P\le H,\quad Y_Q\le H,\quad M(P,Q)>H\}.
\]
Put \(L=w/2\). For every \(H\ge\sqrt{1+L^2}\), the probability has the exact integral
\[
\boxed{\Pr(E_H)=\frac1L\int_{u,v\ge0\,;\,u+v<L}
\frac{uv(L-u-v)}{(H^2-u^2)^{3/2}(H^2-v^2)^{3/2}}\,du\,dv.}
\]
For fixed \(w\), as \(H\to\infty\), this gives the **sharp two-term expansion**
\[
\boxed{\Pr(E_H)=\frac{w^4}{1920H^6}+\frac{w^6}{17920H^8}+O_w(H^{-10}).}
\]
Consequently the horocycle width is recoverable from this single rare-event law:
\[
\boxed{w=\left(1920\lim_{H\to\infty}H^6\Pr(E_H)\right)^{1/4}.}
\]

There is also a *joint marked limit*. Choose the signed shortest horizontal difference \(\Delta\in(-L,L)\) from \(P\) to \(Q\), and set \(Z=|\Delta|\). On \(E_H\), put
\[
U=\sqrt{H^2-Y_P^2},\qquad V=\sqrt{H^2-Y_Q^2},\qquad
R=Z/L,\quad S=U/Z,\quad T=V/Z.
\]
As \(H\to\infty\), the conditional law of \((R,S,T)\) converges in **total variation**, with error \(O_w(H^{-2})\), to a product law in which \(R\sim\operatorname{Beta}(5,1)\) and \((S,T,1-S-T)\sim\operatorname{Dirichlet}(2,2,1)\), independently. Equivalently the limiting joint density is \(120r^4st\) on \(0<r<1\), \(s,t>0\), \(s+t<1\). The sign of \(\Delta\) is exactly fair and independent of these marks for every \(H\); the starting horizontal phase \(x_P\bmod w\) is exactly Haar-uniform and independent as well. These exact independent marks may be included in the total-variation convergence.

## Assumptions and scope

The cusp is the complete **truncated** horoball quotient, regarded as a Riemannian manifold with boundary and its intrinsic path metric. It is not the metric induced on a chosen cusp by allowing paths outside that cusp in some larger surface. Curvature equals \(-1\), the boundary horocycle \(y=1\) has hyperbolic length \(w\), both endpoints are independently normalized-area-uniform, and the geodesic is shortest in the quotient. The parameter \(w\) is held fixed in the large-\(H\) expansion and the conditional limit. Endpoint ties and multiple shortest lifts have probability zero.

## Proof

**1. Shortest lift and sampling coordinates.** The upper-half-plane horoball \(y\ge1\) is geodesically convex: upper-half-plane geodesics are vertical lines or upper semicircles, whose segments do not go below the smaller endpoint height. Therefore the intrinsic shortest quotient geodesic is obtained by taking the unique (almost surely) horizontal difference \(\Delta\in(-w/2,w/2)\) between suitable endpoint lifts. Hyperbolic distance strictly increases with the absolute lift displacement, so no other translate can be shorter. Translation invariance and independent uniform horizontal phases show that \(\Delta\) is uniform on \((-L,L)\), independent of both heights and of the initial phase. Thus \(Z=|\Delta|\) is uniform on \((0,L)\), and its sign is independently fair. Each height has density \(y^{-2}\,dy\), since normalized area in the strip is \(w^{-1}dx\,dy/y^2\).

**2. An exact deterministic horocycle criterion.** Lift the endpoints to \((0,a),(z,b)\), where \(1\le a,b\le H\) and \(z>0\). Their geodesic is a Euclidean semicircle of radius \(\mathcal R\) centered on the horizontal axis (or a vertical line on a null set). If the semicircle's apex lies between the two points, then its horizontal displacement satisfies
\[
z=\sqrt{\mathcal R^2-a^2}+\sqrt{\mathcal R^2-b^2},
\]
a strictly increasing function of \(\mathcal R\ge\max(a,b)\). If its apex is outside the segment, the segment cannot rise above both endpoints. It follows, for \(a,b\le H\), that its segment has maximum height greater than \(H\) **if and only if**
\[
\boxed{z>\sqrt{H^2-a^2}+\sqrt{H^2-b^2}.}
\]
Equality has probability zero. In particular a positive overshoot requires both endpoints in a shrinking layer of vertical thickness \(O_w(H^{-1})\) below the horocycle.

**3. Exact integration.** Set \(u=\sqrt{H^2-a^2}\) and \(v=\sqrt{H^2-b^2}\). Each height density transforms to
\[
\frac{da}{a^2}=\frac{u\,du}{(H^2-u^2)^{3/2}},\qquad
\frac{db}{b^2}=\frac{v\,dv}{(H^2-v^2)^{3/2}},
\]
where the integration signs denote positive absolute Jacobians. Since \(z\le L\), the overshoot criterion forces \(u+v<L\), and the assumed lower bound on \(H\) ensures \(a,b\ge1\) automatically on this domain. Integrating the independent uniform \(z\in(0,L)\) over \((u+v,L)\) produces the factor \((L-u-v)/L\) and proves the exact two-dimensional formula.

**4. Both asymptotic coefficients.** Uniformly over the compact triangular domain \(u,v\ge0,u+v\le L\),
\[
(H^2-u^2)^{-3/2}(H^2-v^2)^{-3/2}
=H^{-6}\left[1+\frac{3(u^2+v^2)}{2H^2}+O_w(H^{-4})\right].
\]
The elementary Dirichlet simplex integrals are
\[
\frac1L\int_{u+v<L}uv(L-u-v)\,du\,dv=\frac{L^4}{120},
\]
\[
\frac1L\int_{u+v<L}uv(L-u-v)(u^2+v^2)\,du\,dv
=\frac{L^6}{420}.
\]
Hence the coefficients are \(L^4/120=w^4/1920\) and \((3/2)L^6/420=L^6/280=w^6/17920\), with the stated remainder. The first is positive, so the power six and leading constant are sharp; solving for \(w\) proves the inverse identity.

**5. Marked total-variation limit.** On \(E_H\), make the substitution \(z=Lr\), \(u=Lrs\), \(v=Lrt\). Its Jacobian is \(L^3r^2\), and the unnormalized joint measure of \((r,s,t)\) is
\[
\frac{L^4}{H^6}r^4st
\left(1-\frac{L^2r^2s^2}{H^2}\right)^{-3/2}
\left(1-\frac{L^2r^2t^2}{H^2}\right)^{-3/2}
\,dr\,ds\,dt
\]
on the fixed domain \(0<r<1,\ s,t>0,\ s+t<1\). The parenthesized factors converge **uniformly** to one, with relative error \(O_w(H^{-2})\). Also \(\int_0^1r^4dr=1/5\) and \(\int_{s+t<1}st\,ds\,dt=1/24\). Normalizing therefore gives the product density \((5r^4)(24st)\) with total-variation error \(O_w(H^{-2})\). The independent sign and phase were established exactly in step 1; adjoining them does not change this convergence.

## Verification

The included `check_cusp_overshoot.py` runs with the Python standard library. It independently tests the deterministic Euclidean-circle apex criterion on 80,000 seeded geometries, integrates the exact transformed probability by two-dimensional composite Simpson quadrature for widths \(1,2,4\) and heights \(5,10,20\), compares the two-term expansion, and checks the beta–Dirichlet normalizations and second moment. Its success marker is `HYPERBOLIC_CUSP_OVERSHOOT_CHECKS_OK`. Numerical checks are only corroboration; the infinite limiting claims, exact integral, and total-variation bound follow from the preceding analytic proof.

## Relationship to prior work

Haas (2007) develops cusp excursion depths and rates for generic **bi-infinite geodesics** on finite-area hyperbolic surfaces; his randomization is Liouville/geodesic-flow sampling, not two independent normalized-area endpoints in a standalone cusp. Gadre (2014) studies long geodesic-ray excursions and partial sums in cusp neighborhoods; those time-asymptotic laws do not yield the two-endpoint horocycle overshoot event. Borthwick (2010) discusses hyperbolic cusp coordinates in spectral resonance bounds, a different observable.

The mathematical record *Sharp random-distance tails and inverse rigidity for finite-area hyperbolic cusps* (2026) studies the **intrinsic distance** of two area-random points in exactly the same cusp and recovers its width from the distance tail. Its inspected complete result has no maximum-height or endpoint-below-threshold event and does not establish the sextic or marked overshoot laws. *Cusp-pair tails for random distances in ideal hyperbolic polygons* (2026) likewise concerns distances in a fixed ideal polygon, not geodesic height in a truncated cusp. Neither scalar distance statement implies the present geodesic-location law without new geometric integration. No claim of exhaustive historical priority is made.

## Limitations

The result applies to exactly two independent area-uniform points, to a single truncated curvature-\(-1\) cusp of fixed width, and to intrinsic shortest geodesics. It does not address nonminimizing winding geodesics, a complete finite-area surface in which a route may leave the chosen cusp, nonuniform endpoint laws, higher dimensions, or a joint limit in which \(w/H\) fails to vanish. Historical priority requires further independent assessment; no independent mathematical audit has been performed.

## References

1. A. Haas, *Geodesic cusp excursions and metric diophantine approximation*, arXiv:0709.0313v1, first submitted 2007-09-04, https://arxiv.org/abs/0709.0313.
2. D. Borthwick, *Sharp geometric upper bounds on resonances for surfaces with hyperbolic ends*, arXiv:1006.5478v1, first submitted 2010-06-28, https://arxiv.org/abs/1006.5478.
3. V. Gadre, *Partial sums of excursions along random geodesics and volume asymptotics for thin parts of moduli spaces of quadratic differentials*, arXiv:1408.5812v1, first submitted 2014-08-25, https://arxiv.org/abs/1408.5812.
4. *Sharp random-distance tails and inverse rigidity for finite-area hyperbolic cusps*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-random-distance-tails-and-inverse-rigidity-for-finite-area--e7c5d4116ecb/RESULT.md.
5. *Cusp-pair tails for random distances in ideal hyperbolic polygons*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-cusp-pair-tails-for-random-distances-in-ideal-hyperbolic-polygon--102d92c50bd6/RESULT.md.
