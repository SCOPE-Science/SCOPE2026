# The prior-slope transition for two-window exoplanet transit cadence

## Finding

Consider two noiseless, continuously monitored observation windows of equal duration \(w\), starting at \(0\) and at selectable time \(L\). A strictly periodic transiting planet has unknown orbital period \(P\in[a,b]\) and an independently uniform orbital phase. A success requires a transit center to fall in **each** window, i.e., two distinct transits. Suppose \(a>0\), \(w>0\), \(a+2w\le b\), and \(b+2w<2a\); restrict the first-repeat observing lag to \(a-w\le L\le b+w\). Let the prior density \(\pi(P)>0\) be continuous on \([a,b]\), and let \(h(P)=\pi(P)/P\).

The phase-averaged two-transit probability is exactly

\[
\mathcal Q(L)=\int_a^b h(P)\bigl(w-|L-P|\bigr)_+\,dP.
\]

Its maximizing lag has the following complete classification:

1. If \(h\) is strictly decreasing, \(\mathcal Q\) has a unique global maximizer \(L_*\in(a,a+w)\). It is the unique solution of
   \[
   \int_{L_*}^{L_*+w}h(P)\,dP=\int_a^{L_*}h(P)\,dP.
   \]
   The optimizer depends only on \(a,w\) and the values of \(h\) in \([a,a+2w]\), not on the upper prior tail.
2. If \(h\) is constant, the entire interval \([a+w,b-w]\) and no other lag maximizes \(\mathcal Q\).
3. If \(h\) is strictly increasing, \(\mathcal Q\) has a unique global maximizer \(L_*\in(b-w,b)\). It is the unique solution of
   \[
   \int_{L_*}^{b}h(P)\,dP=\int_{L_*-w}^{L_*}h(P)\,dP.
   \]
   The optimizer depends only on \(b,w\) and the values of \(h\) in \([b-2w,b]\).

For a power-law period prior \(\pi(P)=cP^{\beta}\), \(c>0\), this is an exact transition at \(\beta=1\): exponents below one favor a lag anchored near the shortest period; exponent one yields a full plateau; exponents above one favor the longest-period edge. In particular, for a uniform period prior (\(\beta=0\)),

\[
L_*=\frac{a+\sqrt{a^2+4aw}}{2}.
\]

For \(\beta=2\), the lag is \(L_*=-w+\sqrt{b^2+2w^2}\). In the unit-consistent illustrative case \((a,b,w)=(3,4,0.2)\), the three regimes give respectively \(3.188194301613\ldots\), every lag in \([3.2,3.8]\), and \(3.809987531153\ldots\).

## Assumptions and scope

The planet is already assumed to geometrically transit; inclination and occurrence are not modeled. Conditional on \(P\), its phase is uniform modulo \(P\). Transit centers are treated as instantaneous and are detected with certainty whenever inside a monitored window; noise, weather, finite transit duration, exposure cadence and signal-to-noise cuts are absent. The two windows have equal duration \(w\), and we maximize the probability of seeing **both** observations contain distinct transit centers. The restriction \(b+2w<2a\) ensures that the admissible lag interval never comes within one window length of a two-orbit or higher alias. The conclusions are not claimed for unrestricted multiorbit lags, intersecting windows or arbitrary nonmonotone priors.

## Proof

Fix \(P\in[a,b]\). Since \(a+2w\le b\) and \(b+2w<2a\), we have \(w<a/4<P\). Thus a single length-\(w\) observation window contains at most one transit center. A uniform phase corresponds to a uniform rotation of the lattice \(\phi+P\mathbb Z\). For the first window to contain a transit center, the possible phases occupy an interval of length \(w\). For the second window to contain the next transit center, the possible phases occupy a congruent interval translated by \(L-P\). Their overlap is of length \((w-|L-P|)_+\), provided no other integer multiple of \(P\) can match \(L\). On the admissible \(L\)-range we have \(0<L<2a-w\), so all non-first-repeat aliases are excluded. Dividing the phase overlap by \(P\) and integrating against \(\pi\) gives the displayed formula.

For \(L\in(a-w,b+w)\), differentiation under the integral (away from the finite set of moving endpoints, with one-sided derivatives at joins) gives the continuous derivative

\[
\mathcal Q'(L)=\int_{\max\{a,L\}}^{\min\{b,L+w\}}h(P)\,dP
-\int_{\max\{a,L-w\}}^{\min\{b,L\}}h(P)\,dP,
\]

