# Two sharp aspect-ratio thresholds in the perimeter of rotated-rectangle intersections

## Finding

Let \(R_a=[-a,a]\times[-1,1]\) be a centered rectangle with aspect ratio \(a\ge1\), and let \(Q_{a,\theta}\) be its counterclockwise rotation through an angle \(\theta\in[0,\pi/2]\) about the origin. Denote the ordinary Euclidean perimeter of their intersection by \(P_a(\theta)\). Put \(t=\tan(\theta/2)\). The **complete exact perimeter profile** is

\[
P_a(\theta)=
\begin{cases}
\displaystyle 4(a+1)\frac{1+t^2}{1+t},&0\le t\le1/a,\\[3pt]
\displaystyle 4\frac{1+t^2}{t},&1/a\le t\le1.
\end{cases}
\]

For \(a\ge1\), its global minimizer set over \([0,\pi/2]\) is exactly

\[
\operatorname{argmin}_{0\le\theta\le\pi/2}P_a(\theta)=
\begin{cases}
\{\pi/4\},&1\le a<\sqrt2,\\
\{\pi/4,\pi/2\},&a=\sqrt2,\\
\{\pi/2\},&a>\sqrt2.
\end{cases}
\]

The minimum perimeter is \(\min\{8(\sqrt2-1)(a+1),8\}\). A distinct **local-extremum threshold** occurs at \(a=1+\sqrt2\). If \(1<a<1+\sqrt2\), the profile has a strict local maximum at \(\theta_a=2\arctan(1/a)\), with value \(4(a+a^{-1})\), and a strict local minimum at \(\theta=\pi/4\). For \(a=1\), the latter is still the unique interior strict local minimum, but the local maximum has moved to the endpoint \(\pi/2\). If \(a\ge1+\sqrt2\), the profile is strictly decreasing throughout the interval (a one-sided derivative vanishes at \(\theta=\pi/4\) when equality holds).

Thus the global optimum jumps discontinuously from the diagonal angle to the perpendicular angle when the aspect ratio crosses \(\sqrt2\), even though the diagonal remains locally optimal until the second threshold \(1+\sqrt2\).

## Assumptions and scope

Both rectangles are closed, have identical side lengths \(2a\) and \(2\), share their center, and only the relative rotation varies. The perimeter is the arclength of the convex intersection polygon, including its contact-boundary cases. Reflection and quarter-turn symmetries reduce relative angles to \([0,\pi/2]\). No assertion is made for freely translated rectangles, independent aspect ratios, or general centrally symmetric bodies. Scaling all side lengths by \(b>0\) multiplies every perimeter by \(b\) but leaves optimal angles and thresholds unchanged.

## Proof

Write \(c=\cos\theta\), \(s=\sin\theta\), \(t=\tan(\theta/2)=(1-c)/s\), first for \(0<\theta<\pi/2\). The rotated rectangle is specified by

\[
|cx+sy|\le a,\qquad |-sx+cy|\le1.
\]

The intersection is convex and, away from endpoint coincidences, every edge is a retained portion of exactly one rectangle boundary. Reflection across the angular bisector \(\theta/2\) interchanges the rectangles, so they contribute equal total lengths. Central inversion shows the retained boundary length of the unrotated rectangle is twice the sum \(H+V\), where \(H\) is the retained segment length on the top side \(y=1\), and \(V\) is the corresponding length on the right side \(x=a\). Consequently \(P_a(\theta)=4(H+V)\).

On the top edge, all three coordinate constraints give

\[
H=\operatorname{length}\left([-a,a]\cap
\left[\frac{-a-s}{c},\frac{a-s}{c}\right]
\cap\left[\frac{c-1}{s},\frac{c+1}{s}\right]\right).
\]

Since \(a\ge1\), the largest lower endpoint is \((c-1)/s=-t\). The smallest upper endpoint is \((a-s)/c\) if \(a\le1/t\), and \(1/t\) if \(a\ge1/t\). Hence

\[
H=\begin{cases}t+(a-s)/c,&a\le1/t,\\t+1/t,&a\ge1/t.\end{cases}
\]

Likewise, the right edge yields

\[
V=\operatorname{length}\left([-1,1]\cap
\left[\frac{-a(1+c)}{s},\frac{a(1-c)}{s}\right]
\cap\left[\frac{as-1}{c},\frac{as+1}{c}\right]\right).
\]

The largest lower endpoint is \((as-1)/c\); the smallest upper endpoint is \(at\) or \(1\), respectively. Therefore

\[
V=\begin{cases}(1-at)/c,&a\le1/t,\\0,&a\ge1/t.\end{cases}
\]

