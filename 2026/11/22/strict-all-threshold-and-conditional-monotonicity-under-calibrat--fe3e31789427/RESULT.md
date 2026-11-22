# Strict all-threshold and conditional monotonicity under calibrated Brownian batch resetting

## Finding

Fix a population of \(N\ge2\) independent \(d\)-dimensional Brownian particles, each with diffusivity \(D>0\). At independent Poisson events, uniformly choose exactly \(m\in\{1,\ldots,N\}\) labels and reset those particles to the origin. **Calibrate the global event rate to \(r_m=\lambda N/m\)**, so every individual particle has the same reset rate \(\lambda>0\) for every batch size; the total expected reset operations per unit time also stay fixed at \(r_m m=\lambda N\). Start every position at the origin, observe at any \(t>0\), or take the stationary limit \(t=\infty\). For distinct tagged particles let \(Y_i(t)=\|X_i(t)\|^2\).

**Theorem.** When \(m\) increases, the entire bivariate law of \((Y_1(t),Y_2(t))\) increases in supermodular (equivalently, with the fixed marginals, concordance) order. For any \(m_1<m_2\), every \(x,y>0\), and each \(t\in(0,\infty]\), the strict inequality
\[
\Pr_{m_1}\{Y_1(t)>x,Y_2(t)>y\}<\Pr_{m_2}\{Y_1(t)>x,Y_2(t)>y\}
\]
holds, although the individual laws of \(Y_1(t)\) and \(Y_2(t)\) do not depend on \(m\). For \(m>1\) the conditional tail \(z\mapsto\Pr_m\{Y_2(t)>y\mid Y_1(t)=z\}\) is **strictly increasing** for every \(y,z>0\); for \(m=1\) it is constant. A sharp boundary of this ordering is that the corresponding *signed* positions are not ordered in concordance when \(m\) changes: positive-positive quadrant probabilities increase, whereas positive-negative-threshold quadrant probabilities decrease.

Let \(c_m=\lambda(m-1)/(N-1)\). With \(h_x(u)=\Pr\{2Du\,\chi_d^2>x\}\) for \(u>0\), and \(h_x(0)=0\), the all-threshold increase is quantified exactly by
\[
\begin{aligned}
&\Pr_{m_2}\{Y_1>x,Y_2>y\}-\Pr_{m_1}\{Y_1>x,Y_2>y\}\\
&\quad=\int_0^t\!\int_0^t h'_x(u)h'_y(v)e^{-\lambda(u+v)}\bigl(e^{c_{m_2}\min(u,v)}-e^{c_{m_1}\min(u,v)}\bigr)\,dv\,du>0.
\end{aligned}
\]
Here integrals with \(t=\infty\) are improper convergent integrals, and \(\chi_d^2\) is chi-square with \(d\) degrees of freedom. The known stationary energy covariance is recovered as a consistency check:
\[
\operatorname{Cov}(Y_1,Y_2)=\frac{4D^2d^2c_m}{\lambda^2(2\lambda-c_m)},\qquad
\operatorname{Corr}(Y_1,Y_2)=\frac{d\,c_m}{(d+4)(2\lambda-c_m)}.
\]
The last two formulas are not separately claimed as novel.

## Assumptions and scope

The Brownian drivers of distinct particles are independent; batch selections at successive Poisson events are uniform, independent of motion and of each other; all selected coordinates reset to the origin, not partially. The observation time \(t\) is common, with deterministic zero initial positions for finite \(t\). The theorem includes \(m=1\), \(m=N\), \(N=2\), all integer spatial dimensions \(d\ge1\), and all positive \(D,\lambda\). Supermodular ordering means that for every bounded smooth test \(f\) with nonnegative mixed derivative, \(\mathbb Ef(Y_1,Y_2)\) is nondecreasing in \(m\), equivalently for integrable supermodular tests for which expectations exist. Strictness is asserted for the stated positive-threshold tails and strictly increasing conditional tails, not every nonconstant supermodular test. Results do not address different initial configurations, non-Poisson reset clocks, or interacting particles.

## Proof

**1. Exact common-shock ages.** For two tagged labels, thinning the marked Poisson reset events yields three independent Poisson clocks: resetting both with rate \(c=c_m\), only label 1 with rate \(\lambda-c\), and only label 2 with the same rate. The remaining events affect neither label. In a two-sided equilibrium clock construction, independent backward waiting times \(E_0,E_1,E_2\) for these clocks give
\[
A_1=\min(t,E_0,E_1),\qquad A_2=\min(t,E_0,E_2).
\]
A zero-rate clock is interpreted as waiting time \(\infty\). This representation is also exact at finite \(t\) when all positions began at zero. For \(0\le u,v<t\),
\[
\Pr\{A_1>u,A_2>v\}
=e^{-\lambda(u+v)+c\min(u,v)},\qquad
\Pr\{A_i>u\}=e^{-\lambda u}.
\]
The bivariate survival increases strictly in \(c\) whenever \(u,v>0\) while marginals stay fixed. Since \(c_m\) increases strictly in \(m\), the age pairs are increasingly concordant. The diagonal singular component of the stationary age distribution is permitted; at finite \(t\), an additional common atom at the horizon is permitted.

