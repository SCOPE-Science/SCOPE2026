# A global clustering-to-midpoint switch under competing stress memories

## Finding

Consider three equal, idealized disturbance or thermal-stress pulses at times \(0,t,T\), where \(T>0\) is fixed and the middle time is freely chosen in \([0,T]\). Suppose the pairwise lag contribution to a cumulative stress-risk surrogate is
\[
 K(s)=a e^{-\alpha s}-b e^{-\beta s},\qquad a,b>0,\quad 0<\alpha<\beta,
\]
where the first term represents slower-decaying detrimental memory and the second term faster-decaying protective priming. Define
\[
 J_T(t)=K(t)+K(T-t)+K(T).
\]
The term \(K(T)\) is fixed by the endpoints. Let \(r=b/a\) and \(c=\alpha/\beta\), with \(0<c<1\).

**Global classification (all strictly positive parameters).** No time strictly between an endpoint and the midpoint can be a minimizer. Every global minimizer lies in \(\{0,T/2,T\}\), and:

1. If \(r\le c^2\), the midpoint \(t=T/2\) is the unique global minimizer for every \(T>0\).
2. If \(r\ge1\), the two endpoint-clustered schedules \(t=0\) and \(t=T\) are the only global minimizers for every \(T>0\).
3. If \(c^2<r<1\), there is exactly one critical horizon \(T_*>0\) determined by
\[
\frac{1-e^{-\alpha T_*/2}}{1-e^{-\beta T_*/2}}=\sqrt{r}.
\]
For \(0<T<T_*\), exactly the two endpoint schedules minimize \(J_T\); for \(T>T_*\), exactly the midpoint minimizes; at \(T=T_*\), exactly the three schedules \(0,T_*/2,T_*\) tie.

**Local/global separation for slope-balanced memories.** If \(b\beta=a\alpha\), then there is a distinct *earlier* local midpoint-stability threshold
\[
 T_{\mathrm{loc}}=\frac{2\log(\beta/\alpha)}{\beta-\alpha}<T_*.
\]
The midpoint is a strict local maximum for \(T\le T_{\mathrm{loc}}\) (quartically flat at equality). For every \(T>T_{\mathrm{loc}}\), both the midpoint and the two endpoint schedules are strict local minima, separated on either half by one strict local maximum. Thus the midpoint becomes locally favorable strictly *before* it becomes globally optimal. The endpoint schedules remain locally favorable for every finite \(T>0\), even after the global switch.

For the slope-balanced illustrative normalization \(a=\alpha=1\), \(\beta=2\), \(b=1/2\), the two different thresholds are
\[
 T_{\mathrm{loc}}=2\log2=1.3862943611\ldots,
 \qquad T_*=2\log(1+\sqrt2)=1.7627471740\ldots.
\]
For \(T>T_{\mathrm{loc}}\), the two intervening local maxima occur exactly at \(t=T/2\pm \operatorname{arcosh}(e^{T/2}/2)\).

## Assumptions and scope

The three pulses are idealized as identical instantaneous exposures with a *postulated additive pairwise* lag interaction. \(K\) is a phenomenological cost, not a proven coral physiological law, and \(J_T\) is not observed mortality or a population projection. Damage and priming amplitudes \(a,b\), decay constants \(\alpha,\beta\) and the horizon \(T\) are held constant during optimization. The attenuation kernel is permitted to be negative because the total objective is a relative risk surrogate; adding a sufficiently large time-independent baseline does not change minimizers. The two endpoint times are compulsory, and coincident pulses are allowed at the boundary \(t=0,T\). If exact temporal coincidence is inadmissible, those endpoint results become infima on the open domain \(0<t<T\), not attained optimal calendars.

More generally, imposing \(\delta\le t\le T-\delta\) for any fixed \(0\le\delta<T/2\) restricts the candidate set to \(\{\delta,T/2,T-\delta\}\). The choice is completely determined by the sign of
\[
 2a e^{-\alpha T/2}\bigl(\cosh(\alpha(T/2-\delta))-1\bigr)
 -2b e^{-\beta T/2}\bigl(\cosh(\beta(T/2-\delta))-1\bigr).
\]
Positive sign selects the midpoint, negative sign selects the two boundary schedules, and zero gives a three-way tie. No claim of a unique critical \(T\) at fixed nonzero \(\delta\) is made.

