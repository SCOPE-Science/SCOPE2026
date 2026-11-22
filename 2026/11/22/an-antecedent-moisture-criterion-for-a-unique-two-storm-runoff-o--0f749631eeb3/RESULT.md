# An antecedent-moisture criterion for a unique two-storm runoff-order reversal

## Finding
Consider a finite soil-water store of capacity \(C>0\), initially holding \(0<s<C\), and two instantaneous rainfall depths \(A>B>0\) separated by a strictly positive interval. Between the impulses, water is lost at a possibly time-varying nonnegative proportional rate with finite positive integrated loss \(K\), so the storage retention factor is \(q=e^{-K}\in(0,1)\). Each impulse spills precisely the water above capacity. Denote total two-event saturation-excess runoff for the larger-then-smaller sequence by \(W_{AB}\), and for the reverse sequence by \(W_{BA}\), retaining the same initial water, depths and inter-event loss profile.

Write \(\Delta=W_{AB}-W_{BA}\). The exact and exhaustive comparison is:

1. If \(s+A\le C\), then \(\Delta\le0\) for every \(K>0\).
2. If \(s+B\ge C\), then \(\Delta\ge0\) for every \(K>0\).
3. If \(s+B<C<s+A\), there is exactly one strict order reversal as \(K\) grows, at

\[
\boxed{K_c=\log\!\left(1+\frac Bs\right)}.
\]

Specifically, \(\Delta<0\) for \(0<K<K_c\), \(\Delta=0\) only at \(K=K_c\), and \(\Delta>0\) for \(K>K_c\). Thus a reversal is possible **if and only if** the larger first rain would initially overflow the store and the smaller would not. The loss-dose threshold is independent of the larger storm depth \(A\), the capacity \(C\) (subject to the straddling inequalities), and the temporal profile of the linear-loss rate. The inequalities in cases 1 and 2 deliberately allow ties.

For a constant proportional drainage rate \(\lambda>0\), the unique crossover gap is \(T_c=\lambda^{-1}\log(1+B/s)\). In the straddling regime, shorter gaps favor smaller-first as the higher-runoff order; longer gaps favor larger-first.

## Assumptions and scope
Let \([x]_+=\max\{x,0\}\). An instantaneous rain depth \(u\ge0\) applied to a store at \(x\in[0,C]\) produces new storage \(x^+=\min\{C,x+u\}\) and immediate saturation-excess runoff \(w=[x+u-C]_+\). No infiltration-excess runoff, supplementary water input, stormwater recapture or threshold hysteresis is included. During the rain-free interval \([0,T]\), storage solves \(\dot x=-k(t)x\), where \(k\) is nonnegative and Lebesgue-integrable and \(0<K=\int_0^T k(t)\,dt<\infty\). Impulse timings are fixed; the two rain depths alone are interchanged. Runoff is measured at both impulses, with no third event or runoff-routing stage. The time profile of \(k\) does not influence the retention factor beyond its integral.

Direct substitution yields the exact identity

\[
\begin{aligned}
\Delta={}&[s+A-C]_+-[s+B-C]_+\\
&+[q\min\{C,s+A\}+B-C]_+\\
&-[q\min\{C,s+B\}+A-C]_+.
\end{aligned}
\]

The classification is for positive unequal rain depths and a strictly interior antecedent moisture state. The equal-depth case has identical sequences and is excluded; a completely dry or saturated initial store can produce degenerate boundary behavior and is not part of the strict-reversal theorem.

## Proof
The scalar loss equation gives \(x(T)=qx(0)\) with \(q=e^{-K}\), even when \(k(t)\) varies, and the impulse rule yields the displayed exact difference.

**Neither first storm saturates.** If \(s+A\le C\), the first overflows vanish. The two second-event overflow arguments differ by

\[
(q(s+B)+A-C)-(q(s+A)+B-C)=(A-B)(1-q)>0.
\]

Monotonicity of the positive part gives \(\Delta\le0\), including the equality case \(s+A=C\).

**Both first storms saturate.** If \(s+B\ge C\), their first-event runoff difference is \(A-B\), and both retain \(C\). Therefore

\[
\Delta=A-B+[qC+B-C]_+-[qC+A-C]_+\ge0,
\]

because the positive-part function is nondecreasing and 1-Lipschitz. This includes \(s+B=C\).

**Exactly the larger storm saturates.** If \(s+B<C<s+A\), set \(y=s+B\in(0,C)\). Then

\[
\Delta=s+A-C+[qC+B-C]_+-[qy+A-C]_+.
\]

Put \(q_c=s/y\in(0,1)\). For \(0<q<q_c\), one has \(qy<s\), and hence \([qy+A-C]_+<s+A-C\), which is strictly positive. The extra second-overflow term is nonnegative, proving \(\Delta>0\). For \(q>q_c\), the last positive part is active, so

\[
\Delta=s-qy+[qC+B-C]_+.
\]

