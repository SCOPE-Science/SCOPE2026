# Sharp random-jump risk and monotone Romberg variance inflation on nested grids

## Finding
For a step function with one uniformly unknown jump on the unit interval, observations on nested uniform grids give an exact covariance law: fine- and coarse-trapezoid errors are correlated as though the coarser error had been replaced by the finer one. Consequently the ordinary finest-grid composite trapezoid is the unique minimum-mean-square estimator of the integral from *all* its sampled values, even against nonlinear or independently randomized estimators. Integer-ratio Richardson–Romberg extrapolation has a precisely computable larger mean-square error (MSE); the ratio to the finest-grid trapezoid's MSE increases **strictly at every extrapolation depth**, approaching a finite explicit limit. At dyadic refinement the limit is approximately \(1.62599155521054\).

More precisely, let \(C\) be uniform on \((0,1)\), let \(f_C(x)=\mathbf1_{\{x>C\}}\), and let \(I(C)=\int_0^1 f_C(x)\,dx=1-C\). Define the uniform composite trapezoid \(T_N\) with \(N\ge1\) equal panels. For any positive integers \(N_0>N_1>\cdots>N_m\) satisfying \(N_{j+1}\mid N_j\), put \(h_j=1/N_j\). Then
\[
 \operatorname{Cov}(T_{N_i}-I,T_{N_j}-I)
 =\frac{\min\{h_i,h_j\}^{2}}{12}.
\]
For real coefficients \(b_j\) with \(\sum_{j=0}^m b_j=1\), the exact risk of \(Q=\sum_j b_jT_{N_j}\) is
\[
 \mathbb E[(Q-I)^2]
 =\frac{h_0^2}{12}
 +\frac1{12}\sum_{k=1}^m(h_k^2-h_{k-1}^2)
                 \left(\sum_{j=k}^m b_j\right)^2.
 \tag{1}
\]
Equality with the finest-grid risk holds **only** for \((b_0,b_1,\ldots,b_m)=(1,0,\ldots,0)\). The same minimum \(h_0^2/12\) holds among *all* measurable finite-risk estimators from the finest-grid sample vector, with uniqueness up to null sets; independent external randomization cannot reduce it.

For the usual geometric Romberg grid, fix an integer refinement factor \(r\ge2\), an extrapolation depth \(m\ge0\), and \(s\ge1\). Put \(N_j=s r^{m-j}\), \(h=1/(sr^m)\), \(q=r^{-2}\), and
\[
 P_j(q)=\prod_{\ell=1}^{j}(1-q^\ell),\qquad P_0(q)=1.
\]
The unique Richardson coefficients cancelling the first \(m\) even-power trapezoid errors, in **finest-to-coarsest order**, are
\[
 a_{m,j}=\frac{(-1)^j q^{j(j+1)/2}}{P_j(q)P_{m-j}(q)},
 \qquad 0\le j\le m.
\]
Let \(Q_m=\sum_{j=0}^m a_{m,j}T_{sr^{m-j}}\) and \(S_{m,k}=\sum_{j=k}^{m}a_{m,j}\). Its exact phase-averaged risk is
\[
 \mathbb E[(Q_m-I)^2]=\frac{h^2}{12}\mathcal C_m(r),\qquad
 \mathcal C_m(r)=1+(r^2-1)\sum_{k=1}^{m}r^{2(k-1)}S_{m,k}^2.
 \tag{2}
\]
For **every** integer \(r\ge2\),
\[
 1=\mathcal C_0(r)<\mathcal C_1(r)<\mathcal C_2(r)<\cdots
 <\mathcal C_\infty(r)<\infty,\qquad
 \mathcal C_1(r)=\frac{r^2}{r^2-1}.
 \tag{3}
\]
Writing \(P_\infty(q)=\prod_{\ell\ge1}(1-q^\ell)>0\), the finite limit is explicitly
\[
 S_{\infty,k}=
 \frac1{P_\infty(q)}\sum_{j=k}^{\infty}
  \frac{(-1)^j q^{j(j+1)/2}}{P_j(q)},\qquad
 \mathcal C_\infty(r)=1+(1-q)
 \sum_{k=1}^\infty q^{-k}S_{\infty,k}^2.
 \tag{4}
\]
At \(r=2\), the first normalized MSE factors are \(\mathcal C_0=1\), \(\mathcal C_1=4/3\), \(\mathcal C_2=208/135\), with limit approximately \(1.625991555210539\). The increase compares each Romberg rule with **its own** finest-grid trapezoid. It does not assert that the *absolute* error rises when the entire mesh is refined at fixed initial panel count.

