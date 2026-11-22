# Exact worst-duration arrival lags for two delayed two-reservoir flood hydrographs

## Finding

Consider two equal instantaneous runoff inputs routed through identical two-reservoir Nash cascades, with the second input arriving a nonnegative time \(d\) after the first. In unit time and discharge units write
\[
 f(t)=\begin{cases}t e^{-t},&t\geq0,\\0,&t<0,\end{cases}
 \qquad Q_d(t)=f(t)+f(t-d).
\]
For a strictly positive hazard threshold \(h\), the *total exceedance duration*, including disconnected episodes, is
\[
 \mathcal T_h(d)=\operatorname{Leb}\{t\geq0:Q_d(t)>h\}.
\]
Here \(\operatorname{Leb}\) denotes one-dimensional Lebesgue measure (ordinary elapsed time for these smooth pulses).

**Theorem (exact global arrival-lag optimization).** For every \(0<h<e^{-1}\), define the two unique isolated-pulse level crossings
\[
 a_h=-W_0(-h)\in(0,1),\qquad b_h=-W_{-1}(-h)>1.
\]
Let \(W_0\) and \(W_{-1}\) denote the two real Lambert-\(W\) branches, and set
\[
 K(d)=(1+e^{-d})\exp\!\left(\frac{d e^{-d}}{1+e^{-d}}\right),
 \qquad c(d)=\frac{d}{1+e^{-d}},
\]
\[
 L(z)=-W_{-1}(-z)+W_0(-z),\qquad 0<z<e^{-1}.
\]
Then the **only possible global maximizing lags** on \([0,\infty)\) are \(0\) and \(b_h\). The global maximum is exactly
\[
 \boxed{\sup_{d\geq0}\mathcal T_h(d)
 =\max\left\{L(h/2),\;c(b_h)-W_{-1}(-h/K(b_h))-a_h\right\}.}
\]
The maximizing lag is uniquely \(0\) when the first displayed candidate is larger, uniquely \(b_h\) when the second is larger, and **both and only both** when they are equal. This is a complete, exact decision test for each \(h\); no assertion is made that the two candidates exchange order only once as \(h\) varies.

For \(e^{-1}\leq h<2e^{-1}\), the unique maximizing lag is \(d=0\), with duration \(L(h/2)\). For \(h\geq2e^{-1}\), exceedance duration is identically zero for every lag. In particular, synchronous pulses always maximize their possible **peak** discharge, but may fail to maximize **time above a hazard threshold**.

At the exact threshold \(h=1/4\), the global maximizer is the staggered arrival lag
\[
 d=b_{1/4}=2.153292364110\ldots,
\]
with duration \(4.293100050525\ldots\), compared with only \(3.117264331439\ldots\) for synchronous arrival. Thus synchronous timing understates the maximized modeled hazard duration by approximately \(37.72\%\) when expressed relative to synchronous duration.

## Assumptions and scope

Time and discharge are nondimensionalized by the common reservoir time constant and one input's volume. Each input is instantaneous and has equal positive volume; routing is linear, causal, and mass-conserving. The hydrograph \(t e^{-t}\) is the normalized impulse response of two identical linear reservoirs in series. Inputs do not alter the routing parameters. The flood hazard proxy is strictly the **measure of time with summed outlet discharge above a fixed discharge threshold**, not tidal or river stage, inundation area, largest peak, or the overlap of two separately thresholded drivers.

The theorem covers every real arrival lag \(d\geq0\) and every strictly positive \(h\); equality cases, isolated threshold contacts, and disconnected intervals use strict exceedance, with individual threshold-contact times contributing measure zero. The initial baseflow is zero. No finite time window is imposed.

## Proof

**1. Exact shape after the second arrival.** For \(t\geq d\), algebra gives
\[
 Q_d(t)=e^{-t}[t+e^d(t-d)]
 =K(d)\,[t-c(d)]e^{-[t-c(d)]}.
\]
Since \(d-c(d)=d/(1+e^d)<1\) for every \(d\geq0\), this post-arrival shape is initially increasing, reaches its sole maximum at \(c(d)+1>d\), and then strictly decreases to zero. Direct differentiation gives
\[
 \frac{d}{dd}\log K(d)=-\frac{d e^{-d}}{(1+e^{-d})^2}<0\quad(d>0),
\]
with \(K(0)=2\) and \(\lim_{d\to\infty}K(d)=1\). For a gamma-shaped pulse with multiplier \(K\), the width of its strict superlevel interval at height \(h\) is \(L(h/K)\) if \(h/K<e^{-1}\), and zero otherwise. Both real Lambert-\(W\) level crossings move inward as \(h/K\) grows, so \(L\) is strictly decreasing on \((0,e^{-1})\).

