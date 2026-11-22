# A period-three discrete spline face raises the convex-regression sensitivity barrier

## Finding
For each integer \(n\ge2\), let \(Q_n\) be Euclidean nearest-point projection onto the cone of convex sequences
\[
\mathcal C_n=\{x\in\mathbb R^n:x_i-2x_{i+1}+x_{i+2}\ge0\text{ for }0\le i\le n-3\}.
\]
Set \(L_n=\sup_{y\ne z}\|Q_n(y)-Q_n(z)\|_\infty/\|y-z\|_\infty\). For each \(m\ge2\), let \(V_m\subset\mathbb R^{3m+1}\) be the sequences linearly interpolated between the sample sites \(0,3,6,\ldots,3m\), and let \(P_m\) denote their Euclidean orthogonal projector. The centered knot row of \(P_m\) has an exact limiting absolute sum
\[
\boxed{\lim_{m\to\infty}\sum_{j=0}^{3m}|(P_m)_{3\lfloor m/2\rfloor,j}|=\frac{9+2\sqrt{33}}{11}=1.862647753916\ldots.}
\]
Equivalently, this constant is the exact \(\ell_\infty\)-operator norm of the bi-infinite, shift-invariant, discrete three-site linear-spline orthoprojector. Each \(V_m\) is the tangent space of a strictly realizable face of \(\mathcal C_{3m+1}\); consequently
\[
\boxed{\liminf_{n\to\infty}L_n\ge\frac{9+2\sqrt{33}}{11}>1+\frac1{\sqrt2}.}
\]
The displayed radical is exact for the bi-infinite discrete spline projector and for the limiting centered face row. The theorem makes **no claim** that it is the exact asymptotic Lipschitz constant of the full convex-regression projector.

## Assumptions and scope
The inputs, fitted values, and perturbations are real and indexed by equally spaced sites, with unweighted Euclidean squared loss defining the metric projection. The coordinate maximum norm appears only in the two-input sensitivity. The integer \(m\ge2\) indexes finite, open-ended interpolation grids with \(3m+1\) samples and \(m+1\) spline knots; no periodic boundary condition is imposed. All limits hold along positive integers; the full-sequence \(\liminf\) follows separately by monotonicity. The expression is not asserted for irregular spacings, weights, or other constraints.

## Proof
**1. A legitimate curvature face.** Index the \(3m+1\) sample sites by \(0,\ldots,3m\), and define the second-difference matrix \(D\) by \((Dx)_i=x_i-2x_{i+1}+x_{i+2}\). Let \(A\) consist of all constraint indices \(i\in\{0,\ldots,3m-2\}\) congruent to \(0\) or \(1\) modulo \(3\). Then
\[
\ker D_A=V_m.
\]
Indeed, the two vanishing second differences in each three-interval cell force the four cell values to lie on the line connecting its two endpoint knots. Conversely every such interpolant satisfies those equalities.

To see that this face occurs as a genuine differentiability region of the metric projector, choose \(x\in V_m\) with knot values \(x_{3k}=k^2\). All constraints in \(A\) hold with equality, while every remaining second difference equals \(2/3>0\). Fix a strictly positive multiplier vector \(\lambda\) on \(A\) and put \(y=x-D_A^{\mathsf T}\lambda\). The normal-cone optimality condition for the closed convex set \(\mathcal C_{3m+1}\) proves \(Q_{3m+1}(y)=x\). The rows of \(D_A\) are independent, strict complementary slackness holds on \(A\), and all inactive inequalities are strict. Thus these same active constraints persist under sufficiently small perturbations of \(y\), and the local projection is the orthogonal affine projection with derivative \(P_m\). Hence
\[
L_{3m+1}\ge\|P_m\|_{\infty\to\infty}.
\]
This inequality is sharp for the local face: one can perturb \(y\) by a sufficiently small positive multiple of a coordinate-sign vector norming any selected row of \(P_m\).

