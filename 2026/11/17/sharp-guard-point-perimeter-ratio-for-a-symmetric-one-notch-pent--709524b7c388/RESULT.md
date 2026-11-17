# Sharp guard-point/perimeter ratio for a symmetric one-notch pentagonal family

## Finding

For the planar pentagon \(F_{b,h,t}\) whose counterclockwise ordered vertices are
\[
(-1,0),\quad(1,0),\quad(b,h),\quad(0,(1-t)h),\quad(-b,h),
\]
with \(b>0\), \(h>0\), and \(0<t<1\), let \(K(F)\) denote its visibility kernel. Write \(C(F)=\operatorname{conv}F\), \(G(F)=|K(F)|/|F|\), and \(P(F)=\operatorname{Per}(C(F))/\operatorname{Per}(F)\). Then
\[
\sup_{b,h>0,\;0<t<1}\frac{G(F_{b,h,t})}{P(F_{b,h,t})}
=\mathcal A_*=
\frac{(1-t_*^2)(t_*+3-2\sqrt2)}{(t_*+\sqrt2-1)^2}
=1.0260783949639667\ldots,
\]
where \(t_*\in(0,1)\) is the unique root of
\[
t^3+3(\sqrt2-1)t^2+(10\sqrt2-13)t+7-5\sqrt2=0.
\]
The supremum is **not attained by any finite-height member**. Its unique maximizing limiting shape parameters are \(t=t_*\) and \(b=b_*:=t_*(1+\sqrt2)/(1-t_*)\), approximately \(t_*=0.0583459039562446\), \(b_*=0.149587277570275\), with \(h\to+\infty\).

The finite pentagon \(F_{3/20,1000,3/50}\) satisfies the strict rational certificate
\[
\frac{G(F)}{P(F)}>
\frac{10312074711061}{10052350547239}>\frac{41}{40}.
\]
All assertions concern this precisely defined symmetric single-notch family; no global optimality among arbitrary simple polygons or arbitrary pentagons is claimed.

## Assumptions and scope

The pentagon is simple, with one inward notch, for every \(b,h>0\) and \(0<t<1\). It contains its boundary and interior. The visibility kernel is the set of points \(z\) for which every segment \([z,w]\) with \(w\in F\) is contained in \(F\). Equivalently, for a counterclockwise simple polygon, the kernel is the intersection of its closed inward edge halfplanes. All areas are planar Lebesgue areas and all perimeters are Euclidean lengths. Translating, uniformly scaling, or reflecting the polygon leaves both ratios unchanged. The normalized lower half-width of the trapezoid is one and the normalized height is \(h\); there is no assumption of equilateral sides or fixed aspect ratio.

## Proof

**1. Kernel and polygon area.** Apply the invertible vertical change of coordinates \((x,y)\mapsto(x,y/h)\), and use the same symbols for the normalized horizontal coordinates. The five inward edge halfplanes intersect in
\[
0\le y\le1-t,\qquad
|x|\le\min\left\{1+(b-1)y,\ \frac b t(1-t-y)\right\}.
\]
The upper boundary comes from the two notch sides. The other two sloping bounds come from the outer trapezoid sides; the bottom side gives \(y\ge0\). The unnormalized polygon area is
\[
|F_{b,h,t}|=h[1+b(1-t)].
\]
Let \(k(b,t)=|K(F_{b,h,t})|/h\). Integrating twice the displayed half-width gives, with the equality point included in either branch,
\[
k(b,t)=
\begin{cases}
\dfrac{b(1-t)^2}{t},&0<b\le\dfrac{t}{1-t},\\[5pt]
\dfrac{b^2(1-t)^2+b(1-t^2)-t}{b(1+t)-t},&b>\dfrac{t}{1-t}.
\end{cases}
\]
In the second branch the active constraint switches at \(y_0=[b(1-t)-t]/[b(1+t)-t]\). This evaluates the kernel area for every admissible parameter (not just sampled cases).

**2. Exact perimeter and the infinite-height bound.** Put \(L=\sqrt{h^2+(1-b)^2}\) and \(N=\sqrt{t^2h^2+b^2}\). The outer hull is the trapezoid with vertices \((-1,0),(1,0),(b,h),(-b,h)\). Direct edge lengths yield
\[
\operatorname{Per}(C)=2(1+b+L),\qquad
\operatorname{Per}(F)=2(1+L+N).
\]
Therefore
\[
\frac GP=\frac{k(b,t)}{1+b(1-t)}\left(1+\frac{N-b}{1+b+L}\right).
\]
For finite \(h>0\), the strict triangle inequality gives \(N-b<th\), and \(1+b+L>h\). Thus
\[
\frac GP<(1+t)\frac{k(b,t)}{1+b(1-t)}=: \Phi(b,t),
\]
while, with \(b,t\) fixed, \(\lim_{h\to\infty}G/P=\Phi(b,t)\). Hence maximizing over all finite heights is exactly the two-variable supremum of \(\Phi\), and cannot be attained at finite height.

