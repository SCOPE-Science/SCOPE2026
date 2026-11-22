# Review: Reentrant equal spacing in a two-opportunity seed-bank rescue model

## Correctness — PASS

The stated exact objective has domain \(0<\kappa\le4\), positive horizon and rate, and an allocated interval including endpoints interpreted as omitted opportunities. The bijection to variables \(xy=q\) makes their sum range over exactly \([2\sqrt q,1+q]\). Expanding both failure factors gives a strict positive quadratic in this sum. Projecting its vertex proves all global optimizers and all exact phase boundaries, including \(\kappa=3,4\); no unobserved critical point can win. The independently written standard-library verifier passed 204786 finite arithmetic assertions. The proof, not the tests, establishes the continuous parameter domain.

## Originality — PASS with residual priority risk

The closest ecological and analytical references are McCarthy, Possingham and Gill (2001; stochastic dynamic programming for stand-age- and density-dependent policies), Tucker and Cadotte (2013; fire-return variance and seeder-resprouter coexistence), Tonnabel and colleagues (2012; age-dependent resource allocation under exogenous fire regimes), Agne et al. (2022; stand regeneration data), and Plumanns Pouton et al. (2024; seedbank occurrence versus fire history). Their inspected objects and objectives do not state or directly imply the closed-form independent-rescue four-regime classification. An exact general polynomial/scheduling result could still dominate it, and the 2013 paper was only partially available through its substantial indexed content, not a retrieved complete manuscript.

## Value — PASS

The emergence, disappearance and re-emergence of equal spacing as a global optimum, controlled by the peak-success parameter, is a structurally motivated counterexample to a standard assumption that uniformly spaced restoration opportunities are always best. Thresholds are explicit, all optimizer geometries are classified, and omission of one opportunity is allowed at small horizons. The finding is an analytically reproducible benchmark for designing and testing richer ecological timing models. It is not a measured conservation policy.

## Limitations

The two success events are independent, environmental cohorts do not interact, maturation and viability rates are equal, and fire intervals are not stochastic. Published studies motivate the gap but do not empirically validate the model. Historical priority remains open to broader comparison.

Self-review: passed. Independent audit: not yet performed.
