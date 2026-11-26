# Independent mathematical audit

## correctness

PASS

Midpoint distance is the specified nearest-endpoint distance plus 1/2. In a collision the multiplicities allow a bijective landmark matching, and each matched step must be the common translation or common reflection between midpoints. Identity matching is impossible since the nonidentity translation has no fixed point and a reflection has at most two. In a transposition the third point is reflection-fixed; if a swapped step uses reflection, its partner is the reflected point and the triple has two equal gaps. Otherwise translation swaps the pair and has displacement n/2; the fixed-point congruence for the third point is solvable exactly when n/2 is odd. A three-cycle has at most one reflection step since two adjacent reflection steps undo each other. The remaining two consecutive translation steps give an arithmetic progression; reversing its orientation if needed, use a positive step less than n/2, so two clockwise gaps coincide. Both obstructions realize a collision, by the triple's preserving reflection or by the half-turn match for the antipodes and midpoint reflection for the third point. A gap n/2 is equivalent to having an antipodal pair. No one- or two-element set resolves because a reflection preserves it and moves an edge; gaps (1,2,n-3) qualify for every n≥7. The marked-start ordered-composition count subtracts the three equal-gap events with the triple-intersection correction, then 3(n/2-1) triples in the odd half-order case; distinct gaps make the action free. Independent exhaustive check /workspace/evidence/cycle.py 7 30 (output cycle-7-30.txt) tested every triple, its criterion and its actual dihedral orbit when qualifying. This bounded replay is not the all-n proof.

## originality

PASS

Scoped to the all-bases criterion, the parity-dependent antipodal obstruction and resulting counts, not discovery of the scalar edge-multiset dimension or of a particular basis. No independently covering equivalent statement was established in the inspected material.

## value

PASS

This is a structural equality-case refinement for a standard resolving invariant. The half-turn obstruction separates asymmetric triples that otherwise appear equivalent by automorphism criteria, and its mod-four behavior yields an exact census, not merely additional examples of the known minimum size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
