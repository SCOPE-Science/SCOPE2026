# Scientific review

## Correctness — PASS

For interior \((\psi,\alpha,\lambda)\), the four history probabilities are exactly determined by three values of the two-exponential no-alarm survival function. Four distinct shared interpolation zeros, including time zero, force equality of the mixtures by the standard exponential Chebyshev zero bound; the parameter ordering removes label exchange. Strict concavity of the logarithmic mean shows the Fisher Jacobian is nonsingular for any distinct positive visit durations and singular when durations coincide. A Vandermonde factorization of its analytic alternant, combined with probability integral factors, establishes a uniform \(T^8\) expansion and the exact limiting maximizers. The symbolic and direct Fisher score checks pass 2,269 assertions. All boundaries \(\psi=0,1\), \(\alpha=0\), or \(\lambda=0\) lie outside the asserted interior; no finite-budget unique-optimum claim is made.

## Originality — PASS relative to compared evidence

The model is a duration-dependent specialization of Royle and Link (2006), not a newly invented false-positive mixture. Miller et al. (2011) use certainty levels or second detection methods to address false positives. Clement (2016) varies survey counts/methods and optimizes occupancy-estimate precision, not the Fisher determinant for a two-duration, three-unknown Poisson experiment. The closest identified published two-visit result without false positives estimates only two unknowns and has a different small-budget optimum, equal durations rather than rank loss. Classical Chebyshev exponential-mixture identifiability itself is prior mathematical technology. No inspected accessible text supplied this full three-parameter, two-visit global criterion together with the universal asymptotic D-optimal 21–79 split. The foundational 2006 full text and some general older optimal-design work were not fully inspected, leaving a material but not decisive historical-priority risk.

## Value — PASS

A two-visit detector that cannot confirm alarms is a natural economical monitoring design. With false-positive background and genuine detection intensity both unknown, identical-duration visits are structurally incapable of estimating all three parameters, regardless of replication. Deliberately varying durations restores identification without requiring a third visit or auxiliary confirmation. The universal short-budget fractions give a concrete, interpretable design benchmark requiring a nontrivial joint Fisher calculation, not a generic recommendation to add sample effort. This is strictly a model-level benchmark and not a field-calibrated protocol.

## Source and scope limitations

Relevant comparisons: Royle and Link (2006), https://doi.org/10.1890/0012-9658(2006)87[835:GSOMAF]2.0.CO;2; Miller et al. (2011), https://doi.org/10.1890/10-1396.1; Clement (2016), https://doi.org/10.1111/2041-210X.12617; published related two-visit occupancy result at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-two-visit-occupancy-experiment-breaks-equal-effort-optimality--b8f26f454426. Source access and historical-priority limitations are listed in the structured assessment. Interpretation of the mathematical mixture as physical occupancy requires prior ecological assumptions.

Self-review: passed. Independent audit: not yet performed.
