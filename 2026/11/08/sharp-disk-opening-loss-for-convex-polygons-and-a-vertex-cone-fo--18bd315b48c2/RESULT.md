# Sharp disk-opening loss for convex polygons and a vertex-cone formula for polytopes

## Finding

For a nonempty compact convex body \(P\subset\mathbb R^d\), let \(B\) be the closed Euclidean unit ball, and set
\[
P_r=\{c:c+rB\subset P\},\qquad P(r)=P_r+rB,\qquad
E_r(P)=d_H(P,P(r)).
\]
Thus \(P(r)\) is the union of all radius-\(r\) balls contained in \(P\). Assume throughout that \(0<r\le R_{\mathrm{in}}(P)\), so \(P_r\ne\varnothing\).

**Vertex-cone certificate in every dimension.** If \(P\) is a full-dimensional convex polytope described by irredundant supporting inequalities \(\langle n_j,x\rangle\le b_j\), with outward *unit* normals \(n_j\), then for every vertex \(v\) let \(I(v)\) be its incident facets and define
\[
\lambda_v=\min\{\|z\|_2:\langle n_i,z\rangle\le-1\ \text{for all }i\in I(v)\}.
\]
The minimum exists, is finite, and satisfies \(\lambda_v>1\) for \(d\ge2\). The exact *small-radius* loss and a lower bound at every admissible radius are
\[
\boxed{\quad E_r(P)\ge r\bigl(\max_{v}\lambda_v-1\bigr)\quad(0<r\le R_{\mathrm{in}}(P)),\quad}
\]
with equality for every sufficiently small positive \(r\). The small-radius threshold may depend on \(P\); no uniform threshold over all polytopes is asserted.

**Sharp planar extremal inequality and rigidity.** If \(P\) is a convex \(n\)-gon with \(n\ge3\) genuine vertices of interior angles \(\theta_1,\ldots,\theta_n\in(0,\pi)\), then for every admissible \(r\),
\[
\boxed{\quad\frac{E_r(P)}r\ge
\frac1{\sin(\frac12\min_i\theta_i)}-1
\ge\sec\!\left(\frac\pi n\right)-1.\quad}
\]
The first inequality becomes equality for all sufficiently small \(r>0\). The second bound is attained for **every** \(r\) up to the inradius of a regular \(n\)-gon, so its constant is sharp globally, not only asymptotically. Equality in the final bound at any positive admissible radius forces all \(n\) angles to be equal; conversely every equiangular \(n\)-gon attains it for all sufficiently small radii.

There is also quantitative rigidity at **every** admissible radius. Put
\[
\theta_0=\pi-\frac{2\pi}n,\qquad
\delta=\frac{E_r(P)}r-\left(\sec\!\frac\pi n-1\right),\qquad
\eta=\theta_0-2\arcsin\left(\frac1{\sec(\pi/n)+\delta}\right).
\]
Then \(\delta,\eta\ge0\) and every interior angle obeys
\[
\boxed{\quad\theta_0-\eta\ \le\ \theta_i\ \le\ \theta_0+(n-1)\eta.\quad}
\]
For fixed \(n\), \(\eta=\frac{2\cos^2(\pi/n)}{\sin(\pi/n)}\delta+O(\delta^2)\) as \(\delta\downarrow0\); the *linear* dependence is optimal already for quadrilaterals.

## Assumptions and scope

The Hausdorff distance is measured using the same Euclidean norm as the inscribed balls. In the polytope statement \(P\) is bounded and full-dimensional, the facet normals are outward and normalized to Euclidean length one, and every listed facet is a genuine supporting facet. A planar \(n\)-gon has no consecutive collinear sides, so all interior angles are in \((0,\pi)\). The inradius is the maximum radius of a Euclidean closed ball contained in \(P\), and the endpoint radius \(r=R_{\mathrm{in}}(P)\) is included even when \(P_r\) is lower-dimensional. The equality and stability statements concern these exact definitions and **do not** assert an exact all-radius formula for each individual nonregular polygon.

## Proof

