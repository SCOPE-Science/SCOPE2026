# Joint inradius–circumradius law and sharp co-saturation for random circular-cylinder shadows

## Finding

Let \(K=\{(x,y,z)\in\mathbb R^3:x^2+y^2\le R^2,\ |z|\le H/2\}\), where \(R,H>0\). Orthogonally project \(K\) onto an unoriented uniformly random two-dimensional plane. Define \(I\) to be the radius of the largest Euclidean disk contained in the projected convex body and \(O\) the radius of its smallest enclosing Euclidean disk. Put \(q=H/(2R)\). With a Haar-uniform unit plane normal \(U\), \(C=|U_3|\sim\operatorname{Uniform}[0,1]\) and \(S=\sqrt{1-C^2}\), the **complete joint law** is

\[
\boxed{\frac IR=\min\{1,C+qS\},\qquad \frac OR=\begin{cases}C+qS,&C>1/\sqrt{1+q^2},\\\sqrt{1+q^2},&C\le1/\sqrt{1+q^2}.\end{cases}}
\tag{1}
\]

When \(0<q<1\), its support is a horizontal segment \(I=R\), a vertical segment \(O=R\sqrt{1+q^2}\), and a positive atom at their common corner. When \(q\ge1\), the inradius is identically \(R\), leaving only the horizontal segment and its terminal atom.

Write \(o_*=R\sqrt{1+q^2}\). The three exact atom weights are

\[
\boxed{\begin{aligned}
\Pr(O=o_*)&=\frac1{\sqrt{1+q^2}},\\
\Pr(I=R)&=\begin{cases}\frac{2q^2}{1+q^2},&0<q<1,\\1,&q\ge1,\end{cases}\\
\Pr(I=R,O=o_*)&=p(q):=\begin{cases}\frac1{\sqrt{1+q^2}}-\frac{1-q^2}{1+q^2},&0<q<1,\\\frac1{\sqrt{1+q^2}},&q\ge1.
\end{cases}
\end{aligned}}
\tag{2}
\]

**Sharp co-saturation optimum:** \(p(q)\le1/\sqrt2\), with equality **if and only if** \(q=1\), equivalently \(H=2R\). There is a cusp at the optimal aspect ratio: the left and right derivatives of \(p\) at \(q=1\) are respectively \((4-\sqrt2)/4\) and \(-1/(2\sqrt2)\).

Both marginal laws are also elementary. For \(0<q<1\) and \(q\le t<1\),
\[
\Pr(I/R\le t)=\frac{t-q\sqrt{1+q^2-t^2}}{1+q^2}.
\tag{3}
\]
Below \(q\) this CDF vanishes and at \(1\) it jumps to \(1\). If \(q\ge1\), \(I=R\) surely. For every \(q>0\) and \(1\le t<\sqrt{1+q^2}\),
\[
\Pr(O/R\le t)=1-\frac{t+q\sqrt{1+q^2-t^2}}{1+q^2}.
\tag{4}
\]
Below \(1\) this CDF vanishes and at \(\sqrt{1+q^2}\) it jumps to \(1\). Knowing the endpoint \(o_*\) and its atom weight \(p_O\) uniquely recovers the similarity scale and aspect ratio:
\[
q=\sqrt{p_O^{-2}-1},\qquad R=o_*p_O,\qquad H=2Rq.
\tag{5}
\]

## Assumptions and scope

The cylinder is filled, closed, finite, circular, right, and centrally symmetric; all projections are orthogonal, not perspective. Its two circular caps are included. The viewing plane is Haar-uniform, equivalently its normal is Haar-uniform on the sphere modulo sign. The inradius and circumradius permit arbitrary center locations, although symmetry proves that centered disks realize both extrema. Formula (2) concerns exact population events, not finite-precision experimental coincidences. There is no claim for oblique cylinders, biased orientations, planar sections, or non-circular bases. The limiting cases \(H=0\) and \(R=0\) are excluded.

## Proof

**1. Geometry of the projected body.** Put \(\theta=\arccos C\in[0,\pi/2]\), \(S=\sin\theta\), so the projected base disk is an ellipse of semiaxes \(R\) and \(RC\), and the projected axial segment has length \(HS\) along that ellipse's minor direction. The shadow is their Minkowski sum. Its planar support function, in a unit direction whose absolute minor-axis component is \(t\in[0,1]\), is exactly
\[
h(t)=R\bigl(\sqrt{1-S^2t^2}+qSt\bigr).\tag{6}
\]
For a centrally symmetric compact convex body, a largest inscribed disk and a smallest enclosing disk can each be centered at its center of symmetry: reflecting a feasible disk center and then averaging the two centers preserves feasibility by convexity (for containment use the triangle inequality). Therefore \(I=\min_{0\le t\le1}h(t)\) and \(O=\max_{0\le t\le1}h(t)\).

**2. Support extrema.** The function (6) is concave in \(t\). Its minimum is at an endpoint: \(h(0)=R\) and \(h(1)=R(C+qS)\), proving the first formula in (1). The interior maximum satisfies \(St/\sqrt{1-S^2t^2}=q\); the stationary point is \(t=q/[S\sqrt{1+q^2}]\), admissible exactly when \(S\ge q/\sqrt{1+q^2}\), or \(\theta\ge\arctan q\). Its support value is \(R\sqrt{1+q^2}\). Otherwise the maximum is at \(t=1\), of value \(R(C+qS)\). This proves the second formula in (1). The endpoint directions follow by continuity.

