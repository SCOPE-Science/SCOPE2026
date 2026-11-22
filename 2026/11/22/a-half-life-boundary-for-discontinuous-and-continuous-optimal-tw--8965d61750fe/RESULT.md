# A half-life boundary for discontinuous and continuous optimal two-bolus fractionation

## Finding

Consider two instantaneous, nonnegative concentration increments at fixed times \(0\) and \(\tau>0\), sharing a fixed total normalized increment \(d>0\). A drug concentration starts at zero and is eliminated at a constant fractional rate \(\lambda>0\); the concentration threshold is a fixed positive constant \(c\). The exact objective is **total time above the threshold on \([0,\infty)\)**, not the largest peak, a bacterial-killing endpoint, or concentration-time area. Write \(a\in[0,d]\) for the first increment divided by \(c\), so that the second is \(d-a\), and put \(q=e^{-\lambda\tau}\in(0,1)\).

For \(d\le1\), no allocation produces positive above-threshold duration and every allocation is optimal. For \(d>1\), the globally optimal first increment is completely classified as follows.

**Longer than one half-life:** If \(0<q<1/2\), put
\[
D_1=4(1-q),\qquad D_2=\frac{2(1-q)}q.
\]
Then \(1<D_1<D_2\), and the full set of maximizers is
\[
\operatorname*{argmax}_{0\le a\le d}\mathcal T(a)=
\begin{cases}
\{0,d\},&1<d<D_1,\\
\{0,2,d\},&d=D_1,\\
\{d/[2(1-q)]\},&D_1<d<D_2,\\
\{q^{-1}\},&d\ge D_2.
\end{cases}
\]
In particular, at the first threshold an **unequal, strictly positive split** of the budget suddenly ties the two single-bolus options. Just above the threshold, that split becomes uniquely optimal, and the first exposure interval ends strictly before the second administration: \(qa<1\).

**At most one half-life:** If \(1/2\le q<1\), then
\[
\operatorname*{argmax}_{0\le a\le d}\mathcal T(a)=
\begin{cases}
\{0,d\},&1<d\le q^{-1},\\
\{q^{-1}\},&d>q^{-1}.
\end{cases}
\]
The nonzero second dose emerges continuously from the all-first-dose option as \(d\) passes \(q^{-1}\). The optimal concentration immediately before the second dose is exactly the threshold, \(qa=1\), so the positive-duration regions meet without a subthreshold gap. The boundary \(q=1/2\) is exactly the separation of one pharmacokinetic half-life, \(\tau=\log(2)/\lambda\).

The optimal duration \(\mathcal T_{\max}=\lambda^{-1}\log V\) has a fully explicit factor \(V\). For \(d\le1\), \(V=1\). For \(d>1\) and \(q<1/2\),
\[
V=\begin{cases}
d,&d\le D_1,\\
d^2/[4(1-q)],&D_1<d<D_2,\\
[qd-(1-q)]/q^2,&d\ge D_2;
\end{cases}
\]
and for \(d>1\) and \(q\ge1/2\), \(V=d\) when \(d\le q^{-1}\), and \(V=[qd-(1-q)]/q^2\) when \(d>q^{-1}\). These formulae agree at the connecting boundaries.

There is also a sharp **unequal-split versus equal-split reversal**. For every \(0<q<1/2\) and every
\[
4(1-q)<d<\frac4{1+q},
\]
the best unequal split is strictly better than a single bolus, but the equal split \(a=d/2\) is strictly *worse* than a single bolus. For example, when \(q=1/4\) and \(d=31/10\), the maximizing first increment is \(a=31/15\). The exponentiated dimensionless durations are exactly \(961/300\) (optimal), \(31/10\) (one bolus), and \(961/320\) (equal split), in that strict descending order.

## Assumptions and scope

The model is a single well-mixed compartment with linear first-order elimination, instantaneous fully bioavailable inputs, no other input or residual concentration, and no subsequent dosing. The concentration increments are normalized by the same fixed threshold \(c\); for instance, a physical dose is divided by the distribution volume and then by \(c\). The two *times* are fixed, the amounts may be zero, and there is no maximum individual dose, peak-toxicity bound, cost for a second administration, finite end-of-observation time, oral absorption phase, nonlinear drug clearance, bacterial growth or killing, resistance evolution, or between-person variability. The objective \(\mathcal T\) is Lebesgue measure of \(\{t\ge0:C(t)>c\}\); changing the strict inequality to non-strict does not change its measure because threshold equality holds at only isolated times. The entire post-second-dose tail is included, even when it extends far beyond \(\tau\). The result is an exact mathematical exposure benchmark, **not a clinical dosing recommendation**.

For \(t\ge0\), the normalized profile is
\[
\frac{C(t)}c=\begin{cases}
a e^{-\lambda t},&0\le t<\tau,\\
\bigl[d-(1-q)a\bigr]e^{-\lambda(t-\tau)},&t\ge\tau.
\end{cases}
\]
At a dosing instant, the post-increment value is used, but a single instant does not affect the duration functional. All parameters and ranges in the finding are exact; no finite enumeration is used to claim a universal result.