If \(qC+B\le C\), this is strictly negative. Otherwise it equals \((1-q)(s+B-C)<0\). At \(q=q_c\), the last positive part equals \(s+A-C\), while the middle one vanishes: indeed \(q_cC+B<C\) is equivalent, after multiplying by \(s+B\), to \(B(s+B-C)<0\). Hence \(\Delta=0\) at precisely \(q_c\). Since \(q=e^{-K}\), this gives the asserted signs and unique critical \(K_c=-\log q_c=\log(1+B/s)\).

The three cases partition the domain because \(s+B<s+A\). In the two weak-sign cases no strict sign reversal is possible, and the third is a strict reversal. This proves both necessity and sufficiency, all stated boundaries, and independence of the rate profile.

## Verification
For \(C=1\), \(s=4/5\), \(A=2/5\), and \(B=1/10\), the straddling inequalities hold. The exact critical retention is \(q_c=8/9\), equivalently \(K_c=\log(9/8)\). At \(q=1/2\), direct counting gives \(\Delta=1/5\); at \(q=9/10\), \(\Delta=-1/100\); at \(q=8/9\), it is exactly zero. The crossover remains \(8/9\) when \(A\) changes among \(1/4,2/5,7/10,3\), all of which straddle the same capacity with the smaller pulse.

The standalone standard-library checker `verify.py` implements the pulse-and-loss recurrence in exact rational arithmetic. It checks the displayed difference, all three sign regimes, strictness and exact equality on **46,683** rational parameter combinations with several capacities, and separately tests the example and the larger-storm independence. Run `python3 verify.py`. These calculations corroborate boundaries but the preceding proof, not a finite census, establishes the universal theorem.

## Relationship to prior work
Zheng and coauthors (2023) analyze rainfall-runoff event variability across 431 Great Britain catchments; their full methods and conclusions identify storm depth and antecedent moisture as important drivers of runoff coefficients. Their empirical comparisons do not classify deterministic two-event runoff orderings. Bartlett and coauthors (2015, particularly Sections 2–3) establish the classic single-store stochastic rainfall/soil-moisture framework and an explicit pure saturation-threshold transformation; their full-text analysis develops runoff probability densities and associated stochastic dynamics, rather than this two-depth **transient initial-state** permutation theorem. The bucket update itself is established hydrological modeling, and is not claimed as new.

Two related published mathematical results concern the same type of storage recurrence but take **stationary periodic** inputs: *A sharp storm-ordering window for saturation runoff in a periodic linear store* (2026) compares two three-event cyclic permutations, while *Exact cyclic-gap law for saturation-excess runoff from two periodic storms* (2026) compares spacing of equal pulses. Neither statement fixes an arbitrary positive transient initial storage and exchanges two unequal rain depths; a cyclic initial state cannot be freely prescribed. The published *A sharp rainfall sequencing law for a Green–Ampt infiltration model* (2026) concerns a different infiltration equation with nondecreasing wetting front and no interstorm drying. Its strong rearrangement result does not imply the present order reversal. Classical finite-dam and buffer interchange results could still include an equivalent transient criterion under other terminology; the inspected sources do not resolve exhaustive priority.

The new assertion is the **complete necessary-and-sufficient antecedent-state criterion and the universal one-crossover integrated-loss formula**, not the elementary storage update, the hydrological relevance of wetness, or a claim about field-scale calibrated performance.

## Limitations
The model has one spatially homogeneous capped store, instantaneous pulses, linear proportional inter-event drainage and pure saturation-excess runoff. Nonlinear evaporation, recharge during the interval, soil heterogeneity, runoff routing, spatially varying saturated areas, three or more storms, and other hydrological mechanisms may change the classification. It predicts modeled two-event overflow volume, not a hydrograph peak or watershed-level flood risk. The result has no empirical calibration; mathematically equivalent finite-buffer work outside the inspected literature remains a historical-priority risk.

## References
1. Zheng, Y., Coxon, G., Woods, R., Li, J., and Feng, P. (2023), *Controls on the Spatial and Temporal Patterns of Rainfall-Runoff Event Characteristics—A Large Sample of Catchments Across Great Britain*, Water Resources Research 59, e2022WR033226. First publicly published 2023-05-22. https://doi.org/10.1029/2022WR033226.
2. Bartlett, M. S., Daly, E., McDonnell, J. J., Parolari, A. J., and Porporato, A. (2015), *Stochastic rainfall-runoff model with explicit soil moisture dynamics*, Proceedings of the Royal Society A 471, 20150389. https://doi.org/10.1098/rspa.2015.0389. Open manuscript: https://water.usask.ca/hillslope/documents/pdfs/2015/Bartlett_Stochastic_20150389.full.pdf.
3. *A sharp storm-ordering window for saturation runoff in a periodic linear store* (2026), public research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-storm-ordering-window-for-saturation-runoff-in-a-periodi--d7dd28e86fa3.
4. *Exact cyclic-gap law for saturation-excess runoff from two periodic storms* (2026), public research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-cyclic-gap-law-for-saturation-excess-runoff-from-two-perio--e537d5c1eb7c.
5. *A sharp rainfall sequencing law for a Green–Ampt infiltration model* (2026), public research record: https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-rainfall-sequencing-law-for-a-green-ampt-infiltration-mo--955c7a9f5dc3.
