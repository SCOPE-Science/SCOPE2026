# The exact read-noise crossover for phase-averaged transient exposure duration

## Finding

Consider a single rectangular astronomical transient whose duration \(T>0\) and positive integrated-flux amplitude per time \(A>0\) are known for matched-filter evaluation, but whose start phase relative to an uninterrupted sequence of exposures is uniform. Exposure width \(h>0\) is a continuously tunable design variable. Background-limited noise variance accumulated in an exposure is \(\nu h\), with \(\nu>0\), and each independent read contributes an additional variance \(R^2>0\).

Let \(\mathcal I(h)\) be the phase average of the *squared known-template matched-filter signal-to-noise ratio*. The unique maximizing duration is
\[
\frac{h_*}{T}=\begin{cases}
\sqrt{r^2+3r}-r,&0<r\le1,\\
\bigl(1+\sqrt{1+3r}\bigr)/3,&r\ge1,
\end{cases}\qquad r=\frac{R^2}{\nu T}.
\]
In particular, the unique optimum is shorter than the transient exactly when the one-read noise variance is less than the background variance accumulated over one transient duration; it is longer in the reverse regime, and equal at equality.

The exact maximized efficiency relative to ideal continuous-time, zero-read-noise observation \(A^2T/\nu\) is
\[
\frac{\mathcal I(h_*)}{A^2T/\nu}=\begin{cases}
1-\frac23(h_*/T),&0<r\le1,\\
\frac1{3(h_*/T)^2},&r\ge1.
\end{cases}
\]
At the crossing \(r=1\), the optimal efficiency is exactly \(1/3\); in the read-noise-small limit \(h_*/T\sim\sqrt{3r}\), and for read-noise-heavy instruments \(h_*/T\sim\sqrt{r/3}\).

## Assumptions and scope

Measurements comprise every disjoint bin \([jh,(j+1)h)\), \(j\in\mathbb Z\). A transient has flux \(A\) on an interval \([U,U+T)\) and zero otherwise, where \(U\) modulo \(h\) is uniform on \([0,h)\). The expected signal in bin \(j\) is \(A\ell_j(U,h)\), where \(\ell_j\) is the Lebesgue length of its intersection with the transient interval. The noise in each exposure is independent, centered, Gaussian with common variance \(\nu h+R^2\), treated as known and independent of signal. A known-start-time matched filter uses every bin overlapping the transient, so its squared noncentrality is \(A^2\sum_j\ell_j^2/(\nu h+R^2)\).

The criterion \(\mathcal I(h)\) averages this squared noncentrality over phase before maximizing in \(h\). It is not the true discovery probability after maximizing over unknown start times. All durations and positive noise parameters are real; no fixed observation overhead, saturation, finite exposure window, or instrumental cadence constraint is imposed.

## Proof

**Phase averaging.** Write \(L_j\) for the intersection of the pulse with bin \(j\). By Tonelli,
\[
\sum_j |L_j|^2=\int_0^T\int_0^T\mathbf 1\{U+s\text{ and }U+t\text{ belong to one bin}\}\,ds\,dt.
\]
For \(U\) uniform modulo \(h\), two instants separated by \(d\ge0\) are in the same bin with probability \((1-d/h)_+\). Consequently
\[
B(T,h):=\mathbb E_U\sum_j\ell_j(U,h)^2
=2\int_0^{\min(T,h)}(T-d)(1-d/h)\,dd
=\begin{cases}
Th-h^2/3,&0<h\le T,\\
T^2-T^3/(3h),&h\ge T.
\end{cases}
\]
The expressions and their first derivatives agree at \(h=T\). Thus \(\mathcal I(h)=A^2B(T,h)/(\nu h+R^2)\). With \(x=h/T\) and \(r=R^2/(\nu T)\), normalize it to \(A^2T/\nu\):
\[
f_r(x)=\begin{cases}(x-x^2/3)/(x+r),&0<x\le1,\\
(1-1/(3x))/(x+r),&x\ge1.
\end{cases}
\]
**Uniqueness and transition.** The derivative's sign for \(0<x<1\) is the sign of \(3r-2rx-x^2\), a strictly decreasing expression with one positive zero \(x_-=-r+\sqrt{r^2+3r}\). This zero lies at or below one precisely when \(r\le1\). For \(x>1\), the derivative's sign is that of \(2x+r-3x^2\), a downward quadratic whose only positive zero is \(x_+=(1+\sqrt{1+3r})/3\); it lies at or above one precisely when \(r\ge1\). At \(x=1\), the common derivative has sign \(r-1\). Hence the function strictly rises until the advertised optimizer and strictly decreases after it for every \(r>0\). Also \(f_r(x)\to0\) as \(x\to0\) or \(x\to\infty\), so this critical point is the unique global maximizer.

