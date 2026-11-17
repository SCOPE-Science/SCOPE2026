# A two-term parity crossover for nearly diametral interior pairs in regular polygons

## Finding
For every integer \(n\ge3\), let \(P_n\) be the regular Euclidean \(n\)-gon with circumradius one. Choose independent **area-uniform** points \(X_n,Y_n\in P_n\), and let \(D_n=\|X_n-Y_n\|\). Put \(\delta_n=2\pi/n\), and set \(\sigma_n=0\) for even \(n\) and \(\sigma_n=1/2\) for odd \(n\). Define the periodic functions
\[
h(u)=\frac12\{u\}(1-\{u\}),\qquad k(u)=-\frac5{24}(\{u\}-\tfrac12)^4+\frac1{16}(\{u\}-\tfrac12)^2-\frac1{384},
\]
where \(\{u\}=u-\lfloor u\rfloor\). For \(\sigma\in\{0,1/2\}\), \(t\ge0\), and \(u\in[0,1]\), \(w\in\mathbb R\), abbreviate
\[
H=h(u)+h(u+\sigma+w),\quad K=k(u)+k(u+\sigma+w),\quad G=H+w^2/4,\quad B=(t-G)_+,\quad Q=tw^2/8-5w^4/192-K.
\]
Define two absolutely convergent explicit integrals
\[
F_\sigma(t)=\int_0^1\!\int_{\mathbb R} B^2\,dw\,du,
\quad J_\sigma(t)=\int_0^1\!\int_{\mathbb R}\bigl[B^2/3+2BQ-HB^2-2B^3/3\bigr]dw\,du.
\]
**Two-term theorem.** For every finite \(T>0\), uniformly over \(0\le t\le T\), as \(n\to\infty\) through either parity,
\[
\boxed{\frac{\pi}{\delta_n^5}\Pr(D_n>2-\delta_n^2 t)
=F_{\sigma_n}(t)+\delta_n^2J_{\sigma_n}(t)+O_T(\delta_n^4).}
\]
The error constant is independent of the parity and of \(t\) in the stated interval. These limits have distinct parity thresholds and quartic onsets:
\[
\boxed{F_0(t)\sim\frac43t^4\ (t\downarrow0),\qquad F_{1/2}(t)=0\ (0\le t\le1/16),\qquad F_{1/2}(1/16+s)\sim\frac{128}{27}s^4\ (s\downarrow0).}
\]
Both match the smooth-disk regime at large rescaled deficits:
\[
\boxed{F_\sigma(t)=\frac{32}{15}t^{5/2}+O(t^{3/2})\qquad(t\to\infty).}
\]
**Conditional geometry.** For fixed \(t\) above its parity threshold, set \(U_n=\{\arg X_n/\delta_n\}\), let \(W_n\in[-n/2,n/2)\) be selected by \(\arg Y_n-\arg X_n\equiv\pi+\delta_nW_n\pmod{2\pi}\), and put \(Z_{1,n}=(1-|X_n|)/\delta_n^2\), \(Z_{2,n}=(1-|Y_n|)/\delta_n^2\). Conditional on \(D_n>2-\delta_n^2t\), the quadruple \((U_n,W_n,Z_{1,n},Z_{2,n})\) converges in distribution to uniform normalized four-dimensional Lebesgue measure on
\[
\mathcal R_{\sigma,t}=\left\{0<u<1,\ w\in\mathbb R,\ z_1\ge h(u),\ z_2\ge h(u+\sigma+w),\ z_1+z_2+w^2/4<t\right\}.
\]
In particular, conditional on the limiting angular pair \((u,w)\), the three normalized shares of the available residual \(t-G(u,w)\)—the two inward radial excesses and remaining distance budget—have the \(\operatorname{Dirichlet}(1,1,1)\) law.

## Assumptions and scope
The two points are independent with respect to **normalized interior Euclidean area**, not uniform perimeter arclength, random invariant-line chords, or uniform vertices. All distances are ambient Euclidean distances. The polygon is regular with fixed circumradius one and is allowed either parity. The refinement parameter \(t\) remains bounded while \(n\) grows: the large-\(t\) formula concerns the limiting crossover and does not assert a jointly uniform limit for growing \(t\). The odd threshold \(1/16\) is the asymptotic gap between the disk diameter two and the odd polygon's actual diameter \(2\cos(\pi/(2n))\).

