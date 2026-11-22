# Cubic extreme detour law and shape recovery for random annular pairs

## Finding

Let \(0<r<R<\infty\), let \(K_{r,R}=\{x\in\mathbb R^2:r\leq\lVert x\rVert\leq R\}\) be the closed planar annulus, and independently sample \(X,Y\) from its normalized area measure. Write \(d_K\) for the intrinsic length distance in \(K_{r,R}\), \(d_E(X,Y)=\lVert X-Y\rVert\), and \(Z=d_K(X,Y)/d_E(X,Y)\) for \(X\ne Y\). Then the sharp metric dilation is

\[
\max_{X\ne Y\in K_{r,R}}\frac{d_K(X,Y)}{d_E(X,Y)}=\frac\pi2,
\]

with equality **if and only if** \(\lVert X\rVert=\lVert Y\rVert=r\) and \(Y=-X\).

Set \(H=R^2-r^2\). For every fixed \(0<r<R\), the complete sharp leading extreme-stretch law is

\[
\boxed{\Pr\!\left(Z>\frac\pi2-\varepsilon\right)
 =\frac{64r^4}{3\pi^3H^2}\varepsilon^3
 +O_{r,R}(\varepsilon^{7/2})}
\qquad(\varepsilon\downarrow0).
\]

This observable is scale invariant. If \(C=\lim_{\varepsilon\downarrow0}\varepsilon^{-3}\Pr(Z>\pi/2-\varepsilon)\) and \(s=\sqrt{3\pi^3C/64}\), then

\[
\boxed{\frac rR=\sqrt{\frac{s}{1+s}}}.
\]

Thus its single extreme-tail coefficient uniquely identifies the annulus aspect ratio. It cannot identify its absolute scale.

There is also a marked limit. Let \(\rho=\lVert X\rVert\), \(\sigma=\lVert Y\rVert\), and let \(\varphi\in[0,\pi]\) be the minor angular separation. Conditional on \(Z>\pi/2-\varepsilon\), the vector

\[
\left(\frac{\pi(\rho-r)}{4r\varepsilon},\ 
\frac{\pi(\sigma-r)}{4r\varepsilon},\ 
\frac{\pi-\varphi}{2\varepsilon}\right)
\]

converges in distribution to the uniform probability distribution (density \(6\)) on \(\{(a,b,c):a,b,c\geq0,\ a+b+c<1\}\).

## Assumptions and scope

The inner hole has positive radius and both radii are fixed as \(\varepsilon\to0\). Distances are lengths of shortest *annulus-constrained* rectifiable paths, including the two circular boundary components. Endpoints are sampled with two-dimensional area measure, not perimeter measure. The ratio is defined away from the probability-zero diagonal \(X=Y\); it can be continuously extended by \(1\) on that diagonal. The theorem concerns the intrinsic-to-ambient distance *ratio*, not an endpoint of the intrinsic distance alone. The limiting law is dimensionless. No convergence uniform in the degenerate limits \(r\downarrow0\) or \(r\uparrow R\) is claimed.

## Proof

**1. The sharp global endpoint and all maximizers.** Put \(d=\lVert X-Y\rVert\). If the segment \([X,Y]\) misses the open inner disk, \(d_K=d\) and \(Z=1\). Otherwise, let \(U,V\) be its first and last intersections with the inner circle along the segment. Follow the straight segment from \(X\) to \(U\), take a shorter circular arc from \(U\) to \(V\), and follow the segment from \(V\) to \(Y\). All three pieces lie in the annulus: the straight portions lie outside the hole and within the convex outer disk, and the circular arc lies on the inner boundary. For \(c=\lVert U-V\rVert\), the shorter circular arc has length at most \(\pi c/2\), with equality only for diametrically opposite \(U,V\). Consequently,

\[
d_K(X,Y)\leq d-c+\frac\pi2c\leq\frac\pi2d.
\]

