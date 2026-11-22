# A first-order enclosing-cylinder switch in the symmetry planes of square pyramids

## Finding
Let \(P_h=\operatorname{conv}(\{(\pm1,\pm1,0)\}\cup\{(0,0,h)\})\), where \(h>0\). Consider all infinite Euclidean circular cylinders containing \(P_h\) whose axis direction belongs to **at least one vertical reflection plane** of this square pyramid. The cylinder axis may be translated freely; only its direction is constrained. Let \(R_{\mathrm{sym}}(h)\) be the least possible radius, and write \(H=\sqrt{2+\sqrt5}\). Then
\[
R_{\mathrm{sym}}(h)=\begin{cases}
1,&0<h\le1,\\
(h^2+1)/(2h),&1<h\le H,\\
\sqrt2\,h/\sqrt{h^2+1},&h\ge H.
\end{cases}
\]
At \(h=H\), the latter two formulas coincide, but there are two inequivalent families of minimizing cylinders. For \(h<H\) every minimizing axis is horizontal and parallel to a base edge. For \(h>H\) every minimizing axis lies in a vertical plane through midpoints of opposite base edges, has a nonzero upward slope and meets the base center. Its unit direction, up to base symmetries and axis reversal, is
\[
\left(\sqrt{\frac2{h^2+1}},0,\sqrt{\frac{h^2-1}{h^2+1}}\right).
\]
At \(h=H\), both the horizontal and the tilted alternatives minimize; no intermediate tilt minimizes. In the one-dimensional orientation profile, a second, strictly local minimum appears at the distinct threshold \(h=\sqrt2\), becoming globally optimal only at \(h=H\). The optimized radius has a first-derivative jump at \(H\), whose one-sided values are \((1-H^{-2})/2=(3-\sqrt5)/2\) and \(\sqrt2/(H^2+1)^{3/2}\), respectively. The first value is approximately \(0.381966\), the second approximately \(0.118034\).

**Scope warning:** This is an exact optimization over **symmetry-plane axis directions only**. No claim is made that these cylinders minimize radius among all three-dimensional axis directions.

## Assumptions and scope
The square base has side length \(2\), lies in the plane \(z=0\), and is centered at the origin. A cylinder is the closed set of points within a specified radius of an arbitrary complete affine line in \(\mathbb R^3\). The permitted directions belong to the union of the four vertical planes fixed by the square's reflections: two planes through opposite edge midpoints and two through opposite vertices. Both vertical components and all affine line offsets are allowed. The result is invariant under uniform scaling: for square half-side \(b>0\) and height \(H_b>0\), multiply the displayed minimum by \(b\) after replacing \(h\) by \(H_b/b\).

## Proof
**1. Reduction to a smallest enclosing circle.** Because a cylinder is convex, it contains \(P_h\) precisely when it contains all five vertices. For a fixed axis direction, orthogonal projection onto its perpendicular two-plane turns the problem into the unique smallest enclosing Euclidean circle of five projected vertices. Reflection and rotation of the square show it suffices initially to take a direction \(u=(\sqrt{1-a^2},0,a)\) with \(0\le a\le1\), in an edge-midpoint reflection plane. Choose perpendicular orthonormal coordinates \(v=(-a,0,\sqrt{1-a^2})\), \(w=(0,1,0)\). The four base vertices project to \((\pm a,\pm1)\) and the apex to \((d,0)\), where \(d=h\sqrt{1-a^2}\). The unique smallest containing circle is centered at \((t,0)\), by reflection symmetry and uniqueness. Moving a negative center towards \(0\) weakly decreases all relevant extreme distances, so \(t\ge0\). Its squared radius is therefore
\[
\min_{t\ge0}\max\{(a+t)^2+1,(d-t)^2\}.
\]
The first expression increases with \(t\); the second decreases until \(t=d\), and then increases. Direct balancing yields the exact fixed-direction radius
\[
R(h,a)=\begin{cases}
\sqrt{1+a^2},&d^2\le1+a^2,\\
\dfrac12\left(D+D^{-1}\right),&d^2>1+a^2,
\end{cases}\qquad D=d+a,
\]
with optimum \(t=0\) in the first case and \(t=(d^2-a^2-1)/(2(d+a))>0\) in the second. The two expressions agree at the boundary.

