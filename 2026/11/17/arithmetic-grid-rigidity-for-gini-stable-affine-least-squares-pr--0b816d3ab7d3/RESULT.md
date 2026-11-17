# Arithmetic-grid rigidity for Gini-stable affine least-squares projection

## Finding

Let \(n\ge2\) and let \(t_1<\cdots<t_n\) be distinct real observation locations. Write \(P_t:\mathbb R^n\to\mathbb R^n\) for **unweighted affine least-squares fitting at the observed locations**: \(P_ty\) consists of the fitted values of \(a+bt_i\), where \((a,b)\) minimizes \(\sum_{i=1}^n(y_i-a-bt_i)^2\). Equip real signals with the translation-invariant complete-pair Gini seminorm
\[
G(y)=\sum_{1\le i<j\le n}|y_i-y_j|.
\]
Let \(\bar t=n^{-1}\sum_i t_i\), \(c_i=t_i-\bar t\), \(S=\sum_i c_i^2\), and \(B=\sum_{i<j}(t_j-t_i)>0\). The exact, attained two-input Gini Lipschitz coefficient is
\[
\boxed{\displaystyle L(t)=\sup_{G(u-v)>0}\frac{G(P_tu-P_tv)}{G(u-v)}
=\frac B S\max_{1\le k<n}\frac{\sum_{i=n-k+1}^{n}c_i}{k(n-k)}.}
\]
Every maximizing term is realized by the indicator of the final \(k\) observation locations (equivalently, by its complementary initial segment). In particular,
\[
\boxed{L(t)=1\ \Longleftrightarrow\ t_i=\alpha+\beta i\quad(1\le i\le n),\quad\beta>0.}
\]
Thus ordinary affine least-squares regression is Gini-nonexpansive on precisely the equally spaced designs; every strictly increasing nonequispaced design yields a strictly amplifying pair of input signals. For example, \(t=(0,1,2,9)\) has \(L(t)=28/25\), attained by a single positive perturbation at its last observation.

The rigidity has a sharp local form. Write \(r_i=i-(n+1)/2\), fix an arbitrary real perturbation \(h=(h_i)\), put \(w_k=k(n-k)\), and set
\[
 d_k=\frac{\sum_{i=n-k+1}^n(h_i-\bar h)}{k(n-k)},\qquad
 \bar d=\frac{\sum_{k=1}^{n-1}w_kd_k}{\sum_{k=1}^{n-1}w_k}.
\]
For sufficiently small nonzero \(\varepsilon\), the design \(t_i=r_i+\varepsilon h_i\) is still strictly increasing, and
\[
 L(r+\varepsilon h)=\begin{cases}
 1+2\varepsilon(\max_k d_k-\bar d)+O(\varepsilon^2),&\varepsilon\downarrow0,\\
 1+2|\varepsilon|(\bar d-\min_kd_k)+O(\varepsilon^2),&\varepsilon\uparrow0.
 \end{cases}
\]
Both first-order coefficients are strictly positive unless \(h_i\) is affine in the index \(i\). The formula therefore quantifies a linear, generally nonsmooth stability penalty for any genuinely irregular perturbation of an arithmetic sampling grid.

## Assumptions and scope

All observations have equal positive least-squares weights, locations are strictly ordered and real, and the seminorm sums **all unordered pairs** with unit weights. The operator is an affine-function projection on the observed vector, not a local windowed convolution or an estimator evaluated between observations. The coefficient concerns arbitrary pairs of real response vectors, and constants are quotiented automatically because \(G(y)=0\) exactly for constant vectors. For \(n=2\) all ordered designs are arithmetic progressions and the fit is the identity.

## Proof

**1. Regression identity.** The normal equations give
\[
 (P_ty)_i=\bar y+\frac{\sum_{j=1}^n c_j y_j}{S}\,c_i.
\]
Since \(t\) is strictly increasing, the complete-pair dispersion of the output is
\[
 G(P_ty)=\frac B S\left|\sum_{j=1}^n c_j y_j\right|.
\]
This also shows that \(P_t\) fixes \(t\) and every constant vector.

**2. Exact dual cut norm.** For any coefficient vector \(c\) with \(\sum c_i=0\), let
\[
 M(c)=\max_{\varnothing\ne A\subsetneq\{1,\ldots,n\}}
 \frac{|\sum_{i\in A}c_i|}{|A|(n-|A|)}.
\]
Order the coordinates of any \(y\) increasingly. The elementary layer-cake decomposition expresses \(y\), modulo a constant vector, as a nonnegative linear combination of proper-subset indicators. For any such indicator, \(G(\mathbf1_A)=|A|(n-|A|)\). The same decomposition yields \(G(y)\) as the corresponding positive linear combination of these crossing counts. By the triangle inequality, \(|\sum c_i y_i|\le M(c)G(y)\); taking an indicator for a maximizing set gives equality. Since \(c_1<\cdots<c_n\), for fixed cardinality \(k\) the largest subset sum is the final-\(k\) sum. A negative maximizing sum is the positive sum of the complementary subset, with the same denominator. Thus
\[
 M(c)=\max_{1\le k<n}\frac{\sum_{i=n-k+1}^{n}c_i}{k(n-k)}.
\]
Combining this with Step 1 proves the claimed exact formula and all its binary-cut sharpness statements.