Equality in both inequalities requires \(c=d\) and antipodal \(U,V\). This forces \(X=U\), \(Y=V\) and antipodal points on the inner circle. Conversely, the intrinsic shortest route between such endpoints is the inner semicircle, of length \(\pi r\), and the chord has length \(2r\). The ratio tends to \(1\) near the diagonal, by smooth local boundary geometry. Compactness therefore localizes all near-maximal ratios to the inner-antipodal circle of ordered pairs.

**2. Exact shortest-path formula near the maximizers.** Put

\[
\rho=r(1+u),\quad \sigma=r(1+v),\quad
\varphi=\pi-\eta,
\qquad u,v,\eta\geq0.
\]

Near the maximizing set, the Euclidean segment crosses the open inner disk. The shortest annular route has two tangent segments meeting a shorter arc of that disk; its length is

\[
\frac{d_K}{r}
 =\pi-\eta+F(u)+F(v),\quad
F(z)=\sqrt{2z+z^2}-\arccos\!\frac1{1+z}.
\]

Indeed, the tangent lengths are \(r\sqrt{2z+z^2}\), and the inner circular arc removes the two tangent angles \(\arccos(1/(1+z))\) from \(\varphi\). With \(t=\arccos(1/(1+z))\), one has \(F(z)=\tan t-t\), so

\[
F(z)=\frac{2\sqrt2}{3}z^{3/2}+O(z^{5/2}).
\]

The chord length, independently, is

\[
\frac{d_E}{r}=\sqrt{(u-v)^2+
4(1+u)(1+v)\cos^2(\eta/2)}
=2+u+v+O((u+v)^2+\eta^2).
\]

Dividing shows that the exact ratio deficit has a uniform local expansion

\[
\boxed{\frac\pi2-Z
=\frac\pi4(u+v)+\frac\eta2
 +O\!\left((u+v)^{3/2}+\eta^2+\eta(u+v)\right).}
\]

The three positive linear coefficients imply that any event \(\pi/2-Z<\varepsilon\) is localized to \(u,v,\eta=O(\varepsilon)\). This follows first by the compactness/unique-maximizer argument in step 1, then by absorbing the smaller local remainder into half the positive linear part.

**3. Joint density and a uniform simplex.** Let \(H=R^2-r^2\). The two independent radial densities are \(2\rho/H\) and \(2\sigma/H\); the minor angular difference is independent and uniform on \([0,\pi]\). In the above \((u,v,\eta)\) coordinates the exact joint density near zero is

\[
\frac{4r^4}{\pi H^2}(1+u)(1+v)\,du\,dv\,d\eta.
\]

Define \(a=\pi u/(4\varepsilon)\), \(b=\pi v/(4\varepsilon)\), and \(c=\eta/(2\varepsilon)\). The Jacobian is \(32\varepsilon^3/\pi^2\), so the pushed-forward density is

\[
\frac{128r^4}{\pi^3H^2}\varepsilon^3
\left[1+O(\varepsilon)\right]\,da\,db\,dc.
\]

The event tends to the unit three-simplex \(a+b+c<1\), of Euclidean volume \(1/6\). The above uniform remainder shifts its boundary by at most \(O(\varepsilon^{1/2})\) in the rescaled coordinates; its volume changes by at most \(O(\varepsilon^{1/2})\), because the positive linear functional has bounded level-set area on the fixed box. Thus the probability is

\[
\frac{128r^4}{\pi^3H^2}\varepsilon^3
\left[\frac16+O(\varepsilon^{1/2})\right]
=\frac{64r^4}{3\pi^3H^2}\varepsilon^3+O_{r,R}(\varepsilon^{7/2}).
\]

Normalizing the same limit integral gives constant density \(6\) on the simplex and establishes weak convergence of the conditional marks.

**4. Unique aspect-ratio recovery.** The coefficient obeys

