# Path-variation instability thresholds for second-difference trend filtering

## Finding
For real data on an equally spaced finite path, the standard \(\ell^1\) second-difference trend filter is not nonexpansive under *two-input* adjacent total variation once there are four sites. The exact smallest-site coefficient is \(6/5\), independent of tuning. The exact coefficients for two through eight sites are:

| Number of observations | Exact two-input coefficient |
|:--:|:--:|
| \(2\) | \(1\) |
| \(3\) | \(1\) |
| \(4\) | \(6/5\) |
| \(5\) | \(4/3\) |
| \(6\) | \(7/5\) |
| \(7\) | \(28/19\) |
| \(8\) | \(11/7\) |

An exact active-face formula computes the coefficient at *every* length. In particular, for all \(n\ge4\),
\[
\Lambda_n\ge\frac{6\lfloor n^2/4\rfloor}{n(n+1)}>1,\qquad
\liminf_{n\to\infty}\Lambda_n\ge\frac32.
\]
The conclusion concerns the variation of the **difference of two filtered signals**, not variation of one filtered signal.

## Assumptions and scope
For each integer \(n\ge2\), let \(D\in\mathbb R^{(n-2)\times n}\) have consecutive rows \((1,-2,1)\). For \(\lambda>0\), define
\[
T_{n,\lambda}(a)=\mathop{\rm argmin}_{z\in\mathbb R^n}
\left\{\frac12\|z-a\|_2^2+\lambda\|Dz\|_1\right\}.
\]
Strict convexity makes the minimizer unique. Write
\[
V_n(u)=\sum_{i=1}^{n-1}|u_{i+1}-u_i|,\qquad
\Lambda_n=\sup_{V_n(a-b)>0}\frac{V_n(T_{n,\lambda}(a)-T_{n,\lambda}(b))}{V_n(a-b)}.
\]
Constant shifts commute with the filter, so \(V_n\) is an appropriate seminorm on the quotient by constants. The constant \(\Lambda_n\) does not depend on \(\lambda>0\).

For \(F\subseteq\{1,\ldots,n-2\}\), let \(D_F\) be the submatrix with rows indexed by \(F\), and let
\[
P_F=I-D_F^{\mathsf T}(D_FD_F^{\mathsf T})^{-1}D_F
\]
when \(F\ne\varnothing\), while \(P_\varnothing=I\). All these rows are linearly independent, so the inverse exists. For \(1\le j<n\), let \(c^{(j)}_i=0\) for \(i\le j\), and \(c^{(j)}_i=1\) otherwise.

## Proof
**1. Local affine pieces and realization of every active set.** For an input \(a\), the optimality conditions are \(a-z=\lambda D^{\mathsf T}u\), with \(u_i=\operatorname{sign}((Dz)_i)\) on nonzero second differences and \(|u_i|\le1\) on zero second differences. On a stratum with zero-curvature rows \(F\), and a fixed sign vector \(s\) on \(F^c\), the solution is
\[
z=P_F(a-\lambda D_{F^c}^{\mathsf T}s).
\]
Its linear derivative is \(P_F\). Such pieces are continuous and polyhedral, and the map is globally piecewise affine. Every set \(F\) really does occur with strict inequalities: since \(D\) is onto, choose \(z_0\) for which \((Dz_0)_i=0\) on \(F\) and \((Dz_0)_i=1\) on \(F^c\). Choose \(u_i=0\) on \(F\) and \(u_i=1\) on \(F^c\); set \(a_0=z_0+\lambda D^{\mathsf T}u\). These strict complementary conditions persist under small perturbations and yield the indicated derivative \(P_F\) in an open neighborhood of \(a_0\). Hence no formally enumerated face is spurious.

**2. Operator norm via one-jump vectors.** Each \(P_F\) fixes constant vectors. Every \(h\in\mathbb R^n\) has the decomposition
\[
h=h_1\mathbf1+\sum_{j=1}^{n-1}(h_{j+1}-h_j)c^{(j)}.
\]
The triangle inequality thus gives the exact quotient seminorm operator norm
\[
\|P_F\|_{V\to V}=\max_{1\le j<n}V_n(P_Fc^{(j)}),
\]
with each term attained by its one-jump vector. Integrating derivatives along any segment proves the global upper bound by the maximum over \(F\). The preceding open-set realization gives the opposite inequality (choose two sufficiently close inputs separated along the attaining one-jump vector). Therefore
\[
\boxed{\displaystyle\Lambda_n=\max_{F\subseteq\{1,\dots,n-2\}}\max_{1\le j<n}V_n(P_Fc^{(j)}).}
\]
The formula is independent of \(\lambda\) and is finite, exact, and attained by pairs of finite inputs.

