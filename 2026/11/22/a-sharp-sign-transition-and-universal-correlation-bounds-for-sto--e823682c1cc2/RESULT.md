# A sharp sign transition and universal correlation bounds for stormwater wash-off

## Finding
Consider independent storm events that remove random fractions of a catchment's pre-event pollutant stock, with independently accumulated new pollutant mass between storms. In the stationary regime the stored mass has nonnegative geometric autocovariance, but successive *exported* loads can have either sign of autocovariance. The sign is identical at every positive event lag and has an exact, distribution-free threshold determined only by three dimensionless moments. Moreover, for every positive lag the output correlation lies between two sharp universal bounds; with deterministic interevent accumulation and genuinely random removal, all such correlations equal their negative lower bounds.

Precisely, let \(F_n\in[0,1]\) be independent identically distributed fractional storm removals with mean \(0<\mu<1\) and variance \(v\), and let \(U_n\ge0\) be independent identically distributed interstorm additions, independent of all removals, with \(a=\mathbb E U_n>0\) and finite second moment. Put \(c=\operatorname{Var}(U_n)/a^2\), \(d=\mu(2-\mu)-v>0\), and define the pre-storm stock and exported event load by
\[
X_{n+1}=(1-F_n)X_n+U_{n+1},\qquad Y_n=F_nX_n.
\]
There is a unique stationary finite-second-moment solution. In it, for every integer \(k\ge1\),
\[
\operatorname{Cov}(Y_n,Y_{n+k})=(1-\mu)^{k-1}a^2
\frac{c\mu^2(1-\mu)-v(1+c\mu)}{d},
\]
whereas \(\operatorname{Cov}(X_n,X_{n+k})=(1-\mu)^k\operatorname{Var}(X_n)\ge0\).
Thus event-load dependence is positive, zero, or negative at **every** positive lag according as
\[
v\quad\text{is less than, equal to, or greater than}\quad v_*(\mu,c)=\frac{c\mu^2(1-\mu)}{1+c\mu}.
\]
When \(\operatorname{Var}(Y_n)>0\), with \(\rho_k=\operatorname{Corr}(Y_n,Y_{n+k})\),
\[
-\frac{\mu}{2}(1-\mu)^{k-1}\ \le\ \rho_k\ \le\ (1-\mu)^k.
\]
Both boundaries are sharp: the lower one is attained whenever \(c=0\) and \(v>0\), and the upper one whenever \(v=0\) and \(c>0\).

For exponential interstorm additions of mean one, \(\mu=1/2\), and symmetric Beta-distributed removal fractions with parameters \((2,2)\), \((1,1)\), and \((1/2,1/2)\), the respective lag-one exported-load covariances are exactly \(1/14\), \(0\), and \(-1/10\) (in squared mass units). Despite the change of sign, the stock autocovariance stays nonnegative.

## Assumptions and scope
Events are indexed by integers. The two innovation sequences \((F_n)\) and \((U_n)\) are independent of one another; each is identically distributed and independent across time. There is no within-storm replenishment, nonlinear wash-off, pollutant decay in the dry period, measurement noise, or capacity constraint. The interstorm addition \(U_n\) may represent constant-rate buildup during a random dry interval, but it is only assumed nonnegative with finite positive first and finite second moments. Neither Poisson storm arrivals nor a parametric distribution for \(F_n\) or \(U_n\) is required. The correlation statements require positive output variance; when both innovations are deterministic, event loads are constant, so Pearson correlations are undefined.

For any \([0,1]\)-valued random variable \(F_n\), \(0\le v\le\mu(1-\mu)\). Consequently \(d\ge\mu>0\). All finite-time and infinite stationary statements are in event count, not clock time. The result does not infer hydrological parameters from data.

## Proof
Set \(q=1-\mu\) and \(r_2=\mathbb E(1-F_n)^2=1-d<1\). On a two-sided sequence of innovations, iterate the affine recurrence backward to obtain the almost surely and \(L^2\)-convergent series
\[
X_n=U_n+(1-F_{n-1})U_{n-1}+(1-F_{n-1})(1-F_{n-2})U_{n-2}+\cdots.
\]
Its summands have \(L^2\)-norm bounded by \(\|U_0\|_2r_2^{j/2}\), so the series converges absolutely in \(L^2\). Coupling any two solutions using identical future innovations contracts their \(L^2\)-distance by \(r_2^{j/2}\), proving uniqueness among finite-second-moment stationary solutions.