where an integral over an empty interval is defined to be zero. For \(L\in(a-w,a]\), this derivative is strictly positive; for \(L\in[b,b+w)\), it is strictly negative. On the full-support interval \([a+w,b-w]\) it is

\[
\mathcal Q'(L)=\int_0^w\bigl[h(L+t)-h(L-w+t)\bigr]dt.
\]

This derivative is strictly negative when \(h\) decreases, zero when \(h\) is constant, and strictly positive when \(h\) increases. When \(h\) decreases, the only remaining possibility is \(L\in(a,a+w)\), where

\[
\mathcal Q'(a)=\int_a^{a+w}h>0,\qquad
\mathcal Q'(a+w)=\int_{a+w}^{a+2w}h-\int_a^{a+w}h<0.
\]

For \(L\in(a,a+w)\), \(\mathcal Q''(L)=h(L+w)-2h(L)<0\). Hence exactly one derivative zero exists there; it is the unique global maximum. The displayed first integral equation is exactly \(\mathcal Q'(L_*)=0\). With increasing \(h\), on \((b-w,b)\) we similarly have

\[
\mathcal Q'(b-w)=\int_{b-w}^bh-\int_{b-2w}^{b-w}h>0,\qquad
\mathcal Q'(b)=-\int_{b-w}^bh<0,
\]

and \(\mathcal Q''(L)=h(L-w)-2h(L)<0\). This proves the opposite-edge uniqueness and its integral equation. Constant \(h\) makes the derivative zero precisely on \([a+w,b-w]\), with strictly signed derivative outside, proving the plateau including the degenerate one-point case \(b=a+2w\).

For \(\pi(P)=cP^{\beta}\), \(h(P)=cP^{\beta-1}\) has exactly the stated monotonicity. At \(\beta=0\), \(\int_{L}^{L+w}dP/P=\int_a^L dP/P\) reduces to \(L^2=a(L+w)\) and the positive root lies in \((a,a+w)\). At \(\beta=2\), the right-edge equality reduces to \((L+w)^2=b^2+2w^2\), giving the unique root in \((b-w,b)\). All implications are exact for the specified ranges.

## Verification

The standalone Python 3 source `CHECK.py` evaluates the exact piecewise moment integral and its derivative for several power-law priors using only standard-library arithmetic. It compares the analytic maximizer against a finite grid and rechecks the explicit formulas and plateau; its finite diagnostics passed 55,922 assertions. This is supplementary to the preceding analytic proof. To reproduce: `python3 CHECK.py`.

## Relationship to prior work

Transit survey window functions, their phase averaging, observation cadence, noise and the minimum required transit count are central to von Braun and Ciardi (2007), von Braun, Kane and Ciardi (2009), and Burke and McCullough (2014). Their inspected treatments respectively use phase-sampled simulations and statistical approximations for broader survey configurations. They do not state the monotone-\(\pi(P)/P\) optimizer classification for two separated, equal-width continuous windows with a continuous period prior, or its explicit edge and plateau cases. The triangular overlap identity is elementary, and general results on convolution/unimodality are relevant; the claimed contribution is the physically interpreted sharp prior-slope design law and closed-form boundary locations **under the specified first-repeat survey constraints**, not the existence of window functions or general unimodality itself. Independent historical-priority verification is outstanding.

## Limitations

A finite transit duration, a requirement for several in-transit data points, photometric sensitivity, weather gaps, transit-time variation, selection effects, and realistic empirical period priors may all change the optimizer. When multiorbit aliases are allowed or the reweighted prior \(\pi(P)/P\) is nonmonotone, this theorem does not classify optimal lags. The result concerns a conditional mathematical experiment and is not an observing proposal certified for any instrument. The theoretical result does not imply that a two-transit signal alone establishes planetary nature or uniquely identifies the orbital period.

## References

- von Braun, K., & Ciardi, D. R. (2007), *Observational Window Functions in Planet Transit Searches*, arXiv:0711.4256, https://arxiv.org/abs/0711.4256 (first submitted 2007-11-27).
- von Braun, K., Kane, S. R., & Ciardi, D. R. (2009), *Observational Window Functions in Planet Transit Surveys*, arXiv:0907.1614, https://arxiv.org/abs/0907.1614 (first submitted 2009-07-09).
- Burke, C. J., & McCullough, P. R. (2014), *Transit and Radial Velocity Survey Efficiency Comparison for a Habitable Zone Earth*, arXiv:1406.6381, https://arxiv.org/abs/1406.6381 (first submitted 2014-06-24).
