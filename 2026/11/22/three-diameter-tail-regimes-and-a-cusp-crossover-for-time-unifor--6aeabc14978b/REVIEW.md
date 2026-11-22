# Scientific review: rolling-phase trochoid diameter laws

## Correctness

PASS. The calculation maximizes exact squared distance first over the phase midpoint, then over the phase gap. Strictness identifies all maximizing parameter pairs for every tracer radius. The local expansions distinguish a linear endpoint deficit, a cubic critical deficit, and a nondegenerate quadratic interior maximum; the calculated areas give the constants and exponents. The critical-window scaling retains both the parameter perturbation and cubic deficit and proves a bounded limiting sublevel set, including a total-variation conditional mark. The `verify.py` script independently evaluates curve distances and numerical area approximations, passing 4,023 deterministic checks; it cannot prove infinite-domain assertions.

## Originality

PASS on currently accessible comparisons, with historical priority provisional. The classical literature derives the rolling parametrization, curve types, area, arclength and inflection or double-point geometry. Those formulas neither state nor directly imply the two-independent-phase rare-diameter probability or the cubic crossover without the additional global extremal-pair analysis. General polygon random-distance studies use different domains and sampling measures. Published near-diametral chord results on ellipses, Reuleaux bodies, polygons and annuli also use different support objects, different cusp geometries, or arclength/area/invariant-line sampling; their stated results do not cover the rolling-phase trochoid transition. A historical source chapter is metadata-accessible but not fully readable; complete priority requires further human source checking.

## Value

PASS. The classical curtate/cycloid/prolate distinction is normally formulated in terms of loop and cusp geometry. Here it produces a quantitative, experimentally sampleable change of the most extreme two-point separation. The time-uniform measurement is natural for a rigid wheel at constant angular speed and cannot be replaced by arclength uniformity. The cubic critical law has exponent \(2/3\), distinct from both neighboring regimes, and the explicit transition-window marked law connects them rather than merely reporting a single isolated constant. This is a natural exact distributional invariant of the rolling system.

## Limitations and closest literature

The earlier literature does not establish priority by an unsuccessful search. The main technical risk is undetected coverage in old specialty literature on trochoids and their extreme distances. Lockwood's Chapter 9 is not full-text accessible from its publisher listing; Bronshtein et al.'s section 2.13.2 and Weisstein's Prolate Cycloid page were readable and treat standard geometry without these stochastic extrema. The theorem is exact only for one full period with two independent uniform rolling phases; arclength-uniform data or multiple-period windows need separate theorems. Analytic proof, not a finite grid, supports the claims.

Self-review: passed. Independent audit: not yet performed.
