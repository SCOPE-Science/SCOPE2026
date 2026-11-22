# A two-ended Pareto law for random hyperbolic cyclic-polygon area deficits

## Finding

Fix an integer \(n\ge3\). Choose \(n\) independent points uniformly by hyperbolic arclength from a geodesic circle of radius \(R>0\) in the curvature-\(-1\) hyperbolic plane, and let \(A_{n,R}\) be the area of their geodesic convex hull. Let \(M_{n,R}\) be the largest area of any geodesic \(n\)-gon inscribed in the **same** circle. For every finite \(R\), the unique maximizing configuration, modulo rotation, is the regular polygon.

Anchor the cyclic labels at the first sampled vertex, and let the successive positive central-angle gaps be \(G_1,\ldots,G_n\), with \(\sum_iG_i=2\pi\). The normalized gaps have distribution \(\operatorname{Dirichlet}(1,\ldots,1)\). Then the regular-maximal area deficit has the almost-sure, fixed-\(n\) limit

\[
\boxed{e^R(M_{n,R}-A_{n,R})\ \longrightarrow\ Z_n
=4\sum_{i=1}^{n}\cot(G_i/2)-4n\cot(\pi/n).}
\]

The law of \(Z_n\) is supported on \([0,\infty)\), has no atom at zero, and has two sharp endpoint asymptotics:

\[
\boxed{\Pr(Z_n>t)\sim\frac{4n(n-1)}{\pi t}\quad(t\to\infty),}
\qquad
\boxed{\Pr(Z_n\le t)\sim K_n t^{(n-1)/2}\quad(t\downarrow0),}
\]

where, defining \(H_n=\cos(\pi/n)/\sin^3(\pi/n)\),

\[
\boxed{K_n=\frac{(n-1)!\,\pi^{(n-1)/2}}{(2\pi)^{n-1}\,\Gamma((n+1)/2)\sqrt n\,H_n^{(n-1)/2}}.}
\]

Consequently \(\mathbb E[Z_n^p]<\infty\) **if and only if** \(0<p<1\); in particular \(\mathbb E Z_n=\infty\) although the unscaled finite-radius deficit is bounded. Conditional on \(Z_n>t\), its unique shortest gap is asymptotically equally likely to have any of the \(n\) cyclic labels; the mark \(t\min_iG_i/8\) converges to \(\operatorname{Uniform}(0,1)\), independently of the limiting normalized other \(n-1\) gaps, which have distribution \(\operatorname{Dirichlet}(1,\ldots,1)\). In particular \(Z_n/t\), conditional on \(Z_n>t\), converges to a Pareto random variable with tail \(1/y\) for \(y\ge1\). At the opposite endpoint, conditioned on \(Z_n\le t\), the rescaled centered gap vector \((G_i-2\pi/n)/\sqrt t\) tends to the uniform distribution in the \((n-1)\)-dimensional ellipsoid \(H_n\sum_i u_i^2\le1\), \(\sum_i u_i=0\).

## Assumptions and scope

All geometry uses Gaussian curvature \(-1\). The sample size \(n\ge3\) is fixed throughout the limit \(R\to\infty\); no statement is uniform over increasing \(n\). Sampling is independent on the hyperbolic circle with normalized intrinsic arclength, equivalently uniform polar angle in a centered Poincaré disk. Cyclic indexing is anchored at the first sampled point, not at the smallest angle relative to a fixed external ray; this makes all \(n\) circular gaps exchangeable with the stated Dirichlet distribution. Hull edges are shortest complete-plane geodesics, and the hull area is intrinsic hyperbolic area. The maximizing area \(M_{n,R}\) is deterministic and taken among \(n\)-vertex polygons on that same circle, not among polygons of arbitrary radii. Conditioning in the marked statements is performed **after** the large-radius limiting law \(Z_n\) is formed. The conditional limit at the lower endpoint uses ordinary intrinsic Lebesgue measure on the hyperplane \(\sum_i u_i=0\), normalized on the ellipsoid.

## Proof

**1. Exact finite-radius area and the regular maximizer.** In the Poincaré disk the circle has Euclidean radius \(r=\tanh(R/2)\). Put \(C=\cosh R=(1+r^2)/(1-r^2)>1\). A disk automorphism carrying the vertex \(r\) to zero converts its two incident geodesics to diameters. Comparing their tangent angles shows that the interior angle between incident edges with adjacent positive polar gaps \(g,h\), where \(g+h<2\pi\), is

\[
\arctan\!\left(C^{-1}\cot(g/2)\right)
+\arctan\!\left(C^{-1}\cot(h/2)\right).
\]

The principal inverse tangents make the expression continuous also when one of the gaps exceeds \(\pi\). Summing the interior angles and applying Gauss--Bonnet gives

\[
A_{n,R}=(n-2)\pi-2\sum_{i=1}^n\arctan\!\left(C^{-1}\cot(G_i/2)\right)
=\sum_{i=1}^n F_C(G_i),
\]

