# Sharp two-input BV modulus of variation-preserving minmod reconstruction

## Finding

For every integer \(n\ge 2\) and every slope-scaling parameter \(0\le\lambda\le1\), a cellwise-affine minmod reconstruction of real samples preserves each input's total variation exactly, but its **sharp two-input variation sensitivity** is
\[
\boxed{\mathcal L_n(\lambda)=
\begin{cases}
1,&n=2,\\
1+\lambda,&n=3,\\
1+2\lambda,&n\ge4.
\end{cases}}
\]
All constants are attained by explicit distinct pairs of input arrays, in every dimension and for every permitted \(\lambda\). Thus full-slope minmod reconstruction is an individual-signal variation isometry while its difference-of-reconstructions variation can grow threefold. The first expansive dimension is three, and the largest amplification is already attained with four samples.

## Assumptions and scope

Fix equal-width cells \(I_i=(i-\tfrac12,i+\tfrac12)\) on the real interval \([\tfrac12,n+\tfrac12]\), indexed by \(1\le i\le n\). For \(u=(u_1,\ldots,u_n)\in\mathbb R^n\), let
\[
\Delta_i u=u_{i+1}-u_i,\qquad
V_d(u)=\sum_{i=1}^{n-1}|\Delta_i u|.
\]
Define
\[
\operatorname{mm}(a,b)=
\begin{cases}
\min(a,b),&a>0,\ b>0,\\
\max(a,b),&a<0,\ b<0,\\
0,&\text{otherwise},
\end{cases}
\]
which is equivalently \(\operatorname{median}(0,a,b)\). Let \(s_1(u)=s_n(u)=0\) and, for every \(2\le i\le n-1\),
\[
s_i(u)=\operatorname{mm}(\Delta_{i-1}u,\Delta_i u).
\]
On \(I_i\) define \((R_\lambda u)(x)=u_i+\lambda s_i(u)(x-i)\). Endpoints and interface point-values may be assigned arbitrarily: total variation \(V\) here means **distributional BV variation** on the whole open interval, including jumps between adjacent cells and internal linear slopes. The two-input modulus is
\[
\mathcal L_n(\lambda)=\sup_{V_d(u-v)>0}\frac{V(R_\lambda u-R_\lambda v)}{V_d(u-v)}.
\]
Adding a constant to either input changes its reconstruction by that constant. No positivity, monotonicity, generic-position, or bounded-amplitude assumption is imposed.

## Proof

**1. Exact variation of an individual reconstruction.** Put \(d_j=\Delta_j u\). At interface \(j+\tfrac12\), the jump in \(R_\lambda u\) equals
\[
J_j=d_j-\frac{\lambda}{2}\bigl(s_j(u)+s_{j+1}(u)\bigr).
\]
Each of the two adjacent minmod slopes has the sign of \(d_j\), or vanishes, and has magnitude at most \(|d_j|\). Hence for \(0\le\lambda\le1\),
\[
|J_j|=|d_j|-\frac\lambda2\bigl(|s_j(u)|+|s_{j+1}(u)|\bigr).
\]
The variation inside the cells is \(\lambda\sum_i|s_i(u)|\). Since both endpoint slopes vanish, the interface subtractions sum to exactly \(\lambda\sum_i|s_i(u)|\). Consequently,
\[
\boxed{V(R_\lambda u)=V_d(u)}\quad\text{for every real }u.
\]
This standard one-input stability property is context, not a claim of its discovery.

**2. The exact secant description.** The minmod function is continuous and piecewise affine on \(\mathbb R^2\), and on each affine chamber its derivative is one of \((0,0)\), \((1,0)\), \((0,1)\). Integrating along the straight segment between two arbitrary argument pairs shows that for each interior index there exist \(\alpha_i,\beta_i\ge0\) with \(\alpha_i+\beta_i\le1\) such that
\[
s_i(u)-s_i(v)=\alpha_i\Delta_{i-1}(u-v)+\beta_i\Delta_i(u-v).
\]
The formula also holds across tie loci by continuity. The coefficients may depend on the pair \((u,v)\), but they are fixed for that pair, independent of subsequent linear decompositions. At the two endpoint cells the slope difference vanishes.

**3. Reduction to single-jump columns.** Write \(h=u-v\) and define \(H_j\in\mathbb R^n\) to be zero in cells \(1,\ldots,j\) and one in cells \(j+1,\ldots,n\). Then
\[
h=h_1\mathbf1+\sum_{j=1}^{n-1}(h_{j+1}-h_j)H_j.
\]
Using the secant coefficients from Step 2, the difference \(R_\lambda u-R_\lambda v\) is the image of \(h\) under a fixed linear operator, preserving constants. Its distributional derivative is a finite signed measure. By the triangle inequality for the total variation of signed measures, it suffices to bound each step column \(H_j\).