**Efficiency.** At \(x=x_-\), the stationary equation gives \(r=x^2/(3-2x)\), so substitution yields \(f_r(x)=1-2x/3\). At \(x=x_+\), the stationary equation gives \(r=3x^2-2x\), yielding \(f_r(x)=1/(3x^2)\). These coincide at one. The asymptotic statements follow by rationalization or Taylor expansion of the explicit roots.

## Verification

The accompanying standalone `check.py` computes phase averages by intersecting the event interval with actual exposure bins, compares them with the derived closed form over 150 randomized parameter pairs, checks exact rational specializations, evaluates stationary equations, and compares the optimizer with several scaled alternatives across 200 noise ratios. The delivered checker returned **PASS 3713 assertions**. These finite checks support, but do not replace, the universal analytic proof above.

## Relationship to prior work

Shamir and Nemiroff (2009) analyze optical transient detection across finite CCD frames and describe verification and coaddition effects, not this phase-averaged squared matched-filter design. Macquart (2014) optimizes radio-transient survey *detection rates across fields* and integration effort, rather than matched-filter noncentrality for a fixed rectangular pulse and random phase. Law and colleagues (2015) quantify sky-versus-read-noise exposure tradeoffs for MaNGA spectroscopy; their observing plan does not supply this exact event-duration crossover. Bélanger (2013) addresses likelihood-based transient searches and cadence granularity more generally. Generic matched-filter theory supplies the conditional squared-SNR expression but not the uniform-phase intersection integral or its piecewise globally optimal exposure duration. Historical priority has not been independently established.

## Limitations

This result optimizes an expected squared-SNR *proxy* with the template timing supplied to the filter, not a false-alarm-controlled unknown-phase search. Real surveys may be limited by dead time, telescope pointing, weather, readout overhead, correlated detector noise, event photon noise, duration uncertainty, varying flux shapes, multiple events, finite observing horizons, or discrete exposure choices. The theorem does not claim calibrated observational performance or optimal survey detection rate. If \(R^2=0\), the optimum moves to an unattained zero-duration limit; the strictly positive read-noise assumption is essential for a positive finite optimum.

## References

- Shamir, L. and Nemiroff, R. J. (2009). *Frequency Limits on Naked-Eye Optical Transients Lasting from Minutes to Years*. Astronomical Journal 138, 956. https://doi.org/10.1088/0004-6256/138/3/956. Publisher reports online publication 2009-08-14.
- Bélanger, G. (2013). *On Detecting Transient Phenomena*. Astrophysical Journal 773, 66. https://arxiv.org/abs/1303.7408 (first deposited 2013-03-29).
- Macquart, J.-P. (2014). *Optimization of Survey Strategies for Detecting Slow Radio Transients*. PASA 31, e031. https://arxiv.org/abs/1406.5790 (first deposited 2014-06-23); https://doi.org/10.1017/pasa.2014.27.
- Law, D. R. et al. (2015). *Observing Strategy for the SDSS-IV/MaNGA IFU Galaxy Survey*. Astronomical Journal 150, 19. https://arxiv.org/abs/1505.04285 (first deposited 2015-05-16).