\[
F_C(g)=2\operatorname{atan2}(C\sin(g/2),\cos(g/2))-g,
\qquad 0<g<2\pi.
\tag{1}
\]

The \(\operatorname{atan2}\) angle in (1) lies in \((0,\pi)\); no unannounced branch change is used. Its derivative is

\[
F_C'(g)=\frac{C}{1+(C^2-1)\sin^2(g/2)}-1.
\tag{2}
\]

For any two positive gaps \(x=t+d,y=t-d\) in the simplex, \(t=(x+y)/2<\pi\). Since \(\sin^2((t+d)/2)-\sin^2((t-d)/2)=\sin t\sin d>0\) when \(d>0\), formula (2) implies \(F_C'(t+d)-F_C'(t-d)<0\). Therefore replacing unequal gaps by their average **strictly increases** their total area contribution. Repeated pair averaging, or the resulting strict Schur-concavity on the simplex, shows that the unique maximum is attained at \(G_i=2\pi/n\), all \(i\). Thus \(M_{n,R}=nF_C(2\pi/n)\). This reasoning does not exclude configurations having one gap greater than \(\pi\).

**2. The limiting random variable and positivity.** For each fixed \(0<g<2\pi\), the principal-angle representation above yields

\[
F_C(g)=\pi-g-2\arctan\!\left(C^{-1}\cot(g/2)\right).
\]

Since \(e^R/C\to2\) as \(R\to\infty\), equation (1) implies, for each fixed positive gap vector,

\[
e^R(M_{n,R}-A_{n,R})\longrightarrow
4\sum_i\left[\cot(G_i/2)-\cot(\pi/n)\right].
\tag{3}
\]

The gaps are positive almost surely, and they can be coupled without changing with \(R\), so (3) is an almost-sure convergence statement. Pair smoothing applied to the sum of cotangents also strictly **decreases** that sum, because the difference between the cotangent derivatives at \(t+d\) and \(t-d\) is positive for \(t<\pi\), \(d>0\). Hence the minimum of the cotangent sum is attained uniquely at equal gaps; this proves \(Z_n\ge0\), with equality only at the probability-zero regular configuration. The cotangent sum grows without bound if a single gap tends to zero with the remaining gaps staying in a compact subset of the positive simplex; thus the support is unbounded above. Connectedness and continuity show it fills \([0,\infty)\).

**3. Upper Pareto tail.** For an unordered sample of \(n\) uniform circular angles, the cyclic gaps have constant density on their simplex. A single gap \(G_i\) obeys \(G_i/(2\pi)\sim\operatorname{Beta}(1,n-1)\), hence

\[
\Pr(G_i<x)=\frac{n-1}{2\pi}x+O_n(x^2),\qquad x\downarrow0.
\tag{4}
\]

Fix \(a\in(1/2,1)\). The chance that two distinct gaps are less than \(t^{-a}\) is \(O_n(t^{-2a})=o(t^{-1})\), because their joint density is locally bounded for fixed \(n\ge3\). Outside this negligible event, if every gap is at least \(t^{-a}\), all positive cotangent contributions are \(O_n(t^a)=o(t)\); thus \(Z_n>t\) is impossible for large \(t\). If instead exactly one gap \(G_i<t^{-a}\), the sum of the other cotangents is uniformly \(O_n(t^a)\) in absolute value. (A second gap can approach \(2\pi\) only by forcing additional gaps below \(t^{-a}\), which has already been excluded.) Using \(\cot(g/2)=2/g+O(g)\), we get

\[
Z_n=\frac8{G_i}+O_n(t^a).
\]

Consequently, up to an \(o(t^{-1})\) error in probability, the event \(Z_n>t\) is equivalent to the disjoint union of \(G_i<8t^{-1}(1+o(1))\) for \(i=1,\ldots,n\). Summing (4) gives

\[
\lim_{t\to\infty}t\Pr(Z_n>t)=\frac{4n(n-1)}\pi.
\tag{5}
\]

For any positive random variable, \(\mathbb E[Z_n^p]=p\int_0^\infty t^{p-1}\Pr(Z_n>t)\,dt\). The boundedness of the distribution at zero and the sharp two-sided asymptotic (5) imply the claimed moment threshold.

For the conditional marks, the \(n\) candidate shortest gaps have equal weights by exchangeability. Conditional on a fixed gap \(G_i=x\), the other \(n-1\) gaps divided by \(2\pi-x\) are uniform on their positive simplex, i.e. \(\operatorname{Dirichlet}(1,\ldots,1)\), and this normalized vector is independent of \(x\). Equation (4) and the threshold \(x<8/t\) give conditional convergence of \(tG_i/8\) to uniform \([0,1]\), independently of the other normalized gaps. The exceptional two-small-gap cases have vanishing conditional probability by the preceding estimates. Finally (5) or the pointwise relation \(Z_n/t\sim8/(tG_i)\) yields the Pareto excess law and joint independence of its marks.

**4. Lower endpoint and conditional shape.** Write \(g_0=2\pi/n\), \(u_i=G_i-g_0\) with \(\sum_i u_i=0\). Taylor's theorem at the unique minimizer and cancellation of linear terms give

