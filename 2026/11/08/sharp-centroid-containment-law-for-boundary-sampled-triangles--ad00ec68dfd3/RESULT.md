# Sharp centroid-containment law for boundary-sampled triangles

## Finding

Let \(T\) be any nondegenerate Euclidean triangle, with side lengths \(a_1,a_2,a_3\), perimeter \(P=a_1+a_2+a_3\), and area centroid \(G\). Independently sample three points uniformly by arclength from the **entire** boundary of \(T\), and denote their convex hull by \(K\). Write \(p_i=a_i/P\), \(e_2=\sum_{i<j}p_ip_j\), and \(e_3=p_1p_2p_3\). Then

\[
\Pr\{G\in K\}=\left(\frac13+\frac{4\log 2}{9}\right)e_2+\left(\frac{8\log2}{3}-1\right)e_3.
\]

In particular, the exact sharp shape-independent range is

\[
\frac1{12}+\frac{\log2}{9}<\Pr\{G\in K\}\le\frac2{27}+\frac{20\log2}{81}.
\]

The upper equality holds precisely for equilateral triangles. The strict lower endpoint is approached, but never attained, by nondegenerate triangles tending to one segment, whose three side-length proportions approach \((1/2,1/2,0)\) in any order. Furthermore, the capture probability is a **strictly Schur-concave function** of the normalized side-length vector: any nontrivial balancing (Robin Hood transfer) of a larger normalized side proportion toward a smaller one increases the probability, provided the resulting proportions remain realizable as nondegenerate triangles.

More generally, fix any three edge-selection probabilities \(q_1,q_2,q_3\ge0\) summing to one. Sample each point by choosing edge \(i\) with probability \(q_i\), then sampling uniformly along that edge. The same polynomial holds with \(p_i\) replaced by \(q_i\). For \(q_1=q_2=q_3=1/3\), the probability is the universal value \(2/27+20\log2/81\) for every triangle, irrespective of its shape. The latter constant is classical; the new content is the exact arbitrary edge-weight formula, its arclength specialization, and the sharp shape comparison.

## Assumptions and scope

All triangles are nondegenerate and planar, sampled points are independent, side endpoints have probability zero, and containment includes the boundary (a zero-probability difference from strict interior containment). An edge's arclength sampling probability is precisely its Euclidean length divided by the perimeter. A side-weighted sampling scheme is a separate model in which edge probabilities are prescribed but locations are conditionally arclength uniform. Probabilities are population probabilities, not finite-sample estimators. The expressions depend only on unordered normalized side lengths; no choice of labeling affects the statements.

## Proof

**Affine reduction and conditional edge allocations.** Every nondegenerate triangle is the affine image of the reference triangle with vertices \(A=(0,0)\), \(B=(1,0)\), and \(C=(0,1)\). The centroid corresponds to \(G=(1/3,1/3)\). Affine transformations preserve convex-hull containment and the uniform *fractional parameter* along any given segment. Thus, for prescribed edge-selection probabilities, the containment probability is independent of the geometric shape conditional on the edge allocation; only occupancy counts matter.

When all three points lie on one edge, capture is impossible. There are two other types, with conditional probabilities \(c_{21}\) (two points on one edge, one on a different edge) and \(c_{111}\) (one point on each edge).

**Two-one allocation.** By relabeling, let the two points on \(AB\) be \((u,0),(v,0)\), and the third point on \(CA\) be \((0,w)\), with \(u,v,w\) independent uniform variables on \([0,1]\). The horizontal slice of their triangle through the centroid has endpoints at horizontal coordinates \(u(1-1/(3w))\) and \(v(1-1/(3w))\). Consequently the centroid lies in their triangle exactly when \(w\ge1/2\) and \(t=w/(3w-1)\) lies between \(u\) and \(v\). Given \(w\), this occurs with probability \(2t(1-t)\). Therefore

\[
 c_{21}=\int_{1/2}^{1}\frac{2w(2w-1)}{(3w-1)^2}\,dw
 =\frac19+\frac{4\log2}{27}.
\]

**One-one-one allocation.** Place the three independent points at \(X=(u,0)\) on \(AB\), \(Y=(1-v,v)\) on \(BC\), and \(Z=(0,w)\) on \(CA\). Their cyclic orientation is counterclockwise except on a measure-zero set. The three cross-product tests for \(G\) to lie in their triangle are

\[
3uv-u-2v+1\ge0,\qquad
3vw-2v-2w+1\le0,\qquad
3uw-u-w\le0.
\]

For \(0\le u\le1/2\), the first constraint restricts \(v\) to the interval \([0,f(u)]\), where \(f(u)=(1-u)/(2-3u)\in[1/2,1]\); the third constraint is automatic. For \(1/2\le u\le1\), the first constraint is automatic and the third says \(w\le h(u)=u/(3u-1)\in[1/2,1]\). The middle constraint, for \(v\in[0,1/2]\), is \(w\ge g(v)=(1-2v)/(2-3v)\in[0,1/2]\); for \(v\ge1/2\), it is automatic. Because \(g(v)\le h(u)\) in the only region where both bounds apply, Fubini's theorem gives

\[
\begin{aligned}
c_{111}
&=\int_0^{1/2}f(u)\,du+\int_{1/2}^{1}h(u)\,du
-\int_0^{1/2}g(v)\,dv\\
&=\frac{2\log2}{3}.
\end{aligned}
\]

For completeness, the three displayed integrals evaluate respectively to \(1/6+2\log2/9\), \(1/6+2\log2/9\), and \(1/3-2\log2/9\). The value of \(c_{111}\) is independently available in earlier work on the equilateral one-point-per-side case and is not claimed as a novel conditional constant.

