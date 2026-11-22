# Review of locating-domination reliability dominance

## Correctness — PASS
For each of the two explicitly defined twenty-vertex graphs, ordinary locating domination is equivalent to requiring distinct nonzero selected-neighborhood signatures for every unselected vertex. Both `checks/verify_cpp.cpp` and `checks/verify_python.py` exhaust all \(2^{20}\) subsets without sampling. The C++ implementation uses a five-symbol disjointness realization of the Desargues graph, while Python uses \(\(GP(10,3)\)\) and checks an explicit isomorphism. The complete coefficient lists agree, so subtraction proves the exact seven-degree difference and its strictly positive Bernoulli reliability expansion for \(0<p<1\). The endpoint and fixed-budget statements follow directly. Verification covers exactly these two graphs, not a family.

## Originality — PASS, subject to residual priority uncertainty
The 2014 and 2015 primary literature provides definitions, girth-based characterizations, and bounds on minimum locating-domination size, not the full two-graph enumerations or a global comparison of their reliability polynomials. Two directly relevant public mathematical findings prove the previously known minimum sizes and optimum counts, but their inspected full result statements do not determine the counts at larger cardinalities. The new statement is therefore not a relabelling of those optimum counts. Searches included full-spectrum, reliability, test-cover, graph-name, coefficient and dominating-parameter terminology. Unindexed older computations remain a possible priority risk; a negative index search cannot certify uniqueness.

## Value — PASS
An exact full success polynomial is the natural invariant for random local-detector placement. The proven coefficientwise domination supplies a strict answer at every intermediate random deployment probability and an exact fixed-budget comparison, not merely the already known difference between minimum detector counts. The phenomenon involves two canonical cubic graphs of the same order, and the exact equality beyond thirteen detectors is an additional non-obvious boundary. The result is a finite benchmark, with no unsupported generalization to other networks.

## Sources and limits
The original locating-domination literature is Balbuena–Foucaud–Hansberg, arXiv:1407.7263 (2014), and Foucaud–Henning, arXiv:1412.2865 (2014). Closest exact minimum-only records are *All 1,475 minimum locating-dominating sets of the Desargues graph* (2026) and *Location-dominating code reconfiguration on the dodecahedral graph* (2026), both in the public published-finding corpus mathematical-results repository. Reproducibility requires executing the two included programs, while independent scholarly priority and proof review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
