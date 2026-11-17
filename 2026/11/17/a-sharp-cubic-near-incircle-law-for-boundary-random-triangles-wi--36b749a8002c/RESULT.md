# A sharp cubic near-incircle law for boundary-random triangles, with equilateral rigidity

## Finding
Let \(T\) be any fixed nondegenerate Euclidean triangle, with side lengths \(a,b,c\), perimeter \(P=a+b+c\), semiperimeter \(s=P/2\), and inradius \(r>0\). Choose three points independently and uniformly in arclength on \(\partial T\), and let \(R\) be the inradius of their convex hull (zero for a degenerate triangle). Then, as \(\varepsilon\downarrow0\),
\[
 \Pr(R>r-\varepsilon)=K_T\varepsilon^3+o(\varepsilon^3),\qquad
 K_T=\frac{(abc)^3}{P^3r^3(s-a)^2(s-b)^2(s-c)^2}.
\]
For the relative deficit \(\delta=\varepsilon/r\), this is
\[
 \Pr(R>r(1-\delta))=G_T\delta^3+o(\delta^3),\quad
 G_T=\frac{(abc)^3}{P^3(s-a)^2(s-b)^2(s-c)^2}\ge\frac{64}{27}.
\]
Equality in the sharp shape bound occurs if and only if \(T\) is equilateral. All assertions hold for obtuse and right as well as acute parent triangles, pointwise in the fixed triangle.

There is also a marked limiting law. On the rare event, with probability tending to one, the sampled points lie near the three distinct original vertices, one near each. At each vertex \(i\), record which of its two incident sides contains its sampled point, and let \(t_i\) be its distance from that vertex. For a route choice \(\eta=(\eta_A,\eta_B,\eta_C)\), define the positive first-order loss coefficient \(\lambda_{i,\eta_i}\) in the proof below. Conditional on \(R>r-\varepsilon\), the route choices converge to three **independent** side choices, with probabilities proportional to the reciprocals of the two associated \(\lambda\)'s. Independently of the limiting route, the three-vector
\[
 \left(\frac{\lambda_{A,\eta_A}t_A}{\varepsilon},
 \frac{\lambda_{B,\eta_B}t_B}{\varepsilon},
 \frac{\lambda_{C,\eta_C}t_C}{\varepsilon}\right)
\]
converges **in total variation** to the uniform probability law on \(\{(u,v,w):u,v,w\ge0,\ u+v+w\le1\}\), or equivalently the first three coordinates of a \(\operatorname{Dirichlet}(1,1,1,1)\) vector.

## Assumptions and scope
The parent triangle is fixed, nondegenerate, Euclidean, and has no restriction on its angles. Its three random points are independent, each with probability measure \(ds/P\) on the entire polygonal boundary. The inradius of the sampled triangle is its area doubled divided by its perimeter, including the continuous value zero at degeneracy. All conditional results concern the event \(\{R>r-\varepsilon\}\), and \(\varepsilon\) tends to zero with the original triangle held fixed. No claim of uniformity in degenerating families of parent triangles is made.