## Assumptions and scope
All samples are exact real values; the single jump location is sampled uniformly once from \((0,1)\), independently of any auxiliary estimator randomization. The jump height is fixed at one and the sample values tell only which finest-grid panel contains the jump. Events in which \(C\) lands on a grid node have probability zero and may be defined arbitrarily. The grid ratios in the first assertion are integer and nested; the Romberg refinement factor in (2)–(4) is an integer at least two. Normalization uses the realized finest spacing \(h\) for each depth. Assertions cover all integers \(m\ge0\), \(s\ge1\), and \(r\ge2\).

## Proof
**Step 1: exact Bernoulli phase and covariance.** For almost every \(C\), direct counting of sample values gives
\[
 T_N[f_C]-(1-C)=\frac1N B_1(\{NC\}),\qquad
 B_1(u)=u-\tfrac12,\quad 0<u<1.
\]
This phase error has mean zero and variance \(1/(12N^2)\). If \(N_f=dN_c\) for a positive integer \(d\), write the coarse phase \(U=\{N_cC\}\), which is uniform on \((0,1)\). The fine phase equals \(\{dU\}\). Splitting \((0,1)\) into \(d\) intervals shows
\[
 \int_0^1 B_1(u)B_1(\{du\})\,du=\frac1{12d}.
\]
Indeed, on interval \(u=(v+k)/d\), \(k=0,\ldots,d-1\), the integrand is \(((v+k)/d-1/2)(v-1/2)\); the constant-in-\(v\) part integrates to zero and the remaining quadratic has integral \(1/(12d)\) after summation. Multiplication by \(h_ch_f\) yields \(h_f^2/12\), proving the covariance formula.

**Step 2: the variance increments and conditional optimality.** Let \(E_j=T_{N_j}-I\) and \(D_0=E_0\), \(D_j=E_j-E_{j-1}\) for \(j\ge1\). The covariance law makes these increments pairwise uncorrelated and gives \(\operatorname{Var}(D_0)=h_0^2/12\) and \(\operatorname{Var}(D_j)=(h_j^2-h_{j-1}^2)/12\). Because \(\sum_jb_j=1\), the error of \(Q\) is \(D_0+\sum_{k=1}^m(\sum_{j=k}^m b_j)D_k\). This proves (1) and strictness for every nonzero coarse-grid coefficient. Conditioning on the entire finest-grid sample vector identifies one finest cell of width \(h_0\); the posterior of \(C\) is uniform within it. The posterior conditional mean of \(I=1-C\) is precisely the midpoint estimate \(T_{N_0}\), and its conditional variance is \(h_0^2/12\). The \(L^2\) conditional-projection identity makes it the unique Bayes MSE minimizer among all square-integrable sample-based estimators, and additional independent randomness adds nonnegative conditional variance.

**Step 3: Richardson coefficients and exact Romberg risk.** The \(m+1\) extrapolation nodes in the even-power error variable are \(1,r^2,\ldots,r^{2m}\). Lagrange interpolation at zero gives the displayed \(a_{m,j}\); in particular \(\sum_j a_{m,j}=1\) and \(\sum_j a_{m,j}r^{2\ell j}=0\) for \(1\le\ell\le m\). Substituting \(h_k=r^kh\) into (1) yields (2).

**Step 4: strictly increasing tail magnitudes.** Write \(A_{m,j}=|a_{m,j}|\). For \(0\le j<m\),
\[
 \frac{A_{m,j+1}}{A_{m,j}}
 =\frac{q^{j+1}(1-q^{m-j})}{1-q^{j+1}}
 \le\frac{q}{1-q}<1.
\]
Thus the alternating tail \(S_{m,k}=\sum_{j=k}^m(-1)^jA_{m,j}\) is nonzero and has sign \((-1)^k\). For the transition \(m\to m+1\), set
\[
 d_j=A_{m+1,j}-A_{m,j}
 =A_{m,j}\frac{q^{m+1-j}}{1-q^{m+1-j}},\quad 0\le j\le m,
 \qquad d_{m+1}=A_{m+1,m+1}.
\]
For \(1\le j<m\),
\[
 \frac{d_{j+1}}{d_j}
 =\frac{q^j(1-q^{m+1-j})}{1-q^{j+1}}<1,
\]
and \(d_{m+1}/d_m=q^m(1-q)/(1-q^{m+1})<1\) when \(m\ge1\). Hence for every \(1\le k\le m+1\), the new-minus-old tail is an alternating sequence of *strictly decreasing* positive magnitudes beginning with sign \((-1)^k\):
\[
 S_{m+1,k}-S_{m,k}=\sum_{j=k}^{m+1}(-1)^jd_j
 \quad\bigl(S_{m,m+1}:=0\bigr).
\]
Consequently \(|S_{m+1,k}|>|S_{m,k}|\) for \(k\le m\), while the newly added \(S_{m+1,m+1}\ne0\). Every term of (2) therefore increases strictly. For \(m=0\), \(S_{1,1}=-q/(1-q)\ne0\), so the conclusion includes the first step. Direct substitution gives \(\mathcal C_1=1/(1-q)\), proving strict monotonicity in (3).

