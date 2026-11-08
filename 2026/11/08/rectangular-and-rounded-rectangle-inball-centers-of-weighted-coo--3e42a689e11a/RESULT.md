# Rectangular and rounded-rectangle inball centers of weighted coordinate discotopes

## Finding

Let \(D_{xy},D_{yz},D_{zx}\) be the radius-one closed circular disks centered at the origin in the named coordinate planes of \(\mathbb R^3\). For positive \(a,b,c\), set
\[
K(a,b,c)=aD_{xy}+bD_{yz}+cD_{zx}.
\]
Relabel coordinate axes and disk weights, when necessary, so that \(a\ge\max\{b,c\}\). Denote by \(\mathcal I(a,b,c)\) **the set of centers of all largest Euclidean balls contained in** \(K(a,b,c)\). Its optimal ball radius is \(r=b+c\), a support-function radius already obtainable from earlier geometric results; the radius alone is not claimed as new.

Put \(R_{b,c}=[-c,c]\times[-b,b]\subset\mathbb R^2\), and let \(B_2\) be the closed planar unit disk. The complete optimal-center locus is
\[
\boxed{\mathcal I(a,b,c)=
\begin{cases}
[-(a-b),a-b]\times[-(a-c),a-c]\times\{0\},&\max\{b,c\}\le a\le b+c,\\[3pt]
\big(R_{b,c}+(a-b-c)B_2\big)\times\{0\},&a\ge b+c.
\end{cases}}
\]
The two descriptions coincide at \(a=b+c\). Thus for a uniquely largest disk weight, the centers form a genuine planar rectangle until the **additive threshold** \(a=b+c\), and a rounded rectangle beyond it. If precisely two largest weights tie, the locus is a nontrivial segment; all three weights tie if and only if the largest inscribed ball has a unique center.

Writing \(F(a)=\operatorname{area}_2\mathcal I(a,b,c)\) for fixed \(b,c>0\), the exact planar area is
\[
F(a)=\begin{cases}
4(a-b)(a-c),&\max\{b,c\}\le a\le b+c,\\[2pt]
4bc+4(b+c)(a-b-c)+\pi(a-b-c)^2,&a\ge b+c.
\end{cases}
\]
At \(a=b+c\), \(F\) is continuously differentiable but not twice differentiable, with the **universal second-derivative jump**
\[
\boxed{F''((b+c)+)-F''((b+c)-)=2\pi-8<0.}
\]
All claims concern actual Euclidean inscribed balls of the three-dimensional Minkowski sum, not merely inscribed disks of a planar projection.

## Assumptions and scope

All weights are strictly positive, all three summands are genuine closed disks, all three coordinate planes are mutually perpendicular, and distances and volumes are Euclidean. The sorting convention \(a\ge\max\{b,c\}\) is harmless under coordinate permutation. The planar area of a segment or a point is zero. A largest inscribed ball is a closed Euclidean ball of maximal radius, allowed to touch the boundary.

## Proof

**Step 1 (optimal radius and forced center plane).** The support function of \(K\) at a unit vector \(u=(x,y,z)\) is
\[
h_K(u)=a\sqrt{x^2+y^2}+b\sqrt{y^2+z^2}+c\sqrt{z^2+x^2}.
\]
Set \(X=x^2,Y=y^2,Z=z^2\). Then \(X+Y+Z=1\) and
\(h_K=a\sqrt{1-Z}+b\sqrt{1-X}+c\sqrt{1-Y}\), a concave function on the standard simplex. Its minimum occurs at a vertex and equals \(\min\{a+b,a+c,b+c\}=b+c\). The centered ball of radius \(r=b+c\) therefore lies in \(K\). Since \(K=-K\), the convex average of a radius-\(r'\) ball and its reflection is a centered radius-\(r'\) ball; hence no off-center ball has radius larger than \(r\). Both normal directions \(\pm e_z\) have support \(r\), so any center \(t\) of a radius-\(r\) ball satisfies \(t\cdot e_z=0\). Write \(t=(s,t_2,0)\).

