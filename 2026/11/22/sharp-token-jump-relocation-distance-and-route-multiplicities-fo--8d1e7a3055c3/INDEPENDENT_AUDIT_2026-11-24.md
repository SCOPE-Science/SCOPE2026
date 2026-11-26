# Independent mathematical audit

## correctness

PASS

Three disjoint row paths require one removal per row in any minimum cut; removing a column realizes size three. A gap of at least two permits a vertical bypass at an intermediate column; with adjacent cut positions differing by at most one, j minus the deleted column of its row cannot go from negative to positive without a zero vertex. Thus the triples and the single-coordinate jump representation are exact, including L=0. Counting over middle coordinates gives 9L-1 vertices and 18L-10 outer-coordinate edges. The middle-coordinate edges contribute 3(L-1)+2 for coincident outer positions and 2L for adjacent outer positions; larger gaps contribute none. For L>0 first and last jumps are unit and internal jumps have absolute length at most two, so net gain 3L forces at least ceil(3L/2)+1 moves. At equality all moves go forward; parity forces two units on the same coordinate for even L, and exactly one unit per coordinate for odd L. Double outer jumps require moving from b-1 to b+1, and a double middle jump requires both outers at b+1. For even L an outer first move leaves no available double; a middle start and end therefore bound alternating ordered pairs of outer doubles and single middle doubles, with two choices per pair. For odd L, an outer start followed by a middle unit either immediately equalizes all three (before the goal) or leaves the last outer unit unusable after its double. So an outer start needs the other outer unit next; then the middle unit cannot be used until the final equalization, and intermediate layers have two outer orders. A middle start leaves only the outer units available: spending one before the last layer ties that coordinate with the middle and stops the next double middle jump, because the tied outer cannot then double and its unit is spent. Thus both outer units are final, with two orders. Each of the two types contributes twice 2^((L-1)/2); L=1 has six one-move-per-row orders and L=0 only the empty route. Independent replay: `python -B /workspace/independent_replay.py 3` generated actual graph cuts and BFS counts for L=0..7, including (62,150,12,32) at L=7. The supplied code and saved checks were read, not run; neither finite diagnostic replaces the all-L argument.

## originality

PASS

The supported distinction is the exact extreme-cut distance and complete shortest state-sequence count in this three-row, full-boundary-attached token-jump graph. Min-separator reconfiguration and the underlying Lipschitz state region are not claimed as new. Exact prior matches were not established in the inspected evidence; inaccessible sections and similarly scoped catalogue results remain residual risks.

## value

PASS

The two extreme cuts are canonical endpoints of a natural fixed-width reconfiguration problem. A fully explicit cost and exact multiplicity distinguish jump geometry from unit-step motion and expose an odd/even change in the mechanism of the optima. The exponential counts come from a complete optimal-route classification, not a tiny-instance speed gain or the recomputation of the unit-step table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
