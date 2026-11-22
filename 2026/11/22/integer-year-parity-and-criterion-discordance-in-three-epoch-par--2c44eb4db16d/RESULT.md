# Integer-year parity and criterion discordance in three-epoch parallax design

## Finding
Fix an integer baseline \(K\geq1\) measured in years. In the ideal scalar astrometric model
\[
Y(s)=a+bs+\varpi\cos(2\pi s)+\epsilon_s,
\qquad s\in\{0,t,K\},
\]
with unknown position \(a\), proper motion \(b\), and parallax amplitude \(\varpi\), let the independent errors have common normal distribution \(N(0,\sigma^2)\), where \(\sigma>0\). The first and last observing epochs are fixed; the one interior epoch \(t\) can be chosen anywhere in \((0,K)\).

**Theorem (complete minimum-variance three-epoch schedule).** Among identifiable schedules, the variance of the unbiased least-squares parallax estimate is
\[
V_K(t)=\sigma^2\frac{1+(1-t/K)^2+(t/K)^2}{[1-\cos(2\pi t)]^2}.
\]
For **odd** \(K\), the unique global minimizer is \(t=K/2\), and the minimum is exactly \(3\sigma^2/8\). For **even** \(K\), exactly two schedules minimize this variance, at
\[
t=K/2-v_K\quad\text{and}\quad t=K/2+v_K,
\]
where the unique \(v_K\in(0,1/2)\) solves
\[
\pi\cot(\pi v_K)=\frac{v_K}{3K^2/2+2v_K^2}.
\]
The optimal even-baseline variance is strictly greater than \(3\sigma^2/8\), decreases strictly along even integer baselines, and converges to \(3\sigma^2/8\). Moreover,
\[
v_K=\frac12-\frac{1}{3\pi^2K^2}+O(K^{-4})
\quad\text{as even }K\to\infty.
\]

For the *joint three-parameter* \(D\)-optimal determinant criterion, every half-integer middle epoch \(t\in(0,K)\) is optimal. Consequently the parallax-variance and full-determinant criteria share their unique parallax-variance-optimal epoch for odd \(K\), but **no parallax-variance-optimal epoch is \(D\)-optimal for even \(K\)**. Increasing the endpoint baseline from any odd integer to the next even integer strictly worsens the best achievable parallax variance with only one freely placed interior epoch, although the chronological baseline becomes longer.

For a two-year baseline, the middle epochs are approximately \(0.507690622172\) and \(1.492309377828\) years, with minimum variance \(0.405769566441\sigma^2\). By contrast the one-year baseline achieves \(0.375\sigma^2\); the exactly central epoch at one year in the two-year design contains no identifiable parallax information.

## Assumptions and scope
The annual parallax factor is one precisely phase-registered cosine in a single known measurement direction. Observations have the same scalar noise variance and errors are independent. No correlated reference-frame errors, field-registration parameters, projection-angle changes, source acceleration, source multiplicity, irregular Earth orbit, or visibility restrictions are included. The first and last times are \(0\) and the integer \(K\), so they have the same parallax factor. The result concerns a three-observation, fixed-endpoints, parallax-variance objective; it is not a global optimum over arbitrary numbers of observations or instruments.

A time is identifiable precisely when \(1-\cos(2\pi t)\ne0\). At integer \(t\) all three rows have the same annual phase; the parallax column is then confounded with the position column, so no finite-variance unbiased parallax estimator exists in this model.

## Proof
1. **Eliminate the nuisance parameters.** The contrast
\[
Z_t=Y(t)-(1-t/K)Y(0)-(t/K)Y(K)
\]
cancels both the constant and linear terms. Because \(K\) is an integer, the two endpoint parallax factors equal one. Thus
\[
\mathbb E Z_t=\varpi[\cos(2\pi t)-1],\qquad
\operatorname{Var}(Z_t)=\sigma^2[1+(1-t/K)^2+(t/K)^2].
\]
When identifiable, division by the nonzero parallax coefficient gives the claimed variance. The full \(3\times3\) design matrix is nonsingular with determinant \(K[1-\cos(2\pi t)]\). Its exact inverse gives the same contrast estimator. In the normal linear model it attains the Cramér–Rao information bound for parallax with the other two parameters unknown, establishing the minimum variance within the stated estimation model.

2. **Universal bound.** Put \(v=t-K/2\). The noise multiplier is
\[
D_K(v)=\frac32+\frac{2v^2}{K^2}\ge\frac32,
\]
with equality only at \(v=0\); the absolute parallax contrast is at most two. Every identifiable schedule therefore has variance at least \(3\sigma^2/8\), and equality requires simultaneously \(v=0\) and opposite annual parallax phase.

3. **Odd baselines.** When \(K\) is odd, \(\cos(2\pi(K/2))=-1\). Thus the centered observation achieves both equalities in step 2. Any other \(t\) has strictly larger noise multiplier and cannot tie. This proves uniqueness and the exact variance.

