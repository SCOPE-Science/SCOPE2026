# Marked core-crossing geodesics on a flat Möbius band: a uniform region and sharp stochastic ordering

## Finding

Let \(M_{L,W}\) be the intrinsic rectangular flat Möbius band with horizontal glide length \(L>0\) and transverse width \(W>0\), and let \(C\) be its central closed geodesic. Join two independent area-uniform points with their (almost surely unique) globally shortest geodesic. On the event \(E\) that its interior meets \(C\), write \(U,V\in(0,1)\) for the endpoint absolute heights relative to the half-width, and \(Z\) for twice the horizontal developed displacement divided by \(L\). Put \(r=W/L\).

**Uniform marked geodesic-current law.** With respect to ordinary three-dimensional Lebesgue measure, the unnormalized joint distribution is
\[
\boxed{\Pr(E,\ U\in du,\ V\in dv,\ Z\in dz)=\frac12\mathbf 1_{\{0<u,v,z<1,\ z+r^2uv<1\}}\,du\,dv\,dz.}
\]
Consequently, conditional on hitting the core, \((U,V,Z)\) is uniform on the three-dimensional region \(\Omega_r=\{(u,v,z)\in(0,1)^3:z+r^2uv<1\}\).

Set
\[
G(t)=\begin{cases}0,&t\le0,\\t(1-\log t),&0<t<1,\\1,&t\ge1,\end{cases}\quad
H(t)=\begin{cases}0,&t\le0,\\t^2(3/4-(\log t)/2),&0<t\le1,\\t-1/4,&t\ge1.\end{cases}
\]
The *entire conditional horizontal-displacement law* is
\[
\boxed{\Pr(Z>z\mid E)=\frac{H((1-z)/r^2)}{H(1/r^2)},\quad 0\le z\le1.}
\]
In particular, for every \(0<r_1<r_2\), the density ratio \(f_{r_2}(z)/f_{r_1}(z)\) is nonincreasing in \(z\in(0,1)\), and it decreases strictly on a nonempty subinterval. Thus \(Z\mid E\) is strictly stochastically smaller at \(r_2\) than at \(r_1\); thinner bands have longer crossing displacements in this precise stochastic sense. The endpoint limits are
\[
Z\mid E\ \Longrightarrow\ \operatorname{Unif}(0,1)\quad(r\downarrow0),\qquad
Z\mid E\ \Longrightarrow\ \operatorname{Beta}(1,2)\quad(r\to\infty).
\]
The location where the crossing meets \(C\), measured by arclength modulo \(L\), is Haar-uniform and independent of the three marks given \(E\). These laws describe the geometry of core-crossing paths, not only their number.

The *unmarked* crossing probability follows by integration:
\[
\Pr(E)=\frac{r^2}{2}H(1/r^2)=\begin{cases}1/2-r^2/8,&0<r\le1,\\(3+4\log r)/(8r^2),&r\ge1.\end{cases}
\]
This scalar formula is already recorded in earlier work and **is not claimed as a new result**.

## Assumptions and scope

The surface is the quotient
\[
M_{L,W}=\big(\mathbb R\times[-W/2,W/2]\big)/\langle(x,y)\mapsto(x+L,-y)\rangle
\]
with its intrinsic flat length metric, not distances induced by a bent embedding. The core \(C\) is the image of \(y=0\). The two endpoints are independent and uniform for normalized two-dimensional area. The unique globally shortest path between them exists almost surely; ties have probability zero. Only crossings of its open interior with the core count. Because each minimizing lift is a straight segment with monotonic transverse coordinate, there is at most one such intersection. The differential \(dx\) descends globally to the Möbius band, since its deck generator preserves \(dx\). Thus the developed horizontal displacement \(\ell=|\int_\gamma dx|\) is defined intrinsically for the chosen path, with no preferred origin or orientation required. The crossing point along \(C\) is defined modulo its length \(L\).

## Proof

**1. Only two relevant lifted geodesics.** Use representatives \((x_i,y_i)\), with \(x_i\) independent uniform in \([0,L)\) and \(y_i\) independent uniform in \([-W/2,W/2]\). Let \(d=|x_1-x_2|\); it has density \(2(L-d)/L^2\) on \((0,L)\). Even deck images give the shortest squared length \(d^2+(y_1-y_2)^2\); odd images give \((L-d)^2+(y_1+y_2)^2\). All other images have longer horizontal displacement in the same parity class, and the covering strip is convex. These two branches alone determine the minimizing geodesic.

**2. Crossing and threshold.** Put \(a=|y_1|=(W/2)u\), \(b=|y_2|=(W/2)v\), with \(u,v\in(0,1)\) independent uniform. Their signs are independent fair signs. For opposite signs the even branch intersects \(C\) and wins precisely when
\[
d<\frac L2-\frac{2ab}{L}=\frac L2(1-r^2uv).
\]
For equal signs the odd branch intersects \(C\) and wins precisely when
\[
d>\frac L2+\frac{2ab}{L}=L-\frac L2(1-r^2uv).
\]
These conditions both require \(r^2uv<1\). The corresponding developed horizontal displacement is respectively \(\ell=d\) and \(\ell=L-d\).

**3. Exact marked law.** At a fixed \(u,v\), add the densities in \(\ell\) from the two sign patterns. Each sign pattern has probability \(1/2\), so for \(0<\ell<(L/2)(1-r^2uv)\), the combined unconditional density is
\[
\frac12\frac{2(L-\ell)}{L^2}+\frac12\frac{2\ell}{L^2}=\frac1L.
\]
The change of variables \(z=2\ell/L\) makes that density exactly \(1/2\). Multiplication by the independent unit densities for \(u,v\) proves the claimed uniform-domain law. It also shows why the nonuniform triangular density of \(d\) cancels: even and odd crossing branches contribute complementary weights.