## Proof
**1. Unique maximizing configuration.** Write \(T'\) for the convex hull of any three boundary points. Since \(T'\subseteq T\), its inradius is at most \(r\). The incircle of \(T\) is the unique disk of radius \(r\) contained in \(T\): a center at distance at least \(r\) from all three host side lines lies in the intersection of their three inward offsets, which consists of the incenter alone. If \(T'\) had inradius \(r\), it would therefore contain the original incircle. Each of the incircle's three original side-tangency points belongs to \(T'\), and also to \(\partial T'\) because it lies on \(\partial T\). At a smooth boundary point of the incircle, any supporting line of \(T'\) through that point must be the unique tangent to the incircle. Hence a tangency point cannot be a genuine vertex of \(T'\); it lies on one of its edges along the corresponding host side. Thus each of the three different sides of \(T'\) is a host side, so \(T'=T\). Compactness of \((\partial T)^3\) and continuity of the inradius imply that all sufficiently near-maximal configurations have one point close to each distinct host vertex.

**2. The six one-sided first derivatives.** At vertex \(A\), write \(b=|CA|\), \(c=|AB|\) and \(a=|BC|\). Move \(A\) distance \(t\) toward \(B\) along \(AB\), keeping \(B,C\) fixed. Then the twice-area is multiplied by \(1-t/c\), while the perimeter is
\[
 P_t=P-t(1+\cos A)+O(t^2).
\]
Consequently, by the cosine law and \(P=2s\),
\[
 r-r_t=r\left(\frac1c-\frac{1+\cos A}{P}\right)t+O(t^2)
 =\frac{r(s-c)}{bc}\,t+O(t^2).
\]
Motion toward \(C\) gives the analogous coefficient \(r(s-b)/(bc)\). Define \(\lambda_{A,AB}=r(s-c)/(bc)\) and \(\lambda_{A,AC}=r(s-b)/(bc)\); the other four rates are their cyclic relabellings. They are all strictly positive. For each of eight side-choice patterns, the smooth inradius function therefore satisfies, uniformly in its local nonnegative coordinates,
\[
 r-R=\lambda_{A,\eta_A}t_A+
 \lambda_{B,\eta_B}t_B+
 \lambda_{C,\eta_C}t_C+O((t_A+t_B+t_C)^2).
\]

**3. Exact leading measure.** In one fixed side-choice chart, the three chosen boundary points have product arclength density \(P^{-3}\). There are \(3!=6\) ways to assign the three independent sample labels to the three host vertices. Rescale \(u_i=\lambda_{i,\eta_i}t_i/\varepsilon\). Because every loss rate is positive, the near-maximal event is trapped between two shrinking simplex neighborhoods; its rescaled indicator converges almost everywhere to that of \(u_A+u_B+u_C<1\). A uniform fixed compact enclosure follows from the positive linear lower bound on the loss for sufficiently small \(t_i\). Dominated convergence yields a local volume
\[
 \frac{6}{P^3}\frac{\varepsilon^3}{\lambda_{A,\eta_A}\lambda_{B,\eta_B}\lambda_{C,\eta_C}}\cdot\frac1{3!}
 =\frac{\varepsilon^3}{P^3\prod_i\lambda_{i,\eta_i}}.
\]
Summing the eight disjoint charts gives \(K_T=P^{-3}\prod_i\bigl(\sum_{\eta_i}\lambda_{i,\eta_i}^{-1}\bigr)\). The explicit rates imply
\[
 \lambda_{A,AB}^{-1}+\lambda_{A,AC}^{-1}
 =\frac{abc}{r(s-b)(s-c)};
\]
combining its cyclic versions proves the asserted \(K_T\). The same dominated-convergence argument applies in \(L^1\) to the rescaled conditional probability densities, proving total-variation convergence to the uniform simplex density \(6\); route weights factor into independent one-vertex factors. For example the limiting chance that vertex \(A\)'s chosen point lies on \(AB\) is \((s-b)/a\), and that it lies on \(AC\) is \((s-c)/a\).

**4. Sharp equilateral coefficient.** Put \(x=s-a\), \(y=s-b\), \(z=s-c\), which are positive and satisfy \(s=x+y+z\). Let \(u=x/s\), \(v=y/s\), \(w=z/s\), so \(u+v+w=1\). Write \(p=uv+uw+vw\) and \(q=uvw\). Since \((u+v)(v+w)(w+u)=p-q\),
\[
 G_T=\frac{(p-q)^3}{8q^2}.
\]
Maclaurin's inequality yields \(p\ge3q^{2/3}\), while AM–GM gives \(q^{1/3}\le1/3\). Therefore \(p-q\ge(8/3)q^{2/3}\), so \(G_T\ge64/27\). Equality in the inequalities forces \(u=v=w=1/3\), equivalently \(a=b=c\), and this shape attains equality.

## Verification
The companion `check_inradius.py` computes independent Cartesian area/perimeter inradii, finite-difference derivatives for every corner/side route, the closed-form coefficient by two algebraic forms, and an importance-sampled rare-event probability for equilateral, scalene and right parent triangles. The three observed ratios of finite-threshold probability to leading prediction at relative deficit \(0.018\) were approximately \(0.986\), \(0.969\) and \(0.954\); all diagnostics passed. Sampling tests are not substitutes for the compactness, differentiation, integration and inequality proof above. Run `python check_inradius.py` with Python 3 and NumPy.

## Relationship to prior work
The use of exact triangle-area and incircle identities is classical. The 2013 report of Tong, Ahmadi and Pan analyzes the random distance between two area-uniform points in a host triangle rather than the inradius of a boundary-sampled triple. The 2015 triangle-shape paper of Edelman and Strang treats normal-vertex/angle sampling and shape-space distributions rather than the present fixed-host boundary measure; its full accessible preprint was checked. A published random-cyclic-triangle inradius law uses a circular boundary rather than a triangular one. Published host-triangle boundary-sampling results on hull area, area deficits and centroid capture concern observables distinct from the new inradius tail. A general local-linearization technique by itself does not supply the stated shape coefficient, its sharp all-triangle optimizer or the conditional independent side-choice law.

## Limitations
Historical priority remains provisional, particularly against unindexed geometry/probability literature and abstract local-cone tail frameworks. The theorem is pointwise for a fixed host and describes only the upper endpoint, not the full inradius distribution. The convergence is self-reviewed, not independently audited, and the stochastic numerical diagnostics give corroboration rather than proof. No conclusion is claimed for nonuniform boundary sampling, higher polygons or collapsing triangles under simultaneous scaling.

## References
- Fei Tong, Maryam Ahmadi and Jianping Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498 (first posted 2013-11-29). https://arxiv.org/abs/1312.2498
- Alan Edelman and Gilbert Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053 (first posted 2015-01-09). https://arxiv.org/abs/1501.03053
- *The full inradius law and two contrasting tails of random cyclic triangles* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-full-inradius-law-and-two-contrasting-tails-of-random-cyclic--f4fa44ae752a
- *Exact finite-sample area and sharp shape order for boundary-random triangles* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-finite-sample-area-and-sharp-shape-order-for-boundary-rand--69daac1de0bc
- *A sharp stochastic envelope and two-moment shape inversion for maximal triangles sampled on triangular boundaries* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-stochastic-envelope-and-two-moment-shape-inversion-for-m--7f674d2377d7