\[
\frac{3\pi^3C}{64}=
\left(\frac{r^2}{R^2-r^2}\right)^2.
\]

Taking the positive square root yields \(s=r^2/(R^2-r^2)\) and \((r/R)^2=s/(1+s)\). This map is strictly increasing from \(0\) to \(1\) as \(r/R\) increases from \(0\) to \(1\), giving the unique inversion above.

## Verification

The standalone Python file `verify_annulus_stretch.py` independently computes shortest paths using both the direct-chord and tangent-plus-inner-arc regimes; brackets and solves the exact angular threshold for the event \(Z>\pi/2-\varepsilon\), integrates that threshold with nested Gauss–Legendre quadrature, and compares the probabilities to the analytic cubic coefficient. For three annulus shapes and three small deficits (nine numerical integrations), the normalized ratios tend toward one; e.g. for \(r/R=1/2\), they are approximately \(1.21028\), \(1.11201\), \(1.06118\) as \(\varepsilon=0.02,0.008,0.003\), and \(1.01707\) at \(0.0003\). It additionally checks 20,000 sampled pairs against the global bound, verifies five inverse reconstructions and checks three local expansions. Its success marker is `ANNULUS_STRETCH_TAIL_CHECKS_OK 20017`. All checks are numerical sanity tests; the infinite theorem is established by the geometric proof above, not by finite samples. Reproduce using Python 3, NumPy and SciPy: `python verify_annulus_stretch.py`.

## Relationship to prior work

Tangency plus circular arcs in obstacle-avoiding shortest paths are classical, as explicitly described by Chang, Choi, Kwon, Park and Yap (2005). Their computational result does not determine a distribution of the *ratio* of intrinsic to Euclidean distances. Earlier work on the two-point *intrinsic distance* on concentric annuli has an upper endpoint attained at outer-antipodal pairs and a cubic distance-tail law. The ratio studied here instead has its maxima at **inner-antipodal** pairs, and its coefficient is scale invariant and encodes aspect ratio directly; the prior marginal distribution of intrinsic distance cannot determine the joint ratio law. Metric-measure distance-matrix theory supplies a general probability framework, not the coefficient or conditional simplex. In a different geometry, cone-sidewall intrinsic-to-extrinsic ratios have a different sharp endpoint and exponent; their surface-development formula cannot be reduced to the annulus with its flat obstacle and path-cut locus. The contribution asserted here is only the coupled ratio law and its marked and inversion consequences, not the known shortest-path formula or the classical bound for circular boundary arcs.

## Limitations

The small-deficit expansion is fixed-shape and is not uniform as the inner hole vanishes or the annulus becomes thin. At the disk endpoint \(r=0\), intrinsic and Euclidean distances are identical and \(Z\equiv1\); the positive-hole tail limit is singular there. The checker uses floating-point quadrature, not interval-certified integration. A complete exact distribution of \(Z\) away from the upper endpoint is not established. Historical priority beyond the inspected literature remains open and the result has not had independent mathematical validation.

## References

1. E.-C. Chang, S. W. Choi, D. Kwon, H. Park and C. K. Yap, *Shortest Path amidst Disc Obstacles is Computable*, 21st ACM Symposium on Computational Geometry, 2005, pp. 116–125. Full public manuscript: https://cs.nyu.edu/exact/doc/computable.pdf ; DOI: https://doi.org/10.1145/1064092.1064112. Conference proceedings began June 6, 2005.
2. S. Gadgil and M. Krishnapur, *Lipschitz correspondence between metric measure spaces and random distance matrices*, arXiv:1110.6333, posted October 28, 2011, https://arxiv.org/abs/1110.6333.
3. D. Z. Chen and H. Wang, *Computing Shortest Paths among Curved Obstacles in the Plane*, ACM Transactions on Algorithms **11** (2015), article 26, first published April 13, 2015, https://doi.org/10.1145/2660771. The accessible abstract concerns computational shortest-path methods.