**2. Separation below the first level crossing.** Let \(0<h<e^{-1}\). For \(0\leq d<a_h\), \(f(t)<h\) throughout \(0\leq t\leq d\). Both exceedance crossings occur after the second arrival, hence
\[
 \mathcal T_h(d)=L(h/K(d)).
\]
It decreases strictly for \(0<d<a_h\), so the maximum over this interval occurs uniquely at \(d=0\), with \(\mathcal T_h(0)=L(h/2)\).

**3. Separation inside the isolated-pulse exceedance interval.** For \(a_h\leq d\leq b_h\), the first pulse exceeds \(h\) from \(a_h\) to \(d\), including equality at the endpoints where appropriate. The post-arrival response begins at \(Q_d(d)=f(d)\geq h\) and reaches a single higher maximum. In addition,
\[
 Q_d(d+1)=f(d+1)+f(1)>e^{-1}>h.
\]
Consequently its unique final downward crossing \(R_h(d)\) satisfies \(R_h(d)>d+1\), and the entire exceedance set is one interval modulo isolated equality points, with
\[
 R_h(d)=c(d)-W_{-1}(-h/K(d)),\qquad
 \mathcal T_h(d)=R_h(d)-a_h.
\]
Implicitly differentiate \(f(R_h(d))+f(R_h(d)-d)=h\). Because \(R_h(d)>d+1\), both arguments lie on the strictly decreasing limb of \(f\), and thus
\[
 R_h'(d)=\frac{f'(R_h(d)-d)}{f'(R_h(d))+f'(R_h(d)-d)}>0.
\]
It follows that \(\mathcal T_h(d)\) increases strictly throughout \((a_h,b_h)\). Its unique maximum on this closed segment is at \(d=b_h\).

**4. Separation after the isolated-pulse decline.** For \(d>b_h\), the first exceedance interval \((a_h,b_h)\) ends *before* the second input. Since \(f(d)<h\), the post-arrival response starts below \(h\) and generates a separate interval, whose length is \(L(h/K(d))\). The post-arrival peak is above \(h\), because \(K(d)>1\) and \(h<e^{-1}\). Therefore
\[
 \mathcal T_h(d)=b_h-a_h+L(h/K(d)),\qquad d>b_h.
\]
This decreases strictly with \(d\); its limiting value as \(d\downarrow b_h\) matches the value from Step 3. Combining Steps 2–4 proves that **all** global maximizers are in \(\{0,b_h\}\) and gives the exact maximum and all ties.

**5. Higher thresholds and peak contrast.** If \(h\geq e^{-1}\), the first pulse never strictly exceeds \(h\) before the second input, since \(f(t)\leq e^{-1}\). For \(e^{-1}\leq h<2e^{-1}\), all exceedance is on the post-arrival curve, so \(\mathcal T_h(d)=L(h/K(d))\) whenever \(h/K(d)<e^{-1}\), and is zero otherwise. The strict decrease of \(K\) yields the unique maximum at \(0\). If \(h\geq2e^{-1}\), the pointwise bound \(Q_d(t)\leq2e^{-1}\) gives zero duration everywhere. Finally, the bound is attained for the synchronous pulses at \(t=1\), whereas no positive lag can place both component peaks at one time, establishing the stated contrast between peak and duration objectives.

