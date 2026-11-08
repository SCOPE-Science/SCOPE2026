# Exact prime-two tongues and neutral fibers in a piecewise-linear doubled circle map

## Finding
For the piecewise-linear circle map
\[
f_{a,b}(x)=\left(2x+a+\frac b2 S(x)\right)\bmod 1,
\qquad S(x)=\begin{cases}4x-1,&0\le x\le1/2,\\3-4x,&1/2\le x\le1,\end{cases}
\]
with \(a\in\mathbb R/\mathbb Z\) and \(0\le b\le1\), a *regular* period-two orbit means two distinct orbit points avoiding the breakpoints \(0\) and \(1/2\). Put
\[
b_*=\frac{\sqrt3}{2},\qquad t(b)=4b^2-3,
\]
and for \(b>b_*\) define
\[
a_j^-(b)=\frac b2+\frac{1-t(b)/2+j}{3+2b},\qquad
 a_j^+(b)=\frac b2+\frac{1+j}{3+2b},\qquad j=0,1.
\]
**Complete regular attracting prime-two parameter classification:** such an orbit exists if and only if
\[
b_*<b\le1,\qquad a\in(a_0^-(b),a_0^+(b))\ \cup\ (a_1^-(b),a_1^+(b)).
\]
There is exactly one regular attracting prime-two orbit at each such parameter. The two displayed regions are disjoint connected period-two tongue regions, whose closures meet the ceiling \(b=1\) in intervals of length \(1/10\); for each fixed \(b\), their common horizontal width is
\[
w(b)=\frac{4b^2-3}{2(3+2b)}.
\]
Their combined planar Lebesgue area in the unit parameter cylinder is exactly
\[
\mathcal A=-\frac{11}{4}+\frac{3\sqrt3}{2}+3\log\frac5{3+\sqrt3}
=0.0133138994263\ldots .
\]
They open linearly at their common vertical threshold:
\[
w(b)=(\sqrt3-1)(b-b_*)+O((b-b_*)^2).
\]
At the critical height \(b=b_*\), the two parameter values
\[
a=\frac12+\frac{\sqrt3}{12},\qquad a=1-\frac{\sqrt3}{12}
\]
each support an entire nondegenerate interval of distinct regular neutral prime-two orbits (their two-step return is the identity on that interval). These are the **only** parameters at this height supporting a regular mixed-itinerary prime-two orbit.

## Assumptions and scope
Points on the circle are represented by \([0,1)\), and the endpoints \(0\) and \(1\) are identified. Attraction means local asymptotic attraction of a regular periodic orbit; nonsmooth cycles passing through either breakpoint are not classified. The two tongues refer to the parameter regions of regular attracting *least-period-two* orbits, not all attracting cycles of other periods. Area is measured using ordinary Lebesgue measure on \([0,1)\times[0,1]\). At the upper height \(b=1\), the contracting affine branch has slope zero but the relevant orbit points are not breakpoints.

## Proof
On the open halves \(I_+=(0,1/2)\) and \(I_-=(1/2,1)\), the real affine lifts are respectively
\[
L_+(x)=p x+a-b/2,\quad L_-(x)=q x+a+3b/2,
\quad p=2(1+b),\ q=2(1-b),\ pq=4(1-b^2).
\]
A regular two-cycle confined to \(I_+\) has return derivative \(p^2\ge4\) and is not attracting. A two-cycle confined to \(I_-\) when \(b<1/2\) has return derivative \(q^2>1\). When \(b\ge1/2\), it cannot have least period two at all: if \(u<v\) in \(I_-\) interchanged, the affine lift gives \((1+q)(v-u)\) as a positive integer, whereas \(0<(1+q)(v-u)<(1+q)/2\le1\). Thus every regular attracting period-two orbit has one point \(x\in I_+\) and the other \(y\in I_-\). Its return derivative is \(pq\); for attraction, necessarily \(pq<1\), or \(b>b_*\). At equality, every local regular fixed point of the affine two-step return has derivative one, hence a local identity, and is not asymptotically attracting.

