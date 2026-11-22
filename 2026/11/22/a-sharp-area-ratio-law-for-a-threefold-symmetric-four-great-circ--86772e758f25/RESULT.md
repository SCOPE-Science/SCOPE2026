# A sharp area-ratio law for a threefold-symmetric four-great-circle arrangement

## Finding
For the explicit one-parameter family of four great circles described below, all fourteen spherical cells and their areas are determined. The quotient of the largest by the smallest cell area is uniquely minimized at the regular tetrahedral normal arrangement, but the identity of the largest cell undergoes a second, distinct transition at a unique parameter \(t_*=0.5192000606114\ldots\).

Define
\[
\alpha(t)=\arccos\!\left(\frac{3t^2-1}{2}\right),\qquad
\beta(t)=\arccos(-t),\qquad 0<t<1,
\]
and
\[
A(t)=2\pi-3\alpha(t),\qquad
B(t)=2\pi-\alpha(t)-2\beta(t),\qquad
C(t)=2\bigl(\alpha(t)+\beta(t)-\pi\bigr).
\]
The arrangement has **two** triangular cells of area \(A\), **six** triangular cells of area \(B\), and **six** quadrilateral cells of area \(C\). The parameter \(t_*\) is the unique root in \((1/3,1)\) of
\[
5\alpha(t_*)+2\beta(t_*)=4\pi.
\]
Its smallest and largest cell areas are exactly
\[
m(t)=\begin{cases}A(t),&0<t\leq 1/3,\\ B(t),&1/3\leq t<1,\end{cases}
\qquad
M(t)=\begin{cases}C(t),&0<t\leq t_*,\\ A(t),&t_*\leq t<1.\end{cases}
\]
Thus the full area-ratio profile is
\[
\frac{M(t)}{m(t)}=\begin{cases}
 C(t)/A(t),&0<t\leq1/3,\\
 C(t)/B(t),&1/3\leq t\leq t_*,\\
 A(t)/B(t),&t_*\leq t<1.
\end{cases}
\]
It decreases strictly on \((0,1/3)\), increases strictly on \((1/3,1)\), and tends to infinity at both ends. Its sharp minimum is
\[
\frac{4\arccos(-1/3)-2\pi}{2\pi-3\arccos(-1/3)}
 =2.465777523812557\ldots,
\]
attained only at \(t=1/3\) **within this family**.

## Assumptions and scope
Work on the unit sphere in Euclidean three-space. For \(j=0,1,2\), put
\[
u_j(t)=\bigl(\sqrt{1-t^2}\cos(2\pi j/3),\sqrt{1-t^2}\sin(2\pi j/3),t\bigr),
\qquad u_3=(0,0,-1),
\]
and define the great circles by \(u_j\cdot x=0\). The parameter satisfies \(0<t<1\); the four circles are then distinct and no three are concurrent. Different orientations of the normal vectors do not change the circles. The result optimizes only these explicitly defined threefold-symmetric arrangements; it does **not** assert the unrestricted optimal ratio for arbitrary four great circles.

## Proof
**The cell list.** The top three normal dot products are \((3t^2-1)/2\), and each top-to-fourth dot product is \(-t\). Their positive dependence is \(u_0+u_1+u_2+3t u_3=0\). Hence exactly the two sign patterns in which all four signed inward normals agree in sign describe empty interiors. Of the other fourteen sign cones, two have all top-three signs agreeing and the fourth opposite; these are triangles bounded by the three top planes, each with three interior angles \(\pi-\alpha\). Among the other twelve sign cones, six have the fourth sign agreeing with the majority top-three sign. Each is a triangle with interior angles \(\pi-\alpha,\pi-\beta,\pi-\beta\). The remaining six are quadrilaterals with consecutive interior angles \(\alpha,\beta,\alpha,\beta\). The spherical excess formula (sum of interior angles minus \((k-2)\pi\)) yields the claimed values \(A,B,C\). In particular \(2A+6B+6C=4\pi\), and all three area expressions are strictly positive for \(0<t<1\).

**Derivative control.** Differentiating and putting
\[
\rho(t)=-\frac{\alpha'(t)}{\beta'(t)}
=\frac{2\sqrt3\,t}{\sqrt{1+3t^2}},\qquad
\beta'(t)=\frac1{\sqrt{1-t^2}}>0,
\]
shows that \(\rho\) increases strictly from \(0\) to \(\sqrt3<2\), with \(\rho(1/3)=1\). It follows that
\[
A'=3\rho\beta'>0,\quad B'=(\rho-2)\beta'<0,\quad C'=2(1-\rho)\beta'.
\]
Now \(A-B=2(\beta-\alpha)\). This expression increases strictly, crosses zero exactly at \(t=1/3\), and proves the minimum-cell assertion once \(C>B\) is established. For that comparison write
\[
C-B=3\alpha+4\beta-4\pi,
\qquad (C-B)'=(4-3\rho)\beta'.
\]
The difference is zero in both limiting configurations \(t\downarrow0\) and \(t\uparrow1\), and its derivative changes from positive to negative exactly once, when \(\rho=4/3\). Consequently \(C>B\) throughout the open parameter interval.