4. **Even baselines and globality.** When \(K\) is even, \(\cos(2\pi(K/2+v))=\cos(2\pi v)\). By symmetry it suffices to consider \(v\ge0\). Every \(v>1/2\) has a \(w\in[0,1/2]\) with the same cosine and \(w<v\), obtained by distance to the nearest integer. Hence its parallax contrast is unchanged and its noise multiplier is strictly larger: it cannot be optimal when its contrast is nonzero. On \((0,1/2]\), maximizing inverse variance is equivalent to maximizing
\[
F_K(v)=\frac{[1-\cos(2\pi v)]^2}{3/2+2v^2/K^2}.
\]
Its logarithmic derivative on \((0,1/2)\) has the sign of
\[
\pi\cot(\pi v)-\frac{v}{3K^2/2+2v^2}.
\]
The first term strictly decreases from \(+\infty\) to zero. The second strictly increases there, since its derivative has numerator \(3K^2/2-2v^2>0\) for even \(K\ge2\). There is exactly one zero \(v_K\), and the derivative crosses from positive to negative. Since \(F_K(0)=0\) and the derivative is negative near \(1/2\), that zero is the unique maximizer for positive offsets; reflection provides exactly two global optimal observing times.

5. **Parity loss, monotonicity and expansion.** For even \(K\) the zero-offset time gives no parallax contrast, while every nonzero offset has noise multiplier strictly greater than \(3/2\). Consequently the universal lower variance bound is unattainable. For two even integers \(K_2>K_1\), at each fixed \(v\in(0,1/2]\), \(F_{K_2}(v)>F_{K_1}(v)\). Evaluating at a maximizing positive \(v\) proves the strict improvement along even baselines. The universal upper information bound is approached as \(K\to\infty\) by choosing \(v=1/2\). Writing \(v_K=1/2-\delta_K\) in the stationarity equation and expanding \(\cot(\pi(1/2-\delta))=\tan(\pi\delta)\) proves \(\delta_K=(3\pi^2K^2)^{-1}+O(K^{-4})\).

6. **Joint-determinant comparison.** The squared determinant of the full design matrix equals \(K^2[1-\cos(2\pi t)]^2\), which has its global maximum at each allowed half-integer \(t\). For odd \(K\), the centered parallax-variance optimum is half-integer. For even \(K\), the two variance optima have offsets strictly between zero and one-half from an integer center, hence cannot be half-integer. The strict increase in variance on moving from an odd baseline to the next even baseline follows from steps 3 and 5.

## Verification
Run `python3 verify.py` from this package's extracted directory. The standalone standard-library checker tests the exact nuisance-cancellation identity, rational half-integer benchmark values, uniqueness and symmetry of computed even roots, exhaustive *sample-grid* comparisons over many integer baselines, monotonicity and asymptotics. It reports `PASS 124806 deterministic assertions; no infinite-proof claim.` These finite checks are corroboration; the all-integer claims are established by the analytical proof above. The two-year numerical root and variance were also evaluated independently with scalar bracketing.

## Relationship to prior work
Riess and colleagues' 2014 space-based astrometry study states the classical three-parameter position/motion/parallax model and describes half-year opposite-parallax observing epochs as effective, while using five actual epochs and accounting for additional registration parameters. It does not present an exact fixed-endpoint, three-observation **marginal parallax variance** minimization or the even/odd baseline theorem. Michalik and colleagues' 2015 Gaia study develops least squares and Bayesian regularization for a *five-parameter* sparse-observation model, not the constrained three-observation optimization here. The AllWISE technical supplement discusses annual-phase aliasing and three-epoch motion measurements, without a global precision-optimal scheduling theorem. Broad experimental-design methods may algorithmically subsume special design problems, but a specific stronger published all-integer theorem was not identified in the sources inspected.

## Limitations
This result has not undergone independent validation or been established as historically first in the broad experimental-design literature. The variance comparison is for one projected coordinate with ideal equal precision and fully known annual phase, not a practical Gaia/HST full astrometric solution. The small c-optimal shift relative to an exact half-year excursion improves the two-year variance by only about \(0.1184\%\); the larger structural lesson is complete aliasing at a centrally placed two-year visit and the precise dependence on endpoint parity. Neither operational visibility nor calibration errors are modeled.

## References
- A. G. Riess, S. Casertano, J. Anderson, J. MacKenty, and A. V. Filippenko, *Parallax Beyond a Kiloparsec from Spatially Scanning the Wide Field Camera 3 on the Hubble Space Telescope*, arXiv:1401.0484v1, first publicly posted January 2, 2014, https://arxiv.org/abs/1401.0484 .
- D. Michalik, L. Lindegren, D. Hobbs, and A. G. Butkevich, *Gaia astrometry for stars with too few observations — a Bayesian approach*, arXiv:1507.02963, first publicly posted July 10, 2015, https://arxiv.org/abs/1507.02963 .
- NASA/IPAC, *AllWISE Explanatory Supplement*, section II.6, https://irsa.ipac.caltech.edu/data/WISE/docs/release/AllWISE/expsup/sec2_6.html .
- H. T. Banks and K. L. Rehm, *Experimental design for vector output systems*, published online May 17, 2013, https://doi.org/10.1080/17415977.2013.797973 (general design context; comparison based on accessible article material).