## Proof
**Polar geometry and localization.** Write \(\delta=2\pi/n\), \(\sigma=\sigma_n\), and \(A_n=\operatorname{area}(P_n)=n\sin\delta/2=\pi\sin\delta/\delta\). The radial boundary of \(P_n\) at angle \(\delta(k+u)\) is exactly
\[
r_n(u)=\frac{\cos(\delta/2)}{\cos(\delta(\{u\}-1/2))},\qquad 0\le u<1.
\]
The cosine expansion, uniformly in \(u\), gives
\[
\frac{1-r_n(u)}{\delta^2}=h(u)+\delta^2k(u)+O(\delta^4).
\]
For an almost diametral pair, write the first polar angle as \(\delta(k+u)\), the second as the first plus \(\pi+\delta w\), and select \(|w|\le n/2\). Its second phase is \(u+\sigma+w\) modulo one. Define \(z_i=(1-\rho_i)/\delta^2\) for the radial coordinates \(\rho_i\). The inequality \(D_n\le\rho_1+\rho_2\le2\) forces \(0\le z_i\le t\) on the event \(D_n>2-\delta^2t\), for large \(n\). The cosine rule then forces \(|w|\le C_T\) whenever \(t\le T\): the upper bound \(D_n\le 2\cos(\delta w/2)\) and a quadratic lower bound for \(1-\cos\) on the principal angular interval suffice. Thus all subsequent expansions occur on a fixed compact box depending only on \(T\).

**The second-order distance defect.** For \(z_i\le T\) and bounded \(w\), let \(S=z_1+z_2\). Since \(\rho_i=1-\delta^2z_i\), the exact cosine rule and Taylor expansion give uniformly
\[
\frac{2-\sqrt{\rho_1^2+\rho_2^2+2\rho_1\rho_2\cos(\delta w)}}{\delta^2}
=S+\frac{w^2}{4}-\delta^2\left(\frac{Sw^2}{8}+\frac{w^4}{192}\right)+O_T(\delta^4).
\]
Write \(z_i=h(u_i)+\delta^2k(u_i)+s_i+O(\delta^4)\), where \(s_i\ge0\) and \(u_1=u\), \(u_2=u+\sigma+w\). To order \(\delta^2\), the admissible simplex is
\[
s_1,s_2\ge0,\qquad s_1+s_2<t-G(u,w)+\delta^2 Q(u,w;t)+O_T(\delta^4),
\]
with the displayed \(G,Q\). Indeed on its leading boundary \(S=t-w^2/4\), and substituting this into the correction gives \(tw^2/8-5w^4/192\). Replacing \(S\) by its boundary value introduces only \(O_T(\delta^4)\) error in the threshold, because its derivative multiplies \(\delta^2\).

**Radial integration.** For every \(A\in\mathbb R\), \(\int_{s_1,s_2\ge0,s_1+s_2<A}ds_1ds_2=A_+^2/2\), while \(\int(s_1+s_2)ds_1ds_2=A_+^3/3\) over the same simplex. The exact polar area Jacobian is
\[
\rho_1\rho_2=1-\delta^2(H+s_1+s_2)+O_T(\delta^4).
\]
Because the positive-part square has Lipschitz first derivative, replacing the perturbed simplex boundary by its order-\(\delta^2\) expansion incurs a **uniform** \(O_T(\delta^4)\) integrated error, including when \(t-G\) is close to zero. Consequently its normalized radial integral is
\[
\frac12 B^2+\delta^2\left[BQ-\frac12 HB^2-\frac13 B^3\right]+O_T(\delta^4).
\]
The polar angular measure is \(d\arg X\,d\arg Y\), with \(d\arg Y=\delta\,dw\), while two radial changes contribute \(\delta^4\,dz_1dz_2\). Averaging the first angle over the \(n\) identical sectors gives exactly \(2\pi\), so
\[
\frac{\pi}{\delta^5}\Pr(D_n>2-\delta^2t)
=\frac{2\pi^2}{A_n^2}\int_0^1\!\int_{\mathbb R}\bigl(\text{radial integral}\bigr)dw\,du.
\]
Finally \(2\pi^2/A_n^2=2+\tfrac23\delta^2+O(\delta^4)\). Multiplication gives precisely \(F_\sigma+\delta^2J_\sigma+O_T(\delta^4)\). Compact localization guarantees that the error remains uniform after both angular integrations.