Finally
\[
C-A=5\alpha+2\beta-4\pi,
\qquad(C-A)'=(2-5\rho)\beta'.
\]
This difference starts at \(\pi/3>0\), initially increases, then decreases strictly after \(\rho=2/5\), and tends to \(-2\pi\) as \(t\uparrow1\). Its value at \(1/3\) is \(7\arccos(-1/3)-4\pi>0\); for example \(\arccos(-1/3)>3\pi/5\). There is therefore exactly one zero \(t_*>1/3\), giving the maximum-cell assertion.

**Strict ratio monotonicity.** On \((0,1/3)\), the derivative quotient
\[
\frac{C'}{A'}=\frac{2(1-\rho)}{3\rho}
\]
is strictly decreasing. Since \(A(0)=0\), \(C(0)=\pi/3>0\), the integral weighted-average form of \(C/A\) proves \((C/A)'<0\): the ratio exceeds the current derivative quotient. On \([1/3,1)\), use the endpoint equalities \(B(1)=C(1)=0\), where the values at \(1\) mean continuous limits, and write
\[
\frac{C(t)}{B(t)}=
\frac{\int_t^1 \frac{2(\rho(s)-1)}{2-\rho(s)}(2-\rho(s))\beta'(s)\,ds}
{\int_t^1 (2-\rho(s))\beta'(s)\,ds}.
\]
The function \(2(\rho-1)/(2-\rho)\) is strictly increasing, and the weights are positive. Thus this tail average strictly exceeds its value at the lower endpoint; differentiating the quotient gives \((C/B)'>0\). Beyond \(t_*\), \(A/B\) is strictly increasing because \(A'>0\) and \(B'<0\). The limiting divergence follows from \(A\to0\) at \(0\), and \(B\to0\) while \(A\to2\pi\) at \(1\). This proves every asserted range and equality condition.

## Verification
The accompanying standalone Python file `verify_profile.py` independently enumerates the sign cones, derives their spherical vertices from plane intersections, triangulates each convex spherical polygon to calculate its area, and compares the complete fourteen-cell multiset to the analytic formulas for nine parameter values. It additionally samples monotonicity at 9,999 parameter points and bisects the maximum-cell transition. These finite checks corroborate the formulas; the proof above, not the sampling, establishes the universal result.

Execute with `python3 verify_profile.py`. No external Python dependencies are required.

## Relationship to prior work
Bhowmick (arXiv:2611.15244v1, made public 11 November 2026) formulates the arbitrary-arrangement cell-area ratio \(R(n)\) and proves bounds only for sufficiently large \(n\). The Fejes Tóth–Fejes Tóth–Kuperberg survey (arXiv:2202.11366, §19) reports Heppes's 1958 sharp four-circle maximization of the *smallest* cell area at the cuboctahedral arrangement. Thus the tetrahedral parameter and its smallest-cell extremality are established background. The present, narrower statement is the full threefold-symmetric **largest/smallest ratio profile**, exact fourteen-cell area spectrum, and the second extremal-cell identity transition at \(t_*\); none follows as a stated ratio theorem from the surveyed smallest-cell optimum alone. Bezdek and Lángi (arXiv:2201.11234) study different inradius/circumradius extremal quantities for great-circle arrangements.

## Limitations
The theorem does not determine \(R(4)\) among unrestricted arrangements, nor classify arbitrary nonsymmetric perturbations. The source comparisons do not constitute an exhaustive guarantee of historical priority. The 1958 original article by Heppes was represented through the cited scholarly survey, not independently verified in full. Numerical values are approximations to exact trigonometric formulas. Independent audit has not been performed.

## References
1. Krishnendu Bhowmick, *Small cells in arrangements of great circles*, arXiv:2611.15244v1 (11 November 2026), https://arxiv.org/html/2611.15244v1.
2. Gábor Fejes Tóth, László Fejes Tóth and Włodzimierz Kuperberg, *Miscellaneous problems about packing and covering*, arXiv:2202.11366 (2022), §19, https://arxiv.org/abs/2202.11366.
3. A. Heppes, *An extremal property of the spherical net of the cuboctahedron* (1958); referenced by [2] (original text not examined).
4. Károly Bezdek and Zsolt Lángi, *From the separable Tammes problem to extremal distributions of great circles in the unit sphere*, arXiv:2201.11234 (2022), https://arxiv.org/abs/2201.11234.
