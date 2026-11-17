# Scientific review

## Correctness — PASS
The graph is a labelled path with the walker starting at an endpoint; the time convention is rotate-before-move. A periodic-state criterion is proved in both directions by an Euler-tour construction and the last-departure property on a tree. The excursion decomposition then gives the exact first-entry clock, not only a candidate periodic hitting time. Partitioning by the farthest initially outward rotor gives the generating polynomial. Rearrangement yields the sharp conditional extrema, and independent Bernoulli analysis yields the exact mean and central limit. Separate whole-functional-graph and direct-step verifications agree on all tested inputs. Bounds for finite checks are explicitly recorded.

## Originality — PASS (qualified)
The inspected historical foundation gives rotor-router Euler-tour eventuality and broad lock-in bounds. The 2015 path exploration result proves an exact worst-case **first-visit** time \((n-1)^2\), not the first complete-state recurrence time \((n-2)^2\). The 2014 Section 5.1 algorithm compresses exploration phases for a given input; it does not enumerate the endpoint initializations or establish this first-entry distribution. The previously recorded one-walker cycle result applies to a topologically distinct graph and is not an implication for paths. Searches for aliases, phase decomposition, first Euler cycle, and endpoint rotor initialization did not identify a statement dominating the full polynomial and Gaussian law. The 2003 original was accessible only in abstract form; an older conference text is bibliographically known, so historical priority is qualified.

## Value — PASS
The first-entry distribution quantifies how an arbitrary rotor initialization controls deterministic time-to-recurring operation; this is not determined by a worst-case coverage bound. The exact generating polynomial simultaneously provides each finite-time population, unique fixed-outward-count extrema, expected delay, and a nontrivial \(m^{3/2}\) fluctuation scale as the path grows. Endpoint initialization is a canonical graph exploration scenario, and the density of all initial rotor configurations is included, rather than an arbitrary finite exception.

## Remaining scientific limitations
The result does not address interior walker starts, multiple tokens, or general graph families. Its priority comparison has the documented inaccessible original-source risk; the mathematical proof is self-contained and the computational checks are finite.

Self-review: passed. Independent audit: not yet performed.
