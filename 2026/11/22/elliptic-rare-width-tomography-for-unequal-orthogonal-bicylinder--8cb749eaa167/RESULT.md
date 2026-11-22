# Elliptic rare-width tomography for unequal orthogonal bicylinders

## Finding
Fix real radii \(0<a<b\). The orthogonal bicylinder is the compact, centrally symmetric convex solid
\[
B_{a,b}=\bigl\{(x,y,z)\in\mathbb R^3:x^2+y^2\le a^2,\quad y^2+z^2\le b^2\bigr\}.
\]
Let \(U\) be uniformly distributed on \(S^2\), and let \(W(U)\) denote its Euclidean width along \(U\), equivalently the length of its projection onto the line through \(U\). Write
\[
K(k)=\int_0^{\pi/2}\frac{dt}{\sqrt{1-k^2\sin^2t}},\qquad 0\le k<1.
\]
Then the minimum width is \(2a\), attained exactly on the great circle \(U_z=0\), and as \(\varepsilon\downarrow0\),
\[
\Pr\{W\le 2a+\varepsilon\}
=\frac{K(a/b)}{\pi b}\,\varepsilon+O_{a,b}(\varepsilon^2).
\]
Moreover, with spherical coordinates \(U=(\sqrt{1-s^2}\cos\theta,\sqrt{1-s^2}\sin\theta,s)\) and
\(g(\theta)=\sqrt{b^2-a^2\sin^2\theta}\), condition on \(E_\varepsilon=\{W\le2a+\varepsilon\}\). The azimuth \(\theta\in[0,2\pi)\), the normalized deviation \(T_\varepsilon=2|s|g(\theta)/\varepsilon\), and the sign of \(s\) converge jointly to independent variables except for the explicitly stated azimuth law: \(\theta\) has density
\[
f_{a,b}(\theta)=\frac{1}{4K(a/b)\sqrt{1-(a/b)^2\sin^2\theta}},
\]
\(T\) is uniform on \([0,1]\), and the sign is symmetric on \(\{-1,1\}\). In particular, the lower endpoint of the width distribution and its finite lower-tail slope uniquely reconstruct both radii.

## Assumptions and scope
All distances are Euclidean. The smaller-radius cylinder has axis parallel to the \(z\)-axis; the larger-radius cylinder has axis parallel to the \(x\)-axis. Radii are *strictly unequal*, \(0<a<b<\infty\). The direction is uniform in spherical surface area, **not** uniform in polar latitude or conditioned on an intersection plane. Every stated conditional limit is a weak limit of probability distributions; no finite-\(\varepsilon\) independence is asserted. Constants in \(O_{a,b}\) may become unbounded as \(b\downarrow a\).

## Proof
**Step 1 (support and minimizing locus).** Since the solid is centrally symmetric, its width is \(W(u)=2h(u)\), where \(h(u)=\max_{q\in B_{a,b}}u\cdot q\). It contains the closed Euclidean radius-\(a\) ball: each of the defining pairwise-coordinate norms of a point in that ball is at most \(a\le b\). Hence \(h(u)\ge a\) for all unit \(u\). For \(u_z=0\), projection of \(B_{a,b}\) onto the \((x,y)\) plane is exactly the disk \(x^2+y^2\le a^2\), so \(h(u)=a\). Conversely if \(u_z\ne0\), the point \(au\) strictly satisfies the first defining inequality and the second defining inequality (the latter because \(b>a\)); moving a small positive distance in direction \(u\) stays feasible, so \(h(u)>a\). Consequently the minimizers are precisely \(u_z=0\). By compactness, for each fixed \(\eta>0\), the width is uniformly separated from its minimum on \(|u_z|\ge\eta\).

**Step 2 (uniform first variation).** Parameterize the uniform sphere by
\[
u=(r\cos\theta,r\sin\theta,s),\qquad r=\sqrt{1-s^2},\quad -1\le s\le1.
\]
Write \(v=(\cos\theta,\sin\theta)\). Every feasible \((x,y)\) lies in the disk \(D_a\), and the maximal feasible signed \(z\) is \(\pm G(y)\), where \(G(y)=\sqrt{b^2-y^2}\). Therefore
\[
h(u)=\max_{q=(x,y)\in D_a}\left[r\,v\cdot q+|s|G(y)\right].
\]
The point \(q_0=av\) gives the lower bound \(ra+|s|G(a\sin\theta)\). Define \(g(\theta)=G(a\sin\theta)\). On \([-a,a]\), the function \(G\) is Lipschitz with constant at most
\[
L=\frac{a}{\sqrt{b^2-a^2}}.
\]
For each \(q\in D_a\), the identity \(|q-av|^2\le2a(a-v\cdot q)\) yields
\[
\begin{aligned}
r\,v\cdot q+|s|G(y)
&\le ra-\frac{r}{2a}|q-av|^2+|s|g(\theta)+L|s||q-av|\\
&\le ra+|s|g(\theta)+\frac{aL^2s^2}{2r}.
\end{aligned}
\]
For \(|s|\le1/2\), \(r\) is bounded away from zero and \(r=1+O(s^2)\). Thus, **uniformly in \(\theta\)**,
\[
h(u)=a+|s|g(\theta)+O_{a,b}(s^2),\qquad |s|\to0.
\]
The lower angular coefficient obeys \(\sqrt{b^2-a^2}\le g(\theta)\le b\), so it is strictly positive throughout.