**2. Exact orientation minimization.** If \(0<h\le1\), the first case applies at every \(a\), and the unique minimum is \(R=1\) at \(a=0\). If \(h>1\), define
\[
a_0=\sqrt{\frac{h^2-1}{h^2+1}}.
\]
For \(a\ge a_0\), the first branch is strictly increasing in \(a\); its minimum is \(R(h,a_0)=\sqrt{1+a_0^2}=\sqrt2 h/\sqrt{h^2+1}\). On \(0\le a<a_0\), the second branch applies and \(D=h\sqrt{1-a^2}+a>1\). The map \(D\mapsto(D+D^{-1})/2\) is strictly increasing for \(D>1\), while \(D(a)\) is strictly concave because \(D''(a)=-h(1-a^2)^{-3/2}<0\). Hence it attains its minimum over \([0,a_0]\) at one of the endpoints, and nowhere in the open interval. The endpoint \(a=0\) gives \((h^2+1)/(2h)\); \(a=a_0\) gives \(\sqrt2 h/\sqrt{h^2+1}\). Thus no other direction in an edge-midpoint plane can minimize. Comparing their squares is equivalent to
\[
(h^2+1)^3\le8h^4\quad\Longleftrightarrow\quad
(h^2-1)(h^4-4h^2-1)\le0,
\]
which, for \(h>1\), holds precisely through \(h=H=\sqrt{2+\sqrt5}\). This gives the three-part law and all edge-plane minimizers.

**3. Other reflection planes.** Every direction lying in a vertical *diagonal* reflection plane is orthogonal to some horizontal base diagonal of Euclidean length \(2\sqrt2\). The two endpoints of that diagonal therefore project to points separated by \(2\sqrt2\). Every enclosing circle has radius at least \(\sqrt2\). The candidates in step 2 have radius strictly below \(\sqrt2\) for every finite \(h>0\). Consequently no diagonal-plane direction is globally minimizing among the permitted directions, and step 2 covers all of them.

**4. Local landscape and contact geometry.** For \(h>1\), on \([0,a_0]\) the derivative of \(D\) vanishes exactly at \(a_1=1/\sqrt{h^2+1}\). The inequality \(a_1<a_0\) is equivalent to \(h>\sqrt2\). Below or at that threshold the orientation profile is increasing. Above it, \(a=0\) and \(a=a_0\) are strict local minima, separated by the strict local maximum \(a=a_1\), of radius \((h^2+2)/(2\sqrt{h^2+1})\); the outer branch increases beyond \(a_0\). When \(1<h<H\), the optimal horizontal cylinder has projected center \(((h^2-1)/(2h),0)\), with the apex and all four base vertices on its boundary (the four base vertices project to two locations). When \(h>H\), the optimal tilted cylinder is centered on the projected origin and all five original vertices contact it. At \(H\) both types coexist. Differentiating the two active analytic formulas yields the stated unequal one-sided derivatives. The jump is downward and strictly nonzero because \(H>\sqrt2\) and the two branches cross transversely. This completes the proof.

## Verification
Run `python3 checker.py` using only the Python standard library. The checker constructs the projected five-point set, independently enumerates all enclosing circles determined by two or three projected points, compares the resulting minimum circle against the analytic fixed-direction formula, and tests the claimed optimum on a deterministic orientation grid over 103 selected and pseudorandom aspect ratios. In the recorded replay, 38,936 assertions passed. Its finite tests corroborate the formulas and do **not** certify the continuum; the continuum proof is given above.

## Relationship to prior work
Schömer, Sellen, Teichmann and Yap (1996 conference; 2000 journal article) develop general exact and numerical methods for minimum-radius enclosing infinite cylinders, including a benchmark for the cube. Petitjean (public preprint August 31, 2010) analyzes algebraic cylinder methods for four and five points and explicitly solves a symmetric *trigonal bipyramid*. The present theorem does **not** claim a new general algorithm. It gives an explicit closed, sharp, all-height phase diagram **under a natural reflection-plane direction constraint** for the five-vertex *square pyramid*, including the distinct local-minimum onset and global switching thresholds. Those explicit equations and contact classifications are not asserted in the inspected portions of the two prior works. A general-purpose exact algorithm could compute individual instances but does not by itself supply this explicit parameter-uniform landscape.

## Limitations
Only vertical reflection-plane axis directions are optimized, not unrestricted directions. The radii and contacts are exact for the specified class. The proof is analytic; the numerical checker is not an exhaustive proof. The earlier algorithmic literature and other historical accounts could contain an equivalent specialized formula not identified in the inspected material. No independent mathematical audit has been performed.

## References
- E. Schömer, J. Sellen, M. Teichmann, C. Yap, *Smallest enclosing cylinders*, SoCG 1996, pp. 413–414, first publicly dated May 1, 1996, https://doi.org/10.1145/237218.237412 .
- E. Schömer, J. Sellen, M. Teichmann, C. Yap, *Smallest Enclosing Cylinders*, Algorithmica 27 (2000), 170–186. https://doi.org/10.1007/s004530010011 . The accessible HTML transcription was read in relevant sections and searched for a square-pyramid specialization: https://www.academia.edu/86051583/Smallest_Enclosing_Cylinders .
- M. Petitjean, *About the Algebraic Solutions of Smallest Enclosing Cylinders Problems*, first public arXiv version 2010-08-31, https://arxiv.org/abs/1008.5259 . Sections 3–7 inspected as text.
