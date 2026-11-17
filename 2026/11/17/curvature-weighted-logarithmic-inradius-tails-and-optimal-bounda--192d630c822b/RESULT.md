# Curvature-weighted logarithmic inradius tails and optimal boundary sampling on convex curves

## Finding
Let \(\Gamma\) be a strictly convex, simple closed \(C^3\) plane curve of perimeter \(L\), positively oriented and parametrized by Euclidean arclength \(s\), with everywhere positive curvature \(\kappa(s)\). Independently sample three boundary points from any positive normalized \(C^1\) arclength density \(f(s)\). Let \(r\) be the inradius of the triangle they span, and put
\[
I(\Gamma,f)=\int_0^L \frac{f(s)^3}{\kappa(s)}\,ds.
\]
Then the sharp small-inradius law is
\[
\boxed{\lim_{t\downarrow0}\frac{\Pr(r<t)}{t\log(L/t)}=24I(\Gamma,f).}
\]

There is a joint marked rare-event law. Order the three sampled points counterclockwise. With probability one their three successive arclength gaps have a unique largest gap; denote the first point following that largest gap by \(S\in\mathbb R/L\mathbb Z\), and denote the next two arclength gaps by \(a,b\), in order. Define
\[
V_t=\frac{\log(a/L)}{\log(t/L)},\qquad W_t=\frac r t.
\]
Conditioned on \(r<t\), the joint law of \((S,V_t,W_t)\) converges **in total variation** to independent variables: the location has density \(f(s)^3/[\kappa(s)I(\Gamma,f)]\) with respect to \(ds\), and the two marks are independent uniform variables on \((0,1)\).

Among positive normalized \(C^1\) sampling densities, the sharp coefficient is uniquely minimized by
\[
\boxed{f_*(s)=\frac{\sqrt{\kappa(s)}}{\int_0^L\sqrt{\kappa(u)}\,du},\qquad 24I(\Gamma,f_*)=\frac{24}{\left(\int_0^L\sqrt{\kappa(s)}\,ds\right)^2}.}
\]
For uniform arclength sampling \(f=1/L\), curves of fixed perimeter obey
\[
\boxed{24I(\Gamma,1/L)=\frac{24}{L^3}\int_0^L\frac{ds}{\kappa(s)}\ \ge\ \frac{12}{\pi L},}
\]
with equality exactly for circles. The law also implies \(\mathbb E[r^{-p}]<\infty\) exactly when \(0<p<1\).

## Assumptions and scope
The curve is compact, embedded, strictly convex, positively oriented and \(C^3\) with \(\kappa>0\) everywhere. Sampling is independent from the fixed, strictly positive \(C^1\) density \(f\) satisfying \(\int_0^L f(s)\,ds=1\). All triangles are nondegenerate almost surely, and their inradius is Euclidean. The limit is pointwise in the fixed curve and density; no uniform estimate over degenerating families is claimed. The threshold \(t\) is a length, so \(\log(L/t)\) is dimensionless. For the marked law, ties for the largest arclength gap have probability zero. Angles are not sampled uniformly unless \(f\) says so.

## Proof
**1. A rooted cyclic-gap identity.** For an unordered three-point configuration, choose the unique counterclockwise root \(S=s\) just after the largest of the three successive arclength gaps. Write \(a,b\) for the first two forward gaps and \(c=L-a-b\) for the third (largest) gap. The change from labeled arclength coordinates to \((s,a,b)\) has unit Jacobian and six label permutations. Consequently, for any symmetric integrable three-point statistic \(H\),
\[
\mathbb EH=6\int_0^L\!ds\!\int_{\substack{a,b>0,\ a+b<L\\c>\max(a,b)}}\!da\,db\;f(s)f(s+a)f(s+a+b) H(s,a,b).
\]
All positions are interpreted modulo \(L\).