**Step 5: a finite explicit limit.** Since \(0<q\le1/4\), \(P_\infty(q)>0\) and
\[
 |a_{m,j}|\le\frac{q^{j(j+1)/2}}{P_\infty(q)^2}
\]
uniformly for \(m\ge j\). Thus \(S_{m,k}\) is bounded by a uniform superexponentially decaying tail in \(k\). For each fixed \(j\), \(a_{m,j}\to(-1)^jq^{j(j+1)/2}/(P_j(q)P_\infty(q))\). Dominated convergence proves (4), and the summable tail bound proves its finiteness. Exact-rational evaluation gives \(\mathcal C_2(2)=208/135\); convergent high-precision evaluation of (4) gives the displayed limit approximation.

## Verification
The standalone standard-library script `artifacts/verify.py` checks the coefficients' cancellation identities, (1) and (2), direct piecewise-exact integration over jump locations, covariance on non-geometric nested grids, and strict tail behavior for bounded test families. Running `python artifacts/verify.py` produces `PASS 375 exact-rational assertions`. These finite checks are **not** proofs of the all-depth assertions, which follow from Steps 1–5. The dyadic infinite-limit decimal is an approximation, not a claim of certified enclosure; formula (4) is exact.

## Relationship to prior work
Romberg's even-power cancellation and the discontinuity-sensitive Euler–Maclaurin remainder are classical. Berrut and Trummer [2] analyze extrapolation using discontinuous functions and **known jump locations**, where appropriate correction can accelerate convergence. The current claim instead fixes an unknown uniformly distributed jump and asks for exact uncorrected MSE and the all-depth extrapolation penalty. Wu [1] studies randomized trapezoidal quadrature for continuous fractional-Sobolev functions; its randomized nodes and smoothness assumptions are different. Camargo [3] and the published positive-weight generalized Romberg theorem [4] concern collected sample weights and sup-norm sample perturbation bounds, not an unknown jump's correlated phase errors. In particular, positive final sample weights do **not** imply MSE optimality against the finest-grid trapezoid for this statistical model. The elementary conditional-mean optimality observation is not presented as separately novel; the assessed mathematical contribution is the exact nested covariance together with the strict, all-depth Romberg penalty and limit.

## Limitations
This is a model-specific average over a *uniformly random* single jump, not a worst-case discontinuity result or a general error theorem for smooth or multijump integrands. Nonuniform jump distributions, noise in function values, nonnested grids, unknown jump height, adaptive sampling, and location-aware jump corrections are not covered. The variance factor compares algorithms sharing their finest grid, not their work budgets at changing depth. Historical general-error analyses of Romberg quadrature may contain equivalent special cases; their exhaustive exclusion is not asserted. The conditional-mean property relies crucially on having only values of this step family at fixed grid nodes.

## References
1. Yue Wu, *A randomised trapezoidal quadrature*, arXiv:2011.15086, first publicly posted November 30, 2020. https://arxiv.org/abs/2011.15086
2. Jean-Paul Berrut and Manfred R. Trummer, *Extrapolation quadrature from equispaced samples of functions with jumps*, Numerical Algorithms 92 (2023), 65–88, first online December 19, 2022. https://doi.org/10.1007/s11075-022-01462-0
3. A. Camargo, *A Chebyshev–Markov–Stieltjes separation type theorem for classical Romberg quadrature*, Numerical Algorithms 91 (2022). https://doi.org/10.1007/s11075-022-01393-w
4. *Positive-weight generalized Romberg quadrature for every integer refinement factor*, mathematical research record, September 21, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/9/21/SCOPE-generalized-romberg-positive-weights-integer-refinement--b7c2819b6648