**3. Exact dimensions two through eight.** The preceding formula reduces evaluation to finitely many rational matrices: \(2^{n-2}\) active sets, each with \(n-1\) one-jump cuts. Full exact-fraction Gaussian elimination in the standalone checker enumerates *all* these cases for \(2\le n\le8\), with respective maxima
\[
1,\quad1,\quad\frac65,\quad\frac43,\quad\frac75,\quad\frac{28}{19},\quad\frac{11}{7}.
\]
These are exhaustive certificates of finite cases because Step 2 analytically covers every affine piece and norming direction; the code does not extrapolate beyond eight sites. At \(n=4\), one can verify the upper bound by hand: for \(F=\varnothing,\{1\},\{2\},\{1,2\}\), the maximal column variations are respectively \(1,7/6,7/6,6/5\). In addition, for every \(\lambda>0\), input \(a=(0,0,\lambda,\lambda)\) has output
\[
T_{4,\lambda}(a)=\lambda(-1/10,3/10,7/10,11/10),
\]
since the scaled dual multiplier is \(v=\lambda(1/10,-1/10)\), strictly inside the allowed coordinate interval \([-\lambda,\lambda]\). Thus the output variation is \(6\lambda/5\), whereas the input variation is \(\lambda\); take the other input to be zero.

**4. Every-length strict amplification.** For \(F=\{1,\ldots,n-2\}\), \(P_F\) is the ordinary Euclidean affine least-squares projector onto \(\operatorname{span}\{\mathbf1,(1,\ldots,n)\}\). On a step at position \(j\) its projected slope equals
\[
\beta_j=\frac{6j(n-j)}{n(n^2-1)}.
\]
The projected path variation is \((n-1)\beta_j=6j(n-j)/[n(n+1)]\), maximized at \(j=\lfloor n/2\rfloor\). This yields the stated strict lower bound for all \(n\ge4\), tending to \(3/2\). It is achieved locally at every fixed penalty strength by the strict-complementarity construction in Step 1; for the fully active face, sufficiently small single-jump inputs around zero suffice.

## Verification
Reproduce the exact finite table with `python3 check_trend_bv.py` (standard Python library only). It enumerates every subset of curvature rows, inverts each Gram matrix using exact fractions, checks that each projector fixes constants, evaluates every single-jump direction, and verifies the four-site dual witness. It separately verifies the affine lower-bound identity for dimensions four through twenty-five; this last finite test is corroboration of the explicit analytic slope calculation, not a substitute for its proof.

## Relationship to prior work
Kim, Koh, Boyd and Gorinevsky (2009) introduce this second-difference \(\ell_1\) trend-filter criterion, establish its optimization properties and its sparse-approximation formulation; they do not state the two-input first-variation Lipschitz coefficient. Tibshirani (2014), especially Section 1.1, explicitly discusses the previously known active-set and sign representation and focuses on spline structure and statistical rates, not on the sharp adjacent-variation perturbation modulus. The active-set formula here therefore uses familiar generalized-lasso geometry; the claimed distinction is its exact induced variation norms, four-site first amplification, and all-length quantitative lower bound.

Other nearby stability work for quadratic Whittaker smoothing, Euclidean convex-sequence projection, and cyclic running medians concerns different operators or different perturbation norms. None of their reported conclusions logically determines the above constants, even where a small-dimensional threshold happens to coincide.

## Limitations
The exact dimension-by-dimension constants are established only through eight equally spaced, equally weighted real sites. The unrestricted larger-dimensional coefficient is reduced to an exact finite optimization and bounded below but is not given a closed form. This is a mathematical self-review, not an independent audit or a guarantee of absolute historical priority. Unequal observation weights, nonuniform spacing, and other penalty orders are not covered.

## References
1. S.-J. Kim, K. Koh, S. Boyd, D. Gorinevsky, “\(\ell_1\) Trend Filtering,” *SIAM Review* **51** (2009), 339–360. https://doi.org/10.1137/070690274 . Electronic public date: 2009-05-04. Full open manuscript: https://web.stanford.edu/~boyd/papers/pdf/l1_trend_filter.pdf .
2. R. J. Tibshirani, “Adaptive Piecewise Polynomial Estimation via Trend Filtering,” *Annals of Statistics* **42** (2014), 285–323. https://doi.org/10.1214/13-AOS1189 . Full open text: https://www.stat.cmu.edu/~ryantibs/papers/trendfilter-aos.pdf .