**Parity onsets.** Let \(q(u)=\operatorname{dist}(u,\mathbb Z)\). Then \(4h(u)=2q(u)(1-q(u))\). For \(\sigma=0\), the sole zero of \(G\), modulo the unit-period \(u\), is \((u,w)=(0,0)\). In unwrapped local variables \(x=u\), \(y=u+w\), one has \(G=(|x|+|y|)/2+O(x^2+y^2)\). Scaling \((x,y)=t(\xi,\eta)\) gives
\[
\lim_{t\downarrow0}\frac{F_0(t)}{t^4}=
\int_{\mathbb R^2}\left(1-\frac{|\xi|+|\eta|}{2}\right)_+^2d\xi\,d\eta=\frac43.
\]
For \(\sigma=1/2\), the circle-metric triangle inequality and \(2q(1-q)\ge q\) yield \(4G\ge\operatorname{dist}(w+1/2,\mathbb Z)+w^2\ge1/4\). Equality occurs in two distinct periodic neighborhoods with \(w=\pm1/2\) and both phase distances zero. Hence \(\min G=1/16\). In local signed coordinates \((x,y)\) at either minimum, the leading excess is \([2|x|+2|y|\pm(y-x)]/4\). For one minimum, the four quadrants have linear slopes \((1,3)\) in each variable, and direct integration gives
\[
\int_{\mathbb R^2}\left(1-\frac{2|x|+2|y|\pm(y-x)}4\right)_+^2dx\,dy=\frac{64}{27}.
\]
The two disjoint minima give \(128/27\). The endpoint neighborhoods are compact after scaling, justifying dominated convergence.

**Disk envelope and conditional geometry.** Since \(0\le h\le1/8\), for \(t\ge1/4\),
\[
\frac{32}{15}(t-1/4)^{5/2}\le F_\sigma(t)\le\frac{32}{15}t^{5/2}.
\]
This yields the stated disk matching with error \(O(t^{3/2})\). Finally, in the localized polar coordinates, the unnormalized joint density of \((u,w,z_1,z_2)\) is a constant times \(\rho_1\rho_2\), converging uniformly to a constant on compact sets. The event constraints converge in measure to the defining inequalities of \(\mathcal R_{\sigma,t}\), whose boundary has four-dimensional Lebesgue measure zero. The domain volume is \(F_\sigma(t)/2\), proving the conditional uniform law. Conditional on \((u,w)\), the two excesses fill a planar simplex uniformly; adjoining its remaining slack is exactly \(\operatorname{Dirichlet}(1,1,1)\).

## Verification
The standalone program `verify_area_polygon_crossover.py` independently evaluates both explicit crossover integrals by Gauss–Legendre quadrature, reconstructs the exact finite-polygon polar geometry, and estimates its near-diameter probability using scrambled-free Sobol integration in four dimensions. The exact distance condition—not its Taylor approximation—is used in those finite-polygon checks. It checks both parities, the two quartic onset constants, large-argument disk matching, and improvement from the explicit \(\delta^2J_\sigma\) correction. These finite calculations corroborate rather than replace the proof.

## Relationship to prior work
Bäsel's 2012 preprint derives **the complete fixed-\(n\)** distribution of distances between two uniform interior points in a regular polygon, as well as invariant-line chord distributions. That work therefore determines each finite-\(n\) probability in principle, but does not state a simultaneous many-side near-diameter expansion, a first nonzero finite-size correction, or the conditional four-dimensional geometry. Pure–Durrani–Tong–Pan (2019 preprint, 2022 journal) give a general analytical/computational framework for pair-distance laws in polygons; the same double-scaling and quantitative correction are not among the results inspected.

A published parity-split **boundary-arclength** crossover gives \(H_\sigma(s)=\int_0^1\int_{\mathbb R}{\bf1}\{4G_\sigma(u,w)<s\}\,dw\,du\). The present leading interior-area profile satisfies the exact relationship \(F_\sigma''(t)=2H_\sigma(4t)\), \(F_\sigma(0)=F_\sigma'(0)=0\). The leading term can consequently be interpreted as a twofold radial integration of that boundary law and is **not** claimed as independent of it. The new claim is the explicit second-order quantitative correction with controlled \(O_T(\delta^4)\) remainder, together with the area-pair conditional geometry. No assertion of historical uniqueness follows from these comparisons.

## Limitations
The two-term expansion holds uniformly for fixed bounded rescaled threshold, not for an unbounded threshold varying with \(n\). It excludes nonregular polygons, arclength-sampled endpoints, sample maxima over growing sets of points, and any claim of independent historical certification. Although exact fixed-polygon distance formulas imply the underlying finite probabilities, extracting the stated two-term, parity-sensitive double scaling requires a separate uniform asymptotic analysis. External independent proof checking remains unperformed.

## References
1. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, v1 posted 2012-04-12, especially the fixed-polygon distance distribution theorem.
2. R. Pure, S. Durrani, F. Tong, J. Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, arXiv:1903.07757, v1 posted 2019-03-18; later journal title *Distance distribution between two random points in arbitrary polygons* (2022).
3. *Parity-split polygon-to-circle crossover for almost-diametral boundary chords*, publicly available mathematical finding, 2026-11-08, identifier f64acf954997. Its boundary-arclength theorem and proof were compared in full.
