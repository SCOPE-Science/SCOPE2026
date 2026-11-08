# Scientific assessment

## Correctness — PASS

The exact geometric-age attachment probabilities yield uniform upper and lower one-vertex tail bounds with matching quadratic exponential rate \(\beta/(2m)\). The upper bound is a Chernoff estimate for the Bernoulli product; the lower bound comes from full-hit blocks of consecutive birth times. Disjoint birth-time windows give independent witnesses among linearly many vertices up to a logarithmic factor. Upper union bounds and lower block bounds are summable along dyadic sizes, and monotonicity extends the almost-sure limit. All quantifiers fix \(m\ge1\) and \(\beta>0\). The exact-rational verifier passes 61,632 finite assertions, but these finite checks do not prove the infinite limit.

## Originality — PASS (subject to historical-priority review)

Aguech–Mahmoud–Mohamed–Yang (2025) introduces the exact one-parent exponentially weighted tree, determines degree laws for individual nodes, and explicitly proposes maximal degree as future research (§4). Tang–Wang–Wu (2026) establish recurrence/collisions for the matching multi-parent graph but no maximum-degree law; their earlier bounded-window tree has uniformly bounded degree. The weighted recursive graph maximal-degree results of Lodewijks and Ortgiese, and the follow-up by Eslava, Lodewijks and Ortgiese, assume identically distributed random weights and do not subsume the deterministic sequence \(e^{\beta k}\). Direct database, model-formulation and parameter searches identified no theorem providing the \(\sqrt{\log n}\) extreme-degree constant. Older deterministic-weight results may still provide an equivalent or dominating statement; novelty is therefore provisional, not a claim of global uniqueness.

## Mathematical value — PASS

The exact leading constant classifies a natural graph statistic across all fixed positive geometric decay rates and every fixed arrival multiplicity. It answers a published natural extreme-degree question for the exponential tree with an exact coefficient and extends it to all fixed multi-edge counts. Unlike a fixed-vertex degree law, a simultaneous graph maximum demands control of rare events across many competing vertices; the \(\sqrt{\log n}\) scale emerges from matching quadratic tails. The matching uniform tail bounds explain the mechanism behind extremes and are useful for further questions about hubs and graph geometry. The result is more than a generic moment identity or a finite simulation.

## Closest literature and remaining limitations

See the references in `RESULT.md`. The result does not cover suppressed parallel edges, variable parameters, second-order extremes or random-walk conclusions. The principal remaining scientific risk is an earlier deterministic-weight recursive-tree theorem sufficiently general to imply this exact constant.

Self-review: passed. Independent audit: not yet performed.
