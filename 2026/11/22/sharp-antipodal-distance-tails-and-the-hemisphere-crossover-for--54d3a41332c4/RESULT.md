# Sharp antipodal-distance tails and the hemisphere crossover for spherical lunes

## Finding

On the unit round sphere \(S^2\), let \(L_\alpha\) be the closed spherical lune whose longitudes lie in \([0,\alpha]\), with \(0<\alpha\le\pi\). Choose \(X,Y\) independently and uniformly by spherical area on \(L_\alpha\). Let \(D=d_{S^2}(X,Y)=\arccos(X\cdot Y)\), the ordinary ambient great-circle separation. The lune has area \(2\alpha\) and diameter \(\pi\).

For **every fixed** \(0<\alpha<\pi\), as \(\varepsilon\downarrow0\),

\[
\boxed{\Pr\{D>\pi-\varepsilon\}=C(\alpha)\varepsilon^4+O_\alpha(\varepsilon^6),\qquad C(\alpha)=\frac{1-\alpha\cot\alpha}{16\alpha^2}.}
\]

The coefficient is strictly increasing, with \(\lim_{\alpha\downarrow0}C(\alpha)=1/48\) and \(\lim_{\alpha\uparrow\pi}C(\alpha)=+\infty\). Hence the leading normalized tail coefficient uniquely determines the lune opening on \((0,\pi)\). Conditional on this near-antipodal event, the ordered north-pole/south-pole assignment has asymptotic probability \(1/2\) in either order; the two endpoint tangent-plane coordinates divided by \(\varepsilon\) jointly converge to normalized Lebesgue measure on

\[
\mathcal W_\alpha=\{(u,v)\in C_\alpha^{\rm tan}\times C_\alpha^{\rm tan}:\ |u+v|<1\},\qquad
C_\alpha^{\rm tan}=\{r(\cos\phi,\sin\phi):r\ge0,\ 0\le\phi\le\alpha\}.
\]

At the hemisphere endpoint \(\alpha=\pi\) the power changes to three:

\[
\Pr\{D>\pi-\varepsilon\}=\frac{\varepsilon^3}{3\pi}+o(\varepsilon^3).
\]

More sharply, for each **fixed** \(\lambda\ge0\), set \(\alpha_\varepsilon=\pi-\lambda\varepsilon\) and independently sample both points from \(L_{\alpha_\varepsilon}\). Then

\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-3}\Pr\{D>\pi-\varepsilon\}=F(\lambda)=\frac1{2\pi^2}\int_0^\pi J(\lambda\sin s)\,ds,}
\]

where, with \(J(t)=0\) for \(t\ge1\),

\[
J(t)=2\int_t^1(z-t)\sqrt{1-z^2}\,dz\quad(0\le t<1).
\]

This limit is uniform for \(\lambda\) in compact subsets of \([0,\infty)\). It satisfies \(F(0)=1/(3\pi)\), is positive and strictly decreasing, and has the matching far-side behavior

\[
\boxed{F(\lambda)\sim\frac1{16\pi\lambda}\quad(\lambda\to\infty).}
\]

Here \(\sim\) denotes a ratio tending to one; it is not an assertion of a uniform error bound when \(\lambda\) varies arbitrarily with \(\varepsilon\).

## Assumptions and scope

Area-uniform sampling means independent draws from the normalized two-dimensional Hausdorff area measure on the spherical *surface region*, not from a three-dimensional solid wedge, its boundary semicircles, or an invariant random line. All angles, including \(\varepsilon\), are measured in radians. The metric is the ordinary round-sphere great-circle distance; no Euclidean chord length is used in the probability event. With \(\alpha\le\pi\) the lune is an intersection of two hemispheres, so nonantipodal minimizing great-circle arcs also stay in the lune. The two polar vertices themselves have area zero. The fixed-opening error constant is allowed to depend on \(\alpha\) and is not asserted uniform as \(\alpha\uparrow\pi\). The critical scaling requires fixed nonnegative \(\lambda\). No larger-than-hemisphere lunes, nonuniform measures, or higher-dimensional spherical wedges are covered.

