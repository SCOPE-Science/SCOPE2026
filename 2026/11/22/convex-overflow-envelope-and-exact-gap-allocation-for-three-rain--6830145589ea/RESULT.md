# Convex overflow envelope and exact gap allocation for three rain pulses

## Finding

For an initially empty finite-capacity store with exponential inter-event drying, fix **three positive rainfall depths** in a prescribed order and fix the times of the first and last event. The exact total saturation-excess spill is convex both in the middle event time and in the fraction of first-event water retained before the middle event. The retention variable yields a complete finite-candidate global minimization theorem, including the full interval of zero additional spill when one exists and a unique optimum when additional spill is unavoidable.

Let \(C,k,T,a,b,c>0\). The three pulses of depths \(a,b,c\) occur at times \(0,t,T\), with \(0\le t\le T\). Write
\[
E=e^{-kT}\in(0,1),\qquad x=e^{-kt}\in[E,1],\qquad u=\min\{a,C\}>0.
\]
The cumulative excess spill is **exactly**
\[
R(x)=(a-C)_+ +\max\!\left\{0,\;ux+b-C,\;Eu+\frac{Eb}{x}+c-C,\;ux+b+\frac{EC}{x}+c-2C\right\},\tag{1}
\]
where \((z)_+=\max\{z,0\}\). In particular \(R(x)\) is convex in \(x\), and \(t\mapsto R(e^{-kt})\) is also convex on \([0,T]\).

The possible minimizers are completely characterized. Define the **finite candidate set** \(\mathcal K\) by intersecting \([E,1]\) with
\[
\left\{E,1,\frac{C-b}{u},\sqrt{\frac{EC}{u}}\right\}
\ \cup\ \left\{\frac{EC}{C-c}:c<C\right\}
\ \cup\ \left\{\frac{Eb}{C-c-Eu}:C-c-Eu>0\right\}.\tag{2}
\]
Then
\[
\min_{E\le x\le1}R(x)=\min_{x\in\mathcal K}R(x).\tag{3}
\]
When the minimum exceeds the unavoidable first-event spill \((a-C)_+\), its optimizer is **unique** and belongs to \(\mathcal K\). If there is no additional spill, the entire set of optimal transformed times is exactly
\[
\mathcal Z=[E,1]\cap\left[\frac{Eb}{C-c-Eu},\frac{C-b}{u}\right],\tag{4}
\]
provided \(b<C\) and \(C-c-Eu>0\); otherwise \(\mathcal Z\) is empty. An empty intersection means an additional spill cannot be avoided. Every \(x\in\mathcal Z\) is optimal, even if the first pulse already spilled.

A particularly interpretable interior regime occurs if
\[
u>EC,\qquad b>C-\sqrt{uEC},\qquad c>C-\sqrt{uEC}.\tag{5}
\]
Then **both later events spill at the optimum**, which is uniquely
\[
x_*=\sqrt{\frac{EC}{u}},\qquad
 t_* =\frac{T}{2}+\frac{1}{2k}\log\frac{u}{C},\qquad
 R_*= (a-C)_+ +b+c-2C+2\sqrt{uEC}.\tag{6}
\]
Conversely, an interior smooth optimum at which both later events strictly spill must satisfy the inequalities in (5), and (6). Since \(u\le C\), the interior optimum in this regime occurs *at or before the midpoint*; it is strictly before whenever \(u<C\).

Equal gaps need not even approximate an optimal gap allocation up to a fixed multiplicative factor. For every integer \(n\ge2\), choose
\[
C=1,\quad a=\frac12,\quad b=\frac14,\quad E=\frac1{n^2},\quad c=1-\frac{1}{2n^2}.
\]
The minimum overflow is \(1/(4n^2)\), achieved **uniquely** by \(x=1\), whereas equal temporal gaps give \(x=1/n\) and total overflow \(1/(4n)\). Their ratio is exactly \(n\), hence unbounded. The durations, rather than the rainfall depths alone, control this failure of an equal-spacing heuristic.

