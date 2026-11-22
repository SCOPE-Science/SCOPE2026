# Self-review

## Correctness — PASS

The claim fixes the stopping time, the reset clock, Brownian diffusivity and the scope \(a,D,\tau_0,\beta>0\). The exact reflection-principle survival and first-hit density supply \(h(t)\) and the defective reset kernel \(k\) with mass \(q<1\). The incomplete-gamma formula for \(p=1-q\) follows from direct substitution and is checked by independent integration. The survival formula is the exact regenerative expansion. The nonstandard tail interchange is proved using an integrable power envelope for the entire defective renewal density, exploiting \(k(t)=O(t^{-\alpha-1})\) and support bounded below by \(\tau_0>0\). The same envelope proves fixed-reset-count localization, yielding a geometric conditional law, an asymptotically negligible last-reset epoch, and a Rayleigh spatial law by the absorbing heat kernel. Strict moment cutoffs follow from survival asymptotics, including the logarithmic boundary case. Finite numerical checks support normalization but are not used as an infinite proof.

## Originality — PASS, subject to independent priority review

The closely related 2024 paper of Liu et al. numerically examines the Pareto-clock free Brownian first-passage distribution and reports an exponential-looking regime at high Pareto index, but its inspected model and Section 3 do not prove an all-index exact large-time survival equivalent or a conditional geometric–Rayleigh survivor law. The 2016 Nagar–Gupta paper treats power-law resetting and first-passage mean formulas without the inspected final-time marked survivor limit. Godrèche–Luck, Section 7, already gives a general renewal transform, **unconditional** geometric numbers of unsuccessful attempts, and the general mean criterion; these are acknowledged rather than counted toward originality. Linn–Lawley's frequent-reset asymptotics concern a different order of limits, and the time-since-reset conditionings of Masó-Puigdellosas et al. concern position observations without an absorbing target. The asserted contribution is restricted to the evaluated all-index algebraic tail plus conditional independence and endpoint law. Its relationship to generic subexponential renewal theory could make the refinement an implicit consequence of older results; this is the principal residual risk. No claim of independent or exhaustive priority validation is made.

## Mathematical value — PASS

The fixed-clock long-time tail directly answers whether even *finite-mean* Pareto resetting truly regularizes an unbounded Brownian target search to an exponential completion law. It quantifies the algebraic tail constant, distinguishes the time asymptotics from long preasymptotic exponential-looking simulation windows, and describes which trajectories dominate extreme delays. The geometric–Rayleigh decoupling is a structural survivor-selection statement, and the proof applies across a full continuum of resetting exponents. Moment thresholds alone and the general renewal equation are not credited as new.

## Closest sources and residual limits

- Liu et al. (2024), DOI 10.1002/cphc.202400313, Sections 2–3 and Figure 2(a): same Pareto clock and a free-Brownian first-passage benchmark, primarily finite-time numerical observations.
- Nagar and Gupta (arXiv:1512.02092), first-passage Section and Appendix: exact older general setting, renewal and first moment, not a derived marked survivor law.
- Godrèche and Luck (arXiv:2309.06997), §7: restart transform, unconditional geometric count and mean criterion, already prior; important theoretical foundation.
- Masó-Puigdellosas, Campos and Méndez (arXiv:2205.01613), §IV: clock age conditioned on a measured *position*, not on no target hit.
- Linn and Lawley (arXiv:2302.05409), §2: fast-resetting limit rather than long-time behavior of a fixed Pareto clock.

The theory excludes non-Brownian underlying motion, finite resetting latency, random reset positions and any assertion of a uniform large-index crossover scale. Independent publication-priority assessment and independent proof review remain unperformed.

Self-review: passed. Independent audit: not yet performed.
