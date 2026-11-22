# Scientific review

## Correctness — PASS
The finite statement is proved by exhaustive enumeration of every binary word of lengths one through eleven. The proof certificate checks all \(4094\) inputs, independently computes each signature both by prefix-sum differences and by direct window summation, and compares complete integer counter vectors rather than hashed approximations. It finds two and only two moment fibers that subdivide under complete substring-composition observations at length eleven. Their explicit members and the cubic repair are checked. The proof is finite; no extrapolation to longer lengths is asserted.

## Originality — PASS (qualified)
The 2010 ISIT source and its 2014 preprint describe equivalence under the *complete* substring-composition multiset, and an indexed complete-spectrum census similarly enumerates complete-observation fibers. The new distinction compares the quotient by **two length-resolved power sums** against that by complete compositions, isolates its first strict difference at length eleven, and identifies the unique two exceptional moment classes and the minimal window length for a cubic repair. A related 2022 partial-observation paper instead restricts which individual compositions are observed. Searches for length-resolved quadratic moments and their aliases did not identify this assertion. Residual risk: unindexed prior treatment of power-sum compression.

## Mathematical value — PASS
The question is a natural exact sufficiency threshold for an economical summary of substring-composition spectroscopy: replacing a full multiplicity histogram by its first two moment coordinates for each length saves readout coordinates but can merge distinguishable strings. The first failure, its entire set of exceptions, and a single additional low-degree moment that repairs the loss are operationally and mathematically well-defined. The result is not offered as a generic finite table, but as the sharp boundary of a specific compression principle and the lowest-window cubic correction.

## Scope and closest literature
The 2010 full-composition reconstruction construction produces true complete-spectrum collisions already at length eight; these are **not** counterexamples to equality of the two resulting partitions. At length eleven the present four-word exceptional moment fibers split into distinct full-spectrum reversal pairs. The full-composition census through length twenty-three has \(1052\) classes at length eleven, compared with \(1050\) here for the two-moment readout. This does not claim a new full-observation reconstruction theorem. The assessment concerns only binary lengths up to eleven; independent external audit is not claimed.

Self-review: passed. Independent audit: not yet performed.