**Step 3 (probability and marks).** Normalized spherical surface measure is precisely \((4\pi)^{-1}\,d\theta\,ds\). The compactness statement from Step 1 and the uniform expansion in Step 2 imply that the event \(E_\varepsilon\) lies in \(|s|=O_{a,b}(\varepsilon)\). Rewriting its inequality \(h(u)-a\le\varepsilon/2\) gives for each \(\theta\), to uniformly bounded absolute error \(O_{a,b}(\varepsilon^2)\), the vertical interval
\[
|s|\le\frac{\varepsilon}{2g(\theta)}.
\]
Integrating both signs gives
\[
\Pr(E_\varepsilon)
=\frac{\varepsilon}{4\pi}\int_0^{2\pi}\frac{d\theta}{g(\theta)}+O_{a,b}(\varepsilon^2)
=\frac{\varepsilon}{\pi b}K(a/b)+O_{a,b}(\varepsilon^2).
\]
The last identity follows from the fourfold symmetry of the integrand. For any bounded continuous test function of azimuth, rescaled \(t=2|s|g(\theta)/\varepsilon\), and the sign of \(s\), change variables in the same integral. The uniform error in the boundary of the event vanishes after division by \(\Pr(E_\varepsilon)\sim c\varepsilon\). The limiting joint law is the product of the stated azimuth density, Lebesgue-uniform \(t\in[0,1]\), and the fair sign law. The density integrates to one because \(\int_0^{2\pi}g(\theta)^{-1}d\theta=4K(a/b)/b\).

**Step 4 (inverse and singular limit).** For a fixed known \(a>0\), the coefficient may be written
\[
c(a,b)=\frac1{4\pi}\int_0^{2\pi}\frac{d\theta}{\sqrt{b^2-a^2\sin^2\theta}}.
\]
Its integrand is strictly decreasing with \(b\), so \(c(a,\cdot)\) is strictly decreasing and continuous. Dominated convergence shows \(c(a,b)\to0\) for \(b\to\infty\); as \(b\downarrow a\), neighborhoods of \(\theta=\pi/2,3\pi/2\) give logarithmic divergence. More precisely the classical complete elliptic integral expansion gives
\[
c(a,b)=\frac1{\pi b}\left[\log\frac{4b}{\sqrt{b^2-a^2}}+O\!\left(\frac{b^2-a^2}{b^2}\log\frac{b}{\sqrt{b^2-a^2}}\right)\right].
\]
Since the support minimum gives \(a=\frac12\inf\operatorname{supp}(W)\), this strict monotonicity uniquely determines \(b\) from the observed lower-tail slope. Both radii are therefore recovered.

**Known limiting equal-radius case, not part of the novelty claim.** At \(b=a\), the bicylinder has the previously established identity \(W(u)=2a\sqrt{1+2|u_xu_z|}\), and its lower tail is \(\varepsilon(\pi a)^{-1}\log(a/\varepsilon)+O_a(\varepsilon)\). The change from a finite linear slope to a logarithmic singularity clarifies why strict inequality \(a<b\) is required above. This equal-radius law is supplied only for comparison with the previously derived equal-radius calculation.

## Verification
The standalone `CHECKER.py` uses only Python 3 standard-library functions. Its 121 deterministic assertions compare (i) direct one-dimensional maximization of the exact support with the first-variation formula, (ii) exact support-threshold integrations against the elliptic coefficient at multiple unequal radii and tolerances, and (iii) the established equal-radius endpoint law. Execute with `python3 CHECKER.py`. Numerical agreement is diagnostic and does **not** replace the analytic proof of the infinite-precision asymptotics or inverse uniqueness.

## Relationship to prior work
J. H. Hubbell (1965) evaluates **volume** of intersections of general circular cylinders, including unequal radii. M. P. May's publicly dated 2013 article treats unwrapped **surface geometry** of intersecting equal-radius cylinders. The Steinmetz-solid literature supplies geometric context and standard elliptic-integral notation but neither of these inspected texts gives the distribution of **directional projection widths**. Vickers and Brown (2001) study distributions of **planar projected areas and perimeters** of different solid families. The known equal-radius bicylinder width distribution is not a new claim here. The new content concerns unequal radii, a finite elliptic near-minimum slope, its conditional angular limit, and the two-number inverse reconstruction. Comparison of the statements is necessary: a general volume formula does not determine random widths, while a plane-section area profile is a different functional. See `REVIEW.md` and `AUDIT.json` for precise comparisons and residual search risks.

## Limitations
This is only a lower-endpoint result, not a full distribution formula. The estimate is not uniform as the radii coalesce; a joint \(b-a\sim\varepsilon\) crossover is not proved. Uniformity concerns the viewing direction, not random sampling on the solid's surface. The proof assumes exactly perpendicular cylinder axes and a shared center; arbitrary angles and translations are not covered. Historical priority is provisional, and an independent mathematical audit has not been performed.

## References
1. J. H. Hubbell, *Common Volume of Two Intersecting Cylinders*, Journal of Research of the National Bureau of Standards C **69C** (1965), 139–143, DOI: 10.6028/jres.069C.017, https://nvlpubs.nist.gov/nistpubs/jres/69C/jresv69Cn2p139_A1b.pdf (historical source dated at issue granularity; no exact day asserted).
2. M. P. May, *A closed-form solution for the flat-state geometry of cylindrical surface intersections bounded on all sides by orthogonal planes*, arXiv:1312.3604, first posted 2013-12-12, https://arxiv.org/abs/1312.3604.
3. G. T. Vickers and D. J. Brown, *The distribution of projected area and perimeter of convex, solid particles*, Proc. R. Soc. Lond. A **457** (2001), 283–306, DOI: 10.1098/RSPA.2000.0667.
4. E. W. Weisstein, *Cylinder-Cylinder Intersection*, MathWorld, https://mathworld.wolfram.com/Cylinder-CylinderIntersection.html (reference compendium, not an original priority claim).