Independence of \(F_n\) and the pre-event \(X_n\) gives \(\mathbb EX_n=a/\mu\). Squaring the recurrence and using independence of \(U_{n+1}\), \(F_n\), and \(X_n\) yields
\[
\mathbb EX_n^2=r_2\mathbb EX_n^2+2qa\mathbb EX_n+\mathbb EU_n^2.
\]
Consequently
\[
\mathbb EX_n^2=\frac{a^2(2-\mu+\mu c)}{\mu d},\qquad
\operatorname{Var}(X_n)=\frac{a^2(c\mu^2+v)}{\mu^2d}.
\]
As \(\mathbb EY_n=\mu\mathbb EX_n=a\), its stationary variance is
\[
\operatorname{Var}(Y_n)=\frac{a^2[2v+c\mu(\mu^2+v)]}{\mu d}.
\]
For successive events, condition on \(F_n,X_n,U_{n+1}\); the next removal is independent, and \(\mathbb E[F_n(1-F_n)]=\mu(1-\mu)-v\). Therefore
\[
\begin{aligned}
\operatorname{Cov}(Y_n,Y_{n+1})
&=\mu[\mu(1-\mu)-v]\mathbb EX_n^2+\mu a^2-a^2\\
&=\frac{a^2[c\mu^2(1-\mu)-v(1+c\mu)]}{d}.
\end{aligned}
\]
Iterated conditional expectation gives \(\mathbb E[X_{n+k}\mid X_{n+1}]=q^{k-1}X_{n+1}+a(1-q^{k-1})/\mu\) for \(k\ge1\). Since the terminal fraction \(F_{n+k}\) is independent of the past, \(\operatorname{Cov}(Y_n,Y_{n+k})=q^{k-1}\operatorname{Cov}(Y_n,Y_{n+1})\). Similarly \(\mathbb E[X_{n+k}\mid X_n]=q^kX_n+a(1-q^k)/\mu\), giving the positive stock covariance. Because \(d>0\) and \(1+c\mu>0\), the sign threshold is exact.

For nondegenerate output, direct division by the variance gives
\[
\rho_1=\frac{\mu[c\mu^2(1-\mu)-v(1+c\mu)]}{2v+c\mu(\mu^2+v)},\qquad \rho_k=q^{k-1}\rho_1.
\]
The two differences from the proposed bounds factor as
\[
\rho_1+\frac\mu2=\frac{c\mu^2d}{2[2v+c\mu(\mu^2+v)]}\ge0,
\qquad
(1-\mu)-\rho_1=\frac{v(2-\mu+c\mu)}{2v+c\mu(\mu^2+v)}\ge0.
\]
This proves the sharp interval, including equality cases. In particular, setting \(c=0\) and \(v>0\) gives \(\rho_k=-\mu(1-\mu)^{k-1}/2\), independent of the entire distribution of removal fractions other than their mean.

For the concrete Beta examples, \(\mathbb EF=1/2\) and \(v=1/[4(2\alpha+1)]\) for \(F\sim\operatorname{Beta}(\alpha,\alpha)\), with \(c=a=1\). Substituting \(\alpha=2,1,1/2\) yields the stated rational covariances. The zero-covariance case does not assert stochastic independence.

## Verification
The standalone `check.py` uses exact rational arithmetic to compare the stationary-moment recurrence with the displayed closed forms for a grid of removal means, admissible variances, input coefficients of variation, and scales. It also rechecks the three Beta examples and uses seeded random simulation only as a diagnostic. Run `python3 check.py` from the same directory as this document. The exact check has 31,192 counted exact-rational checks, and the three finite simulations separately compare their empirical moments to the formulas. These computational checks are not used to establish any universal quantifiers, which are supplied by the proof.

## Relationship to prior work
Chen and Adams (2006) analyze distributions and expectations of stormwater pollutant loads under stochastic rainfall and buildup/wash-off transformations. Al Ali, Bonhomme, and Chebbo (2016) explicitly model residual pollutant mass carried over between rainfall events and evaluate model calibration. Botter (2010) derives autocorrelations for continuous streamflow driven by random recession rates. Daly, Bach, and Deletic (2014) examine stochastic variability in within-event stormwater wash-off. These motivate the recurrence and the distinction between observed event exports and retained stock, but the inspected full texts do not state the event-indexed positive/negative covariance threshold, its all-lag persistence, or the sharp universal correlation bounds. The 2014 paper was available only through an abstract for this comparison; its complete coverage remains an originality risk.

## Limitations
The result concerns a stylized linear stock with independent event-specific removal and between-event accumulation. Actual wash-off efficiency may depend on antecedent dry weather, rain intensity, available sediment, and within-event nonlinearities; such dependence can invalidate the threshold. Calendar-time correlations need not have these event-lag formulas. Zero autocovariance does not imply independence; a model with zero covariance must not be treated automatically as an independent-load process. The originality assessment is relative to accessible literature and does not certify historical priority. No field data or management performance was validated.

## References
1. J. Chen and B. J. Adams, “A framework for urban storm water modeling and control analysis with analytical models,” *Water Resources Research* 42 (2006). First published 2006-06-23. DOI: https://doi.org/10.1029/2005WR004540 .
2. G. Botter, “Stochastic recession rates and the probabilistic structure of stream flows,” *Water Resources Research* 46 (2010). First published 2010-12-09. DOI: https://doi.org/10.1029/2010WR009217 .
3. E. Daly, P. M. Bach, and A. Deletic, “Stormwater pollutant runoff: A stochastic approach,” *Advances in Water Resources* 74 (2014), 148–155. DOI: https://doi.org/10.1016/j.advwatres.2014.09.003 .
4. S. Al Ali, C. Bonhomme, and G. Chebbo, “Evaluation of the Performance and the Predictive Capacity of Build-Up and Wash-Off Models on Different Temporal Scales,” *Water* 8 (2016), 312. Published 2016-07-23. DOI: https://doi.org/10.3390/w8080312 .
