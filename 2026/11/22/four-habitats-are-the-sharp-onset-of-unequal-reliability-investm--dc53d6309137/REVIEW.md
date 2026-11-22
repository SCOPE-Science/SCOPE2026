# Scientific review

## Correctness — PASS

The proof enumerates the exact six unordered-pair connection probabilities. Fixed-budget outer-edge symmetrization is strict by AM--GM, leaving a one-variable objective; a strictly increasing rational function gives one interior maximum for every positive budget. The proof checks endpoint signs, establishes uniqueness and interior positivity, derives the sharp central-edge inequality and proves both asymptotic regimes. Direct enumeration and independent random-allocation checks in `checker.py` passed 40,071 supplementary assertions. The experiments are supplementary and not substituted for proof.

## Originality — PASS on investigated evidence

The most directly relevant ecological connectivity work is Hamonic et al., arXiv:2109.06622 (2021-09-14), and journal DOI 10.1002/net.22131. Its full formulation and results cover a discrete subset-selection problem for upgrades, including the same family of pairwise connectivity indices, rather than continuously divisible exponential edge improvements on a four-patch path. Kettelle (DOI 10.1287/opre.10.2.249, continuous stage section read in full) proves a different objective for overall serial-system reliability; it does not entail the unique all-pairs connectivity allocation. The nearest published mathematical searches included four-habitat corridor allocation and path-connectivity budget variants; the identified results use colonization matrices, extinction times, effective resistances or discrete intervention choices rather than this objective. The 2006 reliability allocation paper (DOI 10.1137/S0036144503434493) could only be assessed from its abstract, leaving a residual historical-priority risk. Search failures were not taken as uniqueness proof.

## Value — PASS

The contribution is a complete natural four-habitat reliability allocation, with an exact global optimizer, a strict central bottleneck premium at every budget, and an exact minimal architecture: the analogous equal-cost three-patch path always divides investment evenly. The premium increases but remains bounded, and the limiting budget shares are explicit. These are concrete calibration and sanity benchmarks for continuous habitat-corridor investment models; no empirical optimality is claimed.

## Scope and limits

Only independent exponentially improvable links, unit-value persistent patches, continuous equal-cost investment, and expected connected-pair score are covered. The score is not species persistence or whole-network reliability. No broader arbitrary-network result or field recommendation follows. Priority and ecological calibration require further external review.

Self-review: passed. Independent audit: not yet performed.