**1. Offset facets and a vertex-distance identity.** For a polytope \(P=\bigcap_j\{x:\langle n_j,x\rangle\le b_j\}\), a radius-\(r\) Euclidean ball centered at \(c\) lies in \(P\) if and only if \(\langle n_j,c\rangle\le b_j-r\) for every facet. Thus
\[
P_r=\bigcap_j\{c:\langle n_j,c\rangle\le b_j-r\}.
\]
It is convex and nonempty for every admissible \(r\). Since \(P(r)=P_r+rB\) is convex and contained in \(P\), the distance-to-convex-set function attains its maximum on the polytope at some vertex. For every point \(x\),
\[
\operatorname{dist}(x,P_r+rB)=\max\{0,\operatorname{dist}(x,P_r)-r\}.
\]
Consequently,
\[
E_r(P)=\max_{v\in\operatorname{Vert}(P)}\max\{0,\operatorname{dist}(v,P_r)-r\}.
\tag{1}
\]
The point-to-offset distance identity also appears as a general step in Cappello's regularity argument (equation (4.2)); here it is used for a different finite-facet quantitative problem.

**2. Exact vertex-cone coefficient.** Fix a vertex \(v\). For any \(c\in P_r\) and every incident facet \(i\in I(v)\),
\[
\langle n_i,c-v\rangle\le-r,
\]
so \(\|c-v\|_2\ge r\lambda_v\). The minimization defining \(\lambda_v\) has a feasible point by moving sufficiently far from \(v\) into the interior of its tangent cone; the unique minimum exists by coercivity of the norm. Let \(z_v\) attain it. For incident facets \(v+rz_v\) satisfies the shifted inequalities. Every nonincident facet has a strictly positive slack at \(v\), and there are finitely many facets; therefore \(v+rz_v\in P_r\) for every sufficiently small \(r>0\). Hence
\[
\operatorname{dist}(v,P_r)\ge r\lambda_v\quad\text{for all admissible }r,
\qquad
\operatorname{dist}(v,P_r)=r\lambda_v\quad\text{for all sufficiently small }r>0.
\]
For \(d\ge2\), a vertex is incident with at least two nonparallel facet normals. If \(\|z\|_2\le1\), each incident constraint \(\langle n_i,z\rangle\le-1\) forces \(z=-n_i\), which is impossible for two distinct normals; thus \(\lambda_v>1\). Taking maxima in (1) proves both polytope statements.

**3. Planar angle reduction.** At a polygon vertex of interior angle \(\theta\), the intersection of the two incident inward-offset halfplanes is a wedge whose new apex lies on the internal angle bisector at distance \(r\csc(\theta/2)\) from the original vertex. The wedge's apex is its nearest point to the old vertex. Hence
\[
\lambda_v=\csc(\theta_v/2).
\]
The preceding step gives the first planar inequality for all \(r\), and exactness for sufficiently small \(r\).

The angle sum is \(\sum_i\theta_i=(n-2)\pi\), so \(\theta_{\min}\le\theta_0=\pi-2\pi/n\). As \(\csc(\theta/2)\) strictly decreases for \(0<\theta<\pi\),
\[
\csc(\theta_{\min}/2)-1\ge\csc(\theta_0/2)-1=\sec(\pi/n)-1.
\]
If equality with this last constant holds at any admissible \(r\), every angle must be at least \(\theta_0\), and their fixed sum forces every angle to equal \(\theta_0\). Conversely, local exactness proves the equiangular sufficiency claim.

**4. Sharpness at every radius.** For a regular \(n\)-gon \(P\) with incenter \(c\), inradius \(R\), and circumradius \(R\sec(\pi/n)\), every supporting side is tangent to \(c+RB\). The facet formula therefore gives
\[
P_r=c+\left(1-\frac rR\right)(P-c)\qquad(0\le r\le R).
\]
By the support-function characterization of Hausdorff distance between convex bodies,
\[
E_r(P)=\max_{\|u\|_2=1}\bigl(h_P(u)-h_{P(r)}(u)\bigr)
=r\left(\frac{\max_{\|u\|_2=1}h_{P-c}(u)}R-1\right)
=r\bigl(\sec(\pi/n)-1\bigr).
\]
This includes \(r=R\), when the inner center set may be a singleton.

**5. Quantitative angular stability and its order.** Put \(s=\sec(\pi/n)\). The first planar inequality at each vertex gives
\[
\csc(\theta_i/2)-1\le E_r(P)/r=s-1+\delta.
\]
Thus \(\theta_i\ge2\arcsin(1/(s+\delta))=\theta_0-\eta\). Summing the deviations from \(\theta_0\), each of the other \(n-1\) angles can be at most \(\eta\) below it, so \(\theta_i\le\theta_0+(n-1)\eta\). Taylor expansion at \(\delta=0\) gives the stated coefficient.

