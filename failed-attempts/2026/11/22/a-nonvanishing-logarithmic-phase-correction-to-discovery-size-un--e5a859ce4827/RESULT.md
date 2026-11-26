# A nonvanishing logarithmic-phase correction to discovery size under periodic invasion surveillance

## Finding

For a newly established population growing exponentially without a carrying-capacity cutoff, observed at regularly spaced survey times with independent Poisson-thinning detection, the sensitivity-weighted expected population size at discovery has a nonconstant, explicitly computable logarithmically periodic leading term as survey sensitivity tends to zero. The dependence on the fractional logarithmic phase persists at every fixed positive survey interval; consequently there is no single weak-sensitivity limit. Its phase average and every Fourier coefficient have closed forms involving the Gamma function.

More precisely, set \(R=e^{gT}>1\), \(a=\sigma A_0>0\), \(c=aR/(R-1)\) and \(\theta(c)=\{\log_R(1/c)\}\). Define

\[
F_R(\theta)=\sum_{j\in\mathbb Z}R^{j-\theta}\exp(-R^{j-\theta}).
\]

The exact expectation and its uniform weak-sensitivity asymptotic are

\[
\sigma\,\mathbb E[A(KT)]
=a\left[1+(R-1)e^c\sum_{n=0}^{\infty}R^n e^{-cR^n}\right]
=\frac{(R-1)^2}{R}F_R(\theta(c))+O_R(a).
\]

Here the error bound is uniform over all \(0<a\le a_0(R)\) and all phases. The periodic function is positive, continuous, and nonconstant for **every** \(R>1\), with Fourier coefficients

\[
\widehat F_R(k)=\frac{1}{\log R}\,\Gamma\!\left(1+\frac{2\pi i k}{\log R}\right),\qquad k\in\mathbb Z.
\]

In particular its phase average is \(1/\log R\) and every nonzero Fourier coefficient is nonzero. The set of all subsequential limits of \(\sigma\mathbb E[A(KT)]\) as \(\sigma\downarrow0\), holding \(A_0,g,T\) fixed, is exactly

\[
\frac{(R-1)^2}{R}\,[\min_{0\le\theta\le1}F_R(\theta),\ \max_{0\le\theta\le1}F_R(\theta)],
\]

which is a nondegenerate closed interval.

## Assumptions and scope

Fix \(A_0>0\), growth rate \(g>0\), spacing \(T>0\) and survey sensitivity \(\sigma>0\). The deterministic population area or abundance is \(A(t)=A_0 e^{gt}\) for all \(t\ge0\), without saturation or stochastic demographic feedback. Surveys occur at exactly \(T,2T,\ldots\). Conditional on no previous alarm, a survey at time \(nT\) fails with probability \(\exp[-\sigma A(nT)]\). The survey-failure events are independent. A positive detection terminates the sequence. Let \(K\in\{1,2,\ldots\}\) be the first successful survey index. The weak-sensitivity limit is \(\sigma\to0+\) at fixed \(A_0,g,T\). The survey programme and the population's founding time have a fixed phase: they are **not** averaged over a uniform unknown invasion time. This distinction is essential for the phase effect.

## Proof

**1. Exact discovery law.** The probability of missing all of the first \(n\) surveys is

\[
\Pr(K>n)=\prod_{j=1}^{n}e^{-aR^j}
=\exp\left[-a\frac{R(R^n-1)}{R-1}\right]
=e^c e^{-cR^n},\qquad n\ge0.
\]

It tends to zero, so \(K\) is finite almost surely. The nonnegative tail-sum identity \(\mathbb E[R^K]=1+(R-1)\sum_{n\ge0}R^n\Pr(K>n)\) gives the stated exact expression. The series converges since \(R^n e^{-cR^n}\) is super-exponentially small; therefore the expected discovery size is finite for each \(a>0\).

**2. Phase extraction with uniform error.** Write \(h(u)=ue^{-u}\), \(m=\lfloor\log_R(1/c)\rfloor\), and \(\theta=\log_R(1/c)-m\). Then \(c=R^{-m-\theta}\) and, exactly,

\[
\sum_{n\ge0}h(cR^n)=\sum_{j\ge-m}h(R^{j-\theta}).
\]

The omitted lower tail is uniformly bounded by

\[
0\le F_R(\theta)-\sum_{n\ge0}h(cR^n)
\le\sum_{j<-m}R^{j-\theta}=\frac{c}{R-1}.
\]

The two-sided series defining \(F_R\) converges uniformly in \(\theta\in[0,1]\): at negative indices its terms are bounded by a geometric series, and at positive indices by a super-exponentially convergent series. Its maximum is therefore finite and independent of \(\theta\). Since \(e^c=1+O_R(c)\) as \(c\downarrow0\), substitution into

\[
a+(R-1)e^c\,\frac{a}{c}\sum_{n\ge0}h(cR^n)
\]

and \(a/c=(R-1)/R\) yields the formula with absolute error \(O_R(a)\), uniformly in phase.

**3. Exact Fourier coefficients and nonconstancy.** Uniform convergence permits termwise integration. With \(y=j-\theta\) and \(u=R^y\), for every integer \(k\),

