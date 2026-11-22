# Review of the sharp four-circle maximin perimeter finding

## Correctness (C): PASS

The proof uses fourteen feasible mixed sign patterns, eight triangular and six quadrilateral regions, and a one-to-one triangle–quadrilateral edge incidence. Hence the eight triangular perimeters total exactly \(8\pi\), giving the universal upper bound. Equality of all eight triangular perimeters is inverted by spherical polarity and the unit-triple solid-angle identity to four *linear* Gram equations; their solution is precisely the orthogonal disphenoid sign-normal family. The three antipodal quadrilateral pairs have polar rectangles with areas \(4\arctan(bc/a)\), \(4\arctan(ac/b)\), and \(4\arctan(ab/c)\), yielding all necessary and sufficient inequalities. The separate standard-library checker reconstructed 900 nondegenerate arrangements and verified all local formulas within numerical tolerance; only the analytic proof establishes the infinite claim. No degenerate three-concurrent arrangements are included.

## Originality (O): PASS, historically provisional

Bhowmick (2026) treats the smallest **area** of cells; Bezdek–Lángi (2022/24) treat inradius/circumradius, and provide the combinatorics used here. Classical spherical polarity and solid-angle formulas are credited. The simple \(\pi\) upper bound follows from earlier combinatorics and is not presented as the sole novelty. The new contribution is the *complete* optimizer classification, including a two-dimensional equality family and a sharp three-inequality boundary derived from exact quadrilateral perimeters. Searches for equivalent minimum-perimeter theorems, dual formulations, stronger prior coverage and tables found none; historical priority remains subject to unindexed older work.

## Mathematical value (V): PASS

This is a natural sharp extremal invariant of the smallest cell in the first nontrivial nondegenerate four-circle arrangement. Unlike area or covering criteria, the perimeter criterion possesses a continuous two-dimensional optimizer region rather than a rigid regular configuration. The statement completely characterizes when the three quadrilateral orbits cease to be limiting; the explicit geometry supplies a reusable boundary classification, not only an isolated numeric bound. The known easy average bound alone would have been low value, so acceptance rests on the complete non-rigid equality theorem.

## Scientific limitations

Only four circles with no three concurrent and geodesic cell perimeters are treated. The standalone checks are finite floating-point corroboration, not a formal proof. A non-exhaustive literature search cannot certify global historical novelty.

Self-review: passed. Independent audit: not yet performed.