**Total probability.** The multinomial probabilities of the different edge configurations give

\[
\Pr\{G\in K\}
=3c_{21}\sum_{i\ne j}q_i^2q_j+6c_{111}q_1q_2q_3.
\]

Using \(\sum_{i\ne j}q_i^2q_j=e_2(q)-3e_3(q)\), this is exactly

\[
\Pr\{G\in K\}
=\left(\frac13+\frac{4\log2}{9}\right)e_2(q)
+\left(\frac{8\log2}{3}-1\right)e_3(q).
\]

This proves the weighted-edge and arclength formulas.

**Sharp range and strict shape monotonicity.** For every nondegenerate triangle, its normalized sides satisfy \(0<p_i<1/2\), \(p_1+p_2+p_3=1\). Both coefficients in the polynomial are positive. Since \(e_2\le1/3\) and \(e_3\le1/27\), with joint equality only for the balanced triple \((1/3,1/3,1/3)\), the stated sharp upper bound and its unique equality case follow.

The bounds \(p_i<1/2\) imply \(\sum_i p_i^2<\frac12\sum_i p_i=1/2\), hence \(e_2=(1-\sum_i p_i^2)/2>1/4\), while \(e_3>0\). This yields the strict lower bound \((1/3+4\log2/9)/4=1/12+\log2/9\). It is approached by proportions \((1/(2+\varepsilon),1/(2+\varepsilon),\varepsilon/(2+\varepsilon))\) as \(\varepsilon\downarrow0\).

For strict Schur concavity, perform a nontrivial pair averaging: replace \((x,y,z)\) by \((x-\delta,y+\delta,z)\) with \(x>y\) and \(0<\delta\le(x-y)/2\). Then the pair product increases by \(\delta(x-y)-\delta^2>0\). Thus \(e_2=xy+z(x+y)\) increases strictly, and \(e_3=zxy\) increases (strictly if \(z>0\)). Positivity of both polynomial coefficients completes the comparison. Every majorization comparison between positive side-proportion triples is generated by such averaging operations; all considered endpoints remain in the triangle domain.

## Verification

The accompanying self-contained `verify.py` uses symbolic integration to reproduce both conditional constants, their decomposition and the sharp endpoint formulas. It also generates independently sampled Euclidean boundary points for five triangles with distinct shapes and three separate weighted-edge laws. The tested finite-sample probabilities agree with the analytical formula within five binomial standard errors in each test. Executing the script produces:

`VERIFY_OK conditional_integrals=4 equilateral_and_degenerate_limits=2 independent_samples=1120000`

The analytic proof, rather than those simulations, establishes the result for all admissible triangles and weights. To reproduce: `python verify.py` with Python 3, NumPy, and SymPy installed.

## Relationship to prior work

Wendel's 1962 absorption theorem addresses centrally symmetric random point distributions. A triangle's perimeter-arclength distribution is not centrally symmetric, so Wendel's universal absorption probability does not govern it. Prékopa's 1972 treatment (especially Section 5 and its 1972 equilateral-triangle value) and subsequent analyses of **interior** uniform random triangles establish the equilateral constant \(2/27+20\log2/81\), which is **not a new constant**. When the three edges are selected equiprobably and sampled uniformly on each, an affine radial projection from the triangle centroid connects that boundary model to the classical interior-uniform model, explaining the common value. The result here concerns **Euclidean arclength** weighting on an arbitrary non-equilateral triangle and its complete shape dependence.

The previously calculated one-point-on-each-side conditional probability \(2\log2/3\) is also credited. Neither that conditional probability nor the classical interior-equiprobable result specifies the true arclength-biased probability for an arbitrary triangle or its strict majorization and sharp lower limit. A related published result on random triangles formed from vertices of regular polygons studies conditional area moments, not this continuous-perimeter capture event. No covering statement was found in the inspected sources and relevant record searches; an unindexed general boundary-absorption theorem remains a historical-priority risk.

## Limitations

This result concerns only a triangle's **area centroid**, uniform fractions on each chosen edge, and exactly three independent sampled points. It does not determine capture probability for other fixed interior points, curved boundaries, arbitrary polygonal boundaries, dependent point samples, or nonlinear densities along edges. The sharp lower bound is unattained. The shape-independent equiprobable-edge constant and the one-point-per-side conditional probability are prior results. Historical priority for the remaining shape-dependent claims has not been independently certified.

## References

1. J. G. Wendel, "A Problem in Geometric Probability," *Mathematica Scandinavica* **11** (1962), 109–112, published June 1, 1962, https://doi.org/10.7146/math.scand.a-10655 .
2. A. Prékopa, "On the Number of Vertices of Random Convex Polyhedra," *Periodica Mathematica Hungarica* **2** (1972), 259–282, especially Section 5 and equation (5.24). Author-hosted text: https://rutcor.rutgers.edu/Prekopa/pdf/number.pdf .
3. S. Halász and D. J. Kleitman, "A Note on Random Triangles," *Studies in Applied Mathematics* **53** (1974), 225–237, https://doi.org/10.1002/SAPM1974533225 .
4. E. J. Ionaşcu, "Random triangles in planar regions containing a fixed point," arXiv:1612.08619, first submitted December 15, 2016, https://arxiv.org/abs/1612.08619 .
5. Starvind, "Triangle Centroid Probability" (2021), https://starvind.com/mathematics/randomtri.html (derivation of the one-per-side conditional probability).
