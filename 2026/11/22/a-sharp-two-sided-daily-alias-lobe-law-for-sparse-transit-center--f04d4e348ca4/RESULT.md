# A sharp two-sided daily-alias lobe law for sparse transit-center surveys

## Finding

**Theorem (exact daily-alias window, both lobes).** Let \(N,r\) be integers with \(r\geq 2\) and \(N\geq 2r\). Let \(0<w<1/(2N)\). Observe continuously on the \(N\) daily windows \([j,j+w]\), \(j=0,\ldots,N-1\), with one day as the time unit. A periodic event train has times \(\phi+kP\), \(k\in\mathbb Z\), where \(\phi\) is uniform on \([0,P)\) and \(1-1/(2N)\leq P\leq1+1/(2N)\). Let \(F(P)\) be the probability that **at least \(r\) different event centers** lie in the observing windows. With \(\delta=|P-1|\) and \(\ell=w-(r-1)\delta\),

\[
F(P)=\begin{cases}
\bigl(\ell+(N-r)\min\{\delta,\ell\}\bigr)/P,&\ell>0,\\
0,&\ell\leq0.
\end{cases}
\]

In particular, the numerator is \(w+(N-2r+1)\delta\) for \(0\leq\delta\leq w/r\), is \((N-r+1)(w-(r-1)\delta)\) for \(w/r\leq\delta\leq w/(r-1)\), and vanishes beyond. The function has a strict local minimum at the exact daily resonance \(P=1\) with \(F(1)=w\), and precisely two positive strict local maxima in the specified interval, at

\[
P_{-}=1-w/r,\qquad P_{+}=1+w/r,
\qquad F(P_{\pm})=\frac{(N-r+1)w}{r\pm w}.
\]

The **unique global optimum** is \(P_-\), on the shorter-than-one-day side. All other points have strictly smaller detection probability. For fixed \(r\ge2\) and \(c\in(0,1/2)\), setting \(w=c/N\) yields \(F(P_- )\to c/r\) as \(N\to\infty\), whereas \(F(1)=c/N\to0\).

## Assumptions and scope

These are deterministic, noiseless, exactly equally spaced daily observation windows and pointlike event **centers**. A counted hit corresponds to a distinct event center, not repeated observations of the same finite-duration transit. Event train phase is random and uniform modulo its specified period. There are no missing nights, phase uncertainty beyond the uniform prior, visibility constraints, detector false negatives, finite transit lengths, or SNR conditions. Window endpoints have probability zero and do not affect results. The exact closed form is claimed only for the stated short-window and near-one-day parameter region. The MSC2020 primary classification is \(85A35\) (statistical astronomy).

## Proof

Since \(P\geq1-1/(2N)>1/2>w\), each observing interval contains at most one event. The phases producing an event in the \(j\)-th window form an arc \([j,j+w]\bmod P\) on the phase circle of circumference \(P\). Because \(P=1\pm\delta\), these arcs are, after reversing orientation when needed and choosing a common lift, exactly \(N\) intervals of length \(w\) with starts \(0,\delta,\ldots,(N-1)\delta\).

Their total lifted span is at most \(w+(N-1)\delta < 1/2 <P\), so this lift creates no unnoticed overlap across different turns of the phase circle. For a point to lie in at least \(r\) of these intervals, it must lie in \(r\) **consecutive** indexed intervals: consecutive membership follows because identical-length intervals with ordered start points have no missing intermediate members. Their common intersection for indices \(j,\ldots,j+r-1\) is

\[
[(j+r-1)\delta,\ j\delta+w],\qquad j=0,\ldots,N-r,
\]

of length \(\ell=w-(r-1)\delta\) if positive. Thus the wanted phase set is a union of \(N-r+1\) equal-length intervals, whose starts are separated by \(\delta\). Their union has length \(\ell+(N-r)\min(\delta,\ell)\) when \(\ell>0\); otherwise the phase set has measure zero. Dividing by the uniform phase circumference \(P\) proves the exact probability formula.

The crossover \(\delta=\ell\) occurs only at \(\delta=w/r\), producing the stated two linear numerator branches. Write \(A=N-2r+1\geq1\) and \(B=N-r+1>0\). On the increasing branch the two period-side derivatives are