For such a step, exactly two cell slopes can be nonzero: the slope in cell \(j\), of size \(a=\beta_j\), and the slope in cell \(j+1\), of size \(b=\alpha_{j+1}\). Terms involving the endpoint slopes are interpreted as zero. We have \(0\le a,b\le1\). The within-cell contribution is \(\lambda(a+b)\), the sum of outer interface jumps is \(\lambda(a+b)/2\), and the middle interface jump has magnitude \(|1-\lambda(a+b)/2|\). This also covers the first and last steps, where one outer contribution is absent because its corresponding slope is zero. Since \(\lambda(a+b)\le2\), the middle jump is nonnegative, so the **exact step-column norm** is
\[
\boxed{V(R^{\mathrm{sec}}_\lambda H_j)=1+\lambda(a+b).}
\]
Here \(R^{\mathrm{sec}}_\lambda\) denotes the linear operator associated with the fixed secant coefficients; it is not an additional nonlinear reconstruction. For \(n=2\), both terms vanish; for \(n=3\), at most one is present; for \(n\ge4\), at most two are present. Consequently
\[
V(R_\lambda u-R_\lambda v)\le
\begin{cases}
V_d(u-v),&n=2,\\
(1+\lambda)V_d(u-v),&n=3,\\
(1+2\lambda)V_d(u-v),&n\ge4.
\end{cases}
\]
All these inequalities include \(\lambda=0\) and \(\lambda=1\).

**4. Explicit sharpness for actual pairs.** Let \(\varepsilon=\tfrac12\). For \(n=2\), take \(u=(0,2)\), \(v=u+\varepsilon(0,1)\). For \(n=3\), take \(u=(0,1,3)\), \(v=u+\varepsilon(0,1,1)\). In the second case, the single interior minmod slope responds to the perturbed first difference with coefficient exactly one, so the ratio is \(1+\lambda\).

For every \(n\ge4\), set \(u=(0,2,3,5,8,11,14,\ldots)\), truncating after \(n\) terms, with all increments following the fourth coordinate equal to three. Set
\[
v_i=u_i+\varepsilon\mathbf1_{\{i\ge3\}}.
\]
The center edge between cells two and three initially has increment one and after perturbation has increment \(\tfrac32\), while both neighboring increments remain two. Thus the minmod slopes in **both** cells two and three respond to that one input step with coefficient one. The input-difference variation is \(\varepsilon\) and the reconstructed-difference variation is \((1+2\lambda)\varepsilon\). These are actual finite input pairs without relying on formal directional derivatives. Sign reversal gives corresponding decreasing-data witnesses. The upper bounds and witnesses prove the theorem.

## Verification

Run the included `verify_minmod_bv.py` with Python 3 and no nonstandard dependencies. It evaluates distributional variation from exact cell slopes and all interface jumps using rational arithmetic. Checks comprise 145 full-dimension witness evaluations (dimensions two through thirty and five reconstruction scales), 125 algebraic step-column evaluations, 22,000 seeded rational random two-input trials, and decreasing-profile witnesses. Every check passed. Finite tests serve as reproducibility checks; the result for **all** dimensions, data, and parameters follows from Steps 1–4.

## Relationship to prior work

The minmod limiter and MUSCL-type piecewise affine reconstructions belong to classical variation-diminishing numerical analysis. Harten (1982) develops total-variation-nonincreasing evolution schemes; Dubois's full-text treatment of nonlinear reconstruction and minmod (Sections 2 and 6) establishes the relevant one-input limiter setting, not the present pairwise variation norm of **differences of reconstructed functions**. The published exact two-input variation calculation for an endpoint-preserving three-point median filter concerns a different transformation: it applies a median to neighboring **signal levels**, whereas the present reconstruction applies a minmod median to **adjacent signal differences** and builds a discontinuous piecewise-affine function. Its factor three at full slope neither proves nor subsumes the interpolation-scale and dimension-dependent law above. The present quantitative question is motivated by perturbation stability of a reconstruction even when every single input is variation preserving.

## Limitations

The statement uses real cell averages, equal cell lengths, two fixed zero endpoint slopes, nearest-neighbor minmod slopes, and the **distributional** total variation that counts intercell jumps. It is not a stability result for a complete finite-volume time-step, for higher-order slopes, different boundary conventions, irregular meshes, or multidimensional reconstructions. The one-input isometry is classical; the distinct asserted finding is the sharp two-input coefficient. Historical-priority assessment is based on the accessible primary texts and related published claims, not an exhaustive bibliography. No uniqueness of all extremizing pairs is claimed.

## References

1. A. Harten, *High-Resolution Schemes for Hyperbolic Conservation Laws*, Courant Mathematics and Computing Laboratory research and development report, March 1982, publicly accessible full report: https://ntrs.nasa.gov/api/citations/19830002586/downloads/19830002586.pdf.
2. F. Dubois, *Nonlinear Interpolation and Total Variation Diminishing Schemes*, arXiv:1006.3921v1, initially posted 2010-06-20, https://arxiv.org/pdf/1006.3921. Relevant material: reconstructed variation in Section 2 and minmod limiter in Section 6.
3. *Sharp two-input variation sensitivity of three-point median smoothing on finite paths*, publicly accessible research result, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-sharp-two-input-variation-sensitivity-of-three-point-median-smoo--5759b99f2a42/RESULT.md.