## Assumptions and scope

A scalar nonnegative storage \(s\in[0,C]\) starts at \(s(0^-)=0\). Rainfall is instantaneous at \(0,t,T\). Whenever a pulse of size \(v\) arrives, immediately spill \((s+v-C)_+\) and retain \(\min(C,s+v)\). Between pulses storage obeys \(\dot s=-ks\), with constant \(k>0\); there is no other inflow, evaporation threshold, release control, or spill between pulses. At coincident pulse times \(t=0\) or \(t=T\), apply the pulses sequentially; the total overflow is independent of their within-instant order. The objective is the **sum of the three overflow volumes**, not peak runoff rate or final storage.

All parameters \(C,k,T,a,b,c\) are positive and finite. The arrival order of depths \(a,b,c\) is *fixed*: only the time \(t\) of the middle pulse varies. The transformation \(x=e^{-kt}\) is a decreasing bijection between \([0,T]\) and \([E,1]\), so minimization on the transformed interval is equivalent to minimization over the available middle-event times.

## Proof

**1. Exact recurrence.** The first pulse spills \(r_1=(a-C)_+\) and leaves \(u=\min(C,a)\). Immediately before the second pulse the store holds \(ux\), so its spill is \(r_2=(ux+b-C)_+\) and its post-event storage is \(s_2=\min(C,ux+b)\). The fraction retained until the third pulse is \(E/x\), so \(r_3=((E/x)s_2+c-C)_+\). Thus
\[
R(x)=(a-C)_++(ux+b-C)_+ +\left(\frac{E}{x}\min(C,ux+b)+c-C\right)_+.\tag{7}
\]

**2. Four-branch convex identity.** Put \(w=ux+b\), and set
\[
A=w-C,\quad B=Eu+\frac{Eb}{x}+c-C,\quad D=w+\frac{EC}{x}+c-2C.
\]
When \(w\le C\), the second pulse cannot spill, so \(r_2+r_3=\max(0,B)\). Moreover \(A\le0\), and
\[
D-B=(w-C)(1-E/x)\le0,
\]
because \(E\le x\). Hence \(r_2+r_3=\max(0,A,B,D)\) on this branch. When \(w\ge C\), the second pulse spills \(A\ge0\), and the third sees capacity \(C\): consequently \(r_2+r_3=\max\{A,D\}\). The same identity above gives \(D\ge B\), so the same four-branch maximum applies. This proves (1) at all points, including boundaries.

The four terms in (1) have second derivatives in \(x\) equal to \(0,0,2Eb/x^3\) and \(2EC/x^3\), respectively, so their maximum is convex in \(x\). Substituting \(x=e^{-kt}\) into the four terms gives second derivatives in \(t\) equal to \(0,k^2u e^{-kt},k^2Eb e^{kt}\) and \(k^2(u e^{-kt}+EC e^{kt})\), respectively. The maximum is therefore convex in \(t\) as well. The first-event spill is constant and does not change either conclusion.

**3. Finite candidate completeness and uniqueness.** On the region \(ux+b<C\), additional spill is \(\max(0,B)\). The positive branch \(B\) is strictly decreasing, and the only possible change to or from zero occurs at \(x=Eb/(C-c-Eu)\), when its denominator is positive. The boundary between unsaturated and saturated second pulses is \(x=(C-b)/u\). On the region \(ux+b>C\), additional spill is \(\max(A,D)\), since \(D\ge B\). The branches \(A\) and \(D\) meet exactly where the third overflow becomes zero, \(x=EC/(C-c)\), provided \(c<C\). The positive \(A\) branch is strictly increasing. The strictly convex \(D\) branch has its sole stationary point at \(x=\sqrt{EC/u}\). Therefore, any positive minimum is either at an interval endpoint, one of these branch-change points, or the single stationary point. These are exactly the admissible candidates (2), proving (3).