**2. The discrete spline mass matrix.** Write \(B_m\) for the \((3m+1)\)-by-\((m+1)\) interpolation matrix taking knot values to sample values. On each cell from knot \(k\) to \(k+1\), its four rows have weights \((1,0),(2/3,1/3),(1/3,2/3),(0,1)\), with knot endpoint rows counted once globally. Hence
\[
P_m=B_m(B_m^{\mathsf T}B_m)^{-1}B_m^{\mathsf T},
\]
and \(T_m=9B_m^{\mathsf T}B_m\) is tridiagonal, with diagonal \(14,19,\ldots,19,14\) and both off-diagonals \(4\). This also follows by summing the four elementary interpolation weights directly.

**3. Interior Green kernel and exponential localization.** Choose a knot index \(k_m=\lfloor m/2\rfloor\). Let \(a^{(m)}_j=(B_m^{\mathsf T}B_m)^{-1}_{k_m,j}\). For the bi-infinite interior Jacobi matrix with diagonal \(19\) and off-diagonal \(4\), put
\[
\Delta=\sqrt{19^2-4\cdot4^2}=3\sqrt{33},\quad
r=\frac{\Delta-19}{8}\in(-1/2,0),\quad
 g_h=\frac9\Delta r^{|h|}.
\]
The identity \(4r^2+19r+4=0\), together with \(19+8r=\Delta\), shows directly that the bi-infinite tridiagonal matrix sends \((g_h)_{h\in\mathbb Z}\) to the delta sequence at zero, after accounting for the factor \(9\). As \(m\to\infty\), one has
\[
 a^{(m)}_{k_m+h}\longrightarrow g_h\quad\text{for every fixed }h\in\mathbb Z.
\]
Here is a justification including endpoint effects. Factor \(T_m=\mathcal D_m+E_m\) with diagonal entries at least \(14\) and absolute off-diagonal row sum at most \(8\). Every row sum of \(|\mathcal D_m^{-1}E_m|\) is at most \(8/19<1\) (at endpoints it is \(4/14\)). The Neumann series for the inverse, and the fact that its \(k\)-th term cannot connect sites at distance greater than \(k\), yield the uniform estimate
\[
 |(B_m^{\mathsf T}B_m)^{-1}_{ij}|
 \le\frac9{14}\frac{(8/19)^{|i-j|}}{1-8/19}.
\]
Every subsequential local limit of the centered inverse row therefore satisfies the bi-infinite recurrence with a delta at zero, is bounded, and decays at infinity. The recurrence has a unique bounded solution (strict diagonal dominance, or the two characteristic roots), which is \(g_h\). Thus every subsequence has that limit. The same exponential bound permits dominated convergence of absolute row sums.

**4. Exact limit of the centered knot row.** The output at sample site \(3k_m\) is the fitted knot value, so its row of \(P_m\) is obtained by linearly interpolating the inverse-Gram row \(a^{(m)}\) across the three inter-knot samples. In the limit its knot coefficients are \(g_h\). On the three positive-side samples following knot \(h\ge0\), the coefficients are
\[
\frac{2g_h+g_{h+1}}3=\frac{g_h(2+r)}3,\qquad
\frac{g_h+2g_{h+1}}3=\frac{g_h(1+2r)}3,\qquad g_{h+1}=rg_h.
\]
Because \(-1/2<r<0\), the first two have the sign of \(g_h\) and the third has the opposite sign. Their absolute values sum to \(|g_h|\), since \((2+r+1+2r)/3+|r|=1\). Reflection gives the same contribution to the negative side, while the center contributes \(g_0\). It follows that the limiting absolute row sum is
\[
\frac9\Delta\left(1+2\sum_{h\ge0}|r|^h\right)
=\frac9\Delta\left(1+\frac2{1+r}\right)
=\frac{9+2\sqrt{33}}{11}.
\]
This proves the corresponding lower bound for \(\liminf_m\|P_m\|_{\infty\to\infty}\).

