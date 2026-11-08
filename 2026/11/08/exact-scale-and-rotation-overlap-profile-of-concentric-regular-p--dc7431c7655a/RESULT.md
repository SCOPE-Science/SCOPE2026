# Exact scale-and-rotation overlap profile of concentric regular polygons

## Finding
For every integer \(n\ge3\), let \(P_a\) be the closed regular Euclidean \(n\)-gon centered at the origin with apothem \(a>0\), and let \(R_\phi P_b\) be another such polygon, rotated through angle \(\phi\), with \(0<b\le a\). Write
\[
 c=\frac{\pi}{n},\qquad C=\cos c,\qquad q=\frac ba,\qquad I(\phi)=\operatorname{area}(P_a\cap R_\phi P_b).
\]
By dihedral symmetry it suffices to take \(0\le\phi\le c\). Put \(x=\cos(c-\phi)\). The **complete overlap-area profile**, valid without general-position assumptions, is
\[
 \boxed{I(\phi)=\begin{cases}
 n b^2\tan c,&qx\le C,\\[2mm]
 n b^2\tan c-n a^2\tan c\,\dfrac{(qx-C)^2}{x^2-C^2},&qx>C.
 \end{cases}}
\]
The first branch includes \(\phi=0\), where the second fraction could be singular; continuity fixes all equality cases. For \(q\le C\), the smaller polygon is contained in the larger **at every rotation**. For \(C<q<1\), the complete-containment plateau is exactly
\[
 0\le\phi\le\phi_*:=c-\arccos(C/q),
\]
and the overlap decreases strictly as \(\phi\) moves from \(\phi_*\) to \(c\). For \(q=1\), the maximum occurs only at the aligned phase \(\phi=0\); in all cases \(q>C\), the minimum occurs only at half-side-step rotation \(\phi=c\), up to the polygon's dihedral symmetries. In particular,
\[
 \boxed{I_{\max}=nb^2\tan c,\quad
 I_{\min}=nb^2\tan c-\frac{n(b-a\cos c)_+^2}{\cos c\sin c}.}
\]
Here \(y_+=\max\{y,0\}\).

The **order of contact of the loss** changes at equal scale. If \(C<q<1\), then as \(h\downarrow0\),
\[
 I(\phi_*)-I(\phi_*+h)=
 n a^2\tan c\frac{q^2(q^2-C^2)}{C^2(1-q^2)}h^2+O_{n,a,q}(h^3).
\]
When \(q=1\), instead,
\[
 I(0)-I(h)=\frac12na^2\tan^2c\,h+O_{n,a}(h^2).
\]
Consequently, the area profile at equal scale has a nonzero one-sided angular slope, while at every strictly unequal scale it has a quadratic onset after a nontrivial plateau.

There is also a **radial-measure strengthening**. Let \(w:[0,\infty)\to[0,\infty)\) be measurable, with integrable radial mass over the bounded polygons, and put
\[
 I_w(\phi)=\int_{P_a\cap R_\phi P_b}w(\lVert z\rVert)\,dz.
\]
Then \(I_w\) is nonincreasing on \([0,c]\) for every such \(w\). If \(q>C\) and \(w>0\) almost everywhere on \((a,b/C)\), the decrease is strict for any \(\phi_*\le\phi_1<\phi_2\le c\). No assertion of strictness is made for weights supported in the common inscribed disk.

## Assumptions and scope
The polygons are closed, nondegenerate, regular, share their circumcenter, have the **same** side number \(n\), and have possibly different scales. An apothem is the distance from the common center to each supporting side. Rotation is about the common center; there is no translation. The angular period is \(2\pi/n=2c\), and reflection identifies \(\phi\) with \(2c-\phi\). The formula is for planar Euclidean area, not perimeter, a translation overlap, or overlap of regular polygons with different side numbers. The radial weight may vanish on sets of positive measure; only the separately stated positivity condition implies strictness.

