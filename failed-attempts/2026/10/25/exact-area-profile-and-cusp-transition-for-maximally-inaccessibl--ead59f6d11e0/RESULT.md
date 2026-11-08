# Exact area profile and cusp transition for maximally inaccessible points of rectangles

## Finding
For a Euclidean rectangle of shorter side length \(b>0\) and longer side length \(hb\), \(h\geq1\), let \(r(p)\) be the least length of a line segment joining two boundary points and containing the interior point \(p\). The maximum of \(r\) is \(b\). Define the *maximal-inaccessibility locus* \(I_h\) to be the closure of interior points for which \(r(p)=b\). Its area is \(b^2 A(h)\), where the elementary closed formula below holds for **every** aspect ratio.

Put
\[
 a=(1-2^{-2/3})^{3/2},\qquad
 \theta_0=\arcsin(2^{-1/3}),
\]
\[
 H(t)=\frac{3t}{16}-\frac{3\sin(2t)}{64}-\frac{3\sin(4t)}{64}+\frac{\sin(6t)}{64},
 \qquad C=2a+4H(\theta_0).
\]
Then
\[
 A(h)=\begin{cases}
 h-C+4H\!\left(\arccos((h/2)^{1/3})\right),&1\leq h\leq2,\\
 h-C,&h\geq2.
 \end{cases}
\]
Moreover \(A(h)/h\) is strictly increasing on \([1,\infty)\), so the square uniquely minimizes the proportion of a rectangle occupied by points of maximal inaccessibility; that proportion increases to \(1\) as \(h\to\infty\). The exact transition at aspect ratio \(2\) has a nonanalytic exponent:
\[
 A(h)=h-C+\frac{4}{15\sqrt3}(2-h)^{5/2}
       +O((2-h)^{7/2})\quad(h\uparrow2),
\]
whereas \(A(h)=h-C\) exactly for \(h\geq2\). In particular \(A\) is twice but not three times continuously differentiable at \(h=2\).
Numerically \(A(1)=0.164357556864\ldots\) and \(C=1.006869844116\ldots\).

## Assumptions and scope
The boundary-to-boundary segment is **the entire intersection with the rectangle of a complete straight line through the chosen interior point**. There is no choice of preferred direction, no restriction to segments bisected at that point, and no boundary value of \(r(p)\) is used. Area means planar Lebesgue measure; the limiting boundary of \(I_h\) has area zero. The result holds for all nondegenerate axis-aligned rectangles and, by Euclidean isometry and scaling, for every rectangle. The parameter \(h\) is the larger-to-smaller side ratio and is at least one.

## Proof
Scaling gives \(Q_h=(0,h)\times(0,1)\). Every point admits the vertical full chord of length \(1\); thus \(r(p)\leq1\). For each point, a full chord joining opposite horizontal sides has length at least \(1\), and one joining opposite vertical sides has length at least \(h\geq1\). Therefore a chord of length strictly below \(1\) must join two **adjacent** sides.

Consider the two sides meeting at the origin. A chord with intercepts \((u,0)\) and \((0,v)\), \(u,v>0\), passes through \((x,y)\) precisely when \(x/u+y/v=1\). Minimizing \(u^2+v^2\) under this constraint over unrestricted positive intercepts gives \(u=S x^{1/3}\) and \(v=S y^{1/3}\), where \(S=x^{2/3}+y^{2/3}\); the minimum chord length is \(S^{3/2}\). If \(S<1\), then \(x,y<1\), and these intercepts satisfy \(0<u<1\leq h\), \(0<v<1\), hence they lie on the actual adjacent sides. Conversely, if \(S\geq1\), no chord through that adjacent-side pair can have length below one. The same argument at the other three corners proves that \(r(p)=1\) if and only if
\[
 (x_\varepsilon)^{2/3}+(y_\delta)^{2/3}\geq1
 \quad\text{for every }\varepsilon,\delta\in\{0,1\},
\]
where \(x_0=x\), \(x_1=h-x\), \(y_0=y\), and \(y_1=1-y\). The center satisfies these inequalities for every \(h\geq1\); thus the maximal value is exactly one. The locus is the rectangle with four astroid-corner cutoffs, extending the qualitative bow description from the cited geometric study.

