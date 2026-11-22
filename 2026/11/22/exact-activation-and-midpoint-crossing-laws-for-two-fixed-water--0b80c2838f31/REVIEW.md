# Self-review

## Correctness — PASS
The state solution is explicit on each segment. Integrating its rational saturation gives identity (1), and exact differentiation gives a quadratic with precisely one positive zero. This establishes the unique global schedule and all boundary cases. Evaluating at the geometric midpoint establishes the second threshold; differentiation and asymptotics establish sensitivity. A standalone symbolic/numerical checker passed 36,369 supplementary assertions. The proof does not infer a universal statement from the grid.

## Originality — PASS, subject to historical-priority risk
The complete fixed, ordered two-pulse scheduling classification was compared at statement level to the accessible full manuscript of Shani–Tsur–Zemel (continuous-rate biomass-and-moisture turnpike), the full article of Viola et al. (stochastic moisture transient) and the full article of Vico–Porporato (rainfall and intervention-triggered irrigation statistics). None of the inspected results states or directly implies the particular two-input saturating objective's exact activation and midpoint thresholds. Semantic comparisons against relevant published mathematical records did not identify equivalent coverage. General optimal impulse-control literature could contain a dominating theorem; the search does not prove universal novelty.

## Value — PASS
Two fixed applications are a natural low-frequency scheduling restriction, and the precise switch between coincidence, early interior timing, and late interior timing answers a resource-allocation question absent from the motivating models. The midpoint transition requires a nontrivial amount condition, so the classification rules out late optimal pulses for a broad parameter region. A dimensionless benchmark yields a 12.79% objective gain against simultaneous application; this demonstrates model-level, not field-level, materiality.

## Closest literature and limitations
Shani–Tsur–Zemel (2004), Viola et al. (2008) and Vico–Porporato (2013) supply relevant but different formulations. Hall and Butcher (1968) is an especially relevant historical title whose full text was unavailable, so no full-document negative coverage determination is made. Wider impulse control, general concave reward scheduling and unindexed older studies remain residual priority risks. The single unbounded store, linear drying, no feedback, constant response and fixed prescribed amounts exclude operational irrigation recommendations.

Self-review: passed. Independent audit: not yet performed.