## Proof
**1. Polygonal halfspaces and unique exposed vertices.** Orient the supporting outer normals of \(P_a\) at angles \(2kc\), and of \(R_\phi P_b\) at \(\phi+2kc\). The vertices of the latter polygon occur at angles \(\phi+(2k+1)c\) with radius \(b/C\). Fix an outer supporting normal, say at angle \(2c\). Its nearest small-polygon vertex has angular separation \(c-\phi\) and outward projection \(bx/C\). Every other small-polygon vertex has separation at least \(c+\phi\) from this normal, and projection at most \(b\cos(c+\phi)/C\le b\le a\). Hence this outer supporting line either does not cut the small polygon, or cuts off exactly one vertex. Such cutting occurs precisely when \(qx>C\). These vertices are distinct for the \(n\) outer supporting lines.

Each edge midpoint of the smaller polygon lies at radius \(b\le a\), within the incircle of \(P_a\). Therefore the pieces cut from distinct vertices lie on disjoint half-edges; the removed triangles have pairwise disjoint interiors. This holds for \(n=3\) and at all nondegenerate angles, and extends by continuity to \(\phi=0,c\) and tangencies.

**2. Exact clipping area.** For \(0<\phi<c\) and \(qx>C\), the overshoot of the exposed small vertex beyond the outer supporting line is
\[
 \delta=\frac{a(qx-C)}{C}>0.
\]
The inward projections onto the outer normal of the two incident small-polygon edges are \(-\sin\phi\) and \(-\sin(2c-\phi)\) per unit edge length, respectively. The cut-off triangle therefore has adjacent edge lengths \(\delta/\sin\phi\) and \(\delta/\sin(2c-\phi)\) and included angle \(\pi-2c\). Its area is
\[
 T=\frac{\delta^2\sin(2c)}{2\sin\phi\sin(2c-\phi)}
 =a^2\tan c\frac{(qx-C)^2}{x^2-C^2},
\]
using \(\sin\phi\sin(2c-\phi)=\cos^2(c-\phi)-\cos^2c=x^2-C^2\). The small polygon has area \(nb^2\tan c\). Subtracting the \(n\) disjoint equal triangles proves both branches of the exact profile.

**3. Sharp extrema and containment.** The function \(x(\phi)=\cos(c-\phi)\) strictly increases on \((0,c)\). For \(qx>C\),
\[
 \frac{d}{dx}\frac{(qx-C)^2}{x^2-C^2}
 =\frac{2C(qx-C)(x-qC)}{(x^2-C^2)^2}>0.
\]
For \(q\le C\), the inequality \(qx\le C\) holds at every phase. For \(C<q\le1\), the condition \(qx>C\) is exactly \(\phi>c-\arccos(C/q)\), and Step 3 gives strict decrease beyond that threshold. Evaluating at \(x=1\) proves the minimum formula; the maximum is the entire area of the smaller polygon, with the equality sets just described.

