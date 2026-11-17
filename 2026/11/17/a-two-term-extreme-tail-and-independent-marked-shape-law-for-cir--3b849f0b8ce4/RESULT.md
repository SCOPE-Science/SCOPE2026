# A two-term extreme-tail and independent marked shape law for circular three-point spanning trees

## Finding

Let \(V_1,V_2,V_3\) be independent points sampled uniformly by arclength on the unit circle. Let \(T\) be the total Euclidean length of the minimum spanning tree on these three vertices, equivalently the sum of the two shortest of the three pairwise chord lengths. Let \(P\) be the perimeter of their triangle. Then \(T\le 2\sqrt3\), with equality precisely for an equilateral triangle, and as \(t\downarrow0\),

\[
\Pr\{T>2\sqrt3-t\}
=\frac9{\pi^2}t^2-\frac{18\sqrt3}{\pi^2}t^3+O(t^4).
\]

There is also a **marked total-variation limit**. Anchor the cyclic order at the labelled vertex \(V_1\). Denote its three counterclockwise angular gaps by \(\alpha_1,\alpha_2,\alpha_3\), with sum \(2\pi\). On the event \(T>2\sqrt3-t\), let \(I\) be the unique index of the largest gap, put \(r=\alpha_I-2\pi/3\) and \(z=(\alpha_{I+1}-2\pi/3)-(\alpha_{I+2}-2\pi/3)\), with cyclic subscripts. Define \(R_t=r/(2t)\) and \(U_t=z/(3r)\). Then

\[
 (I,R_t,U_t)\ \xrightarrow{\mathrm{TV}}\ (I_*,R_*,U_*),
\]

where \(I_*\) is uniform on \(\{1,2,3\}\), \(R_*\sim\operatorname{Beta}(2,1)\), and \(U_*\sim\operatorname{Uniform}[-1,1]\), **all independent**. Consequently the following pair converges jointly in distribution under the same conditioning:

\[
\left(\frac{2\sqrt3-T}{t},\frac{3\sqrt3-P}{t^2}\right)
\Longrightarrow
\left(R_*,\frac{3\sqrt3}{4}(1+3U_*^2)R_*^2\right).
\]

The second coordinate records the different, quadratic perimeter scale concealed within the linearly constrained spanning-tree configuration. The joint pair is asserted to converge weakly, not in total variation; the latter assertion is reserved for the three-dimensional marked coordinates above.

## Assumptions and scope

Exactly three independent unit-circle vertices and their complete Euclidean chord graph are used. The spanning tree may use either pair of edges sharing a vertex; with three vertices it is obtained by deleting a largest-length edge. The three points are distinct almost surely. The angular gaps are defined by starting at \(V_1\) and moving counterclockwise, so their joint density (in the first two gaps) is constant. All limits concern \(t\to0^+\) with this sampling model fixed. Ties of chord lengths have probability zero and can be resolved arbitrarily outside the rare-event conditioning.

## Proof

**1. Global maximum and localization.** Put \(s(\alpha)=2\sin(\alpha/2)\). The three pairwise chord lengths are \(s(\alpha_1),s(\alpha_2),s(\alpha_3)\). By strict concavity of sine on \((0,\pi)\) and \(\alpha_1+\alpha_2+\alpha_3=2\pi\),

\[
P=\sum_i 2\sin(\alpha_i/2)\le 3\sqrt3,
\]

with equality only for the three equal gaps. As the largest edge has length at least \(P/3\), \(T=P-\max_i s(\alpha_i)\le 2P/3\le2\sqrt3\), and equality is again unique at equal gaps.

Set \(\delta_i=\alpha_i-2\pi/3\), so \(\sum_i\delta_i=0\). Compactness and the unique maximum show that \(T>2\sqrt3-t\) forces \(\delta\to0\). In a fixed small neighborhood of zero, \(s\) is strictly increasing and Taylor expansion gives