**3. Optimize the trapezoid and notch parameters.** For \(b\le t/(1-t)\), \(\Phi\) is strictly increasing in \(b\), and its boundary maximum equals \(1-t<1\). For \(b>t/(1-t)\), differentiation of the second displayed kernel-area branch gives
\[
\frac{\partial\Phi}{\partial b}=
\frac{-2t(1+t)[b^2(1-t)^2-2bt(1-t)-t^2]}
{[1+b(1-t)]^2[b(1+t)-t]^2}.
\]
The numerator changes sign once, at \(b=b(t)=t(1+\sqrt2)/(1-t)>t/(1-t)\), making \(b(t)\) the unique global maximum for each \(0<t<1\). Substitution gives
\[
\max_{b>0}\Phi(b,t)=H(t):=
\frac{(1-t^2)(t+3-2\sqrt2)}{(t+\sqrt2-1)^2}.
\]
Its exact derivative is \(H'(t)=-p(t)/(t+\sqrt2-1)^3\), where \(p(t)\) is the stated cubic. The derivative
\[
p'(t)=3t^2+6(\sqrt2-1)t+10\sqrt2-13
\]
is strictly positive for \(t\ge0\). Because \(p(0)=7-5\sqrt2<0\) and \(p(1)>0\), there is exactly one root \(t_*\in(0,1)\); \(H\) increases then decreases, uniquely maximizing at \(t_*\). Moreover \(H(t_*)>H(0)=1\). This finishes the exact supremum, uniqueness of its limiting shape, and nonattainment.

**4. Explicit finite strict witness.** For \(b=3/20\) and \(t=3/50\), the kernel formula gives \(G=12149/12551\). With \(h=1000\), use \(N>th\) and \(L<h+(1-b)^2/(2h)\) (the latter follows by squaring positive terms). Then
\[
\frac GP>\frac{12149}{12551}\left(1+
\frac{th-b}{1+b+h+(1-b)^2/(2h)}\right)
=\frac{10312074711061}{10052350547239}>\frac{41}{40}.
\]
Every inequality and comparison in this final witness is exact rational arithmetic.

## Verification

The included standalone `verify.py` reconstructs the visibility kernel from the five oriented edge halfplanes using exact rational clipping, computes its area independently by the shoelace formula, and tests the derived piecewise formula against a grid of rational parameters covering both active-constraint chambers and their common boundary. It also checks the polygon area, the rational witness inequality, and the cubic-root sign pattern. These finite tests are regression checks, not substitutes for the universal analytic proof above. Run `python verify.py` with the Python 3 standard library; no third-party dependencies are used.

## Relationship to prior work

Nakano's 2026 study defines the guard-point and perimeter ratios, proves the general inequality \(G\le2P\), gives a pentagonal counterexample to \(G\le P\), and explicitly asks for analysis of symmetric pentagonal notch families. Baker's subsequent 2026 study strengthens the *area* inequality and gives a certified **global lower bound exceeding \(1.061\)** for the distinct unrestricted perimeter supremum, as well as reductions and outstanding one-notch optimization tasks. The present \(1.026078\ldots\) is therefore **not** a new record global lower bound. It is an exact sharp value and unique limiting optimizer for the specific three-parameter symmetric centered-notch family defined here, not implied by their general inequalities, constructions, or certified global bound. The finite witness by itself is not the principal new claim.

## Limitations

No global optimum over all pentagons or arbitrary simple polygons is established. The one-notch family restricts the notch tip to the vertical symmetry axis, with two identical upper arms and a trapezoidal hull. Shapes approaching the sharp constant become infinitely tall in the fixed-bottom normalization, so no finite member attains it. The related literature search cannot rule out an unindexed equivalent result, and the complete text of Sibley's earlier paper could not be inspected; only its abstract and later citations were available. Independent expert validation has not occurred.

## References

1. M. Nakano, *Sibley's Guard-Point Convexity Measure: A Perimeter Counterexample and a Dominance Bound*, arXiv:2606.05052, first public June 3, 2026; especially Section 6, Question 1 and the first proposed direction. https://arxiv.org/abs/2606.05052
2. D. C. Baker, *The Kernel Deficit Dominates Twice the Hull Deficit: A Sharp Strengthening of Nakano's Inequality*, arXiv:2608.25057, first public August 25, 2026; especially Section 9 on the separate unrestricted perimeter optimization. https://arxiv.org/abs/2608.25057
3. T. Sibley, *Comparing Convexity Measures*, 2025, DOI:10.1080/0025570X.2025.2495526; abstract and cited definitions only, full text unavailable. https://doi.org/10.1080/0025570X.2025.2495526
