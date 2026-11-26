# Independent mathematical audit

## correctness

PASS

In a simple graph the vertices W incident to no selected edge are independent, and every edge inside the complementary red set must be selected (otherwise two distinct selected edges dominate it). A red vertex must have a red neighbor, and if it has a white neighbor it must have precisely one red neighbor. These rules are sufficient and recover W uniquely from the selected set. On degree-two paths they reduce to white spacing at least three, with a red penultimate vertex next to a leaf. With a red hub either all neighbors are red or exactly one is red; the latter neighbor is on the cycle (two orientations) or in one designated arm. With a white hub, both vertices next to each end of the cycle path and each of the first two arm vertices are red, which rules out length-one arms. The cycle word counts are I_(c-3), I_(c-5), and I_(c-7) for the three red-hub endpoint types, with both-white impossible at c=3,4 and one remaining permitted endpoint pattern at c=5. Both-end two-zero forcing gives I_(c-5) for the white hub, including overlapping prefixes at c=3,4. Splitting arm words by their last bit, a final 1 forces its immediately preceding two positions (where present) to zero, including the already-red penultimate. This gives the displayed I formulas, base triples and recurrence. Thus cases are disjoint and exhaustive, and the length-one and length-two formulas follow by substitution for r>=2. Independently enumerated all edge subsets for 93 small heterogeneous or boundary instances, with c=3..7, r=2 or 3, lengths 1..4 and total order at most 12, directly imposing the outside-edge test; all agreed. Examples: c=3 gives 3 and 5 for arms (1,1) and (2,2), and c=5 with arms (1,2) gives 8. The symbolic proof, not the finite check, establishes the unrestricted result.

## originality

PASS

The new content supported by the inspected sources is the four-class product for one cycle with at least two independently sized pendant paths, and the resulting change of growth under single subdivision of all arms. The one-tail count, hub-refined cycle-bouquet product, and generalized series-parallel counting algorithm are genuine overlaps in method or scope, but none supplies this multiarm statement.

## value

PASS

The formula classifies every feasible edge set with arbitrary heterogeneous arm lengths, including when a length-one arm blocks an entire root class. It also proves an at-most-affine versus exponential dependence on the number of arms for every fixed cycle size. This is a structural benchmark beyond evaluation of a single graph and does not imply the general extremal conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