## Proof

**1. Diameter and localization.** The north and south poles both lie in every lune, so the great-circle diameter is exactly \(\pi\). If \(\alpha<\pi\), any other antipodal pair would require two longitudes differing by \(\pi\) to lie in the same interval of length less than \(\pi\), which is impossible. Thus the only maximizers are the two ordered pole pairs. Put \(Z=-Y\); the exact identity \(D(X,Y)=\pi-d_{S^2}(X,Z)\) converts the desired event into \(d_{S^2}(X,Z)<\varepsilon\). Compactness and the preceding maximizer classification localize every such pair near opposite poles for small \(\varepsilon\).

Near the north and south poles, write respectively

\[
X=(u,\sqrt{1-|u|^2}),\qquad Y=(v,-\sqrt{1-|v|^2}),\qquad u,v\in C_\alpha^{\rm tan}.
\]

The spherical area elements are \((1-|u|^2)^{-1/2}du\) and \((1-|v|^2)^{-1/2}dv\). Because \(\alpha<\pi\), the elementary bound \(|u+v|\ge\cos(\alpha/2)(|u|+|v|)\) holds for the two tangent cone vectors. Since \(X+Y=(u+v,\sqrt{1-|u|^2}-\sqrt{1-|v|^2})\), it follows, uniformly in the localized region, that

\[
d_{S^2}(X,-Y)=|u+v|+O_\alpha((|u|+|v|)^3).
\]

The probability event forces \(|u|+|v|=O_\alpha(\varepsilon)\). Upon setting \(u=\varepsilon U\), \(v=\varepsilon V\), both area densities equal \(1+O_\alpha(\varepsilon^2)\), and the boundary of the scaled event moves only \(O_\alpha(\varepsilon^2)\) in a bounded domain. Its defining homogeneous norm has a nonzero radial derivative away from the origin, so the scaled four-dimensional volume changes by \(O_\alpha(\varepsilon^2)\). Including the two equiprobable ordered pole arrangements gives

\[
\Pr\{D>\pi-\varepsilon\}=\frac{2\varepsilon^4}{(2\alpha)^2}\left[M(\alpha)+O_\alpha(\varepsilon^2)\right],\quad
M(\alpha)=\iint_{C_\alpha^{\rm tan}\times C_\alpha^{\rm tan}}\mathbf1_{\{|U+V|<1\}}\,dU\,dV.
\]

The same compact rescaling and dominated convergence with any bounded continuous test function gives the stated joint conditional limit, as well as the equal weights for the two ordered polar assignments.

**2. Exact cone-pair volume.** Write \(e_0=(1,0)\) and \(e_\alpha=(\cos\alpha,\sin\alpha)\). Every tangent-cone vector has a unique representation \(u=se_0+te_\alpha\) with \(s,t\ge0\); the Jacobian is \(\sin\alpha\). For a pair write the two coefficient sums as \(S=s+s'\), \(T=t+t'\). The interval fibers have lengths \(S,T\), hence

\[
M(\alpha)=\sin^2\alpha\int_{\substack{S,T\ge0\\S^2+2ST\cos\alpha+T^2<1}}ST\,dS\,dT
=\frac{\sin^2\alpha}{4}\int_0^\infty\frac{z\,dz}{(1+2z\cos\alpha+z^2)^2}.
\]

Completing the square and evaluating this elementary rational integral gives

\[
\int_0^\infty\frac{z\,dz}{(1+2z\cos\alpha+z^2)^2}
=\frac{1-\alpha\cot\alpha}{2\sin^2\alpha},\qquad
M(\alpha)=\frac{1-\alpha\cot\alpha}{8}.
\]

