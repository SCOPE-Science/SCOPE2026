# Independent mathematical audit

## correctness

PASS

Flipping a vertex with d disagreeing neighbors changes the disagreement count by 4−2d; the doubled accepted-flip rates are 2 for d>2, 1 for d=2 and 0 otherwise. The generator is invariant under vertex symmetries and spin reversal. A separate full-state implementation used bit-mask neighbor intersections and different coordinate-permutation generators to validate the 222 orbit values on all 65,536 labeled states. It found 720,896 directed positive-rate moves and exactly the two monochromatic and eight coordinate half-cube absorbing masks. Reverse reachability from those masks covers every state, ruling out any other closed class; this also proves uniqueness of the finite harmonic solution. The replay checked each harmonic identity with integers scaled by a common denominator, and checked the boundary values against independently constructed absorbing masks. Independent enumeration reproduced all six distance classes, the exact weighted mean and the four reachability witnesses; all states with at most two minority spins have hitting probability zero. This is exhaustive on Q₄, not a claim for other dimensions or other tie rules.

## originality

PASS

The same-dynamics hypercube publication supplies the general no-blinker result and balanced-initial-state statistics, and known periodic-square stripe dynamics supplies close context. The distinct supported claim is the geometry-conditioned six-class exact three-spin law and sharp minority-seed boundary, not the general absence of blinkers, the stripe mechanism, or absorbing-chain algebra.

## value

PASS

Q₄ is a natural degree-four cube where a minority configuration must grow to an eight-site half-cube to freeze. The smallest successful seeds include dispersed triples but not a length-two path; four geometric classes have distinct exact positive basin probabilities. This supplies a finite benchmark for geometry-sensitive nucleation that neither static frozen-state counts nor balanced-initial simulations provide. The standard Markov-chain method is not itself the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
