# Scientific assessment

## Correctness — PASS

The identifying property is exactly equivalent to pairwise nonzero, distinct intersections of a candidate sensor set with each of the 27 closed radius-one neighborhoods. The supplied complete Python and C++ programs independently enumerate all eight- and nine-sensor sets; both find zero eight-sensor codes and exactly 4,366 nine-sensor codes. Monotonicity excludes smaller codes. Reversal fixes nine vertices and pairs the remaining eighteen, giving a complete partition into eighteen orbits. Exhausting their 262,144 unions establishes an invariant minimum of eleven and exactly 117 attaining placements. The full natural-group orbit counts are reproduced and checked by a supplied representative list. Both explicit witness codes validate under the same predicate.

## Originality — PASS, with historical-priority qualification

Horan, Adachi and Bak (arXiv:1504.08011, Figures 8–9) report the ternary three-letter minimum sensor size nine; this size itself is established prior art. Horan (arXiv:1508.00403) establishes general existence, not the enumerated equality populations or symmetry-constrained minimum. The main new claim instead concerns 4,366 equality cases, a sharp cost of two sensors for reversal invariance, the 117 symmetric equality cases, and the two full natural-group orbit spectra. Searches across published mathematical research records, relevant primary literature, and relevant existing mathematical claims did not identify stronger statements implying these exact quantities. Historical coverage outside accessible indexed materials remains possible.

## Mathematical value — PASS

Undirected de Bruijn networks are natural finite models for identifying sensor locations. Reversal is a structural automorphism expressing orientation-independent installation. Requiring that symmetry raises a previously known nine-sensor optimum by two sensors, a 22.2% relative increase, rather than changing a cosmetic property of an optimizer. The exact equality and symmetry-orbit censuses quantify deployment flexibility and classify all optimal configurations in a natural first nonbinary length-three case. The result is finite and does not purport to generalize to larger parameters.

## Scope and limitations

The assertions are restricted to ternary words of length three, closed radius one, simple undirected shift adjacency, and the explicit 12-element natural group. The historical minimum nine is not presented as newly discovered; it is independently reconfirmed only to validate the equality census. The calculation is reproducible from supplied source files, but no independent expert audit was performed.

Self-review: passed. Independent audit: not yet performed.