Substitution into Step 1 proves the fixed-opening coefficient and its \(O_\alpha(\varepsilon^6)\) error. For strict monotonicity one may logarithmically differentiate the classical Euler product \(\sin\alpha/\alpha=\prod_{k\ge1}(1-\alpha^2/(k\pi)^2)\), valid on \(0<\alpha<\pi\), obtaining

\[
C(\alpha)=\frac18\sum_{k=1}^{\infty}\frac1{k^2\pi^2-\alpha^2}.
\]

Every summand is positive and strictly increasing. The limits follow from the sum at zero and the divergent first summand at \(\pi\). This also proves uniqueness of opening reconstruction from the coefficient, without numerical monotonicity assumptions.

**3. Critical geometry at the hemisphere.** Write \(\delta=\pi-\alpha_\varepsilon=\lambda\varepsilon\). For \(Z=-Y\), the domains occupied by \(X\) and \(Z\) approach opposite hemispheres as \(\delta\to0\). An \(\varepsilon\)-close pair therefore lies in an \(O_\lambda(\varepsilon)\)-wide strip about their limiting common great-circle boundary. This great circle has two semicircle branches of length \(\pi\), corresponding to the two possible ordered choices of the lune's bounding meridians. On a branch parameterized by arclength \(s\in(0,\pi)\), the two domain boundaries are transversely separated by \(\delta\sin s+O_\lambda(\delta^2)\).

Use inward Fermi normal distances \(u,w\ge0\) from those respective boundary arcs for \(X\) and \(Z\), and let \(s'\) be the arclength coordinate of \(Z\). In the active strip \(u,w,|s-s'|=O_\lambda(\varepsilon)\), the exact round metric in Fermi coordinates and the cosine formula yield

\[
\frac{d_{S^2}(X,Z)^2}{\varepsilon^2}
= h^2+(a+b+\lambda\sin s)^2+o(1),\quad
h=\frac{s'-s}{\varepsilon},\quad a=\frac u\varepsilon,\quad b=\frac w\varepsilon.
\]

The normalized product area element is \((4\pi^2)^{-1}\varepsilon^3(1+o(1))\,ds\,dh\,da\,db\). Each of the two boundary branches contributes equally. The neighborhoods of the two polar vertices can be excluded by a fixed small arclength cutoff, and their scaled contribution is bounded by a constant times the cutoff plus \(O_\lambda(\varepsilon)\): an \(\varepsilon\)-close pair must remain in the transverse \(O_\lambda(\varepsilon)\) strip, and the second point must lie in a geodesic disk of area \(O(\varepsilon^2)\). Thus letting the cutoff tend to zero after the limit loses no mass. These bounds are uniform for bounded \(\lambda\).

Dominated convergence now gives

\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-3}\Pr\{D>\pi-\varepsilon\}
=\frac{2}{4\pi^2}\int_0^\pi\int_{a,b\ge0}\int_{\mathbb R}
\mathbf1_{\{h^2+(a+b+\lambda\sin s)^2<1\}}\,dh\,da\,db\,ds.
\]

For fixed \(a+b=t\), the \((a,b)\) fiber length is \(t\); integrating first in \(h\) gives \(2\sqrt{1-(t+\lambda\sin s)^2}_+\). This proves the integral formula for \(F\) with the stated \(J\), including compact-uniform convergence. The case \(\lambda=0\) is the hemisphere.

**4. Crossover endpoint values and matching.** At zero, \(J(0)=2/3\), giving \(F(0)=1/(3\pi)\). The integral defining \(J\) shows it is positive on \([0,1)\), strictly decreasing there, and zero thereafter; consequently \(F\) is positive and strictly decreasing. As \(\lambda\to\infty\), the integrand is supported in two shrinking intervals around \(s=0,\pi\). Using \(t=\lambda\sin s\) on both intervals and dominated convergence,