In the first regime, use \(s=2t/(1+t^2)\) and \(c=(1-t^2)/(1+t^2)\) to simplify \(H+V=(a+1)(1+t^2)/(1+t)\). In the second regime, \(H+V=t+t^{-1}=(1+t^2)/t\). This proves the stated two-branch formula on the open angular interval. The branches agree at \(t=1/a\), both equaling \(4(a+a^{-1})\). At \(\theta=0\), the rectangles coincide and their perimeter is \(4(a+1)\); at \(\theta=\pi/2\), their intersection is a square of half-side \(1\) and perimeter \(8\). These values agree with the continuous extensions. Any double-counting of coincident boundary edges at the endpoints is therefore avoided.

For \(t\in[0,1/a]\), the derivative of the dimensionless first-branch factor is

\[
\frac{d}{dt}\frac{1+t^2}{1+t}
=\frac{t^2+2t-1}{(1+t)^2},
\]

which changes sign uniquely at \(t_*=\sqrt2-1\), corresponding to \(\theta_*=\pi/4\). In the second regime, \(P_a(\theta)=8/\sin\theta\) strictly decreases until \(\pi/2\). The first branch includes \(t_*\) precisely if \(a\le1+\sqrt2\); when \(1<a<1+\sqrt2\), its increasing terminal segment joins the decreasing second branch at a strict local maximum \(t=1/a\). At \(a=1+\sqrt2\) the two critical locations merge; at larger aspect ratios both branches decrease, establishing the second threshold.

When the diagonal local minimum exists, its value is

\[
P_a(\pi/4)=8(\sqrt2-1)(a+1),
\]

whereas the perpendicular endpoint always has value \(8\). All other angles have strictly larger perimeter than the smaller of these two candidates. Their equality occurs exactly when \(a=\sqrt2\), which yields the first threshold and the complete set of equality cases. For \(a>1+\sqrt2\), only the perpendicular candidate survives, consistently completing the classification. \(\square\)

## Verification

A standalone Python checker, `scripts/check_rectangles.py`, evaluates the piecewise expression and independently computes intersection-polygon perimeters by sequential clipping against the four rotated half-planes. Using only the Python standard library, it passes 21,344 comparisons and global-lower-bound assertions across exact threshold values, endpoint orientations, random aspect ratios, and random angles. These numerical tests check the formulas but do not replace the proof above. Reproduce with `python3 scripts/check_rectangles.py` after extracting the script from the package.

## Relationship to prior work

General work on intersections of rotations of centrally symmetric convex bodies, such as Brazitikos and Stavrakakis (2014), addresses volume and radius bounds in higher dimensions. The publicly accessible abstract does not establish this perimeter minimization result; its complete text could not be inspected, so no stronger exclusion is asserted. Classical equal-rectangle intersection problems, including Prasolov's 1986 area inequality as reproduced by Bogomolny, concern area rather than the orientation-dependent boundary length. The 2012 polygon-clipping discussion computes overlaps for rotated rectangles, but does not prove sharp global perimeter minimizers. A 2013 discussion of optimizing two rectangles' overlap again treats area and different placement freedoms. The present sharp perimeter classification and its two aspect thresholds were not identified in the searches detailed in the review; negative searches do not establish absolute priority.

## Limitations

The rectangles must be congruent and concentric, and only Euclidean perimeter is optimized. The classification does not apply unchanged under translations, unequal side lengths, weighted perimeters, or other polygons. This is a complete exact formula in the stated family, not a claim of a universal convex-body optimization theorem. The accessible literature inspection cannot exclude all historical appearances, and no independent audit has been performed.

## References

1. S. Brazitikos and P. Stavrakakis, *On the intersection of random rotations of a symmetric convex body*, Mathematical Proceedings of the Cambridge Philosophical Society **157** (2014), 13–30. DOI: https://doi.org/10.1017/S0305004114000115 (first published online March 28, 2014; abstract inspected, full text unavailable).
2. *Area of Intersection of Two Rotated Rectangles*, Stack Overflow, July 26, 2012. https://stackoverflow.com/questions/11670028/area-of-intersection-of-two-rotated-rectangles (full discussion inspected; generic clipping, not the optimized perimeter claim).
3. *Maximize area of intersection between two rectangles*, Mathematics Stack Exchange, March 17–18, 2013. https://math.stackexchange.com/questions/332737/maximize-area-of-intersection-between-two-rectangles (full discussion inspected).
4. V. V. Prasolov, *Problems in Geometry*, Vol. 2, 1986, Problem 15.47; reproduced and discussed in A. Bogomolny, *Area of the Intersection of Two Equal Rectangles*. https://www.cut-the-knot.org/m/Geometry/TwoEqualRectangles.shtml (reproduction inspected; original book not inspected).