## Proof

**1. Exact duration reduction.** Before the second administration, the positive-above-threshold time is
\[
\min\{\max\{\lambda^{-1}\log a,0\},\tau\},
\]
where the value is interpreted as zero for \(a=0\). After the second administration, the duration is
\[
\max\{\lambda^{-1}\log[d-(1-q)a],0\}.
\]
The post-second increment \(d-(1-q)a\) is nonnegative, and zero logarithm arguments again give duration zero. Exponentiating the sum yields the continuous, piecewise-polynomial factor
\[
\boxed{W(a):=e^{\lambda\mathcal T(a)}
=\min\{\max\{a,1\},q^{-1}\}\;\max\{1,d-(1-q)a\}.}
\]
Consequently maximizing duration is exactly maximizing \(W\). For \(d\le1\), both post-input concentrations are at most one, hence \(W\equiv1\). For \(d>1\), either unsplit allocation \(a=0\) or \(a=d\) has \(W=d\).

**2. The only potentially improving branch.** Put \(r=1-q\in(0,1)\). When \(a\le1\), the first factor of \(W\) is one and the second is at most \(d\), with equality only at \(a=0\) if \(d>1\). When \(d-ra\le1\), \(W\le\min\{\max\{a,1\},q^{-1}\}\le d\); its possible equality at the upper endpoint is already counted. When \(a\ge q^{-1}\) and \(d-ra>1\), the factor \(W=q^{-1}(d-ra)\) decreases strictly with \(a\). Therefore any strictly improving optimum must lie either on the interior branch
\[
1<a<q^{-1},\quad d-ra>1,\quad W(a)=a(d-ra),
\]
or at the clipping boundary \(a=q^{-1}\). The quadratic has derivative \(d-2ra\), second derivative \(-2r<0\), and unconstrained vertex \(a_0=d/(2r)\) with value \(d^2/(4r)\). Its maximum can exceed the unsplit value \(d\) only when \(d>4r\).

**3. Long-gap classification and exact ties.** Suppose \(q<1/2\), so \(r>1/2\). At \(d=4r\), the vertex is \(a_0=2\), which satisfies \(1<2<q^{-1}\), \(2<d\), and \(d-2r=2r>1\). Its quadratic value equals \(d\), and strict concavity shows that it is the only interior tie. Below \(4r\), strict concavity and the bound \(d^2/(4r)<d\) exclude all interior ties or improvements. Above \(4r\) the vertex is feasible until \(d=2r/q\): throughout this interval \(a_0>1\), \(a_0<d\), and \(d-ra_0=d/2>1\), while \(qa_0<1\) is strict before the upper endpoint. At and beyond \(d=2r/q\), the quadratic is increasing up to the boundary \(a=q^{-1}\); after that boundary the capped branch is strictly decreasing. Its value \([qd-r]/q^2\) exceeds \(d\) because their difference is \(r(qd-1)/q^2>0\) in this regime. The unique optimizer is therefore \(q^{-1}\). All equality cases and the displayed optimal values follow.

**4. Short-gap classification.** Suppose \(q\ge1/2\), so \(r\le1/2\). On \(0\le a\le\min\{d,q^{-1}\}\), the quadratic derivative obeys \(d-2ra\ge d(1-2r)\ge0\). Hence no strictly interior quadratic maximizer can improve on its right endpoint. If \(d\le q^{-1}\), the endpoint value of that quadratic is \(q d^2\le d\); the two unsplit allocations are the only maximizers. If \(d>q^{-1}\), the clipping boundary \(q^{-1}\) is feasible, its factor exceeds \(d\) by \(r(qd-1)/q^2>0\), and both sides of that boundary strictly decrease away from the optimizer in the appropriate direction. Thus \(a=q^{-1}\) is unique. At \(q=1/2\) and \(d=2\), the interior vertex and first-only endpoint coincide; there is no extra maximizer.

**5. Equal-split inversion.** If \(q<1/2\) and \(4r<d<4/(1+q)\), then \(1<d/2<q^{-1}\) and \(d-rd/2=d(1+q)/2>1\). Thus
\[
W(d/2)=\frac{d^2(1+q)}4<d=W(0)=W(d),
\]
whereas Steps 2–3 give \(\max_a W(a)>d\). For \(q=1/4,d=31/10\), substitution gives the three claimed exact rational factors. This proves the reversal on a nonempty open parameter region, rather than merely at an isolated example.

The branch inequalities, strict concavity, and clipping comparisons exhaust every \(a\in[0,d]\). Hence the classification and uniqueness statements hold for all real parameters in the stated domain.

## Verification

The included self-contained `verify.py` uses rational arithmetic to compute \(W(a)\) exactly and compares the analytical solution with all piecewise endpoints, transition points, and quadratic stationary points for thousands of rational parameter choices. It also checks exact one-sided boundary regimes and rational equal-versus-unequal fractionation examples. Executing `python verify.py` prints `VERIFY_OK assertions=183183`. This finite reproducibility check is ancillary; Steps 1–5 are a proof for the full continuous parameter domain.

