# A sharp source-to-remote filtration transition in a two-zone pollutant model

## Finding

For a fixed linear filtration budget across two interacting equal-volume compartments, three natural steady pollutant objectives have **three distinct optimal placement laws**. The concentration in the only emitting room is uniquely minimized by placing every unit of filtration there. The concentration in the source-free room is uniquely minimized by splitting filtration equally. By contrast, the *sum of both concentrations* makes a sharp budget-dependent transition: all filtration belongs in the source room at low budgets, but above a closed-form threshold a strictly positive, sub-half share should be moved to the source-free room.

Explicitly, with local baseline loss rate \(r>0\), interroom exchange \(m>0\), fixed source intensity \(q>0\), total filtration rate \(B>0\), and remotely allocated amount \(y\in[0,B]\), the unique whole-space optimizer is

\[
y_*(B)=\begin{cases}0,&B\le 2r+r^2/m,\\ \sqrt{m(B+2r+4m)}-r-2m,&B>2r+r^2/m.\end{cases}
\]

When positive, \(y_*(B)<B/2\). For large budgets, \(y_*(B)\sim\sqrt{mB}\) and the fractional whole-space reduction relative to allocating everything to the source room approaches \(m/(r+2m)\).

## Assumptions and scope

There are two equal-volume, internally well-mixed rooms. A nonreactive contaminant has a constant external input only in room 1, denoted \(q>0\) in concentration-per-time units. Each room loses contaminants at the fixed first-order rate \(r>0\), and the rooms exchange air at symmetric per-volume rate \(m>0\). Additional linear removal is provided at fixed total per-volume rate \(B>0\). A decision variable \(y\in[0,B]\) assigns removal rate \(B-y\) to room 1 and \(y\) to room 2, without changing exchange or baseline loss. Both source and removal are time-independent. Dynamics are

\[
\dot c_1=q-(r+m+B-y)c_1+mc_2,\qquad
\dot c_2=mc_1-(r+m+y)c_2.
\]

For physical clean-air delivery rates and equal room volume \(V\), multiply the rate variables \(r,m,B,y\) by \(V\) to obtain volume-per-time units. Concentrations are compared at the unique attracting steady state; the equal-volume average is half their sum. No emission from room 2 or exogenous contaminated air input is assumed.

## Proof

Let \(a=r+m>0\) and define

\[
\Delta(y)=(a+B-y)(a+y)-m^2
 =r(r+2m)+(r+m)B+By-y^2.
\]

For every \(0\le y\le B\), \(\Delta(y)>0\) because \((a+B-y)(a+y)\ge a^2>m^2\). The linear system has negative trace \(-(2a+B)\) and positive determinant \(\Delta(y)\), hence a strictly stable equilibrium. Cramer's rule yields

\[
C_1(y)=\frac{q(a+y)}{\Delta(y)},\qquad
C_2(y)=\frac{qm}{\Delta(y)},\qquad
J(y)=C_1+C_2=\frac{q(r+2m+y)}{\Delta(y)}.
\]

**Source-room objective.** Differentiating gives

\[
C_1'(y)=\frac{q\{r(r+2m)+2(r+m)y+y^2\}}{\Delta(y)^2}>0.
\]

Thus \(C_1\) increases strictly in \(y\) and its unique minimum is at \(y=0\).

**Remote-room objective.** Since \(C_2(y)=qm/\Delta(y)\), minimizing it means maximizing the strictly concave quadratic \(\Delta(y)\); its unique vertex is \(y=B/2\).

**Whole-space objective.** Direct differentiation gives

\[
J'(y)=\frac{qP_B(y)}{\Delta(y)^2},\quad
P_B(y)=y^2+2(r+2m)y+r(r+2m)-mB.
\]

For \(y\ge0\), the polynomial \(P_B\) increases strictly because \(P_B'(y)=2y+2(r+2m)>0\). It starts at \(P_B(0)=r(r+2m)-mB\), which is nonnegative precisely for \(B\le 2r+r^2/m\). In that regime \(J\) is strictly increasing in \(y>0\) and uniquely minimized at zero. If \(B>2r+r^2/m\), then \(P_B(0)<0\), but \(P_B(B/2)=B^2/4+(r+m)B+r(r+2m)>0\). There is exactly one critical point \(y_*\in(0,B/2)\), and \(J'\) changes from negative to positive there. It is the unique global minimum over \([0,B]\). Solving \(P_B(y_*)=0\) gives the asserted square-root expression.

**High-budget limit.** Since \(y_*\sim\sqrt{mB}\), its fractional budget share tends to zero. Source-only allocation has

\[
J(0)=\frac{q(r+2m)}{(r+m)(r+m+B)-m^2}
\sim \frac{q(r+2m)}{(r+m)B}.
\]