For sharpness of the *order*, consider the rhombi
\[
P_t=\operatorname{conv}\{(1,0),(0,1+t),(-1,0),(0,-1-t)\},\qquad t>0.
\]
Every rhombus is tangential, so its disk-opening error at every admissible radius equals its local minimum-angle expression. Here \(\theta_{\min}=2\arctan(1/(1+t))=\pi/2-t+O(t^2)\) and \(E_r(P_t)/r=\sqrt{1+(1+t)^2}-1\). Thus its deficit from \(\sec(\pi/4)-1\) is \(t/\sqrt2+O(t^2)\), while an angle deviates by \(t+O(t^2)\). No stability modulus \(o(\delta)\) can replace the linear order uniformly across quadrilaterals.

## Verification

The supplied `opening_verify.py` builds inward-offset polygons by half-plane clipping; determines inradii by linear programming; calculates vertex-to-inner-body distances using nearest points on offset edges; and checks the global lower bound, small-radius equality, and the angular stability inequality on 220 randomly generated convex polygons at two radius scales each. It also checks seven radius values for each regular polygon with 3 to 18 sides (112 tests) and four radii for each of four rectangles (16 tests). It reports `OPENING_GEOMETRY_NUMERIC_OK ...` when all checks succeed. The program needs Python 3 with NumPy and SciPy. These finite numerical checks do not establish the universal theorem; its proof is the preceding geometric argument.

## Relationship to prior work

Cappello (arXiv:2610.36238v1, October 26, 2026) introduces and studies the approximate inner ball condition for \(C^{1,\alpha}\) convex bodies, including the definitions of \(P_r\) and \(P(r)\) and the basic point-to-opening distance identity. The present result concerns nonsmooth polytopes and supplies exact vertex-cone coefficients, a sharp **global** edge-budget extremum, equality characterization, and angular stability. The cited regularity result by itself does not determine any of those angle constants.

The morphological opening operation (erosion followed by dilation) is classical and is not claimed as new. Heppes (1963, pp. 363–364) explicitly describes convex-polygon disk openings as rounded-off corners, and cites even earlier work on disks inside convex domains. This qualitative corner-rounding observation is credited; that paper studies area and perimeter inequalities and does not state the Hausdorff cone coefficient, the sharp fixed-side-count inequality at every radius, or quantitative angular stability. Standard geometry-software documentation separately credits Serra's 1982 text. Prior polygonal angle and distance invariants include the published exact triangle roundness formula and a sharp short-pair distance coefficient for polygons in the mathematical record; those address different functionals. The connection between the corner cone and this particular disk-opening Hausdorff loss, as well as its sharp equiangular minimax statement at every radius, was not located in the searches described in `AUDIT.json`. A classical equivalent in the broader mathematical-morphology literature remains a priority risk; lack of a search hit is not a novelty proof.

## Limitations

There is no claim of a new definition of mathematical opening or a new general property of Euclidean distance to a Minkowski sum. The vertex-cone formula is locally exact for each polytope, but not necessarily at large admissible radii. The planar universal bound applies only to convex polygons with a fixed **number of genuine sides**, and near-equality controls angles, not side lengths or Hausdorff distance to a regular polygon. No claim is made for nonconvex sets, non-Euclidean structuring bodies, general smoothness exponents, or independent mathematical certification.

## References

1. A. R. Cappello, *An approximate inner ball condition characterizing \(C^{1,\alpha}\) convex bodies*, arXiv:2610.36238v1, first publicly posted October 26, 2026, https://arxiv.org/abs/2610.36238 (especially equations (1.1), (1.2), (4.2), Proposition 2.4, and Theorem 1.1).
2. J. Serra, *Image Analysis and Mathematical Morphology*, Academic Press, 1982, as identified in the `spatstat.geom` documentation of morphological opening, https://search.r-project.org/CRAN/refmans/spatstat.geom/html/opening.html. Original book text was not inspected.
3. A. Heppes, *Filling of a domain by discs*, A Magyar Tudományos Akadémia Matematikai Kutató Intézetének Közleményei **8** (1963), 363–371, especially p. 363, https://real.mtak.hu/201454/1/cut_MATKUTINT_8_3_1963_pp363_-_371.pdf (the qualitative disk-opening polygon corner-rounding construction; no Hausdorff loss theorem in the inspected text).
4. Published mathematical records: *Exact triangle formula for Pach--Tardos roundness and sharp fatness calibration*, https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-exact-triangle-roundness-sharp-fatness--f4944b61f2db; and *Sharp uniform angular stability for the short-pair distance coefficient of convex polygons*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b (comparison of the different invariants only).