\[
\int_0^\pi J(\lambda\sin s)\,ds\sim\frac2\lambda\int_0^1J(t)\,dt,\qquad
\int_0^1J(t)\,dt=\int_0^1z^2\sqrt{1-z^2}\,dz=\frac\pi{16}.
\]

This yields \(F(\lambda)\sim1/(16\pi\lambda)\). Independently, \(C(\pi-\delta)\sim1/(16\pi\delta)\) as \(\delta\downarrow0\), so the overlapping formal limits match their coefficients; this matching does not assert uniformity for arbitrary diverging \(\lambda\).

## Verification

Run `python3 verification/check_lune.py` using the Python 3 standard library. The checker evaluates the four-dimensional cone convolution by an independent one-dimensional Simpson integral, checks exact special endpoint identities, and computes finite-distance probabilities from the *exact spherical dot products* using deterministic four-dimensional Halton cubature. It compares three fixed-angle cases and four critical-window cases against the limiting coefficients and confirms far-window matching numerically. The expected successful terminal line is `LUNE_ANTIPODAL_TAIL_CHECKS_OK 20`. Computation is supplementary: the all-angle, limit, and strict-monotonicity statements depend on the above analytic proof, not on any finite grid or numerical extrapolation.

## Relationship to prior work

Gille (2005) derives distributions of isotropically sampled chords of a **solid hemisphere**, a different measure from independent spherical-area endpoints. Cabré, Fosalba, Gaztañaga, and Manera (2007), Appendix B1, derive pair-separation/containment probabilities for **spherical polar caps**, including the hemispherical special geometry, rather than a varying narrow lune. Maehara and Martini (2017) derive area geometry of lunes and selected expectations for random point distances on hemispheres; the basic hemisphere observations and lune-area formula are not claimed as new. Moseeva, Tarasov, and Zaporozhets (2020) develop random-distance laws for spherical convex bodies generated by line-free cones and explicitly specialize to caps, whereas a full lune contains an antipodal pole pair. Existing published analyses of independent area-uniform pairs **on the same lune family** establish squared-distance moments, their shape optimization, and inverse moment classification, but do not give the near-antipodal distance coefficient, the four-to-three power change, or the opening-dependent critical scaling stated here. Published results on hemispherical caps, spherical-football quotients, and Haar-random great-circle sections do not imply the displayed lune-pair formulas under their different domains or sampling. A definitive comprehensive historical-priority determination has not been made.

## Limitations

The result is for the full spherical surface lune in dimension two with opening no greater than \(\pi\), and for two independent area-uniform endpoints. The \(O_\alpha(\varepsilon^6)\) bound is not uniform near the hemisphere. The crossover is proved only for fixed nonnegative \(\lambda\), uniformly on bounded sets; no global double-scaling error bound is asserted. The conditional limit is for fixed \(\alpha<\pi\), not a full joint conditional limit in the moving-opening window. Independent mathematical audit and definitive historical-priority confirmation are not part of this result.

## References

1. W. Gille, *Chord Length Distributions of the Hemisphere*, Journal of Mathematics and Statistics **1** (2005), 24–28. First public date verified as 2005-03-31 from the publisher: https://doi.org/10.3844/jmssp.2005.24.28 .
2. A. Cabré, P. Fosalba, E. Gaztañaga, M. Manera, *Error analysis in cross-correlation of sky maps: application to the ISW detection*, arXiv:astro-ph/0701393, first posted 2007-01-15; see Appendix B1: https://arxiv.org/abs/astro-ph/0701393 .
3. H. Maehara, H. Martini, *Geometric Probability on the Sphere*, Jahresbericht der Deutschen Mathematiker-Vereinigung **119** (2017), 93–132, published online 2017-01-30, https://doi.org/10.1365/s13291-017-0158-5 .
4. T. Moseeva, A. Tarasov, D. Zaporozhets, *Random sections of spherical convex bodies*, first posted 2020-07-14, https://arxiv.org/abs/2007.07297 .
