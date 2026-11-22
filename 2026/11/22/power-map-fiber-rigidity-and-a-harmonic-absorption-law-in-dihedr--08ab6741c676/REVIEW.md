# Scientific review

## Correctness — PASS

The proof uses the canonical dihedral alternating-word normal form and the right-descent rule, derives the exact power length, then counts nonabsorbed even and odd source lengths separately. Distinct initial letters and output parity enforce uniqueness away from the longest-element fiber. The root congruence cases, absorption CDF, harmonic mean and limit law follow with all parameter boundaries explicit. Independent finite computations in `verify_power_maps.py` verify all powers and fibers for every \(3\le m\le80\) and a range of exponents, including an independent multiplication algorithm; these experiments corroborate rather than replace the proof. The claim is about set power maps, not monoid homomorphisms.

## Originality — PASS, subject to historical priority

The published 2010 \(\mathcal J\)-trivial monoid study proves the presentation and Coxeter indexing; the 2011 dissertation states the qualitative formula \(x^\omega=w^+_{J(x)}\) but does not derive the complete quantitative dihedral power-map fiber or first-absorption laws in its inspected sections. The dissertation's diagram-demipotent nilpotence degree concerns different elements in the monoid algebra. The closest relevant published result on \(0\)-Hecke idempotents treats commuting-pair support rather than nonidempotent powers. Another published record proves the identical limiting heavy-tail distribution in a *different* semigroup, the consecutive-diagonal rook inverse monoid; this law itself is credited as precedented outside the dihedral family. Explicit root-fiber rigidity, mod-four counts and the dihedral realization remain distinguishable claims. Searches cannot establish global novelty; an unlocated quantitative dihedral treatment is a residual priority risk.

## Value — PASS

The saturation exponent is a canonical measure of aperiodic power dynamics. A full power-fiber census is more informative than eventual idempotence, since it detects how the \(2m\) elements progressively collapse to four idempotents. The mod-four square-root population is an exact arithmetic feature, and the heavy-tailed limit with diverging mean gives a motivated asymptotic for a standard rank-two Coxeter family. This is a self-contained classification and natural invariant, not a generic relabeling of the rook-monoid result. It is limited in breadth and relies on elementary rank-two combinatorics; no higher-rank conclusion is asserted.

Self-review: passed. Independent audit: not yet performed.
