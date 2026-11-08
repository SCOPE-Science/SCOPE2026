# A universal aspect-ratio reversal in rectangular boundary-chord interception

## Finding
Let \(R_{a,b}=[-a,a]\times[-b,b]\), with \(a,b>0\). Independently choose \(X,Y\) from its **entire perimeter by normalized Euclidean arclength**. For \(0<r<1\), let \(H_{a,b}(r)\) be the probability that the Euclidean segment \([X,Y]\) meets the concentric homothetic rectangle \(rR_{a,b}\). Define
\[
 p_{\mathrm{opp}}(r)=1-\frac{(1-r)^2}{1+r},\qquad
 p_{\mathrm{adj}}(r)=\frac{(1+r)^2-(1-r)^2\left[1+2\log\frac{1+r}{1-r}\right]}4,
\]
\[
w(a,b)=\frac{2ab}{(a+b)^2}\in(0,1/2].
\]
Then the **complete interception law** is
\[
\boxed{H_{a,b}(r)=\frac{1-w(a,b)}2\,p_{\mathrm{opp}}(r)+w(a,b)\,p_{\mathrm{adj}}(r).}
\]
There is exactly one universal scale \(r_\star\in(0,1)\), numerically \(r_\star=0.5604879233027861\ldots\), satisfying \(2p_{\mathrm{adj}}(r_\star)=p_{\mathrm{opp}}(r_\star)\). At this scale **every rectangle has the same interception probability**, namely
\[
H_{a,b}(r_\star)=\tfrac12 p_{\mathrm{opp}}(r_\star)=0.4381056198263137\ldots.
\]
For \(0<r<r_\star\), a square uniquely minimizes interception within rectangles having any fixed perimeter; for \(r_\star<r<1\), a square uniquely maximizes it. The reverse bound in each regime is a sharp but unattained limiting bound as \(a/b\to0\) or \(a/b\to\infty\). At \(r=r_\star\) all aspect ratios give equality. The full minimum-central-box-scale distribution also has an atom of mass \((1-w)/2\) at scale one, consisting of the chords with both endpoints on the same side.

## Assumptions and scope
The rectangle is nondegenerate, axis-aligned only for convenient coordinates; rotation and translation do not change the law. The inner target is obtained by scaling both half-side lengths by the **same** factor \(r\). Two endpoint samples are independent and perimeter-uniform. Segments, not supporting infinite lines, are tested for intersection. Replacing the closed inner rectangle by its interior changes none of the probabilities for \(0<r<1\), since tangencies have probability zero. The limiting degenerate aspect ratios are not included in the class of genuine rectangles.

## Proof
**Side weights.** Each vertical side has normalized arclength mass \(b/[2(a+b)]\), and each horizontal side has mass \(a/[2(a+b)]\). For an ordered endpoint pair, summing over all opposite-side configurations gives weight
\[
\frac{a^2+b^2}{2(a+b)^2}=\frac{1-w}2;
\]
summing over all adjacent-side configurations gives weight \(2ab/(a+b)^2=w\). Equal-side configurations do not meet the strictly smaller central rectangle except on a null set. The conditional hit probabilities of opposite and adjacent side pairs are independent of \(a,b\): affine normalization by \((x,y)\mapsto(x/a,y/b)\) preserves the uniform coordinate along any fixed side and the intersection event. (It is not asserted to preserve perimeter-uniform sampling across different sides; that is accounted for by the weights.)

**Opposite sides.** In normalized coordinates take endpoints \((-1,u)\) and \((1,v)\), where \(u,v\) are independent uniform on \([-1,1]\). The segment misses \([-r,r]^2\) precisely when its ordinates at \(x=-r\) and \(x=r\) are both above \(r\), or both below \(-r\). Put \(s=(u+v)/2\), \(t=|u-v|/2\). The domain is \(0\le t\le1\), \(|s|\le1-t\), with joint density one. The first miss event is \(s>r(1+t)\), hence has probability
\[
\int_0^{(1-r)/(1+r)}[(1-r)-(1+r)t]\,dt=\frac{(1-r)^2}{2(1+r)}.
\]
Reflection doubles the miss probability. Consequently the opposite-side hit probability is \(p_{\mathrm{opp}}(r)\).

**Adjacent sides.** By symmetry take \(X=(1,v)\) and \(Y=(u,1)\), where \(u,v\) are independent uniform on \([-1,1]\). The segment crosses the diagonal \(x=y\) at
\[
h=\frac{1-uv}{2-u-v}\ge0.
\]
As the two coordinates vary monotonically in opposite directions along this segment, it meets \([-r,r]^2\) if and only if \(h\le r\), equivalently \(u,v\le r\) and
\[
(r-u)(r-v)\ge(1-r)^2.
\]
With \(z=r-u\) and \(z'=r-v\), the favorable area in the square \([0,1+r]^2\) is the full area \((1+r)^2\) minus the region \(zz'<(1-r)^2\). For \(0<c<A^2\), this latter area in \([0,A]^2\) is exactly \(c[1+\log(A^2/c)]\), by splitting the \(z\)-integral at \(c/A\). Dividing by the original parameter-square area four gives \(p_{\mathrm{adj}}(r)\). Together with the side weights, this proves the formula.

