# Scientific review

## Correctness — PASS
The one-cycle renewal/Dynkin identity is proved from the killed Brownian Poisson problem. The Lipschitz bound proves the obstruction uniformly in all positive reset rates and interior positions. The killed Green kernel gives explicit hyperbolic formulas for cumulative exploration and return distance; the small-position limit and large-rate limit establish the constructive converse at all \(aL/D>2\). The weak derivative is an exact Green-kernel polynomial, and the representative improvement is checked by strict rational interval bounds. The analytic argument, not numerical checking, proves the continuum statement. Return mean \(|y-x|/a\) follows from the drifted Brownian hitting-time ODE and is insensitive to return diffusion.

## Originality — PASS, qualified
Searches covered exact wording and equivalent formulations involving linear distance reset costs, finite return times, two-target Brownian first passage, global reset-speed thresholds, Lipschitz and potential-obstacle arguments, and finite-rate gain despite positive small-rate derivative. The strongest primary comparator is Chen–Tang–Li (18 November 2026), whose mean formula subsumes the expression for the mean and whose weak-rate phase boundary is \(aL/D=4\). It does not state the all-rate criterion \(aL/D>2\) or the derived explicit opposite-sign example; the distinction is one of quantifiers and global optimization, not merely parameter values. Sunil et al. (2025) concern discrete half-line linear costs, not a Brownian two-absorber global threshold; Dubey–Pal (2026) concern harmonic return and target-active absorption. The related Brownian star-graph result establishes the qualitative possibility of weak/finite-rate reversal for a different graph and instantaneous restarting, not the sharp return-drift threshold here. Accessible own historical claims were checked for overlapping statements, without re-evaluating historical records.

Priority risk: the exact finite-time mean formula in the 18 November paper plus classical killed-diffusion comparison tools may make this a previously implicit corollary. No independently certified exhaustive novelty conclusion is asserted.

## Value — PASS
The critical return speed \(2D/L\) resolves a physically meaningful all-rate feasibility question for finite-return search, gives a universal impossibility bound from the bare exit-time potential, and exposes a real global-versus-infinitesimal-rate distinction. The sharp counterexample within \(2<aL/D<4\) warns against using a weak-reset criterion as a global search-design rule. These are structural statements about a natural dimensionless control parameter, not an arbitrary finite parameter slice or a numerical gain alone.

## Scientific limitations
Both targets must be inactive during return, and the expected return duration must equal distance divided by \(a\). The threshold is existential across positions and rates. Comparison with the 18 November 2026 model is source-priority evidence only. Other possible implicit literature coverage remains a risk; independent review is pending.

Self-review: passed. Independent audit: not yet performed.
