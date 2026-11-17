# Six-corner logarithmic–Dirichlet shape law for small side-inscribed triangle areas

## Finding
Let one point be chosen independently and uniformly on each side of **any nondegenerate Euclidean triangle**. Write \(Q\) for the area of their inscribed triangle divided by the parent area, and condition on \(0<Q<t\), \(t\downarrow0\). The statement concerns **the marked shape**, not the already-published scalar distribution of \(Q\).

Use independent \(X,Y,Z\sim\operatorname{Unif}(0,1)\) as directed side parameters, for which
\[
Q=XYZ+(1-X)(1-Y)(1-Z).
\]
Let \(\mathcal C=\{0,1\}^3\setminus\{(0,0,0),(1,1,1)\}\). Fix \(\delta=1/5\). If \((X,Y,Z)\) lies within coordinatewise distance \(\delta\) of exactly one \(j\in\mathcal C\), let \(J=j\); otherwise set \(J=\dagger\) and all following marks to zero. At any such mixed corner \(j\), let \(\xi,\eta\) be the distances of the **two coordinates with the same corner bit** from their corner values (ordered by original coordinate index), and let \(\omega\) be the distance of the remaining coordinate from its corner value. Define
\[
U_t=\frac{\log\xi}{\log(\xi\eta)},\qquad A_t=\frac{\xi\eta}{t},\qquad B_t=\frac{\omega}{t}.
\]
Then the **joint conditional law** \(\mathcal L(J,U_t,A_t,B_t\mid Q<t)\) converges in **total variation** to the distribution in which \(J\) is uniform over the six mixed corners, \(U\) is independent \(\operatorname{Unif}(0,1)\), and \((A,B)\) is independent of both with density
\[
f_{A,B}(a,b)=2\,\mathbf 1\{a>0,\ b>0,\ a+b<1\}.
\]
Equivalently, \((A,B,1-A-B)\sim\operatorname{Dirichlet}(1,1,1)\). Thus the logarithmic split of the two multiplicative corner distances is uniform and independent of the three-way rare-area budget. In particular \(Q/t\mid Q<t\Rightarrow\operatorname{Beta}(2,1)\), but that last **scalar** consequence was already implied by the published area CDF and is not independently new.

## Assumptions and scope
The parent triangle is any fixed nondegenerate Euclidean triangle. Each sampled point is uniform in relative arclength on a different specified side, independently of the other two. Zero-area configurations have probability zero. All logarithms are natural. Total variation refers to the joint marks \((J,U_t,A_t,B_t)\) only; a continuous slack variable added as an exact deterministic function of these marks is not claimed to converge in total variation. Boundary conventions for the six disjoint corner boxes have no effect. The limit is affine-universal because directed uniform side fractions remain uniform under nonsingular affine maps.

## Proof
**1. Area and geometry of rare configurations.** An affine map sends the parent triangle to the vertices \((0,0),(1,0),(0,1)\). The three sampled positions can be represented by \((X,0),(1-Y,Y),(0,1-Z)\). Their signed determinant, normalized by the parent determinant, is
\[
Q=XY+(1-X-Y)(1-Z)=XYZ+(1-X)(1-Y)(1-Z)\ge0.
\]
The zero set is a union of six cube edges, where at least one parameter equals zero and a different parameter equals one. The logarithmically dominant regions are the six **mixed cube corners** where such zero edges intersect; the interiors of the zero edges make only a lower-order contribution, as the global normalization below confirms.

**2. Local chart near one corner.** Fix \(j\in\mathcal C\) and let \(\xi,\eta\) be the two small distances to the majority-bit corner coordinates, \(\omega\) the small distance to the minority-bit coordinate. Exchanging zeros with ones in the area formula yields identically
\[
Q=\xi\eta(1-\omega)+(1-\xi)(1-\eta)\omega
  =\xi\eta+\omega(1-\xi-\eta).
\]
The map \((\xi,\eta,\omega)\mapsto (a,u,b)\), with
\[
p=\xi\eta=ta,\quad \xi=p^u,\quad \eta=p^{1-u},\quad \omega=tb,
\]
is bijective on positive coordinates, with \(0<u<1\) and Jacobian
\[
d\xi\,d\eta\,d\omega=t^2\bigl|\log(ta)\bigr|\,da\,du\,db.
\]
Inside the \(\delta=1/5\) corner box the inequality \(Q<t\) implies \(0<a\le(1-\delta)^{-1}=5/4\), because \(Q\ge p(1-\omega)\), and \(0<b\le(1-2\delta)^{-1}=5/3\), because \(Q\ge\omega(1-\xi-\eta)\). In chart variables the area condition is exactly
\[
a+b\bigl(1-(ta)^u-(ta)^{1-u}\bigr)<1.
\]
For each fixed \(a>0\), \(u\in(0,1)\), and \(b>0\), the corner-box condition eventually holds and this indicator tends almost everywhere to \(\mathbf1\{a+b<1\}\). In addition,
\[
\frac{|\log(ta)|}{\log(1/t)}=1+\frac{\log(1/a)}{\log(1/t)}
\]
for \(ta<1\), and for \(0<a<5/4\) and small \(t\) its absolute value is bounded by a constant multiple of \(1+|\log a|\). This dominates the transformed measure on the fixed bounded \((a,b,u)\)-box and is integrable. Dominated convergence therefore proves **\(L^1\)-convergence of densities** of the rescaled local subprobability measures:
\[
\frac{\Pr\bigl(Q<t,\ J=j,\ (A_t,U_t,B_t)\in d(a,u,b)\bigr)}{t^2\log(1/t)}
\xrightarrow[L^1]{}\mathbf1\{a>0,b>0,a+b<1,0<u<1\}\,da\,du\,db.
\]
The total mass of this limiting density is \(1/2\). Consequently every mixed corner has probability \(\tfrac12t^2\log(1/t)(1+o(1))\).