At \(q=1/4,d=31/10\), the optimal split has normalized first dose \(31/15\) and second dose \(31/30\); the pre-second concentration is \(31/60<1\), illustrating the deliberately uncovered interval in the long-gap regime. The maximum duration is \(\lambda^{-1}\log(961/300)\), whereas equal splitting gives \(\lambda^{-1}\log(961/320)\), strictly less than the single-bolus \(\lambda^{-1}\log(31/10)\).

## Relationship to prior work

Time above minimum inhibitory concentration is a classical pharmacodynamic summary, and exponential clearance and impulse superposition are standard; these components are not claimed as new. Corvaisier and colleagues (1998) explicitly calculated the time-above-MIC index for one-compartment intravenous pharmacokinetic simulations over an initial 24-hour window and compared it with bacterial killing, rather than globally optimizing a fixed-total **two-bolus allocation over an unbounded tail**. Jacobs (2001) discussed time-dependent killing and exposure-based regimen design, not the exact global two-bolus optimizer or its half-life boundary. Ibrahim and colleagues (2004) experimentally compared several fixed standard and pulse metronidazole schedules with monoexponential washout, but did not establish an all-dose exact allocation law. Bachmann and colleagues (2024) numerically optimized antibiotic-associated bacterial-count/AUC targets using a substantially more elaborate dynamic model, not this explicitly solved level-set-duration objective.

Related mathematical results on periodic oral dosing optimize squared concentration fluctuation while varying temporal phase with fixed amounts, and on delayed oral inputs classify numbers of concentration peaks. Neither implies a discontinuous optimal dose-allocation transition for instantaneous boluses with a fixed interval and a level-set-duration objective. The result here is the exact phase diagram, including all ties, the half-life switch between jump and continuous onset, and the interval where *equal splitting loses despite the existence of a beneficial unequal split*. The priority comparison is limited to the inspected sources and nearby published mathematical results; no exhaustive historical novelty certification is asserted.

## Limitations

The exact statement concerns a deliberately minimal exposure functional, not antimicrobial effectiveness in patients. Real therapies are subject to peak toxicity, infusion/absorption kinetics, tissue distribution, resistance, dose granularity, finite treatment windows, repeated schedules, nonlinear elimination, and uncertain MIC or patient parameters; these constraints can change the optimizer or eliminate the mathematical jump. The benchmark allows a zero second dose and includes arbitrarily late above-threshold time, unlike steady-state percentage-of-interval measures. No clinical inference, patient recommendation, independent experimental validation, or generalization to more than two inputs is proved. Historical coverage remains potentially incomplete, especially for older nonuniform dosing calculations not available as lawful full text.

## References

1. Corvaisier, S., Maire, P. H., Bouvier d'Yvoire, M. Y., Barbaut, X., Bleyzac, N., and Jelliffe, R. W. (1998), *Comparisons between antimicrobial pharmacodynamic indices and bacterial killing as described by using the Zhi model*. Antimicrobial Agents and Chemotherapy 42, 1731–1737. First public journal date 1998-07-01. DOI: https://doi.org/10.1128/AAC.42.7.1731. Full HTML examined: https://journals.asm.org/doi/10.1128/aac.42.7.1731.
2. Jacobs, M. R. (2001), *Optimisation of antimicrobial therapy using pharmacokinetic and pharmacodynamic parameters*. Clinical Microbiology and Infection 7, 589–596. Published 2001-12-20. DOI: https://doi.org/10.1046/j.1198-743x.2001.00295.x. Full HTML: https://onlinelibrary.wiley.com/doi/full/10.1046/j.1198-743x.2001.00295.x.
3. Plusquellec, Y., De Biasi, J., and Souhait, J. (1999), *Concentration at steady-state after periodic and non-uniform administration of drug*. European Journal of Pharmaceutics and Biopharmaceutics 47, 305–307. DOI: https://doi.org/10.1016/S0939-6411(99)00017-X. Abstract and bibliographic record only; full text not inspected.
4. Ibrahim, K. H., Gunderson, B. W., Hermsen, E. D., Hovde, L. B., and Rotschafer, J. C. (2004), *Pharmacodynamics of pulse dosing versus standard dosing: in vitro metronidazole activity against Bacteroides fragilis and Bacteroides thetaiotaomicron*. Antimicrobial Agents and Chemotherapy 48, 4195–4199. Published 2004-11-01. DOI: https://doi.org/10.1128/AAC.48.11.4195-4199.2004. Full HTML: https://journals.asm.org/doi/full/10.1128/aac.48.11.4195-4199.2004.
5. Bachmann, F., Koch, G., Bauer, R. J., et al. (2024), *Computing optimal drug dosing regarding efficacy and safety: the enhanced OptiDose method in NONMEM*. Journal of Pharmacokinetics and Pharmacodynamics 51, 919–934. Published 2024-10-08. DOI: https://doi.org/10.1007/s10928-024-09940-9. Full HTML: https://link.springer.com/article/10.1007/s10928-024-09940-9.