**2. Local inradius factorization, uniformly in unequal gaps.** Write \(\gamma(s)\) for the unit-speed parametrization and \(V(s)=\gamma'(s)\). For \(a+b\le\delta\), the oriented double area is
\[
2A=\int_0^a\!du\int_a^{a+b}\!dv\,\det(V(s+u),V(s+v)).
\]
Since the tangent turns at positive continuous rate \(\kappa\), uniformly in \(s\) and in \(0<a,b\) with \(a+b\le\delta\),
\[
A=\frac{\kappa(s)}4ab(a+b)(1+o_\delta(1)),
\qquad p=2(a+b)(1+O(\delta^2)),
\]
where \(p\) is triangle perimeter and \(o_\delta(1)\to0\) as \(\delta\downarrow0\). Because \(r=2A/p\),
\[
r(s,a,b)=\frac{\kappa(s)}4ab(1+o_\delta(1)).
\]
The error is uniform even when \(a/b\) tends to zero or infinity. Differentiating the integral and chord formulas also yields \(\partial r/\partial b=(\kappa(s)a/4)(1+o_\delta(1))\) uniformly on these small-gap sectors. This controls the marked change of variables below.

**3. The hyperbolic cusp area.** For fixed \(h>0\) and fixed small \(\delta>0\), elementary splitting of the \(a\)-integral gives
\[
\operatorname{Leb}_2\{a,b>0:\ a+b<\delta,\ ab<h t\}
=h t\log(1/t)+O_{h,\delta}(t).
\]
Indeed the central range \(ht/\delta<a<\delta-O(t)\) contributes \(ht\int da/a\), and both truncated ends contribute \(O(t)\). The same leading law holds uniformly for \(h\) in a fixed compact positive interval.

**4. Complete dominance analysis.** The region where \(a+b<\delta\) lies in the rooted domain for \(\delta<L/3\). There \(f(s)f(s+a)f(s+a+b)=f(s)^3(1+o_\delta(1))\). The second and third steps, with \(h=4/\kappa(s)\), show that this region contributes
\[
24t\log(L/t)\int_0^L\frac{f(s)^3}{\kappa(s)}\,ds\;(1+o_\delta(1))+O_\delta(t).
\]
It remains to exclude missing contributions of this order. On the compact part of the rooted gap domain away from the three zero-gap edges, \(r\) has a positive minimum. If one of the short gaps tends to zero while the other two stay bounded below by \(\delta\), the area vanishes linearly in that gap: for instance at \(a=0\), its first derivative is a positive multiple of \(\det(\gamma'(s),\gamma(s+b)-\gamma(s))\). Strict convexity makes this determinant uniformly positive for \(b\in[\delta,L-\delta]\). The semiperimeter stays bounded away from zero. Thus the one-gap boundary strips have probability \(O_\delta(t)\). The rooted condition excludes the remaining two-small-gap corners: if \(c\) were small it could not be the largest gap. Letting \(t\downarrow0\) then \(\delta\downarrow0\) proves the asserted limit.

**5. Conditional marks.** On the principal small-gap sector set \(v=\log(a/L)/\log(t/L)\) and \(w=r/t\). Fix any \(0<v,w<1\) and \(s\in\mathbb R/L\mathbb Z\). Then \(a=L(t/L)^v\to0\), while the implicit solution of \(r(s,a,b)=tw\) has
\[
b=\frac{4tw}{\kappa(s)a}(1+o(1))\to0.
\]
The Jacobian, using the derivative in step 2, is
\[
\left|\frac{\partial(a,b)}{\partial(v,w)}\right|
=\frac{4t\log(L/t)}{\kappa(s)}(1+o(1)).
\]
After multiplication by the rooted density factor six and division by \(\Pr(r<t)\), the density tends pointwise for almost every \((s,v,w)\) in \([0,L)\times(0,1)^2\) to \(f(s)^3/[\kappa(s)I(\Gamma,f)]\). The distribution outside this limiting domain has vanishing conditional probability by the same cusp estimate and one-gap strip bound. These densities integrate to one; Scheffé's lemma therefore gives convergence in total variation, hence the stated independence.

**6. Sharp density and shape comparisons.** Hölder's inequality with exponents \(3\) and \(3/2\) yields
\[
1=\int_0^L f\,ds\le I(\Gamma,f)^{1/3}\left(\int_0^L\sqrt\kappa\,ds\right)^{2/3}.
\]
The equality condition is \(f\propto\sqrt\kappa\), proving uniqueness of the optimum. For uniform sampling, Cauchy--Schwarz and the total-curvature theorem imply
\[
\int_0^L\frac{ds}{\kappa(s)}\ge\frac{L^2}{\int_0^L\kappa(s)\,ds}=\frac{L^2}{2\pi}.
\]
Equality means constant positive curvature, hence a circle. Finally, the standard layer-cake integral for negative moments and the two-sided sharp small-radius tail give the threshold \(p=1\).

## Verification
The standalone \(\texttt{verify.py}\) checks the exact unit-circle three-gap inradius identity, verifies the local curvature product expansion on a noncircular ellipse with strongly unbalanced short gaps, numerically checks the coefficient \(24I\) and its optimum on that ellipse, and confirms the circle coefficient \(6/\pi^2\). These finite tests corroborate algebra and normalizations but do not establish the infinite limit or total-variation convergence. The analytic steps establishing those claims are given above.

## Relationship to prior work
The exact circle law and its logarithmic small-inradius coefficient were already recorded for three uniform circle points; the circle special case here is **not** claimed as original. The circle specialization of the marked assertion is likewise not a separate novelty claim. The present theorem varies both the smooth positively curved boundary and its positive sampling density, obtaining a curvature-weighted spatial mark and a sharp, distinct sampling optimum. The previously published general-curve small-**area** law has exponent \(2/3\) and optimum \(f\propto\kappa^{1/3}\); its statistic is area rather than inradius, and its formula does not determine the ratio of area to semiperimeter needed here. The density \(f\propto\sqrt\kappa\) is also known as optimal for an unrelated expected Hausdorff approximation error, but that criterion does not imply the inradius coefficient or its marked law. Classical affine-arclength approximation and finite random-polygon area/perimeter limits likewise do not state this inradius law. Historical priority against all unindexed publications is not asserted.

## Limitations
The argument needs positive curvature, enough smoothness for the local tangent expansions, and a fixed positive sampling density; corners, flat points, correlated sampling, and densities that vanish are not covered. Rates of convergence and higher-order terms are not established. The joint mark uses Euclidean arclength to define logarithmic gaps; it is not an affine-invariant law. The circle limit and prior special cases must not be mistaken for independently novel findings. No independent mathematical audit has been performed.

## References
1. M. Craizer, R. C. Teixeira and M. A. H. B. da Silva, *Affine Properties of Convex Equal-Area Polygons*, arXiv:1103.2722, first public 2011-03-14. https://arxiv.org/abs/1103.2722
2. N. Koroleva and Ya. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360, first public 2013-01-07. https://arxiv.org/abs/1301.1360
3. S. R. Finch, *Random Cyclic Quadrilaterals*, arXiv:1610.00510, first public 2016-10-03 (for uniform circle-triangle background). https://arxiv.org/abs/1610.00510
4. *The full inradius law and two contrasting tails of random cyclic triangles*, publicly available research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-full-inradius-law-and-two-contrasting-tails-of-random-cyclic--f4fa44ae752a
5. *A sharp small-area law for inscribed random triangles and the optimal affine sampling density*, publicly available research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-small-area-law-for-inscribed-random-triangles-and-the-op--36a2639eeafd
6. *Clipped-curvature minimax sampling for Hausdorff and area approximation of convex curves*, publicly available research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-clipped-curvature-minimax-sampling-for-hausdorff-and-area-approx--7dfc7d4760ff
