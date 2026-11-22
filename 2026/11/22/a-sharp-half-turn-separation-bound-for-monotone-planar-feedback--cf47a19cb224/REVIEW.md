# Scientific review: a sharp half-turn separation bound for monotone planar feedback trajectories

## Correctness: PASS

The statement is an all-parameter, all-state qualitative oscillation bound in the exact common-degradation, opposite-monotonicity, finite-slope regime. Secant slopes between two solutions are bounded in the correct orientation, and the rescaled difference solves a time-dependent, two-dimensional signed rotation with angular speed between zero and \(\sqrt{AB}\). A first-coordinate return requires a half-turn, proving the gap. An explicit logistic model with a transverse simple zero in its linearization proves optimality by smooth dependence. A separate saturating, strictly monotone \(C^1\) model has an exactly affine invariant neighborhood and identical first-coordinate samples at every integer multiple of \(\pi\) for a continuum of initial states. The checker reproduced the plateau identities and the logistic near-critical values; computations are corroboration, not the universal proof. The comparison does not cover unequal degradation or unbounded regulation slopes.

## Originality: PASS within available evidence

Belgacem's arXiv:2611.17232v1 (2026-11-12) was inspected through its main model, observability sections, conclusion and cascade appendix. It reconstructs the hidden state from a continuously observed coordinate and its derivative, but does not state a quantitative separation law for zero crossings of differences of two trajectories. Earlier sampled-observability articles of Ammar--Vivalda (2004), Ammar--Massaoud--Vivalda (2016), and Ammar--Vivalda--Zitouni (2020) are genuine potentially related background; their accessible abstracts address preservation or genericity under sampling. The 2004/2016 full texts could not be inspected; they may contain a related general theorem. Generic observability or the standard half-period alias of a fixed linear oscillator does not, by itself, state the all-trajectory sharp \(\pi/\sqrt{AB}\) first-zero bound with a bounded nonlinear-feedback permanent-alias example. Broad prior-result searches did not identify a matching statement; search absence alone is not proof of novelty.

## Mathematical value: PASS

This is a sharp disconjugacy/zero-spacing theorem for an entire, physically motivated class of monotone planar ODEs, with arbitrary nonlinear feedback functions rather than one special linear oscillator. It converts a pair of abstract slope bounds into a guaranteed time window in which the measured coordinate cannot return to equality for two distinct initial states. The endpoint construction shows the exact qualitative loss of information at the boundary, even under bounded strict monotonicity and convergence of trajectories to one equilibrium. The contrast is useful for deciding whether discrete sampling can distinguish trajectories without differentiation. It does not claim a new observer algorithm or biological parameter fit.

## Closest literature and limitations

- Belgacem, *Luenberger observers for two-gene regulatory networks with sigmoidal regulation*, arXiv:2611.17232v1. Full HTML sections examined.
- Ammar--Vivalda, *On the preservation of observability under sampling* (2004), doi:10.1016/j.sysconle.2003.08.008. Abstract available; full-text priority risk.
- Ammar--Massaoud--Vivalda, *Observability Under Sampling for Nonlinear Systems* (2016), doi:10.1002/asjc.1284. Abstract available; full-text priority risk.
- Ammar--Vivalda--Zitouni, *Strong Differential Observability for Sampled-Time Systems* (2020), doi:10.1137/19M1302867. Abstract/reference comparison only.

The theorem assumes a common degradation rate and bounded slopes; its endpoint permanent-alias construction is a \(C^1\) regulation in the full model class, not an assertion about the standard logistic's exact sampled data at the critical time. Independent external review is not available.

Self-review: passed. Independent audit: not yet performed.