**Step 2 (all three-dimensional inequalities reduce to horizontal normals).** A ball \(B_3(t,r)\) is inside \(K\) exactly when
\(u\cdot t+r\le h_K(u)\) for every unit \(u\). Every nonvertical unit normal can be written as
\(u=(\rho v_1,\rho v_2,\pm\sqrt{1-\rho^2})\), with \(0<\rho\le1\) and \(v=(v_1,v_2)\in S^1\). After subtracting \(r=b+c\) and dividing by \(\rho\), the condition becomes
\[
(s,t_2)\cdot v\ \le\ a-b\Phi_{v_1^2}(\rho)-c\Phi_{v_2^2}(\rho),
\quad \Phi_q(\rho)=\frac{1-\sqrt{1-q\rho^2}}{\rho}
=\frac{q\rho}{1+\sqrt{1-q\rho^2}}.
\]
For every \(q\in[0,1]\), \(\Phi_q\) is nondecreasing in \(\rho\in(0,1]\): the numerator is nondecreasing and the positive denominator nonincreasing. The right side is therefore **smallest at \(\rho=1\)**. All nonhorizontal normal constraints follow from the horizontal ones, and conversely horizontal normals are among the original constraints. The exact condition is consequently
\[
(s,t_2)\cdot v\le a-b-c+c|v_1|+b|v_2|\qquad(v\in S^1).
\]
There is no lost vertical condition, because \(t_z=0\) and \(h_K(\pm e_z)=r\).

**Step 3 (support functions give the complete center set).** The rectangle \(R_{b,c}\) has support function \(h_R(v)=c|v_1|+b|v_2|\). Let \(\kappa=a-b-c\). If \(\kappa\ge0\), the preceding inequalities are exactly the support-function membership test for \((s,t_2)\in R_{b,c}+\kappa B_2\). If \(\kappa<0\), writing \(\delta=-\kappa=b+c-a>0\), they are equivalent to \((s,t_2)+\delta B_2\subseteq R_{b,c}\). Since \(a\ge\max\{b,c\}\), we have \(\delta\le\min\{b,c\}\), and the latter erosion is the rectangle \([-(c-\delta),c-\delta]\times[-(b-\delta),b-\delta]\), equal to the first displayed formula. This proves necessity and sufficiency without a generic-position restriction. The dimensions follow from its side lengths and the positivity of \(b,c\).

**Step 4 (area, continuity and sharp transition).** For \(\kappa\le0\), multiply the two side lengths of the rectangle to obtain \(4(a-b)(a-c)\). For \(\kappa\ge0\), \(R_{b,c}+\kappa B_2\) consists of a rectangle, four side strips, and four quarter-circular sectors. Their combined area is \(4bc+4(b+c)\kappa+\pi\kappa^2\). Both expressions agree at \(\kappa=0\). Differentiating at fixed \(b,c\) gives a common first derivative \(4(b+c)\), whereas the one-sided second derivatives are \(8\) and \(2\pi\), respectively. Because \(2\pi\ne8\), the non-\(C^2\) transition is genuine and the quoted jump is exact.

## Verification

The accompanying standalone file `CHECK.py` checks the support-function constraints for sampled normals, exact predicted incenter-boundary points, excluded exterior test centers, and the analytic area transition across balanced, tied, rectangular, additive-threshold, and rounded-rectangle parameter regimes. Its successful output is `WEIGHTED_DISCOTOPE_INCENTER_LOCUS_CHECKS_PASSED`. The infinite assertions are established by the proof, not by the finite samples.

## Relationship to prior work

Mathis and Meroni, *Fiber Convex Bodies* (first publicly posted 26 May 2021, arXiv:2105.12406), study discotopes and the three-unit-disk example, including its support function and its fiber-body behavior. Gesmundo and Meroni, *The Geometry of Discotopes* (first publicly posted 1 November 2021, arXiv:2111.01241), study the same three coordinate-plane disks, their exposed boundary and associated algebraic hypersurface. Neither of the inspected full manuscripts states the present complete inball-center locus or its universal area-regularity transition. The underlying Minkowski-sum representation, support-function additivity, and radius-only minimization are prior techniques; none is claimed as new. Earlier exact radius optimizations for perpendicular disk sums establish radius formulas and outer-contact phases but do not imply the full set of translated maximum balls by statement alone. The novelty assessed here is limited to the complete optimal-center set and its additive morphology/area transition, not a new radius formula.

## Limitations

The result does not classify arbitrary discotopes with oblique disk planes, ellipses, or nonpositive weights. Standard support-function and morphological-dilation identities are essential prior ingredients. The historical originality assessment is provisional; an equivalent older treatment under inner-parallel-body or morphological-erosion terminology remains possible. No independent mathematical audit is claimed.

## References

1. L. Mathis and C. Meroni, *Fiber Convex Bodies*, arXiv:2105.12406, submitted 26 May 2021; Sections 5.2–5.3, especially Definition 5.20 and Eq. (5.8). https://arxiv.org/abs/2105.12406
2. F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241, submitted 1 November 2021; Sections 2 and 7. https://arxiv.org/abs/2111.01241