## Proof

Write \(u=|t-T/2|\in[0,T/2]\) and discard the constant \(K(T)\). The symmetric objective becomes
\[
 F_T(u)=2a e^{-\alpha T/2}\cosh(\alpha u)-2b e^{-\beta T/2}\cosh(\beta u).
\]
For \(u>0\), its derivative has the same sign as
\[
 \frac{a\alpha}{b\beta}e^{(\beta-\alpha)T/2}
 - \frac{\sinh(\beta u)}{\sinh(\alpha u)}.
\]
Indeed the omitted factor is \(2b\beta e^{-\beta T/2}\sinh(\alpha u)>0\). The quotient \(\sinh(\beta u)/\sinh(\alpha u)\) is strictly increasing for \(u>0\): its logarithmic derivative is \(\beta\coth(\beta u)-\alpha\coth(\alpha u)>0\), because \(x\mapsto x\coth x\) is strictly increasing on \((0,\infty)\), with derivative \((\sinh x\cosh x-x)/\sinh^2x>0\). Consequently \(F'_T\) can only change from positive to negative, never negative to positive. Therefore the minimum on \([0,T/2]\) is attained only at \(u=0\) (the midpoint) and/or \(u=T/2\) (either endpoint), with no hidden interior minimizers. If the two endpoints of this reduced interval tie, every internal point lies strictly above their common value: otherwise the derivative pattern would contradict a strict interior minimum or constant segment.

Direct subtraction gives
\[
 J_T(0)-J_T(T/2)=a(1-e^{-\alpha T/2})^2-b(1-e^{-\beta T/2})^2.
\]
The ratio \(R(T)=(1-e^{-\alpha T/2})/(1-e^{-\beta T/2})\) increases strictly from \(\alpha/\beta\) as \(T\downarrow0\) to \(1\) as \(T\to\infty\). To prove strict increase, differentiate \(\log R\):
\[
 \frac{d}{dT}\log R(T)=\frac12\left(\frac{\alpha}{e^{\alpha T/2}-1}-\frac{\beta}{e^{\beta T/2}-1}\right)>0,
\]
using the strict decrease of \(x/(e^x-1)\) for \(x>0\). Thus the sign of the difference is exactly the sign of \(R(T)^2-r\), yielding all three global cases and the unique critical horizon. Endpoint symmetry gives exactly the listed optimal times.

For the slope-balanced case \(b\beta=a\alpha\), the second derivative at the midpoint is
\[
 F_T''(0)=2a\alpha^2 e^{-\alpha T/2}-2b\beta^2e^{-\beta T/2},
\]
which crosses from negative to positive exactly at \(T_{\mathrm{loc}}=2\log(\beta/\alpha)/(\beta-\alpha)\). At equality the quartic Taylor coefficient is negative because
\[
 F_T^{(4)}(0)=2a\alpha^2e^{-\alpha T/2}(\alpha^2-\beta^2)<0.
\]
So the critical midpoint is still a strict local maximum. At a left endpoint, differentiation in the allowed inward direction gives
\[
 J_T'(0)=K'(0)-K'(T)=a\alpha(e^{-\alpha T}-e^{-\beta T})>0,
\]
so both endpoints are strict constrained local minima for every positive horizon. For \(T>T_{\mathrm{loc}}\), the midpoint and each endpoint are strict local minima; the strict monotonicity of the hyperbolic quotient above forces precisely one intervening maximum on each half. At \(T=T_{\mathrm{loc}}\) the midpoint is not a local minimum, so the global switch cannot yet have occurred; hence \(T_{\mathrm{loc}}<T_*\). Finally, at \((a,b,\alpha,\beta)=(1,1/2,1,2)\), the threshold ratio simplifies to \(R(T)=1/(1+e^{-T/2})\), while the stationary equation reduces to \(2\cosh u=e^{T/2}\), giving the stated elementary expressions.

The constrained \(\delta\) variant follows by applying the same no-interior-minimum argument on \(0\le u\le T/2-\delta\), then subtracting the two surviving candidate values.

## Verification

Run \(\texttt{python3 verify_memory_pulses.py}\) using only Python standard-library modules. The program checks exact algebra at a rational-decay benchmark, tests the two analytic transition formulae, verifies the derivative-sign geometry across a deterministic parameter grid and seeded random sample, and checks the globally minimal candidate against a dense numerical grid. A numeric grid is explicitly supplementary: the proof above, not finite testing, establishes the universal theorem. The critical monotonicity and absence of interior minima are established symbolically in the proof.

At \(a=\alpha=1\), \(\beta=2\), \(b=1/2\), the witness \(e^{-T/2}=\sqrt2-1\) gives exact equality between the center and endpoints. At \(T=1.6\), endpoint schedules still beat the locally stable midpoint; at \(T=2.4\), the midpoint is uniquely global but the endpoints remain local minima.

## Relationship to prior work

Brown et al. (2023) document physiological legacies, acclimatization and species-specific trade-offs after consecutive marine heatwaves; they do not posit this pairwise lag surrogate or derive its optimization phase diagram. Martell (2023) reports a dose-dependent upfront priming cost and candidate hormesis in Acropora, motivating the coexistence of protective and detrimental effects without proving their exponential decay laws. A 2024 numerical study of molecular network motifs (Network motifs exhibiting a differential response to spaced and massed inputs) varies *uniform* inter-stimulus intervals in ODE motif simulations and explicitly distinguishes unequal spacing as a separate issue; its published qualitative spacing-effect observations do not imply the present universal pinned-three-event classification. Classical Morse-type interaction potentials contain two exponentials as a mathematical ingredient, but identifying an ingredient is not the same as establishing this exact global and metastable schedule classification; a comprehensive literature-priority claim is not made.

A current semantic search of published mathematical records for biphasic exponential memory, three-event timing, endpoint versus midpoint transitions, and exact kernel equivalents found nearby but non-dominating results on ecological survey placement, pinned two-exponential *parameter-estimation* designs and pulse timing in other physical systems. Their objectives, kernels, and quantifiers differ: none of the checked claims implies the present exact minimizer set and local/global separation. The possibility of equivalent results under another discipline's terminology remains a residual priority risk.

## Limitations

No mechanism of heat acclimation, evolution, stochastic mortality, species turnover, or field sampling was inferred from this simplified mathematical model. The model assumes linear additive pairwise lag effects and two pure exponential memories with opposite signs; other memory kernels, uneven pulse magnitudes, changing baseline vulnerability, mortality selection, and non-pairwise interactions can change the optimum. Endpoints represent coincident ideal pulses unless a positive separation constraint is imposed. The classification is exact only for the specified mathematical objective. Independent biological or mathematical validation has not been performed.

## References

1. Brown, K. T. et al. (2023). *Marine heatwaves modulate the genotypic and physiological responses of reef-building corals to subsequent heat stress.* Ecology and Evolution 13, e10798. First publicly published 2023-12-13. https://doi.org/10.1002/ece3.10798 . Full text: https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.10798
2. Martell, H. A. (2023). *Thermal priming and bleaching hormesis in the staghorn coral, Acropora cervicornis.* Journal of Experimental Marine Biology and Ecology 560, 151820. https://doi.org/10.1016/j.jembe.2022.151820
3. *Network motifs exhibiting a differential response to spaced and massed inputs.* Learning & Memory 31 (2024), article a054012. https://pmc.ncbi.nlm.nih.gov/articles/PMC11369633/
4. Classical Morse two-exponential pair potential: P. M. Morse (1929), *Diatomic molecules according to the wave mechanics. II. Vibrational levels*. Physical Review 34, 57–64. https://doi.org/10.1103/PhysRev.34.57
