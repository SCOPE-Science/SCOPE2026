# Scientific review: Exact run-erosion clocks for thresholded cyclic dynamics on complete graphs

## Correctness — PASS

The predecessor-dependent clock follows from the exact nonreactivating occupancy recurrence and run erosion, not experimental extrapolation. Every active run loses its leftmost color at successive updates until one active color survives, and the original deficient predecessor occupancy propagates as a final packet only when positive. The all-active case forces every vertex to advance with primitive period \(q\). The EGF formula separates zero, positive subthreshold, and active color categories. The limit uses a single deficient color of mass \(\theta-1\) as the dominant rare event. The two independent reproducibility programs passed; they corroborate but do not prove the parameter-uniform theorem.

## Originality — PASS, qualified

Fisch–Gravner–Griffeath (1991) defines arbitrary-color thresholded cyclic contact dynamics in its planar-media setting. The accessible published three-color clique classification has an arbitrary threshold but no higher-color claim. Earlier all-color threshold-one and four-color threshold-two classifications concern special slices; neither supplies the simultaneous arbitrary-color/arbitrary-threshold run-erosion law or the uniform sharp \(q-1\) clock. An early Fisch (1990) article remained inaccessible in full, so historical priority is not certified. Search and scientific implication comparisons are documented in `AUDIT.json`.

## Mathematical value — PASS

This is an exact whole-family dynamical classification: all eventual periods, statewise first-entry times, sharp worst-case delay, a complete finite-size labelled census, and asymptotic concentration conditional on loss of collective rotation. The extra update caused by a positive but subthreshold predecessor provides a structural distinction between threshold one and larger thresholds rather than a simple change of numerical constants.

## Limits

The theorem assumes a loopless complete graph, synchronous vertex updates and fixed integer color/threshold parameters in the asymptotic statement. It does not extend to local lattice adjacency or asynchronous update orders. The cited 1990 original source was not available for full inspection. No independent validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
