# Correlation-driven optimal phase of two unreliable periodic transit departures

## Finding

Consider two candidate public-transit departures per cycle of length \(T>0\), the first scheduled at \(nT\) and the second at \((n+x)T\), \(n\in\mathbb Z\), where \(x\in[0,1]\). In each cycle their operating indicators \((A_n,B_n)\) are identically distributed across cycles, with independent pairs between cycles and
\[
\Pr(A_n=1)=p,\quad \Pr(B_n=1)=q,\quad \Pr(A_n=B_n=1)=r.
\]
Assume \(0<p,q<1\) and \(\max\{0,p+q-1\}\le r\le\min\{p,q\}\). Passengers arrive uniformly in the cycle, independently of the service indicators, and board the first operating departure, regardless of route. Their mean forward waiting time is exactly
\[
\boxed{\frac{W(x)}{T}=
\frac{2pqx^2-2rx+2-p-q+r}{2(p+q-r)}.}
\]
The **unique global minimizer** on \([0,1]\) is
\[
\boxed{x_* = \min\left\{1,\frac{r}{2pq}\right\}.}
\]
Thus the best schedule has coincident departures at the start of a cycle exactly when \(r=0\), an interior phase offset exactly when \(0<r<2pq\), and coincidence across the boundary between adjacent cycles exactly when \(r\ge2pq\). In particular, under independence within each cycle, \(r=pq\), the unique best offset is \(x_*=1/2\), whatever the marginal reliabilities. Writing \(c=\operatorname{Cov}(A_n,B_n)=r-pq\), this may be expressed as
\[
 x_*=\operatorname{clip}_{[0,1]}\left(\frac12+\frac{c}{2pq}\right),
\]
where the clipping notation denotes truncation to the closed interval. Positive dependence pushes the second departure later; negative dependence pushes it earlier.

For example, when \(p=q=r=2/5\) (one shared failure/success condition per cycle), the best offset is \(x_*=1\); the mean waiting time is \(7T/5\), versus \(8T/5\) under conventional half-cycle spacing. The difference is \(T/5\), without altering either route's operating frequency.

## Assumptions and scope

There is an infinite two-sided sequence of cycles; a scheduled trip either operates exactly at its scheduled time or does not operate, with no intermediate delay. The pair \((A_n,B_n)\) may be correlated, but distinct cycle pairs are independent. The four within-cycle outcome probabilities are respectively \(r\), \(p-r\), \(q-r\), and \(1-p-q+r\) for both running, first only, second only, and neither. The stated Fréchet bounds make all four nonnegative. Since \(p+q-r>0\), successive completely empty cycles have a geometric tail and a next operating trip exists almost surely with finite mean waiting time.

The parameter \(x=0\) means both scheduled opportunities occur at the same clock instant within the same cycle. The parameter \(x=1\) means the second opportunity associated with cycle \(n\) occurs at the same clock instant as the first opportunity associated with cycle \(n+1\). Those two opportunities retain their **different** cycle labels and hence different dependence structure. This boundary convention is essential: relabeling correlated pairs at this endpoint would specify a different stochastic model. Simultaneous operating buses count as one opportunity for a passenger who boards the first available vehicle.

The objective is the expectation of the forward waiting time at an independent time-uniform passenger arrival, not the expectation of waiting conditional on a given successful departure, nor the average of conditional waits over only cycles in which service occurred.

## Proof

Rescale time to \(T=1\). Put \(h=1-p-q+r\), the probability that a complete cycle has no operating departure, and \(s=1-h=p+q-r>0\). For \(x\in[0,1]\), let \(V\) denote the expected waiting time from immediately after the second scheduled opportunity in a cycle. The next first opportunity is in \(1-x\) time units. If it fails (probability \(1-p\)), another \(x\) units elapse before the second opportunity in the next cycle; if both fail (probability \(h\)), the residual expectation is once again \(V\). Independence between cycle pairs gives the exact recurrence
\[
V=(1-x)+(1-p)x+hV,
\qquad V=\frac{1-px}{s}.
\]
At a passenger arrival phase \(t\) strictly between \(0\) and \(x\), the first possible trip is the second one, at phase \(x\). The remaining expected waiting time is
\[
w(t)=x-t+(1-q)V,\qquad 0<t<x.
\]
At phase \(x<t<1\), the first possible trip is the next first departure; the first-to-second gap after its failure contributes \((1-p)x\), and failure of both upcoming opportunities contributes \(hV\). Hence
\[
w(t)=1-t+(1-p)x+hV,\qquad x<t<1.
\]
The values at the finitely many exact departure instants do not affect a time-uniform arrival. Integrating over the full cycle,
\[
\frac{W(x)}{T}
=\frac{x^2+(1-x)^2}{2}
+x(1-q)V+(1-x)\bigl((1-p)x+hV\bigr).
\]
Substituting \(V=(1-px)/s\) and simplifying gives the displayed quadratic. Its derivatives are
\[
\frac{d}{dx}\frac{W(x)}{T}=\frac{2pqx-r}{s},\qquad
\frac{d^2}{dx^2}\frac{W(x)}{T}=\frac{2pq}{s}>0.
\]
Thus the minimum is unique and lies at the projection of \(r/(2pq)\) onto \([0,1]\). Since \(r\ge0\), the projection is exactly \(\min\{1,r/(2pq)\}\). Equality cases at \(r=0\) and \(r=2pq\) follow from strict convexity, proving uniqueness even at either boundary.

