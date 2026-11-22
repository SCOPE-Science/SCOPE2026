# Exact bifurcation and selection obstruction for planar half-quasinorm projection

## Finding

Let \(C=\{(x,y)\in\mathbb R^2:\sqrt{|x|}+\sqrt{|y|}\le1\}\), and let \(P_C(z)\) denote the full set of Euclidean nearest points in \(C\) to \(z\). For every \(t\ge0\), the complete diagonal projection is
\[
P_C(t,t)=\begin{cases}
\{(t,t)\},&0\le t\le\frac14,\\
\{(\frac14,\frac14)\},&\frac14<t\le\frac34,\\
\{(t-\frac12+\sqrt{t-\frac34},t-\frac12-\sqrt{t-\frac34}),\ (t-\frac12-\sqrt{t-\frac34},t-\frac12+\sqrt{t-\frac34})\},&\frac34<t<1,\\
\{(1,0),(0,1)\},&t\ge1.
\end{cases}
\]
The exact squared-distance profile \(D(t)=\operatorname{dist}((t,t),C)^2\) is
\[
D(t)=\begin{cases}
0,&0\le t\le\frac14,\\
2(t-\frac14)^2,&\frac14\le t\le\frac34,\\
2t-1,&\frac34\le t\le1,\\
(t-1)^2+t^2,&t\ge1.
\end{cases}
\]
It is continuously differentiable but not twice differentiable at the three transition parameters \(\frac14,\frac34,1\). At the symmetry-breaking threshold, writing \(t=\frac34+\delta\), the two projected points are \((\frac14+\delta\pm\sqrt\delta,\frac14+\delta\mp\sqrt\delta)\). Their separation is \(2\sqrt{2\delta}\), giving an exact square-root bifurcation and sharp one-half Hölder onset along diagonal inputs. For every \(t>\frac34\), no continuous single-valued selection of \(P_C\) exists on any open neighborhood of \((t,t)\).

## Assumptions and scope

The constraint is the compact nonconvex unit sublevel set of the two-coordinate \(\ell_{1/2}\) quasi-norm, written as \(\sqrt{|x|}+\sqrt{|y|}\le1\). Distances are ordinary Euclidean distances. The input is restricted to the nonnegative diagonal only for the exact formula; the no-continuous-selection conclusion concerns full planar neighborhoods of those diagonal inputs. No claim is made about all off-diagonal projection fibers or arbitrary dimensions and exponents.

## Proof

**Reduction to the positive boundary.** For any \(t>0\), changing a negative coordinate of a feasible point to its absolute value keeps feasibility and strictly decreases squared distance to \((t,t)\). Thus every minimizer has nonnegative coordinates. For \(0\le t\le\frac14\), \((t,t)\in C\), so its zero-distance nearest point is uniquely itself. For \(t>\frac14\), the target lies outside \(C\); every closest point belongs to the boundary (otherwise a small move toward the target decreases distance inside a feasible neighborhood). The positive boundary admits the full parametrization \((x,y)=(u^2,(1-u)^2)\) with \(0\le u\le1\).

**A convex scalar reduction.** Put \(v=u(1-u)\in[0,\frac14]\). Direct expansion yields
\[
(u^2-t)^2+((1-u)^2-t)^2
=2v^2+4(t-1)v+1-2t+2t^2.
\]
The right side is strictly convex in \(v\), with unconstrained minimizer \(v=1-t\). Thus its unique minimizing \(v\) is \(\operatorname{clip}_{[0,1/4]}(1-t)\). For \(\frac14<t\le\frac34\), this is \(\frac14\), whose only preimage is \(u=\frac12\). For \(\frac34<t<1\), it is \(1-t\in(0,\frac14)\), with exactly two preimages \(u=(1\pm\sqrt{4t-3})/2\). For \(t\ge1\), it is zero, with exactly two preimages \(u=0,1\). Squaring the components gives precisely the asserted projection fibers. Substituting the optimal \(v\) proves all four squared-distance branches.

**Regularity and onset.** The four expressions have common first derivatives \(0\) at \(\frac14\) and \(2\) at both \(\frac34\) and \(1\). Their one-sided second derivatives at those points are respectively \((0,4)\), \((4,0)\) and \((0,4)\). For \(t=\frac34+\delta\) with \(\delta>0\) small, the two exact branches differ in Euclidean norm by \(2\sqrt{2\delta}\). Each differs from \((\frac14,\frac14)\) by \(\sqrt{2\delta+2\delta^2}\), so the onset has exact Hölder exponent \(1/2\), not any larger exponent.

**No continuous local selection.** Fix \(t>\frac34\) and let \(z_+=(a,b)\) and \(z_-=(b,a)\) be its two distinct nearest points, where \(a>b\ge0\). For the perturbed target \((t+\varepsilon,t-\varepsilon)\), \(\varepsilon>0\), swapping a candidate \((x,y)\) with \(x<y\) strictly improves squared distance, by \(4\varepsilon(y-x)>0\). Thus no nearest point has \(x<y\). As \(\varepsilon\downarrow0\), compactness of \(C\) and continuity of distance show that every limit of nearest points belongs to \(P_C(t,t)\); the ordering forces the limit to equal \(z_+\). For \(\varepsilon<0\), the symmetric argument forces limit \(z_-\). Any putative single-valued nearest-point selection on a neighborhood would therefore have two different directional limits at \((t,t)\), contradicting continuity.

## Verification

The reproducible standalone `check_projection.py` verifies the polynomial energy identity exactly using rational coefficients; checks all transition endpoints, exact rational distances, and the branch classifications over many rational parameters; and numerically contrasts a dense boundary search with the analytical minimum. These checks are supplemental: the exhaustive global minimization follows from the strictly convex quadratic in \(v\), not from the finite tests.

## Relationship to prior work

Yang, Wang and Wang (first arXiv publication 2021-01-05) formulate general nonconvex \(\ell_p\)-ball Euclidean projection, derive necessary optimality conditions and iterative methods, and explicitly acknowledge that projections may have multiple minimizers. Won, Lange and Xu (first arXiv publication 2022-03-01) develop primal/dual methods for convex and nonconvex \(\ell_p\)-ball projection, including caveats about duality gaps. The inspected full-text sections of these sources do not state this exact diagonal global phase diagram, square-root separation law, or local continuous-selection obstruction. Their general algorithms address a broader computational setting but do not explicitly give this global classification. Absence of an exact match in searched sources does not prove historical originality.

## Limitations

Only the two-dimensional half-quasinorm ball and equal nonnegative input coordinates are classified explicitly. This does not yield an all-input closed-form nearest-point map, and does not imply an algorithmic complexity result. Unseen equivalent formulations in earlier nonconvex projection or sparse-shrinkage literature remain a priority risk. The analytic proof has been checked internally; an independent mathematical audit has not been performed.

## References

1. Xiangyu Yang, Jiashan Wang and Hao Wang, *Towards An Efficient Approach for the Nonconvex \(\ell_p\) Ball Projection: Algorithm and Analysis*, arXiv:2101.01350 (first posted 2021-01-05), https://arxiv.org/abs/2101.01350 .
2. Joong-Ho Won, Kenneth Lange and Jason Xu, *A unified analysis of convex and non-convex \(\ell_p\)-ball projection problems*, arXiv:2203.00564 (first posted 2022-03-01), https://arxiv.org/abs/2203.00564 .