By horizontal and vertical reflection, its area is four times its intersection with \([0,h/2]\times[0,1/2]\). In this quadrant the nearest-corner inequality is strongest, so only \(x^{2/3}+y^{2/3}\geq1\) remains. Set \(a=(1-2^{-2/3})^{3/2}\), so the active region has \(x\geq a\) and \(y\geq b(x)=(1-x^{2/3})^{3/2}\) for \(x\leq1\), with no cutoff once \(x\geq1\). Consequently
\[
 A(h)=4\int_a^{\min\{h/2,1\}}
       \left(\frac12-(1-x^{2/3})^{3/2}\right)\,dx
       +(h-2)_+.
\]
Using \(x=\cos^3 t\) and \(b(x)=\sin^3 t\), the antiderivative becomes
\[
 H(t)=3\int_0^t \sin^4(s)\cos^2(s)\,ds
 =\frac{3t}{16}-\frac{3\sin(2t)}{64}-\frac{3\sin(4t)}{64}+\frac{\sin(6t)}{64}.
\]
The cutoff \(x=a\) corresponds to \(t=\theta_0=\arcsin(2^{-1/3})\), while the upper limit \(h/2\leq1\) corresponds to \(t=\arccos((h/2)^{1/3})\). Evaluating the integral gives the stated two-branch formula.

For \(1\leq h<2\), let \(f(x)=\frac12-(1-x^{2/3})^{3/2}\), strictly increasing on \([a,1)\). Then \(A'(h)=2f(h/2)\). Since \(A(h)=4\int_a^{h/2}f(x)\,dx<2h f(h/2)=hA'(h)\), it follows that \((A(h)/h)'>0\). For \(h\geq2\), \(A(h)/h=1-C/h\), also strictly increasing because \(C>0\).

Finally, for \(h<2\), \(A(h)-(h-C)=4H(\arccos((h/2)^{1/3}))\). As \(h\uparrow2\), the angle is \(\sqrt{(2-h)/3}+O((2-h)^{3/2})\), and \(H(t)=3t^5/5+O(t^7)\). This proves the sharp \(5/2\) law and the differentiability assertion.

## Verification
The companion `rectangle_chord_profile_check.py` numerically compared the exact antiderivative to direct high-accuracy quadrature for ten aspect ratios; checked the area fractions against independent Monte Carlo points for each ratio; and compared the four-corner test with brute angular sampling of actual full chords on 87 noncritical point cases. All tests passed. The program displays the square constant and the approach to the analytic \(5/2\) coefficient. These finite checks are only corroboration; the proof above is exact and covers all real \(h\geq1\).

## Relationship to prior work
Calvo and Muñoz (2010, arXiv:1009.2948v1), Sections 3, 5 and 6, defined maximal shortest-chord inaccessibility and proved a general bow-intersection description for convex polygons. They identified positive-area maximal-inaccessibility loci in rectangles and the change in boundary contact at aspect ratio two. Those contributions are **not** claimed here. The present result evaluates the **complete area-vs-aspect-ratio function**, proves strict monotonicity of the normalized area, and identifies the sharp fractional-power transition; these quantitative assertions are not stated or calculated in the inspected source. The familiar astroid parametrization is likewise background, not claimed as new.

## Limitations
This is a rectangle theorem, not a general classification of maximal-inaccessibility area for arbitrary parallelograms or convex bodies. The formula does not locate all maximizers in scalene triangles, nor does it resolve general minimum-chord inverse problems. Bibliographic searches cannot exclude an unindexed earlier evaluation of the same area profile. The computer checks do not constitute independent scientific validation.

## References
- M. Calvo and V. Muñoz, *The most inaccessible point of a convex domain*, arXiv:1009.2948v1, first public version 2010-09-15, https://arxiv.org/html/1009.2948v1. The relevant full-text material is Definitions 2.5, Proposition 3.3, Lemma 6.1, Corollary 6.2, and the rectangle discussion following it.