The covariance expression follows from \(r=pq+c\). For the example, \(p=q=r=2/5\) gives \(x_*=1\); exact substitution gives \(W(1)/T=7/5\), \(W(1/2)/T=8/5\). This completes the classification.

## Verification

The standalone Python 3 file `verify.py` checks the stated quadratic against an independently implemented next-event recurrence using exact rational arithmetic over grids of feasible joint Bernoulli laws and phase offsets. It checks global optimality and strict equality cases on that grid, then performs supplementary pathwise squared-gap simulations with reproducible seeds. Run `python3 verify.py` in the same directory. At preparation the output was: `PASS: 15510 diagnostics (exact rational checks plus supplementary simulations).` The analytic recurrence and strict quadratic convexity are the proof for the continuum; finite checks are diagnostic only.

## Relationship to prior work

Mean forward wait for uniformly arriving passengers is classically controlled by the second moment of realized headways. The transit-reliability literature accordingly emphasizes even spacing of reliable services. Van Oort, Boterman and van Nes (2012) optimize scheduled trip times and holding points for unreliable long-headway transit; Ma, Ferreira and Mesbah (2014) estimate reliability measures from vehicle-location data; Fonzone, Schmöcker and Liu (2015) model non-uniform passenger-arrival behavior with stochastic departure times; and Schmöcker and collaborators (2016) study interactions between two routes on a common corridor. These are different stochastic objectives and mechanisms. The new mathematical point is an exact **paired Bernoulli service-loss** model in which departure survival has a specified joint probability in each cycle: this changes the optimum away from half-spacing and yields a sharp boundary transition at \(r=2pq\).

The general renewal-reward and residual-life methods are not claimed to be new. The contribution is the exact phase law for the stated dependence structure and the counterexample it supplies to extrapolating deterministic equal-spacing advice to positively or negatively correlated complete-trip cancellations. Historical priority beyond the inspected sources is not certified.

## Limitations

The result assumes cycle-to-cycle independence, a fixed common cycle length, time-uniform passenger arrivals, first-available boarding, no capacity constraint, no variable delays, and binary all-or-nothing operation. The covariance is tied to the **labeled cycle pair**, not to a physical-time correlation kernel: moving an arrival changes the time gap without changing the joint operating probability. If cancellation correlation changes with phase, or persists between cycles, the formula need not apply. Endpoint coincidence may not be operationally feasible. The result is a stylized planning benchmark and not an empirical estimate of an optimal bus timetable. Finite numerical diagnostics do not establish mathematical originality or field performance.

## References

1. Zhao, J., Dessouky, M., and Bukkapatnam, S., *Optimal Slack Time for Schedule-Based Transit Operations*, Transportation Science 40 (2006), 529–539, publicly posted November 1, 2006. https://doi.org/10.1287/trsc.1060.0170.
2. van Oort, N., Boterman, J. W., and van Nes, R., *The impact of scheduling on service reliability: trip-time determination and holding points in long-headway services*, Public Transport 4 (2012), 39–56, first published June 12, 2012. https://doi.org/10.1007/s12469-012-0054-4.
3. Ma, Z., Ferreira, L., and Mesbah, M., *Measuring Service Reliability Using Automatic Vehicle Location Data*, Mathematical Problems in Engineering (2014), article 468563, first published April 24, 2014. https://doi.org/10.1155/2014/468563.
4. Fonzone, A., Schmöcker, J.-D., and Liu, R., *A model of bus bunching under reliability-based passenger arrival patterns*, Transportation Research Part C 59 (2015), 164–182. https://doi.org/10.1016/j.trc.2015.05.020.
5. Schmöcker, J.-D., Sun, W., Liu, R., and Fonzone, A., *Bus bunching along a corridor served by two lines*, Transportation Research Part B 93 (2016), 300–317. https://doi.org/10.1016/j.trb.2016.07.005.