**Unique crossover.** Define \(t=(1-r)/(1+r)\in(0,1)\) and \(G(r)=2p_{\mathrm{adj}}(r)-p_{\mathrm{opp}}(r)\). Direct substitution gives
\[
G(r)=\frac{N(t)}{(1+t)^2},\qquad N(t)=1-2t-t^2+2t^3+4t^2\log t.
\]
On \((0,1)\), \(N'''(t)=12+8/t>0\), while \(N''(0+)=-\infty\) and \(N''(1)=22\). Thus \(N''\) has one zero. Moreover \(N'(0+)=-2\), \(N'(1)=6\); therefore \(N'\) has exactly one zero, and \(N\) strictly decreases and then strictly increases. Finally \(N(0+)=1\), \(N(1)=0\), and \(N'(1)=6>0\), so \(N\) is negative just to the left of one. Hence \(N\) has exactly one zero in \((0,1)\). Its transform is \(r_\star\). Since
\[
H_{a,b}(r)=\tfrac12 p_{\mathrm{opp}}(r)+\tfrac12 w(a,b)G(r),
\]
its aspect-ratio monotonicity is the sign of \(G\). The arithmetic–geometric mean inequality gives \(0<w\le1/2\), with equality only when \(a=b\), and \(w\to0\) only under aspect-ratio degeneration. This proves all sharp optimizing statements.

## Verification
A dependency-free Python checker in `checker.py` samples independent endpoints by actual perimeter arclength on rectangles of three aspect ratios, clips their segments directly against the inner rectangles, and compares 1,650,000 generated pairs with the exact probability. It separately checks the universal crossover by bisection and the direction reversal. The completed diagnostic output was `RECTANGLE_BOUNDARY_CHORD_INTERCEPTION_OK 1650000 0.5604879233027861`.

For the square \(a=b\), \(H_{a,a}(r)=\frac14p_{\mathrm{opp}}(r)+\frac12p_{\mathrm{adj}}(r)\), with \(H_{a,a}(r)=3r/4+r^3/3+O(r^4)\) as \(r\downarrow0\). For any fixed nondegenerate rectangle, setting \(\delta=1-r\) gives
\[
H_{a,b}(1-\delta)=\frac{1+w}2-w\delta+\frac w2\delta^2\log\delta+O_{a,b}(\delta^2).
\]
The logarithmic second-order term comes from adjacent-side chords. In particular \(\lim_{r\uparrow1}H_{a,b}(r)=(1+w)/2<1\), whereas the probability at \(r=1\) would be one; this endpoint jump comes from same-side chords, which remain on the outer boundary.

## Relationship to prior work
The 2014 preprint by Balko, Jelínek, Valtr, and Walczak studies the Beer index of convexity, with two **area-uniform** points inside a region; it does not provide this **boundary-arclength** chord-interception law. Its introduction also credits Beer, Stern, and Rote for general visibility functionals and polygonal algorithms. Standard random-chord models distinguish endpoint-uniform sampling from invariant random lines; neither distinction is novel here. Existing results on random chord-length moments of parallelograms and on center-passing chords of regular polygons concern different observables. The claimed content here is the complete rectangular interception probability and its universal, aspect-ratio-independent reversal threshold.

## Limitations
No result is asserted for nonhomothetic inner targets, nonrectangular polygons, area-uniform samples, Crofton-invariant chords, or random line intersections. General geometric-integration algorithms could evaluate this four-side calculation in principle; no algorithmic breakthrough is claimed. Historical-priority verification is not exhaustive, and relevant older geometric-probability books or isolated problem solutions could contain the same formula. Numerical simulations are corroboration, not proof. The equal-perimeter restriction is used only in interpreting the aspect-ratio extremizers; the exact formula itself is valid for every \(a,b>0\).

## References
- M. Balko, V. Jelínek, P. Valtr, and B. Walczak, *On the Beer index of convexity and its variants*, arXiv:1412.1769, first posted 2014-12-04; later *Discrete & Computational Geometry* 57 (2017), 179–214, DOI: 10.1007/s00454-016-9821-3. The paper's 2014 preprint supplies the archival research context, not the present theorem.
- G. Rote, *The degree of convexity*, Abstracts of the 29th European Workshop on Computational Geometry (2013), pp. 69–72 (as cited in Balko et al.). A general polygonal interior-sampling algorithm, not an equivalent boundary-interception theorem.
- J. Bertrand, *Calcul des probabilités* (1889), classical distinction among random-chord sampling conventions (background only).