**3. Geometry of the joint distribution.** The function \(g(\theta)=\cos\theta+q\sin\theta\) has a unique maximum \(\sqrt{1+q^2}\) at \(\theta=\arctan q\). Also
\[
g(\theta)-1=2\sin(\theta/2)\bigl(q\cos(\theta/2)-\sin(\theta/2)\bigr),
\]
so \(g(\theta)\ge1\) iff \(\theta\le2\arctan q\), with the inequality holding for every \(\theta\in[0,\pi/2]\) when \(q\ge1\). Consequently, for \(0<q<1\), the interval \(0\le\theta<\arctan q\) contributes the horizontal segment, \(\arctan q\le\theta\le2\arctan q\) contributes the corner atom, and \(2\arctan q<\theta\le\pi/2\) contributes the vertical segment. For \(q\ge1\), there is no vertical segment. The relative interior of each nondegenerate segment has a continuous pushforward law. Since \(C=\cos\theta\) is uniform on \([0,1]\), the measures of these disjoint regions give precisely (2): \(\Pr(\theta\ge\arctan q)=\cos(\arctan q)=(1+q^2)^{-1/2}\) and, for \(q<1\), \(\Pr(\theta\le2\arctan q)=1-\cos(2\arctan q)=2q^2/(1+q^2)\). Their intersection has the corner mass stated.

**4. Marginal CDFs.** For \(0<q<1\), on the strictly falling branch \(2\arctan q<\theta\le\pi/2\), write \(t=g(\theta)\) and solve \(t=C+q\sqrt{1-C^2}\). The relevant smaller root is
\[
C_-(t)=\frac{t-q\sqrt{1+q^2-t^2}}{1+q^2},\quad q\le t<1.
\]
The event \(I/R\le t\) occurs precisely when \(C\le C_-(t)\), giving (3). The other marginal is below its terminal atom exactly on \(0\le\theta<\arctan q\), where the larger root of the same equation is
\[
C_+(t)=\frac{t+q\sqrt{1+q^2-t^2}}{1+q^2},\quad 1\le t<\sqrt{1+q^2}.
\]
The event \(O/R\le t\) is \(C\ge C_+(t)\), giving (4). The full endpoint/atom conventions and inverse formulas follow directly.

**5. Sharp optimum.** For \(0<q<1\), differentiation of (2) gives
\[
p'(q)=\frac{q(4-\sqrt{1+q^2})}{(1+q^2)^2}>0.
\]
For \(q>1\), differentiation gives \(p'(q)=-q/(1+q^2)^{3/2}<0\). The formulas meet continuously at \(q=1\), giving the unique maximum \(p(1)=1/\sqrt2\) and the stated one-sided derivatives. No numerical or asymptotic approximation enters this proof.

## Verification

The standalone standard-library script `checker.py` compares both analytic radii against independent discretizations of the full planar support function and of the actual projected circular rims, across short, equal and tall cylinders and 4,287 diagnostics. It checks marginal CDFs against deterministic midpoint integration in uniform viewing coordinates and the corner atom against direct orientation counting. All passed in the recorded replay. These tests check implementation and boundary conventions; all continuum statements follow from Steps 1–5.

## Relationship to prior work

Vickers and Brown (2001) analyzed the distributions of projected **area and perimeter** for convex particles, including cylinders, and their joint area–perimeter statistic, rather than the pair of enclosing-circle radii. Finch (2012) explicitly represents convex hulls of parallel disks and obtains surface area and mean width; the base-disk projection to an ellipse is a prior geometric fact used above. Kim, Yaskin and Zvavitch (first circulated 2015) investigate unlabelled distribution functions of projection **volumes**, not the extremal inscribed/enclosing circles of a random planar cylinder shadow. Existing results on the complete line-direction width distribution of the circular cylinder concern **one-dimensional projections**, whereas the law here concerns the minima and maxima taken *within the same randomly oriented two-dimensional shadow*. Related cylinder shadow area/perimeter moment formulas also do not determine this joint radius law, its atom, or its height-diameter optimum. The statements are compared by their mathematical observables and implications, not by title alone.

## Limitations

This is a sharp two-parameter elementary classification for circular cylinders, not a uniqueness theorem for general convex bodies. The joint law is singular because one viewing parameter controls both radii; it has no two-dimensional Lebesgue density. Exact atoms are an idealized infinite-precision statistic; recovery under measurement noise is not addressed. Historical priority outside the specifically inspected sources cannot be ruled out. No independent mathematical validation is claimed.

## References

1. G. T. Vickers and D. J. Brown, *The distribution of projected area and perimeter of convex, solid particles*, *Proc. R. Soc. Lond. A* **457** (2001), 283–306, DOI 10.1098/rspa.2000.0667, https://doi.org/10.1098/rspa.2000.0667 .
2. S. R. Finch, *Oblique Circular Cones and Cylinders*, arXiv:1212.5946v1, first public 24 December 2012, https://arxiv.org/abs/1212.5946 .
3. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first public 22 December 2015, https://arxiv.org/abs/1512.07289 .