**5. Exact norm for the infinite discrete spline projector.** Let \(B_\infty:\ell^2(\mathbb Z)\to\ell^2(\mathbb Z)\) interpolate knot samples at sites \(3k\), with the same cellwise weights as Step 2. It is bounded and has closed range because each knot coordinate appears unchanged among the output samples. Its Gram operator is the strictly positive, invertible Jacobi operator with diagonal \(19/9\) and neighboring entries \(4/9\). Therefore \(P_\infty=B_\infty(B_\infty^{\mathsf T}B_\infty)^{-1}B_\infty^{\mathsf T}\) is the Hilbert-space orthogonal projector onto its closed range. The Green coefficients \(g_h\) decay geometrically, giving uniformly absolutely summable matrix rows and hence a bounded extension of \(P_\infty\) to \(\ell^\infty\). Every knot row is a translate of the row computed in Step 4, with absolute sum exactly \(C_*=(9+2\sqrt{33})/11\). Every nonknot sample output is a convex combination of its two neighboring knot outputs; thus every other row has absolute sum at most \(C_*\). Taking the signs of the knot row as input attains the operator norm on \(\ell^\infty\) (or approximates it with finite-support inputs in \(\ell^2\)), so \(\|P_\infty\|_{\infty\to\infty}=C_*\). No global upper bound for the nonlinear convex-sequence projection is inferred. 

**6. From the subsequence to every sample count.** For any active subset \(A\) of the second differences on \(n\) sites, retain it on \(n+1\) sites and leave the final new inequality inactive. Its orthogonal active-space projector is \(H_A\oplus[1]\). Since every independent active subset is realized on a full-dimensional local differentiability region by the strictly complementary construction in Step 1, the full projector Lipschitz constants satisfy \(L_{n+1}\ge L_n\). Therefore the bound along \(n=3m+1\) extends to the full limit inferior. The strict improvement over \(1+1/\sqrt2\) follows immediately from the explicit constants.

## Verification
Run `python3 CHECK.py` with Python 3 and no additional dependencies. It reconstructs the interpolation and Gram matrices with rational arithmetic for \(2\le m\le9\), computes exact orthogonal projectors, checks symmetry, idempotence, the convex-combination bound on every interior sample row, and the Green-kernel value at longer grids using an independently coded tridiagonal solver. It reports **692 supplementary assertions passed**, a limiting coefficient of approximately \(1.862647753916005\), and finite centered-row values approaching this limit. The finite calculations do not replace the analytic recurrence, boundary control, or local-face realization.

## Relationship to prior work
A published study of convex least-squares projection on equally spaced sites gives exact \(L_n\) at two through five sites and the lower bound \(\liminf_n L_n\ge1+1/\sqrt2\) using alternating active curvature constraints [4]. The present argument uses a different, period-three face and gives a strictly stronger limit-inferior bound, not a restatement of the earlier conclusion. Meyer [2] and Lin–Sun–Toh [1] establish shape-constrained regression and its computational and convex-optimization framework, but not the period-three Green-kernel coefficient. Passenbrunner [3] establishes uniform control of **continuous** spline orthoprojectors; the projector here is with respect to counting measure on **discrete sites** and serves as a local derivative of a nonlinear convex-sequence projector. Their general continuity or boundedness results do not imply this exact radical from the results inspected.

## Limitations
No exact global formula for \(L_n\) at arbitrary \(n\) is obtained, nor an exact unrestricted limiting constant; other active faces may have larger amplification. The coefficient is exact for the infinite discrete spline projector and the limiting central row of finite period-three faces; a full finite-face operator-norm limit is not asserted. The argument uses unweighted equally spaced real samples; it does not cover continuous spline least squares or arbitrary sampling designs. Earlier equivalent discrete spline Green-kernel estimates or numerical-stability results under other terminology remain a priority risk. No independent audit has been performed.

## References
1. M. Lin, D. Sun, K.-C. Toh, *An augmented Lagrangian method with constraint generation for shape-constrained convex regression problems*, first public preprint arXiv:2012.04862v1 (2020-12-09), https://arxiv.org/abs/2012.04862.
2. M. C. Meyer, *Inference using shape-restricted regression splines*, first public preprint arXiv:0811.1705v1 (2008-11-11), https://arxiv.org/abs/0811.1705.
3. M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, first public preprint arXiv:1608.06720v1 (2016-08-24), https://arxiv.org/abs/1608.06720.
4. *Five-point nonlocal instability and a persistent lower bound for convex least-squares projection*, published open mathematical result (2026-11-01), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-five-point-nonlocal-instability-and-a-persistent-lower-bound-for--45dce1453393.
5. *Sharp rough-input slope amplification for periodic linear-spline orthoprojection*, published open mathematical result (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-rough-input-slope-amplification-for-periodic-linear-spline--ce52dee09ef7.
