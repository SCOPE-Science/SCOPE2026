# Exact second-order variation norm of locally secant-blended cubic Hermite interpolation

## Finding

For arbitrary positive adjacent knot lengths, the sharp gain from discrete changes of secant slope to integrated absolute second derivative of a locally secant-blended \(C^1\) cubic Hermite interpolant is
\[
\boxed{\|H_\theta\|_{\mathrm{discrete}\,W^{2,1}\to\mathrm{derivative\,TV}}
=\frac53\sup_{j\in\mathbb Z}\left(|1-\theta_j|+|\theta_j|\right).}
\]
Consequently the sharp constant is \(5/3\) for **every** (possibly spatially varying) convex choice \(0\le\theta_j\le1\), independent of arbitrarily strong knot-spacing contrasts. These and only these convex choices minimize the constant over all real linear blends. More generally, the exact nonconvex factor is \((5/3)(1+2\sup_j\operatorname{dist}(\theta_j,[0,1]))\). If \(L\) is the continuous piecewise-linear nodal interpolant, then its distributional second derivative is the atomic measure \(D^2L=\sum_j a_j\delta_{x_j}\), with \(\delta_{x_j}\) denoting a point mass. The total variation of that measure is \(\sum_j|a_j|\). Thus the theorem measures the exact roughness cost of replacing the jumps of \(L'\) by a continuous Hermite derivative. It is not a statement about geometric graph curvature.

## Assumptions and scope

Let \((x_i)_{i\in\mathbb Z}\) be strictly increasing, with \(\lim_{i\to-\infty}x_i=-\infty\) and \(\lim_{i\to\infty}x_i=\infty\). Write \(h_i=x_{i+1}-x_i>0\), \(\delta_i=(y_{i+1}-y_i)/h_i\), and \(a_i=\delta_i-\delta_{i-1}\). Real nodal data are admissible when \(\sum_i|a_i|<\infty\); their discrete homogeneous second-order variation is \(V_2(y)=\sum_i|a_i|\). Affine nodal data have zero seminorm and are quotiented out. The full space is identified with \(\ell^1(\mathbb Z)\) by specifying all secant jumps and then integrating them twice up to an affine function.

Fix any real sequence \((\theta_i)\), independently of the data and of the knot positions. At each knot prescribe
\[
d_i=(1-\theta_i)\delta_{i-1}+\theta_i\delta_i.
\]
The unique classical cubic Hermite polynomial on each cell matching values \(y_i,y_{i+1}\) and derivatives \(d_i,d_{i+1}\) gives a globally \(C^1\) piecewise cubic \(H_\theta y\). This is a linear, affine-reproducing scheme. When the weight sequence is bounded, the weak second derivative belongs to \(L^1(\mathbb R)\), and \(V_1((H_\theta y)')=\int_{\mathbb R}|(H_\theta y)''|\). For unbounded weights the map is not bounded in this seminorm, as seen on finite-support jumps.

## Proof

**1. Exact local kernel.** On the cell \([x_i,x_{i+1}]\), let \(t=(x-x_i)/h_i\). The standard cubic Hermite polynomial in normalized coordinates is
\[
P_i(t)=y_i(2t^3-3t^2+1)+h_id_i(t^3-2t^2+t)
+y_{i+1}(-2t^3+3t^2)+h_id_{i+1}(t^3-t^2).
\]
Since \(d_i=\delta_i-(1-\theta_i)a_i\) and \(d_{i+1}=\delta_i+\theta_{i+1}a_{i+1}\), twice differentiating and simplifying cancels every secant-background term, leaving
\[
h_i(H_\theta y)''(x_i+h_it)
=(4-6t)(1-\theta_i)a_i+(6t-2)\theta_{i+1}a_{i+1}.
\tag{1}
\]
The two universal kernels satisfy the **exact** identities
\[
\int_0^1|4-6t|\,dt=\int_0^1|6t-2|\,dt=\frac53.
\tag{2}
\]
Their respective sign changes are at \(2/3\) and \(1/3\). The change of variables \(dx=h_i\,dt\) cancels the factor \(h_i^{-1}\) in (1), so mesh lengths disappear.

**2. Universal upper bound.** By the triangle inequality inside each cell and by (2),
\[
\int_{x_i}^{x_{i+1}}|(H_\theta y)''|\,dx
\le\frac53\bigl(|1-\theta_i||a_i|+|\theta_{i+1}||a_{i+1}|\bigr).
\]
Summing over all cells (nonnegative sums; first finite, then monotone convergence) yields
\[
\int_\mathbb R|(H_\theta y)''|\,dx
\le\frac53\sum_{j\in\mathbb Z}\left(|1-\theta_j|+|\theta_j|\right)|a_j|.
\tag{3}
\]
For bounded weights this proves the claimed bounded operator and the asserted \(L^1\) regularity.

**3. Sharpness and quantifiers.** For any selected integer \(j\), choose all secant jumps zero except \(a_j=1\). Such data exist: choose constant secant slopes to the left of \(j\) and those slopes plus one to its right, and integrate to nodal values. This input has \(V_2(y)=1\). Formula (1) shows that its second derivative vanishes outside the two cells adjacent to \(x_j\), with integrated absolute masses \((5/3)|\theta_j|\) and \((5/3)|1-\theta_j|\), one of which is zero when \(\theta_j=0\) or \(1\). The cell interiors are disjoint, so
\[
\int_\mathbb R|(H_\theta y)''|\,dx
=\frac53\left(|\theta_j|+|1-\theta_j|\right).
\tag{4}
\]
Taking the supremum over \(j\) proves equality in the operator norm, whether or not the supremum is itself attained by an index. It also proves that an unbounded weight sequence cannot define a bounded operator. In the convex case, (4) is a global extremizer for **every** \(j\).

**4. Exact minimax classification.** The elementary identity
\[
|1-v|+|v|=1+2\operatorname{dist}(v,[0,1]),\qquad v\in\mathbb R,
\]
shows that every real blend has norm at least \(5/3\), with equality if and only if \(\theta_j\in[0,1]\) for every index. It gives the precise excess norm for nonconvex extrapolating knot slopes and completes the classification. No mesh regularity or limiting argument is used.

## Verification

The standalone `curvature_transfer_check.py` uses exact rational arithmetic. It checks both kernel integrals, the one-jump equality for selected convex and nonconvex weights, and finite-cell estimates and mesh-length cancellation in 1,000 pseudorandom rational cases. These tests corroborate the displayed identities but do not replace the unrestricted analytic proof. Reproduce with `python curvature_transfer_check.py`; expected final line: `ALL_SECOND_ORDER_VARIATION_TRANSFER_CHECKS_PASS`.

## Relationship to prior work

Lavery (2002) studies \(C^1\) cubic interpolants by **minimizing** second-derivative or geometric-curvature \(L^1\) objectives, and displays a general Hermite representation. The present map instead prescribes **fixed linear local secant blends** and determines their exact induced operator norm for arbitrary mesh and all such weights. These are different objectives: this theorem is neither a formula for the spline that minimizes \(\int|s''|\) nor a claim about geometric curvature.

Aràndiga (2013) studies nonuniform monotone cubic Hermite derivative prescriptions and approximation orders, including nonlinear schemes. Its available abstract does not state a sharp \(\ell^1\)-secant-jump to \(L^1\)-second-derivative norm; complete full-text comparison was unavailable. The result is also distinct from first-order total-variation amplification and \(L^\infty\) spline projection norm estimates, because those control different derivatives or operators.

## Limitations

The statement is for real bi-infinite grids with no finite accumulation, linear data-independent local derivative blends, and the **integral of absolute second derivative**. It does not establish optimality among all nonlinear derivative limiters, all nonlocal cubic splines, or all \(C^1\) interpolants, nor does it assert monotonicity of every interpolated curve. A one-jump witness may have affine growth at infinity; that is allowed in the homogeneous second-order variation class. For arbitrary nonconvex weights, the global operator-norm supremum need not be attained unless an index realizes its maximal coefficient. Historic priority remains conditional on more complete access to the 2013 article and uncatalogued earlier literature.

## References

- John E. Lavery, “Shape-preserving, multiscale interpolation by univariate curvature-based cubic \(L_1\) splines in Cartesian and polar coordinates,” *Computer Aided Geometric Design* **19** (2002), 257–273, DOI: [10.1016/S0167-8396(02)00087-0](https://doi.org/10.1016/S0167-8396(02)00087-0). Full lawful copy: https://people.eecs.berkeley.edu/~sequin/CS284/PAPERS/L1Spline_Lavery.pdf.
- Francesc Aràndiga, “On the Order of Nonuniform Monotone Cubic Hermite Interpolants,” *SIAM Journal on Numerical Analysis* **51** (2013), 2613–2633, DOI: [10.1137/12088495X](https://doi.org/10.1137/12088495X). Published online September 12, 2013.
