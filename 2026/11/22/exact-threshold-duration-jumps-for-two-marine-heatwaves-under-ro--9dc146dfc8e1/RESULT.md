# Exact threshold-duration jumps for two marine heatwaves under rolling thermal accumulation

## Finding
Consider the continuous-time rolling-window analog of a degree-heating-weeks (DHW) stress index. Two equal, constant-strength heatwaves of duration \(d\) are separated by a clean interval \(g\), while accumulation uses a window \(W\geq 2d\). At every threshold \(q\) strictly between zero and the total possible exposure \(2d\), the topology and total duration of the accumulated-stress superlevel set change at exactly the same gap \(g_*=W-q\).

More precisely, let \(E_q(g)=\{t\in\mathbb R:H_g(t)\geq q\}\) and \(L_q(g)\) be its length. For \(0<q\leq d\),
\[
E_q(g)=\begin{cases}
[q,W+2d+g-q],&0\leq g\leq W-q,\\
[q,W+d-q]\cup[d+g+q,W+2d+g-q],&g>W-q.
\end{cases}
\]
The first regime has one component and \(L_q(g)=W+2d+g-2q\); the second has two components and \(L_q(g)=2(W+d-2q)\). Consequently, the threshold-exceedance duration drops by exactly \(q\) upon crossing \(g_*=W-q\) from below, although the heat exposure comprises the same two pulses and has unchanged total thermal dose.

For \(d<q<2d\),
\[
E_q(g)=\begin{cases}
[g+q,W+2d-q],&0\leq g\leq W-q,\\
\varnothing,&g>W-q.
\end{cases}
\]
Thus \(L_q(g)=W+2d-g-2q\) up to and including the critical separation and is zero above it. At the transition the entire single above-threshold interval disappears, through a drop of precisely \(2d-q\) in its duration. The weak and strong threshold regimes have opposite pretransition slopes: \(+1\) and \(-1\) in gap duration, respectively.

## Assumptions and scope
Time is continuous, with all durations measured in one common unit (e.g. weeks). Parameters satisfy \(d>0\), \(W\geq2d\), \(g\geq0\), and \(0<q<2d\). The normalized heat-stress forcing is
\[
f_g(s)={\mathbf{1}}_{[0,d]}(s)+{\mathbf{1}}_{[d+g,2d+g]}(s),\qquad
H_g(t)=\int_{t-W}^{t}f_g(s)\,ds.
\]
Intervals' endpoints do not affect the integral. A rectangular heatwave has identical positive intensity within each pulse and zero heat stress in the intervening gap. The threshold relation uses \(\geq\), not \(>\), so nonzero equality plateaus count. When the physical HotSpot amplitude is \(A\) degrees Celsius, the DHW threshold in degree Celsius-weeks is \(Aq\) provided the unit of duration is a week. The index analyzed here is the *DHW-only threshold set*, not the full NOAA Bleaching Alert Area classification (which additionally examines the current HotSpot and composites alerts). This is a continuous-time idealization, not the daily sampled NOAA algorithm.

## Proof
Let \(R(t)=\int_{t-W}^{t}{\mathbf{1}}_{[0,d]}(s)\,ds\). Because \(W\geq2d\), the one-pulse response is
\[
R(t)=\begin{cases}
0,&t\leq0,\\
t,&0\leq t\leq d,\\
d,&d\leq t\leq W,\\
W+d-t,&W\leq t\leq W+d,\\
0,&t\geq W+d.
\end{cases}
\]
Thus \(H_g(t)=R(t)+R(t-d-g)\), a continuous piecewise-affine function whose only slope changes occur at \(0,d,W,W+d,d+g,2d+g,W+d+g,W+2d+g\). The formula holds also when some breakpoints coincide.

First suppose \(0<q\leq d\). The earliest threshold contact is \(t=q\), since the second pulse starts no earlier than \(d\), and the last threshold contact is \(t=W+2d+g-q\). Each isolated pulse alone gives the interval \([q,W+d-q]\) or its shift by \(d+g\). To determine whether these two threshold components connect, inspect the possible trough between them. Before the first response starts to fall, its value is \(d\geq q\). After the second response begins rising, its growth can offset the first response's decline; a subthreshold trough appears precisely when \(g>W-q\). At the boundary \(g=W-q\), their combined response equals \(q\) on the entire interval \([d+g,W+d]\) (whose length is \(q\)), so the closed superlevel set remains connected. Direct substitution of the displayed five pieces of \(R\) then gives exactly the two superlevel-set formulas in the Finding section, including their endpoints. Taking interval lengths yields the first duration formula and its jump \(q\).