**2. Brownian mixing preserves the complete order.** At the observation time, independent post-reset Brownian increments imply the distributional representation
\[
Y_i=2D A_i Z_i,\qquad Z_1,Z_2\stackrel{\mathrm{iid}}\sim\chi_d^2,
\]
with the \(Z_i\) independent of the reset clocks. For any \(x>0\), the function \(h_x(u)=\Pr\{2DuZ_i>x\}\) is zero at \(u=0\) and strictly increasing for \(u>0\). Writing \(s=d/2\) and \(w=x/(4Du)\), its derivative is
\[
h'_x(u)=\frac{w^s e^{-w}}{u\,\Gamma(s)}>0.
\]
By the layer-cake identity, \(\mathbb E[h_x(A_1)h_y(A_2)]\) equals the double integral of \(h'_x(u)h'_y(v)\Pr(A_1>u,A_2>v)\). Subtracting at two shared-clock rates gives the displayed strictly positive exact formula. To extend from threshold indicators to all smooth supermodular tests, note that conditional on positive independent \(Z_1,Z_2\), the function \((a,b)\mapsto f(2DZ_1 a,2DZ_2 b)\) remains supermodular. Integration over the \(Z_i\) preserves this property. The fixed-marginal age survival ordering yields the asserted supermodular order; truncation gives the integrable extension.

**3. Strict conditional predictability.** For \(c>0\), conditioning on a reset age \(A_1=a\in(0,t)\) yields, for \(0<b<t\) away from \(b=a\),
\[
K_c(a,b):=\Pr\{A_2>b\mid A_1=a\}=
\begin{cases}
(1-c/\lambda)e^{-\lambda b+ca},&a<b,\\
e^{-(\lambda-c)b},&a>b.
\end{cases}
\]
At the endpoint atom \(A_1=t\) the second branch holds for \(b<t\). This is obtained by considering whether the most recent reset of label 1 was an exclusive or a common reset; the exclusive probability conditional on a reset of label 1 is \(1-c/\lambda\). For each \(b>0\), the kernel is nondecreasing in \(a\), including its upward jump when \(a\) crosses \(b\). Moreover, for any \(a_1<a_2\) in the age support and any \(b\in(a_1,a_2)\), \(K_c(a_1,b)<K_c(a_2,b)\). Thus
\[
g_y(a):=\Pr\{Y_2>y\mid A_1=a\}=\int_0^t h'_y(b)K_c(a,b)\,db
\]
is strictly increasing in \(a\) for \(c>0\) and every \(y>0\). More precisely, for \(0<a<t\), differentiating the two branches gives the strictly positive expression
\[
g'_y(a)=\frac{c}{\lambda}h'_y(a)e^{-(\lambda-c)a}+c(1-c/\lambda)e^{ca}\int_a^t h'_y(b)e^{-\lambda b}\,db>0.
\]
The same identity holds with an infinite upper endpoint at stationarity. This also covers \(c=\lambda\), when the ages coincide. For \(c=0\), the two ages and observables are independent.

Conditional on \(A_1=a>0\), the density of \(Y_1=z>0\) is proportional, as a function of \(a\), to
\[
a^{-d/2}\exp\!\left(-\frac{z}{4Da}\right).
\]
For \(z_2>z_1>0\), the ratio of these likelihoods is proportional to \(\exp(-(z_2-z_1)/(4Da))\), strictly increasing in \(a\). Consequently the posterior law of \(A_1\) given \(Y_1=z\) increases strictly in likelihood-ratio order with \(z\). Averaging the strictly increasing \(g_y(a)\) against this posterior proves the strict conditional tail monotonicity. The posterior is nondegenerate for every \(t>0\), including the boundary atom at \(t\).

**4. Why the radial qualification matters.** Conditional on the two ages, each Cartesian Brownian position is centered and has an independent symmetric sign. In one dimension, for every \(x,y>0\), the positive-positive quadrant tail is one quarter of the corresponding absolute-value joint tail and therefore strictly increases with \(m\). However
\[
\Pr\{X_1>x,X_2>-y\}=\tfrac12\Pr\{|X_1|>x\}-\tfrac14\Pr\{|X_1|>x,|X_2|>y\}
\]
strictly decreases with \(m\). Thus the signed bivariate laws cannot be concordance ordered in either direction. In every dimension, the signed cross-coordinate covariance is zero; the ordering applies to squared radii and monotone radial observables.