**4. Exact onset orders.** If \(C<q<1\), write \(x_0=C/q\). At the threshold, \(x'(\phi_*)=\sqrt{q^2-C^2}/q\) and \(x_0^2-C^2=C^2(1-q^2)/q^2>0\). Taylor expansion of the exact loss gives the quadratic coefficient above. If \(q=1\), the numerator and denominator vanish together at \(x=C\); cancel one factor to obtain \((x-C)/(x+C)\), and use \(x-C=\sin c\,\phi+O(\phi^2)\). This gives the stated nonzero linear coefficient.

**5. Universal radial order.** At radius \(r\in(a,b/C)\), both polygons meet the concentric circle in \(n\) congruent arcs centered on their respective vertex directions. On the fundamental angular circle of circumference \(2c\), the arc half-width for apothem \(d\) is \(\eta_d(r)=c-\arccos(d/r)\in(0,c)\). Two centered circular arcs of fixed lengths have nonincreasing intersection length as their center separation moves from \(0\) to half the circle's circumference. (Cut the circle at the centers and compare the two linear-overlap contributions; their slopes are \(0\) or \(-1\) until a possible terminal plateau.) Thus the angular measure of the intersection on each radius is nonincreasing in \(\phi\); all other radii contribute phase-independent mass or zero. Tonelli's theorem proves the inequality for arbitrary nonnegative integrable radial \(w\). For \(q>C\), the small polygon has vertex radius \(b/C>a\). If \(\phi_*\le\phi_1<\phi_2\le c\), Step 3 proves that the ordinary intersection-area difference is strictly positive. Since every phase-dependent angular contribution is confined to the annulus \(a<r<b/C\) and its pointwise difference is nonnegative by the preceding arc argument, there is a positive-measure set of radii in that annulus where the difference is strictly positive. Positivity of \(w\) almost everywhere there therefore makes the weighted inequality strict.

## Verification
A dependency-free checker (`verify.py`) uses Sutherland--Hodgman halfplane clipping of the literal rotated polygon vertices and the independent shoelace area formula. Its default deterministic test uses a seeded suite with \(7{,}200\) configurations covering \(3\le n\le50\), \(0<b/a\le1\), and the full reduced rotation interval. The maximum normalized area deviation observed was below \(7\times10^{-16}\). It additionally checks the exact minimum, the containment plateau, and the two distinct onset orders by finite differences. Numerical agreement is diagnostic only; Steps 1--5 establish the universal claim.

## Relationship to prior work
Mathar's *Tightly Circumscribed Regular Polygons* (arXiv:1301.6293v1, 2013), especially Section III, gives support-contact equations for concentric regular polygons with rotations, primarily for containment and possibly differing side numbers. Its support-contact calculus already entails the containment threshold, so that elementary fact alone is **not** claimed as new. Kiss and Vidnyánszky (arXiv:1402.5452v1, 2014) study unions of **congruent** regular polygons and their perimeter-to-area ratios. Har-Peled and Roy (arXiv:1406.5778v1, 2014) study general polygon-overlap approximation under **translation**. O'Rourke and Zaimi (MathOverflow, 2015-10-17) count sides of intersections of origin-centered equal-circumradius regular polygons. An existing exact radial-coverage theorem for unions of arbitrarily many **congruent** concentric regular polygons gives strong prior coverage of the equal-scale endpoint of the present setting; it neither assumes unequal scales nor states the two-scale overlap area, plateau onset, and transition from quadratic to linear clipping loss.

The claim here is the full exact area and strict angular spectrum at **every unequal scale** together with its quantitatively different contact-order transition and radial-weight order. General polygon clipping methods can compute individual numerical instances but do not by themselves state this parameter-uniform closed phase classification.

## Limitations
The proof concerns only regular polygons with the same number of sides and common center, not arbitrary convex shapes, different polygon orders, translations, or higher dimensions. At \(q\le\cos(\pi/n)\), the overlap is phase-independent; no strict minimizer exists. Results about the equal-scale case, generic polygon clipping, containment, and radial arc rearrangement are not claimed as new. Mathematical priority is relative to the specifically examined sources, not established against every historical publication. An independent audit has not been performed.

## References
1. Richard J. Mathar, *Tightly Circumscribed Regular Polygons*, arXiv:1301.6293v1 (first public 2013-01-26), particularly §§I--III, https://arxiv.org/html/1301.6293v1 .
2. Viktor Kiss and Zoltán Vidnyánszky, *Unions of regular polygons with large perimeter-to-area ratio*, arXiv:1402.5452v1 (first public 2014-02-21), https://arxiv.org/html/1402.5452v2 .
3. Sariel Har-Peled and Subhro Roy, *Approximating the Maximum Overlap of Polygons under Translation*, arXiv:1406.5778v1 (first public 2014-06-22), https://arxiv.org/html/1406.5778v1 .
4. Joseph O'Rourke and Gjergji Zaimi, *Intersection of rotating regular polygons*, MathOverflow discussion, 2015-10-17, https://mathoverflow.net/questions/221120/intersection-of-rotating-regular-polygons .
5. *Universal radial coverage by concentric regular-polygon unions*, published research record, published published-finding corpus research record 4705952c9b28 (2026-10-11). .