Now suppose \(d<q<2d\). No single pulse reaches the threshold. Hence the superlevel set must lie where both pulse responses are simultaneously positive. In that region it has precisely one connected plateau or peak: on entering it crosses \(q\) at \(t=g+q\), while on leaving it crosses \(q\) at \(t=W+2d-q\). These crossings occur in their stated order exactly if \(g\leq W-q\). At equality they bound a constant-height \(q\) plateau and therefore remain included; for larger gaps the peak height is strictly below \(q\). Again these assertions follow by evaluating \(R(t)+R(t-d-g)\) separately on its finitely many affine pieces. This proves the second formula. Its interval length at the critical gap is \(2d-q\), whereas any larger gap has empty superlevel set. The claimed jump and pretransition slopes follow by subtraction.

For completeness, equality \(q=d\) belongs to the first case, because either individual rectangular pulse attains \(q\); it is not an instance of the disappearance regime. Strict thresholding instead of \(\geq\) changes behavior *at* the transition by excluding equality plateaus. No limit statement for a smoothed, noisy, discrete-day, unequal-amplitude, or differently shaped heatwave follows from this theorem.

## Verification
The standalone `checker.py` evaluates the same continuous model with exact rational arithmetic. It independently partitions time at all pulse and shifted-window endpoints, constructs the \(H_g\geq q\) intervals using exact linear interpolation, merges touching intervals, and compares the total length and the number of positive-length components against the formula. Running `python checker.py` passes 6,451 deterministic rational cases, including boundaries where the gap is exactly critical. This is diagnostic corroboration; the preceding case analysis supplies the all-parameter proof.

For an illustrative \(W=12\)-week window and two \(d=3\)-week pulses with contribution amplitude \(A=2\) degrees Celsius, the \(4\) degree-Celsius-week threshold corresponds to \(q=2\) weeks: its critical clean gap is \(10\) weeks and its duration changes from \(24\) weeks at the critical gap to \(22\) weeks immediately beyond. The \(8\) degree-Celsius-week threshold corresponds to \(q=4\) weeks: its critical gap is \(8\) weeks, at which its duration is \(2\) weeks; it vanishes for every larger gap. These are analytic inputs, not field observations.

## Relationship to prior work
Liu et al. (2014) describe the actual NOAA Coral Reef Watch daily HotSpot/DHW algorithm, which sums qualifying anomalies across an 84-day window. NOAA's earlier technical report (Liu et al., 2013, section 2.5) gives the same cumulative-window interpretation for the earlier twice-weekly product. Little et al. (2022) explicitly discuss persistence of an apparent thermal event beyond its physical heatwave because of the rolling accumulation window. These are established starting points, not claimed as new. Their inspected discussions do not state the present complete two-rectangular-pulse superlevel-set classification, critical gap, or exact right-discontinuous exceedance-duration laws. The result applies elementary convolution geometry to a concrete thermal-monitoring diagnostic; it does not claim a new general convolution identity.

## Limitations
Actual NOAA products operate on daily sampled data and include a lower HotSpot inclusion threshold. Bleaching Alert Area categories also depend on ongoing HotSpot and seven-day aggregation, whereas \(E_q(g)\) records only the rolling-DHW threshold. Equality plateaus and discontinuities here arise from idealized constant-height, sharp-edged pulses; measurement noise, smooth heatwave shoulders, unequal pulse amplitudes and discrete sampling can substantially alter or remove exact jumps. No bleaching occurrence, biological damage, statistical confidence or optimal management action is inferred. Historical literature beyond the inspected sources may contain an equivalent convolution-level formulation; independent priority checking is still warranted.

## References
1. Liu, G. et al. (2014), “Reef-Scale Thermal Stress Monitoring of Coral Ecosystems: New 5-km Global Products from NOAA Coral Reef Watch,” *Remote Sensing* 6, 11579–11606, published 20 November 2014. https://doi.org/10.3390/rs61111579
2. Liu, G. et al. (2013), *NOAA Coral Reef Watch 50 km Satellite Sea Surface Temperature-Based Decision Support System for Coral Bleaching Management*, NOAA Technical Report NESDIS 143, March 2013, section 2.5. https://coralreefwatch.noaa.gov/satellite/publications/NOAA.Tech.Report.143.pdf
3. Little, C. M. et al. (2022), “Global coral bleaching event detection from satellite monitoring of extreme heat stress,” *Frontiers in Marine Science* 9, 883271, 5 September 2022. https://doi.org/10.3389/fmars.2022.883271
4. NOAA Coral Reef Watch, daily 5-km thermal-stress product methodology, section 6, accessed 17 November 2026. https://www.coralreefwatch.noaa.gov/product/5km/methodology.php