If a positive additional-spill minimum were attained at two distinct points, convexity would force the entire intervening open interval to share that strictly positive minimum. On that interval, at least one of the four analytic component functions must equal the minimum at infinitely many points with an accumulation point. Analyticity would force that component to be constant, but only the identically zero component is constant: the others have strictly positive or negative first derivative, or strictly positive second derivative, since \(u,b,C,E>0\). Contradiction. Thus the positive-additional-spill optimum is unique.

**4. The exact zero-spill interval.** Both later events avoid overflow if and only if \(ux+b\le C\) and \((E/x)(ux+b)+c\le C\). The first inequality gives \(x\le(C-b)/u\). The second is equivalent to \(Eb/x\le C-c-Eu\) and, because \(Eb>0\), requires \(C-c-Eu>0\), then \(x\ge Eb/(C-c-Eu)\). Also \(b<C\) is necessary. Intersecting these constraints with \([E,1]\) gives precisely (4). Since first-event spill cannot be changed by moving \(t\), these and only these points globally minimize total spill whenever this interval is nonempty. Its left endpoint is either \(E\) or \(Eb/(C-c-Eu)\); either way it belongs to \(\mathcal K\), proving (3) also when no additional spill is needed.

**5. Sharp interior both-spill formula.** At an interior point where both later events strictly overflow, (7) reduces to \((a-C)_++D\). The derivative of \(D\) is \(u-EC/x^2\). Its unique zero is \(x_*=\sqrt{EC/u}\), and the second derivative is positive. This point lies inside \((E,1)\) precisely when \(u>EC\) (the lower bound follows automatically from \(u\le C\) and \(E<1\)). At that point the second and third positive overflow conditions are exactly \(b>C-\sqrt{uEC}\) and \(c>C-\sqrt{uEC}\). Conversely, under (5) the point \(x_*\) is interior, both later pulses spill, and \(D(x_*)=b+c-2C+2\sqrt{uEC}\). Since \(D\) is one component of a convex maximum, no other point can beat its strict global minimum \(D(x_*)\); the full objective equals \(D\) at \(x_*\), proving uniqueness and (6). The time expression follows by taking \(-\log(x_*)/k\).

**6. Unbounded penalty for equal gaps.** For the displayed family indexed by \(n\), first-event spill vanishes and the second post-event storage is \(ux+b=x/2+1/4\le3/4<C\) for all \(x\in[E,1]\). Thus the third event spills
\[
\frac{E}{x}\left(\frac{x}{2}+\frac14\right)+1-\frac E2-1=\frac{E}{4x}>0.
\]
This is strictly decreasing in \(x\), so its unique minimizer is \(x=1\), with value \(E/4=1/(4n^2)\). Equal gaps correspond to \(t=T/2\) and \(x=\sqrt E=1/n\); their spill is \(\sqrt E/4=1/(4n)\). The ratio equals \(n\), proving unboundedness.

## Verification

For an exact both-spill example take \(C=a=1\), \(b=c=9/10\), and \(E=1/4\). The conditions (5) hold, \(x_*=1/2\), and (7) gives \(R(x_*)=4/5\). Either endpoint \(x=1\) or \(x=E\) gives \(21/20\). The reduction relative to either endpoint is exactly \(5/21\), or about \(23.81\%\). The equal-gap choice happens to be optimal in this example; the second family proves it is not universally near-optimal.

Run the included `verify.py` using only the Python standard library: `python3 verify.py`. It independently evaluates the original three-event recurrence and the four-branch envelope for 648 rational choices of positive event depths and retention factor, checks convexity on rational midpoint grids, tests the precise zero-spill interval, and compares all finite-candidate minima against an independent 101-point grid. It also verifies the exact examples and selected arbitrary-gap penalty ratios by rational arithmetic. The script reports 88,156 successful exact or controlled-tolerance assertions. **These finite checks supplement, but do not establish, the universal assertions proved above.**

## Relationship to prior work

