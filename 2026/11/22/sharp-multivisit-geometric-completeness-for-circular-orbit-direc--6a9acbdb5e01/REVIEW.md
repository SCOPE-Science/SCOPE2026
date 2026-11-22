# Review of the multivisit geometric-completeness theorem

## Correctness — PASS

A uniform three-dimensional sightline has independent uniform absolute vertical coordinate and projective azimuth. At each fixed vertical coordinate, the visible phases form congruent arcs on a circle of circumference \(\pi\); the uncovered length is exactly the sum of positive parts of the consecutive phase gaps after subtracting the two arc radii. Convexity and Jensen prove optimality for all schedules. The full range of arc radii proves rigidity and characterizes every zero-miss schedule. Uniform Taylor expansion about the unique first-contact latitude establishes the \(3/2\)-law and the stated positive coefficient. The standard-library checker passes finite numerical diagnostics, but the universal claim is based on these explicit analytical steps. All assertions are scoped to circular orbits, \(m\ge3\), and \(0<t<1\).

## Originality — PASS on inspected evidence

The closest public result, *Exact two-visit direct-imaging completeness and its sharp quarter-orbit transition*, proves the two-observation case but does not state the all-\(m\ge3\) integrated phase-gap formula, all-optimizer census, sharp guarantee threshold or coefficient for each number of visits. Brown and Soummer (2010) treat realistic sequential completeness; Kane and colleagues (2018) treat largest-separation epochs for known orbits; Dallant and colleagues (2023) optimize multiepoch likelihoods and orbit estimates; Plavchan and colleagues (2024) explicitly exclude revisits from their analytic yield calculations. Standard convex spacing and circle-covering arguments are known mathematics, not claimed as novel. No inspected source contains this joint all-visit theorem. Residual risk: older uninspected optimal arc-covering and survey-scheduling literature could imply one or more components; the complete public text of the closest indexed two-visit result was unavailable during review. The inspected scientific implication comparisons, not title differences or a failed keyword search, underpin this assessment.

## Value — PASS

Unknown orbit orientation makes multivisit geometric detection a natural, practically motivated sampling problem. A sharp all-visit completeness guarantee, the complete set of schedules achieving it, uniqueness above the threshold, and a quantitative \(3/2\)-power loss law form a usable benchmark for testing more realistic direct-imaging schedulers. The three-visit cutoff \(\sqrt3/2\) and a closed visit-count requirement provide more specific information than unquantified equal-spacing advice. No telescope recommendation or empirical predictive performance is asserted.

## Scientific limitations and closest literature

The model ignores brightness and phase-dependent flux, noise and false positives, eccentricity, uncertain periods, mission windows and timing costs. The previously known two-visit geometric result is credited rather than relabeled. The closest empirical/instrumental sources and residual historical-priority risk are detailed in RESULT.md and AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