\[
s(2\pi/3+\delta)=\sqrt3+\tfrac12\delta-\tfrac{\sqrt3}{8}\delta^2+O(|\delta|^3),
\qquad
2\sqrt3-T=\tfrac12\max_i\delta_i+O(\|\delta\|^2).
\]

On the two-dimensional zero-sum plane \(\max_i\delta_i\ge c\|\delta\|\) for some \(c>0\). Shrinking the neighborhood if needed, \(2\sqrt3-T\ge c'\|\delta\|\). Thus throughout the rare event \(\delta_i=O(t)\) uniformly. This justifies all uniform local Taylor and coordinate manipulations that follow.

**2. Exact wedge geometry.** The anchored gaps have density \(2/(2\pi)^2=1/(2\pi^2)\) on the open gap simplex. On the wedge \(I=i\), define

\[
r=\delta_i\ge0,\qquad z=\delta_{i+1}-\delta_{i+2},\qquad
\delta_{i+1}=(-r+z)/2,\quad\delta_{i+2}=(-r-z)/2.
\]

The wedge constraints are precisely \(|z|\le3r\). Write \(u=z/(3r)\in[-1,1]\). The Jacobian from \((r,u)\) to any two independent gaps is \(3r/2\). The longest chord is precisely \(s(\alpha_i)\) throughout the localized event, and the sum of the other two chords has the **exact** representation

\[
T=4\sin\left(\frac\pi3-\frac r4\right)\cos\left(\frac{3ru}{4}\right).
\]

Hence the deficit function satisfies, uniformly over \(|u|\le1\),

\[
D(r,u)=2\sqrt3-T
=\frac r2+\frac{\sqrt3}{16}(1+9u^2)r^2+O(r^3).
\]

For sufficiently small \(r\), its derivative in \(r\) is positive uniformly in \(u\). Thus, for sufficiently small \(t>0\), the event in each wedge is \(0<r<r_t(u)\), where the unique positive solution of \(D(r_t(u),u)=t\) satisfies by uniform implicit expansion

\[
r_t(u)=2t-\frac{\sqrt3}{2}(1+9u^2)t^2+O(t^3).
\]

**3. Exact integral and two-term probability.** Each of the three wedge integrals is equal by cyclic symmetry. Using the density and the wedge Jacobian yields the exact small-\(t\) identity

\[
\Pr(T>2\sqrt3-t)=\frac9{8\pi^2}\int_{-1}^1r_t(u)^2\,du.
\]

Substitution gives

\[
r_t(u)^2=4t^2-2\sqrt3(1+9u^2)t^3+O(t^4),
\qquad \int_{-1}^1(1+9u^2)\,du=8.
\]

The claimed coefficient pair \(9/\pi^2\) and \(-18\sqrt3/\pi^2\), with an \(O(t^4)\) remainder, follows directly. Uniform analyticity on a compact \(u\)-interval gives a uniform remainder, not merely pointwise asymptotics.

**4. Conditional marks.** On a wedge, set \(r=2tR\). The unnormalized conditional measure becomes

\[
\frac{1}{2\pi^2}\cdot\frac{3r}{2}\,dr\,du
=\frac{3t^2}{\pi^2}R\,dR\,du,
\qquad 0<R<\frac{r_t(u)}{2t}.
\]

The upper endpoint is \(1+O(t)\), uniformly in \(u\), while the event probability is \(9t^2/\pi^2+O(t^3)\). The normalized densities therefore converge in \(L^1\), for all three wedges jointly, to density \(R/3\) on \(\{1,2,3\}\times(0,1)\times(-1,1)\), which factors into uniform \(I\), density \(2R\) for \(R\), and density \(1/2\) for \(U\). This proves total-variation convergence.

Finally, \(D(2tR,u)/t=R+O(t)\) on the conditioned compact domain. Also

\[
3\sqrt3-P=\frac{\sqrt3}{8}\sum_i\delta_i^2+O(t^3)
=\frac{3\sqrt3}{4}(1+3u^2)R^2t^2+O(t^3).
\]

The joint weak limit of the two deficits follows by continuous mapping and uniform remainder control. In particular \((2\sqrt3-T)/t\) tends to \(\operatorname{Beta}(2,1)\).

## Verification

The self-contained checker `verify_mst.py` evaluates the exact one-dimensional cutoff integral by root finding and Gauss–Legendre quadrature; independently approximates the two-dimensional region by a rectangular gap grid; and simulates iid circle vertices with a fixed seed. The checker uses the anchored cyclic gaps described here. It prints `CIRCLE_THREE_POINT_MST_TWO_TERM_AND_MARKED_LAW_OK` upon satisfying all numerical tests.

For example, the cutoff integral gives \(0.000342300351319\) at \(t=0.02\), compared with the two-term asymptotic \(9t^2/\pi^2-18\sqrt3t^3/\pi^2\). At \(t=0.04\), the independent grid quadrature has relative error below \(8\times10^{-5}\) against the wedge integral. The direct iid-circle simulation uses 2,400,000 triples at \(t=0.08\), giving frequency \(0.0047050\), versus the exact local integral \(0.0047308\). The observed conditional mark means exhibit finite-threshold bias, as expected; simulations are corroboration, not an infinite limiting proof.

## Relationship to prior work

Lao and Mayer (2007/2008) computed the near-maximal **perimeter** tail for three circle-uniform vertices, with linear rather than quadratic deficit probability. Koroleva and Nikitin (2013/2014) extended maximal perimeter and area tails to inscribed polygons, while Nikitin and Simarova (2020/2022) developed smooth-kernel Hessian theory. Their smooth-kernel hypotheses do not hold for the spanning-tree length, which is a sum of the two smaller edges and is nonsmooth at the equilateral configuration. The present result concerns a different, geometrically meaningful functional and gives its own wedge cutoff, second coefficient, and marked conditional shape law. None of the perimeter formulas alone fixes the nonsmooth extreme-tail coefficient.

Classical Euclidean minimum-spanning-tree literature (e.g. Aldous and Steele, 1992; Cooper et al., 2015/2016) addresses large samples in domains or independent edge weights rather than the fixed-three-vertex circular tail. A published analysis of the **minimum width** of a circle-inscribed random triangle shares the same equilateral maximizer but uses a different invariant: its reported upper-tail coefficient and conditional constraints are not the spanning-tree formulas here. These comparisons do not constitute exhaustive historical priority certification.

## Limitations

Only three iid arclength-uniform vertices of a Euclidean circle are covered. No claim is made for larger Euclidean spanning trees, nonuniform vertex laws, Steiner trees, or higher-dimensional random polygons. The exact cutoff integral is established only for sufficiently small thresholds, when the unique maximizing configuration controls the whole event. The exact critical small-\(t\) threshold need not be specified to prove the asymptotics. The marked total-variation statement applies to \((I,R_t,U_t)\), not to the two-deficit pair. Historical priority is based on the named searches and inspected publications; independent audit has not been performed.

## References

1. W. Lao and M. Mayer, *U-max-Statistics*, first public arXiv version 2007-04-11, arXiv:0704.1379; journal version 2008, DOI:10.1016/j.jmva.2008.02.001. Section 6 and Lemma 6.2 address the circular triangle **perimeter**.
2. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, first public arXiv version 2013-01-07, arXiv:1301.1360. Section 2.1 and Lemma 2.1 address maximum inscribed-polygon perimeter tails.
3. Ya. Yu. Nikitin and E. N. Simarova, *Generalized Limit Theorems For U-max Statistics*, first public arXiv version 2020-10-09, arXiv:2010.04460. Conditions A5–A6 require a smooth, nondegenerate-Hessian extremum.
4. D. Aldous and J. M. Steele, *Asymptotics for Euclidean minimal spanning trees on random points*, 1992, DOI:10.1007/BF01194923 (different large-sample model).
5. C. Cooper, A. Frieze, N. Ince, S. Janson and J. Spencer, *On the Length of a Random Minimum Spanning Tree*, online 2015-01-23, DOI:10.1017/S0963548315000024 (independent graph edge weights).