**4. Exact conditional distribution.** For independent unit uniforms \(U,V\), the product CDF is \(G(t)=t(1-\log t)\) on \((0,1)\), extended by zero and one. Integration gives the displayed \(H\), with \(H'(t)=G(t)\) everywhere on \((0,\infty)\). From Step 3,
\[
\Pr(E,Z>z)=\frac12\int_z^1G((1-s)/r^2)\,ds=\frac{r^2}{2}H((1-z)/r^2).
\]
The same formula at \(z=0\) gives \(\Pr(E)>0\), proving the conditional survival law. Its density is
\[
f_r(z)=\frac{G((1-z)/r^2)}{r^2H(1/r^2)}\quad(0<z<1).
\]

**5. Monotone likelihood-ratio and the limits.** For \(t\in(0,1)\) define the logarithmic elasticity \(e(t)=tG'(t)/G(t)=(-\log t)/(1-\log t)\), and set \(e(t)=0\) for \(t\ge1\). This continuous elasticity is nonincreasing in \(t\) and strictly decreasing below one. For any \(0<r_1<r_2\), differentiating the logarithm of the density ratio for \(0<z<1\) gives
\[
\frac{d}{dz}\log\frac{f_{r_2}(z)}{f_{r_1}(z)}=-\frac{e((1-z)/r_2^2)-e((1-z)/r_1^2)}{1-z}\le0.
\]
It is strictly negative for every \(z>\max\{0,1-r_2^2\}\), so the ratio is not constant. Both densities are positive and integrate to one; the monotone likelihood-ratio comparison implies strict first-order stochastic ordering at each interior threshold. For \(r\downarrow0\), the exact formula gives \(H(t)=t-1/4\) at sufficiently large arguments, yielding survival \(1-z\). For \(r\to\infty\), \(H(t)=t^2(3/4-\frac12\log t)\) near zero, yielding survival \((1-z)^2\). These limits are exactly the uniform and Beta distributions stated.

**6. Uniform independent crossing location.** Horizontal translations \((x,y)\mapsto(x+c,y)\) are isometries of the quotient, preserve the endpoints' joint uniform area law, preserve \(E,U,V,Z\), and translate the core intersection arclength by \(c\pmod L\). Thus for any conditional set of marks, the crossing-location measure is invariant under the circle-translation group. Uniqueness of normalized Haar measure proves independence and uniformity.

## Verification

The standalone Python standard-library script `verify_marked.py` samples the *original endpoints* and selects the shortest among the two deck-parity geodesics. It compares the crossing frequency with the known scalar formula and the conditional survival at three internal thresholds against the new exact formula, for five strip aspect ratios. It also checks the normalization, likelihood-ratio monotonicity and endpoint limit laws. The code is corroboration; Steps 1–6 are the proof of the quantified statements. Run `python3 verify_marked.py` alongside this document.

## Relationship to prior work

The earlier **core-crossing probability law** for area-uniform endpoint pairs on flat Möbius bands determines the scalar \(\Pr(E)\) and its aspect-ratio threshold; the formula in this note reproduces that *already known marginal*. The present result instead determines a three-dimensional **joint marked crossing law**, the complete conditional horizontal-span distribution, a global monotone likelihood-ratio ordering, the thin/thick conditional limits and uniform independent intersection location. None of these marked statements follows from the previously published scalar probability alone. Earlier work on the **complete unmarked pair-distance CDF** of the flat Möbius band and its matching cylinder, and on the twist-related squared-distance defect, likewise reports no conditional geodesic-path marks. The boundary-lens rigidity result of Croke and Herreros studies geodesics with boundary endpoint data and uses a Crofton intersection formula, but does not evaluate this area-endpoint-conditioned marked geodesic law. The physically embedded Möbius-strip equilibrium model of Starostin and van der Heijden is extrinsic, not this intrinsic sampling experiment. General Crofton/Santaló identities concern different geodesic measures and do not directly imply the uniform-domain law.

## Limitations

Only the flat constant-width Möbius quotient and independent uniform area endpoints are covered. The horizontal-displacement mark is not total arclength and no formula for a conditional *angle* distribution is asserted. The ratio monotonicity is non-strict on an initial density interval in some thin bands, although the stochastic comparison is strict at each interior threshold. Historical priority is based on the checked sources, not a claim of exhaustive literature coverage; older unindexed marked-geodesic formulas remain possible. The result is an exact population law, not a finite-sample stability or estimation theorem. Independent mathematical audit has not been performed.

## References

1. C. B. Croke and P. Herreros, *Lens rigidity with trapped geodesics in two dimensions*, arXiv:1108.4938v1 (first public 2011-08-24), §§2–3, https://arxiv.org/html/1108.4938v1 .
2. E. L. Starostin and G. H. M. van der Heijden, *The shape of a Möbius strip*, Nature Materials 6 (2007), 563–567 (first published 2007-07-15), https://doi.org/10.1038/nmat1929 .
3. *A core-crossing law that determines the shape of a flat Möbius band*, prior research record, item 20951824-bccf-4d73-a954-c49639676ad4 (unmarked probability and rigidity; exact provenance retained in archival records).
4. *A complete two-point distance ordering for the flat Möbius band and its matched cylinder*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-complete-two-point-distance-ordering-for-the-flat-m-bius-band--d61dc15f6cd5 .
5. *Twisted identification stochastically shortens flat-band distances with a fourth-order threshold*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-twisted-identification-stochastically-shortens-flat-band-distanc--dc6c7d67e0d1 .
6. H. Santaló, *Integral Geometry and Geometric Probability* (1976), Chapter 19, background Crofton/Santaló identities.