**3. Unique nonexpansive designs.** The projection is not the zero operator modulo constants and fixes the nonconstant vector \(t\). Therefore \(L(t)\ge1\). If \(L(t)=1\), the linear functional \(y\mapsto\sum_i c_i y_i\) satisfies
\[
 \sum_i c_i y_i\le\frac S B G(y)
 \quad\hbox{for all real }y,
\]
with equality at \(y=t\). Because every pair of components of \(t\) is distinct, \(G\) is differentiable at \(t\), with gradient \((2i-n-1)_{i=1}^n\). Equality in the supporting-functional inequality forces
\[
 c_i=\frac S B(2i-n-1),
\]
so the design is arithmetic. Conversely, for \(t_i=\alpha+\beta i\), direct summation gives
\[
 B=\beta\frac{n(n^2-1)}6,\qquad
 S=\beta^2\frac{n(n^2-1)}{12},\qquad
 \sum_{i=n-k+1}^n c_i=\frac\beta2 k(n-k).
\]
Step 2 then yields \(L(t)=1\). This proves the equivalence without extrapolation or generic-position assumptions beyond distinct sampling locations.

**4. First-order departure from equal spacing.** Set \(t=r+\varepsilon h\). For sufficiently small \(\varepsilon\), the order of the locations is unchanged. The cut ratios in Step 2 are exactly \(1/2+\varepsilon d_k\). Thus their maximum is \(1/2+\varepsilon\max d_k\) for positive \(\varepsilon\), or \(1/2+\varepsilon\min d_k\) for negative \(\varepsilon\). The identities
\[
 \sum_{k=1}^{n-1}w_k=\frac{n(n^2-1)}6,
 \qquad \sum_{k=1}^{n-1}w_kd_k=\sum_i r_i h_i
\]
and \(B(r)=2S(r)\) imply, by direct differentiation,
\[
 \frac{B(r+\varepsilon h)}{S(r+\varepsilon h)}
 =2-4\varepsilon\bar d+O(\varepsilon^2).
\]
Multiplication gives both displayed local formulas. Finally, all \(d_k\) are equal if and only if \(\sum_{i=n-k+1}^n(h_i-\bar h)\) is proportional to \(k(n-k)\) for every \(k\). Taking successive differences proves that this is equivalent to \(h\) being affine in the observation index. Otherwise the strict weighted-average inequalities \(\min d_k<\bar d<\max d_k\) prove strictly positive one-sided penalties.

## Verification

An accompanying standard-library Python checker (`code/check_exact.py`) computes the regression projection and all proper binary-cut ratios using exact fractions. It compares the full cut maximum with the closed formula on representative arithmetic and irregular rational grids from two through eight sites, checks the operator bound on all ternary input vectors for these grids, tests the exact norm-one rigidity and the perturbation derivative identities, and verifies the rational witness \(28/25\). Execute with `python code/check_exact.py`. The proof above, rather than the finite tests, establishes the formula for all real designs and all dimensions.

## Relationship to prior work

Classical least-squares curve fitting describes the projection and its ordinary Euclidean statistical performance; the six-page Rust (2001) primary exposition was read for the normal equations, conditioning and statistical variance sections, and does not state a complete-pair Gini induced norm. Savitzky and Golay (1964) motivate least-squares smoothing of noisy measured data, but their original paper's inspected motivation and filtering section do not formulate this all-pair response-distance stability question. Gerstenberger and Vogel (arXiv:1405.5027v1, 2014) introduce the empirical Gini mean difference and analyze its statistical efficiency and influence function; their full-text definitions and efficiency discussion concern a scalar dispersion estimator, not operator norms of fitted responses.

The closest published Gini/variance result, *Sharp mass-sensitive finite-atomic Gini–variance bound* (2026), proves a universal variance-dispersion bound with an equal-spacing equality case for uniform masses. Its full RESULT statement was examined. That is a **different optimization** (maximizing a Gini-to-standard-deviation ratio over atomic supports), and does not give the exact norm of the affine least-squares projector, its worst binary response perturbations, or the two-sided linear stability defect when the sampling design is irregular. Nearby published affine-projection results in \(L^\infty\) or on metric spaces concern different geometries. Berztiss's 1964 paper on least-squares fitting of irregularly spaced data is a closely relevant historical title whose accessible bibliography and source description do not resolve whether it treats the present Gini operator seminorm; its unexamined full text remains a specific priority risk. These distinctions do not establish historical uniqueness.

## Limitations

The theorem is deterministic and concerns unweighted linear regression at fixed, pairwise distinct observation locations. It does not assert stability for weighted least squares, repeated design points, higher polynomial degrees, local polynomial smoothers, the residual map, or other pairwise dispersion weights. The comparisons of older irregular-design literature are not exhaustive, and historical novelty should be checked independently. The local expansion is for a fixed finite dimension and a fixed perturbation direction; no dimension-uniform error estimate is claimed.

## References

1. A. Savitzky and M. J. E. Golay, “Smoothing and Differentiation of Data by Simplified Least Squares Procedures,” *Analytical Chemistry* 36 (1964), 1627–1639. DOI: 10.1021/ac60214a047. Original article reprinted as Appendix A of Stanford RSL Technical Report 70-11, June 1970 (NASA report 19700027052).
2. B. W. Rust, “Fitting Nature's Basic Functions I: Polynomials and Linear Least Squares,” *Computing in Science & Engineering* 3(5) (2001), 86–91. Open original PDF: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=150831.
3. C. Gerstenberger and D. Vogel, “On the Efficiency of Gini's Mean Difference,” arXiv:1405.5027v1, first public preprint 20 May 2014; later published in *Statistical Methods & Applications* 24 (2015), 569–596.
4. A. T. Berztiss, “Least Squares Fitting of Polynomials to Irregularly Spaced Data,” *SIAM Review* 6(3) (1964), 203–227. DOI: 10.1137/1006059 (full text not accessed).
5. “Sharp mass-sensitive finite-atomic Gini–variance bound,” published research record, 4 October 2026, identifier `2026/10/4/SCOPE-sharp-mass-sensitive-finite-atomic-gini-variance-bound--cc38c112bff2`, RESULT text inspected.