McGrath, Hinz and Sivapalan (2007, Sections 2 and 5 and Appendix A; discussion version public 1 September 2006) treat saturation-threshold runoff and stochastic inter-event times, deriving first-passage and runoff statistics for Poisson rainfall arrivals. They do not optimize a chosen middle arrival time with fixed endpoints and fixed event depths. Bartlett and colleagues (2015, model equations and appendices) similarly analyze stochastic rainfall/storage dynamics and their stationary distributions, not finite deterministic inter-event scheduling.

The periodic three-storm ordering result [5] and the periodic two-storm cyclic-gap result [6] require a cyclic stationary state. The empty-start ordering result [7] instead holds the gaps equal and varies the pulse order. Here the order and total duration are fixed, the depths need not be equal, and the middle event moves continuously. Those results do not give the four-branch envelope, zero-additional-spill interval, finite-candidate classification, or equal-gap penalty in this setting. The contribution is the timing characterization, not simple bucket recurrences, convexity of \(1/x\), or saturation-excess hydrology itself.

Miralles and colleagues (2010) discuss canopy interception including the complete-drying-between-storms assumption of the traditional Gash model, while Xu and colleagues (2020) optimize **controlled prestorm releases** based on forecasts. Both address relevant temporal water-storage effects, but neither supplies this passive-store gap-allocation theorem. General finite-buffer rearrangement and event-scheduling results could imply parts of it; no assertion of exhaustive historical priority is made.

## Limitations

The result depends on deterministic positive pulse depths, initially empty storage, homogeneous exponential loss, a scalar fixed capacity, instantaneous clipping, and a fixed first-to-last pulse duration. Its design variable is timing of a hypothetical middle rainfall event, not control of naturally occurring storms. The exact ratio comparison concerns **total modeled excess volume**, not a runoff peak, flood risk, storage usefulness, field-calibrated hydrological response, or stochastic performance. Neither the claims nor their proof extend automatically to general drying kinetics, infiltration-excess rules, spatially distributed stores, or more than three events. Historical priority beyond inspected source material remains provisional; an abstract finite-buffer theorem could subsume this special case.

## References

1. McGrath, G. S., Hinz, C., and Sivapalan, M. (2007). *Temporal dynamics of hydrological threshold events*. Hydrology and Earth System Sciences 11, 923–938. Public discussion 1 September 2006. DOI: 10.5194/hess-11-923-2007. https://hess.copernicus.org/articles/11/923/2007/hess-11-923-2007.pdf.
2. Bartlett, M. S., Daly, E., McDonnell, J. J., Parolari, A. J., and Porporato, A. (2015). *Stochastic rainfall-runoff model with explicit soil moisture dynamics*. Proceedings of the Royal Society A 471, 20150389. DOI: 10.1098/rspa.2015.0389.
3. Miralles, D. G., Gash, J. H. C., Holmes, T. R. H., de Jeu, R. A. M., and Dolman, A. J. (2010). *Global canopy interception from satellite observations*. Journal of Geophysical Research: Atmospheres 115, D16122. DOI: 10.1029/2009JD013530.
4. Xu, W. D., Burns, M. J., Cherqui, F., and Fletcher, T. D. (2020). *Real time control of rainwater harvesting systems: The benefits of increasing rainfall forecast window*. Water Resources Research 56, e2020WR027856. DOI: 10.1029/2020WR027856.
5. *A sharp storm-ordering window for saturation runoff in a periodic linear store* (2026). https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-a-sharp-storm-ordering-window-for-saturation-runoff-in-a-periodi--d7dd28e86fa3
6. *Exact cyclic-gap law for saturation-excess runoff from two periodic storms* (2026). https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-cyclic-gap-law-for-saturation-excess-runoff-from-two-perio--e537d5c1eb7c
7. *The largest-storm-first rule holds through three pulses but fails at four* (2026). https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-the-largest-storm-first-rule-holds-through-three-pulses-but-fail--e27dfe4f22cd