\[
\begin{aligned}
\widehat F_R(k)&=\int_0^1 F_R(\theta)e^{-2\pi i k\theta}\,d\theta\\
&=\int_{-\infty}^{\infty}h(R^y)e^{2\pi i ky}\,dy\\
&=\frac{1}{\log R}\int_0^\infty e^{-u}u^{2\pi i k/\log R}\,du
=\frac{1}{\log R}\Gamma\left(1+\frac{2\pi i k}{\log R}\right).
\end{aligned}
\]

The Gamma function has no zeros. One elementary justification for this particular vertical line follows from the standard reciprocal Euler product

\[
\Gamma(1+z)^{-1}=e^{\gamma z}\prod_{n\ge1}(1+z/n)e^{-z/n}.
\]

For purely imaginary \(z\), no factor vanishes and the logarithmic tail converges absolutely because its terms are \(O(n^{-2})\); hence the product is finite and nonzero. Therefore the first Fourier coefficient of \(F_R\) is nonzero for every \(R>1\), establishing nonconstancy. The coefficient at \(k=0\) is \(1/\log R\).

**4. Full subsequential-limit interval.** For any chosen \(\theta\in[0,1)\), set \(a_m=(R-1)R^{-m-\theta}/R\), so that \(\sigma_m=a_m/A_0\downarrow0\) and \(\theta(c_m)=\theta\). The uniform formula then gives limit \((R-1)^2 F_R(\theta)/R\). Conversely every subsequence has a further subsequence with its phases converging on the circle, and the uniform formula forces its limit to be a value of this same continuous periodic function. The continuous image of the connected phase circle is the indicated compact interval; by nonconstancy it is not a point.

## Verification

The included standalone \(\texttt{check.py}\) uses only the Python standard library. It independently checks geometric sums against survey-wise failure products, sums detection-index masses against the tail identity, compares small-sensitivity expectations across fixed logarithmic phases, tests periodicity, and integrates the periodic profile against its exact phase mean. A replay produced 276 passed numerical diagnostics. No finite diagnostic establishes the infinite asymptotic, uniform bound, or Gamma zero-free statement; those are proved in the preceding section.

For \(R=10\), the leading values are \(3.805605035176776\) at \(\theta=0\) and \(3.227809993075674\) at \(\theta=1/2\), versus phase average \(8.1/\log 10=3.517785303416339\). Thus the fixed-survey-phase effect can remain appreciable even in the weak-sensitivity regime. These numbers illustrate the theorem rather than calibrate a particular species.

## Relationship to prior work

Parnell, Gottwald, Gilks and van den Bosch (2012) introduced repeated-survey first-discovery incidence calculations and a continuous-sampling approximation. Parnell and coauthors (2015) developed a regular-sampling plant-pathogen model with a randomly timed introduction and an averaged rule of thumb for expected discovery prevalence. Epanchin-Niell and coauthors (2012) modelled discrete surveys with growing, size-dependent detection probability, finite population-size classes, repeated introductions and management costs. Guillera-Arroita, Hauser and McCarthy (2014) considered optimizing bounded surveys terminated at detection. These works motivate the problem and supply relevant exact finite-survey detection models; the claim here is narrowly the all-spacing **nonconstant logarithmic-phase weak-sensitivity limit**, its uniform error and explicit Gamma-spectrum, for an unbounded exponential-growth population whose founding phase is fixed. These asymptotic phase statements were not located in the accessible inspected texts. They are not asserted to be independent of the underlying published first-detection probability formulations.

## Limitations

The claim is a deterministic, unbounded exponential-growth idealization and may fail when growth saturates, invasions appear at random phases, detection events are correlated, or surveys have varying effort. Averaging over unknown invasion time can suppress or change the phase oscillation. The asymptotic regime makes predicted populations large; extrapolating it past a biological carrying capacity is not justified. The closest 2012 first-discovery article was available only as an abstract, and a 2025/2026 size-at-detection study was also available only in partial form; these leave a substantive historical-priority risk. No assertion of independently verified novelty or field-management effectiveness is made.

## References

1. S. Parnell, T. R. Gottwald, W. R. Gilks, F. van den Bosch, “Estimating the incidence of an epidemic when it is first discovered and the design of early detection monitoring,” *Journal of Theoretical Biology* 305 (2012), 30–36. DOI: 10.1016/j.jtbi.2012.03.009. Public electronic article date: 2012-03-29.
2. R. S. Epanchin-Niell, R. G. Haight, L. Berec, J. M. Kean, A. M. Liebhold, “Optimal surveillance and eradication of invasive species in heterogeneous landscapes,” *Ecology Letters* 15 (2012), 803–812. DOI: 10.1111/j.1461-0248.2012.01800.x. First published 2012-05-30.
3. S. Parnell et al., “Early detection surveillance for an emerging plant pathogen: a rule of thumb to predict prevalence at first discovery,” *Proceedings of the Royal Society B* 282 (2015), 20151478. DOI: 10.1098/rspb.2015.1478.
4. G. Guillera-Arroita, C. E. Hauser, M. A. McCarthy, “Optimal surveillance strategy for invasive species management when surveys stop after detection,” *Ecology and Evolution* 4 (2014). DOI: 10.1002/ece3.1056.
5. A. P. Robinson et al., “Using survival analysis to develop models for estimating size-at-detection of invasive species under surveillance,” *Oikos* 2026, e11269 (first published 2025-11-20). DOI: 10.1002/oik.11269. Related later work, not a source-date anchor.