For a mixed orbit introduce integers \(j_0,\ell\) satisfying
\[
y=p x+a-b/2-j_0,\qquad x=q y+a+3b/2-\ell.
\]
Subtracting gives
\[
(1+q)y-(p+1)x=\ell-j_0-2b.
\]
Because \(0<x<1/2\) and \(1/2<y<1\), the latter forces \(0<\ell-j_0<3\). Thus \(\ell-j_0\) equals \(2\) or \(1\). Denote these possibilities by \(j=0\) and \(j=1\), respectively. They give the **only** possible coordinates and parameter residues:
\[
x_j(b,y)=\frac{(1+q)y-q+j}{p+1},\qquad
 a_j(b,y)=\frac b2+\frac{pq+(1-pq)y+j}{p+1}\pmod1.
\]
For \(b\in[b_*,1]\) and \(1/2<y<1\), both \(x_j\) are strictly between \(0\) and \(1/2\): the smallest endpoint is \((1-q)/(2(p+1))>0\) and the largest is \(2/(p+1)<1/2\). Both \(a_j\) have their ordinary displayed representatives strictly between \(0\) and \(1\): the smallest exceeds \(b/2\), while the largest is \(b/2+2/(p+1)<1\). Thus the congruence lifts uniquely with \(j_0=j\) and \(\ell=2\). Substitution directly proves \(f_{a_j,b}(x_j)=y\) and \(f_{a_j,b}(y)=x_j\); the two points lie in different halves, so the least period is exactly two.

For \(b>b_*\), \(1-pq=t(b)>0\) and \(y\mapsto a_j(b,y)\) is strictly increasing. Its images as \(y\) runs through \((1/2,1)\) are exactly the stated intervals with endpoints \(a_j^-\) and \(a_j^+\). This proves necessity, sufficiency, and uniqueness within each interval. The two intervals cannot overlap, since
\[
a_1^-(b)-a_0^+(b)=\frac{1-t(b)/2}{3+2b}>0.
\]
Continuous endpoint graphs make each region connected. At \(b=1\) the two horizontal sections are \((3/5,7/10)\) and \((4/5,9/10)\), verifying the ceiling intersections.

At \(b=b_*\), \(pq=1\), so \(a_j(b_*,y)\) becomes independent of \(y\). Simplification gives precisely the two critical parameters displayed above. For each of them, every \(y\in(1/2,1)\), paired with \(x_j(b_*,y)\in(0,1/2)\), is a prime-two orbit. The open two-step branch is affine with slope \(pq=1\) and fixes this interval pointwise. The integer-difference argument excludes any other regular mixed-itinerary two-cycle at the same height.

Finally, the width follows by subtracting the endpoints, and differentiation at \(b_*\) gives \(w'(b_*)=\sqrt3-1\). Fubini's theorem and polynomial division give
\[
\mathcal A=2\int_{b_*}^1 w(b)\,db
=\int_{b_*}^1\left(2b-3+\frac6{2b+3}\right)db,
\]
which evaluates to the closed form in the statement.

## Verification
The accompanying standalone `check.py` verifies the affine orbit identities symbolically for both tongues, the critical algebraic parameter values, the linear opening coefficient, and the exact area integral. It also tests fifty explicit rational cycles using exact fraction arithmetic and performs an independent exhaustive integer-lift search for candidate mixed cycles at 255 rational parameter points. Run `python check.py` with SymPy installed. Finite checks are corroboration; the necessity and all-parameter conclusions follow from the proof above.

## Relationship to prior work
Bhattacharyya and Banerjee (2025) introduce exactly this piecewise-linear perturbation of the doubling map, identify attracting tongues and eyes, prove uniqueness of attracting cycles, and prove that single-minus itineraries give tongues; the present classification concerns the first prime period and adds its **exact two component boundaries, parameter-area formula, and two neutral interval fibers**. Their Lemma 7.1 notes that a neutral affine return slope forces algebraic coupling; here the exact algebraic resonance and its entire prime-two fixed intervals are computed. These findings do not assert originality of the map, the tongue/eye terminology, or their qualitative existence theorems. Dezotti (2009) concerns the different analytic sine double-standard family, not the piecewise-affine map or its parameter geometry.

## Limitations
The conclusions are confined to regular prime-two orbits, and no assertion about nonsmooth breakpoint cycles, higher periods, other attracting tongues or eyes, or global basin measures is made. The two critical fibers are neutral, not attracting. The exact area is for the particular given piecewise-linear circle-map family and the full stated parameter cylinder. Historical priority beyond the inspected literature remains subject to further expert review; computational corroboration is not independent proof validation.

## References
- A. Bhattacharyya and K. Banerjee, *On the Piecewise Linear Perturbations of the Doubling Map*, arXiv:2510.11441v1 (first submitted 13 October 2025), https://arxiv.org/html/2510.11441 . Sections 1–2 define the map and slopes, Section 4 treats tongues, Section 7 discusses algebraic neutral multipliers.
- A. Dezotti, *Connectedness of the Arnold tongues for double standard maps*, arXiv:0904.0593v1 (3 April 2009), https://arxiv.org/abs/0904.0593 . Different analytic perturbation of the doubling map.