\[
\frac{d}{d\delta}\frac{w+A\delta}{1+\delta}
=\frac{A-w}{(1+\delta)^2}>0,
\qquad
\frac{d}{d\delta}\frac{w+A\delta}{1-\delta}
=\frac{A+w}{(1-\delta)^2}>0.
\]

On the descending branch,

\[
\frac{d}{d\delta}\frac{B(w-(r-1)\delta)}{1+\delta}
=-\frac{B(w+r-1)}{(1+\delta)^2}<0,
\qquad
\frac{d}{d\delta}\frac{B(w-(r-1)\delta)}{1-\delta}
=\frac{B(w-r+1)}{(1-\delta)^2}<0.
\]

The latter inequality uses \(w<1\le r-1\). Therefore each of the two sides is uniquely maximized at \(\delta=w/r\), while \(P=1\) is a strict local minimum. Their maxima have the stated values; \(r-w<r+w\) makes \(P_-\) the unique global maximizer. For \(\delta\ge w/(r-1)\) the probability is zero. For the asymptotic claim substitute \(w=c/N\) into the exact maximum: \(F(P_-)=(N-r+1)c/(rN-c)\to c/r\), and at resonance \(c/N\to0\). No numerical step enters the infinite assertion.

## Verification

Run `python3 check.py`. The independent exact-fraction phase-partition checker constructs all survey arcs modulo each period, partitions the full phase circle at every arc endpoint, counts how many nights cover each cell, and sums lengths of cells covered at least \(r\) times. It reports 29,988 exact-rational assertions comparing this independent computation to the formula, as well as boundary and maximum-location tests. This is supplementary evidence; the proof above supplies the universal quantifiers.

As a numerical illustration, for \(N=30\), \(r=2\), and \(w=1/144\) day (ten minutes),

\[
P_-=287/288,\quad F(P_-)=0.10104529616724739\ldots,\\
F(1)=1/144=0.00694444444444\ldots,\\
P_+=289/288,\quad F(P_+)=0.10034602076124567\ldots.
\]

The maximum is about \(14.55\) times the exact-resonance coverage under this center-hit definition; this is **not** a forecast of physical exoplanet detection yields.

## Relationship to prior work

von Braun and Ciardi (2007) develop and simulate astronomical transit-observing window functions across night length, cadence and correlated noise; their open article and corresponding preprint describe simulations over initial orbital phases. Beatty and Gaudi (2008), Section II.1.2 and Appendix B, derive a randomized-observation approximation and explicitly note that it omits daily and half-daily aliasing effects. von Braun, Kane and Ciardi (2009), particularly Sections II and III.5, simulate the effect of requiring multiple transits, with realistic signal-to-noise assumptions. These sources motivate phase-dependent window completeness but, in the material inspected, do not state this exact all-\(N\), all-\(r\), short-window closed form or its asymmetric two-lobe optimizer. The core interval-union technique is elementary and is not claimed to be new by itself. General exact phase-coverage software or earlier astronomical alias formulas might already imply the present narrow theorem; that remains a historical-priority uncertainty.

## Limitations

The point-center, short-window approximation is restrictive. Actual transits have duration and finite-integration observability; nighttime visibility, measurement errors, weather, red noise, observing-time allocation and selection biases can change the shape and optimal period. This result concerns coverage conditional on a period, not a policy for changing an exoplanet's period, nor a statistical inference of that period. It is not an empirical confirmation, and independent expert validation has not been performed. A separate search of general circular-arc coverage and astronomy window-function literature would be useful for historical-priority certainty.

## References

1. K. von Braun and D. R. Ciardi, *Observational Window Functions in Planet Transit Searches*, Proceedings of the International Astronomical Union, online 1 October 2007, https://doi.org/10.1017/S1743921308016451 ; open version https://arxiv.org/html/0711.4256v2 .
2. T. G. Beatty and B. S. Gaudi, *Predicting the Yields of Photometric Surveys for Transiting Extrasolar Planets*, first preprint 7 April 2008, https://arxiv.org/abs/0804.1150 .
3. K. von Braun, S. R. Kane and D. R. Ciardi, *Observational Window Functions in Planet Transit Surveys*, first preprint 9 July 2009, https://arxiv.org/html/0907.1614v1 .