**5. Moment consistency.** For the stationary ages, integrating the joint survival yields \(\mathbb EA_i=1/\lambda\) and \(\operatorname{Cov}(A_1,A_2)=c/[\lambda^2(2\lambda-c)]\). Since \(\mathbb E Z_i=d\) and \(\mathbb E Z_i^2=d(d+2)\), the displayed energy covariance follows. The single energy variance is \(4D^2d(d+4)/\lambda^2\), giving the stated correlation. Substitution of \(r_m=\lambda N/m\) and \(c=\lambda(m-1)/(N-1)\) agrees with the established pair covariance in the motivating paper.

## Verification

A standalone `checker.py` implements the independent age-clock sampler, the finite-horizon and stationary double-integral formula, and the conditional age-kernel comparison. With \(N=6\), \(D=0.8\), \(\lambda=1.3\), \(d=2\), thresholds \(x=1.1\) and \(y=1.7\), the analytical pair-exceedance probabilities at \(t=1\) are, for batch sizes \(m=1,3,6\), respectively \(0.1480998447\), \(0.1686580255\), and \(0.2070572328\). At stationarity they are \(0.1727553344\), \(0.1990971433\), and \(0.2508530429\). Independent Monte Carlo tests with \(200000\) sampled age/position pairs per case agreed within five binomial standard deviations. Analytic derivative and covariance identities and strict conditional kernel comparisons were checked numerically. These finite computations check formulas; the all-parameter conclusions are proved above, not inferred from samples. Run \(`python checker.py`\) with NumPy and SciPy installed.

## Relationship to prior work

De Mauro, Majumdar, and Schehr (2026), arXiv:2601.20077, introduce this batch-reset gas and derive exact one-/two-point laws, transient and stationary squared-position correlations, and their nonmonotone optimization when the **global** reset rate is fixed. Their supplemental Sections S2, S3, S6 and S10 give the mathematical baseline; their formulas subsume the marginal laws and the stationary pair covariance reproduced here. The new statement compares **all joint radial exceedance thresholds and conditional risks** across batch sizes when the *individual* reset hazard is fixed. It adds an exact positive comparison integral, an all-time supermodular classification, a strict conditional monotone-regression law, and the signed-position boundary. None of those is asserted as a newly invented distribution or copula.

The shock-age survival formula is a classical Marshall–Olkin common-shock construction (Marshall and Olkin, 1967), and its positive dependence is established prior theory. The new contribution is the calibrated multi-particle resetting application together with the strict observable-level and posterior-prediction conclusions. Previously indexed findings on anisotropic joint far-tail exponents under fixed marginal reset rates, batch-reset pair tail prefactors, and random-batch connected cumulants address different observables and do not imply the stated **all-finite-threshold** strict conditional prediction theorem. The Gaussian-mixture transfer and likelihood-ratio argument are necessary beyond a statement about ordinary covariance or extreme-tail rates.

## Limitations

The result relies on independent Brownian noises, uniform fixed-size selection, instantaneous complete origin resets, Poisson clocks, and the calibrated family \(r_m=\lambda N/m\). It is not a claim of monotonicity at fixed *global* event rate: the established fixed-rate correlations can be nonmonotone in batch size. It is not a signed-position concordance theorem. The source paper provides a complete stationary pair law from which some special cases might be derivable, and unindexed or inaccessible results could contain an equivalent dependence-order treatment. No claim is made about heterogeneous reset rates, interactions, non-Poisson clocks, or individual posterior inference from signed coordinates.

## References

1. G. de Mauro, S. N. Majumdar, G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077 (first public 27 January 2026), https://arxiv.org/abs/2601.20077, especially supplemental Sections S2, S3, S6, S10.
2. A. W. Marshall and I. Olkin, *A multivariate exponential distribution*, Journal of the American Statistical Association **62** (1967), 30–44. A readable summary of the common-shock construction: https://formal-applied-math.github.io/formal-mathfin/m/MathFin.Probability.Dependence.MarshallOlkin.html.
3. *Anisotropic joint excursion rates under asymmetric shared and individual Brownian resetting*, indexed prior result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-anisotropic-joint-excursion-rates-under-asymmetric-shared-and-in--707257f9e1f5.
4. *Sharp pair-exceedance prefactor and singular tail dependence under batch resetting*, indexed prior result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-pair-exceedance-prefactor-and-singular-tail-dependence-und--6eb1adb91d8a.