**3. Global mass and total-variation normalization.** The pre-existing exact scalar distribution of the same random area, established by Maesumi, has the elementary branch for \(0<t<1/4\):
\[
F_Q(t)=t-\left(3t-\tfrac12\right)\log t+(1-4t)^{3/2}\operatorname{arctanh}\sqrt{1-4t}.
\]
Its small-\(t\) expansion gives \(F_Q(t)=3t^2\log(1/t)+O(t^2)\). Thus the six disjoint corner-box masses account for all the leading probability: the conditional mass of \(J=\dagger\) tends to zero. Dividing the six \(L^1\) density limits by \(F_Q(t)\) gives limiting density \(1/3\) on each corner chart's unit-\(u\) simplex \(a+b<1\). Summing over corners gives total mass \(6\cdot(1/3)\cdot(1/2)=1\). The \(L^1\) convergence of the normalized densities plus vanishing outside-box mass is precisely convergence in total variation of the marked laws, and factors into a uniform corner, a uniform logarithmic split, and density \(2\) on the triangle.

**4. Area fraction as a corollary.** On each corner chart,
\[
\frac Q t = A_t+B_t\bigl(1-(tA_t)^{U_t}-(tA_t)^{1-U_t}\bigr)
\]
tends in probability to \(A+B\), as established by the same dominated-convergence argument. Integrating the uniform simplex density gives \(\Pr(A+B\le s)=s^2\) for \(0\le s\le1\), hence the \(\operatorname{Beta}(2,1)\) scalar limit. This last marginal follows also directly from the known scalar CDF and is not the novel component. QED.

## Verification
A standalone NumPy/mpmath checker reproduces the affine-cube area identity, checks the published scalar CDF against direct cube sampling, evaluates its leading small-area expansion at three scales, and independently importance-samples the exact corner change of variables at three small thresholds. It tests the predicted \(1/2\) local mass coefficient and the three \(1/3,1/3,1/3\) simplex means as well as the uniform logarithmic mark. Run `python check_marked_side_triangle.py` after installing the two dependencies in `requirements.txt`. The finite diagnostic is corroborative only; the total-variation theorem is proved by the preceding \(L^1\) argument.

## Relationship to prior work
The inscribed-triangle area polynomial, complete scalar area distribution, and moment formulas were established by A. Maesumi (2018 preprint; 2019 journal paper) and are **not** asserted to be new. A 2015 public question concerns the same side-stratified model. Published geometric-probability records about the inclusion depth of side-sampled triangles concern containment of a target point rather than the conditional rare-area shape. Separate work on near-maximal random triangles in squares employs a logarithmic split and Dirichlet limit but samples three points **inside** a square and conditions on almost maximal area; its statement does not imply this limit for one sample on each side of a triangle at nearly zero area. The new claim is restricted to the **six-corner marked conditional law with total-variation convergence**.

## Limitations
The theorem is not a new derivation of the scalar area CDF, its tail exponent, its beta marginal, or a result for independently perimeter-uniform points without side stratification. The proof does not give a numerical convergence rate in total variation, nor claim an exact finite-threshold Dirichlet law. The full novelty review of older literature is necessarily subject to independent historical verification.

## References
- A. Maesumi, “Triangle Inscribed-Triangle Picking,” arXiv:1804.11007 (first posted 2018-04-30), https://arxiv.org/abs/1804.11007.
- A. Maesumi, “Triangle Inscribed-Triangle Picking,” *College Mathematics Journal* 50 (2019), 364–371, DOI:10.1080/07468342.2019.1669383. Author-hosted full text: https://armanmaesumi.github.io/papers/2019_triangle_picking/Triangle_Inscribed_Triangle_Picking.pdf.
- “Three points on sides of equilateral triangle,” public mathematical question dated 2015-04-29, https://math.stackexchange.com/questions/1258210/three-points-on-sides-of-equilateral-triangle.
