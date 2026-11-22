# Self-review

## Correctness — PASS

The finite object, pin constraint, strict threshold-two update, sample space and first-entry convention are explicit. The coordinatewise monotonicity lemma reduces the universal-consensus question to the all-zero-free seed state, with no improper assumption that unpinned active sites remain active. The four distinct three-edge patterns on five labels exhaust all possible triples, and the explicit star/nonstar seed trajectories establish exactly twenty universally forcing triples and a sharp three-update star bound. Every pair extends to a nonforcing triple, proving minimality. The exact, distinct majority-basin fractions and entry times are certified by two independently coded full integer enumerations of all 120 pin sets times 128 compatible starts. The two-pin checks cover 45 pairs times 256 starts. Every trajectory is followed to its first repeated state, not cut off at a guessed iteration count. Source and output files are supplied for replay.

Residual scientific risk: there is no formally machine-checked proof; both checkers rely on correct implementation of the stated ten-vertex graph, although they construct adjacency separately and the forcing theorem is proved directly by hand. No infinite-graph claim is made.

## Originality — PASS, with stated historical uncertainty

The nearest full inspected Petersen result, *A four-step Petersen majority projection and the Desargues double-cover basin spectrum*, treats the unpinned map. Its 124 recurrent Petersen symbols and basin fibers cannot be substituted for the present frozen-vertex map, which changes each affected coordinate and whose four pin-layout basin distributions are not supplied there. The 2012 strict-majority dynamic-monopoly paper studies irreversible activation and general upper/lower bounds, not synchronous opinions that can turn off or the four-class exact census. The 2014 general synchronous-majority paper supplies general period-at-most-two theory, not the finite pinned Petersen computation. A 2026 odd-graph bootstrap paper again uses irreversible two-neighbor activation. Direct named-claim and equivalent-terminology searches of the public mathematical record found no dominating or identical statement. Different titles and a failed search alone are not a proof of priority; a previously tabulated computation or unseen general pinned-majority theorem remains possible.

## Value — PASS

This is a natural small, vertex-transitive, nontrivial benchmark for *where* permanent opinion interventions should be placed, not an arbitrary selected subset: the smallest budget that guarantees unanimous consensus is proved to be three, but only one of the four geometry types actually guarantees it, with a factor-of-twenty exact placement census and full basin probabilities for the other types. The triangle and wedge-plus-disjoint placements still support genuine oscillatory attractors despite the same number of fixed opinion leaders. The contrast offers structural guidance for stubborn-agent placement and an exact stringent test case for majority-dynamics algorithms. No general-graph theorem is implied.

## Verification and independence

The finite results were reproduced by `check_bitmask.py` and `check_tuples.py`, each using the Python standard library and disjoint implementations, with their corresponding JSON outputs attached. External mathematical validation has not been performed; scope and historical-priority limitations are recorded in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