**6. A genuine preference difference and transition.** For \(h=1/4\), exact rational exponential enclosures (reproduced in `checks/verify.py`) prove
\[
 0.357<a_h<0.358,\quad 2.153<b_h<2.154,
\]
\[
 Q_{b_h}(4.65)>1/4,\qquad f(3.3)<1/8.
\]
On the final declining limb the first inequality forces \(R_{1/4}(b_h)>4.65\), so the delayed duration exceeds \(4.65-0.358=4.292\). The final synchronous crossing is less than \(3.3\), so its entire duration is less than \(3.3\). Hence the delayed option strictly wins, without reliance on rounded decimal output. Conversely, as \(h\uparrow e^{-1}\), the lower and upper isolated crossings both converge to \(1\), and the delayed candidate approaches \(L(e^{-1}/K(1))<L(e^{-1}/2)\). Continuity establishes that the synchronous option wins at sufficiently high subcritical thresholds and that **at least one** preference crossover occurs. The number of such crossovers is not classified here. This completes the proof.

## Verification

The standalone standard-library script `checks/verify.py` contains exact-rational exponential-tail enclosures for all inequalities required in the \(h=1/4\) witness. It independently computes superlevel interval lengths using bracketed monotone crossing searches (without the candidate-formula case split), and checks the formulas on 1,100 pseudorandom threshold/lag pairs, 8,008 regular-grid dominance cases, and 30 higher-threshold comparisons. The observed maximum absolute discrepancy for independent crossing measurements is below \(6\times10^{-15}\) in these tests. The exact witness and the symbolic argument, not finite numerical sampling, prove the all-parameter theorem.

To reproduce from the package, save all embedded files preserving their relative paths and run `python3 checks/verify.py` from that directory. No external Python packages, downloads, or input data are needed. The expected success line begins `VERIFY_OK`.

## Relationship to prior work

The two-reservoir Nash unit hydrograph and linear summation of rain responses are established hydrological primitives. Gnecco, Palla, and La Barbera (2018) derive peak-oriented analytical relationships for gamma-type unit hydrographs. Lyddon and colleagues (2022) motivate above-threshold **duration**, hydrograph-relative timing, and compound-event overlap using fitted gamma curves, but treat individual-driver duration and overlap, not total exceedance duration of their sum. Lyddon and colleagues (2024) simulate the effect of alternative driver lags on estuarine flooding area, rather than classify a continuous optimization of the summed two-reservoir discharge's exceedance duration.

Related published mathematical findings classify **local crest number** for delayed four-stage hydrographs, delayed three-stage hydrographs, and two-rate parallel two-stage cascades. Those results do not imply the present all-threshold global-duration optimizer: crest count, largest peak, and time above a fixed level are distinct functionals, and those works do not give the \(\{0,b_h\}\) alternative or its exact comparison. Existing probability-density level-set widths and Lambert-\(W\) formulas are used as standard ingredients rather than claimed as discoveries. The exact arrival-lag optimization under this particular objective is the contribution assessed here; broader historical priority is not claimed conclusively.

## Limitations

The theorem is exact for two *equal*, *instantaneous*, fixed-kernel impulses through the same two-reservoir cascade. Unequal pulse volumes, finite rainfall durations, different response times, nonzero baseflow, tide–river hydraulic coupling, field flood elevations, nonlinear saturation, and a finite observation horizon can change the optimum. The discharge threshold is nondimensional and does not translate directly into inundation or damage risk. The preference-crossover count as a function of threshold is not proved unique. General rearrangement and translated-density level-set literature may contain earlier equivalents and remains a historical-priority risk. No independent external validation or field calibration is asserted.

## References

1. Lyddon, C., et al. *Historic Spatial Patterns of Storm-Driven Compound Events in UK Estuaries*. Estuaries and Coasts **46**, 30–56 (2023); first published online 31 August 2022. https://doi.org/10.1007/s12237-022-01115-4.
2. Gnecco, I., Palla, A., and La Barbera, P. *A dimensionless approach for the runoff peak assessment: effects of the rainfall event structure*. Hydrology and Earth System Sciences **22**, 943–956 (2018). https://doi.org/10.5194/hess-22-943-2018.
3. Lyddon, C., et al. *Thresholds for estuarine compound flooding using a combined hydrodynamic–statistical modelling approach*. Natural Hazards and Earth System Sciences **24**, 973–997 (2024). https://doi.org/10.5194/nhess-24-973-2024.
4. Nash, J. E. *The Form of the Instantaneous Unit Hydrograph* (1957), as cited and discussed in Gnecco, Palla, and La Barbera (2018).