\[
Z_n=H_n\sum_{i=1}^n u_i^2+O_n(\|u\|^3),\qquad
H_n=\frac{\cos(\pi/n)}{\sin^3(\pi/n)}>0.
\tag{6}
\]

The \(n-1\) free coordinates \(u_1,\ldots,u_{n-1}\) have constant joint density \((n-1)!/(2\pi)^{n-1}\), and \(u_n=-\sum_{i<n}u_i\). The quadratic form \(\sum_i u_i^2\) has matrix \(I_{n-1}+\mathbf1\mathbf1^\top\), of determinant \(n\). Its sublevel set \(H_n\sum_i u_i^2\le t\) has coordinate volume \(\pi^{(n-1)/2}(t/H_n)^{(n-1)/2}/[\Gamma((n+1)/2)\sqrt n]\). The unique strict minimum and the uniform cubic remainder in a small neighborhood justify replacing the true sublevel volume with this quadratic volume up to relative \(o(1)\). Multiplying by the gap density proves \(K_n\) and the stated small-\(t\) probability. The same blow-up of constant density and of the sublevel sets proves the conditional uniform-ellipsoid limit by dominated convergence.

## Verification

The self-contained `check_cyclic_area_tail.py` (Python 3, NumPy) compares the exact \(\operatorname{atan2}\) area expression against the independently calculated Gauss--Bonnet angle expression over many irregular samples and several radii; checks the regular extremum, finite-radius convergence to (3), and the quadratic Hessian (6); and performs reproducible Dirichlet simulations of the Pareto coefficient and conditional shortest-gap mark. It reports `HYPERBOLIC_CYCLIC_PARETO_CHECK_OK (1310 deterministic checks)` with the pinned random seed. The analytic argument, not this finite simulation, establishes the infinite-law statements. The reported samples are diagnostics, not a proof that no alternative law is possible.

## Relationship to prior work

Abrosimov and Mednykh (2013), Section 4.2, derive deterministic area identities for hyperbolic cyclic quadrilaterals; Kouřimská, Skuppin and Springborn (2015), Section 4, establish existence and uniqueness of hyperbolic cyclic polygons via prescribed lengths. Neither inspected paper studies boundary-uniform random polygons or these two endpoint laws. The previously established all-\(n\) exact **mean-area** formula for the identical hyperbolic-circle sampling model has a mean deficit with leading factor \(4n(n-1)R e^{-R}/\pi\). That factor matches the coefficient in (5), illustrating a typical-versus-mean discrepancy caused by rare angular collisions, but the mean result alone does not imply a distributional limit, a Pareto moment threshold, a lower-tail constant, or the marked rare configurations. A separately established random cyclic-polygon critical-window law sends \(n\to\infty\) and is not the fixed-\(n\), \(R\to\infty\) law here. A published Pareto deficit for **horocycle-segment** triangles has different sampling and a different numerical coefficient. A prior result on the **inradius**, rather than area, of triangles on expanding circles has a different rescaling and Pareto exponent. Classical Dirichlet spacing methods and the hyperbolic area formula themselves are not claimed as new. Historical priority is not independently certified; unindexed equivalent distribution identities remain possible.

## Limitations

The two endpoint asymptotics concern the limiting variable after a fixed-\(n\), increasing-radius limit; they are not uniform finite-radius estimates when the deficit threshold grows jointly with \(R\). The result does not cover samples in a hyperbolic disk, random horocycle segments, nonuniform angular measures or the joint \(n\to\infty\) regime. No finite-sample statistical optimality statement is made. The existing mean-area asymptotic is used for comparison, not claimed as a new finding. No independent mathematical or historical audit has been conducted.

## References

1. N. Abrosimov and A. Mednykh, *Volumes of polytopes in spaces of constant curvature*, arXiv:1302.4919v1 (first public posting 2013-02-20), Section 4.2, https://arxiv.org/abs/1302.4919.
2. H. Kouřimská, L. Skuppin and B. Springborn, *A variational principle for cyclic polygons with prescribed edge lengths*, arXiv:1506.08069v1 (first public posting 2015-06-26), Section 4, https://arxiv.org/abs/1506.08069.
3. *Finite polylogarithmic mean-area laws for random hyperbolic cyclic polygons* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-finite-polylogarithmic-mean-area-laws-for-random-hyperbolic-cycl--205189fce0d1/RESULT.md.
4. *A critical logarithmic-radius crossover for random hyperbolic cyclic-polygon area* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-a-critical-logarithmic-radius-crossover-for-random-hyperbolic-cy--a2dad3e05c2a/RESULT.md.
5. *A Pareto area-deficit law for triangles sampled on expanding hyperbolic horocycles* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-a-pareto-area-deficit-law-for-triangles-sampled-on-expanding-hyp--df9c2fffee99/RESULT.md.
6. *A universal half-Pareto incircle deficit in large random hyperbolic triangles* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-universal-half-pareto-incircle-deficit-in-large-random-hyperbo--da972935bd1e.
