# Review of arithmetic capture and firing-rate staircases

## Correctness — PASS

For phase x in [0,eta], exact forward projection of x+beta produces rotation modulo one if allowed and reset to zero otherwise. Irrational minimality forces every orbit to hit the open hole, while rational q-grids meet holes of width >1/q; hence a single finite zero orbit captures all phases in these regimes. Summing r physical inter-spike intervals gives precisely mr+ceil(r beta), and one positive delay. A rational q-grid avoids the hole exactly at eta>=1-1/q; disjoint translates give |E|=q eta-q+1 and unique q-point orbit precisely at equality. Upper records of {j beta} generate monotone rational plateaux; the Diophantine bound follows from 1-{r beta} >= ||r beta||. The exact-fraction checker tests 2356 rational cases, and finite high-precision irrational sampling tests 210492 subcases; these tests are corroboration, not proof of the infinite assertions.

The proof explicitly excludes integral intrinsic phase, defines the observation scale and both rational thresholds, and distinguishes finite eventual phase capture from coincidence of absolute spike times. No numerical enumeration is used as a proof of the irrational case. The checker runs independently from `verification/check.py` using built-in Python exact rational arithmetic and high-precision floating approximations.

## Originality — PASS within checked literature

The motivating 2026 projection theorem states the universal recursion and lattice quantization, not the exact rational/irrational interval-window orbit/rate classification. Earlier hole-survival and flat-spot works explain first-hit combinatorics, but inspected assertions neither directly cover a piecewise rigid discontinuous reset clock nor its physically elapsed rate staircase. Stronger historical coverage remains a risk, explicitly acknowledged; comparisons rest on inspected material rather than negative-search proof.

Closest antecedents: Kaymakçalan–Selçuk (2026, arXiv:2611.17219v1), which supplies the exact projection recurrence; Anagnostopoulou–Díaz-Ordaz–Jenkinson–Richard (2010), which supplies a different expanding continuous flat-spot entrance-time framework; and Bunimovich–Dettmann (2004/2024), whose open-rotation-hole survival mechanism overlaps the elementary rational exceptional set. These antecedents are credited. Prior published claims in the accessible relevant ledger and published-finding corpus were checked for implication rather than title similarity; no exact integrated clock/rate statement was recovered. An inaccessible historical reset-circle theorem remains a priority risk, not a negative full-text finding. See `AUDIT.json` for query-level comparisons.

## Mathematical value — PASS

A one-periodic interval of observation availability is a natural closed time scale for event-based threshold-reset systems. An exact global classification, unique-versus-nonunique invariant phase measures, sharp rational q-grid threshold, formula for physical firing frequency, and irrational arithmetic rate steps distinguish phenomena obscured by the universal projected-recursion statement. The exact physical-time law is useful without requiring a physiological interpretation and is not an arbitrary numerical slice.

## Limitations

No result is asserted for multiple observation windows, variable reset-to-threshold travel time, stochastic clocks, or neuron networks. The orientation of time projection is to the next permitted instant. The output concerns mathematical threshold-reset timing rather than empirically validated neuronal rates. The primary source's general reset formula and prior survivor geometry remain prior contributions.

Self-review: passed. Independent audit: not yet performed.
