# Independent mathematical audit

## correctness

PASS

With d_i=x_i XOR x_(i+1), admissibility forbids adjacent zeros of d and the telescoping parity condition forces n−k even. Conversely each independent k-set with that parity reconstructs exactly two complementary indexed words. Flipping x_i toggles d_(i−1),d_i, so only a 01↔10 exchange preserving independence is legal; each slide lifts uniquely from either word. At 0<k<n/2 the gaps between tokens have positive total surplus. Transferring surplus to one gap and cycling a unit of surplus to translate the compressed configuration give a canonical route in O(kn) slides. The displayed closed walk first moves the compressed tokens one step clockwise in reverse order, then another, then moves the foremost token through the wrap to zero. The condition n>2k leaves room for each move, including at n=2k+1. Exactly one traversal of every site-cycle edge flips every indexed bit once and joins the two lifts; this step is necessary because connectivity of the projection alone does not imply connectivity of a two-sheeted graph. At k=0 the two alternating words are frozen. At k=n/2 the two frozen difference patterns each lift twice, and parity requires 4|n. Distinguishing a token and composing its positive gaps counts n/k times binomial(n−k−1,k−1) projected vertices; clockwise slides count n times binomial(n−k−2,k−1) projected edges by requiring the two sites ahead of the moving token and the site directly behind it to be empty. The residual sites form a path, with n=3,k=1 checked directly as a six-cycle in the lift. Doubling and counting the permitted parity sectors give the stated formulas. Independent literal word enumeration, direct legal flips and BFS matched the census at all n=3 through 18; the path routine checked all ordered pairs within components for n≤8 and sampled paths in every interior sector through n=18.

## originality

PASS

The projected token connectivity, saturated frozen token states, and existence of a length-n rotational slide walk are established ingredients; they are not credited as new. The supported distinct result is the parity-filtered binary-word lift, the sheet exchange induced by the slide walk, and the resulting exact census and constructive reachability for indexed binary words. The closest literal-constraint catalogue result changes both the boundary and the move. No inspected source supplied the same lifted graph results or a stronger theorem covering them.

## value

PASS

For the simplest cyclic binary constraint forbidding both constant triples, it is not enough to label difference-token sectors: a word and its complement project to the same placement but are not automatically connected. The lift calculation resolves this obstruction and yields exact component and edge counts, frozen cases and a polynomial-length path without enumerating words. This supplies a reusable benchmark for constrained single-coordinate reconfiguration rather than just re-counting independent sets of a cycle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