At the interior optimum, substituting \(P_B(y_*)=0\) yields \(J(y_*)=q/[B+2r+4m-2\sqrt{m(B+2r+4m)}]\sim q/B\). Therefore

\[
\lim_{B\to\infty}\frac{J(y_*)}{J(0)}=\frac{r+m}{r+2m},\qquad
\lim_{B\to\infty}\frac{J(0)-J(y_*)}{J(0)}=\frac{m}{r+2m}>0.
\]

All inequalities are strict wherever stated, and all results hold for every positive parameter triple and every positive budget, including the exact threshold.

## Verification

Run the accompanying dependency-free Python script `checker.py` with Python 3. It checks the stationary equations and derivative identities on deterministic and pseudorandom positive parameters; verifies objective minimizers numerically including budget thresholds; and reproduces a dimensional illustrative example. The proof, not its finite numerical checks, establishes the uniform result.

**Illustrative benchmark.** Two rooms of volume \(50\,\mathrm{m}^3\) each have baseline removal \(25\,\mathrm{m}^3/\mathrm{h}\) per room, exchange \(50\,\mathrm{m}^3/\mathrm{h}\), total filtration \(300\,\mathrm{m}^3/\mathrm{h}\), and a source only in room 1 of \(2000\,\mu\mathrm{g}/\mathrm{h}\). The corresponding rates are \(r=0.5\,\mathrm{h}^{-1}\), \(m=1\,\mathrm{h}^{-1}\), \(B=6\,\mathrm{h}^{-1}\), and \(q=40\,\mu\mathrm{g}\,\mathrm{m}^{-3}\mathrm{h}^{-1}\). The sharp threshold is \(B_c=1.25\,\mathrm{h}^{-1}\), so the unique optimal remote filtration is \(y_*\approx0.81662479\,\mathrm{h}^{-1}\), or \(40.83124\,\mathrm{m}^3/\mathrm{h}\). The source-room filtration is the remaining \(259.16876\,\mathrm{m}^3/\mathrm{h}\). The two-room mean concentration is approximately \(4.58006\,\mu\mathrm{g}/\mathrm{m}^3\), versus \(4.87805\) when all filtration is at the source and \(5.71429\) under an equal split. These are model calculations, not measured performance.

## Relationship to prior work

Du et al. (2012) empirically motivate two-zone indoor pollution models with localized emissions, interzonal flow and air filters; their model and scenario study do not state this fixed-budget continuous allocation theorem. Novoselac and Siegel (2009) analyze multizone portable air-cleaner placement with simulation, rather than proving an exact budget splitting threshold. Kikumoto and Ooka (2022/2023) optimize the physical position of an air cleaner through an adjoint concentration model, not steady allocation between two communicating boxes. The later Airgle multiroom example directly writes the same two-room balance equations and compares *all-in-one-room* against *equal-split* allocations, including a source-only scenario. That example already supplies the physical model and the finite two-design comparison. The precise claim here is only the newly derived continuous optimum, its threshold, the three-objective separation and its high-budget limit. Full priority is not proved; other unindexed air-filtration optimization studies or general rational allocation theorems could subsume it.

## Limitations

The theorem assumes equal volumes and identical baseline loss, symmetric exchange independent of filtration placement, one constant source, a passive contaminant and strictly linear removal. Real filters have nonlinear airflow and pollutant-dependent performance; air movement, spatial gradients, source fluctuations and occupancy priorities can change practical decisions. The conclusion concerns ideal steady concentration, not transient exposure, infection, health or device selection. Historical originality is supported by targeted comparisons rather than an exhaustive review, and there is no independent scientific audit.

## References

- Du, L., Batterman, S., et al. (2012), *Air Change Rates and Interzonal Flows in Residences, and the Need for Multi-Zone Models for Exposure and Health Analyses*, International Journal of Environmental Research and Public Health 9, 4639–4661. https://doi.org/10.3390/ijerph9124639 (publicly dated 12 December 2012).
- Novoselac, A. and Siegel, J. (2009), *Impact of placement of portable air cleaning devices in multizone residential environments*, Building and Environment 44, 2348–2356. https://doi.org/10.1016/j.buildenv.2009.03.023.
- Kikumoto, H. and Ooka, R. (first online 2022), *Study on influence of air cleaner on room dispersion field and its optimal placement using adjoint concentration*, Japan Architectural Review 6, e12318. https://doi.org/10.1002/2475-8876.12318.
- Airgle Research (online multiroom example accessed 2026), *One Larger Air Purifier or Two Smaller Units? A Multiroom Comparison*. https://www.airgle.com/research/one-large-or-two-small-air-purifiers.
